FROM python:3.9-alpine
WORKDIR /app
COPY . .
ENTRYPOINT ["python"]
CMD ["main.py"]
