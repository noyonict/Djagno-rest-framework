from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSets, all_employees, employee_detail


router = routers.DefaultRouter()
router.register('', EmployeeViewSets)

urlpatterns = [
    path('employees/', all_employees, name='all_employees'),
    path('employees/<id>', employee_detail, name='employee_detail'),
    path('', include(router.urls)),
]

