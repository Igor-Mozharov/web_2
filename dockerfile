FROM python:3.11

MAINTAINER Igor Mozharov "r5@ukr.net"

COPY . .

WORKDIR /power9bot

ENTRYPOINT ["python"]

CMD ["main.py"]

