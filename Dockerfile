FROM kalilinux/kali-rolling

WORKDIR /script

VOLUME . /script

COPY . /script

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script