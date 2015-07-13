FROM elasticsearch

MAINTAINER blacktop, https://github.com/blacktop

RUN plugin -install kafka-river -url https://github.com/mariamhakobyan/elasticsearch-river-kafka/releases/download/v1.3.0/elasticsearch-river-kafka-1.3.0-plugin.zip

COPY elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
