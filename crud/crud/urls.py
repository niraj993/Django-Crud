"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import view
from django.conf import settings
from django.conf.urls.static import static
from configs.routs import ADD_BOOK_ROUTE,EDIT_BOOK_ROUTE,DELETE_BOOK_ROUTE,AUTH_ROUTE



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",view.home,name="home"),
    path(AUTH_ROUTE,include("accounts.urls")),
    path(ADD_BOOK_ROUTE,view.add_book,name="add_book"),
    path(EDIT_BOOK_ROUTE,view.edit_book,name="edit_book"),
    path(DELETE_BOOK_ROUTE,view.delete_book,name="delete_book"),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
