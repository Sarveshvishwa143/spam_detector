from django.contrib import admin
from django.urls import path , include

admin.site.site_header = "UMSRA Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "i am sarvesh"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spam_app.urls')),
]
  #  path('services', include('myproject.urls')),
   # path('secondpage',include('classify.urls')),
   
