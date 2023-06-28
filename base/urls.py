from django.urls import path
from .views import CreateLiftView, LiftView

urlpatterns =[
     path('lift/',LiftView.as_view()),
    path('create/', CreateLiftView.as_view())
]
