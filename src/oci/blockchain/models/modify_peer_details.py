# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModifyPeerDetails(object):
    """
    peer to modify ocpu allocation
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModifyPeerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param peer_name:
            The value to assign to the peer_name property of this ModifyPeerDetails.
        :type peer_name: str

        :param ocpu_allocation_param:
            The value to assign to the ocpu_allocation_param property of this ModifyPeerDetails.
        :type ocpu_allocation_param: oci.blockchain.models.OcpuAllocationNumberParam

        """
        self.swagger_types = {
            'peer_name': 'str',
            'ocpu_allocation_param': 'OcpuAllocationNumberParam'
        }

        self.attribute_map = {
            'peer_name': 'peerName',
            'ocpu_allocation_param': 'ocpuAllocationParam'
        }

        self._peer_name = None
        self._ocpu_allocation_param = None

    @property
    def peer_name(self):
        """
        **[Required]** Gets the peer_name of this ModifyPeerDetails.
        peer identifier


        :return: The peer_name of this ModifyPeerDetails.
        :rtype: str
        """
        return self._peer_name

    @peer_name.setter
    def peer_name(self, peer_name):
        """
        Sets the peer_name of this ModifyPeerDetails.
        peer identifier


        :param peer_name: The peer_name of this ModifyPeerDetails.
        :type: str
        """
        self._peer_name = peer_name

    @property
    def ocpu_allocation_param(self):
        """
        **[Required]** Gets the ocpu_allocation_param of this ModifyPeerDetails.

        :return: The ocpu_allocation_param of this ModifyPeerDetails.
        :rtype: oci.blockchain.models.OcpuAllocationNumberParam
        """
        return self._ocpu_allocation_param

    @ocpu_allocation_param.setter
    def ocpu_allocation_param(self, ocpu_allocation_param):
        """
        Sets the ocpu_allocation_param of this ModifyPeerDetails.

        :param ocpu_allocation_param: The ocpu_allocation_param of this ModifyPeerDetails.
        :type: oci.blockchain.models.OcpuAllocationNumberParam
        """
        self._ocpu_allocation_param = ocpu_allocation_param

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
