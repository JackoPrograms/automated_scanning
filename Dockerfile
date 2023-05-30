FROM kalilinux/kali-rolling

WORKDIR /script

COPY . /script

RUN bash requirements.sh

CMD [ "bash", "script.sh" ]

VOLUME ./script