import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success/x_cnt #конверсия контроля
    p2 = y_success/y_cnt #конверсия теста
    p = (x_success+y_success)/(x_cnt + y_cnt) #общая конверсия
    z = (p1-p2)/sqrt(p*(1-p)*(1/x_cnt + 1/y_cnt))
   
#1 вариант
    crit = st.norm.ppf(1 - 0.06/2) #для определения критических точек
    return ((z < crit) or (z > crit)) #проверяем входит ли z в область (-inf, -Zcr) U (Zcr, +inf) и возвращаем true/false
  
#2 вариант
    p_value = 2 * norm.sf(abs(z))
    return p_value < 0.06 # H0 отвергается (1) или не отвергается (0)
  
#В случае двустороннего теста p-значение равно: P(t)=2\min(P_0,P)
#Если p(t) меньше заданного уровня значимости, то нулевая гипотеза отвергается в пользу альтернативной. В противном случае она не отвергается.
