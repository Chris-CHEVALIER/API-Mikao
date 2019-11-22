from django.conf.urls import url
from rest_framework import routers
from api.mikao.views import UserViewSet, TreatmentViewSet, SymptomViewSet, FavoriteListViewSet, CustomView
from rest_framework_swagger.views import get_swagger_view
from api.mikao import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('treatments', TreatmentViewSet)
router.register('symptoms', SymptomViewSet)
router.register('favoriteLists', FavoriteListViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url('customview', CustomView.as_view()),
    url('docs', schema_view),
]

urlpatterns += router.urls