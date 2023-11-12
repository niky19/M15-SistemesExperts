import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Apunts i proves/2022_MeteoCat_Detall_Estacions.csv')
#print(df.info())
print(df.corr())