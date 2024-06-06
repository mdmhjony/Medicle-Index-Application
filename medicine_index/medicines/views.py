from rest_framework import viewsets, permissions
from .models import Medicine
from .serializers import MedicineSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import models


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(models.Q(name__icontains=search) | models.Q(generic_name__icontains=search))
        return queryset


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def insert_medicine(request):
    serializer = MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_medicine(request, pk):
    try:
        medicine = Medicine.objects.get(pk=pk)
    except Medicine.DoesNotExist:
        return Response(status=404)
    serializer = MedicineSerializer(medicine, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_medicine(request, pk):
    try:
        medicine = Medicine.objects.get(pk=pk)
    except Medicine.DoesNotExist:
        return Response(status=404)
    medicine.delete()
    return Response(status=204)

@api_view(['GET'])
def fetch_all_medicines(request):
    medicines = Medicine.objects.all()
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def fetch_medicine_by_id(request, pk):
    try:
        medicine = Medicine.objects.get(pk=pk)
    except Medicine.DoesNotExist:
        return Response(status=404)
    serializer = MedicineSerializer(medicine)
    return Response(serializer.data)


@api_view(['GET'])
def search_medicines(request, query):
    medicines = Medicine.objects.filter(models.Q(name__icontains=query) | models.Q(generic_name__icontains=query))
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data)
