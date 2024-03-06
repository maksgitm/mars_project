import flask
from data import db_session
from flask import jsonify
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
    jobs = db_sess.query(Jobs).first()
    return jsonify(
        {
            'jobs': [item.to_dict(only=('id', 'team_leader', 'job', 'work_size',
                                        'collaborators', 'start_date', 'end_date', 'is_finished')) for item in jobs]
        }
    )
