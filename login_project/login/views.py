from django.http import HttpResponse
from django.shortcuts import render, redirect
import sqlite3
from django.http import HttpResponseRedirect
from django.contrib import messages
import os
import cgi
import cgitb; cgitb.enable()




def loginscreen(request):
	response = HttpResponse("Hello world!")
	response["My-Header"] = "header value"
	return render(request,'login.html')


def loginpage(request):
	username= request.POST.get('username')
	#print(username)
	password = request.POST.get('password')
	conn = sqlite3.connect('db.sqlite3')
	sql="select * from cred_user where username='%s' and password='%s'" % (username,password)
	data=conn.execute(sql)
	if (data.fetchall()):
		return redirect('log/')
	else:
		messages.error(request,'Username or Password not correct.')
		return redirect('login/')

	return render(request,'login.html')

def loginsuccess(request):
	return render(request,'loggedIn.html')

def sqli(request):
	vuln=request.GET['fname']
	print(vuln)
	conn = sqlite3.connect('db.sqlite3')
	sql="select first_name from info_user where username=?"
	data=conn.execute(sql,(vuln,))


	return render(request,'account.html',{'data':data,'vuln':vuln})

def sqli_vuln(request):
	return render(request,'sqli.html')

def xss_vuln(request):
	return render(request,'xss.html')

def csrf_vuln(request):
	return render(request,'editprofile.html')

def file_vuln(request):
	return render(request,'editprofile.html')


def editprofile(request):
		first_name= request.POST.get('fname')
		last_name= request.POST.get('lname')
		bio= request.POST.get('bio')
		print(first_name,last_name,bio)
		
		conn  =  sqlite3.connect('db.sqlite3')
		cursor  =  conn.cursor ()
		cursor.execute("INSERT INTO info_user(username, first_name) VALUES ('test','%s')" % (first_name))
		conn.commit ()
		print ( 'Data entered successfully.' )
		conn . close ()
		if (conn):
		  conn.close()
		  print("\nThe SQLite connection is closed.")
		return render(request,'loggedIn.html')


def cmdi_vuln(request):
		IP_ping= request.POST.get('IP')
		real_IP='ping -c 2 %s' % (IP_ping)
		command_out=os.system(real_IP)
		

		return render(request,'cmdi.html')

def lfi_vul(request):
	return render(request,'lfi.html')

def lfi_vuln(request):
	inc_file=request.POST.get('lfi')
	#print (inc_file)
	f = open(str(inc_file), 'r')
	users = f.read()
	return render(request,'lfi.html',{'users':users})


def file_vuln(request):
	form = cgi.FieldStorage()
	fileitem=form['filenam']
	if fileitem.filenam:
		fn = os.path.basename(fileitem.filenam)
		open('/tmp/' + fn, 'wb').write(fileitem.file.read())
		message = 'The file "' + fn + '" was uploaded successfully'
	else:
		message = 'No file was uploaded'

		
		return render(request,'fileupload.html')
