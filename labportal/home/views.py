from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def lab_rules(request):
    return render(request, 'home/lab-rules.html')

