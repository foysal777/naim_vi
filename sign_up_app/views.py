from django.shortcuts import render,redirect
from  .forms import RegisterForm
# Create your views here.
def home(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
        return redirect('homepage')
    
    else:
     form = RegisterForm()  
     print(form)
    return render(request, 'home.html' , {'data' : form})