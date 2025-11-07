from django.urls import path, include
from .views import sample_view
from .views import InstructionViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'instructions', InstructionViewSet, basename='instruction')


urlpatterns = [
    path('sample/', sample_view, name='sample'), # Sample view for testing

    # Register the InstructionViewSet with the router    
    path('', include(router.urls)),
   
]