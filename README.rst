.. -*- mode: rst -*-

|Travis|_ |Codecov|_

.. |Travis| image:: https://travis-ci.com/ajunwalker/skopt.svg?branch.master
.. _Travis: https://travis-ci.com/ajunwalker/skopt

.. |Codecov| image:: https://codecov.io/gh/ajunwalker/skopt/branch/master/graph/badge.svg
.. _Codecov: https://codecov.io/gh/ajunwalker/skopt

skopt
=====

skopt is a python module for automatically performing bayesian optimization on scikit-learn machine learning algorithms.

Installation
------------

skopt has been tested to work with the following packages:

- GPyOpt==1.2.5
- scikit-learn==0.21.2

Supported algorithms
--------------------

The following algorithms are currently supported by skopt:

Classification
~~~~~~~~~~~~~~
- LinearSVC
- RandomForestClassifier

Regression
~~~~~~~~~~
- LinearSVR
- RandomForestRegressor

Getting started
---------------

Below is a simple example of using skopt to find the optimal parameters for a random forest classifiers with features ``X`` and labels ``y``::

    from skopt import model_searcher
    searcher = model_searcher.ModelSearcher('RandomForestClassifier')
    searcher.fit(X, y, 'accuracy')
