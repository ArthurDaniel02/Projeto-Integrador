"""
URL configuration for edutrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # painel administrativo do Django
from django.urls import path, include # path para rotas, include para incluir outras URLs
from rest_framework.routers import DefaultRouter # router que gera rotas para ViewSets
from sistema.views import AlunoViewSet, ProfessorViewSet, TurmaViewSet, MatriculaViewSet, PresencaViewSet # ViewSets registrados no router

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet) # registra endpoints para alunos: /api/alunos/
router.register(r'professores', ProfessorViewSet) # registra endpoints para professores: /api/professores/
router.register(r'turmas', TurmaViewSet) # registra endpoints para turmas: /api/turmas/
router.register(r'matriculas', MatriculaViewSet) # registra endpoints para matriculas: /api/matriculas/
router.register(r'presencas', PresencaViewSet) # registra endpoints para presencas: /api/presencas/

urlpatterns = [
 path('admin/', admin.site.urls), # rota do Django admin
 path('api/', include(router.urls)), # inclui rotas geradas pelo router sob o prefixo/api/
]
