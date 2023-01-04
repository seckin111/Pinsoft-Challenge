from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path('Minesweeper/', views.minesweeper),
    path('Calculator/', views.calculator),
    path('Home/', views.home),

]