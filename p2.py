import numpy as np
import pandas as pd

data = {
    'A': np.array([1, 4, 7]),
    'B': np.array([2, 5, 8]),
    'C': np.array([3, 6, 9]),
}

df = pd.DataFrame(data)
print(df)