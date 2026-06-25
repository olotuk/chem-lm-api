from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from functions import featurize

bundle = joblib.load("models/model.joblib")
model = bundle["model"]
feature_names = bundle["feature_names"]
app = FastAPI()

@app.get("/health")
async def health():
    return {"status" : "ok"}

class MoleculeInput(BaseModel):
    smiles : str

class PredictionOutput(BaseModel):
    prediction : float
    descriptors : dict[str, float]
    property_name : str


@app.post("/predict", response_model=PredictionOutput)
def predict(payload : MoleculeInput):
    try:
        descriptors = featurize(payload.smiles)
        vector = [descriptors[nome] for nome in feature_names]
        prediction = float(model.predict([vector])[0])
        return {
            "prediction" : prediction,
            "descriptors" : descriptors,
            "property_name" : "Solubility",
        }
    except ValueError as e:
        raise HTTPException (status_code=422, detail=str(e))