
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

COPY  alzer_Api.py .
COPY requirements.txt .
COPY final_model_cat.pk1 .
COPY final_scaler_cat.pk1 .
COPY col_names_cat.pk1 .

# Upgrade pip to the latest version
RUN pip install --upgrade pip

RUN pip install numpy==1.21.4

# Install the rest of the dependencies from requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "alzer_Api:app"]
