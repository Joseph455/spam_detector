from typing import Annotated
from pydantic import BaseModel
from fastapi.routing import APIRouter
from fastapi import Body
from server.models.enums import Model as MLModel, ModelLable, MODEL_LOCATIONS, VECTORIZER_LOCATIONS
from server.models.train_nb_model import test_model as test_naive_bayes_model
from server.models.train_svm_model import test_model as test_svm_model
from server.models.train_rf_model import test_model as test_random_forest_model
from server.models.utils import load_resource


router = APIRouter()


class SPAMDetectionRequest(BaseModel):
    email_content: str
    model: MLModel


class SPAMDetectionResponse(BaseModel):
    prediction: ModelLable



MODELS_TEST_FUNCTIONS = {
    MLModel.NB: test_naive_bayes_model,
    MLModel.SVM: test_svm_model,
    MLModel.RF: test_random_forest_model,
}

MODELS = {
    MLModel.NB: load_resource(path=MODEL_LOCATIONS[MLModel.NB]),
    MLModel.SVM: load_resource(path=MODEL_LOCATIONS[MLModel.SVM]),
    MLModel.RF: load_resource(path=MODEL_LOCATIONS[MLModel.RF]),
}

MODEL_VECTORIZERS = {
    MLModel.NB: load_resource(path=VECTORIZER_LOCATIONS[MLModel.NB]),
    MLModel.SVM: load_resource(path=VECTORIZER_LOCATIONS[MLModel.SVM]),
    MLModel.RF: load_resource(path=VECTORIZER_LOCATIONS[MLModel.RF]),
}


@router.get('/health/')
def health_check() -> None:
    return {"status": "UP"}


@router.post('/scan/')
def detect_spam(data: Annotated[SPAMDetectionRequest, Body(...)]) -> SPAMDetectionResponse:
    model = MODELS[data.model]
    vectorizer = MODEL_VECTORIZERS[data.model]
    connector = MODELS_TEST_FUNCTIONS[data.model]

    prediction = connector(
        model=model,
        vectorizer=vectorizer,
        content=data.email_content, 
    )

    return SPAMDetectionResponse(prediction=prediction)
