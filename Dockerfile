FROM kalilinux/kali-rolling

WORKDIR /script

VOLUME . .

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script