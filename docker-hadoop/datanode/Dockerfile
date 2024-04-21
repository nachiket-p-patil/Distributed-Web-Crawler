FROM pramodraob/hadoop-base:latest

MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>

HEALTHCHECK CMD curl -f http://localhost:9864/ || exit 1

ENV HDFS_CONF_dfs_datanode_data_dir=file:///hadoop/dfs/data
RUN mkdir -p /hadoop/dfs/data
VOLUME /hadoop/dfs/data

ADD datanode/run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 9864

RUN apt-get update && apt-get install python3-venv python3-pip -y
RUN python3 -m venv /opt/hvenv
ENV PATH="/opt/hvenv/bin:$PATH"

COPY req.txt /tmp/req.txt
RUN pip install -r /tmp/req.txt

CMD ["/run.sh"]
