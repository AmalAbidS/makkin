from flask import Flask, request, render_template, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
import pymysql
import openai
import os
import json
import PyPDF2

app = Flask(__name__)

#app.secret_key = ''

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Replace with your OpenAI API key
#openai.api_key = ''

#def get_db_connection():
 #   return pymysql.connect(
  #      host='localhost',
   #     user='root',
    #    password='',
     #   db='MakkinDB',
      #  charset='utf8mb4',
       # cursorclass=pymysql.cursors.DictCursor
    #)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor()

        # Check in job_seekers first
        cursor.execute("SELECT * FROM job_seekers WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user['id']
            session['user_role'] = 'job-seeker'
            session['user_name'] = user['name']
            return redirect(url_for('job_seekers_dashboard'))
        # If not found in job_seekers, check employers
        cursor.execute("SELECT * FROM employers WHERE email = %s AND password = %s", (email, password))
        employer = cursor.fetchone()

        if employer:
            session['user_id'] = employer['id']
            session['user_role'] = 'employer'
            session['user_name'] = employer['name']
            return redirect(url_for('employer_dashboard'))
        flash('البريد الإلكتروني أو كلمة المرور غير صحيحة.', 'error')
        cursor.close()
        connection.close()

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('تم تسجيل الخروج بنجاح.', 'success')
    return redirect(url_for('index'))


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

@app.route('/signup/job_seeker', methods=['GET', 'POST'])
def signup_job_seeker():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        education = request.form['education']
        experience = request.form['experience']
        skills = ','.join(request.form.getlist('skills[]'))
        national_id = request.form['national_id']
        birthdate = request.form['birthdate']
        marital_status = request.form['marital_status']
        employment_status = request.form['employment_status']
        major = request.form['major']
        gender = request.form['gender']

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM job_seekers WHERE national_id = %s", (national_id,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('رقم الهوية موجود بالفعل. الرجاء استخدام رقم آخر.', 'error')
        else:
            try:
                sql = """
                INSERT INTO job_seekers (name, email, password, education, experience, skills, national_id, birthdate, marital_status, employment_status, major, gender)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (name, email, password, education, experience, skills, national_id, birthdate, marital_status, employment_status, major, gender))
                connection.commit()
                flash('تم إنشاء الحساب بنجاح!', 'success')
            except pymysql.MySQLError as e:
                flash('حدث خطأ أثناء إنشاء الحساب.', 'error')
                print(e)
                
        cursor.close()
        connection.close()

    return render_template('signup_job_seeker.html')

@app.route('/signup/employer', methods=['GET', 'POST'])
def signup_employer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        company_name = request.form['company_name']
        contact_number = request.form['contact_number']

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM employers WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('البريد الإلكتروني موجود بالفعل. الرجاء استخدام بريد آخر.', 'error')
        else:
            try:
                sql = """
                INSERT INTO employers (name, email, password, company_name, contact_number)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (name, email, password, company_name, contact_number))
                connection.commit()
                flash('تم إنشاء الحساب بنجاح!', 'success')
            except pymysql.MySQLError as e:
                flash('حدث خطأ أثناء إنشاء الحساب.', 'error')
                print(e)

        cursor.close()
        connection.close()

    return render_template('signup_employer.html')

@app.route('/job_seekers_dashboard')
def job_seekers_dashboard():
    if 'user_id' in session and session['user_role'] == 'job-seeker':
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT name FROM job_seekers WHERE id = %s"
            cursor.execute(sql, (session['user_id'],))
            user = cursor.fetchone()
        connection.close()
        return render_template('job_seekers_dashboard.html', username=user['name'])
    return redirect(url_for('login'))

@app.route('/employer_dashboard')
def employer_dashboard():
    if 'user_id' in session and session['user_role'] == 'employer':
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT company_name FROM employers WHERE id = %s"
            cursor.execute(sql, (session['user_id'],))
            user = cursor.fetchone()
        connection.close()
        return render_template('employer_dashboard.html', company_name=user['company_name'])
    return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
def job_seeker_profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()
    cursor = connection.cursor()

    if session['user_role'] == 'job-seeker':
        user_query = "SELECT * FROM job_seekers WHERE id = %s"
        update_query = """
            UPDATE job_seekers 
            SET name = %s, email = %s, password = %s, 
                education = %s, experience = %s, 
                skills = %s, resume_path = %s,
                national_id = %s, birthdate = %s, 
                marital_status = %s, employment_status = %s,
                major = %s, gender = %s
            WHERE id = %s

        """
    else:
        user_query = "SELECT * FROM employers WHERE id = %s"
        update_query = """
            UPDATE employers 
            SET name = %s, email = %s, password = %s, 
                company_name = %s, contact_number = %s
            WHERE id = %s
        """

    cursor.execute(user_query, (session['user_id'],))
    user = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        education = request.form.get('education', '')
        experience = request.form.get('experience', '')
        skills = ','.join(request.form.getlist('skills[]'))
        national_id = request.form.get('nationalId', '')
        birthdate = request.form.get('birthdate', '')
        marital_status = request.form.get('maritalStatus', '')
        employment_status = request.form.get('employmentStatus', '')
        major = request.form.get('major', '')
        gender = request.form.get('gender', '')
        resume_path = user['resume_path']

        if password:
            hashed_password = password  # استخدم تشفير كلمات المرور الحقيقي هنا
        else:
            hashed_password = user['password']

        if 'resume' in request.files:
            resume_file = request.files['resume']
            if resume_file.filename:
                resume_path = 'uploads/' + secure_filename(resume_file.filename)
                resume_file.save(resume_path)

        cursor.execute(update_query, (name, email, hashed_password, education, experience, skills, resume_path, national_id, birthdate, marital_status, employment_status, major, gender, session['user_id']))
        connection.commit()

        flash('تم تحديث الملف الشخصي بنجاح.', 'success')

    cursor.close()
    connection.close()

    return render_template('job_seeker_profile.html', user=user)

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are CV Evaluation Bot. Check the CV and give detailed suggestions for improvement based on it. Always provide thorough and accurate evaluations and suggestions in Arabic. Make your response organized with new lines, numbering, headings, commas, periods... . Format your response using HTML tags for headings. Note: don't write تقييم السيرة الذاتية"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"].strip()

@app.route('/cv_evaluation', methods=['GET', 'POST'])
def cv_evaluation():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('cv_evaluation.html', message="لم يتم اختيار ملف")
        file = request.files['file']
        if file.filename == '':
            return render_template('cv_evaluation.html', message="لم يتم اختيار ملف")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Extract text from the uploaded file
            cv_text = extract_text_from_pdf(file_path)
            
            # Generate evaluation response
            bot_response = generate_response(cv_text)
            
            return render_template('cv_result.html', cv_text=cv_text, bot_response=bot_response)
    return render_template('cv_evaluation.html')

@app.route('/job_requirements', methods=['GET', 'POST'])
def job_requirements():
    if 'user_id' in session and session['user_role'] == 'employer':
        if request.method == 'POST':
            job_title = request.form['job_title']
            qualifications = ','.join(request.form.getlist('qualifications[]'))
            experience = ','.join(request.form.getlist('experience[]'))
            skills = ','.join(request.form.getlist('skills[]'))
            job_description = request.form['job_description']
            required_experience_years = request.form['required_experience_years']
            try:
                connection = get_db_connection()
                cursor = connection.cursor()
                
                # تحقق من وجود الوظيفة التي أدخلها نفس المستخدم
                check_sql = "SELECT * FROM jobs WHERE employer_id = %s AND job_title = %s"
                cursor.execute(check_sql, (session['user_id'], job_title))
                job_exists = cursor.fetchone()
                
                if job_exists:
                    flash('الوظيفة موجودة بالفعل.', 'info')
                    return redirect(url_for('job_requirements'))
                
                # إدخال بيانات الوظيفة إذا لم تكن موجودة
                sql = """
                INSERT INTO jobs (employer_id, job_title, qualifications, experience, skills, job_description, required_experience_years) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (session['user_id'], job_title, qualifications, experience, skills, job_description, required_experience_years))
                connection.commit()

                job_id = cursor.lastrowid

                # توليد الأسئلة تلقائيًا عند إضافة الوظيفة
                generate_and_save_questions(job_id, job_description, skills, required_experience_years)

                flash('تم إدخال الوظيفة وتوليد الأسئلة بنجاح!', 'success')

            except Exception as e:
                connection.rollback()
                flash(f'حدث خطأ أثناء إدخال الوظيفة: {str(e)}', 'danger')
            
            finally:
                cursor.close()
                connection.close()

        return render_template('job_requirements.html')
    return redirect(url_for('login'))

def match_candidates_with_jobs():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Fetch all jobs
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    
    for job in jobs:
        job_skills = {skill.strip().lower() for skill in job['skills'].split(',')} if job['skills'] else set()
        required_experience_years = int(job['required_experience_years'])
        qualifications = {qual.strip().lower() for qual in job['qualifications'].split(',')} if job['qualifications'] else set()

        # Fetch all job seekers
        cursor.execute("SELECT * FROM job_seekers")
        seekers = cursor.fetchall()
        
        for seeker in seekers:
            seeker_skills = {skill.strip().lower() for skill in seeker['skills'].split(',')} if seeker['skills'] else set()
            seeker_experience = int(seeker['experience']) if seeker['experience'] else 0
            seeker_education = seeker['education'].strip().lower() if seeker['education'] else ""
            
            # Calculate skill match percentage
            skill_match_count = len(job_skills.intersection(seeker_skills))
            skill_match_percentage = (skill_match_count / len(job_skills) * 100) if job_skills else 0
            
            # Match skills, experience, and qualifications
            if skill_match_percentage >= 60 and seeker_experience >= required_experience_years and seeker_education in qualifications:
                # Ensure the candidate is not already in the candidates table
                cursor.execute("SELECT * FROM candidates WHERE job_id = %s AND seeker_id = %s", (job['id'], seeker['id']))
                candidate_exists = cursor.fetchone()
                
                if not candidate_exists:
                    cursor.execute("INSERT INTO candidates (job_id, seeker_id, match_percentage, test_passed) VALUES (%s, %s, %s, %s)",
                                   (job['id'], seeker['id'], skill_match_percentage, False))
    
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/candidates')
def candidates():
    if 'user_id' in session and session['user_role'] == 'employer':
        match_candidates_with_jobs()  # Run matching before fetching candidates
        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Fetch all jobs added by the current employer
            cursor.execute("""
            SELECT j.id, j.job_title, js.name, js.email, c.test_passed, c.pdf_report_path, c.match_percentage
            FROM jobs j
            LEFT JOIN candidates c ON j.id = c.job_id
            LEFT JOIN job_seekers js ON js.id = c.seeker_id
            WHERE j.employer_id = %s
            """, (session['user_id'],))
            jobs = cursor.fetchall()
            
            # Organize candidates by job
            jobs_dict = {}
            for job in jobs:
                if job['id'] not in jobs_dict:
                    jobs_dict[job['id']] = {'job_title': job['job_title'], 'candidates': []}
                if job['name']:
                    jobs_dict[job['id']]['candidates'].append(job)
            
        connection.close()
        return render_template('candidates.html', jobs=jobs_dict.values())
    return redirect(url_for('login'))

@app.route('/applications_feedback', methods=['GET', 'POST'])
def applications_feedback():
    if 'user_id' not in session or session['user_role'] != 'job-seeker':
        return redirect(url_for('login'))
    connection = get_db_connection()
    cursor = connection.cursor()
    user_id = session['user_id']
    sql = """
    SELECT j.job_title, e.company_name, c.test_passed, c.pdf_report_path, c.hired, e.id AS employer_id, c.id AS candidate_id
    FROM candidates c
    JOIN jobs j ON c.job_id = j.id
    JOIN employers e ON j.employer_id = e.id
    WHERE c.seeker_id = %s
    """
    cursor.execute(sql, (user_id,))
    candidates = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('applications_feedback.html', candidates=candidates)




def evaluate_candidate_result(candidate_id, job_id, answers):
    with open('static/questions/questions.json', 'r', encoding='utf-8') as f:
        all_questions = json.load(f)

    job_id = str(job_id)
    if job_id not in all_questions:
        flash('لا يوجد أسئلة للاختبار لهذه الوظيفة.', 'error')
        return False

    questions = all_questions[job_id]
    correct_answers = 0

    for question in questions:
        selected_answer = answers.get(question['question_text'])
        if question['correct_answer'] == selected_answer:
            correct_answers += 1

    score = (correct_answers / len(questions)) * 100
    passed = score >= 70  # Set the passing score as 70%

    connection = get_db_connection()
    cursor = connection.cursor()

    # Update the test_passed field in the candidates table
    sql = """
    UPDATE candidates SET test_passed = %s WHERE seeker_id = %s AND job_id = %s
    """
    cursor.execute(sql, (passed, candidate_id, job_id))
    connection.commit()

    # Save results in the test_results table
    sql = """
    INSERT INTO test_results (candidate_id, job_id, score, passed) 
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE score = VALUES(score), passed = VALUES(passed)
    """
    cursor.execute(sql, (candidate_id, job_id, score, passed))
    connection.commit()
    cursor.close()
    connection.close()

    # Generate PDF report
    generate_pdf_report(candidate_id, job_id, passed)

    return passed

def generate_pdf_report(candidate_id, job_id, passed):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM job_seekers WHERE id = %s", (candidate_id,))
    candidate = cursor.fetchone()
    cursor.execute("SELECT job_title FROM jobs WHERE id = %s", (job_id,))
    job = cursor.fetchone()
    cursor.execute("SELECT score FROM test_results WHERE candidate_id = %s AND job_id = %s", (candidate_id, job_id))
    result = cursor.fetchone()
    
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Test Result Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Candidate Name: {candidate['name']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Job Title: {job['job_title']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Score: {result['score']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Passed: {'Yes' if passed else 'No'}", ln=True, align='L')

    pdf_path = f"static/reports/{candidate['name']}_test_report.pdf"
    pdf.output(pdf_path)

    # Update report path in the database
    cursor.execute("UPDATE candidates SET pdf_report_path = %s WHERE seeker_id = %s AND job_id = %s", (pdf_path, candidate_id, job_id))
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/tests_overview')
def tests_overview():
    if 'user_id' in session and session['user_role'] == 'job-seeker':
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Fetch jobs associated with the candidate
        cursor.execute("SELECT job_id FROM candidates WHERE seeker_id = %s", (session['user_id'],))
        candidate_jobs = cursor.fetchall()
        
        # Load questions from JSON file
        with open('static/questions/questions.json', 'r', encoding='utf-8') as f:
            all_questions = json.load(f)
        
        questions = []
        for job in candidate_jobs:
            job_id = str(job['job_id'])
            if job_id in all_questions:
                questions.extend(all_questions[job_id])
        
        cursor.close()
        connection.close()
        
        if questions:
            return render_template('tests_overview.html', questions=questions)
        else:
            flash('لا يوجد أسئلة للاختبار لهذه الوظيفة.', 'error')
            return redirect(url_for('job_seekers_dashboard'))
        
    return redirect(url_for('login'))

@app.route('/submit_test', methods=['POST'])
def submit_test():
    if 'user_id' in session and session['user_role'] == 'job-seeker':
        connection = get_db_connection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT job_id FROM candidates WHERE seeker_id = %s", (session['user_id'],))
        candidate_jobs = cursor.fetchall()
        
        if candidate_jobs:
            job_id = candidate_jobs[0]['job_id'] 
            answers = request.form.to_dict()
            passed = evaluate_candidate_result(session['user_id'], job_id, answers)
            
            cursor.close()
            connection.close()
            flash('تم إرسال الاختبار وتحديث النتيجة بنجاح!', 'success')
            return redirect(url_for('job_seekers_dashboard'))
        
    return redirect(url_for('login'))

@app.route('/job_admin')
def job_admin():
    return render_template('job_admin.html')
@app.route('/manar_profile')
def manar_profile():
    return render_template('manar_profile.html')

@app.route('/amal_profile')
def amal_profile():
    return render_template('amal_profile.html')

@app.route('/dania_profile')
def dania_profile():
    return render_template('dania_profile.html')

@app.route('/jana_profile')
def jana_profile():
    return render_template('jana_profile.html')

if __name__ == '__main__':
    app.run(debug=True)

