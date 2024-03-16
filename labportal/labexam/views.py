from django.shortcuts import render

# Create your views here.
def labexam_home(request):
    return render(request, 'labexam/labexam-home.html')