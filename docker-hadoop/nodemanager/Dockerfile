FROM pramodraob/hadoop-base:latest

MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>

HEALTHCHECK CMD curl -f http://localhost:8042/ || exit 1

ADD nodemanager/run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8042

RUN apt-get update && apt-get install python3-venv python3-pip -y
RUN python3 -m venv /opt/hvenv
ENV PATH="/opt/hvenv/bin:$PATH"

COPY req.txt /tmp/req.txt
RUN pip install -r /tmp/req.txt

CMD ["/run.sh"]
