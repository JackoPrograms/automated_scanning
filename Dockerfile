FROM kalilinux/kali-rolling

WORKDIR /script

COPY . .

ADD . /result

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script