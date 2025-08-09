from django.urls import path
from .views import OrchestratorView

urlpatterns = [
    path('orchestrate/<str:service_name>/', OrchestratorView.as_view()),
]