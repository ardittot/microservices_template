import os
# local import
from app import create_app
from app.classes import class_bucketlists, class_ex1

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)

class_bucketlists(app)
class_ex1(app)

if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST'), port=int(os.getenv('FLASK_PORT')))
    # app.run()
# curl http://127.0.0.1:5000/
# curl -X GET http://127.0.0.1:5000/ex1
# curl -X POST -H "Content-Type: application/json" -d '{"amount":7000, "description":"bonuslala", "id":2}' http://127.0.0.1:5000/ex1
# curl -X GET http://127.0.0.1:5000/bucketlists/
# curl -X POST -H "Content-Type: application/json" -d '{"name":"Arditto T"}' http://127.0.0.1:5000/bucketlists/
