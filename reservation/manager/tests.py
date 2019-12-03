from django.test import TestCase
from django.urls import resolve
from .views import *
from point.views import *

# 관리자 홈페이지/ 그 외에 기능들로 잘 가는지 체크
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        # 관리자 페이지에 잘 들어갔는지
        found1 = resolve('/manager/page/')
        self.assertEqual(found1.func, m_home)
        # 예약 확인 페이지에 잘 들어갔는지
        found3 = resolve('/manager/page/reserv/')
        self.assertEqual(found3.func, m_reserv)
        # 매장 관리 페이지에 잘 들어갔는지
        found4 = resolve('/manager/page/restaurant/')
        self.assertEqual(found4.func, m_restaurant)
        # 유저관리 페이지에 잘 들어갔는지
        found5 = resolve('/manager/page/user/')
        self.assertEqual(found5.func, m_user)
        # 포인트 페이지에 잘 들어가는지
        found6 = resolve('/manager/page/point')
        self.assertEqual(found6.func, point)
      
#매니져 기능 테스트
class ManagerFunctionTest(TestCase):
#포인트 계산 테스트    
    def calPoint(self):
        mode1 = 1
        mode2 = 2
        mode3 = 3
        money = 100000
        before_point = 5000
        
         # 판매 포인트적립
        if (mode1 == 1):
            point = before_point + (money * 0.1)
            self.assertEqual(((money*0.1)+before_point) , point)
        
        # 선 입금 포인트적립
        elif (mode2 == 2):
            point = before_point + money
            self.assertEqual(money+before_point , point)
        
        # 포인트 사용
        elif (mode3 == 3):
            if (before_point < money):
                self.fail('테스트 불가능')
            point = before_point - money 
            self.assertEqual(before_point-money , point)

            
        