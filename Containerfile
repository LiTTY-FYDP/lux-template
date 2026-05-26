FROM python:3.14.5-slim
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir .
CMD ["lux_template"]
