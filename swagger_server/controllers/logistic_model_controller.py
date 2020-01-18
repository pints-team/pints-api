import connexion
import six

from swagger_server import util


def logistic_model(x):  # noqa: E501
    """Evaluates this log-likelihood

    Returns the natural logarithm of the likelihood for this problem.  The size of the parameter &#x60;&#x60;x&#x60;&#x60; is given by /n_parameters&#x60;.  # noqa: E501

    :param x: Parameter value at which to calculate likelihood
    :type x: List[float]

    :rtype: float
    """
    return 'do some magic!'


def logistic_model_evaluate_s1(x):  # noqa: E501
    """Evaluates this log-likelihood with derivatives

    Returns the result plus the partial derivatives of the result with respect to the parameters. The returned data is an 2D array of parameter arrays [L, L&#x27;] where L is a scalar value and L&#x27; is a sequence of length n_parameters. Note that the derivative returned is of the log-pdf, so L&#x27; &#x3D; d/dp log(f(p)), evaluated at p&#x3D;x.  # noqa: E501

    :param x: Parameter at which to calculate log pdf
    :type x: List[float]

    :rtype: float
    """
    return 'do some magic!'


def logistic_model_n_parameters():  # noqa: E501
    """Returns the dimension of the space

    Returns the dimension of the space # noqa: E501


    :rtype: int
    """
    return 'do some magic!'
