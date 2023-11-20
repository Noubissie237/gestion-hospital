from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import fichForm
from .models import file_d_attente, patients, fiche_medicale, prescription
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from doctor_customer import settings
import datetime, hashlib

# Create your views here.

def formGet(request):
    if request.method == "POST":
        form = fichForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            getName = file_d_attente.objects.filter(numero__startswith='DEN', statut='False')
            person = getName[0]
            person.statut = 'True'
            getEmail = patients.objects.filter(email=person.email)
            mail=getEmail[0].email
            #Génération de l'adresse de la page
            code = mail.encode('utf-8')
            hasher = hashlib.sha256()
            hasher.update(code)
            cryptMail = hasher.hexdigest()
            LINK = "http://localhost:8000/profil/"+cryptMail
            PRESC = "http://localhost:8000/prescription/"+cryptMail
            #Fin

            # Génération du lien personnel
            post_data = request.POST.copy()
            post_data['lien'] = LINK
            form = fichForm(post_data)
            qrcode = prescription.objects.create(key=PRESC)

            nom=getEmail[0].nom
            subject = "SUIVI DE PRESCRIPTION"
            message = "Hey M./Mme {} retrouvez votre profil médical personel en cliquant sur le lien ci dessous \n {}\nRetrouvez egalement votre fiche de prescription soit cliquant sur ce lien : {}".format(nom, LINK, PRESC)
            from_email = settings.EMAIL_HOST_USER
            to_list = [mail]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            person.save()
            form.save()
            return HttpResponseRedirect(request.path)
    
    else:
        getName = file_d_attente.objects.filter(numero__startswith='DEN', statut='False')
        if getName.exists():       
            mail = getName[0].email
            getName = patients.objects.get(email=mail)
            nom = getName.nom
            Age = getName.age
        else:
            nom = 'Aucun patient'
            Age = 0
            
        initial_value = {}
        initial_value["nom_patient"] = nom
        initial_value["age"] = Age
        initial_value["prescription2"] = "R.A.S"
        initial_value["prescription3"] = "R.A.S"
        initial_value['lien'] = "lien de depart"
        form = fichForm(initial=initial_value)
    return render(request, "formulaire.html", {"form": form})

def profile(request, link_Id):
    elt = patients.objects.all()
    for i in range(len(elt)):
        email = elt[i].email
        code = email.encode('utf-8')
        hasher = hashlib.sha256()
        hasher.update(code)
        final = hasher.hexdigest()

        if final == link_Id:
            elt = patients.objects.get(email=email)
            lien = "http://localhost:8000/profil/"+link_Id
            tmp = "http://localhost:8000/prescription/"+link_Id
            test = prescription.objects.get(key=tmp)
            imgLink = str(test.qrcode)
            extract = "qr_img"+"/"
            imgLinkFinal = imgLink.replace(extract, '')
            lienImg = imgLinkFinal
            eltSuite = fiche_medicale.objects.get(lien=lien)
            if eltSuite:
                data = {
                    "date":datetime.date.today(),
                    "nom": elt.nom,
                    "prenom":elt.prenom,
                    "age":elt.age,
                    "poids":eltSuite.poids,
                    "sexe":elt.sexe,
                    "desc":eltSuite.description,
                    "presc1":eltSuite.prescription1,
                    "presc2":eltSuite.prescription2,
                    "presc3":eltSuite.prescription3,
                    "image":lienImg,
                }
                return render(request, 'patient.html', data)
    
    return render(request, 'katcentkat.html')

def presc(request, link_Id):
    elt = patients.objects.all()
    for i in range(len(elt)):
        email = elt[i].email
        code = email.encode('utf-8')
        hasher = hashlib.sha256()
        hasher.update(code)
        final = hasher.hexdigest()

        if final == link_Id:
            elt = patients.objects.get(email=email)
            lien = "http://localhost:8000/profil/"+link_Id
            eltPresc = fiche_medicale.objects.get(lien=lien)

            data = {
                "sexe": elt.sexe,
                "age":elt.age,
                "prescription1":eltPresc.prescription1,
                "prescription2":eltPresc.prescription2,
                "prescription3":eltPresc.prescription3,
            }

            return render(request, 'prescription.html', data)
    return render (request, 'katcentkat.html')