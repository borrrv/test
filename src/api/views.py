from datetime import datetime
from random import choices
from string import ascii_letters

from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView

from .models import Tests
from .serializers import (CreateTestSerializer, ResultAllTestsSerializer,
                          ResultTestEQSerializer, ResultTestIQSerialiser)


class CreateTest(APIView):
    """Создание тестов"""
    def post(self, request):
        login = ''.join(choices(ascii_letters, k=10))
        while Tests.objects.filter(login=login).exists():
            login = ''.join(choices(ascii_letters, k=10))
        create = Tests.objects.create(login=login)
        serializer = CreateTestSerializer(create)
        return Response(serializer.data, status=HTTP_201_CREATED)


class SaveResultIQ(APIView):
    """Сохранение результата теста IQ"""
    def post(self, request, login):
        test = Tests.objects.filter(login=login).first()
        if test is not None:
            iq_time = datetime.now()
            iq_score = request.data.get('iq_score')
            if iq_score is None:
                content = {'error': 'Поле iq_score обязательное'}
                return Response(content, status=HTTP_400_BAD_REQUEST)
            serializer = ResultTestIQSerialiser(
                test,
                data={
                    'iq_score': iq_score,
                    'iq_time': iq_time
                },
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        content = {'error': 'Тест с таким логином не существует'}
        return Response(content, status=HTTP_400_BAD_REQUEST)


class SaveResultEQ(APIView):
    """Сохранение результата теста EQ"""
    def post(self, request, login):
        test = Tests.objects.filter(login=login).first()
        if test is not None:
            eq_time = datetime.now()
            eq_letters = request.data.get('eq_letters')
            if eq_letters is None:
                content = {'error': 'Поле eq_letters обязательное'}
                return Response(content, status=HTTP_400_BAD_REQUEST)
            serializer = ResultTestEQSerializer(
                test,
                data={
                    'eq_letters': eq_letters,
                    'eq_time': eq_time
                },
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        content = {'error': 'Тест с таким логином не существует'}
        return Response(content, status=HTTP_400_BAD_REQUEST)


class ResultAllTests(APIView):
    """Результаты всех тестов"""
    def get(self, request):
        try:
            login = request.data.get('login')
            if login is None:
                content = {'error': 'Поле login обязательное'}
                return Response(content, status=HTTP_400_BAD_REQUEST)
            test = Tests.objects.get(login=login)
            serializer = ResultAllTestsSerializer(test)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception:
            content = {'error': 'Тест с таким логином не существует'}
            return Response(content, status=HTTP_400_BAD_REQUEST)
