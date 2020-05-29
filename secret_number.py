secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

secret = int(input("Enter my secret number: "))

while secret_number != secret:
    print("\nHa ha! You're stuck in my loop!")
    secret = int(input("\nEnter my secret number: "))
if secret == secret_number:
    print("\nWell done, muggle! You are free now.\n")


