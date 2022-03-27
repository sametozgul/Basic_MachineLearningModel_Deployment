import numpy as np
import pandas as pd

data=pd.read_csv("storepurchasedata.csv")

X=data.iloc[:,:-1]
y=data.iloc[:,-1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.20,random_state=0)

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier

model=KNeighborsClassifier(n_neighbors=5)

model.fit(X_train,y_train)

# y_pred=model.predict(X_test)
# y_prop=model.predict_proba(X_test)[:,-1]

# from sklearn.metrics import confusion_matrix

# cf=confusion_matrix(y_test,y_pred)
# print(cf)

# from sklearn.metrics import accuracy_score

# acc=accuracy_score(y_test,y_pred)
# print(acc)

# from sklearn.metrics import classification_report

# print(classification_report(y_test,y_pred))
def  make_prediction(age,salary):
    new_predict=model.predict(scaler.transform(np.array([[age,salary]])))
    return new_predict

