FROM kalilinux/kali-rolling

WORKDIR /script

COPY . /script

VOLUME /automated_scanning

RUN bash requirements.sh

ENTRYPOINT [ "bash", "script.sh" ]

CMD [ "", "", "" ]