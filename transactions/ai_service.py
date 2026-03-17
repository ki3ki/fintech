from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Others"]

def categorize_transaction(text):
    result = classifier(text, CATEGORIES)
    return result["labels"][0]