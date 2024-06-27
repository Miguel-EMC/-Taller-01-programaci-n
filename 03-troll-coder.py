import sys

def send_query(query):
    print("Q", " ".join(map(str, query)))
    sys.stdout.flush()

def receive_response():
    return int(input().strip())

# Leer la longitud de la secuencia N
N = int(input().strip())
guess = [0] * N
send_query(guess)
correct_bits = receive_response()

# Iterar a través de cada bit para determinar la secuencia correcta
for i in range(N):
    guess[i] = 1
    send_query(guess)
    new_correct_bits = receive_response()
    if new_correct_bits <= correct_bits:
        guess[i] = 0
    else:
        correct_bits = new_correct_bits

print("A", " ".join(map(str, guess)))
sys.stdout.flush()