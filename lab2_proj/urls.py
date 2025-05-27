# myproject/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from lab2_app import views  # Make sure to replace 'myapp' with your actual app name

urlpatterns = [
    path('', views.home, name='home'),
    path('test/step1/', views.test_step1, name='test_step1'),
    path('test/step2/', views.test_step2, name='test_step2'),
    path('test/step3/', views.test_step3, name='test_step3'),
    path('test-step4/', views.test_step4, name='test_step4'),
    path('static/positive_content.html',views.positive, name='positive'
    )
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
