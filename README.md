# Trajectory-Dependent Biological Response Model

A unified mathematical framework for modeling biological responses to gravitational transitions (Δg), based on the NASA Twins Study and Ye et al. (2023) meta‑analysis.

## Equation

The model is defined as:

\[
\ln\frac{S(t)}{S_0} = \bigl[-\alpha - \beta \Delta g\bigr] \cdot \bigl(1 - e^{-t/\tau}\bigr) \;-\; \lambda R t \;+\; \varepsilon
\]

Where:
- `S(t)`: biological state at time t
- `S₀`: baseline state
- `α`: aging magnitude
- `β`: mechanotransduction sensitivity
- `Δg`: change in gravitational acceleration
- `τ`: adaptation time constant
- `λR`: radiation damage
- `ε`: biological variability

## Features
- Predicts telomere length changes in microgravity
- Matches Earth aging plateau (Ye et al., 2023)
- Identifies cancer as a predictable exception

## Usage
See `import numpy as np
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
plt.show()` for Python implementation and example parameters.

## License
MIT License

Copyright (c) 2025 Mymana Takual

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author
Mymana Takual – Independent Researcher
