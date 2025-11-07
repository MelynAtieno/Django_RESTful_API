from rest_framework import serializers
from .models import Instruction, GPSurgery, GP, Patient, InstructionType


# Serializer for the patient model
class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    # Combine patient's first and last name into full name
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    class Meta:
        model = Patient
        fields = [ 'id', 'full_name']

# Serializer for GPSurgery model
class GPSurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSurgery
        fields = ['id', 'name']

# Serializer for GP model, including the related GPSurgery
class GPSerializer(serializers.ModelSerializer):
    surgery = GPSurgerySerializer()

    class Meta:
        model = GP
        fields = ['id', 'name', 'surgery']

# Serializer for InstructionType model
class InstructionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionType
        fields = ['id', 'name']

# Serializer for Instruction model, including related models
class InstructionSerializer(serializers.ModelSerializer):  
    instruction_id = serializers.IntegerField(source='id', read_only=True)  
    patient = PatientSerializer()
    instruction_type = InstructionTypeSerializer()
    gp = GPSerializer()
    
    #surgery = GPSurgerySerializer() -> The surgery details are nested within GP serializer. Uncomment if you want to include surgery in the output.
    
    # Fields to be included in the serialized output
    class Meta:
        model = Instruction
        fields = [
            'instruction_id', 
            'date',
            'patient',
            'instruction_type', 
            'gp'
            ]
