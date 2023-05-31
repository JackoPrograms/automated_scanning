FROM kalilinux/kali-rolling

WORKDIR /script

COPY . /script

ADD . /script

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script