"""one_last_try URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from topics.views import topic_view,home_view,detail_view,form_view,entryform_view,edit_view
from users.views import logout_view, register_view
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view , name='home'),
    path('topic/', topic_view, name='topic'),
    path('topic/<int:id>/', detail_view, name='detail'),
    path('new_topic/', form_view, name='new_topic'),
    path('new_topic/<int:id>/', entryform_view, name='new_entry' ),
    path('edit_entry/<entry_id>', edit_view, name='edit'),
    path('users/',LoginView.as_view(template_name='users.html'),name= 'user'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register')
]
