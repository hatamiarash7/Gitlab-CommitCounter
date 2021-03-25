FROM python:3.10.0a4-alpine

WORKDIR /usr/local/share/

COPY counter.py /usr/local/share/

RUN python -m pip install requests

CMD ["python", "counter.py"]
