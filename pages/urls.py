
from django.urls import path
from .views.index_view import IndexView
from .views.about_view import AboutView

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('about/', AboutView.as_view(), name='about'),
]