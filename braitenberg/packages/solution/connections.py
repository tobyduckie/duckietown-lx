from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    #left_motor  = const + gain *  np.sum( LEFT * preprocess(image) )
    # these are random values
    res[230:480, 320:420] = -1
    #res[400:480, 320:640] = -1
    res[258:480, 420:530] = -0.45
    res[280:480, 530:640] = -0.2
    
    #res[200:400, 250:320] = 1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    #right_motor = const + gain *  np.sum( RIGHT * preprocess(image) )
    # these are random values
    res[230:480, 220:320] = -1
    #res[400:480, 0:320] = -1
    res[258:480, 110:220] = -0.45
    res[280:480, 0:110] = -0.2
    
    #res[230:480, 280:360] = 1
    # ---
    return res
