FROM kalilinux/kali-rolling

WORKDIR /script

VOLUME . ./

COPY . /script

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]