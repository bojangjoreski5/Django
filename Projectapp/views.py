from django.shortcuts import render
import mimetypes
import os
from django.http.response import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'home.html')

def page1(request):
	return render(request, 'page1.html')

def page2(request):
	return render(request, 'page2.html')

def page3(request):
	return render(request, 'page3.html')

def page4(request):
	return render(request, 'page4.html')

def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'cert.txt'
    # Define the full file path
    filepath = BASE_DIR + '/data/file/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

	