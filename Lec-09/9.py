import tiktoken
encoding = tiktoken.get_encoding("gpt2")
with open("./Lec-07/the-verdict.txt", "r") as f:
    rawtext = f.read()
    tokens = encoding.encode(rawtext)
    print(len(tokens))