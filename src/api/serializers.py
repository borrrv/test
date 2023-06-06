from rest_framework import serializers

from .models import Tests


class BaseTestSeriazizer(serializers.ModelSerializer):
    """Общий сериалайзер для eq_letters"""
    eq_letters = serializers.CharField(required=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        eq_letters = representation['eq_letters'].split(', ')
        representation['eq_letters'] = sorted(set(eq_letters))
        return representation


class CreateTestSerializer(serializers.ModelSerializer):
    """Создание логина для тестов"""
    class Meta:
        model = Tests
        fields = (
            'login',
        )


class ResultTestIQSerialiser(serializers.ModelSerializer):
    """Сохранить результаты теста IQ"""
    login = serializers.ReadOnlyField()
    iq_score = serializers.IntegerField(required=True)

    class Meta:
        model = Tests
        fields = (
            'login',
            'iq_score',
            'iq_time',
        )

    def validate_iq_score(self, value):
        print(value)
        if value > 50 or value < 0:
            raise serializers.ValidationError(
                'Введите количество баллов от 0 до 50'
            )
        return value


class ResultTestEQSerializer(BaseTestSeriazizer):
    """Сохранить результаты теста EQ"""
    login = serializers.ReadOnlyField()
    eq_letters = serializers.CharField(required=True)

    class Meta:
        model = Tests
        fields = (
            'login',
            'eq_letters',
            'eq_time',
        )


class ResultAllTestsSerializer(BaseTestSeriazizer):
    """Результаты всех тестов по логину"""
    login = serializers.CharField(required=True)

    class Meta:
        model = Tests
        fields = (
            'login',
            'iq_time',
            'iq_score',
            'eq_letters',
            'eq_time',
        )
