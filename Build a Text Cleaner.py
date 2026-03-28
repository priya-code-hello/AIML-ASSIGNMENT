import string

text = "Hii brooo!!! I am sooo happy 😊, pls send notes!!!"


text = text.lower()


text = text.translate(str.maketrans('', '', string.punctuation))


stopwords = ["i", "am", "is", "are", "the", "pls"]

words = text.split()

clean_words = [word for word in words if word not in stopwords]

clean_text = " ".join(clean_words)

print("Original:", "Hii brooo!!! I am sooo happy 😊, pls send notes!!!")
print("Cleaned:", clean_text)