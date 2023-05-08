FROM ubi9
RUN dnf -y install python3 && dnf -y remove dnf
WORKDIR /
ADD ./main.py .
EXPOSE 8080
USER 1001
CMD python3 /main.py
