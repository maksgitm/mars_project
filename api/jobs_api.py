import flask
from data import db_session
from flask import jsonify, make_response, request
from data.jobs import Jobs
from sqlalchemy_serializer import SerializerMixin


blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs': [item.to_dict(only=('id', 'team_leader', 'job', 'work_size',
                                        'collaborators', 'start_date', 'end_date', 'is_finished')) for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>')
def get_one_job(job_id):
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if jobs:
        return jsonify(
            {
                'jobs': [jobs.to_dict(only=('id', 'team_leader', 'job', 'work_size',
                                            'collaborators', 'start_date', 'end_date', 'is_finished'))]
            }
        )
    else:
        return make_response({'ERROR': 'Not found'}, 404)


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        end_date=request.json['end_date'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})
