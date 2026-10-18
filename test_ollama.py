import ollama

MODEL = "hf.co/Boollm/Qwen3.5-4B-GGUF:Q4_K_M"

def main():
    response = ollama.chat(
        model = MODEL,
        messages=[
            {
                "role":"user",
                "content": (
                    "summarize this email in one sentence: "
                    "Your college assignment must be submitted by Friday."
                )

            }
        ],
        options ={
            "temperature":0.1,
            "num_ctx":8192
        }
    )

    print("\nQwen Response:")
    print(response["message"]["content"])

if __name__ == "__main__":
    main()