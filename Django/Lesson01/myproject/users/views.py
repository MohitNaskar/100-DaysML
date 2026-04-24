from math import e
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('posts:list')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    # Placeholder for login view logic
    if request.method == 'POST':
        # Handle login logic here
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('posts:list')  # Redirect to a page after successful login
    else:
        # Render the login form
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})  # Create a login.html template later


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:list')  # Redirect to a page after logout
    return render(request, 'users/logout.html')  # Create a logout.html template later