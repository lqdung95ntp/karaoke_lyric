FROM python:3.9.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt karaoke_lyric/ /app/

# hadolint ignore=DL3013
# install dependencies
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# make migration
RUN python manage.py makemigrations && \
    python manage.py migrate

# expose port 3001
EXPOSE 3001

# run django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:3001"]
