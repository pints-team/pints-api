# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestLogisticModelController(BaseTestCase):
    """LogisticModelController integration test stubs"""

    def test_logistic_model(self):
        """Test case for logistic_model

        Evaluates this log-likelihood
        """
        query_string = [('x', 3.4)]
        response = self.client.open(
            '/pints-team/pints2/1.0.0/logistic-model',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logistic_model_evaluate_s1(self):
        """Test case for logistic_model_evaluate_s1

        Evaluates this log-likelihood with derivatives
        """
        query_string = [('x', 3.4)]
        response = self.client.open(
            '/pints-team/pints2/1.0.0/logistic-model/evaluateS1',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logistic_model_n_parameters(self):
        """Test case for logistic_model_n_parameters

        Returns the dimension of the space
        """
        response = self.client.open(
            '/pints-team/pints2/1.0.0/logistic-model/n_parameters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
