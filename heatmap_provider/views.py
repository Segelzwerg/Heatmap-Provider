from django.http import HttpResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView


def index(request):
    return HttpResponse("Welcome to Heatmap Provider.")


@APIView
@parser_classes([FileUploadParser])
def put(request, filename, format=None):
    file_object = request.data['file']
    return HttpResponse("File Uploaded")
