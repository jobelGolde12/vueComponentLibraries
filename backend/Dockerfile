FROM python:3.12.4

RUN apt-get update && apt-get install -y \
    libpq-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /backend

COPY requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir gunicorn
RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend


EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "FlaskApp:app"]


#for real world 