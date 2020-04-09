# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Mahasiswa
from .serializers import MahasiswaSerializer

class MahasiswaView(ListCreateAPIView):
	queryset = Mahasiswa.objects.all()
	serializer_class = MahasiswaSerializer

class MahasiswaRUDView(RetrieveUpdateDestroyAPIView):
	lookup_field = 'nrp'
	queryset = Mahasiswa.objects.all()
	serializer_class = MahasiswaSerializer