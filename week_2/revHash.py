import hashlib

given_hash = "a2099f4c2c2de141afb474dfe4b765ce83448100e77f4359314d94807b00862d53316c03963fc60cbdbd7bc6915778f1830f0f4fd9364a4bc71a09c5e83a0a67"

with open('pass.txt') as f:
    lines = f.readlines()
    for words in lines: 
        normal_words = words.strip()
        hashed_words= hashlib.sha3_512(normal_words.encode()).hexdigest()
        if hashed_words == given_hash:
            print(normal_words)