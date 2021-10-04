import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from 

base = pd.read_csv("autos.csv", encoding="ISO-8859-1")

base = base.drop("dateCrawled", axis=1)
base = base.drop("dateCreated", axis=1)
base = base.drop("nrOfPictures", axis=1)
base = base.drop("postalCode", axis=1)
base = base.drop("lastSeen", axis=1)

base["abtest"].value_counts()

base["gearbox"].value_counts()

base["fuelType"].value_counts()

base["notRepairedDamage"].value_counts()

base["name"].value_counts()

base["seller"].value_counts()

base["offerType"].value_counts()


base = base.drop("name", axis=1)

base = base.drop("seller", axis=1)

base = base.drop("offerType", axis=1)

varInconsis1= base.loc[base.price <= 10]
varInconsis2= base.loc[base.price > 450000 ]

base = base.loc[base.price > 10]
base = base.loc[base.price < 450000]

base.loc[pd.isnull(base["vehicleType"])]
base["vehicleType"].value_counts() #limousine


base.loc[pd.isnull(base["gearbox"])]
base["gearbox"].value_counts() #manuell


base.loc[pd.isnull(base["model"])]
base["model"].value_counts() #golf


base.loc[pd.isnull(base["fuelType"])]
base["fuelType"].value_counts() #benzin



base.loc[pd.isnull(base["notRepairedDamage"])]
base["notRepairedDamage"].value_counts() #nein


valuesReplace = {"vehicleType":"limousine", "gearbox":"manuell",
                 "model":"golf", "fuelType":"benzin",
                 "notRepairedDamage":"nein"}


base= base.fillna(value = valuesReplace)


inputs = base.iloc[:,1:13].values

outputs = base.iloc[:,0].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_inputs = LabelEncoder()


inputs[:,0] = labelencoder_inputs.fit_transform(inputs[:,0])
inputs[:,1] = labelencoder_inputs.fit_transform(inputs[:,1])
inputs[:,3] = labelencoder_inputs.fit_transform(inputs[:,3])
inputs[:,5] = labelencoder_inputs.fit_transform(inputs[:,5])
inputs[:,8] = labelencoder_inputs.fit_transform(inputs[:,8])
inputs[:,9] = labelencoder_inputs.fit_transform(inputs[:,9])
inputs[:,10] = labelencoder_inputs.fit_transform(inputs[:,10])

onehotencoder = ColumnTransformer(transformers=[("OneHot", OneHotEncoder(), [0,1,3,5,8,9,10])],remainder='passthrough')

inputs = onehotencoder.fit_transform(inputs).toarray()


