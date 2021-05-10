import psycopg2
import pandas as pd
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    return render(request, 'app/index.html')
