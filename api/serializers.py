# api/serializers.py
from rest_framework import serializers
from .models import AppSetting, AddTransaction

class AppSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSetting
        fields = ['currency']
class AddtransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddTransaction
        fields = '__all__'