from rest_framework.serializers import ModelSerializer
from base.models import Player


class PlayerSerializaer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'