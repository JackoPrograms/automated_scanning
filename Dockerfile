FROM kalilinux/kali-rolling

WORKDIR /script

COPY . .

ADD ./result /result

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]

VOLUME ./script