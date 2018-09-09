from rest_framework import serializers
from demo1.models import EmployeeInformation


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInformation
        fields = [
            'id',
            'name',
            'designation',
            'employee_id',
            'department',
            'team_name',
            'email',
            'phone',
            'address',
            'joining_date',
            'working_area',
        ]


