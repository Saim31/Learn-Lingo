from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # ONLY this (your custom urls)
    path('accounts/', include('accounts.urls')),
     path('', include('courses.urls')),     
    path('quiz/', include('quizzes.urls')),
    path('progress/', include('progress.urls')),

    path('', include('courses.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
