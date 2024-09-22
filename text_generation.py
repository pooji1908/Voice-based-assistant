import openai

def get_reply(question, api_key):
    try:
        openai.api_key = api_key
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': "system", 'content': "You are a helpful assistant"},
                {'role': 'user', 'content': question}
            ],
            max_tokens=200
        )
        answer = completion.choices[0].message['content']
        return answer
    except Exception as e:
        print(f"Error in getting response: {e}")
        return "Sorry, I couldn't process your request."
