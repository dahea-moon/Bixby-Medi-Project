from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="main.html"),),    
    path('privacy/', TemplateView.as_view(template_name="privacy.html"),),    
    path('admin/', admin.site.urls),
    path('api/AED/', include('AED.urls')),
    path('api/sooyusil/', include('sooyusil.urls')),
    path('api/pharmacy/', include('pharmacy.urls')),
    path('api/emergency/', include('emergency.urls')),
    path('api/anal/', include('anal.urls')),
    path('api/bone/', include('bone.urls')),
    path('api/child/', include('child.urls')),
    path('api/dental/', include('dental.urls')),
    path('api/external/', include('external.urls')),
    path('api/eye/', include('eye.urls')),
    path('api/family/', include('family.urls')),
    path('api/general/', include('general.urls')),
    path('api/internal/', include('internal.urls')),
    path('api/men/', include('men.urls')),
    path('api/mental/', include('mental.urls')),
    path('api/moonlight/', include('moonlight.urls')),
    path('api/nose/', include('nose.urls')),
    path('api/nerve/', include('nerve.urls')),
    path('api/nursing/', include('nursing.urls')),
    path('api/oriental/', include('oriental.urls')),
    path('api/plastic/', include('plastic.urls')),
    path('api/public_health/', include('public_health.urls')),
    path('api/skin/', include('skin.urls')),
    path('api/total/', include('total.urls')),
    path('api/women/', include('women.urls')),
]
