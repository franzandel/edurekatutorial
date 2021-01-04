from django.db.models import fields
from rest_framework import serializers
from .models import employee

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ('firstname', 'lastname')
        # fields = '__all__' # FOR ALL FIELDS