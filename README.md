# Referral-system-API

1. **Django**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It provides a powerful ORM (Object-Relational Mapper) for interacting with databases and includes built-in authentication and authorization mechanisms.

2. **Django REST Framework (DRF)**: Django REST Framework is a powerful and flexible toolkit for building Web APIs in Django. It provides serialization, authentication, permissions, and other useful features for developing RESTful APIs.

3. **APIView**: `@api_view` is a decorator provided by DRF to create views based on function-based views. It allows you to define API views using normal Django view functions.

4. **Permission Classes**: DRF provides permission classes to control access to API views. In this code, `IsAuthenticated` is a permission class that ensures only authenticated users can access the endpoint.

5. **Paginator**: Django's Paginator class allows you to paginate querysets and display a certain number of objects per page. It simplifies the process of paginating large datasets in API responses.

6. **Models**: In Django, models are Python classes that represent database tables. The provided code defines a `User` model with fields such as name, email, password, referral_code, and registration_timestamp.

7. **Serializers**: Serializers are used to convert complex data types, such as querysets and model instances, into native Python data types that can be easily rendered into JSON, XML, or other content types. In this code, `UserSerializer` serializes `User` model instances into JSON format.

8. **GET requests**: HTTP GET requests are used to retrieve data from a server. The Referrals Endpoint in this code accepts GET requests to fetch a list of user referrals.

9. **Authorization Header**: The Authorization header is used to send credentials (such as tokens) with a request to authenticate the user. This code requires a valid token in the Authorization header for accessing the User Details and Referrals endpoints.

10. **Response**: DRF's `Response` class is used to return HTTP responses from API views. It simplifies the process of creating API responses and ensures consistency in the response format.

You can use these explanations to provide context and understanding for users who are reading your README file on GitHub.
