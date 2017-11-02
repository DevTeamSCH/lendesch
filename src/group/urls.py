from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('groups', views.LenderGroupViewSet)

urlpatterns = router.urls
