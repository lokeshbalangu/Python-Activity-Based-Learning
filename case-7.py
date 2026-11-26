text = input("Enter text without spaces: ")

if text == "":
    print("Empty input")
else:
    encoded = ""
    current = text[0]
    count = 1

    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            encoded += current + str(count)
            current = ch
            count = 1

    encoded += current + str(count)

    print("Original text:", text)
    print("Encoded text:", encoded)

    if len(encoded) < len(text):
        print("Encoded text is shorter.")
    else:
        print("Compression is not beneficial, keep original text.")