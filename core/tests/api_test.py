from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from core.models import Instruction, Patient, GPSurgery, GP, InstructionType    

class InstructionsAPITest(APITestCase):

    # Test case for the Instructions API
    def setUp(self):
    
        # Create instances of GPSurgery, GP, Patient, InstructionType, and Instruction models, to test the API.
        self.surgery = GPSurgery.objects.create(name="Test Surgery")
        self.gp = GP.objects.create(name="Dr. Smith", surgery=self.surgery)
        self.patient = Patient.objects.create(first_name="Faith", last_name="Grace")
        self.instruction_type = InstructionType.objects.create(name="AMRA")
        
        self.instruction = Instruction.objects.create(
            instruction_type=self.instruction_type,
            patient=self.patient,
            gp=self.gp,
            surgery=self.surgery,
            date="2023-10-01"
        )
        
        # URL for the instructions API endpoint
        self.url = reverse('instructions') 

    # Test to check if the API returns the correct data
    def test_get_instructions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)