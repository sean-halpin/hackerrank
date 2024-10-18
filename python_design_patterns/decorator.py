# Basic user request handler function
def handle_request(user):
    return f"Request handled for user: {user}"

# Decorator for logging
def logging_decorator(func):
    def wrapper(user):
        print(f"Logging: Handling request for {user}")
        response = func(user)  # Call the original function
        print("Logging: Request handled successfully")
        return response
    return wrapper

# Decorator for authentication
def authentication_decorator(func):
    def wrapper(user):
        if user != "admin":  # Simple authentication check
            return "Access denied: User not authorized."
        return func(user)  # Call the original function if authenticated
    return wrapper

# Apply decorators to the handle_request function
@logging_decorator
@authentication_decorator
def decorated_handle_request(user):
    return handle_request(user)

# Tests
if __name__ == "__main__":
    # Test with an authorized user
    print(decorated_handle_request("admin"))  # Should log and handle the request

    # Test with an unauthorized user
    print(decorated_handle_request("guest"))  # Should deny access
