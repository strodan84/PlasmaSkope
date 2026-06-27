# physics/blackbody_emission.py

import numpy as np

sigma = 5.670374419e-8  # Stefan-Boltzmann constant (W/m^2/K^4)

def blackbody_power_density(T):
    """
    Compute radiated power density from a surface at temperature T (K).

    Parameters
    ----------
    T : float or ndarray
        Surface temperature in Kelvin.

    Returns
    -------
    float or ndarray
        Radiated power per unit area (W/m^2)
    """
    return sigma * T**4


def photon_flux_estimate(T, wavelength=550e-9):
    """
    Rough estimate of photon flux at a given wavelength.

    This is a simplified diagnostic model:
    assumes peak emission near visible band.

    Parameters
    ----------
    T : float
        Temperature in Kelvin
    wavelength : float
        Wavelength in meters

    Returns
    -------
    float
        Relative photon flux (arbitrary units)
    """
    k_B = 1.380649e-23
    h = 6.62607015e-34
    c = 3e8

    energy = h * c / wavelength
    thermal_factor = np.exp(-energy / (k_B * T))

    return thermal_factor * blackbody_power_density(T)