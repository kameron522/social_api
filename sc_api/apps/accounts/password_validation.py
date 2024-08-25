from rest_framework.response import Response

def password_validation(self, request):
    try:
        if 'password' in request.data and 'password_confirmation' in request.data:
            return request.data and request.data['password'] == request.data['password_confirmation']
        return False
    except Exception as ex:
        return Response({'error' : str(ex)}, status=500)
    
    
    