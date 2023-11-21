from django.contrib import admin
from django.urls import path, include
from general.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('task/', include('task.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
]
