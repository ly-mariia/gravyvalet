from rest_framework_json_api import serializers
from rest_framework_json_api.relations import HyperlinkedRelatedField

from addon_service.models import (
    ConfiguredStorageAddon,
    InternalResource,
)


RESOURCE_NAME = "internal-resources"


class InternalResourceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name=f"{RESOURCE_NAME}-detail")
    configured_storage_addons = HyperlinkedRelatedField(
        many=True,
        queryset=ConfiguredStorageAddon.objects.all(),
        related_link_view_name=f"{RESOURCE_NAME}-related",
        self_link_view_name=f"{RESOURCE_NAME}-relationships",
    )

    included_serializers = {
        "configured_storage_addons": (
            "addon_service.serializers.ConfiguredStorageAddonSerializer"
        ),
    }

    class Meta:
        model = InternalResource
        resource_name = RESOURCE_NAME
        fields = [
            "url",
            "resource_uri",
            "configured_storage_addons",
        ]