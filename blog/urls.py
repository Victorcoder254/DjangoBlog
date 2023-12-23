from django.urls import path
from .views import signupPage,landingPage, loginPage, logOut, detailPage

urlpatterns = [
    path('', landingPage,name="home"),
    path('<slug:slug>/', detailPage,name="detail"),
    path('signup//', signupPage,name="signup"),
    path('loginPage///', loginPage,name="login"),
    path('logout////', logOut,name="logout"),
]