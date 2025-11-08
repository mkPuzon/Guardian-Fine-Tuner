# Guardian: Fine-tuning DistilBERT for Content Moderation

A project for fine-tuning a LLMs using LoRA (Low-Rank Adaptation) for content moderation tasks, with options for model merging and API deployment.

## Features

- Fine-tune DistilBERT using LoRA for efficient training
- Merge LoRA weights with the base model for standalone deployment
- Deploy as a FastAPI web service with Docker
- Simple REST API for text classification

## Prerequisites

- Python 3.11+
- PyTorch
- Transformers
- PEFT (Parameter-Efficient Fine-Tuning)
- FastAPI
- Docker (for deployment)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd guardian
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Fine-tuning the Model

Run the fine-tuning script with default parameters:
```bash
python training/fine_tuning_pipeline.py
```

### 2. Merging LoRA Weights (Optional)

To merge the fine-tuned LoRA weights with the base model:
```bash
python training/merge_model.py
```

### 3. Local Development

Run the FastAPI server locally:
```bash
uvicorn app.main:app --reload
```

### 4. Docker Deployment

Build the Docker image:
```bash
docker build -t guardian-api .
```

Run the container:
```bash
docker run -p 8000:8000 guardian-api
```

## API Documentation

Once running, access the API documentation at:
```
http://localhost:8000/docs
```

### Example Request

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "Your text to classify"
  }'
```

### Response Format

```json
{
  "label": "Appropriate",
  "score": 0.98
}
```

## Project Structure

```
guardian/
├── app/
│   └── main.py           # FastAPI application
├── training/
│   ├── fine_tuning_pipeline.py  # Model training with LoRA
│   ├── merge_model.py           # Merge LoRA weights
│   └── load_custom_data.py      # Data loading utilities
├── Dockerfile                   # Container configuration
├── requirements.txt             # Python dependencies
└── requirements-dev.txt         # dependencies for notebooks and datasets
```

