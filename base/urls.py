from django.urls import path
from .views import CreateLiftView, LiftView,ElevatorUpView,DoorMotionView,toggleLiftMotionView

urlpatterns =[
    path('lift/',LiftView.as_view()),
    path('create/', CreateLiftView.as_view()),
    path('moveUp/', ElevatorUpView.as_view()),
    path('door/<str:pk>',DoorMotionView.as_view()),
    path('move/<str:pk>',toggleLiftMotionView.as_view())
]
