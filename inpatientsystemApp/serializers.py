from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id_bed', 'id_doctor', 'patient_department', 'first_name', 'last_name', 'date_of_birth', 'gender_patient')