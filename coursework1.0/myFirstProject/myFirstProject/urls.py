from django.contrib import admin
from django.urls import path, include
from graph import views as graph_views
from django.contrib.auth import views as auth_views
from graph.forms import CustomLoginForm

urlpatterns = [
    path('', graph_views.index, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', graph_views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=CustomLoginForm), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('graphs/', include('graph.urls')),
]
