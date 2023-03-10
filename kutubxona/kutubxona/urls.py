"""kutubxona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from kutub.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Bosh_sahifaView.as_view()),
    path("muallif/", MuallifView.as_view()),
    path("kitob/", KitobView.as_view()),
    path("talaba/", TalabaView.as_view()),
    path("adminview/", AdminView.as_view()),
    path("record/", RecordView.as_view()),
    # path("kitob/update/<int:pk>/", KitobUpdate.as_view()),
    # path("talaba/update/<int:pk>/", TalabaUpdate.as_view()),
    # path("muallif/update/<int:pk>/", MuallifUpdate.as_view())
]
