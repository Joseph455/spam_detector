import pandas  as pd
import joblib
from typing import Any
from .enums import Model, ModelLable, MODEL_LOCATIONS


def load_dataset() -> pd.DataFrame:
    data = pd.read_csv('./server/models/data/spam_Emails_data.csv')
    return data


def save_resource(resource: Any, path: str) -> None:
    """Save the vectorizer."""
    joblib.dump(resource, path)


def load_resource(path: str) -> Any:
    return joblib.load(path)


