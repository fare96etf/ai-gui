DELIMITERS = [
    (",", ","),
    (".", "."),
    ("|", "|")
]

ACTIVATION_CHOICES = [
    ("relu", "relu"),
    ("sigmoid", "sigmoid"), 
    ("softmax", "softmax"), 
    ("softplus", "softplus"), 
    ("softsign", "softsign"), 
    ("tanh", "tanh"), 
    ("selu", "selu"), 
    ("elu", "elu"), 
    ("exponential", "exponential")
]

OPTIMIZERS = [
    ("adam", "adam"),
    ("adamw", "adamw"),
    ("adadelta", "adadelta"),
    ("adagrad", "adagrad"),
    ("adamax", "adamax"),
    ("adafactor", "adafactor"),
    ("nadam", "nadam"),
    ("sgd", "sgd"),
    ("rmsprop", "rmsprop"),
    ("ftrl", "ftrl")
]

LOSSES = [
    ("binary_crossentropy", "binary_crossentropy"),
    ("categorical_crossentropy", "categorical_crossentropy"),
    ("sparse_categorical_crossentropy", "sparse_categorical_crossentropy"),
    ("poisson", "poisson"),
    ("kl_divergence", "kl_divergence"),
    ("mean_squared_error", "mean_squared_error"),
    ("mean_absolute_error", "mean_absolute_error"),
    ("mean_absolute_percentage_error", "mean_absolute_percentage_error"),
    ("mean_squared_logarithmic_error", "mean_squared_logarithmic_error"),
    ("cosine_similarity", "cosine_similarity"),
    ("huber_loss", "huber_loss"),
    ("log_cosh", "log_cosh")
]