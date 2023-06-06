from django.urls import path

from .views import CreateTest, ResultAllTests, SaveResultEQ, SaveResultIQ

urlpatterns = [
    path('create_tests/', CreateTest.as_view()),
    path('result_test_iq/<str:login>/', SaveResultIQ.as_view()),
    path('result_test_eq/<str:login>/', SaveResultEQ.as_view()),
    path('results/', ResultAllTests.as_view()),
]
