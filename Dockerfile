FROM kalilinux/kali-rolling

WORKDIR /script

VOLUME . .

COPY . .

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script