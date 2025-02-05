# Utiliser une image Python optimisée
FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir /pokemon_api
WORKDIR /pokemon_api
COPY . /pokemon_api/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000

# Commande de démarrage
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pokemon.wsgi:application"]