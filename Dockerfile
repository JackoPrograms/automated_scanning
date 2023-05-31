FROM kalilinux/kali-rolling

WORKDIR /script

ADD . ./result

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script