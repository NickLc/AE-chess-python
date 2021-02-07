# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
df = pd.read_csv("cotas_funcion_evaluacion.csv", sep = ';')


# %%
df


# %%
cotas_inferiores = df.cota_inferior.values
cotas_inferiores = cotas_inferiores.tolist()
cotas_inferiores


# %%
cotas_superiores = df.cota_superior.values
cotas_superiores = cotas_superiores.tolist()
cotas_superiores


