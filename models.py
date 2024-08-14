from app import db

class Employer(db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    company_name = db.Column(db.String(255))
    contact_number = db.Column(db.String(20))


class JobSeeker(db.Model):
    __tablename__ = 'job_seekers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    education = db.Column(db.String(255))
    experience = db.Column(db.Integer)
    skills = db.Column(db.Text)
    resume_path = db.Column(db.String(255))
    national_id = db.Column(db.String(10), unique=True)
    birthdate = db.Column(db.Date)
    marital_status = db.Column(db.String(20))
    employment_status = db.Column(db.String(20))
    major = db.Column(db.String(100))
    gender = db.Column(db.String(10))

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id', ondelete='CASCADE'))
    job_title = db.Column(db.String(255))
    qualifications = db.Column(db.Text)
    experience = db.Column(db.Text)
    skills = db.Column(db.Text)
    job_description = db.Column(db.Text)
    required_experience_years = db.Column(db.Integer)
    questions = db.relationship('TestQuestion', backref='job', cascade="all, delete-orphan", lazy='dynamic')

class Candidate(db.Model):
    __tablename__ = 'candidates'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'))
    seeker_id = db.Column(db.Integer, db.ForeignKey('job_seekers.id', ondelete='CASCADE'))
    test_passed = db.Column(db.Boolean, default=False)
    pdf_report_path = db.Column(db.String(255))
    hired = db.Column(db.Boolean, default=False)
    match_percentage = db.Column(db.Numeric(5, 2))

class TestQuestion(db.Model):
    __tablename__ = 'test_questions'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'))
    question_text = db.Column(db.Text)
    correct_answer = db.Column(db.String(255))
    options = db.Column(db.Text)

class TestResult(db.Model):
    __tablename__ = 'test_results'
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id', ondelete='CASCADE'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'))
    score = db.Column(db.Numeric(5, 2))
    passed = db.Column(db.Boolean)
