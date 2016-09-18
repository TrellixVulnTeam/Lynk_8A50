from app import app
from random import randint
from flask import Flask, jsonify

adjectives, adverbs, nouns = [], [], []
with open("C:\\Users\\amcafee\\Documents\\GitHub\\Lynk\\adjectives\\adjectives.txt") as f:
	adjectives = f.read().split()
with open("C:\\Users\\amcafee\\Documents\\GitHub\\Lynk\\adverbs\\adverbs.txt") as f:
	adverbs = f.read().split()
with open("C:\\Users\\amcafee\\Documents\\GitHub\\Lynk\\nouns\\nouns.txt") as f:
	nouns = f.read().split()

print((adjectives[0]  + adjectives[1]).encode("utf-8", errors='waaaat'))



@app.route('/')
@app.route('/index')
def index():
	return "Hello, World. Fucker"

@app.route('/shortener')
def shortener():
	return (adjectives[randint(0,len(adjectives))] + adverbs[randint(0,len(adverbs))] + nouns[randint(0,len(nouns))])

@app.route('/test')
def tester():
	return "Testing"

@app.route('/nuts', methods=['GET'])
def get_tasks():
	nuts = [
		{
			'id': u'amcafee',
			'title': u'http://www.sexandsubmission.com',
			'description': u'squirr.el/' + (adjectives[randint(0,len(adjectives))] + adverbs[randint(0,len(adverbs))] + nouns[randint(0,len(nouns))]),
		},
		{
			'id': u'aelahi',
			'title': u'https://www.bdsmgrandmamidgetshit.com',
			'description': u'squirr.el/' + (adjectives[randint(0,len(adjectives))] + adverbs[randint(0,len(adverbs))] + nouns[randint(0,len(nouns))]), 
		}
	]
	return jsonify({'nuts': nuts})

@app.route('/nuts/<int:task_id>', methods=['PUT'])
def update_nut(task_id):
    nut = [nut for nut in nuts if nut['id'] == task_id]
    if len(nut) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    return jsonify({'task': task[0]})
