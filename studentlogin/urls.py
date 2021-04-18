from django.contrib import admin
from django.urls import path
from userinfo import views as a
from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', a.home, name='home'),
    #  path('products/', a.products, name='products'),
  

    path('catlogin', a.catlogin, name='catlogin'),
    path('catvai', a.catvai, name='catvai'),
    path('login/', a.catlogin, name="login"),  
	path('logout/', a.logoutUser, name="logout"),
	path('bookvai', a.bookvai, name="bookvai"),
	path('sem', a.sem, name="sem"),
	path('xvai', a.xvai, name="sem"),
	path('amishow', a.amishow, name="amishow"),
	path('std', a.std, name="std"),
	path('stdshow', a.stdshow, name="stdshow"),
	path('sdelete/<str:id>', a.sdelete, name="sdelete"),
	path('sedit/<str:id>', a.sedit, name="edit"),
    
	# path('userinfo', a.userinfo, name="userinfo"),

     
    path('e', a.hotel_image_view, name = 'image_upload'),
   
    path('f', a.displayimages, name = 'f'),

    path('ami', a.ami, name = 'ami'),
    
     path('<id>/delete', a.delete, name="delete"),


]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if  settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

elif not settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


# if not settings.DEBUG: urlpatterns += [ url(r'^uploads/(?P<path>.)$', serve,{'document_root': settings.MEDIA_ROOT}), url(r'^static/(?P<path>.)$', serve,{'document_root': settings.STATIC_ROOT}), ]