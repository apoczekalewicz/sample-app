FROM ubi8
RUN dnf -y install python3
WORKDIR /
ADD ./main.py .
ADD ./robots.txt .
EXPOSE 8080
USER 1001
CMD python3 /main.py
