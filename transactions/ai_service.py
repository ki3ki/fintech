# from transformers import pipeline

# classifier = pipeline(
#     "zero-shot-classification",
#     model="typeform/distilbert-base-uncased-mnli"
# )

# CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Others"]

# def categorize_transaction(text):
#     result = classifier(text, CATEGORIES)
#     return result["labels"][0]

from transformers import pipeline

_classifier = None  # global variable

CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Others"]

def get_classifier():
    global _classifier
    if _classifier is None:
        print("🔄 Loading AI model...")
        _classifier = pipeline(
            "zero-shot-classification",
            model="typeform/distilbert-base-uncased-mnli"
        )
    return _classifier


def categorize_transaction(text):
    classifier = get_classifier()
    result = classifier(text, CATEGORIES)
    return result["labels"][0]