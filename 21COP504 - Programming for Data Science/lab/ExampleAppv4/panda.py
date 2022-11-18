import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
        'name': ['Wii Sport', 'Super Mario Bros', 'Pokemon Red', 'Ninendogs' ],
        'Platform': ['Wii', 'NES', 'GB', 'DS'],
        'EU_Sale': [29.02, 3.58, 8.89, 11.00],
        'Genre': ['Sports', 'Platform', 'Role-Playeing', 'Simulation']
        }
        
vgsale = pd.DataFrame(data = data)
vgsale['Year'] =[2006, 1985, 1996, 200]