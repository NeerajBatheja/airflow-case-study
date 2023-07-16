# How to Run This Project ?

## docker build
- docker build -t airflow2:local .
## run docker-compose-db-redis.yaml to setup postres and redis docker
- docker-compose -f docker-compose-db-redis.yaml
## postres creds will db: airflow , username:airflow , pass:airflow
- change host and port accordingly via airflow.cfg of postgres and redis
## initialize database
- docker run airflow2:local airflow db init
## now up airflow components using
- docker-compose up -d
## create user via docker exec command
- docker exec -it webserver_container_id /bin/bash
## after entering in bash use below command with changes accordingly 
- airflow users  create --role Admin --username neeraj --password neeraj --email hi@neerajbatheja.com --firstname neeraj --lastname batheja
## congrats you have setup project succesfully

# What This project is doing ?
- This project is about transforming data using some custom formula.
- Helper Folder have 3 files (2 inputs comission.csv and orders.csv) and one output file (transofrmed_data.csv)

Screenshots

![Screenshot](https://github.com/NeerajBatheja/airflow-case-study/blob/master/screenshots/screenshot%20airflow%201.png)
![Screenshot](https://github.com/NeerajBatheja/airflow-case-study/blob/master/screenshots/screenshot%20airflow%202.png)
![Screenshot](https://github.com/NeerajBatheja/airflow-case-study/blob/master/screenshots/screenshot%20airflow%203.png)
![Screenshot](https://github.com/NeerajBatheja/airflow-case-study/blob/master/screenshots/screenshot%20airflow%204.png)
![Screenshot](https://github.com/NeerajBatheja/airflow-case-study/blob/master/screenshots/screenshot%20airflow%205.png)
