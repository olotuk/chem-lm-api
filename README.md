# chem-lm-api

[![CI](https://github.com/olotuk/chem-lm-api/actions/workflows/ci.yml/badge.svg)](https://github.com/olotuk/chem-lm-api/actions/workflows/ci.yml)

REST API that predicts the aqueous solubility 
of a molecule from its SMILES string, using RDKit descriptors and a scikit-learn model
## Overview
The API receives a SMILES string, computes molecular descriptors with RDKit, and returns a predicted property using a Random Forest model trained on the ESOL dataset

**Stack:** FastAPI · RDKit · scikit-learn · Docker · pytest

## How it works

1. Input: a SMILES string
2. Featurization: 6 molecular descriptors via RDKit
3. Prediction: scikit-learn Random Forest
4. Output: JSON with descriptors + predicted solubility

## Installation
### With Docker (recommended)
docker compose up

The API will be available at http://localhost:8000

### Local development
```
conda create -n chem-api python=3.11

conda activate chem-api

pip install -r requirements.txt

uvicorn app.main:app --reload
```
 ## Usage
 Interactive documentation available at `http://localhost:8000/docs`.

 curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"smiles": "CCO"}'

 **example response.**
```json
 {
  "prediction": 0.9646999999999992,
  "descriptors": {
    "MolWt": 46.069,
    "MolLogP": -0.0014000000000000123,
    "NumHDonors": 1,
    "NumHAcceptors": 1,
    "TPSA": 20.23,
    "NumRotatableBonds": 0
  },
  "property_name": "Solubility"
}
```
## Model
- **Dataset:** ESOL/Delaney-about 1000 molecules
- **Model:** Random Forest Regressor
- **Performance:** R² ≈ 0.85, MAE ≈ 0.57 on test set

## Tests
pytest

3 tests covering featurization, prediction and error handling

## Project structure
```
chem-ml-api/
├── app/                  # FastAPI application
│   └── main.py
├── functions.py          # RDKit featurization
├── train.py              # model training script
├── models/               # serialized model
├── tests/
├── Dockerfile
└── docker-compose.yml
```
