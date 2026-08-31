import pandas as pd
from transformers import pipeline, set_seed

# ---------------------------------------------------------------------------
# Sample reviews
# ---------------------------------------------------------------------------

# Negative customer review about an iPhone purchase
REVIEW_NEGATIVE = (
    "Extremely disappointed with my recent iPhone purchase from Apple. "
    "The device constantly lags, and the battery life is abysmal, barely "
    "lasting through the day. Despite the hefty price tag, the performance "
    "is far from satisfactory. Customer support has been unhelpful, "
    "providing no viable solutions to address these persistent issues. "
    "This experience has left me regretting my decision to choose Apple, "
    "and I expected much better from a company known for its premium "
    "products."
)

# Positive customer review about an iPhone purchase
REVIEW_POSITIVE = (
    "I recently purchased an iPhone from Apple, and it has been an "
    "absolute delight! The device runs smoothly, and the battery life is "
    "impressive, easily lasting throughout the day. The price, though "
    "high, is justified by the excellent performance and top-notch "
    "customer support. I am thoroughly satisfied with my decision to "
    "choose Apple, and it reaffirms their reputation for delivering "
    "premium products. Highly recommended for anyone seeking a reliable "
    "and high-performance smartphone."
)


def classify_sentiment(reviews: dict) -> None:
    """
    Task 1: Sentiment Classification
    Analyze each review and classify its sentiment (positive / negative).
    """
    sentiment_classifier = pipeline(
        task="text-classification",
        framework="pt",  # Force PyTorch backend to avoid TensorFlow / Keras issues
    )

    for label, review_text in reviews.items():
        outputs = sentiment_classifier(review_text)
        df = pd.DataFrame(outputs)
        print(f"Sentiment for {label}:")
        print(df, "\n")


def generate_customer_service_reply(review_text: str) -> str:
    """
    Task 2: Text Generation
    Generate a customer service response to a given review.
    """
    set_seed(42)  # For reproducible generation

    text_generator = pipeline(
        task="text-generation",
        framework="pt",  # Again, force PyTorch
        # You can also specify a model explicitly, e.g. model="gpt2"
    )

    base_response = (
        "Dear Customer, thank you for taking the time to share your feedback. "
        "I'm very sorry to hear about your experience with your iPhone."
    )

    prompt = review_text + "\n\nCustomer service response:\n" + base_response

    ## generated = text_generator(prompt, max_length=150, num_return_sequences=1)
    generated = text_generator(prompt, max_new_tokens=100, num_return_sequences=1)

    return generated[0]["generated_text"]


def main() -> None:
    reviews = {
        "review1 (negative review)": REVIEW_NEGATIVE,
        "review2 (positive review)": REVIEW_POSITIVE,
    }

    classify_sentiment(reviews)

    reply = generate_customer_service_reply(REVIEW_NEGATIVE)
    print(reply)


if __name__ == "__main__":
    main()
