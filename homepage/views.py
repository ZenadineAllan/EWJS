from django.shortcuts import render
from .forms import NewStudentForm
from .models import Students
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def newstudent(request):
    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            Students.save()

        return redirect('homepage:newstudent')
    
    else:
        form = NewStudentForm()
    
    return render(request, 'homepage/newstudent.html', {"form": form})
    
    
