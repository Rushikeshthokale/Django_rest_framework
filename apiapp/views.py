from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from apiapp.serializers import EmployeeSerializer
from django.http import JsonResponse
from rest_framework import status
from apiapp.models import Employe
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@csrf_exempt
def employees(request):
    if request.method=="POST":
        receivedData=JSONParser().parse(request)
        # print(type(receivedData))#dict
        ser=EmployeeSerializer(data=receivedData)
        if ser.is_valid():
            ser.save()
            obj=ser.data
            return JsonResponse(obj,status=status.HTTP_201_CREATED)
        else:
            err={}
            err['message']="The data must be in proper format!!!"
            err["Details"]=ser.errors
            return JsonResponse(err,status=status.HTTP_400_BAD_REQUEST)
    else:
        employes=Employe.objects.all()
        ser=EmployeeSerializer(employes,many=True)
        return JsonResponse(ser.data,status=status.HTTP_200_OK,safe=False)

@csrf_exempt
def empDetails(request,empid):
    try:
        emp=Employe.objects.get(id=empid)
    except ObjectDoesNotExist:
        error={"message":"Please provide valid employe id!!!"}
        return JsonResponse(error,status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        ser=EmployeeSerializer(emp)
        return JsonResponse(ser.data,status=status.HTTP_200_OK)
    elif request.method=="DELETE":
        emp.delete()
        success={"message":'deleted successfully!!'}
        return JsonResponse(success,status=status.HTTP_204_NO_CONTENT)
    elif request.method=="PUT":
        receivedData=JSONParser().parse(request)
        ser=EmployeeSerializer(emp,data=receivedData)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status.HTTP_200_OK)
        else:
            return JsonResponse("Please provide proper format for data!!!",status.HTTP_400_BAD_REQUEST)

    