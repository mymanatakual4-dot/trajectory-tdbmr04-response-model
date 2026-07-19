import numpy as np
import matplotlib.pyplot as plt

def biological_response(t, S0=1.0, alpha=1.345, beta=0.145, delta_g=-9.8,
                        tau=39.2, lam=0.01, R=0.001, eps=0.0):
    """
    Compute the biological state S(t) based on the trajectory-dependent model.

    Parameters:
    - t: time (years)
    - S0: baseline state
    - alpha: aging magnitude
    - beta: mechanotransduction sensitivity
    - delta_g: change in gravitational acceleration (m/s²)
    - tau: adaptation time constant (years)
    - lam: radiation sensitivity constant
    - R: radiation dose rate
    - eps: noise term

    Returns:
    - S(t): relative biological state
    """
    driver = -alpha - beta * delta_g
    adaptation = 1 - np.exp(-t / tau)
    radiation = -lam * R * t
    noise = eps

    ln_ratio = driver * adaptation + radiation + noise
    return S0 * np.exp(ln_ratio)

# Example: Telomere length over 10 years in microgravity
t = np.linspace(0, 10, 100)
S = biological_response(t)

plt.plot(t, S)
plt.xlabel('Time (years)')
plt.ylabel('Relative Telomere Length')
plt.title('Model Prediction: Telomere Lengthening in Microgravity')
plt.grid(True)
plt.show()
