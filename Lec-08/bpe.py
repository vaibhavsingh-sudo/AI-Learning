import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")
text = "Hello, how are you doing today? <|endoftext|> I hope you're having a great day!"

tokenize = tokenizer.encode(text,allowed_special={"<|endoftext|>"})
print(tokenize)
print(tokenizer.decode(tokenize))
