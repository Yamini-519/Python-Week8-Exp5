dict = {"apple": 1, "banana": 2, "cherry": 1}
value = 2
key = next((k for k, v in dict.items() if v == value), None)
print(f"First key found: {key}")