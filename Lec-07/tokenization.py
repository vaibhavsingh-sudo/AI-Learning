with open('Lec-07\\the-verdict.txt','r',encoding='utf-8') as f:
    raw_text=f.read()

print("Total number of character:",len(raw_text))
print(raw_text[:99].split())

import re
exp_text="Hello, World. This is a test.--?!"
print(re.split(r'(\s)',exp_text))


#split with commas, and periods[,.]
print(re.split(r'([,.]|\s)',exp_text))

#to remove white spaces
result=re.split(r'([,.]|\s)',exp_text)
result=[item for item in result if item.strip()]
print(result)

#split with commas, and periods[,.!?"();:\_']--
result=re.split(r'([,.!?"();:_\']|--|\s)',exp_text)
result=[item for item in result if item.strip()]
print(result)

#tokenizing the-verdict.txt
print()
print("-"*30,"Preprocessing the-verdict.txt","-"*30)
preprocessed=re.split(r'([,.!?"();:_\']|--|\s)',raw_text)
preprocessed=[item for item in preprocessed if item.strip()]
print(preprocessed[:30])
print(len(preprocessed))


#sorting in alphabetical order
print('\nSorting all in alphabetical order')
all_words=sorted(set(preprocessed))
print(len(all_words))

#Assigning IDs,Vocabulary 
print('\nAssigning IDs,Vocabulary')
vocab={token:integer for integer,token in enumerate(all_words)}
print(vocab)


print("\n","-"*30,"Testing SimpleTokenizer","-"*30)
from SimpleTokenizer import SimpleTokenizerV1
tokenizer = SimpleTokenizerV1(vocab)
text = "Well!--even through the prism of Hermia's tears I felt able to face the fact with equanimity. Poor Jack Gisburn!"
ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))

#Adding 2 more tokens to the vocabulary
print("\n","-"*30,"Adding 2 more tokens to the vocabulary","-"*30)
all_tokens=sorted(list(set(preprocessed)))
all_tokens.extend(['<unk>','<endoftext>'])
vocab={token:integer for integer, token in enumerate(all_tokens)}
print(len(vocab.items()))

#Testing SimpleTokenizerV2
print("\n","-"*30,"Testing SimpleTokenizerV2","-"*30)
from SimpleTokenizer import SimpleTokenizerV2
tokenizer = SimpleTokenizerV2(vocab)
text="Hello, World. This is a test.--?! This sentence contains some unknown tokens like @ and #."
text2="Well!--even through the prism of Hermia's tears I felt able to face the fact with equanimity. Poor Jack Gisburn!"
text = " <endoftext> ".join((text,text2))
ids=tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))

