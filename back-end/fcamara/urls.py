from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from agendai.views import escritorioViewSet, cadeiraViewSet, sala_reuniaoViewSet, agendamento_escritorioViewSet, agendamento_reuniaoViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="cristianpcpaes@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'escritorio', escritorioViewSet , basename='escritorio')
router.register(r'cadeira', cadeiraViewSet, basename='cadeira')
router.register(r'sala_reuniao', sala_reuniaoViewSet, basename='sala_reuniao')
router.register(r'agendamento_escritorio', agendamento_escritorioViewSet, basename='agendamento_escritorio')
router.register(r'agendamento_reuniao', agendamento_reuniaoViewSet, basename='agendamento_reuniao')

urlpatterns = [
    path('', RedirectView.as_view(url='admin/')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('documentacao/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
