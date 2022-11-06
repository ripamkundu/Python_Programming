from tkinter import S
import numpy as np
import pandas as pd
arr = np.array(['Riapm', 'Priyanka', 'Gourav', 'Anish'])
se = pd.Series(arr, index= (['student - 1', 'student - 2', 'student - 3']))
print("Name : ", arr)
print(se)
