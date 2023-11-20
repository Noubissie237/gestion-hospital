from django import forms
from .models import fiche_medicale

class fichForm(forms.ModelForm):
    class Meta:
        model = fiche_medicale
        fields = [
            "nom_patient",
            "age",
            "poids",
            "description",
            "prescription1",
            "prescription2",
            "prescription3",
            "lien",
        ]

        labels = {
            "nom_patient": "Nom",
            "lien": "",
            }
        widgets = {
            "date_naiss": forms.SelectDateWidget(years=range(1923, 2023)),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom_patient'].widget.attrs.update({'class': 'form-control text-primary mt-2 mb-2',})
        self.fields['age'].widget.attrs.update({'class': 'form-control text-primary mt-2 mb-2 col-4',})
        self.fields['poids'].widget.attrs.update({'class': 'form-control mt-2 mb-2 col-4',})
        self.fields['description'].widget.attrs.update({'class': 'form-control',})
        self.fields['prescription1'].widget.attrs.update({'class': 'form-control mt-2 mb-2',})
        self.fields['prescription2'].widget.attrs.update({'class': 'form-control mt-2 mb-2',})
        self.fields['prescription3'].widget.attrs.update({'class': 'form-control mt-2 mb-2',})
        self.fields['lien'].widget.attrs.update({'class': 'form-control mt-2 mb-2',})
