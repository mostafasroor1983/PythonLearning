from datetime import date
from math import sqrt
from json import dumps
print(sqrt(9))
print("#"*50)

today = date.today()
print(f"today: {today}")
print("#"*50)

json_data = {"id": 1, "name": "mostafa"}
data = dumps(json_data)
print(f"data: {data}")
print("#"*50)

import pandas as pd

