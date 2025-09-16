# from fastapi import FastAPI
# from pydantic import BaseModel
# import pickle
# from typing import Optional

# # Cargar modelo entrenado desde archivo modelo.pkl
# with open("modelo.pkl", "rb") as f:
#     vectorizer, model = pickle.load(f)

# app = FastAPI()

# class HistoriaClinica(BaseModel):
#     sintomas: str

# @app.post("/diagnostico")
# def generar_diagnostico(historia: HistoriaClinica):
#     texto = historia.sintomas
#     X = vectorizer.transform([texto])
#     diagnostico = model.predict(X)[0]
#     razon = f"Se detectaron palabras clave relacionadas con {diagnostico}."
#     return {
#         "diagnostico": diagnostico,
#         "razonamiento": razon
#     }
