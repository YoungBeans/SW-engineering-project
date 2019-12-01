from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import reserv_home, reserv_check, reserv_modify_render
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
    def test_root_url_resolves_to_home_page_view(self) :
        found = resolve('/reserv/check/')
        self.assertEqual(found.func, reserv_check)

    def test_home_page_returns_correct_html(self) :
        response = self.client.get('/reserv/check/')
        self.assertTemplateUsed(response, 'reserv/reservation_check.html')

# class Reserv_modify_render(TestCase) :
#     def test_root_url_resolves_to_home_page_view(self) :
#         found = resolve('/reserv/check/')
#         self.assertEqual(found.func, reserv_check)

#     def test_home_page_returns_correct_html(self) :
#         response = self.client.get('/reserv/check/')
#         self.assertTemplateUsed(response, 'reserv/reservation_check.html')