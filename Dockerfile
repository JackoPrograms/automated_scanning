FROM kalilinux/kali-rolling

VOLUME /opt/app/data

WORKDIR /script

COPY . /script

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script