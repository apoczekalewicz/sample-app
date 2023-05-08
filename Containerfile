#FROM ubi8
FROM registry.redhat.io/rhel8/python-39@sha256:abc94eab0105261e801a79bccdcce23f1aa08d82b3d595fa9ed2666e36dff2ee
#RUN dnf -y install python3
WORKDIR /
ADD ./main.py .
ADD ./robots.txt .
EXPOSE 8080
USER 1001
CMD python3 /main.py
