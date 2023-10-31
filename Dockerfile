FROM python:3.9

COPY requirements.txt /requirements.txt
COPY config.yml /config.yml

RUN python3.9 -m pip install --upgrade pip
RUN python3.9 -m pip install -r requirements.txt

COPY bot.py /bot.py

ENTRYPOINT ["python", "bot.py"]