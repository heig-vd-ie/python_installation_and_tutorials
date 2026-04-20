import numpy as np
import pandas as pd

def compute_admittance_matrix(line_pu: pd.DataFrame) -> np.ndarray:
    """
    Compute Ybus from line data in per unit.

    we should have the following columns in line_pu:
    - from_bus
    - to_bus
    - r_pu
    - x_pu
    - b_pu  
    """

    # list of bus numbers
    bus_ids = sorted(pd.unique(line_pu[['from_bus', 'to_bus']].values.ravel()))
    n_bus = len(bus_ids)

    # map real bus numbers -> matrix indices
    bus_map = {bus_id: idx for idx, bus_id in enumerate(bus_ids)}

    # initialize Ybus
    Y_bus = np.zeros((n_bus, n_bus), dtype=np.complex128)

    # Off-diagonal elements
    for _, row in line_pu.iterrows():
        i = bus_map[row["from_bus"]]
        j = bus_map[row["to_bus"]]

        r = row["r_pu"]
        x = row["x_pu"]
        b = row["b_pu"]

        y_series = 1 / complex(r, x)
        y_shunt_half = 1j * b / 2
        
        # Diagonal elements
        Y_bus[i, i] += y_series + y_shunt_half
        Y_bus[j, j] += y_series + y_shunt_half
        
        # Off-diagonal elements
        Y_bus[i, j] -= y_series
        Y_bus[j, i] -= y_series


    return Y_bus

def compute_power_injections(Ybus: np.ndarray, Vm: np.ndarray, Va_deg: np.ndarray):
    """
    Compute bus active/reactive injections in pu:
        P_i = sum_h Ui Uh [ Gih cos(theta_i-theta_h) + Bih sin(theta_i-theta_h) ]
        Q_i = sum_h Ui Uh [ Gih sin(theta_i-theta_h) - Bih cos(theta_i-theta_h) ]
    """
    n = len(Vm)
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