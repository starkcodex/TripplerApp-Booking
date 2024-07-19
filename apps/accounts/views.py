from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model



# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password =  request.POST.get('password')
        
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None and user.is_active:
#             login(request, user)
#             messages.success(request, f'Welcome! You are logged in as {user}')
#             return redirect('homepage')
#         else:
#             messages.warning(request, 'Something went wrong! please try again.')
#             return redirect('login')
#     return redirect(request, 'accounts/login.html')