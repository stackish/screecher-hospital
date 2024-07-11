"""
from django.urls import path
from account.views import CustomLogoutView CustomUSerCreationView,CustomLoginView, 




urlpatterns = [
path('signup/',CustomUSerCreationView.as_view(),name="signup"),
path('login/',CustomLoginView.as_view(),name="login"),
path('logout/',CustomLogoutView.as_view(),name="logout"),
]
"""