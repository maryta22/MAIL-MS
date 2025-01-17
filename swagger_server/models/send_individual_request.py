# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SendIndividualRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, to_email: str=None, to_name: str=None, message: str=None, sender_email: str=None, sender_name: str=None, subject: str=None):  # noqa: E501
        """SendIndividualRequest - a model defined in Swagger

        :param to_email: The to_email of this SendIndividualRequest.  # noqa: E501
        :type to_email: str
        :param to_name: The to_name of this SendIndividualRequest.  # noqa: E501
        :type to_name: str
        :param message: The message of this SendIndividualRequest.  # noqa: E501
        :type message: str
        :param sender_email: The sender_email of this SendIndividualRequest.  # noqa: E501
        :type sender_email: str
        :param sender_name: The sender_name of this SendIndividualRequest.  # noqa: E501
        :type sender_name: str
        :param subject: The subject of this SendIndividualRequest.  # noqa: E501
        :type subject: str
        """
        self.swagger_types = {
            'to_email': str,
            'to_name': str,
            'message': str,
            'sender_email': str,
            'sender_name': str,
            'subject': str
        }

        self.attribute_map = {
            'to_email': 'to_email',
            'to_name': 'to_name',
            'message': 'message',
            'sender_email': 'sender_email',
            'sender_name': 'sender_name',
            'subject': 'subject'
        }
        self._to_email = to_email
        self._to_name = to_name
        self._message = message
        self._sender_email = sender_email
        self._sender_name = sender_name
        self._subject = subject

    @classmethod
    def from_dict(cls, dikt) -> 'SendIndividualRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SendIndividualRequest of this SendIndividualRequest.  # noqa: E501
        :rtype: SendIndividualRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def to_email(self) -> str:
        """Gets the to_email of this SendIndividualRequest.

        Email address of the recipient  # noqa: E501

        :return: The to_email of this SendIndividualRequest.
        :rtype: str
        """
        return self._to_email

    @to_email.setter
    def to_email(self, to_email: str):
        """Sets the to_email of this SendIndividualRequest.

        Email address of the recipient  # noqa: E501

        :param to_email: The to_email of this SendIndividualRequest.
        :type to_email: str
        """
        if to_email is None:
            raise ValueError("Invalid value for `to_email`, must not be `None`")  # noqa: E501

        self._to_email = to_email

    @property
    def to_name(self) -> str:
        """Gets the to_name of this SendIndividualRequest.

        Name of the recipient  # noqa: E501

        :return: The to_name of this SendIndividualRequest.
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name: str):
        """Sets the to_name of this SendIndividualRequest.

        Name of the recipient  # noqa: E501

        :param to_name: The to_name of this SendIndividualRequest.
        :type to_name: str
        """
        if to_name is None:
            raise ValueError("Invalid value for `to_name`, must not be `None`")  # noqa: E501

        self._to_name = to_name

    @property
    def message(self) -> str:
        """Gets the message of this SendIndividualRequest.

        Content of the message  # noqa: E501

        :return: The message of this SendIndividualRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this SendIndividualRequest.

        Content of the message  # noqa: E501

        :param message: The message of this SendIndividualRequest.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def sender_email(self) -> str:
        """Gets the sender_email of this SendIndividualRequest.

        Sender's email address  # noqa: E501

        :return: The sender_email of this SendIndividualRequest.
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email: str):
        """Sets the sender_email of this SendIndividualRequest.

        Sender's email address  # noqa: E501

        :param sender_email: The sender_email of this SendIndividualRequest.
        :type sender_email: str
        """
        if sender_email is None:
            raise ValueError("Invalid value for `sender_email`, must not be `None`")  # noqa: E501

        self._sender_email = sender_email

    @property
    def sender_name(self) -> str:
        """Gets the sender_name of this SendIndividualRequest.

        Name of the sender  # noqa: E501

        :return: The sender_name of this SendIndividualRequest.
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name: str):
        """Sets the sender_name of this SendIndividualRequest.

        Name of the sender  # noqa: E501

        :param sender_name: The sender_name of this SendIndividualRequest.
        :type sender_name: str
        """
        if sender_name is None:
            raise ValueError("Invalid value for `sender_name`, must not be `None`")  # noqa: E501

        self._sender_name = sender_name

    @property
    def subject(self) -> str:
        """Gets the subject of this SendIndividualRequest.

        Subject of the email  # noqa: E501

        :return: The subject of this SendIndividualRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        """Sets the subject of this SendIndividualRequest.

        Subject of the email  # noqa: E501

        :param subject: The subject of this SendIndividualRequest.
        :type subject: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject
