from .models import User, Treatment, Symptom, FavoriteList
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treatment
        fields = '__all__'

class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        fields = '__all__'

class FavoriteListSerializer(serializers.ModelSerializer):

    class Meta:
        #view_name = 'favoriteList-detail'
        model = FavoriteList
        fields = '__all__'