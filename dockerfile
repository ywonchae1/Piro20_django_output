FROM python
RUN apt-get update
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt && python server/manage.py collectstatic --no-input
EXPOSE 8000
CMD ['python' 'server/manage.py', 'runserver', '0.0.0.0:8000']