from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .validators import validate_file_size, validate_file_extensions
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError

# Create your views here.
def home(request:HttpResponse):
    return render(request, 'index.html')

def upload_resume(request:HttpResponse):
    if request.method =='POST' and request.FILES.get("file"):
        file:UploadedFile = request.FILES['file']
        
        try:
            validate_file_extensions(file)
            validate_file_size(file)
        except ValidationError as err:
            return JsonResponse({"error": err.message})
        return JsonResponse({"error":"Invalid Request"}, status=400)