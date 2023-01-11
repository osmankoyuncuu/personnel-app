from django.urls import path,include
from rest_framework import routers
from .views import (
    DepartmentView,
    DepartmentPersonalView,
    PersonnelView,
)

router = routers.DefaultRouter()
router.register("department", DepartmentPersonalView )
router.register("personnel", PersonnelView )


urlpatterns = [
    path('', DepartmentView.as_view()),
    path('', include(router.urls)),
    #path('department/<str:department>/', DepartmentPersonalView.as_view())
]