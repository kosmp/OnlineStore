from .views import statistic_show, tables_show, predict_show
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'statistic'

urlpatterns = [
    path('', statistic_show, name='statistic'),
    path('tables/<int:id>/', predict_show),
    path('tables/', tables_show, name='tables'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)