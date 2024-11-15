def lambda_handler(event: dict, context) -> dict:
    message = f"This is {event.get("first_name")} {event.get("last_name")}, I am {event.get("age")} years old."
    return {"code":200 ,"message": message}

if __name__ == "__main__":
    event={
        "first_name": "Krupal",
        "last_name": "Patel",
        "age": 21
    }
    response = lambda_handler(event=event, context=None)
    print(response)