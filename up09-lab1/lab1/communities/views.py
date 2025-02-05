from django.shortcuts import render,redirect
from .models import Communities
from django.contrib.auth.decorators import login_required
from . import forms 

# Create your views here.

def comms_list(req):
    comms = Communities.objects.all().order_by('-date')
    return render(req, 'communities/comms_list.html', {'comms': comms})

def comm_page(req, slug):
    comm = Communities.objects.get(slug=slug)
    return render(req, 'communities/comm_page.html', {'comm': comm})



@login_required(login_url="/users/login/")
def comm_new(request):
    if request.method == 'POST': 
        form = forms.CreateComm(request.POST, request.FILES) 
        if form.is_valid():
            newcomm = form.save(commit=False) 
            newcomm.author = request.user 
            newcomm.save()
            return redirect('comms:list')
    else:
        form = forms.CreateComm()
    return render(request, 'communities/new_comm.html', { 'form': form })