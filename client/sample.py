from elasticsearch import Elasticsearch




def create_index():
	# by default we don't sniff, ever
	es = Elasticsearch([
    	{'host': '192.168.168.176'},
		])

	# ignore 400 cause by IndexAlreadyExistsException when creating an index
	es.indices.create(index='test-index', ignore=400)

	a = es.indices.exists(index='test-index')
	print(a)



