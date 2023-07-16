FROM apache/airflow:2.5.0-python3.8


WORKDIR /app
USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    libsasl2-dev \
    libkrb5-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/requirements.txt


USER airflow
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt
USER root
ENV AIRFLOW_HOME /opt/airflow


COPY . /app
COPY dags /opt/airflow/dags
COPY plugins /opt/airflow/plugins
COPY logs /opt/airflow/logs
COPY helper /opt/airflow/helper

RUN chmod -R 777  /opt/airflow/logs/
RUN chmod -R 777 /opt/airflow/plugins/
RUN chmod -R 777 /opt/airflow/dags/
RUN chmod -R 777 /opt/airflow/helper

# USER airflow
# Set the default command to run when the container starts
#CMD ["airflow", "webserver"]
