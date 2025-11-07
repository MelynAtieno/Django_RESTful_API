from django.http import HttpResponse
from rest_framework import viewsets, status 
from rest_framework.response import Response
from .models import Instruction
from .serializers import InstructionSerializer
from .filters import InstructionFilter


def sample_view(request):
    return HttpResponse("A sample response from the core app.")

class InstructionViewSet(viewsets.ViewSet):
    
    # List all instructions with filtering capabilities
    # GET /instructions/
    def list(self, request):
        queryset = Instruction.objects.all()

        # Filtering logic
        filtered_queryset = InstructionFilter(request.query_params, queryset=queryset).qs

        serializer = InstructionSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    # Retrieve a specific instruction by ID
    # GET /instructions/{id}/
    def retrieve(self, request, pk=None):
        try:
            instruction = Instruction.objects.get(pk=pk)
            serializer = InstructionSerializer(instruction)
            return Response(serializer.data)
        except Instruction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Create a new instruction
    # POST /instructions/
    def create(self, request):
        serializer = InstructionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    