# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponderRecipeSummary(object):
    """
    Summary of the ResponderRecipe.
    """

    #: A constant which can be used with the owner property of a ResponderRecipeSummary.
    #: This constant has a value of "CUSTOMER"
    OWNER_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the owner property of a ResponderRecipeSummary.
    #: This constant has a value of "ORACLE"
    OWNER_ORACLE = "ORACLE"

    #: A constant which can be used with the lifecycle_state property of a ResponderRecipeSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ResponderRecipeSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ResponderRecipeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ResponderRecipeSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ResponderRecipeSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ResponderRecipeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ResponderRecipeSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ResponderRecipeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ResponderRecipeSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ResponderRecipeSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ResponderRecipeSummary.
        :type description: str

        :param owner:
            The value to assign to the owner property of this ResponderRecipeSummary.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type owner: str

        :param responder_rules:
            The value to assign to the responder_rules property of this ResponderRecipeSummary.
        :type responder_rules: list[oci.cloud_guard.models.ResponderRecipeResponderRule]

        :param source_responder_recipe_id:
            The value to assign to the source_responder_recipe_id property of this ResponderRecipeSummary.
        :type source_responder_recipe_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ResponderRecipeSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ResponderRecipeSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ResponderRecipeSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ResponderRecipeSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ResponderRecipeSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ResponderRecipeSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ResponderRecipeSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ResponderRecipeSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'owner': 'str',
            'responder_rules': 'list[ResponderRecipeResponderRule]',
            'source_responder_recipe_id': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'owner': 'owner',
            'responder_rules': 'responderRules',
            'source_responder_recipe_id': 'sourceResponderRecipeId',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._owner = None
        self._responder_rules = None
        self._source_responder_recipe_id = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ResponderRecipeSummary.
        Identifier for ResponderRecipe.


        :return: The id of this ResponderRecipeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ResponderRecipeSummary.
        Identifier for ResponderRecipe.


        :param id: The id of this ResponderRecipeSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this ResponderRecipeSummary.
        ResponderRecipe Display Name


        :return: The display_name of this ResponderRecipeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ResponderRecipeSummary.
        ResponderRecipe Display Name


        :param display_name: The display_name of this ResponderRecipeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ResponderRecipeSummary.
        ResponderRecipe Description


        :return: The description of this ResponderRecipeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ResponderRecipeSummary.
        ResponderRecipe Description


        :param description: The description of this ResponderRecipeSummary.
        :type: str
        """
        self._description = description

    @property
    def owner(self):
        """
        Gets the owner of this ResponderRecipeSummary.
        Owner of ResponderRecipe

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The owner of this ResponderRecipeSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this ResponderRecipeSummary.
        Owner of ResponderRecipe


        :param owner: The owner of this ResponderRecipeSummary.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(owner, allowed_values):
            owner = 'UNKNOWN_ENUM_VALUE'
        self._owner = owner

    @property
    def responder_rules(self):
        """
        Gets the responder_rules of this ResponderRecipeSummary.
        List of responder rules associated with the recipe


        :return: The responder_rules of this ResponderRecipeSummary.
        :rtype: list[oci.cloud_guard.models.ResponderRecipeResponderRule]
        """
        return self._responder_rules

    @responder_rules.setter
    def responder_rules(self, responder_rules):
        """
        Sets the responder_rules of this ResponderRecipeSummary.
        List of responder rules associated with the recipe


        :param responder_rules: The responder_rules of this ResponderRecipeSummary.
        :type: list[oci.cloud_guard.models.ResponderRecipeResponderRule]
        """
        self._responder_rules = responder_rules

    @property
    def source_responder_recipe_id(self):
        """
        Gets the source_responder_recipe_id of this ResponderRecipeSummary.
        The id of the source responder recipe.


        :return: The source_responder_recipe_id of this ResponderRecipeSummary.
        :rtype: str
        """
        return self._source_responder_recipe_id

    @source_responder_recipe_id.setter
    def source_responder_recipe_id(self, source_responder_recipe_id):
        """
        Sets the source_responder_recipe_id of this ResponderRecipeSummary.
        The id of the source responder recipe.


        :param source_responder_recipe_id: The source_responder_recipe_id of this ResponderRecipeSummary.
        :type: str
        """
        self._source_responder_recipe_id = source_responder_recipe_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ResponderRecipeSummary.
        Compartment Identifier


        :return: The compartment_id of this ResponderRecipeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ResponderRecipeSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this ResponderRecipeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this ResponderRecipeSummary.
        The date and time the responder recipe was created. Format defined by RFC3339.


        :return: The time_created of this ResponderRecipeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ResponderRecipeSummary.
        The date and time the responder recipe was created. Format defined by RFC3339.


        :param time_created: The time_created of this ResponderRecipeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ResponderRecipeSummary.
        The date and time the responder recipe was updated. Format defined by RFC3339.


        :return: The time_updated of this ResponderRecipeSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ResponderRecipeSummary.
        The date and time the responder recipe was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this ResponderRecipeSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ResponderRecipeSummary.
        The current state of the Example.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ResponderRecipeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ResponderRecipeSummary.
        The current state of the Example.


        :param lifecycle_state: The lifecycle_state of this ResponderRecipeSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ResponderRecipeSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ResponderRecipeSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ResponderRecipeSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ResponderRecipeSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ResponderRecipeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ResponderRecipeSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ResponderRecipeSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ResponderRecipeSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ResponderRecipeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ResponderRecipeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ResponderRecipeSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ResponderRecipeSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ResponderRecipeSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ResponderRecipeSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ResponderRecipeSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ResponderRecipeSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
