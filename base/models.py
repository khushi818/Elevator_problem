from django.db import models

# Create your models here.
class Elevator(models.Model):
    #the current floor in which the lift is 
    floor = models.IntegerField(default=0)
    #it is true when door open
    door_open = models.BooleanField(default=False)
    #it is true if lift is in maintainance
    maintainence = models.BooleanField(default=False)
    # lift moves up if true
    move_up = models.BooleanField(default=False)
    # left moves down if false
    move_down = models.BooleanField(default=False)
    group_number = models.CharField(max_length=20)
