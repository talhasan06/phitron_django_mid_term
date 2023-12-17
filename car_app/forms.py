from django import forms 
from . models import Car,Brand,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = '__all__'
        exclude=['author']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        exclude = ['slug']

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['name','body']
        
class ChangeUserForm(UserChangeForm):
    class Meta:
        password=None
        model =User
        fields=['username','first_name','last_name']

