from enum import Enum


class ModelLable(Enum):
    SPAM = 1
    HAM = 0


class Model(Enum):
    NB = 'naive_bayes'
    SVM = 'support_vector_machine'
    RF = 'random_forest'


MODEL_LOCATIONS = {
    Model.RF: 'server/models/data/random_forest_spam_model.sav',
    Model.NB: 'server/models/data/naive_bayes_spam_model.sav',
    Model.SVM: 'server/models/data/svm_spam_model.sav',
}


VECTORIZER_LOCATIONS = {
    Model.RF: 'server/models/data/random_forest_spam_vectorizer.sav',
    Model.NB: 'server/models/data/naive_bayes_spam_vectorizer.sav',
    Model.SVM: 'server/models/data/svm_spam_vectorizer.sav',
}