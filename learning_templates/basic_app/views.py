from django.shortcuts import render
from basic_app.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'basic_app/users.html',{'form':form})
