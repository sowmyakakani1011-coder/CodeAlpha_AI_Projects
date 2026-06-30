from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "What is AI?",
    "What is Machine Learning?",
    "What is Python?",
    "Who developed Python?"
]

answers = [
    "AI stands for Artificial Intelligence.",
    "Machine Learning is a subset of AI.",
    "Python is a programming language.",
    "Python was developed by Guido van Rossum."
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(questions)

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    query_vec = vectorizer.transform([query])

    similarity = cosine_similarity(query_vec, X)

    index = similarity.argmax()

    print("Bot:", answers[index])