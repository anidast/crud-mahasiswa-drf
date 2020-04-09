from django.urls import path

from .views import MahasiswaView, MahasiswaRUDView

app_name = "mahasiswa"

urlpatterns = [
	path('mahasiswa/<int:nrp>', MahasiswaRUDView.as_view()),
	path('mahasiswa/', MahasiswaView.as_view()),
]