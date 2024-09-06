import replicate

model = replicate.models.create(
    owner="ummtushar",
    name="pilot",
    visibility="public",  # or "private" if you prefer
    hardware="gpu-t4",  # Replicate will override this for fine-tuned models
    description="A fine-tuned FLUX.1 model v1.1"
)

print(f"Model created: {model.name}")
print(f"Model URL: https://replicate.com/{model.owner}/{model.name}")

# Now use this model as the destination for your training
training = replicate.trainings.create(
    version="ostris/flux-dev-lora-trainer:4ffd32160efd92e956d39c5338a9b8fbafca58e03f791f6d8011f3e20e8ea6fa",
    input={
        "input_images": open("dataset/mcdonalds.zip", "rb"),
        "steps": 500,
        "hf_token": "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",  # optional
        "hf_repo_id": "ummtushar/lora-pilot",  # optional
    },
    destination=f"{model.owner}/{model.name}"
)

print(f"Training started: {training.status}")
print(f"Training URL: https://replicate.com/p/{training.id}")