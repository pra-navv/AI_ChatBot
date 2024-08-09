import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "YOUR API KEY"

    def get_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("What is Artificial Intelligence?")
    print(response)
