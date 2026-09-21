def request_key(request):
    return "|".join([request.client_name.lower(),request.location.lower(),request.property_type or "",str(request.budget or "")])
