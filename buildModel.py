# %%
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import numpy as np
# %%
df = sns.load_dataset("tips")

xtrain, xtest, ytrain, ytest = train_test_split(df.drop("tip", axis=1), df["tip"], train_size=0.8)
# %%

numcols = ["total_bill"]
catcols = xtrain.select_dtypes("category").columns

ohe = OneHotEncoder()
ss = StandardScaler()

prep_pl_categorical = Pipeline([
    ("OHE", ohe)
])

prep_pl_numeric = Pipeline([
    ("Scaling", ss)
])


ct = ColumnTransformer([
    ("1", prep_pl_categorical, catcols),
    ("2", prep_pl_numeric, numcols)
])

# %%

ct.fit(xtrain)
xtrain = ct.transform(xtrain)
xtest = ct.transform(xtest)

# %%
new_input = pd.DataFrame({"total_bill": 16.99, "sex": "Female", "smoker": "No", "day": "Sun", "time": "Dinner", "size":2}, index=[0])

# %%
from sklearn.linear_model import LinearRegression
lmodel = LinearRegression()
lmodel.fit(xtrain, ytrain)

# %%
import pickle
with open("lmodel.pck", "wb") as f:
    pickle.dump(lmodel, f)

with open("transformer.pck", "wb") as f:
    pickle.dump(ct, f)

# %%

