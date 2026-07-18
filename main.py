import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

response = client.converse(
    modelId= model_id,
    messages=[
        {
            "role": "user",
            "content": [{"text": "Hello, Bedrock!"}],
        }
    ],
)

print(response["output"]["message"]["content"][0]["text"])
