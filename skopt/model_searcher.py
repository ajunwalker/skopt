# Third party imports
from GPyOpt.methods import BayesianOptimization
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import cross_validate
from sklearn.svm import LinearSVC, LinearSVR

# Local imports
from configs.classifier_configs import all_classifier_configs
from configs.regressor_configs import all_regressor_configs

class ModelSearcher:
    """
    This class acts as an interface for performing bayesian optimization on
    a specified model, or several models.
    """

    def __init__(self, model_name: str) -> None:
        """
        Initializes models and grids for grid search.
        :param str model_name:
        """

        available_classifiers = {
            'RandomForestClassifier': RandomForestClassifier,
            'LinearSVC'             : LinearSVC,
        }

        available_regressors = {
            'RandomForestRegressor' : RandomForestRegressor,
            'LinearSVR'             : LinearSVR,
        }

        if model_name in available_classifiers:
            self.selected_model = available_classifiers[model_name]
            self.grid = all_classifier_configs[model_name]
            self.metrics = ['accuracy', 'f1', 'roc_auc']

        elif model_name in available_regressors:
            self.selected_model = available_regressors[model_name]
            self.grid = all_regressor_configs[model_name]
            self.metrics = ['r2', 'neg_mean_absolute_error',
                            'neg_mean_squared_error']

        else:
            msg = "Unsupported model name '{}'\n".format(model_name)

            msg += "Available classifiers:\n"
            for classifier in available_classifiers:
                msg += "    {}\n".format(classifier)

            msg += "Available regressor:"
            for regressor in available_regressors:
                msg += "\n    {}".format(regressor)

            raise ValueError(msg)

        self.results = []
        self.tried = {}


    def run_iteration(self, params: list):
        """
        Fits model with paramaters selected by bayesian optimization.

        :param list params: Parameters for model.
        """
        print(params)

        if str(params) in self.tried:
            return self.tried[str(params)]

        param_dict = {}

        # Construct parameter dict for model
        for param, value in zip(self.grid, params[0]):
            if param['type'] == 'discrete':
                param_dict[param['name']] = int(value)
            else:
                param_dict[param['name']] = value

        cv = cross_validate(
            estimator=self.selected_model(**param_dict),
            X=self.X,
            y=self.y,
            scoring=self.metrics,
            cv=5,
            return_estimator=True,
            return_train_score=True)

        result = {'params': param_dict, 'time': cv['score_time'].mean()}
        for metric in self.metrics:
            result[metric] = cv['test_' + metric].mean()
        self.results.append(result)

        return 1 - result[self.core_metric]


    def fit(self, X: list, y: list, metric: str=None, max_iter: int=50,
            silence=False) -> None:
        """
        Perform bayesian optimization on hyperparameter space.

        :param list x: Array containing training input data.
        :param list y: Array containing data labels.
        :param int max_iter: Number of iterations to perform bayesian optimization.
        """

        if metric not in self.metrics:
            msg = "Unsupported metric '{}'".format(metric)
            msg += "\nSupported metrics are: {}".format(self.metrics)
            raise ValueError(msg)

        self.X = X
        self.y = y
        self.core_metric = metric
        opt = BayesianOptimization(f=self.run_iteration, domain=self.grid)
        opt.run_optimization(max_iter=max_iter)
