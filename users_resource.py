from flask import jsonify, request
from flask_restful import reqparse, abort, Api, Resource

from data import db_session
from data.users import User
from users_parser import parser


class UsersResource(Resource):
    def abort_if_jobs_not_found(self, user_id):
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        if not users:
            abort(404, message=f"Jobs {user_id} not found")

    def get(self, user_id):
        self.abort_if_jobs_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'users': users.to_dict(
            only=('name', 'surname', 'age', 'position',
                  'speciality', 'address', 'email', 'hashed_password', 'modified_date'))})

    def delete(self, user_id):
        self.abort_if_jobs_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('name', 'surname', 'age', 'position',
                  'speciality', 'address', 'email', 'hashed_password', 'modified_date')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            modified_date=args['modified_date'],
        )
        user.set_password(args['password'])
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
