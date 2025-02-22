# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SupportedHostShapeSummary(object):
    """
    A specific compute shape supported by the Oracle Cloud VMware Solution.
    """

    #: A constant which can be used with the supported_operations property of a SupportedHostShapeSummary.
    #: This constant has a value of "CREATE_SDDC"
    SUPPORTED_OPERATIONS_CREATE_SDDC = "CREATE_SDDC"

    #: A constant which can be used with the supported_operations property of a SupportedHostShapeSummary.
    #: This constant has a value of "DELETE_SDDC"
    SUPPORTED_OPERATIONS_DELETE_SDDC = "DELETE_SDDC"

    #: A constant which can be used with the supported_operations property of a SupportedHostShapeSummary.
    #: This constant has a value of "CREATE_ESXI_HOST"
    SUPPORTED_OPERATIONS_CREATE_ESXI_HOST = "CREATE_ESXI_HOST"

    #: A constant which can be used with the supported_operations property of a SupportedHostShapeSummary.
    #: This constant has a value of "DELETE_ESXI_HOST"
    SUPPORTED_OPERATIONS_DELETE_ESXI_HOST = "DELETE_ESXI_HOST"

    #: A constant which can be used with the supported_operations property of a SupportedHostShapeSummary.
    #: This constant has a value of "UPGRADE_HCX"
    SUPPORTED_OPERATIONS_UPGRADE_HCX = "UPGRADE_HCX"

    #: A constant which can be used with the supported_operations property of a SupportedHostShapeSummary.
    #: This constant has a value of "DOWNGRADE_HCX"
    SUPPORTED_OPERATIONS_DOWNGRADE_HCX = "DOWNGRADE_HCX"

    #: A constant which can be used with the supported_operations property of a SupportedHostShapeSummary.
    #: This constant has a value of "CANCEL_DOWNGRADE_HCX"
    SUPPORTED_OPERATIONS_CANCEL_DOWNGRADE_HCX = "CANCEL_DOWNGRADE_HCX"

    #: A constant which can be used with the supported_operations property of a SupportedHostShapeSummary.
    #: This constant has a value of "REFRESH_HCX_LICENSE_STATUS"
    SUPPORTED_OPERATIONS_REFRESH_HCX_LICENSE_STATUS = "REFRESH_HCX_LICENSE_STATUS"

    #: A constant which can be used with the supported_sddc_types property of a SupportedHostShapeSummary.
    #: This constant has a value of "PRODUCTION"
    SUPPORTED_SDDC_TYPES_PRODUCTION = "PRODUCTION"

    #: A constant which can be used with the supported_sddc_types property of a SupportedHostShapeSummary.
    #: This constant has a value of "NON_PRODUCTION"
    SUPPORTED_SDDC_TYPES_NON_PRODUCTION = "NON_PRODUCTION"

    def __init__(self, **kwargs):
        """
        Initializes a new SupportedHostShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SupportedHostShapeSummary.
        :type name: str

        :param supported_operations:
            The value to assign to the supported_operations property of this SupportedHostShapeSummary.
            Allowed values for items in this list are: "CREATE_SDDC", "DELETE_SDDC", "CREATE_ESXI_HOST", "DELETE_ESXI_HOST", "UPGRADE_HCX", "DOWNGRADE_HCX", "CANCEL_DOWNGRADE_HCX", "REFRESH_HCX_LICENSE_STATUS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type supported_operations: list[str]

        :param shape_family:
            The value to assign to the shape_family property of this SupportedHostShapeSummary.
        :type shape_family: str

        :param default_ocpu_count:
            The value to assign to the default_ocpu_count property of this SupportedHostShapeSummary.
        :type default_ocpu_count: float

        :param supported_ocpu_count:
            The value to assign to the supported_ocpu_count property of this SupportedHostShapeSummary.
        :type supported_ocpu_count: list[float]

        :param supported_sddc_types:
            The value to assign to the supported_sddc_types property of this SupportedHostShapeSummary.
            Allowed values for items in this list are: "PRODUCTION", "NON_PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type supported_sddc_types: list[str]

        :param description:
            The value to assign to the description property of this SupportedHostShapeSummary.
        :type description: str

        :param is_support_shielded_instances:
            The value to assign to the is_support_shielded_instances property of this SupportedHostShapeSummary.
        :type is_support_shielded_instances: bool

        """
        self.swagger_types = {
            'name': 'str',
            'supported_operations': 'list[str]',
            'shape_family': 'str',
            'default_ocpu_count': 'float',
            'supported_ocpu_count': 'list[float]',
            'supported_sddc_types': 'list[str]',
            'description': 'str',
            'is_support_shielded_instances': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'supported_operations': 'supportedOperations',
            'shape_family': 'shapeFamily',
            'default_ocpu_count': 'defaultOcpuCount',
            'supported_ocpu_count': 'supportedOcpuCount',
            'supported_sddc_types': 'supportedSddcTypes',
            'description': 'description',
            'is_support_shielded_instances': 'isSupportShieldedInstances'
        }

        self._name = None
        self._supported_operations = None
        self._shape_family = None
        self._default_ocpu_count = None
        self._supported_ocpu_count = None
        self._supported_sddc_types = None
        self._description = None
        self._is_support_shielded_instances = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SupportedHostShapeSummary.
        The name of the supported compute shape.


        :return: The name of this SupportedHostShapeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SupportedHostShapeSummary.
        The name of the supported compute shape.


        :param name: The name of this SupportedHostShapeSummary.
        :type: str
        """
        self._name = name

    @property
    def supported_operations(self):
        """
        **[Required]** Gets the supported_operations of this SupportedHostShapeSummary.
        The operations where you can use the shape. The operations can be CREATE_SDDC or CREATE_ESXI_HOST.

        Allowed values for items in this list are: "CREATE_SDDC", "DELETE_SDDC", "CREATE_ESXI_HOST", "DELETE_ESXI_HOST", "UPGRADE_HCX", "DOWNGRADE_HCX", "CANCEL_DOWNGRADE_HCX", "REFRESH_HCX_LICENSE_STATUS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The supported_operations of this SupportedHostShapeSummary.
        :rtype: list[str]
        """
        return self._supported_operations

    @supported_operations.setter
    def supported_operations(self, supported_operations):
        """
        Sets the supported_operations of this SupportedHostShapeSummary.
        The operations where you can use the shape. The operations can be CREATE_SDDC or CREATE_ESXI_HOST.


        :param supported_operations: The supported_operations of this SupportedHostShapeSummary.
        :type: list[str]
        """
        allowed_values = ["CREATE_SDDC", "DELETE_SDDC", "CREATE_ESXI_HOST", "DELETE_ESXI_HOST", "UPGRADE_HCX", "DOWNGRADE_HCX", "CANCEL_DOWNGRADE_HCX", "REFRESH_HCX_LICENSE_STATUS"]
        if supported_operations:
            supported_operations[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in supported_operations]
        self._supported_operations = supported_operations

    @property
    def shape_family(self):
        """
        **[Required]** Gets the shape_family of this SupportedHostShapeSummary.
        The family of the shape. ESXi hosts of one SDDC must have the same shape family.


        :return: The shape_family of this SupportedHostShapeSummary.
        :rtype: str
        """
        return self._shape_family

    @shape_family.setter
    def shape_family(self, shape_family):
        """
        Sets the shape_family of this SupportedHostShapeSummary.
        The family of the shape. ESXi hosts of one SDDC must have the same shape family.


        :param shape_family: The shape_family of this SupportedHostShapeSummary.
        :type: str
        """
        self._shape_family = shape_family

    @property
    def default_ocpu_count(self):
        """
        Gets the default_ocpu_count of this SupportedHostShapeSummary.
        The default OCPU count of the shape.


        :return: The default_ocpu_count of this SupportedHostShapeSummary.
        :rtype: float
        """
        return self._default_ocpu_count

    @default_ocpu_count.setter
    def default_ocpu_count(self, default_ocpu_count):
        """
        Sets the default_ocpu_count of this SupportedHostShapeSummary.
        The default OCPU count of the shape.


        :param default_ocpu_count: The default_ocpu_count of this SupportedHostShapeSummary.
        :type: float
        """
        self._default_ocpu_count = default_ocpu_count

    @property
    def supported_ocpu_count(self):
        """
        Gets the supported_ocpu_count of this SupportedHostShapeSummary.
        Support OCPU count of the shape.


        :return: The supported_ocpu_count of this SupportedHostShapeSummary.
        :rtype: list[float]
        """
        return self._supported_ocpu_count

    @supported_ocpu_count.setter
    def supported_ocpu_count(self, supported_ocpu_count):
        """
        Sets the supported_ocpu_count of this SupportedHostShapeSummary.
        Support OCPU count of the shape.


        :param supported_ocpu_count: The supported_ocpu_count of this SupportedHostShapeSummary.
        :type: list[float]
        """
        self._supported_ocpu_count = supported_ocpu_count

    @property
    def supported_sddc_types(self):
        """
        Gets the supported_sddc_types of this SupportedHostShapeSummary.
        The supported SDDC types for the shape.

        Allowed values for items in this list are: "PRODUCTION", "NON_PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The supported_sddc_types of this SupportedHostShapeSummary.
        :rtype: list[str]
        """
        return self._supported_sddc_types

    @supported_sddc_types.setter
    def supported_sddc_types(self, supported_sddc_types):
        """
        Sets the supported_sddc_types of this SupportedHostShapeSummary.
        The supported SDDC types for the shape.


        :param supported_sddc_types: The supported_sddc_types of this SupportedHostShapeSummary.
        :type: list[str]
        """
        allowed_values = ["PRODUCTION", "NON_PRODUCTION"]
        if supported_sddc_types:
            supported_sddc_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in supported_sddc_types]
        self._supported_sddc_types = supported_sddc_types

    @property
    def description(self):
        """
        Gets the description of this SupportedHostShapeSummary.
        Description of the shape.


        :return: The description of this SupportedHostShapeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SupportedHostShapeSummary.
        Description of the shape.


        :param description: The description of this SupportedHostShapeSummary.
        :type: str
        """
        self._description = description

    @property
    def is_support_shielded_instances(self):
        """
        Gets the is_support_shielded_instances of this SupportedHostShapeSummary.
        Indicates whether the shape supports shielded instances.


        :return: The is_support_shielded_instances of this SupportedHostShapeSummary.
        :rtype: bool
        """
        return self._is_support_shielded_instances

    @is_support_shielded_instances.setter
    def is_support_shielded_instances(self, is_support_shielded_instances):
        """
        Sets the is_support_shielded_instances of this SupportedHostShapeSummary.
        Indicates whether the shape supports shielded instances.


        :param is_support_shielded_instances: The is_support_shielded_instances of this SupportedHostShapeSummary.
        :type: bool
        """
        self._is_support_shielded_instances = is_support_shielded_instances

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
