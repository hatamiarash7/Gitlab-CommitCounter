FROM python:3.12.3-alpine

ARG DATE_CREATED

LABEL maintainer="Arash Hatami <hatamiarash7@gmail.com>"
LABEL org.opencontainers.image.created=$DATE_CREATED
LABEL org.opencontainers.image.authors="hatamiarash7"
LABEL org.opencontainers.image.vendor="hatamiarash7"
LABEL org.opencontainers.image.title="Gitlab-CommitCounter"
LABEL org.opencontainers.image.description="Count commits for gitlab project"
LABEL org.opencontainers.image.source="https://github.com/hatamiarash7/Gitlab-CommitCounter"

WORKDIR /usr/local/share/

COPY counter.py /usr/local/share/

RUN python -m pip install --no-cache-dir requests==2.28.2

CMD ["python", "counter.py"]
