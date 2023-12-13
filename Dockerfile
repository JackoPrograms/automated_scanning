FROM kalilinux/kali-bleeding-edge

WORKDIR /script

COPY . /script

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

