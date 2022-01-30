from django.conf import Settings, settings
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
