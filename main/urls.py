from django.urls import path
from main.views import show_main
from main.views import signup
from main.views import login_user
from main.views import logout_user
from main.views import show_catalog

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('catalog/', show_catalog, name='show_catalog')

]