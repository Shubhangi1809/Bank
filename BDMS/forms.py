from django.forms import ModelForm
from .models import Project
from  django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class Profile(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ["Profile_Pic","FullName","PhoneNo","Age","city","State","Country"]




class ProjectForm(UserCreationForm):
    email = forms.EmailField(label= "Email")
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]




class ProjectForms(ModelForm):
    class Meta:
        model = Project
        fields = ["Profile_Pic","FullName","PhoneNo","Age","city","State","Country"]

class UserLoginForm(forms.Form):
    Username=forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        Username= self.cleaned_data.get('Username')
        Password = self.cleaned_data.get('Password')


        if Username and Password:
            user = authenticate(Username= Username, Password= Password)
            if not user:
                raise forms.ValidationError("This User Does Not Exist!!!")
            if not user.check-Password(Password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This User Is Not Active!!!")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserUpdate(forms.ModelForm):
    email = forms.EmailField(label= "Email")
    def __init__(self, *args, **kwargs):
        super(UserUpdate, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None


    class Meta:
        model = User
        fields = ["username", "email"]
    





