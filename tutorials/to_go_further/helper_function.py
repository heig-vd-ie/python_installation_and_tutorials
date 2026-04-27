import numpy as np
import pandas as pd

def compute_admittance_matrix(line_pu: pd.DataFrame):
    bus_ids = sorted(pd.unique(line_pu[["from_bus", "to_bus"]].values.ravel()))
    n_bus = len(bus_ids)
    bus_map = {bus_id: idx for idx, bus_id in enumerate(bus_ids)}

    Y_bus = np.zeros((n_bus, n_bus), dtype=np.complex128)

    for _, row in line_pu.iterrows():
        i = bus_map[row["from_bus"]]
        j = bus_map[row["to_bus"]]

        r = row["r_pu"]
        x = row["x_pu"]
        b = row["b_pu"]

        y_series = 1 / complex(r, x)
        y_shunt_half = 1j * b / 2

        Y_bus[i, i] += y_series + y_shunt_half
        Y_bus[j, j] += y_series + y_shunt_half
        Y_bus[i, j] -= y_series
        Y_bus[j, i] -= y_series

    return Y_bus, bus_map

def compute_power_injections(Ybus: np.ndarray, Vm: np.ndarray, Va_deg: np.ndarray):
    n = len(Vm) # Vm is the voltage magnitude vector, so its length gives the number of buses
    Va_rad = np.radians(Va_deg)

    G = Ybus.real
    B = Ybus.imag

    P = np.zeros(n)
    Q = np.zeros(n)

    for i in range(n):
        for h in range(n):
            dth = Va_rad[i] - Va_rad[h]
            P[i] += Vm[i] * Vm[h] * (
                G[i, h] * np.cos(dth) + B[i, h] * np.sin(dth)
            )
            Q[i] += Vm[i] * Vm[h] * (
                G[i, h] * np.sin(dth) - B[i, h] * np.cos(dth)
            )

    return P, Q

def build_jacobian(Ybus, Vm, Va_deg, slack_bus, pq_buses):
    Va = np.radians(Va_deg)
    G = Ybus.real
    B = Ybus.imag
    n = len(Vm) 
    
    P, Q = compute_power_injections(Ybus, Vm, Va_deg)
    angle_buses = [i for i in range(n) if i != slack_bus]
    
    n_theta = len(angle_buses)
    n_v = len(pq_buses)
    
    J11 = np.zeros((n_theta, n_theta), dtype=float)
    J12 = np.zeros((n_theta, n_v), dtype=float)
    J21 = np.zeros((n_v, n_theta), dtype=float)
    J22 = np.zeros((n_v, n_v), dtype=float)
    
    # compute J11
    for r, i in enumerate(angle_buses):
        for c, h in enumerate(angle_buses):
            if i == h:
                # diagonal term
                J11[r, c] = -Q[i] - B[i, i] * Vm[i]**2
            else:
                # off-diagonal term
                dth = Va[i] - Va[h]
                J11[r, c] = Vm[i] * Vm[h] * (
                    G[i, h] * np.sin(dth) - B[i, h] * np.cos(dth)
                )
    # compute J12
    for r, i in enumerate(angle_buses):
        for c, h in enumerate(pq_buses):
            if i == h:
                # diagonal term
                J12[r, c] = P[i] / Vm[i] + G[i, i] * Vm[i]
            else:
                # off-diagonal term
                dth = Va[i] - Va[h]
                J12[r, c] = Vm[i] * (
                    G[i, h] * np.cos(dth) + B[i, h] * np.sin(dth)
                )
    # compute J21
    for r, i in enumerate(pq_buses):
        for c, h in enumerate(angle_buses):
            if i == h:
                # diagonal term
                J21[r, c] = P[i] - G[i, i] * Vm[i]**2
            else:
                # off-diagonal term
                dth = Va[i] - Va[h]
                J21[r, c] = -Vm[i] * Vm[h] * (
                    G[i, h] * np.cos(dth) + B[i, h] * np.sin(dth)
                )
    # compute J22
    for r, i in enumerate(pq_buses):
        for c, h in enumerate(pq_buses):
            if i == h:
                # diagonal term
                J22[r, c] = Q[i] / Vm[i] - B[i, i] * Vm[i]
            else:
                # off-diagonal term
                dth = Va[i] - Va[h]
                J22[r, c] = Vm[i] * (
                    G[i, h] * np.sin(dth) - B[i, h] * np.cos(dth)
                )       
    # combine into full Jacobian
    J = np.block([
        [J11, J12],
        [J21, J22]
    ])

    return J, angle_buses, pq_buses

def power_mismatch(Ybus, Vm, Va_deg, P_spec, Q_spec, slack_bus, pq_buses):
    P_calc, Q_calc = compute_power_injections(Ybus, Vm, Va_deg)
    n = len(Vm)
    angle_buses = [i for i in range(n) if i != slack_bus]
    dP = np.array([P_spec[i] - P_calc[i] for i in angle_buses])
    dQ = np.array([Q_spec[i] - Q_calc[i] for i in pq_buses])
    mismatch = np.concatenate([dP, dQ])
    return mismatch

def newton_raphson_power_flow(Ybus, P_spec, Q_spec, slack_bus, pv_buses, pq_buses,
                              Vm_init, Va_init_deg, tol=1e-8, max_iter=20):
    
    Vm = Vm_init.astype(float).copy()
    Va_deg = Va_init_deg.astype(float).copy()
    
    n = len(Vm)
    angle_buses = [i for i in range(n) if i != slack_bus]
    
    for iteration in range(max_iter):
        mismatch = power_mismatch(Ybus=Ybus, Vm=Vm, Va_deg=Va_deg, P_spec=P_spec, Q_spec=Q_spec, slack_bus=slack_bus, pq_buses=pq_buses)
        max_mismatch = np.max(np.abs(mismatch))
        print(f"Iteration {iteration+1}: max mismatch = {max_mismatch:.2e}")
        
        if max_mismatch < tol:
            print("Convergence achieved!")
            return Vm, Va_deg, iteration
        
        J, angle_buses, pq_buses = build_jacobian(Ybus=Ybus, Vm=Vm, Va_deg=Va_deg, slack_bus=slack_bus, pq_buses=pq_buses)
        
        # Solve for updates
        delta = np.linalg.solve(J, mismatch)
        
        n_theta = len(angle_buses)
        dtheta = delta[:n_theta]
        dV = delta[n_theta:]
        
        # Update voltage angles and magnitudes
        for idx, bus in enumerate(angle_buses):
            Va_deg[bus] += dtheta[idx] * 180 / np.pi  # convert radians to degrees
        for idx, bus in enumerate(pq_buses):
            Vm[bus] += dV[idx]
            
    raise RuntimeError("Newton-Raphson did not converge within max_iter")