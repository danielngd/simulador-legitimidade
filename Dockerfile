FROM praekeltfoundation/django-bootstrap

COPY . /app

RUN pip install -e .

ENV DJANGO_SETTINGS_MODULE simulador.settings
ARG SECRET_KEY
ENV SECRET_KEY $SECRET_KEY
ARG ALLOWED_HOSTS
ENV ALLOWED_HOSTS $ALLOWED_HOSTS

RUN django-admin collectstatic --noinput

#CMD ["simulador.wsgi:application", "--timeout", "1800"]