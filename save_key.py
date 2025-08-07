s = "APIKEY={key}"
print("Input your API key")
key = input(":")
with open(".env", mode="w", encoding="utf-8") as f:
    f.write(s.format(key=key))
print("SUCCESS")