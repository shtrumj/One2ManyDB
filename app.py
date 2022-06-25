from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import SitesForm

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fm, vkdsanlmdscv nkjmdshgi9redkvnmel'

db = SQLAlchemy(app)
Migrate(app, db)


class Sites(db.Model):  ### Puppies ###
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    available = db.Column(db.Boolean)
    sysadmin_id = db.Column(db.Integer, db.ForeignKey('sysadmins.id'))
    hypervisor_id = db.relationship('Hypervisor', backref='site', lazy=True)
    external_ip = db.Column(db.String(15))


class Admins(db.Model):  ## Owers
    __tablename__ = 'sysadmins'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(10))
    lastName = db.Column(db.String(10))
    site_id = db.relationship('Sites', backref='sysadmin', lazy=True)


class Hypervisor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15))
    ilo_ip_address = db.Column(db.String(15))
    logic_servers = db.relationship
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)
    servers = db.relationship('Servers', backref='hyperHost', lazy=True)


class Servers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_name = db.Column(db.String(15))
    server_ip = db.Column(db.String(15))
    server_os = db.Column(db.String(15))
    nrpe_port = db.Column(db.String(15))
    hypervisor_id = db.Column(db.Integer, db.ForeignKey('hypervisor.id'), nullable=False)


@app.route('/', methods=('GET','POST'))
def hello_world():  # put application's code here
    return render_template('home.html')


@app.route('/addSite', methods=('GET', 'POST'))
def addSite():
    form = SitesForm()
    if request.method == 'POST':
        site_name = form.siteName.data
        site_ex_ip = form.external_ip.data
        new_site = Sites(name=site_name, external_ip=site_ex_ip)
        db.session.add(new_site)
        db.session.commit()

    return  render_template('addSite.html', form=form)

if __name__ == '__main__':
    app.run()
