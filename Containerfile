FROM ubi8:latest
RUN dnf -y install python3
WORKDIR /
ADD ./main.py .
EXPOSE 8080
USER 1001
CMD python3 /main.py
