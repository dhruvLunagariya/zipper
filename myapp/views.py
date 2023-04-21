from django.shortcuts import render
from tkinter import E
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser

# Create your views here.
def home(request):
    return render(request,'home.html')
def download(request , uid):
    return render(request , 'download.html' , context = {'uid' : uid})
#uid is unique idetifier(render download page with uid)

# a view to handle file upload via POST request
class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]
    def post(self , request):
        try:
            data = request.data

            #validate the serializer
            #
            serializer = FileListSerializer(data = data)        
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : 200,
                    'message' : 'files uploaded successfully',
                    'data' : serializer.data
                })
            
            return Response({
                'status' : 400,
                'message' : 'somethign went wrong',
                'data'  : serializer.errors
            })
        except Exception as e:
            print(e)