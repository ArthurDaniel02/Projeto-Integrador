from pathlib import Path
import inspect
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ue0!bz172d6)6a--yjf)yy72c0r#3au(h_zz4+sch8kh4^$n5$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'sistema',
    'django_filters',
    'drf_spectacular',
]
REST_FRAMEWORK = {
 'DEFAULT_AUTHENTICATION_CLASSES': [
 'rest_framework.authentication.TokenAuthentication',
 'rest_framework.authentication.SessionAuthentication',
 ],
 'DEFAULT_PERMISSION_CLASSES': [
 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
 ],
 'DEFAULT_FILTER_BACKENDS': [
 'django_filters.rest_framework.DjangoFilterBackend',

 ],
 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'API Sistema de Chamada de Alunos',

    'DESCRIPTION': inspect.cleandoc("""
    ## Bem-vindo à API Sistema de Chamada de Alunos!

    ### Professores
    - **Listar Professores** — `GET /api/professores/` *(público)*
    - **Professor específico** — `GET /api/professores/{id}/` *(público)*
    - **Criar Professores** — `POST /api/professores/` *(autenticado)*
    - **Atualizar Professores** — `PUT/PATCH /api/professores/{id}/` *(autenticado)*
    - **Excluir Professores** — `DELETE /api/professores/{id}/` *(autenticado)*

    ### Alunos
    - **Listar Alunos** — `GET /api/alunos/` *(público)*
    - **Aluno específico** — `GET /api/alunos/{id}/` *(público)*
    - **Criar Alunos** — `POST /api/alunos/` *(autenticado)*
    - **Atualizar Alunos** — `PUT/PATCH /api/alunos/{id}/` *(autenticado)*
    - **Excluir Alunos** — `DELETE /api/alunos/{id}/` *(autenticado)*

    ### Turmas
    - **Listar Turmas** — `GET /api/turmas/` *(público)*
    - **Turma específica** — `GET /api/turmas/{id}/` *(público)*
    - **Criar Turmas** — `POST /api/turmas/` *(autenticado)*
    - **Atualizar Turmas** — `PUT/PATCH /api/turmas/{id}/` *(autenticado)*
    - **Excluir Turmas** — `DELETE /api/turmas/{id}/` *(autenticado)*

    ---

    ### Rotas de Relacionamento

    - **Professor ↔ Turma (1:N)**  
        - `GET /api/professores/{id}/turmas/` - lista turmas lecionadas pelo professor  
        - `POST /api/turmas/{id}/atribuir-professor/` - atribui professor à turma  

    - **Turma ↔ Aluno (N:N)**  
        - `GET /api/turmas/{id}/alunos/` - lista alunos matriculados  
        - `POST /api/turmas/{id}/matricular-aluno/` - matricula aluno na turma  

    - **Turma ↔ Representante (1:1)**  
        - `PUT /api/turmas/{id}/definir-representante/` - define aluno como representante  
        - `GET /api/turmas/{id}/representante/` - retorna representante
                                    
    ---
                                    
    ### Autenticação
    Use o endpoint `/api/token/` para obter seu token e inclua no cabeçalho:

    ```
    Authorization: Token <sua_chave>
    ```
    """),
    
    'VERSION': '1.0.0',

    'SERVE_INCLUDE_SCHEMA': False,

    'SECURITY': [{'TokenAuth': []}],

    'COMPONENTS': {
        'securitySchemes': {
            'TokenAuth': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization',
                'description': 'Use o formato: Token <sua_chave>',
            },
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'edutrack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'edutrack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'