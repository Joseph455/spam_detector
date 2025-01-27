from server.models.train_nb_model import (
    train_model as train_naive_bayes_model,
    test_model as test_naive_bayes_model,
)
from server.models.train_svm_model import (
    train_model as train_svm_model,
    test_model as test_svm_model,
)

from server.models.train_rf_model import (
    train_model as train_random_forest_model,
    test_model as test_random_forest_model,
)
from server.models.utils import save_resource, load_resource
from server.models.enums import ModelLable, Model, MODEL_LOCATIONS, VECTORIZER_LOCATIONS


def main():
    print("Training Random Forest model...")
    model, vectorizer, accuracy = train_random_forest_model()
    print(f"Model accuracy: {accuracy}")
    print("Model trained successfully!")

    print('Saving Model & Vecorizer')
    save_resource(resource=model, path=MODEL_LOCATIONS[Model.RF])
    save_resource(resource=vectorizer, path=VECTORIZER_LOCATIONS[Model.RF])
    print('Model Saved')

    print('Loading model & vectorizer')
    loaded_model = load_resource(path=MODEL_LOCATIONS[Model.RF])
    loaded_vectorizer = load_resource(path=VECTORIZER_LOCATIONS[Model.RF])
    print('Model loaded & vectorizer')

    # testing_model on a value
    print('Making a preiction')
    content = """
    'We’re on a mission to connect you with a dream 
    job— maybe you’ll find one on this curated list. 
    To refine these recommendations, search for more jobs on Glassdoor or update your profile. We’re rooting for you!
    """

    prediction = test_random_forest_model(
        content=content, 
        model=loaded_model, 
        vectorizer=loaded_vectorizer,
    )

    print(f'Prediction is {prediction}')


if __name__ == "__main__":
    main()
