# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse4001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error: str=None):  # noqa: E501
        """InlineResponse4001 - a model defined in Swagger

        :param error: The error of this InlineResponse4001.  # noqa: E501
        :type error: str
        """
        self.swagger_types = {
            'error': str
        }

        self.attribute_map = {
            'error': 'error'
        }
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse4001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_400_1 of this InlineResponse4001.  # noqa: E501
        :rtype: InlineResponse4001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self) -> str:
        """Gets the error of this InlineResponse4001.


        :return: The error of this InlineResponse4001.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this InlineResponse4001.


        :param error: The error of this InlineResponse4001.
        :type error: str
        """

        self._error = error