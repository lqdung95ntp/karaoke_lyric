FROM python:3.9.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt karaoke_lyric/ /app/

# install dependencies
RUN python3 -m pip install --upgrade pip &&\
    python3 -m pip install --trusted-host pypi.python.org -r requirements.txt
# hadolint ignore=DL3013

# make migration
RUN python3 manage.py makemigrations && \
    python3 manage.py migrate

# expose port 3001
EXPOSE 3001

# run django server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:3001"]
