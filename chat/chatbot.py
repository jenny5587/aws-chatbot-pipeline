import os
from langchain.memory import ConversationBufferMemory
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationChain

def get_llm():
        
    model_kwargs = {
        "prompt": "\n\nHuman:<prompt>\n\nAssistant:",
        "max_tokens_to_sample": 1024, 
        "temperature": 0, 
        "top_p": 0.5, 
        "stop_sequences": ["\n\nHuman:"]
    }
    
    llm = Bedrock(
        credentials_profile_name=os.environ.get("**"), 
        region_name=os.environ.get("us-east-1"), 
        endpoint_url=os.environ.get("**"),
        model_id="anthropic.claude-v2",
        model_kwargs=model_kwargs)
    
    return llm

def get_memory(): 
    llm = get_llm()
    chat_memory = ConversationBufferMemory(human_prefix='Human', ai_prefix='Assistant')
    conversation = ConversationChain(llm=llm, verbose=False, memory=chat_memory)
    
    return chat_memory

def get_chat_response(input_text, memory):
    
    llm = get_llm()
    conversation_with_summary = ConversationChain( 
        llm = llm, 
        memory = memory,
        verbose = True
    )
    
    chat_response = conversation_with_summary.predict(input=input_text)
    return chat_response
