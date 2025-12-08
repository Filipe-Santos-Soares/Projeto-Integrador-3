#!/bin/bash

echo "===== Iniciando deploy do Django no Render ====="

# Ativar virtualenv
#source .venv/bin/activate

# Instalar dependências (caso necessário)
pip install -r Requirements.txt

# Migrar banco de dados
echo "Aplicando migrações..."
python manage.py makemigrations
python manage.py migrate

# Coletar arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# (Opcional) criar superusuário admin se não existir

# Criar superusuário automaticamente se não existir
echo "Verificando se o superusuário existe..."
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-admin}
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-admin@admin.com}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-admin}

echo "from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
" | python manage.py shell

# Inicia o Gunicorn
echo "Iniciando Gunicorn..."
gunicorn projetointegrador3.wsgi:application --bind 0.0.0.0:$PORT
