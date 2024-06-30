from rest_framework import serializers
from apiapp.models import Employe

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields='__all__'