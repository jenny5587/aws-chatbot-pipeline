import os
from langchain.llms.bedrock import Bedrock

def get_text_response(input_content):

    llm = Bedrock(
        # credentials_profile_name=os.environ.get("**"),
        # region_name=os.environ.get("us-east-1"), 
        # endpoint_url=os.environ.get("**"), 
        model_id="anthropic.claude-v2", 
        model_kwargs={
            "max_tokens_to_sample": 512,
            "temperature": 0,
            "top_p": 0.1,
            "top_k": 0,
        }
    )
    
    return llm.predict(input_content)
