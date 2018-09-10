from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, mixins
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from demo1.models import EmployeeInformation


# Model View sets and routers
class EmployeeModelViewSets(viewsets.ModelViewSet):
    queryset = EmployeeInformation.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


class EmployeeModelMixinAPIView(generics.GenericAPIView,
                                mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin):
    queryset = EmployeeInformation.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    # def perform_create(self, serializer):
    #     serializer.save(create_by=self.request.user)

    def put(self, request, id=None):
        return self.update(request, id)

    # def perform_update(self, serializer):
    #     serializer.save(create_by=self.request.user)

    def delete(self, request, id=None):
        return self.destroy(request, id)


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


class DemoAPIView(APIView):
    def get(self, request):
        employees = EmployeeInformation.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class DemoDetailAPIView(APIView):
    def get_object(self, id=None):
        try:
            return EmployeeInformation.objects.get(id=id)
        except EmployeeInformation.DoesNotExist as e:
            return Response({'error': "Object not found!"}, status=400)

    def get(self, request, id):
        instance = self.get_object(id)
        serializer = EmployeeSerializer(instance)
        return Response(serializer.data, status=200)

    def put(self, request, id=None):
        instance = self.get_object(id)
        data = request.data
        serializer = EmployeeSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)

