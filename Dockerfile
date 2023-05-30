FROM kalilinux/kali-rolling

WORKDIR /script

COPY . /script

RUN pip3 install -r requirements.txt

CMD [ "bash", "script.sh" ]

VOLUME ./script