from django.contrib import admin
from django.urls import path
from .views import (usersignupview, userhomepageview, userloginview, logoutuser, myorderview, cart, checkout, 
	profileview,resetpasswordview,grocery, stationary, fashion, food, dairy, electrical, fruits, special, dairy1, electrical1,
	food1, fruit1, fashion1, grocery1, special1, stationary1 )

urlpatterns =[
	path('signup/', usersignupview, name='usersignuppage'),
	path('login/', userloginview, name = "userloginpage"),
	path('', userhomepageview, name= "userhomepage"),
	path('userlogout/', logoutuser),
	path('yourorders/', myorderview, name="myorderpage"),
	path('cart/', cart, name="cartpage"),
	path('checkout/', checkout, name="checkoutpage"),
	path('profile/', profileview, name="profilepage"),
	path('resetpassword/', resetpasswordview, name="resetpage"),
	path('stationary/', stationary, name="stationarypage"),
	path('grocery/', grocery, name="grocerypage"),
	path('fashion/', fashion, name="fashionpage"),
	path('food/', food, name="foodpage"),
	path('dairy/', dairy, name="dairypage"),
	path('electrical/', electrical, name="electricalpage"),
	path('vegetables/', fruits, name="fruitpage"),
	path('special/', special, name="specialpage"),
	path('dairyshops/', dairy1, name="dairy1page"),
	path('electricalshops/', electrical1, name="electrical1page"),
	path('foodshops/', food1, name="food1page"),
	path('fashionshops/', fashion1, name="fashion1page"),
	path('fruitshops/', fruit1, name="fruit1page"),
	path('groceryshops/', grocery1, name="grocery1page"),
	path('specialshops/', special1, name="special1page"),
	path('stationaryshops/', stationary1, name="stationary1page"),

	]