from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app

# initialize database object
db = SQLAlchemy(app)

class Company(db.Model):
    __tablename__ = "company"
    # set column types
    company_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
    summary = db.Column(db.String, unique=True)
    people = db.Column(db.String)
    city = db.Column(db.String)
    financial_orgs = db.Column(db.String)
    twitter = db.Column(db.String)
    website = db.Column(db.String)
    logo_url = db.Column(db.String)

    # set column values in constructor
    #def __init__(self, name, summary, people, city, financial_orgs, twitter, website, logo_url):
    def __init__(self, company_id, name, summary, people, city, financial_orgs, twitter, website, logo_url):
        self.company_id = company_id
        self.name = name
        self.summary = summary
        self.people = people
        self.city = city
        self.financial_orgs = financial_orgs
        self.twitter = twitter
        self.website = website
        self.logo_url = logo_url

    def __repr__(self):
        return '<Company %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['company_id'] = self.company_id
        dict_rep['name'] = self.name
        dict_rep['summary'] = self.summary
        dict_rep['people'] = self.people
        dict_rep['city'] = self.city
        dict_rep['financial_orgs'] = self.financial_orgs
        dict_rep['twitter'] = self.twitter
        dict_rep['website'] = self.website
        dict_rep['logo_url'] = self.logo_url
        return dict_rep


class FinancialOrg(db.Model):
    __tablename__ = "financial_org"
    # set the column types
    financial_org_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
    summary = db.Column(db.String, unique=True)
    city = db.Column(db.String)
    companies = db.Column(db.String)
    twitter = db.Column(db.String)
    website = db.Column(db.String)
    logo_url = db.Column(db.String)

    # set the column values in constructor
    #def __init__(self, name, summary, city, companies, twitter, website, logo_url):
    def __init__(self, financial_org_id, name, summary, city, companies, twitter, website, logo_url):
        self.financial_org_id = financial_org_id
        self.name = name
        self.summary = summary
        self.city = city
        self.companies = companies
        self.twitter = twitter
        self.website = website
        self.logo_url = logo_url

    def __repr__(self):
        return '<FinancialOrg %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['financial_org_id'] = self.financial_org_id
        dict_rep['name'] = self.name
        dict_rep['summary'] = self.summary
        dict_rep['city'] = self.city
        dict_rep['companies'] = self.companies
        dict_rep['twitter'] = self.twitter
        dict_rep['website'] = self.website
        dict_rep['logo_url'] = self.logo_url
        return dict_rep


class Person(db.Model):
    __tablename__ = "person"
    # set the column types
    person_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
    summary = db.Column(db.String, unique=True)
    city = db.Column(db.String)
    companies = db.Column(db.String)
    role = db.Column(db.String)
    twitter = db.Column(db.String)
    logo_url = db.Column(db.String)

    # set the column values in constructor
    def __init__(self, person_id, name, summary, city, companies, role, twitter, logo_url):
        self.person_id = person_id
        self.name = name
        self.summary = summary
        self.city = city
        self.companies = companies
        self.role = role
        self.twitter = twitter
        self.logo_url = logo_url

    def __repr__(self):
        return '<Person %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['person_id'] = self.person_id
        dict_rep['name'] = self.name
        dict_rep['summary'] = self.summary
        dict_rep['city'] = self.city
        dict_rep['companies'] = self.companies
        dict_rep['role'] = self.role
        dict_rep['twitter'] = self.twitter
        dict_rep['logo_url'] = self.logo_url
        return dict_rep


class City(db.Model):
    __tablename__ = "city"
    # set the column types
    city_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
    state = db.Column(db.String)
    region = db.Column(db.String)
    companies = db.Column(db.String)
    financial_orgs = db.Column(db.String)
    people = db.Column(db.String)

    # set the column values in constructor
    def __init__(self, city_id, name, state, region, companies, financial_orgs, people):
        self.city_id = city_id
        self.name = name
        self.state = state
        self.region = region
        self.companies = companies
        self.financial_orgs = financial_orgs
        self.people = people

    def __repr__(self):
        return '<City %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['city_id'] = self.city_id
        dict_rep['name'] = self.name
        dict_rep['state'] = self.state
        dict_rep['region'] = self.region
        dict_rep['companies'] = self.companies
        dict_rep['financial_orgs'] = self.financial_orgs
        dict_rep['people'] = self.people
        return dict_rep
