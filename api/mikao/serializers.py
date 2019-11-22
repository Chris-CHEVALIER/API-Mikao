from .models import User, Treatment, Symptom, FavoriteList
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TreatmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'

class SymptomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'

class FavoriteListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #view_name = 'favoriteList-detail'
        model = FavoriteList
        fields = '__all__'