from django.shortcuts import render
from django.views.generic import View
import io
from .models import Employee
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from testapp.serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'resource created successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='applicaton/json',status=400)

    def put(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id = id)
        serializer = EmployeeSerializer(emp,data=pdata, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'resource updated successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='applicaton/json', status=400)

    def delete(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg':'resource deleted successfully'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')





