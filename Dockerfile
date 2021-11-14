FROM python:buster
WORKDIR /app
COPY . .
ENTRYPOINT ["python"]
CMD ["main.py"]
