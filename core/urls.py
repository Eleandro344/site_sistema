from django.contrib import admin
from django.urls import path, include # adicionar include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),      
    path('contas/', include('contas.urls')), # Adiciona contas
    path('perfil/', include('perfil.urls')),
    path('config/', include('config.urls')),    
    path('', include('pages.urls')),


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto