def jwt_response_payload_handle(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }