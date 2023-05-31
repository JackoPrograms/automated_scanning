FROM kalilinux/kali-rolling

WORKDIR /script

COPY . .

ADD . .

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script