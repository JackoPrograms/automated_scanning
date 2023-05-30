FROM kalilinux/kali-rolling

WORKDIR /script

COPY . /script

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "-d", "-s", "-x" ]

VOLUME ./script