text = input()
addr = ["www", "http://", "https://"]

words = text.split(" ")
for word in words:
    for page in addr:
        if word.lower().startswith(page) and len(word) > 7:
            print(word)
        else:
            continue
