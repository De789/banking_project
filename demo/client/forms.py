# kyc/forms.py
from django import forms
from .models import KycDocument

class KycDocumentForm(forms.ModelForm):
    class Meta:
        model = KycDocument
        fields = ["id_proof_image", "selfie_image", "document_url"]
