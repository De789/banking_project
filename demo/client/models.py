from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class KycDocument(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="kyc_documents"
    )
    id_proof_image = models.ImageField(upload_to="kyc/id_proofs/", null=True, blank=True)
    selfie_image = models.ImageField(upload_to="kyc/selfies/", null=True, blank=True)
    document_url = models.URLField(max_length=1024, blank=True, null=True)
    verified = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"KYC #{self.pk} for {self.user}"
