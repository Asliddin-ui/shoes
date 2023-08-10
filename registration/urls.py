from django.urls import path
from .views import UserRegistration, user_login, main_index, user_logout, update, about_user, settings

app_name = 'registration'

urlpatterns = [
    path('update/<int:id>/', update, name='update'),
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('aboutMe/<int:id>/', about_user, name='about'),
    path('settings/', settings, name='settings'),

]
