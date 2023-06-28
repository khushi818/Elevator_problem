from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Elevator
from .serializer import ElevatorSerializer
import random,string
# Create your views here.


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_lowercase, k=length))
        if(Elevator.objects.filter(group_number=code).count() == 0):
            break

    return code

def closest_lift(next_floor,group):
       Elevators = Elevator.objects.filter(group_number = group)[0]
       floor = Elevators.floor
       total = Elevators.total_floors
       if (abs(next_floor) == floor):
           lift = Elevators
       elif(next_floor > 0 and next_floor <= total):
           lift = Elevator.objects.filter(floor__lt = next_floor).order_by('-floor')[0]
       elif (next_floor < 0):
           next_floor = -next_floor
           lift = Elevator.objects.filter(floor__gt=next_floor).order_by('-floor')[0]         

       return lift.id

class LiftView(generics.ListAPIView):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

class CreateLiftView(APIView):
    serializer_class = ElevatorSerializer
    lookup_url_kwargs = ('number','floors') 
      
    
    def post(self,request,format = None):
        number = int(request.GET.get(self.lookup_url_kwargs[0]))
        floors = int(request.GET.get(self.lookup_url_kwargs[1]))
        print(number,floors)
        lift =[]
        
        if number != None:
            code = generate_unique_code()
            group_number = code
            for _ in range(0,number):
                lift.append(Elevator(group_number=group_number, total_floors = floors))
            Elevator.objects.bulk_create(lift)
            return Response({'message': 'lift has been created'},status=status.HTTP_200_OK)
        return  Response({ 'message' : 'badrequest'},status=status.HTTP_400_BAD_REQUEST)    

class ElevatorUpView(APIView):
        serializer_class = ElevatorSerializer
        lookup_url_kwargs = ('above_floor','group')
        
        def put(self,request,format=None):
            above_floor = int(request.GET.get(self.lookup_url_kwargs[0]))
            group = request.GET.get(self.lookup_url_kwargs[1])
            lift_id = closest_lift(above_floor,group)
            lift = Elevator.objects.get(id = lift_id)
            print(lift.maintainence)
            if not lift.maintainence:
                if not lift.move_up:
                   lift.move_up = True
                   lift.floor = above_floor
                   lift.save()
                serialiser = ElevatorSerializer(lift)
                return Response(serialiser.data, status=status.HTTP_200_OK)
            return Response({'message':'in_maintainance'}, status=status.HTTP_400_BAD_REQUEST)


class ElevatorDownView(APIView):
          serializer_class = ElevatorSerializer
          lookup_url_kwargs = ('down_floor','group')
            
          def put(self,request,format=None):
              down_floor = int(request.GET.get(self.lookup_url_kwargs[0]))
              group = request.GET.get(self.lookup_url_kwargs[1])
              lift_id = closest_lift((-down_floor),group)
              lift = Elevator.objects.get(id=lift_id)
              if not lift.maintainence:
                if not lift.move_down:
                   lift.move_down = True
                   lift.floor = down_floor
                   lift.save()
                   serialiser = ElevatorSerializer(lift)
                   return Response(serialiser.data, status=status.HTTP_200_OK)
              return Response({'message':'in_maintainance'}, status=status.HTTP_400_BAD_REQUEST)
