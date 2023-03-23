import paralleldots

class API:

    def __init__(self) -> None:
        # Setting your API key
        paralleldots.set_api_key('tDqM6nvLOefEjo2LrZw8k8GObhCZ8mMF180a9Gf7R8A')

    def sentiment_analysis(self,txt):
       response =  paralleldots.sentiment(txt)
       return response
    
    def ner_analysis(self,txt):
       response =  paralleldots.ner(txt)
       return response
    
    def emotion_analysis(self,txt):
       response =  paralleldots.emotion(txt)
       return response
