FROM debian:bullseye-slim

USER root

# Zaroori packages aur 'xauth' install karein (Taki error na aaye)
RUN apt-get update && apt-get install -y \
    wget xvfb python3 curl \
    libnss3 libasound2 libgbm-dev xauth \
    && rm -rf /var/lib/apt/lists/*

# FeelingSurf officially install karein
RUN wget https://github.com/feelingsurf/viewer/releases/download/2.5.0/FeelingSurfViewer-linux-amd64-2.5.0.deb -O fs.deb && \
    apt-get update && apt-get install -y ./fs.deb && \
    rm fs.deb

# Aapka Token
ENV access_token=a66728c47adfaacd86291986d9f9827e
RUN mkdir -p /tmp /dev/shm

# Aapki app.py file copy karein
COPY app.py /app.py

# CHANGE: Hugging Face port 7860 se Northflank port 8080 kar diya
EXPOSE 8080

ENTRYPOINT ["python3", "-u", "/app.py"]
