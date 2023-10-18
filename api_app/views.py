from rest_framework import viewsets
from .serializers import AppleCeoSerializer
from .models import AppleCeo

# Create your views here.
class CeoViewSet(viewsets.ModelViewSet):
    queryset = AppleCeo.objects.all().order_by('-first_year_active')
    serializer_class = AppleCeoSerializer
    