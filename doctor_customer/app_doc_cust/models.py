from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw 

# Create your models here.

#   Table de prescription + generation du QR CODE
class prescription(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=1500)
    qrcode = models.ImageField(upload_to='qr_img', null=True, blank=True)

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.key)
        canvas = Image.new('RGB', (qr_image.pixel_size, qr_image.pixel_size), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        file_name = f"{self.key}.png"
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcode.save(file_name, File(buffer), save=False)
        canvas.close()
        return super().save(*args, **kwargs)
    
    def __int__(self):
        return self.id
    
    class Meta:
        db_table = 'prescription'
        verbose_name = "prescription"
        verbose_name_plural = ("prescriptions")

#   Choix de sexe
class tsexe(models.Model):
    choix = models.CharField(max_length=1)

    def __str__(self):
        return self.choix

    class Meta:
        db_table = 'tsexe'

#   Choix du service
class services(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'services'
        verbose_name = "service"
        verbose_name_plural = "services"

#   Table des patients
class patients(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField()
    sexe = models.ForeignKey(tsexe, null=True, on_delete=models.SET_NULL)
    telephone = models.IntegerField()
    email = models.EmailField(max_length=254, unique=True)
    service = models.ForeignKey(services, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'patients'
        verbose_name = ("patient")
        verbose_name_plural = ("patients")

#   Ordre de passage
class file_d_attente(models.Model):
    email = models.ForeignKey(patients, on_delete=models.SET_NULL, null=True, to_field='email')
    numero = models.CharField(null=False)
    statut = models.BooleanField(null=False, default=False)

    def __int__(self):
        return self.nom
    
    class Meta:
        db_table = 'file_d_attente'
        verbose_name = 'file_d_attente'
        verbose_name_plural = 'file_d_attentes'

#   Fiche medicale
class fiche_medicale(models.Model):
    nom_patient = models.CharField(null=False, default="")
    age = models.IntegerField(null=True)
    poids = models.IntegerField(null=True)
    description = models.TextField(max_length=500)
    prescription1 = models.CharField(max_length=50)
    prescription2 = models.CharField(max_length=50, null=True, default='Vide')
    prescription3 = models.CharField(max_length=50, null=True, default='Vide')
    lien = models.CharField(max_length=300)
    date_jour = models.DateField(auto_now_add=True)

    def __int__(self):
        return self.nom_patient
    
    class Meta:
        db_table = 'fiche_medicale'
        verbose_name = "fiche_medicale"
        verbose_name_plural = "fiche_medicales"
