import tiktoken
encoding = tiktoken.get_encoding("gpt2")
with open("./Lec-07/the-verdict.txt", "r") as f:
    rawtext = f.read()
    tokens = encoding.encode(rawtext)
    # print(len(tokens))

    context_size = 4
    enc_sample = tokens[50:] # for tokens
    enc_sameple1 = rawtext[50:] # for raw text
    print("text:", enc_sameple1[:context_size])
    print("text:", enc_sameple1[1:context_size+1])
    x=enc_sample[:context_size]
    y=enc_sample[1:context_size+1]
    print("x:", x)
    print("y:", y)


    # context and desired using for loop
    for i in range(1,context_size+1):
        x=enc_sample[:i] # context
        y=enc_sample[i] # desired
        print(x,"----->",y)