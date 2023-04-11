import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1022285388 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    test = stats.ks_2samp(x, y)
    p_value = test[1]
    if p_value < 0.03:
        answer = True
    else:
        answer = False
    return answer # Ваш ответ, True или False
