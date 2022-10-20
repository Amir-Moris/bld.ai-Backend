from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pathlib
import json
# Create your views here.

def read_json():
    file = open(f'{pathlib.Path(__file__).parent.resolve()}' + '/data.json', "r")
    data = file.read()
    file.close()
    return json.loads(data)
    
def write_json(newData):
    file = open(f'{pathlib.Path(__file__).parent.resolve()}' + '/data.json', "w")
    file.write(json.dumps(newData))
    file.close()

def get_post(request):
    Data = read_json()
    if request.method == 'GET':
        return JsonResponse(Data["student"], safe = False)
    elif request.method == 'POST':
        Data["student"].append((json.loads(request.body)))
        write_json(Data)
        return JsonResponse(Data["student"], safe = False)

def put_delete(request, ID):
    Data = read_json()
    if request.method == 'PUT':
        for index in range(0, len(Data["student"])):
            if Data["student"][index]["id"] == ID:
                Data["student"][index] = json.loads(request.body)
                write_json(Data)
                return JsonResponse(Data["student"][index], safe = False)
    elif request.method == 'DELETE':
        for index in range(0, len(Data["student"])):
            if Data["student"][index]["id"] == ID:
                print(Data)
                Data["student"].pop(index)
                write_json(Data)
                return HttpResponse("Data deleted successfully")
    return HttpResponse("Error there is no student with such id please try another")