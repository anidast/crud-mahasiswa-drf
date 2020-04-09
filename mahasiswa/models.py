from django.db import models

def imageName(instance, filename):
	return '/'.join(['images', str(instance.nama), filename])

class Mahasiswa(models.Model):
	nrp = models.IntegerField(primary_key=True)
	nama = models.CharField(max_length=60)
	alamat = models.CharField(max_length=255)
	foto = models.ImageField(upload_to=imageName, max_length=255, blank=True, null=True)

	def __str__(self):
		return self.nama