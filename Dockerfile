FROM python:3.9.13-alpine

ARG DATE_CREATED

LABEL maintainer="Arash Hatami <hatamiarash7@gmail.com>"
LABEL org.opencontainers.image.created=$DATE_CREATED
LABEL org.opencontainers.image.authors="hatamiarash7"
LABEL org.opencontainers.image.vendor="hatamiarash7"
LABEL org.opencontainers.image.title="Directory Index"
LABEL org.opencontainers.image.description="The first Persian comment system"
LABEL org.opencontainers.image.source="https://github.com/hatamiarash7/docker-directory-index"

WORKDIR /usr/local/share/

COPY counter.py /usr/local/share/

RUN python -m pip install --no-cache-dir requests

CMD ["python", "counter.py"]
