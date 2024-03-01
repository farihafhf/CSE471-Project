from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import UserProfile

@login_required
def edit_profile(request):
    try:
        form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
    except User.userprofile.RelatedObjectDoesNotExist:
        # Create a new profile for the user if it doesn't exist
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)  # Avoid saving twice
            user_profile.user = request.user
            user_profile.save()  # Now save the profile with the user association
            messages.success(request, 'Profile created and updated successfully')
            return redirect('dashboard')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'authentication/edit_profile.html', {'form': form})

@login_required
def view_profile(request):
    try:
        user_profile = request.user.userprofile
        if not user_profile.profile_pic:
        # If not, use the default profile picture
            user_profile.profile_pic = 'default_profile_pic/default.jpg'
    except User.userprofile.DoesNotExist:
        # Handle the case where the user doesn't have a profile yet (optional)
        messages.info(request, 'You haven\'t created a profile yet.')
        return redirect('create_profile')  # Redirect to profile creation view if desired
    
    # # Print statements for debugging
    # print(f"User profile retrieved: {user_profile}")
    # print(f"Profile picture URL: {user_profile.profile_picture.url}")   
    
    return render(request, 'authentication/view_profile.html', {'user_profile': user_profile})

from tasks.models import Project
# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
    
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Account created successfully!")
        return redirect('signin')  # Redirect to sign-in page after successful sign-up


    return render(request, "authentication/signup.html")

def signin(request):

    if request.method=="POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user=authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            return redirect('dashboard')

        else:
            messages.error(request,"Wrong Username or Password")
            return redirect('home')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect("home")

@login_required
def dashboard(request):
    fname = request.user.first_name
    user_projects = Project.objects.filter(created_by=request.user)
    return render(request, 'authentication/dashboard.html', {'user_projects': user_projects,'fname': fname})
