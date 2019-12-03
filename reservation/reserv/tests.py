from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import *
from reservation import settings
from .models import Reservation
# Create your tests here.

class ReservHome(TestCase) :
    def test_root_url_resolves_to_home_page_view(self) :
        found = resolve('/reserv/')
        self.assertEqual(found.func, reserv_home)

    def test_home_page_returns_correct_html(self) :
        response = self.client.get('/reserv/')
        self.assertTemplateUsed(response, 'reserv/reservate.html')

    def test_can_save_a_POST_request(self) :
        response = self.client.post('/reserv/', data={'date' : '2020-05-15T13:12', 'hopping_member' : '3'})
        self.assertIn('date', response.content.decode())

class ReservCheck(TestCase) :
    def session_test(self) :
        found = resolve('/reserv/check/')
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
        self.assertEqual(found.func, reserv_check)

    def test_session_and_check_reserv_page_view(self) :
        response = self.client.get('/reserv/check/')
        self.assertTemplateNotUsed(response, 'reserv/reservation_check.html')

class Reserv_modify_render(TestCase) :
    def test_root_url_resolves_to_home_page_view(self) :
        reservation = Reservation.objects.all()
        for reserv in reservation :
            found = resolve('/reserv/modify/'+ reserv.pk+'/')
            self.assertEqual(found.func, reserv_modify_render)

    def test_home_page_returns_correct_html(self) :
        reservation = Reservation.objects.all()
        for reserv in reservation :
            response = self.client.get('/reserv/modify/'+reserv.pk+'/')
            self.assertTemplateUsed(response, 'reserv/reserv_modify.html')
        
class Reserv_modify(TestCase) :
    def test_reservation_modify_first(self) :
        reservation = Reservation.objects.all() 
        for reserv in reservation :
            found = resolve('/reserv/modify/'+ reserv.pk +'/success/')
            self.assertEqual(found.func, reserv_modify)

    def test_reservation_modify_response_html(self) :
        reservation = Reservation.objects.all() 
        for reserv in reservation :
            response = self.client.get('/reserv/modify/'+reserv.pk+'/success/')
            self.assertTemplateUsed(response, 'reserv/reserv_modify.html')

    def test_resevation_modify_a_POST_request(self) :
        reservation = Reservation.objects.all() 
        for reserv in reservation :
            response = self.client.post('/reserv/modify/'+reserv.pk+'/success/', data={'date' : '2020-05-15T13:12', 'many' : '3'})
            self.assertIn('date', response.content.decode())

class Non_Reservation(TestCase) : # ReservHome
    def test_root_url_resolves_to_home_page_view(self) :
        found = resolve('/reserv/none/user/')
        self.assertEqual(found.func, non_user_reservate)

    def test_home_page_returns_correct_html(self) :
        response = self.client.get('/reserv/none/user/')
        self.assertTemplateUsed(response, 'reserv/reservate.html')

    def test_can_save_a_POST_request(self) :
        response = self.client.post('/reserv/',
        data={'date' : '2020-05-15T13:12', 'hopping_member' : '3', 'phone_number' : '01032270986', 'user_name' : 'kyong'})
        self.assertIn('date', response.content.decode())
        self.assertIn('hopping_member', response.content.decode())
        self.assertIn('phone_number', response.content.decode())
        self.assertIn('user_name', response.content.decode())

class Non_Reservation_Check(TestCase) :
    def test_root_url_resolves_to_home_page_view(self) :
        found = resolve('/reserv/none/user/check/')
        self.assertEqual(found.func, non_user_reservate_check)

    def test_home_page_returns_correct_html(self) :
        response = self.client.get('/reserv/none/user/check/')
        self.assertTemplateUsed(response, 'reserv/non_reserv_lookup.html')

class Non_reservation_delete(TestCase) :
    def test_root_url_resolves_to_home_page_view(self) :
        found = resolve('/reserv/none/user/delete/')
        self.assertEqual(found.func, non_user_delete)