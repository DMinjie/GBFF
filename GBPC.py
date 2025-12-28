import numpy as np
from PIL import Image
import os


def GBPC(A, B):
    if not isinstance(A, Image.Image) or not isinstance(B, Image.Image):
        raise ValueError("Inputs must be PIL images")

    A = np.array(A).astype(np.float32)
    B = np.array(B).astype(np.float32)
    A = np.clip(A, 0, 255)
    B = np.clip(B, 0, 255)
    X = np.zeros_like(A)
    print(f"The GBPC coming soon~!")
    Y=0
    BND=0
    POS=0

    return Y, BND, POS




