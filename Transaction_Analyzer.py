# Nicholas Zimmermann

# 10/8/2026

file = open("transactions.txt", "r")

for line in file:
    customer, amount_due = line.strip().split(",")

    amount_due = float(amount_due)

    print(f"Customer: {customer} | Amount Due: ${amount_due:.2f}")

file.close()
