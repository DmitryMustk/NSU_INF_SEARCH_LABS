from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import University, Student
from app.forms import UniversityForm, StudentForm

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/universities/')
def university_list():
    universities = University.query.order_by(University.short_name).all()
    return render_template('university_list.html', universities=universities)

@main_bp.route('/universities/create/', methods=['GET', 'POST'])
@login_required
def university_create():
    form = UniversityForm()
    if form.validate_on_submit():
        university = University(
            full_name=form.full_name.data,
            short_name=form.short_name.data,
            creation_date=form.creation_date.data
        )
        db.session.add(university)
        db.session.commit()
        flash('Университет добавлен', 'success')
        return redirect(url_for('main.university_detail', id=university.id))
    return render_template('university_form.html', form=form, title='Добавить университет')

@main_bp.route('/universities/<int:id>/')
def university_detail(id):
    university = University.query.get_or_404(id)
    return render_template('university_detail.html', university=university)

@main_bp.route('/universities/<int:id>/edit/', methods=['GET', 'POST'])
@login_required
def university_edit(id):
    university = University.query.get_or_404(id)
    form = UniversityForm(obj=university)
    if form.validate_on_submit():
        form.populate_obj(university)
        db.session.commit()
        flash('Университет обновлён', 'success')
        return redirect(url_for('main.university_detail', id=university.id))
    return render_template('university_form.html', form=form, title='Редактировать университет')

@main_bp.route('/universities/<int:id>/delete/', methods=['GET', 'POST'])
@login_required
def university_delete(id):
    university = University.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(university)
        db.session.commit()
        flash('Университет удалён', 'success')
        return redirect(url_for('main.university_list'))
    return render_template('university_delete.html', university=university)

@main_bp.route('/students/')
def student_list():
    students = Student.query.order_by(Student.full_name).all()
    return render_template('student_list.html', students=students)

@main_bp.route('/students/create/', methods=['GET', 'POST'])
@login_required
def student_create():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            full_name=form.full_name.data,
            birth_date=form.birth_date.data,
            university_id=form.university_id.data,
            enrollment_year=form.enrollment_year.data
        )
        db.session.add(student)
        db.session.commit()
        flash('Студент добавлен', 'success')
        return redirect(url_for('main.student_detail', id=student.id))
    return render_template('student_form.html', form=form, title='Добавить студента')

@main_bp.route('/students/<int:id>/')
def student_detail(id):
    student = Student.query.get_or_404(id)
    return render_template('student_detail.html', student=student)

@main_bp.route('/students/<int:id>/edit/', methods=['GET', 'POST'])
@login_required
def student_edit(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        form.populate_obj(student)
        db.session.commit()
        flash('Студент обновлён', 'success')
        return redirect(url_for('main.student_detail', id=student.id))
    return render_template('student_form.html', form=form, title='Редактировать студента')

@main_bp.route('/students/<int:id>/delete/', methods=['GET', 'POST'])
@login_required
def student_delete(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
        flash('Студент удалён', 'success')
        return redirect(url_for('main.student_list'))
    return render_template('student_delete.html', student=student)

