FROM alpine

RUN echo "---- install Python ----" && \
    apk add --no-cache python3 && \
    \
    echo "---- install pip ----" && \
    apk add py3-pip && \
    \
    echo "---- install vim ----" && \
    apk add vim

WORKDIR /app
COPY . /app/

RUN pip3 install --requirement ./requirements.txt
EXPOSE 5000

CMD [ "python3", "./app/app.py", "--host"]
