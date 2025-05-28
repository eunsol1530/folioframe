from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hackathon
from .serializers import HackathonSerializer

@api_view(['POST'])
def create_hackathon(request):
    serializer = HackathonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
