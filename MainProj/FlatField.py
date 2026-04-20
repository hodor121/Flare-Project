import numpy as np

def flat_field_correction(image, flat, dark, eps=1e-8):
    """
    Perform flat-field correction on an image.

    Parameters
    ----------
    image : ndarray
        Raw image (H, W) or (H, W, 3)
    flat : ndarray
        Flat-field image (same shape as image)
    dark : ndarray
        Dark-field image (same shape as image)
    eps : float
        Small number to avoid division by zero

    Returns
    -------
    corrected : ndarray
        Flat-field corrected image (float64)
    """

    # Convert to float for safe arithmetic
    image = image.astype(np.float64)
    flat = flat.astype(np.float64)
    dark = dark.astype(np.float64)

    # Subtract dark field
    image_corr = image - dark
    flat_corr = flat - dark

    # Prevent division by zero
    flat_corr[flat_corr < eps] = eps

    # Compute median per channel if RGB
    if image.ndim == 3:
        median_flat = np.median(flat_corr, axis=(0, 1))
    else:
        median_flat = np.median(flat_corr)

    # Apply flat-field correction
    corrected = image_corr * median_flat / flat_corr

    return corrected
print("SpectralSensitivity module loaded")
print("Available names:", dir())