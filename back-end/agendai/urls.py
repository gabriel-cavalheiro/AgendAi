
from agendai.views import escritorioViewSet, cadeiraViewSet, sala_reuniaoViewSet, agendamento_escritorioViewSet, agendamento_reuniaoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'escritorio', escritorioViewSet , basename='escritorio')
router.register(r'cadeira', cadeiraViewSet, basename='cadeira')
router.register(r'sala_reuniao', sala_reuniaoViewSet, basename='sala_reuniao')
router.register(r'agendaemnto_escritorio', agendamento_escritorioViewSet, basename='agendaemnto_escritorio')
router.register(r'agendaemnto_reuniao', agendamento_reuniaoViewSet, basename='agendaemnto_reuniao')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]