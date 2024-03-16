from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from . models import CreateExam
from . forms import CreateExamForm


# Create your views here.
def labexam_home(request):
    exam_data = CreateExam.objects.all()    
    return render(request, 'labexam/labexam-home.html', {'exam_data': exam_data})

def create_exam(request):    
    if request.method == 'POST':
        form = CreateExamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            return HttpResponseRedirect(reverse(labexam_home))    
    else:
        form = CreateExamForm()
        return render(request, 'labexam/create-exam.html', {'form': form})

    