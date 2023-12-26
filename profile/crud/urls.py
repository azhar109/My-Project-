from django.urls import path
from .views import Index, About, Apply1, Loginform, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', Index.as_view(), name ='home'),
   path('about', About.as_view()),
   path('apply', Apply1.as_view()),
   path('login', Loginform.as_view(), name= 'login'),
   path('logout', logout)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)