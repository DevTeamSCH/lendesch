from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^api/v1/', include('group.urls')),
    url('^api/v1/', include('account.urls')),
    url('^api/v1/', include('loan.urls')),
    url('^api/v1/', include('constraint.urls')),
    url('', include('social_django.urls', namespace='social')),
]
