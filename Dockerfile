FROM ubuntu:20.04

RUN apt update
RUN apt install python3 python3-pip -y

RUN mkdir /app
WORKDIR /app

EXPOSE 80

COPY ./* ./
# RUN rm -rf env
RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
