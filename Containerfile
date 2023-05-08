FROM registry.redhat.io/ubi8/ubi@sha256:e3311058176628ad7f0f288f894ed2afef61be77ad01d53d5b69bca0f6b6cec1
RUN dnf -y install python3
WORKDIR /
ADD ./main.py .
EXPOSE 8080
USER 1001
CMD python3 /main.py
