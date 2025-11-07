import django_filters
from .models import Instruction

class InstructionFilter(django_filters.FilterSet):
    # Filter fields for the Instruction model. Can filter by patient name, GP name, instruction type, and date range.
    # Each filter uses the related field's name and applies a case-insensitive contains lookup for string fields.
    
    instruction_type = django_filters.CharFilter(field_name='instruction_type__name', lookup_expr='icontains')

    patient_name = django_filters.CharFilter(field_name='patient__first_name', lookup_expr='icontains')    
    gp_name = django_filters.CharFilter(field_name='gp__name', lookup_expr='icontains')

    # The date fields, use greater than or equal (gte) and less than or equal (lte) lookups.
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')

    # Meta class to specify the model and fields that the filter will operate on.
    class Meta:
        model = Instruction
        fields = ['patient_name','gp_name','instruction_type', 'start_date', 'end_date']