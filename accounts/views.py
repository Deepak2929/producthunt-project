from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
	if request.method=="POST":
		#Userwants to signin
		if request.POST["password"]== request.POST["Cpassword"]:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html',{'error':'Username allready Exist.Try new one!'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'],password=request.POST["Cpassword"])
				auth.login(request,user)
				return redirect('home')
			
	else:
		
		return render(request, 'accounts/signup.html')

	
	
def login(request):
	return render(request, 'accounts/login.html')
	
	
def logout(request):
	#NEED TO ROUTE TO HOMEPAGE
	#DON'T FORGET TO LOGOUT
	
	return render(request, 'accounts/signup.html')