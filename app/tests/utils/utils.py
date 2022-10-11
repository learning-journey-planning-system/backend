import random
import string

# def random_lower_string() -> str:
#     return "".join(random.choices(string.ascii_lowercase, k=32))

# def random_email() -> str:
#     return f"{random_lower_string()}@{random_lower_string()}.com"

def random_num_in(end) -> int:
    return random.randint(0, end-1)

def random_num_out(end) -> int:
    return random.randint(end, 100)