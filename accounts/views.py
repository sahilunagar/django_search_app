from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
import math, random
from django.core.mail import send_mail
from .models import CustomUser
from django.conf import settings

def register(request):
    if request.method == 'POST':
        # Process the signup form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        # Generate and send OTP
        otp = generateOTP()  
        send_otp(email, otp)  

        # Create the user (with a temporary password for now)
        user = CustomUser.objects.create_user(username=CustomUser.USERNAME_FIELD, email=email, password=CustomUser.DEFAULT_PASSWORD, first_name=first_name, last_name=last_name, gender=gender, phone_number=phone_number)

        # Store the OTP in the user's session for verification later
        request.session['otp'] = otp
        request.session['email'] = email

        # Redirect to OTP verification page
        return redirect('accounts:verify_otp')

    return render(request, 'signup.html')

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        email = request.session.get('email')
        # Verify the OTP
        if otp == request.session.get('otp'):
            # Remove the temporary password and set the user as active
            user = CustomUser.objects.get(email=email)
            # user.set_password(None)
            # user.password = None
            user.is_active = True
            user.save()

            # Log the user in
            # user = auth.authenticate(username=email, password=None)
            user = authenticate(request, email=email, password=CustomUser.DEFAULT_PASSWORD)
            if user is not None:
                # login(request, user)
                auth.login(request, user)
                return redirect('search')
        else:
            return redirect('accounts:verify_otp')

    return render(request, 'verify_otp.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']

        # Generate and send OTP
        otp = generateOTP() 
        send_otp(email, otp) 

        # Store the OTP in the user's session for verification later
        request.session['otp'] = otp
        request.session['email'] = email

        # Redirect to OTP verification page
        return redirect('accounts:verify_otp')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('accounts:register')


# function to generate OTP
def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

def send_otp(email, otp):
    email_from = settings.EMAIL_HOST_USER
    send_mail(
        "Verify your WorldSearch account",
        'The One Time Password to login to your WorldSearch account is '+otp+ '. Do not share your OTP with anyone else.',
        email_from,
        [email],
        fail_silently=False,
    )
