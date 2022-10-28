from django.views import View
from django.http import JsonResponse
from django.core import serializers
import json
from .forms import *
from .models import *

# Create your views here.

# student views
class studentView(View):
    def get(self, request):
        try:
            data = json.loads(serializers.serialize("json", student.objects.all()))
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse({'message': 'No students found'}, status = 422)

    def post(self, request):
        try:
            form = studentForm(data=json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Record created successfully'})
            else:
                return JsonResponse(form.errors, status = 422)
        except:
            return JsonResponse({'message': 'Format error'}, status = 422)

class studentViewID(View):
    def get(self, request, *args, **kwargs):
        try:
            data = json.loads(serializers.serialize("json", student.objects.filter(id=kwargs["id"])))
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse({f'student {kwargs["id"]}': "Not found"}, status = 422)

    def put(self, request, *args, **kwargs):
        try:
            form = studentForm(data = json.loads(request.body), instance = student.objects.get(id = kwargs['id']))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Student updated successfully'})
            else:
                return JsonResponse(form.errors, status = 422)
        except:
            return JsonResponse({'message': 'Format error!'}, status=422)

    def delete(self, request, *args, **kwargs):
        try:
            student.objects.filter(id = kwargs["id"])
            student.delete()
            return JsonResponse({'message': 'Student deleted successfully'}, status=422)
        except:
            return JsonResponse({'message': 'Student not deleted'}, status=422)


# parent views
class parentView(View):
    def get(self, request):
        try:
            data = json.loads(serializers.serialize("json", parent.objects.all()))
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse({'message': 'No parents found'}, status = 422)

    def post(self, request):
        try:
            form = parentForm(data=json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Record created successfully'})
            else:
                return JsonResponse(form.errors, status = 422)
        except:
            return JsonResponse({'message': 'Format error'}, status = 422)

class parentViewID(View):
    def get(self, request, *args, **kwargs):
        try:
            data = json.loads(serializers.serialize("json", parent.objects.filter(id=kwargs["id"])))
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse({f'parent {kwargs["id"]}': "Not found"}, status = 422)

    def put(self, request, *args, **kwargs):
        try:
            form = parentForm(data = json.loads(request.body), instance = parent.objects.get(id = kwargs['id']))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Parent updated successfully'})
            else:
                return JsonResponse(form.errors, status = 422)
        except:
            return JsonResponse({'message': 'Format error!'}, status=422)

    def delete(self, request, *args, **kwargs):
        try:
            parent.objects.filter(id = kwargs["id"])
            parent.delete()
            return JsonResponse({'message': 'Parent deleted successfully'}, status=422)
        except:
            return JsonResponse({'message': 'Parent not deleted'}, status=422)

# subject views
class subjectView(View):
    def get(self, request):
        try:
            data = json.loads(serializers.serialize("json", subject.objects.all()))
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse({'message': 'No subjects found'}, status = 422)

    def post(self, request):
        try:
            form = subjectForm(data=json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Record created successfully'})
            else:
                return JsonResponse(form.errors, status = 422)
        except:
            return JsonResponse({'message': 'Format error'}, status = 422)

class subjectViewID(View):
    def get(self, request, *args, **kwargs):
        try:
            data = json.loads(serializers.serialize("json", subject.objects.filter(id=kwargs["id"])))
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse({f'subject {kwargs["id"]}': "Not found"}, status = 422)

    def put(self, request, *args, **kwargs):
        try:
            form = subjectForm(data = json.loads(request.body), instance = subject.objects.get(id = kwargs['id']))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Subject updated successfully'})
            else:
                return JsonResponse(form.errors, status = 422)
        except:
            return JsonResponse({'message': 'Format error!'}, status=422)

    def delete(self, request, *args, **kwargs):
        try:
            subject.objects.filter(id = kwargs["id"])
            subject.delete()
            return JsonResponse({'message': 'Subject deleted successfully'}, status=422)
        except:
            return JsonResponse({'message': 'Subject not deleted'}, status=422)