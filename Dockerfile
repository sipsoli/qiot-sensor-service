FROM quay.io/olivier_sips/qiot-sensor-service-base:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

ENV FLASK_APP /usr/src/app/app.py
ENV FLASK_APP_PORT 5000
ENV FLASK_APP_HOST "0.0.0.0"
ENV FLASK_APP_LOG "--access-logfile"
ENV FLASK_APP_LOG_FILE "/var/log/gunicorn.log"

ENV GUNICORN_CMD_ARGS "--bind=$FLASK_APP_HOST:$FLASK_APP_PORT $FLASK_APP_LOG $FLASK_APP_LOG_FILE"

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "app:app"]
