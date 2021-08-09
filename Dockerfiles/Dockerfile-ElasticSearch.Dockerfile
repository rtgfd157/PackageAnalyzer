FROM docker.elastic.co/elasticsearch/elasticsearch:7.14.0

# RUN  yes | curl -XPUT 'localhost:9200/elastic_packages_tree?pretty'

# working for now but show container with yellow mark on vs code docker extenstion
HEALTHCHECK CMD curl -XPUT  'localhost:9200/elastic_packages_tree?pretty' | grep -E '^green'

# another idea is to make another image in compose file of python that will have script with curl command
# and will be depend on elasticsearch image.
# https://stackoverflow.com/questions/35526532/how-to-add-an-elasticsearch-index-during-docker-build