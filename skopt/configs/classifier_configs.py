all_classifier_configs = {

    'RandomForestClassifier': [
        {
            'name'  : 'max_depth',
            'type'  : 'discrete',
            'domain': (5, 20, 40)
        },
        {
            'name'  : 'min_samples_split',
            'type'  : 'discrete',
            'domain': (2, 8, 32)
        },
        {
            'name'  : 'n_estimators',
            'type'  : 'discrete',
            'domain': (50, 300)
        }
    ],

    'LinearSVC': [
        {
            'name'  : 'tol',
            'type'  : 'continuous',
            'domain': (1e-5, 1e-1),
        },
        {
            'name'  : 'C',
            'type'  : 'continuous',
            'domain': (1e-4, 25),
        }
    ],

}
