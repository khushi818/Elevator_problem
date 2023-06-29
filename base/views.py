from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Elevator
from .serializer import ElevatorSerializer
import random,string
from django.db.models import Q
# Create your views here.


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_lowercase, k=length))
        if(Elevator.objects.filter(group_number=code).count() == 0):
            break

    return code

floor =[]
id =[]
def closest_lift(next_floor,group):
    Elevators = Elevator.objects.filter(group_number = group).values()
    from_roof = list(filter(lambda x : x['floor'] < next_floor , Elevators))
    from_ground = list(filter(lambda x: x['floor'] > next_floor, Elevators))
    
    if(len(from_roof) == 0 and len(from_ground)== 0):
            return list(Elevators)[0]['id']
    if(len(from_roof)== 0):
            return from_ground[0]['id']
    if(len(from_ground) == 0):
            return from_roof[0]['id']
    if(abs(from_ground[0].floor-next_floor) > abs(from_roof[0].floor-next_floor)):
         return from_roof[0]['id']
    else:
         return from_ground[0].id           
    
class LiftView(generics.ListAPIView):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

class CreateLiftView(APIView):
    serializer_class = ElevatorSerializer
    lookup_url_kwargs = ('number','floors') 
      
    
    def post(self,request,format = None):
        number = int(request.GET.get(self.lookup_url_kwargs[0]))
        floors = int(request.GET.get(self.lookup_url_kwargs[1]))
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
        lookup_url_kwargs = ('next_floor','group')
        
        def put(self,request,format=None):
            next_floor = int(request.GET.get(self.lookup_url_kwargs[0]))
            group = request.GET.get(self.lookup_url_kwargs[1])
            lift_id = closest_lift(next_floor,group)
            lift = Elevator.objects.get(id = lift_id)
            if not lift.maintainence:
                   if(lift.floor > next_floor):
                       lift.move_up = False
                   elif (lift.floor < next_floor):
                       lift.move_up = True
                   lift.floor = next_floor
                   lift.save()
                   serialiser = ElevatorSerializer(lift)
                   return Response(serialiser.data, status=status.HTTP_200_OK)
            return Response({'message':'in_maintainance'}, status=status.HTTP_400_BAD_REQUEST)
     

class toggleLiftMotionView(APIView):
    serializer_class = ElevatorSerializer

    def put(self, request, pk=None):
          lift = Elevator.objects.get(pk=pk)
          lift.in_motion = not lift.in_motion
          if(lift.in_motion): lift.door_open = False
          lift.save()
          serialiser = ElevatorSerializer(lift)
          return Response(serialiser.data, status=status.HTTP_200_OK)


class DoorMotionView(APIView):
      serializer_class = ElevatorSerializer
      
      def put(self,request,pk = None):
           lift = Elevator.objects.get(pk=pk)
           if not lift.in_motion:
                lift.door_open = True
           else :
               lift.door_open = False

           lift.save()   
           serialiser = ElevatorSerializer(lift)
           return Response(serialiser.data, status=status.HTTP_200_OK)
       
