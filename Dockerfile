FROM python:3.7.7

WORKDIR /usr/local/share/

COPY counter.py /usr/local/share/

RUN python -m pip install requests

CMD ["python", "counter.py"]
