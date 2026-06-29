'''
This model aims to do three things:
    1. Convert incident heat flux → surface temperature evolution
    2. Include a simple energy balance model
    3. Provide a bridge to what the camera would actually observe
'''

import numpy as np

sigma = 5.670374419e-8  # Stefan-Boltzmann constant (W/m^2/K^4)

materials = {

    "Tungsten": {
        "rho":19300,
        "Cp":134,
        "emissivity":0.30,
        "k":174
    },

    "Graphite":{
        "rho":1800,
        "Cp":710,
        "emissivity":0.80,
        "k":120
    },

    "Molybdenum":{
        "rho":10200,
        "Cp":250,
        "emissivity":0.18,
        "k":138
    }

}

# Set which material PFC is made of:
material = materials["Graphite"]

def surface_energy_balance(
    q_in,
    T0,                             
    t,
    rho=material["rho"],                # tdensity (kg/m^3)
    Cp=material["Cp"],                  # J/(kg K)
    thickness=0.005,                    # 5 mm tile
    emissivity=material["emissivity"],
    k=material["k"],                    # Thermal conductivity of tungsten (W/m/K)
    T_bulk=500                          # Bulk substrate temperature (K)
):
    
    """
    Simple 1D lumped thermal model for a plasma-facing component.

    Governing equation:
        rho * Cp * dT/dt = q_in - q_rad - q_cond

    where:
        q_rad = emissivity * sigma * T^4    [radiative cooling]
        q_cond = h * (T - T_bulk)           [heat conduction into bulk material]

    Parameters
    ----------
    q_in : float or ndarray
        incident heat flux (W/m^2), assumed constant or time-dependent
    T0 : float
        initial temperature (K)
    t : ndarray
        time array (s)
    rho : float
        material density (kg/m^3)
    Cp : float
        heat capacity (J/kg/K)
    thickness : float
        effective thickness of heated layer (m)
    emissivity : float
        surface emissivity

    Returns
    -------
    T : ndarray
        surface temperature evolution (K)
    """

    h = 0.8 * k / thickness # Effective thermal conductance (W/m²/K)
    dt = np.diff(t)
    T = np.zeros_like(t)
    q_rad_arr = np.zeros_like(t)
    q_cond_arr = np.zeros_like(t)
    areal_heat_capacity = rho * Cp * thickness  # J/m^2/K
    T[0] = T0

    for i in range(1, len(t)):

        # Allow scalar or time-dependent heat flux
        q = q_in if np.isscalar(q_in) else q_in[i-1]

        # Radiative cooling
        q_rad = emissivity * sigma * T[i-1]**4

        # Conductive heat removal into bulk
        q_cond = h * (T[i-1] - T_bulk)

        q_rad_arr[i] = q_rad
        q_cond_arr[i] = q_cond


        # Net heat flux
        q_net = q - q_rad - q_cond

        # Temperature derivative
        dTdt = q_net / areal_heat_capacity

        # Euler integration
        T[i] = T[i-1] + dTdt * dt[i-1]

        # Prevent nonphysical temperatures
        if T[i] < 0:
            T[i] = 0

    # return T, q_rad_arr, q_cond_arr
    return {
    "T": T,
    "q_rad": q_rad_arr,
    "q_cond": q_cond_arr
}
        
        
def steady_state_temperature(q_in, emissivity=0.3):
    """
    Solve approximate steady-state temperature:
        q_in = emissivity * sigma * T^4
    """

    return (q_in / (emissivity * sigma)) ** 0.25


# def demo_heat_pulse():
#     """
#     Generate a simple fusion-relevant heat pulse scenario.

#     Example:
#     - plasma shot lasting ~1 second
#     - Gaussian-like heat flux profile

    
#     """

#     t = np.linspace(0, 2.0, 1000) 

#     q_peak = 5e6  # 5 MW/m^2 (typical divertor scale)
#     q_in = q_peak * np.exp(-((t - 0.5)**2) / 0.02)

#     T0 = 500  # initial wall temperature (K)

#     results = surface_energy_balance(q_in, T0, t)

#     return {
#         "t": t,
#         "q_in": q_in,
#         "T": results["T"],
#         "q_rad": results["q_rad"],
#         "q_cond": results["q_cond"]
#     }


def demo_heat_pulse(
    duration=5.0,
    dt=0.005,
    q_peak=5e6,
    pulse_center=None,
    pulse_width=0.5
):
    """
    Generate a Gaussian plasma heat pulse.
    NSTX-U: plasma pulses are typically 1-5 seconds (historically around 1-2 s, with longer pulses as operating goals increase).

    Parameters
    ----------
    duration : float
        Total simulation time (s)
    dt : float
        Time step (s)
    q_peak : float
        Peak heat flux (W/m²)
    pulse_center : float
        Center of Gaussian pulse (s)
    pulse_width : float
        Standard deviation of pulse (s)
    """

    if pulse_center is None:
        pulse_center = duration / 2

    t = np.arange(0, duration + dt, dt)

    q_in = q_peak * np.exp(
        -((t - pulse_center) ** 2) / (2 * pulse_width**2)
    )

    T0 = 500

    results = surface_energy_balance(q_in, T0, t)

    return {
        "t": t,
        "q_in": q_in,
        "T": results["T"],
        "q_rad": results["q_rad"],
        "q_cond": results["q_cond"],
    }