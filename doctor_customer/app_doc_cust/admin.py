from django.contrib import admin
from .models import prescription, patients, services, fiche_medicale, file_d_attente

# Register your models here.
class AdminPrescription(admin.ModelAdmin):
    list_display = ("id", "key", "qrcode")

class AdminPatient(admin.ModelAdmin):
    list_display = ("nom", "prenom", "age", "sexe", "telephone", "email", "service")

class AdminServices(admin.ModelAdmin):
    list_display = ("nom",)

class AdminFiche(admin.ModelAdmin):
    list_display = ("nom_patient", "age", "poids", "description", "prescription1", "prescription2", "prescription3", "lien", "date_jour", )

class AdminFile(admin.ModelAdmin):
    list_display = ("email", "numero", "statut")


admin.site.register(prescription, AdminPrescription)
admin.site.register(patients, AdminPatient)
admin.site.register(services, AdminServices)
admin.site.register(fiche_medicale, AdminFiche)
admin.site.register(file_d_attente, AdminFile)