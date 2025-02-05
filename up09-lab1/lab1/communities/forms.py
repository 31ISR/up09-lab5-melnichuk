from django import forms 
from . import models 

class CreateComm(forms.ModelForm): 
    class Meta: 
        model = models.Communities
        fields = ['name','description','slug','banner']