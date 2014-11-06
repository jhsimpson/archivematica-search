#vcr_sample.py
from elasticsearch import Elasticsearch
import pytest
import requests
import vcr
from client import sample

ES_URL='http://192.168.168.176:9200'

@vcr.use_cassette('fixtures/vcr_cassettes/es_test.yaml')
def test_get_es():
    response = requests.get(ES_URL)
    assert 'for Search' in response.text

@vcr.use_cassette('fixtures/vcr_cassettes/es_index_test.yaml')    
def test_create_index():
	sample.create_index()
	response = requests.get(ES_URL + '/_cat/indices?v')
	assert 'test-index' in response.text

@vcr.use_cassette('fixtures/vcr_cassettes/es_index_exists.yaml')
def test_index_exists():
	sample.create_index()
	es = Elasticsearch([
    	{'host': '192.168.168.176'},
		])
	es.indices.exists(index='test-index')
