from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .forms import CustomUserForm
from .models import CustomUser
from django.contrib import messages, auth 
from .utils import send_verification_email
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied 

def home(request):
    #pass
    return render(request, 'accounts/index.html')

def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in.!')
        return redirect('home')
    elif request.method =='POST':
        # print(request.POST)
        form = CustomUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()

            # Send verification email
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject,email_template )

            messages.success(request, "Your account has been registered successfully!")    
            return redirect('login')
        else:
            print(form.errors)    
    else:    
        form =  CustomUserForm()

    context = {
        'form': form, 
    }
    return render(request, 'accounts/registerUser.html', context)


def activate(request, uidb64, token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist): 
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('myAccount')
    else: 
        messages.error(request, 'Invalid activation link.')   
        return redirect('myAccount')


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in.!')
        return redirect('home')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials ')
            return redirect('login')   
    return render(request, 'accounts/login.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('login')