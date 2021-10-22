FROM python:3-alpine

COPY src/* /

RUN pip install --upgrade pip \
        && pip install -r requirements.txt

CMD [ "python", "./app.py" ]