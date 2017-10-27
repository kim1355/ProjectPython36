from django.shortcuts import render

# Create your views here.
from django.template import Context
from django.shortcuts import render
from django.db import models
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import pymysql.cursors

def search_db():
    config = {'host': '127.0.0.1',
              'port': 3306,
              'user': 'root',
              'password': 'root',
              'db': 'test',
              'cursorclass': pymysql.cursors.DictCursor,}
    connection = pymysql.connect(**config)

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * from employee1'
            cursor.execute(sql)
            result = cursor.fetchone()
        connection.commit()

    finally:
        connection.close()
    return result


from django.template.loader import render_to_string
def index(request):
    list_info = search_db()
    return render_to_response('home.html', {'employee': list_info})

def home(request):
    return HttpResponse('hello world')