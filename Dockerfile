FROM python:3.10-buster
WORKDIR /opt/app
ENV PYTHONPATH=/opt/app/platform_srv:/opt/app/inference
COPY inference ./inference
COPY platform_srv ./platform_srv
COPY requirements.txt main.py ./
RUN apt-get update \
    && apt-get install libgl1 -y
RUN pip install -r requirements.txt
CMD python main.py