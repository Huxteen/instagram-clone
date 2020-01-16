from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import auth
from accounts.forms import SignUpForm


# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], 
            password=request.POST['password1']
            )

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            # if we couldnt find a match take them back to the login page with the error
            messages.error(request, 'Email or password do not match our record')
            return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')



def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        context = { 'form': form,}
        return render(request, 'accounts/signup.html', context)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            # form is a valid response then save the data
            user = User.objects.create_user(
                username=(request.POST['username']).casefold(),
                password=request.POST['password1'],
            ) 
            # auth.login(request, user)
            # return redirect('home')
            messages.success(request, 'Account creation was successful. Please, login to dashboard')
            return redirect('signup')
        else:
            # Form has error relay the error to the user
            context = {'form': form}
            return render(request, 'accounts/signup.html', context)
    return render(request, 'accounts/signup.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('login')