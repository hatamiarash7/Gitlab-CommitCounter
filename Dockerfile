FROM python:3-alpine

WORKDIR /usr/local/share/

COPY counter.py /usr/local/share/

RUN python -m pip install requests

CMD ["python", "counter.py"]
