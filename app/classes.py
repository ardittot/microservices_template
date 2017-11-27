from flask import request, jsonify, abort
from database.models import db, Bucketlist, Ex1

def class_bucketlists(app):
	@app.route('/bucketlists/', methods=['POST', 'GET'])
	def bucketlists():
	    if request.method == "POST":
	        name = str(request.data.get('name', ''))
	        if name:
	            bucketlist = Bucketlist(name=name)
	            bucketlist.save()
	            response = jsonify({
	                'id': bucketlist.id,
	                'name': bucketlist.name,
	                'date_created': bucketlist.date_created,
	                'date_modified': bucketlist.date_modified
	            })
	            response.status_code = 201
	            return response
	    else:
	        # GET
	        bucketlists = Bucketlist.get_all()
	        results = []

	        for bucketlist in bucketlists:
	            obj = {
	                'id': bucketlist.id,
	                'name': bucketlist.name,
	                'date_created': bucketlist.date_created,
	                'date_modified': bucketlist.date_modified
	            }
	            results.append(obj)
	        response = jsonify(results)
	        response.status_code = 200
	        return response

def class_ex1(app):
	@app.route('/ex1', methods=['POST','GET'])
	def ex1():
	    if request.method == 'POST':
	        try:
	            id = request.get_json()["id"]
	            amount = request.get_json()["amount"]
	            description = request.get_json()["description"]

	            reg = Ex1(id=id, amount=amount, description=description)
	            db.session.add(reg)
	            db.session.commit()
	            return jsonify(204)
	        except (RuntimeError, TypeError, NameError, IntegrityError):
	            return jsonify(400)

	    else:
	        data = Ex1.query.all() #fetch all products on the table
	        data_all = []
	        for d in data:
	            data_all.append([d.id, d.amount, d.description]) #prepare visual data
	        return jsonify(products=data_all)

