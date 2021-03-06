# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())
def first():
    session.counter = (session.counter or 0) + 1
    tree = "yahoo mike check"
    return dict(counter=session.counter, now=request.now,check =tree)

def populate_db():
	## Populate DB Script

	## clear database
	for table in db.tables():
		try:
			db(db[table].id>0).delete()
			print "Cleared",table
		except Exception, e:
			print "Couldn't clear",table

	## create 4 students
	db.users.insert(
		first_name="John",
		last_name="Doe",
		email="cs1110200@cse.iitd.ac.in",
		username="cs1110200",
		entry_no="2011CS10200",
		type_=0,
		password="john",
	)

	db.users.insert(
		first_name="Jasmeet",
		last_name="Singh",
		email="cs5110281@cse.iitd.ac.in",
		username="cs5110281",
		entry_no="2011CS50281",
		type_=0,
		password="jasmeet",
	)

	db.users.insert(
		first_name="Abhishek",
		last_name="Bansal",
		email="cs5110271@cse.iitd.ac.in",
		username="cs5110271",
		entry_no="2011CS50271",
		type_=0,
		password="abhishek",
	)


	db.users.insert(
		first_name="Shubham",
		last_name="Jindal",
		email="cs5110300@cse.iitd.ac.in",
		username="cs5110300",
		entry_no="2011CS50300",
		type_=0,
		password="shubham",
	)


	## create 3 professors
	db.users.insert(
		first_name="Vinay",
		last_name="Ribeiro",
		email="vinay@cse.iitd.ac.in",
		username="vinay",
		entry_no="vinay",
		type_=1,
		password="vinay",
	)

	db.users.insert(
		first_name="Suresh",
		last_name="Gupta",
		email="scgupta@cse.moodle.in",
		username="scgupta",
		entry_no="scgupta",
		type_=1,
		password="scgupta",
	)

	db.users.insert(
		first_name="Subodh",
		last_name="Kumar",
		email="subodh@cse.iitd.ac.in",
		username="subodh",
		entry_no="subodh",
		type_=1,
		password="subodh",
	)
@request.restful()
def api():
    response.view = 'generic.'+request.extension
    def GET(*args,**vars):
        patterns = 'auto'
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(table_name,**vars):
        return db[table_name].validate_and_insert(**vars)
    def PUT(table_name,record_id,**vars):
        return db(db[table_name]._id==record_id).update(**vars)
    def DELETE(table_name,record_id):
        return db(db[table_name]._id==record_id).delete()
    return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
