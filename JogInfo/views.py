from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Jog, Datapoint
from .serializers import JogSerializer, DatapointSerializer


@csrf_exempt
def jog_list(request):
    if request.method == 'GET':
        jogs = Jog.objects.all()
        serializer = JogSerializer(jogs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = JogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def datapoints_list(request, pk):
    try:
        datapoints = Datapoint.objects.get(pk=pk)
    except Datapoint.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DatapointSerializer(datapoints)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DatapointSerializer(datapoints, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        datapoints.delete()
        return HttpResponse(status=204)


@csrf_exempt
def new_jog(request):
    if request.method == 'POST':
        print(request.POST.get("startTime", None))

        # serializer = DatapointSerializer(datapoints, data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data)
        return HttpResponse(status=200)
