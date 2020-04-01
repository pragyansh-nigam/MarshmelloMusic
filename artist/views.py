from django.shortcuts import render
from django.conf import settings
import random

"""def all_songs(request):
    songs_list = Songs.objects.all()
    songs_list=random.shuffle(songs_list)"""

def home(request):
    return render(request,"home.html")

def bio(request):
    return render(request,"bio.html")

def gallery(request):
    return render(request,"gallery.html")

def music(request):
    return render(request,"music.html")

def spotify(request):
    return render(request,"spotify.html")

def videos(request):
    return render(request,"videos.html")

def tour(request):
    return render(request,"tour.html")

def booking(request):
	#name = request.POST.get('name')
	#mob = request.POST.get('phone')
	#mail = request.POST.get('email')
	#city = request.POST.get('city')

	#query = "insert into booking(NAME,MOBILE,EMAIL,CITY) value('{0}','{1}','{2}','{3}')".format(name,mob,mail,city)

	#cnn = settings.CONNECTION()

	#cr = cnn.cursor()
	#cr.execute(query)
	#cnn.commit()

	return render(request,"booking.html")

def contact(request):
	name = request.POST.get('name')
	mail = request.POST.get('email')
	sub = request.POST.get('subject')
	msg = request.POST.get('message')

	query = "insert into contact(name,email,subject,message) value('{0}','{1}','{2}','{3}')".format(name,mail,sub,msg)

	cnn = settings.CONNECTION()

	cr = cnn.cursor()
	cr.execute(query)
	cnn.commit()
	msg = "Contact Saved!"

	return render(request,"contact.html",{"msg":msg})
	 