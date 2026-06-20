"""
parameter_estimation.py
Module 11 — The Integrated Digital Twin

Fits a twin model parameter (friction) to a measured step response using
least-squares, shrinking the healthy residual so faults stand out.

Run:
    python parameter_estimation.py
"""

import numpy as np

try:
    from scipy.optimize import curve_fit
    HAVE_SCIPY = True
except ImportError:
    HAVE_SCIPY = False


def twin_step(t, friction):
    """Twin's step-response model, parameterized by friction."""
    tau = 0.5 + friction * 0.1
    return 150 * (1 - np.exp(-t / tau))


def fit_friction(t, measured, guess=5.0):
    if HAVE_SCIPY:
        popt, _ = curve_fit(twin_step, t, measured, p0=[guess])
        return popt[0]
    # simple grid search fallback
    best, best_err = guess, 1e18
    for f in np.linspace(1, 20, 200):
        err = np.mean((measured - twin_step(t, f)) ** 2)
        if err < best_err:
            best, best_err = f, err
    return best


if __name__ == "__main__":
    print("=" * 56)
    print("THE TWIN FITS ITSELF (parameter estimation)")
    print("=" * 56)
    t = np.linspace(0, 4, 50)
    rng = np.random.RandomState(0)
    true_friction = 8.0
    measured = twin_step(t, true_friction) + rng.normal(0, 0.5, len(t))

    guess = 5.0
    fitted = fit_friction(t, measured, guess)

    resid_guess = np.sqrt(np.mean((measured - twin_step(t, guess)) ** 2))
    resid_fit = np.sqrt(np.mean((measured - twin_step(t, fitted)) ** 2))

    print(f"\n  friction guess: {guess}, fitted: {fitted:.1f} (true {true_friction})")
    print(f"  healthy residual before fit: {resid_guess:.2f} mm")
    print(f"  healthy residual after fit:  {resid_fit:.2f} mm")
    print(f"\n  -> fitting shrinks the residual {resid_guess/resid_fit:.1f}x, "
          f"sharpening fault detection")
    print("=" * 56)
