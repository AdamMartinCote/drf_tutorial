from django.urls import path

from drf_tutorial.snippets import views

urlpatterns = [
    path('', views.snippet_list),
    path('<int:pk>/', views.snippet_detail),
]
