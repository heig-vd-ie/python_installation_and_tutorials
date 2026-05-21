import pandapower as pp
import numpy as np


def create_5bus_network():
    net = pp.create_empty_network(sn_mva=100)

    # Create buses
    b1 = pp.create_bus(net, vn_kv=400, name="Bus 1", max_vm_pu=1.1, min_vm_pu=0.9)
    b2 = pp.create_bus(net, vn_kv=400, name="Bus 2", max_vm_pu=1.1, min_vm_pu=0.9)
    b3 = pp.create_bus(net, vn_kv=400, name="Bus 3", max_vm_pu=1.1, min_vm_pu=0.9)
    b4 = pp.create_bus(net, vn_kv=400, name="Bus 4", max_vm_pu=1.1, min_vm_pu=0.9)
    b5 = pp.create_bus(net, vn_kv=20,  name="Bus 5", max_vm_pu=1.1, min_vm_pu=0.9)

    # Slack and generators
    pp.create_ext_grid(net, b1, vm_pu=1.00, name="Slack Bus")

    pp.create_gen(
        net, b2,
        p_mw=150,
        vm_pu=1.05,
        min_p_mw=50.0,
        max_p_mw=250.0,
        min_q_mvar=-200,
        max_q_mvar=200,
        name="PV Generator Bus 2"
    )

    pp.create_gen(
        net, b5,
        p_mw=100,
        vm_pu=1.00,
        min_p_mw=20.0,
        max_p_mw=150.0,
        min_q_mvar=-100,
        max_q_mvar=100,
        name="PV Generator Bus 5"
    )

    # Loads
    pp.create_load(net, b2, p_mw=100, q_mvar=20, name="Load Bus 2")
    pp.create_load(net, b3, p_mw=200, q_mvar=80, name="Load Bus 3")

    # Lines
    line_data = [
        ("A", b1, b2, 0.02, 0.20, 0.8),
        ("B", b2, b3, 0.02, 0.40, 0.8),
        ("C", b1, b3, 0.02, 0.40, 0.4),
        ("D", b3, b4, 0.04, 0.40, 0.4),
        ("E", b2, b4, 0.04, 0.40, 0.4),
    ]

    f_hz = 50
    length_km = 1.0

    for name, from_bus, to_bus, r_pu, x_pu, b_total_pu in line_data:
        vn_kv = net.bus.at[from_bus, "vn_kv"]
        sn_mva = net.sn_mva

        z_base_ohm = vn_kv**2 / sn_mva
        y_base = 1 / z_base_ohm

        r_ohm = r_pu * z_base_ohm
        x_ohm = x_pu * z_base_ohm

        b_total = b_total_pu * y_base
        c_nf = b_total / (2 * np.pi * f_hz) * 1e9

        pp.create_line_from_parameters(
            net,
            from_bus=from_bus,
            to_bus=to_bus,
            length_km=length_km,
            r_ohm_per_km=r_ohm / length_km,
            x_ohm_per_km=x_ohm / length_km,
            c_nf_per_km=c_nf / length_km,
            max_i_ka=1.0,
            name=f"Line {name}"
        )

    # Transformer
    pp.create_transformer_from_parameters(
        net,
        hv_bus=b4,
        lv_bus=b5,
        sn_mva=200,
        vn_hv_kv=400,
        vn_lv_kv=20,
        vk_percent=10,
        vkr_percent=0,
        pfe_kw=0,
        i0_percent=0,
        name="T1"
    )

    return net