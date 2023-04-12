# General porpouse functions of the project
import random
import numpy as np

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)