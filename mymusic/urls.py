from django.urls import path, include

urlpatterns=[
				path('artist/', include('artist.urls'))
			]
