# Transformer Example

A small demo using [Hugging Face Transformers](https://huggingface.co/docs/transformers) to:

1. **Classify sentiment** of two sample iPhone customer reviews (one negative, one positive).
2. **Generate a customer service reply** to the negative review.

This shows how transformer pipelines can produce context-aware, human-like text that's useful for automated customer support.

Source: [mytechnotes.net – Transformer Example](https://www.mytechnotes.net/projects/transformer_example)

## Requirements

- Python 3.8+
- PyTorch (CPU build is sufficient)
- Transformers
- pandas

## Setup

```bash
# Install PyTorch CPU wheels
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install / upgrade Transformers and pandas
pip install --upgrade transformers pandas

# (Optional) Remove TensorFlow / Keras to avoid Keras 3 + Transformers conflicts
pip uninstall tensorflow keras -y
```

## Usage

```bash
python transformer_example.py
```

The script will:

1. Load a default `text-classification` pipeline and print sentiment scores for both sample reviews.
2. Load a default `text-generation` pipeline, seed it for reproducibility (`set_seed(42)`), and generate a customer service reply continuing from the negative review.

## Notes

- Both pipelines use `framework="pt"` to force the PyTorch backend and avoid TensorFlow/Keras version conflicts.
- No model is explicitly specified, so Transformers will use its default model for each task (a lightweight sentiment model for classification, and GPT-2 for generation). You can pin a specific model by passing `model="..."` to `pipeline(...)`, e.g. `pipeline(task="text-generation", model="gpt2", framework="pt")`.
- Because no model is pinned, exact output (especially the generated text) may vary between Transformers/model versions, even with a fixed seed.
- This is a demonstration script, not production customer-support code — the generated reply is not reviewed or moderated before being printed.

## Example Output

```
Sentiment for review1 (negative review):
      label     score
0  NEGATIVE  0.999...

Sentiment for review2 (positive review):
      label     score
0  POSITIVE  0.999...

Extremely disappointed with my recent iPhone purchase from Apple. ...

Customer service response:

Dear Customer, thank you for taking the time to share your feedback. I'm very sorry to hear about your experience with your iPhone. ...
```

(Actual scores and generated text will vary by environment and library version.)
