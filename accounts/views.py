from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import auth
from accounts.forms import SignUpForm
from django.contrib.auth.decorators import login_required

from accounts.models import Profile


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




@login_required(login_url="/")
def profile(request):
    uid = request.user.id
    if request.method == "GET":
        profile = Profile.objects.filter(author__id=uid)
        context = {
            'profile':profile
            }
        return render(request, 'accounts/profile.html', context)

    if request.method == "POST":
        create_post = Profile()
        create_post.description = request.POST['description'][0:100]
        create_post.image = request.FILES['image']
        create_post.author = User(pk=uid)
        create_post.publish = int(request.POST['publish'])
        create_post.save()

        messages.success(request, 'Profile post created successfully')
        return redirect("profile")



@login_required(login_url="/")
def delete_profile(request, post_id):
    if request.method == 'POST':
        delete_post = Profile.objects.get(pk=post_id)
        delete_post.delete()
        return redirect('profile')
    else:
        return redirect('profile')


def update_profile(request, post_id):
    if request.method == "GET":
        profile = Profile.objects.get(pk=post_id)
        context = {
            'profile':profile
            }
        return render(request, 'accounts/update_profile.html', context)

    if request.method == "POST":
        update_post = Profile.objects.get(pk=post_id)
        update_post.description = request.POST['description'][0:100]
        if 'image'in request.FILES:
            update_post.image = request.FILES['image']
        update_post.publish = int(request.POST['publish'])
        update_post.save()

        messages.success(request, 'Profile post updated successfully')
        return redirect('profile')


    





    
