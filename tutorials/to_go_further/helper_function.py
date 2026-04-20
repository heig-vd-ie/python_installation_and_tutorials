import numpy as np
import pandas as pd

def compute_admittance_matrix(line_pu: pd.DataFrame) -> np.ndarray:
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

    return Y_bus

def compute_power_injections(Ybus: np.ndarray, Vm: np.ndarray, Va_deg: np.ndarray):
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