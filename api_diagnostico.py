from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pickle

app = FastAPI()

# Cargar modelo entrenado
with open("modelo_optica.pkl", "rb") as f:
    modelo = pickle.load(f)

# Diccionarios con justificaciones y prescripciones clínicas
justificaciones = {
    "Miopía": "La miopía causa dificultad para ver objetos lejanos debido a un enfoque incorrecto en la retina.",
    "Astigmatismo": "El astigmatismo provoca visión borrosa, dolor ocular y visión doble debido a irregularidades en la curvatura corneal.",
    "Presbicia": "La presbicia dificulta enfocar objetos cercanos, común en personas mayores debido a pérdida de elasticidad del cristalino.",
    "Conjuntivitis": "La conjuntivitis se manifiesta con enrojecimiento, picazón y secreción ocular, causada por inflamación o infección de la conjuntiva.",
    "Glaucoma": "El glaucoma puede causar pérdida gradual de visión periférica y daño al nervio óptico por presión ocular elevada.",
    "Cataratas": "Las cataratas provocan visión nublada y halos alrededor de luces por opacidad progresiva del cristalino.",
    "Síndrome de ojo seco": "Este síndrome genera sensación de arenilla y enrojecimiento por falta de lubricación ocular adecuada.",
    "Degeneración macular": "Afecta la visión central progresivamente, dificultando actividades como la lectura y reconocimiento facial.",
    "Migraña oftálmica": "La migraña oftálmica produce dolor ocular intenso asociado a cefalea y alteraciones visuales temporales.",
    "Retinopatía diabética": "Complicación de la diabetes que daña los vasos sanguíneos de la retina, causando pérdida visual.",
    "Uveítis": "Inflamación de la úvea que causa dolor, enrojecimiento y sensibilidad a la luz.",
    "Blefaritis": "Inflamación crónica de los párpados con picazón y secreción, comúnmente por infección o disfunción glandular."
}

prescripciones = {
    "Miopía": "Uso de lentes correctivos y consultas periódicas con optómetra.",
    "Astigmatismo": "Lentes tóricos para corregir visión y seguimiento oftalmológico.",
    "Presbicia": "Lentes bifocales o progresivos según evaluación clínica.",
    "Conjuntivitis": "Colirios antibióticos o antiinflamatorios, mantener higiene ocular.",
    "Glaucoma": "Tratamiento con gotas para reducir presión intraocular y seguimiento estricto.",
    "Cataratas": "Evaluación para cirugía y medidas para evitar progresión.",
    "Síndrome de ojo seco": "Lágrimas artificiales y evitar ambientes secos.",
    "Degeneración macular": "Suplementos antioxidantes y control médico frecuente.",
    "Migraña oftálmica": "Tratamientos analgésicos y preventivos según neurología.",
    "Retinopatía diabética": "Control estricto de glucemia y terapias oftalmológicas.",
    "Uveítis": "Corticosteroides tópicos o sistémicos y seguimiento especializado.",
    "Blefaritis": "Higiene de párpados y antibióticos tópicos si son necesarios."
}

class HistoriaClinica(BaseModel):
    motivo: Optional[str] = ""
    sintomas_1: Optional[str] = ""
    sintomas_2: Optional[str] = ""
    sintomas_3: Optional[str] = ""

@app.post("/diagnostico")
async def diagnostico(historia: HistoriaClinica):
    texto_combinado = " ".join(filter(None, [
        historia.motivo.lower(),
        historia.sintomas_1.lower(),
        historia.sintomas_2.lower(),
        historia.sintomas_3.lower()
    ])).strip()

    pred = modelo.predict([texto_combinado])[0]

    justificacion = justificaciones.get(pred, "Diagnóstico basado en los síntomas proporcionados.")
    prescripcion = prescripciones.get(pred, "Consulta con un profesional para prescripción adecuada.")

    return {
        "diagnostico": pred,
        "razonamiento": justificacion,
        "prescripcion": prescripcion
    }
