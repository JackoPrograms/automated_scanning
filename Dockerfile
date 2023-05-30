FROM alpine:3.14

WORKDIR /script

COPY . /script

RUN pip3 install -r requirements.txt

CMD [ "bash", "script.sh" ]

VOLUME ./script