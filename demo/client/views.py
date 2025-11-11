# kyc/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import KycDocumentForm
from .models import KycDocument

@login_required
def upload_kyc(request):
    # if user already has a pending one, you might want to show/edit it instead
    if request.method == "POST":
        form = KycDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            kyc = form.save(commit=False)
            kyc.user = request.user
            kyc.save()
            return redirect("kyc_detail", pk=kyc.pk)
    else:
        form = KycDocumentForm()
    return render(request, "kyc/upload.html", {"form": form})

@login_required
def kyc_detail(request, pk):
    kyc = get_object_or_404(KycDocument, pk=pk, user=request.user)
    return render(request, "kyc/detail.html", {"kyc": kyc})

@login_required
def my_kyc_list(request):
    items = KycDocument.objects.filter(user=request.user).order_by("-submitted_at")
    return render(request, "kyc/list.html", {"items": items})
