FROM kalilinux/kali-rolling

WORKDIR /script

COPY . /script

RUN bash requirements.sh

ENTRYPOINT [ "bash", "-s -x -d" ]

CMD [ "bash", "script.sh" ]

VOLUME ./script