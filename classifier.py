from google.cloud import aiplatform
from google.oauth2 import service_account
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'C:\Users\DebadattaNayak\Desktop\chatbot\responsive-sun-431711-b6-90f457c3c889.json'

def predict_text_classification_single_lable_sample(project,location,endpoint,content):
    if not content or content.strip() == "":
        raise ValueError("Text content is empty. Please provide valid text for classification.")
    try:
        aiplatform.init(project=project,location=location)
        predictor=aiplatform.Endpoint(endpoint_name=endpoint)
        
        result=predictor.predict(instances=[{'content':content}],parameters={})

        names=result[0][0]['displayNames'].copy()
        values=result[0][0]['confidences'].copy()

        print(names,values)

        max_index=values.index(max(values))

        print(names[max_index])
        
        return names[max_index]
    except Exception as e:
        print(f"An error occoures:{e}")
        return None
    
    
    
def classifier(user_input):
    project="responsive-sun-431711-b6"
    location="us-central1"
    endpoint="6242166104907579392"
    content=user_input
     
    return predict_text_classification_single_lable_sample(project,location,endpoint,content)

def classify_text(user_input):
    if not user_input or user_input.strip() == "":
        return "Sorry, I didn't understand that. Could you please provide more information?"

    result=classifier(user_input)

    if result is None:
       result = "Sorry, I couldn't classify your input. Please try again."
    return result
    


