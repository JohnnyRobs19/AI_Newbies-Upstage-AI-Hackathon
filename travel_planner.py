import streamlit as st
import requests
import os
import json
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Function to load the model and tokenizer with adapter configuration
def load_model_and_tokenizer(model_name, adapter_dir):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Load the model
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16,
    )
    
    # Load adapter configuration
    adapter_config_path = os.path.join(adapter_dir, "config.json")
    with open(adapter_config_path, 'r') as f:
        adapter_config = json.load(f)
    
    # Apply the adapter configuration to the model
    model = apply_adapter(model, adapter_config)
    
    return model, tokenizer

# Function to apply adapter configuration to the model
def apply_adapter(model, adapter_config):
    # Implement logic to apply adapter configuration based on your specific setup
    print("Applying adapter configuration...")
    print(adapter_config)
    # Add actual logic here to apply adapter settings to the model
    return model

# Path to the model and adapter
model_name = "UpstageSharePredibase/Solar-1.1-10.7B-32K-chat-240612"
adapter_dir = "AI_Newbies-Upstage-AI-Hackathon\\Uncle Roger AI_Newbies Tourism GPT Adapter"

# Load the model and tokenizer with the adapter
model, tokenizer = load_model_and_tokenizer(model_name, adapter_dir)

# Function to call Upstage API for generating travel plans
def get_travel_plan(destination, start_date, end_date, interests, api_key):
    url = 'https://api.upstage.ai/v1/solar/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    messages = [
        {"role": "system", "content": "You are a helpful assistant specialized in travel planning."},
        {"role": "user", "content": f"Plan a trip to {destination} from {start_date} to {end_date} focusing on {interests}."}
    ]
    data = {
        "model": "solar-1-mini-chat",
        "messages": messages,
        "stream": False
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Streamlit interface
st.title('AI-Powered Travel Planner')
st.write('Plan your trip with AI recommendations based on your preferences.')

# User inputs
destination = st.text_input('Destination', 'e.g., Paris')
start_date = st.date_input('Start Date')
end_date = st.date_input('End Date')
interests = st.text_input('Interests', 'e.g., museums, food, music')

# Button to get travel plan
if st.button('Get Travel Plan'):
    try:
        travel_plan = get_travel_plan(destination, start_date, end_date, interests, api_key)
        st.write(travel_plan)
    except Exception as e:
        st.error(f"Failed to fetch travel plan: {str(e)}")
