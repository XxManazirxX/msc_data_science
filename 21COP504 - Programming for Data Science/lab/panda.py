import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
        'apple' : [600, 200, 50, 300],
        'orange' : [200, 300, 700, 400]
        }

dfFruit = pd.DataFrame(data)

dfFruit = pd.DataFrame(data, index = ['March', 'April', 'May', 'June'])
dfFruit['Compare'] = dfFruit['apple'] - dfFruit['orange']
        
                       
print(dfFruit)

print(dfFruit.columns)