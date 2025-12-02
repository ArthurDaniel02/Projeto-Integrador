from django.contrib import admin 
from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from sistema.views import AlunoViewSet, ProfessorViewSet, TurmaViewSet, MatriculaViewSet, PresencaViewSet,AlunoRepViewSet
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
router = DefaultRouter()
router.register(r'alunos', AlunoViewSet) 
router.register(r'professores', ProfessorViewSet) 
router.register(r'turmas', TurmaViewSet) 
router.register(r'matriculas', MatriculaViewSet) 
router.register(r'presencas', PresencaViewSet) 
router.register(r'alunosrep',AlunoRepViewSet)

urlpatterns = [
 path('admin/', admin.site.urls), 
 path('api/', include(router.urls)), 
 path('api/token/', obtain_auth_token),
 path('api/schema/', SpectacularAPIView.as_view(), name='schema'), 
 path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
 path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
