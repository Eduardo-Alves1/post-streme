from rest_framework import serializers
from publi.models import PubliModel


class PubliSerializer(serializers.ModelSerializer):
    class Meta:
        model = PubliModel
        fields = "__all__"
