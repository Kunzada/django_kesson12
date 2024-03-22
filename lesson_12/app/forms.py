from django import forms 
from .models import CustomUser 

class UserForm(forms.ModelForm):
    class Meta:
        model=CustomUser 
        fields=['fio','age','status']
        widgets={
            'fio':forms.TextInput(attrs={'class':'title'})
        }