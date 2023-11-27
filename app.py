from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired


app=Flask(__name__)
app.config['SECRET_KEY']='rahul'

class MyForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')
    salary = DecimalField('Salary', validators=[InputRequired()])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    country = SelectField('Country', choices=[('IN', 'India'), ('US', 'United States'), ('UK', 'United Kingdom')])
    message = TextAreaField('Message', validators=[InputRequired()])
    photo = FileField('photo')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        remember_me = form.remember_me.data
        salary = form.salary.data
        gender = form.gender.data
        country = form.country.data
        message = form.message.data
        photo = form.photo.data.filename
        return f"name = {name}<br > password = {password}<br > remember_me = {remember_me}<br > salary = {salary}<br > gender = {gender}<br > country = {country}<br > message = {message}<br > photo = {photo}<br >"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)