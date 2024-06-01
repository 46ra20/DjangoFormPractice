from django.http import HttpResponse
from django.shortcuts import render

def Hello(r):
    data ={
        'userData':[{
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        },
        {
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        },
        {
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        },
        {
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        },
        {
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        },
        {
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        },
        {
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        },
        {
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        },
        {
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        },
        {
            'id':'01',
            'name':'Md Rakib Bhuiyan',
            'education':'UCTC',
            'subject':'CSE'
        }]
    }
    d ={'num':[10,20,30,50]}
    return render(r,'PracticeModule_10_5/index.html',d)


# templates/PracticeModule_10_5/index.html