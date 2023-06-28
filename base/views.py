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
class LiftView(generics.ListAPIView):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

class CreateLiftView(APIView):
    serializer_class = ElevatorSerializer
    lookup_url_kwargs = 'number'
      
    
    def post(self,request,format = None):
        number = int(request.GET.get(self.lookup_url_kwargs))
        print(number)
        lift =[]
        
        if number != None:
            code = generate_unique_code()
            group_number = code
            for _ in range(0,number):
                lift.append(Elevator(group_number=group_number))
            Elevator.objects.bulk_create(lift)
            return Response({'message': 'lift has been created'},status=status.HTTP_200_OK)
        return  Response({ 'message' : 'badrequest'},status=status.HTTP_400_BAD_REQUEST)    

