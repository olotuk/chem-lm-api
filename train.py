import pandas as pd
from functions import featurize
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
if __name__ == "__main__":

    df = pd.read_csv("C:/Users/olotu/OneDrive/Desktop/progetti_exp/chem-lm-api/chem-lm-api/data/delaney-processed.csv")  

    # measured log solubility in mols per litre - 1128

    righe_buone = []
    scartati = 0
    target = []


    for index, row in df.iterrows():
        try:
            buone = featurize(row["smiles"])
            righe_buone.append(buone)
            target.append(row["measured log solubility in mols per litre"])
        except ValueError:
            scartati += 1


        

    x = pd.DataFrame(righe_buone)
    y = target

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mean = mean_absolute_error(y_test, y_pred)
    print(r2)
    print(mean)

    feature_names = x.columns.tolist()
    bundle = {"model" : model, "feature_names" : feature_names}
    joblib.dump(bundle, "models/model.joblib")

