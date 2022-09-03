
from django.contrib import admin
from django.urls import path
from Projectapp.views import home
from Projectapp.views import page1
from Projectapp.views import page2
from Projectapp.views import page3

from Projectapp.views import page4
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Projectapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('page1/', page1, name="page1"),
    path('page2/', page2, name="page2"),
    path('page3/', page3, name="page3"),
    path('page4/', page4, name="page4"),
    
    path('download/', views.download_file),
]
urlpatterns += staticfiles_urlpatterns()
