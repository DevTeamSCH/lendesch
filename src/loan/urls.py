from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('loans', views.LoanViewSet)
router.register('resources', views.ResourceViewSet)
router.register('resource-type', views.ResourceTypeViewSet)
router.register('remarks', views.RemarkViewSet)

urlpatterns = router.urls
