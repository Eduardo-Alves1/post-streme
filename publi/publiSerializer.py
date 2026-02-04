from rest_framework import serializers
from publi.models import PubliModel


class PubliSerializer(serializers.ModelSerializer):
    class Meta:
        model = PubliModel
        fields = "__all__"
        # exclude = ["criado_em"]

    def validate_conteudo(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                "O conteúdo não deve ser maior que 200 caracteres."
            )
        return value
