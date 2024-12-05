# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SendBulkBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, recipients: List[str]=None, message: str=None):  # noqa: E501
        """SendBulkBody - a model defined in Swagger

        :param recipients: The recipients of this SendBulkBody.  # noqa: E501
        :type recipients: List[str]
        :param message: The message of this SendBulkBody.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'recipients': List[str],
            'message': str
        }

        self.attribute_map = {
            'recipients': 'recipients',
            'message': 'message'
        }
        self._recipients = recipients
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'SendBulkBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The send_bulk_body of this SendBulkBody.  # noqa: E501
        :rtype: SendBulkBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def recipients(self) -> List[str]:
        """Gets the recipients of this SendBulkBody.

        List of recipient addresses  # noqa: E501

        :return: The recipients of this SendBulkBody.
        :rtype: List[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients: List[str]):
        """Sets the recipients of this SendBulkBody.

        List of recipient addresses  # noqa: E501

        :param recipients: The recipients of this SendBulkBody.
        :type recipients: List[str]
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def message(self) -> str:
        """Gets the message of this SendBulkBody.

        Message content  # noqa: E501

        :return: The message of this SendBulkBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this SendBulkBody.

        Message content  # noqa: E501

        :param message: The message of this SendBulkBody.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message
