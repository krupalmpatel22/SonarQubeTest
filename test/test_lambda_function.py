from calc.lambda_function import lambda_handler

#testing lambda function
def test_lambda_handler1():
    event = {
        "first_name": "Krupal",
        "last_name": "Patel",
        "age": 21
    }

    output = {
        "code": 200,
        "message": "This is Krupal Patel, I am 21 years old."
    }

    response = lambda_handler(event=event, context=None)

    assert response == output

def test_lambda_handler2():
    event = {
        "first_name": "Kapish",
        "last_name": "Patel",
        "age": 25
    }

    output = {
        "code": 200,
        "message": "This is Kapish Patel, I am 25 years old."
    }

    response = lambda_handler(event=event, context=None)

    assert response == output