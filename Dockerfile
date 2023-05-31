FROM kalilinux/kali-rolling

VOLUME . .

WORKDIR /script

COPY . /script

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script