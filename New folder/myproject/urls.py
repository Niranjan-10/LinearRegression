
from django.urls import path
from . import views

urlpatterns = [
    path('', views.linearRegression),
    # path('', include('myproject.urls'))
]
