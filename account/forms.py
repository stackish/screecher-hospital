from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from account.models import CustomUser
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm




class CustomUserCreationForm(UserCreationForm):
    pass
    # Validations
    """
    email = forms.EmailField(label="Email address",min_length=8,max_length=50,validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message="Put a valid email address")],
    widget=forms.EmailInput(attrs={'placeholder':'Email address'}))

    first_name = forms.CharField(label="First name",min_length=3,max_length=50,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],
    required=True,
    widget=forms.TextInput(attrs={'placeholder':'First name'}))

    last_name = forms.CharField(label="Last name",min_length=3,max_length=50,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],
    required=True,
    widget=forms.TextInput(attrs={'placeholder':'Last name'}))

    username = forms.CharField(label="Username",min_length=3,max_length=50,validators=[RegexValidator(r'^[a-zA-Z\s]+[0-9]*$',message="Only letters and numbers are allowed")],
    
    widget=forms.TextInput(attrs={'placeholder':'Username'}))
    
   
    

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ["email","first_name","last_name","username","password1","password2"]

       # widgets = {
       #     'phone_number': forms.TextInput(attrs={'style':'font-size:13px','placeholder':'Phone','data-mask':'(000) 000-000-0000'})
       # }


    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        return email.lower()

    #Super functions
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm password'})
    """

class CustomUserChangeForm(UserChangeForm):
    #upon change the email is returned as lowercase
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        
        return email.lower()

    #upon change the username is returned as lowercase
    def clean_username(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        return username.lower()



"""
     # Validations
    email = forms.CharField(label="Email address",min_length=8,max_length=50,validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message="Put a valid email address")],
    widget=forms.TextInput(attrs={'placeholder':'Email address'}))

    first_name = forms.CharField(label="First name",min_length=3,max_length=50,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],
    required=True,
    widget=forms.TextInput(attrs={'placeholder':'First name'}))

    last_name = forms.CharField(label="Last name",min_length=3,max_length=50,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],
    required=True,
    widget=forms.TextInput(attrs={'placeholder':'Last name'}))

    username = forms.CharField(label="Username",min_length=3,max_length=50,validators=[RegexValidator(r'^[a-zA-Z\s]+[0-9]*$',message="Only letters and numbers are allowed")],
    
    widget=forms.TextInput(attrs={'placeholder':'Username'}))

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ["first_name","last_name"]

        widgets = {
            'phone_number': forms.TextInput(attrs={'style':'font-size:13px','placeholder':'Phone Number','data-mask':'(000) 000-000-0000'})
        }


    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        return email.lower()


   


    








class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email address",min_length=8,max_length=50,validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message="Put a valid email address")],
    widget=forms.TextInput(attrs={'placeholder':'Email address'}))

  
     # Validations


    

    
    class Meta(AuthenticationForm):
        model = CustomUser
        fields = ["email","password"]


    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        return email.lower()



    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password'].widget.attrs.update({'placeholder':'Password'})

  

"""

   


    




