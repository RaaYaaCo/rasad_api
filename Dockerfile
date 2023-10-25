FROM python:3.11.4-slim

RUN apt -y update && apt -y install gdal-bin  && \
    apt -y install gettext && rm -rf /var/lib/apt/lists/* && \
    apt autoclean


ARG port=8088
ENV GUNICORN_WORKER_NO=10
ENV GUNICORN_LISTENINIG_PORT=${port}
ENV GUNICORN_TIMEOUT=1900


WORKDIR /app
RUN mkdir media static
VOLUME [ "/app/media" ]
VOLUME [ "/app/static" ]
RUN pip3 install --upgrade pip 
COPY requirments.txt .
RUN pip3 install --no-cache-dir -r requirments.txt
COPY . .

RUN chmod +x start.sh
EXPOSE ${port}
CMD [ "./start.sh" ]


