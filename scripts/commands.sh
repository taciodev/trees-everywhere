#!/bin/sh

set -e

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  echo "⏳ Aguardando PostgreSQL em $POSTGRES_HOST:$POSTGRES_PORT..."
  sleep 2
done

echo "✅ PostgreSQL disponível em $POSTGRES_HOST:$POSTGRES_PORT"

mkdir -p /data/web/static /data/web/media
chown -R duser:duser /data/web/static /data/web/media 2>/dev/null || true
chmod -R 700 /data/web/static /data/web/media 2>/dev/null || true

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin")
EOF

python manage.py runserver 0.0.0.0:8000
