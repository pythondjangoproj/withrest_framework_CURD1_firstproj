from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=30)
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length=30)
    def validate_esal(self,value):
        if value >10000:
            raise serializers.ValidationError('Employee salary should be minimum 10000')
        return value

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.eno = validated_data.get('eno',instance.eno)
        instance.ename = validated_data.get('eno', instance.ename)
        instance.esal = validated_data.get('eno', instance.esal)
        instance.eaddr = validated_data.get('eno', instance.eaddr)
        instance.save()
        return instance

