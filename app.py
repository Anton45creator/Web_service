from models import *
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import requests
import os
import psycopg2


app = Flask(__name__)
app.config.from_pyfile("config.py")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

client = app.test_client()
db = SQLAlchemy(app)
api = Api(app, prefix='/api/v1.0')


def get_info(number) -> int:
    payload = {'count': number}
    response = requests.get('https://jservice.io/api/random',
                            params=payload)
    data = response.json()
    return data


class Quiz(Resource):

    def post(self):
        json_data = request.get_json()
        if 'number' not in json_data:
            return jsonify(str="The key number doesn't exist")
        number = json_data['number']
        dictionary = get_info(number)
        for key in dictionary:
            peter = db.session.query(QuizModel).filter_by(id=key['id']).first()
            if peter is None:
                db.session.add(
                    QuizModel(
                        id=key['id'],
                        answer=key['answer'],
                        question=key['question'],
                        date_of_creation=key['created_at']
                    )
                )
                db.session.commit()

        return {'code': 201, 'message': f'Ok!'}, 201


api.add_resource(Quiz, '/number/', methods=['POST'])

if __name__ == '__main__':
    app.run()
