from rest_framework import serializers
from tutorials.models import Tutorial

# Serializer pour le modèle Tutorial
class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = (
            'id',
            'title',
            'description',
            'published',
        )

# Serializer pour un autre modèle utilisateur (supposé)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial  # Remplacez Tutorial par le modèle correct, par exemple User.
        fields = (
            'login',
            'pwd',
        )
