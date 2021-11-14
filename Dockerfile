FROM python:alpine
WORKDIR /app
COPY . .
ENTRYPOINT ["python"]
CMD ["main.py"]
