from random import choices, randint

from api.models import Car
from api.serializers import CarSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def car_list(request):
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def car_detail(request, uuid):
    car = get_object_or_404(Car, id=uuid)
    serializer = CarSerializer(car)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def car_generate(request, amount=1):
    LETTERS = 'АВЕКМНОРСТУХ'
    lst = []
    for _ in range(amount):
        letters = choices(LETTERS, k=3)
        car_plate = f'{str(letters[0])}{randint(1, 999):03d}{str(letters[1])}{str(letters[2])}'
        lst.append(car_plate)
    return Response(data=lst)
