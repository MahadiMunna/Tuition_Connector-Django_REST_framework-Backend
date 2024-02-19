from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views
router = DefaultRouter()

router.register('class',views.StudentClassViewset)
router.register('subject',views.SubjectViewset)
router.register('list',views.TuitionViewset)

urlpatterns = [
    path('', include(router.urls)),
]
