# kyc/admin.py
from django.contrib import admin
from .models import KycDocument

@admin.register(KycDocument)
class KycDocumentAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "verified", "submitted_at")
    list_filter = ("verified", "submitted_at")
    readonly_fields = ("submitted_at", "updated_at")
