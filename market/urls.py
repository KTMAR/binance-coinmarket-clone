from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import index, LoginView, RegistrationView

urlpatterns = [
    path('', index, name='base'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
