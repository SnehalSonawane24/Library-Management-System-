from rest_framework import serializers, status
from django.contrib.auth import get_user_model
from library.models import AdminUser, Book, BookGenre, BookReview, StudentFeedback
from rest_framework.response import Response

User = get_user_model()

def standard_response(success, message, data=None, errors=None):
    return Response(
        {
            "success": success,
            "message": message,
            "errors": errors or {"code": None, "message": None, "fields": []},
            "data": data or {},
        },
        status=status.HTTP_200_OK if success else status.HTTP_400_BAD_REQUEST,
    )


# Admin Signup Serializer
class AdminSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ["id", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data["username"] = validated_data["email"]
        return AdminUser.objects.create_user(**validated_data)


# Admin Login Serializer
class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


# Book Genre Serializer
class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = '__all__'


# Book Serializer (Updated)
class BookSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=BookGenre.objects.all())

    class Meta:
        model = Book
        fields = '__all__'


# Book Review Serializer
class BookReviewSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = BookReview
        fields = ['id', 'book', 'student', 'review_text', 'rating', 'created_at']
        extra_kwargs = {'created_at': {'read_only': True}}


# Student Feedback Serializer
class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFeedback
        fields = '__all__'