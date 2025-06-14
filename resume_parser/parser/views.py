from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request:HttpResponse):
    return render(request, 'index.html')

def upload_resume(request:HttpResponse):
    if request.method =='POST' and request.FILES.get("file"):
        ...
        return JsonResponse({"error":"Invalid Request"}, status=400)