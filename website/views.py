from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




def home(request):

	#check to see if logging in
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"You have been Logged in!")
			return redirect('home')
		else :
			messages.error(request,"There was an error Logging in. Please try again...")
			return redirect('home')
	else:
		return render(request,'home.html',{})


def logout_user(request):
	logout(request)
	messages.success(request, "You have been Logged out")
	return redirect('home')

def signup_user(request):
	return render(request,'signup.html',{})
