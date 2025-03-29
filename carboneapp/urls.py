from django.urls import path
from .views import home, login_view, logout_view

app_name = 'carboneapp'

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]