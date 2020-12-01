FROM  python:3

WORKDIR /usr/src/app

RUN pip install discord

COPY . .

EXPOSE 80

CMD [ "python", "main.py" ]

