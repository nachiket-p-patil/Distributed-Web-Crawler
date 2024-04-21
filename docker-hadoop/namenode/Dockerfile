FROM pramodraob/hadoop-base:latest

MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>

HEALTHCHECK CMD curl -f http://localhost:9870/ || exit 1

ENV HDFS_CONF_dfs_namenode_name_dir=file:///hadoop/dfs/name
RUN mkdir -p /hadoop/dfs/name
VOLUME /hadoop/dfs/name

ADD namenode/run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 9870

RUN apt-get update && apt-get install python3-venv python3-pip -y
RUN python3 -m venv /opt/hvenv
ENV PATH="/opt/hvenv/bin:$PATH"

COPY req.txt /tmp/req.txt
RUN pip install -r /tmp/req.txt

CMD ["/run.sh"]
