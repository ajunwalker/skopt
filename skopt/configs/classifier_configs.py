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
            'name'  : 'alpha',
            'type'  : 'continuous',
            'domain': (1e-6, 1e-2),
        },
        {
            'name'  : 'max_iter',
            'type'  : 'discrete',
            'domain': (200,),
        }
    ],

}
