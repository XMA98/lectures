import pandas as pd
import numpy as np
from unanswered import *

aud_usd_lst = [
    ('2020-09-08', 0.7280),
    ('2020-09-09', 0.7209),
    ('2020-09-11', 0.7263),
    ('2020-09-14', 0.7281),
    ('2020-09-15', 0.7285),
    ]

eur_aud_lst = [
    ('2020-09-08',  1.6232),
    ('2020-09-09',  1.6321),
    ('2020-09-10',  1.6221),
    ('2020-09-11',  1.6282),
    ('2020-09-15',  1.6288),
    ]

# Replace unanswered with your solution.

# change aud_usd_lst to series, date-index, rate-value
index = [key for key, value in aud_usd_lst]
data = [value for key, value in aud_usd_lst]
aud_usd_series = pd.Series(data=data, index=index)

# print(index)
# print(data)
# print(aud_usd_series)

#  change eur_aud_lst to series, date-index, rate-value
index = [key for key, value in eur_aud_lst]
data = [value for key, value in eur_aud_lst]
eur_aud_series = pd.Series(data=data, index=index)
# print(eur_aud_series)

# combine two series
df = pd.DataFrame({'AUD/USD': aud_usd_series, 'EUR/AUD': eur_aud_series})
# print(df)
