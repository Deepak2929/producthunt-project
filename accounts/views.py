from django.shortcuts import render

# Create your views here.
def signup(request):
	return render(request, 'accounts/signup.html')

	
	
def login(request):
	return render(request, 'accounts/login.html')
	
	
def logout(request):
	#NEED TO ROUTE TO HOMEPAGE
	#DON'T FORGET TO LOGOUT
	
	return render(request, 'accounts/signup.html')