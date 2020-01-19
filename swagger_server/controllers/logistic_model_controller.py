import connexion
import six

from swagger_server import util

import pints
import pints.toy
import numpy as np

# Load a forward model
model = pints.toy.LogisticModel()

# Create some toy data
real_parameters = [0.015, 500]
times = np.linspace(0, 1000, 1000)
values = model.simulate(real_parameters, times)

# Add noise
values += np.random.normal(0, 10, values.shape)

# Create an object with links to the model and time series
problem = pints.SingleOutputProblem(model, times, values)

# create a log_likelihood using gaussian independent noise
log_likelihood = pints.GaussianLogLikelihood(problem)


def logistic_model(x):  # noqa: E501
    """Evaluates this log-likelihood

    Returns the natural logarithm of the likelihood L for this problem. The size of the parameter
    ``x`` is given by /n_parameters`.

    :param x: Parameter value at which to calculate likelihood
    :type x: List[float]

    :rtype: float
    """
    print('called logistic_model with',x)
    return log_likelihood(x)


def logistic_model_evaluate_s1(x):  # noqa: E501
    """Evaluates this log-likelihood with derivatives

    Returns the result plus the partial derivatives of the result with respect to the parameters.
    The returned data is an array of length n_parameters+1 of the form [L, dL/dp_1, dL/dp_2, ...],
    where L is the log-likelihood and dL/dp_1 is the derivative of the log-likelihood with respect
    to p_1, the first parameter.

    :param x: Parameter at which to calculate log pdf
    :type x: List[float]

    :rtype: float
    """
    print('called logistic_model_evaluate_s1 with',x)
    L, dLdp = log_likelihood.evaluateS1(x)
    return [L] + dLdp.tolist()


def logistic_model_n_parameters():  # noqa: E501
    """Returns the dimension of the space

    Returns the dimension of the space # noqa: E501


    :rtype: int
    """
    return log_likelihood.n_parameters()
