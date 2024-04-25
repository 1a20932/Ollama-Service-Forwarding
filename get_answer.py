import click
import requests
import json

@click.command()
@click.option('--model', default='gemma', help='The model to use for generation.')
@click.argument('prompt', required=True, type=str)
def generate_text(model, prompt):
    url = 'http://localhost:11434/api/generate'
    payload = {"model": model, "prompt": prompt}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise ValueError(f"Failed to generate text. Server returned status code {response.status_code}")
    response_lines = response.text.split('\n')

    # Remove the last element if it is empty
    if not response_lines[-1]:
        del response_lines[-1]
    for line in response_lines:
        data = json.loads(line)
        print(data['response'], end="")

if __name__ == '__main__':
    generate_text()