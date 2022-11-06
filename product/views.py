from itertools import product
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.core import serializers
import json
from .models import student
# Create your views here.

class productViewSingle(View):
    def get(self, request, id):
        data = serializers.serialize('json', student.objects.get(id = id))
        return JsonResponse(json.loads(data), safe=False)

    def put(self, request, id):
        updated = json.loads(request.body)
        data = student.objects.filter(id = id).update(firstName=updated["firstName"], lastName=updated["lastName"], email=updated["email"], age=updated_student["age"], Class=updated["Class"])
        return JsonResponse({'status' : 'Updated'}, safe=False)

    def delete(self, request, id):
        student.objects.get(id = id).delete() 
        return JsonResponse({'status' : 'Deleted'}, safe=False)

class productViewMultiple(View):
    def get(self):
        data = serializers.serialize('json', student.objects.all())
        return JsonResponse(json.loads(data), safe=False)

    def post(self, request):
        myData = json.loads(request.body)
        data = student.objects.create(firstName=myData["firstName"], lastName=myData["lastName"], email=myData["email"], age=myData["age"], Class=myData["Class"])
        return JsonResponse({'status' : 'Created'}, safe=False)
