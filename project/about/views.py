from django.shortcuts import redirect, render

# Create your views here.
from . import forms,models


def home(request):
    consulta_about = models.About.objects.all()
    context = {"about": consulta_about}
    return render(request, "about/index.html", context)
def about_create(request):
    if request.method == 'POST':
        form = forms.AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about:home')
    else:
        form = forms.AboutForm()    
    return render(request,"about/about_create.html", context={"form": form})
