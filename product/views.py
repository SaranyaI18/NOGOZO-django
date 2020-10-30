from django.shortcuts import render

# Create your views here.
def userloginview(request):
	return render(request, "userlogin.html")

def usersignupview(request):
	return render(request, 'usersignup.html')

def userhomepageview(request):
	return render(request, "index.html")


def cart(request):
	return render(request, "cart.html")

def checkout(request):
	return render(request, "checkout.html")

def myorderview(request):
	return render(request, "yourorders.html")

def profileview(request):
	return render(request, "profile.html")


def logoutuser(request):
	return render(request, "userlogin.html")

def resetpasswordview(request):
	return render(request, "resetpw.html")

def stationary(request):
	return render(request, "station.html")

def fruits(request):
	return render(request, "fruit.html")

def grocery(request):
	return render(request, "grocery.html")

def food(request):
	return render(request, "food.html")

def fashion(request):
	return render(request, "fashion.html")

def dairy(request):
	return render(request, "dairy.html")

def special(request):
	return render(request, "special.html")

def electrical(request):
	return render(request, "electrical.html")

def dairy1(request):
	return render(request, "dairy1.html")

def electrical1(request):
	return render(request, "electrical1.html")

def fashion1(request):
	return render(request, "fashion1.html")

def food1(request):
	return render(request, "food1.html")

def grocery1(request):
	return render(request, "grocery1.html")

def special1(request):
	return render(request, "special1.html")

def fruit1(request):
	return render(request, "fruit1.html")

def stationary1(request):
	return render(request, "stationary1.html")

