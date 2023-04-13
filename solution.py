import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 734920047 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success/x_cnt #конверсия контроля
    p2 = y_success/y_cnt #конверсия теста
    p = (x_success+y_success)/(x_cnt + y_cnt) #общая конверсия
    z = (p1-p2)/np.sqrt(p*(1-p)*(1/x_cnt + 1/y_cnt))
    p_value = 2 * norm.sf(abs(z))
    return p_value < 0.06 # H0 отвергается (1) или не отвергается (0)
