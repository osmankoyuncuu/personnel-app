from django.urls import path,include
from rest_framework import routers
from .views import DepartmentView, PersonnelView

router = routers.DefaultRouter()
router.register("department", DepartmentView )
router.register("personnel", PersonnelView )


urlpatterns = [
    path('', include(router.urls)),
]