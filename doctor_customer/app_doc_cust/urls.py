from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import formGet, profile, presc, getFromNdeuna

urlpatterns = [
    path('',formGet, name='formGet'),
    path('profil/<str:link_Id>',profile ,name="profile"),
    path('prescription/<str:link_Id>', presc, name="prescription"),
    path('getous/', getFromNdeuna)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)