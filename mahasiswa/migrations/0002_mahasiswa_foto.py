# Generated by Django 3.0.5 on 2020-04-09 07:03

from django.db import migrations, models
import mahasiswa.models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahasiswa',
            name='foto',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=mahasiswa.models.imageName),
        ),
    ]
