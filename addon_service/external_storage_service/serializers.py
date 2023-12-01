from rest_framework_json_api import serializers
from rest_framework_json_api.relations import HyperlinkedRelatedField

from addon_service.models import (
    AuthorizedStorageAccount,
    ExternalStorageService,
)


RESOURCE_NAME = ExternalStorageService.JSONAPIMeta.resource_name


class ExternalStorageServiceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name=f"{RESOURCE_NAME}-detail")

    authorized_storage_accounts = HyperlinkedRelatedField(
        many=True,
        queryset=AuthorizedStorageAccount.objects.all(),
        related_link_view_name=f"{RESOURCE_NAME}-related",
        self_link_view_name=f"{RESOURCE_NAME}-relationships",
    )

    included_serializers = {
        "authorized_storage_accounts": (
            "addon_service.serializers.AuthorizedStorageAccountSerializer"
        ),
    }

    class Meta:
        model = ExternalStorageService
        fields = [
            "url",
            "max_concurrent_downloads",
            "max_upload_mb",
            "auth_uri",
            "authorized_storage_accounts",
        ]