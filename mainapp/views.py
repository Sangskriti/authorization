from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .signupform import CustomUserCreationForm

# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})

# Sign Up View
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, "Your account has been created successfully. You can now log in.")
            return redirect('login')  # Redirect to login page after successful sign-up
        else:
            messages.error(request, "Please correct the errors below.")  # Display error message
    else:
        form = CustomUserCreationForm()  # Empty form when it's a GET request
    
    return render(request, 'registration/sign_up.html', {'form': form})
