from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('accounts', views.AccountViewSet)


urlpatterns = router.urls
