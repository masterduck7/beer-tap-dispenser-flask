FROM python:3.10-alpine
 
WORKDIR /code
 
COPY requirements.txt /code
RUN pip install -r requirements.txt
 
COPY . /code
 
EXPOSE 8000
CMD [ "flask", "run","--host","0.0.0.0","--port","8000"]