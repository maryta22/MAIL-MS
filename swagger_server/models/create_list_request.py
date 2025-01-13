# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CreateListRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, folder_id: str=None, emails: List[str]=None):  # noqa: E501
        """CreateListRequest - a model defined in Swagger

        :param name: The name of this CreateListRequest.  # noqa: E501
        :type name: str
        :param folder_id: The folder_id of this CreateListRequest.  # noqa: E501
        :type folder_id: str
        :param emails: The emails of this CreateListRequest.  # noqa: E501
        :type emails: List[str]
        """
        self.swagger_types = {
            'name': str,
            'folder_id': str,
            'emails': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'folder_id': 'folder_id',
            'emails': 'emails'
        }
        self._name = name
        self._folder_id = folder_id
        self._emails = emails

    @classmethod
    def from_dict(cls, dikt) -> 'CreateListRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateListRequest of this CreateListRequest.  # noqa: E501
        :rtype: CreateListRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this CreateListRequest.

        Name of the list  # noqa: E501

        :return: The name of this CreateListRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this CreateListRequest.

        Name of the list  # noqa: E501

        :param name: The name of this CreateListRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def folder_id(self) -> str:
        """Gets the folder_id of this CreateListRequest.

        ID of the folder where the list will be created  # noqa: E501

        :return: The folder_id of this CreateListRequest.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id: str):
        """Sets the folder_id of this CreateListRequest.

        ID of the folder where the list will be created  # noqa: E501

        :param folder_id: The folder_id of this CreateListRequest.
        :type folder_id: str
        """
        if folder_id is None:
            raise ValueError("Invalid value for `folder_id`, must not be `None`")  # noqa: E501

        self._folder_id = folder_id

    @property
    def emails(self) -> List[str]:
        """Gets the emails of this CreateListRequest.

        List of emails to add to the list after creation  # noqa: E501

        :return: The emails of this CreateListRequest.
        :rtype: List[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails: List[str]):
        """Sets the emails of this CreateListRequest.

        List of emails to add to the list after creation  # noqa: E501

        :param emails: The emails of this CreateListRequest.
        :type emails: List[str]
        """

        self._emails = emails
