from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSets, all_employees, employee_detail, DemoAPIView, DemoDetailAPIView, \
    EmployeeModelMixinAPIView


router = routers.DefaultRouter()
router.register('', EmployeeViewSets)

urlpatterns = [
    path('generic-mixin-api-view/', EmployeeModelMixinAPIView.as_view()),
    path('generic-mixin-api-view/<int:id>/', EmployeeModelMixinAPIView.as_view()),
    path('employees-class-view/', DemoAPIView.as_view()),
    path('employees-class-view/<int:id>/', DemoDetailAPIView.as_view()),
    path('employees/', all_employees, name='all_employees'),
    path('employees/<int:id>/', employee_detail, name='employee_detail'),
    path('', include(router.urls)),
]

