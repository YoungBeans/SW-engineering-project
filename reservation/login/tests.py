import unittest
from django.test.client import Client
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.shortcuts import reverse
from .views import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your tests here.

# Login TestCase

class SingUp (TestCase) :
    def test_root_url_resolves_to_default_page_view(self) :
        found = resolve('/login/signup/')
        self.assertEqual(found.func, sign_up)
    
    def login_page(self) :
        response = self.client.get('/login/signup/')
        if not self.client.session:
            engine = import_module(settings.SESSION_ENGINE)
            
            self.client.session = engine.SessionStore()
            self.client.session.save()

        session_cookie = settings.SESSION_COOKIE_NAME
        self.client.cookies[session_cookie] = self.client.session.session_key
        cookie_data = {
            'manager': None,
            'userid' : "alkad1234"
        }
        self.client.cookies[session_cookie].update(cookie_data)
        self.assertTemplateUsed(response, 'login/login.html')

class login_test(TestCase) :
    def test_login_home_page(self) :
        found = resolve('/login/')
        self.assertEqual(found.func, login)

    def test_login_return_html(self) :
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, "login/login.html")

    def test_login_save_a_POST_request(self) :
        response = self.client.post('/login/',
        data={'id' : 'alkad1234', 'pwd' : '7751klog!@'})
        self.assertIn('id', response.content.decode())
        self.assertIn('pwd', response.content.decode())

class logout_test(TestCase) :
    def test_login_home_page(self) :
        found = resolve('/login/logout/')
        self.assertEqual(found.func, logout)

    def test_login_return_html(self) :
        response = self.client.get('/login/logout/')
        self.assertTemplateNotUsed(response, 'main/home.html')

class Find_password(TestCase) :
    def test_find_password_page(self) :
        found = resolve('/login/find/password/')
        self.assertEqual(found.func, find_pwd)

    def test_find_pawssword_save_a_POST_request(self) :
        response = self.client.get('/login/find/password/', data={'id' : 'alkad1234', 'number' : '01032270986'})
        # self.assertIn('id', response.content.decode())
        # self.assertIn('phone', response.content.decode())    
        self.assertTemplateUsed(response, "login/find_pwd.html")

    def test_find_no_POST_return (self) :
        response = self.client.get('/login/find/password/')
        self.assertTemplateUsed(response, 'login/find_pwd.html')

class Change_password(TestCase) :
    def test_change_password_func_test(self) :
        found = resolve('/login/find/password/change/')
        self.assertEqual(found.func, change_pwd)
    
    def test_change_password_POST_return_test(self) :
        response = self.client.post('/login/find/password/change/',
        data={'id' : 'alkad1234', 'pwd' : '111111', 'checkpwd' : '11111'} )
        self.assertIn('id', response.content.decode())
        self.assertIn('pwd', response.content.decode())
        self.assertIn('checkpwd', response.content.decode())    
        self.assertTemplateUsed(response, 'login/change.html')

    def test_change_pasword_wrong(self) :
        response = self.client.post('/login/find/password/change/',
        data={'id' : 'alkad1234', 'pwd' : '111111', 'checkpwd' : '22222'} )
        self.assertTemplateUsed(response, "login/change.html")

# Review TestCase

class Show_Review_test (TestCase) :
    def test_root_url_resolves_to_default_page_view(self) :
        found = resolve('/login/user/review/')
        self.assertEqual(found.func, show_review)

    def show_Review_url_resolves_to_default_page_view (self) :
        response = self.client.get('/login/user/review/')
        if not self.client.session:
            engine = import_module(settings.SESSION_ENGINE)
            
            self.client.session = engine.SessionStore()
            self.client.session.save()

        session_cookie = settings.SESSION_COOKIE_NAME
        self.client.cookies[session_cookie] = self.client.session.session_key
        cookie_data = {
            'manager': None,
            'userid' : "alkad1234"
        }
        self.client.cookies[session_cookie].update(cookie_data)
        self.assertTemplateUsed(response, "statistics/review.html")

class Write_review_test (TestCase) :
    def write_POST_return_test(self) :
        response = self.client.post('/login/user/review/write/',
        data={'menu' : '토시살', 'star' : '3', 'title' : '맛있어요', 'content' : '정말 맛있어요'} )
        # self.assertIn('menus', response.content.decode())
        self.assertIn('star', response.content.decode())
        self.assertIn('title', response.content.decode())
        self.assertIn('content', response.content.decode())
        if not self.client.session:
            engine = import_module(settings.SESSION_ENGINE)
            
            self.client.session = engine.SessionStore()
            self.client.session.save()

        session_cookie = settings.SESSION_COOKIE_NAME
        self.client.cookies[session_cookie] = self.client.session.session_key
        cookie_data = {
            'manager': None,
            'userid' : "alkad1234"
        }
        self.client.cookies[session_cookie].update(cookie_data)

        self.assertTemplateUsed(response, "statistics/review.html")

class My_reviews_test (TestCase) :
    def test_root_url_resolves_to_default_page_view(self) :
        users = User.objects.all()
        for user in users :    
            found = resolve('/login/user/review/myreview/'+user.pk+'/')
            self.assertEqual(found.func, my_review)
    
    def can_save_a_POST_request (self) :
        users = User.objects.all()
        for user in users :    
            response = self.client.get('/login/user/review/myreview/'+user.pk+'/')
            if not self.client.session:
                engine = import_module(settings.SESSION_ENGINE)
                
                self.client.session = engine.SessionStore()
                self.client.session.save()

            session_cookie = settings.SESSION_COOKIE_NAME
            self.client.cookies[session_cookie] = self.client.session.session_key
            cookie_data = {
                'manager': None,
                'userid' : "alkad1234"
            }
            self.client.cookies[session_cookie].update(cookie_data)

            self.assertTemplateUsed(response, 'statistics/myreview.html')
    
    def test_cant_session (self) :
        users = User.objects.all()
        for user in users :    
            response = self.client.get('/login/user/review/myreview/'+user.pk+'/')
            self.assertTemplateUsed(response, 'main/home.html')

class Modify_review_test (TestCase) :
    def modify_reviews_POST_return_test(self) :
        reviews = Review.objects.all()
        for review in reviews :    
            response = self.client.post('/login/user/review/myreview/modify/'+review.pk+'/',
            data={'menu' : '토시살', 'star' : '3', 'title' : '맛있어요', 'content' : '정말 맛있어요'} )
            self.assertIn('menus', response.content.decode())
            self.assertIn('star', response.content.decode())
            self.assertIn('title', response.content.decode())
            self.assertIn('content', response.content.decode())
            if not self.client.session:
                engine = import_module(settings.SESSION_ENGINE)
                
                self.client.session = engine.SessionStore()
                self.client.session.save()

            session_cookie = settings.SESSION_COOKIE_NAME
            self.client.cookies[session_cookie] = self.client.session.session_key
            cookie_data = {
                'manager': None,
                'userid' : "alkad1234"
            }
            self.client.cookies[session_cookie].update(cookie_data)

            self.assertTemplateUsed(response, "statistics/myreview.html")

    def test_modify_reviews_none_POST_return_test(self) :
        reviews = Review.objects.all()
        for review in reviews :    
            response = self.client.post('/login/user/review/myreview/modify/'+review.pk+'/',
            data={'menu' : '토시살', 'star' : '3', 'title' : '맛있어요', 'content' : '정말 맛있어요'} )
            self.assertIn('menus', response.content.decode())
            self.assertIn('star', response.content.decode())
            self.assertIn('title', response.content.decode())
            self.assertIn('content', response.content.decode())

            self.assertTemplateUsed(response, "statistics/review.html")

class Search_review_test (TestCase) :
    def test_search_on_POST (self) : # 키워드 메뉴 둘 다 검색했을 경우 정보가 입력되서 올바른 frontend로 가는지
        response = self.client.post('/login/review/search/',
        data={'menu' : '토시살', 'keyword' : '맛있'} )
        # self.assertIn('menus', response.content.decode())
        # self.assertIn('keyword', response.content.decode())
        self.assertTemplateNotUsed(response, "statistics/search_review.html")
    def test_search_page_on_root(self) :
        found = resolve('/login/review/search/')
        self.assertEqual(found.func, search_review)
    def test_search_on_POST2 (self) : # 키워드만 검색했을 경우
        response = self.client.post('/login/review/search/',
        data={ 'keyword' : '맛있'} )
        # self.assertIn('keyword', response.content.decode())
        self.assertTemplateUsed(response, "statistics/search_review.html")
    def test_search_on_POST3 (self) : # 메뉴만 검색했을 경우
        response = self.client.post('//login/review/search/',
        data={'menu' : '토시살'} )
        # self.assertIn('menus', response.content.decode())
        self.assertTemplateNotUsed(response, "statistics/search_review.html")
