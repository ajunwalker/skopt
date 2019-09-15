import numpy as np
from skopt import model_searcher

def test_forest_classifier():
    X = np.random.normal(size=(100,100))
    y = [0 for i in range(50)] + [1 for i in range(50)]
    searcher = model_searcher.ModelSearcher('RandomForestClassifier')
    searcher.fit(X, y, 'accuracy')


def test_svm_classifier():
    X = np.random.normal(size=(100,100))
    y = [0 for i in range(50)] + [1 for i in range(50)]
    searcher = model_searcher.ModelSearcher('LinearSVC')
    searcher.fit(X, y, 'accuracy')


def test_forest_regressor():
    X = np.random.normal(size=(100,100))
    y = np.random.normal(size=(100,))
    searcher = model_searcher.ModelSearcher('RandomForestRegressor')
    searcher.fit(X, y, 'r2')


def test_svm_regressor():
    X = np.random.normal(size=(100,100))
    y = np.random.normal(size=(100,))
    searcher = model_searcher.ModelSearcher('LinearSVR')
    searcher.fit(X, y, 'r2')
