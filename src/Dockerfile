FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
RUN pip3 install -r req.txt
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
