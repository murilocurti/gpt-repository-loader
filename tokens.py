import tiktoken

# read text from output.txt
text = open("output.txt", "r").read()

# text = "This is an example text."
encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)
print(f"{len(tokens):,}")
