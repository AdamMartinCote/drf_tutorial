from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from drf_tutorial.snippets import views

urlpatterns = [
    path('', views.snippet_list),
    path('<int:pk>/', views.snippet_detail),
]

# Allows the generation of different content-type automatically
# using <pk>.json, <pk>.api
urlpatterns = format_suffix_patterns(urlpatterns)
