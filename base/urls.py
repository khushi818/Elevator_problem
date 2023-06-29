from django.urls import path
from .views import CreateLiftView, LiftView,ElevatorUpView,DoorMotionView

urlpatterns =[
    path('lift/',LiftView.as_view()),
    path('create/', CreateLiftView.as_view()),
    path('moveUp/', ElevatorUpView.as_view()),
    path('door/',DoorMotionView.as_view())
]
