from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import auth
from accounts.forms import SignUpForm


# Create your views here.
def login(request):
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
                username=(form.cleaned_data['username']).casefold(),
                password=form.cleaned_data['password1'],
            )
            # auth.login(request, user)
            # return redirect('home')
            messages.success(request, 'Account creation was successful. Please, login to dashboard')
            return redirect('signup')
        # Form has error relay the error to the user
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    return render(request, 'accounts/signup.html')
