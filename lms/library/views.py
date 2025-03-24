from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Book, BookGenre, BookReview, StudentFeedback
from .serializers import AdminSignupSerializer, AdminLoginSerializer, BookGenreSerializer, BookReviewSerializer, BookSerializer, StudentFeedbackSerializer, User, standard_response


# Admin Signup
class AdminSignupView(generics.CreateAPIView):
    serializer_class = AdminSignupSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return standard_response(True, "Admin registered successfully.", {"id": str(user.id), "email": user.email})
        return standard_response(False, "Failed to register admin.", errors=serializer.errors)


# Log in
class AdminLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return standard_response(True, "Login successful.", {"token": token.key})
        return standard_response(False, "Invalid creif user:dentials.")


# Book Genre Views
class BookGenreListCreateView(generics.ListCreateAPIView):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return standard_response(True, "Book genres retrieved successfully", response.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return standard_response(True, "Book genre added successfully", response.data)


# Book Management Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return standard_response(True, "Books retrieved successfully", response.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return standard_response(True, "Book added successfully", response.data)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return standard_response(True, "Book details retrieved successfully", response.data)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return standard_response(True, "Book updated successfully", response.data)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return standard_response(True, "Book deleted successfully")


class BookReviewListCreateView(generics.CreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "success": True,
            "message": "Review added successfully.",
            "errors": {
                "code": None,
                "message": None,
                "fields": []
            },
            "data": response.data
        }, status=status.HTTP_201_CREATED)


# Student Feedback Views
class StudentFeedbackListCreateView(generics.ListCreateAPIView):
    queryset = StudentFeedback.objects.all()
    serializer_class = StudentFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return standard_response(True, "Student feedback retrieved successfully", response.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return standard_response(True, "Student feedback submitted successfully", response.data)


# Public Student Book View
class StudentBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return standard_response(True, "Books retrieved for students", response.data)