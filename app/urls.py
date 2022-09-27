from django.urls import path
from .views import HomeView, MainView


urlpatterns = [
    path('', HomeView.as_view()),
    path('<int:pk>/', MainView.as_view())
]
