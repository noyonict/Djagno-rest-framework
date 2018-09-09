from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from .serializers import EmployeeSerializer
from demo1.models import EmployeeInformation


class EmployeeViewSets(viewsets.ModelViewSet):
    queryset = EmployeeInformation.objects.all()
    serializer_class = EmployeeSerializer


@csrf_exempt
def all_employees(request):
    if request.method == 'GET':
        employees = EmployeeInformation.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def employee_detail(request, id=None):
    # try:
    #     employee = EmployeeInformation.objects.filter(id=id)
    # except EmployeeInformation.DoesNotExist as e:
    #     return JsonResponse({'error': 'Employee information not found'}, status=404)

    employee = get_object_or_404(EmployeeInformation, id=id)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=204)






