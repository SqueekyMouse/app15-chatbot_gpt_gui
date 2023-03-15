import openai

# commit: openai chat class created Sec49

# install openai,
# sign in to platform.openai.com to get api key
# will use davinci3 algo

# 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
class Chatbot:
    def __init__(self) -> None:
        openai.api_key='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'

    def get_response(self,user_input):
        response=openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        # max_tokens - basically how long should the reply be
        # temparature - 0 exact answer but rigid, high - low accuracy but diverse
        return(response)
    

if __name__=='__main__':
    chatbot=Chatbot()
    response=chatbot.get_response('Write a joke about birds')
    print(response)