
"""
from django.shortcuts import render,reverse,redirect
from django.views.generic.edit import CreateView
from account.models import CustomUser
from django.contrib.auth import login, authenticate
from account.forms import CustomUserCreationForm,CustomUserChangeForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.


class CustomUSerCreationView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url=reverse_lazy('home')
    template_name ="account/signup.html"

    def form_valid(self,form):
        valid = super(CustomUSerCreationView,self).form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request,user)
            messages.success(self.request," {}  ".format(first_name) + " you are now logged in.")

        return valid 


    def dispatch(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('frontend'))
        return super(CustomUSerCreationView,self).dispatch(*args,**kwargs)







#Custom login view



class CustomLoginView(LoginView):
    form_class = LoginForm
    #success_url=reverse_lazy('home')
    next_page ="/"
    template_name ="registration/login.html"


    def form_valid(self, form):
        valid = super(CustomLoginView,self).form_valid(form)
        email = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(email = email ,password = password)
        if user is not None:
            login(self.request,user)
            messages.success(self.request,"Login successful !")
        
        return valid


    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('frontend'))
            
        return super(CustomLoginView,self).dispatch(*args, **kwargs)
    




class CustomLogoutView(LogoutView):
    next_page ="frontend/"
    template_name ="homepage.html"
"""