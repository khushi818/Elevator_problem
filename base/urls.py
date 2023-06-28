from django.urls import path
from .views import CreateLiftView, LiftView,ElevatorUpView,ElevatorDownView

urlpatterns =[
     path('lift/',LiftView.as_view()),
    path('create/', CreateLiftView.as_view()),
    path('moveUp/', ElevatorUpView.as_view()),
    path('moveDown/', ElevatorDownView.as_view())
]
