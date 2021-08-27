import random

# Answer
def get_ans(req):
    req = req.lower()

    if 'hi'in req or 'hello' in req:
        return "Hello!"
    elif 'weather' in req:
        return "It's a great sunny day!"
    elif 'president' in req and 'United States' in req:
        return 'Joe Biden!'
    elif 'bitcoin' in req:
        return "48123,00 USD"
    elif 'your' in req and 'name' in req:
        return "My name is Hulk!"
    elif 'color' in req:
        return "I like green color!" 
    else:
        return "It's a pleasure to meet you!"
 

sentences = ["How are you?", "Hi", "Say anything..",
            "Waiting...","Are you ok?"]
    

def chatting():
    return random.choice(sentences)