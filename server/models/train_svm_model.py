import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from .utils import load_dataset
from .enums import ModelLable, Model, MODEL_LOCATIONS



def train_model() -> tuple[SVC, TfidfVectorizer, float]:
    """Train Naive Bayes model."""

    data_set =  load_dataset()

    # convert the labels to binary values
    data_set['binary_label'] = data_set['label'].apply(
        lambda x: ModelLable.SPAM.value if x == 'Spam' else ModelLable.HAM.value
    )

    # split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        data_set['text'], 
        data_set['binary_label'], 
        random_state=1,
        train_size=0.7,
    )

    # convert the text data to a matrix of token counts
    vectorizer = TfidfVectorizer(stop_words='english')
    training_data = vectorizer.fit_transform(X_train.apply(lambda x: np.str_(x)).values)
    testing_data = vectorizer.transform(X_test.apply(lambda x: np.str_(x)).values)

    # train the model
    model = SVC(C=0.1, kernel='linear')
    model.fit(training_data, y_train)

    # calculate the accuracy of the model
    accuracy = model.score(testing_data, y_test)

    return model, vectorizer, accuracy


def test_model(content: str, model: SVC, vectorizer: TfidfVectorizer) -> ModelLable:
    """Test naive bayes model."""

    prediction = model.predict(vectorizer.transform([content]))
    return ModelLable.SPAM if prediction[0] == ModelLable.SPAM.value else ModelLable.HAM
