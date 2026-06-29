import numpy as np

# ------------------------------------------------------------------
# Physical Constants
# ------------------------------------------------------------------

h = 6.62607015e-34      # Planck constant
c = 2.99792458e8        # Speed of light

# ------------------------------------------------------------------

class CameraSensor:
    """
    Simple CMOS camera model.
    """

    def __init__(self,
                 quantum_efficiency=0.80,
                 pixel_size=5.5e-6,
                 resolution=(2048, 2048),
                 exposure_time=100e-6,
                 read_noise=3.0,
                 full_well=30000):

        self.QE = quantum_efficiency
        self.pixel = pixel_size
        self.resolution = resolution
        self.exposure = exposure_time
        self.read_noise = read_noise
        self.full_well = full_well

    @property
    def pixel_area(self):
        return self.pixel**2

    @staticmethod
    def photon_energy(wavelength):
        return h * c / wavelength

    def photons_from_power(self, optical_power, wavelength=900e-9):
        E = self.photon_energy(wavelength)
        return optical_power * self.exposure / E

    def electrons(self, photons):
        actual_electrons = photons * self.QE
        # Cap the electrons at the physical full well capacity
        return np.minimum(actual_electrons, self.full_well)

    def shot_noise(self, electrons):
        return np.sqrt(np.maximum(electrons, 0))

    def total_noise(self, electrons):
        return np.sqrt(
            self.shot_noise(electrons)**2 +
            self.read_noise**2
        )

    def snr(self, electrons):
        return electrons / self.total_noise(electrons)

    def saturation_fraction(self, electrons):
        return electrons / self.full_well
    
# ------------------------------------------------------------------

# class CameraSensor:
#     def __init__(self,
#                  exposure_time=0.01,
#                  gain=2.0,
#                  bit_depth=12,
#                  full_well_capacity=5e4,
#                  read_noise_e=5.0):

#         self.exposure_time = exposure_time
#         self.gain = gain
#         self.bit_depth = bit_depth
#         self.adc_max = 2**bit_depth - 1
#         self.full_well_capacity = full_well_capacity
#         self.read_noise_e = read_noise_e

#     def optical_power_to_adu(self, optical_power):
#         # signal → electrons
#         signal_e = optical_power * self.exposure_time * self.gain

#         # shot noise
#         shot_noise = np.sqrt(np.maximum(signal_e, 1e-12))

#         # read noise
#         read_noise = np.random.normal(0, self.read_noise_e, size=len(signal_e))

#         # total electrons
#         signal_e = signal_e + read_noise

#         # saturation
#         signal_e = np.clip(signal_e, 0, self.full_well_capacity)

#         # ADC conversion
#         adu = (signal_e / self.full_well_capacity) * self.adc_max
#         adu_q = np.round(adu)

#         return adu_q


# ------------------------------------------------------------------
# Future Sensor Models
# ------------------------------------------------------------------
# InGaAsSensor
# EMCCD
# sCMOS