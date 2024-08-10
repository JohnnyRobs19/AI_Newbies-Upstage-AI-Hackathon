# AI_Newbies-Upstage-AI-Hackathon

## Overview
This repository contains the code and documentation for the AI_Newbies team participating in the Upstage AI Hackathon. Our project focuses on implementing a fine-tuned model that showcases how tourism ambassadors can leverage AI to promote tourism in Jeju. These ambassadors can use the model to communicate in a manner that reflects their unique personalities and insights about local attractions.

## Institution
University of Malaya, Malaysia

## Team Members
1. Jonathan Siew Zunxian
2. Ooi Rui Zhe (Rexton)
3. Wong Yoong Yee (Mack)

## Brief Synopsis
This project includes two main Jupyter notebooks:
1. [AINewbiesTourismGPT solar_predibase.ipynb](https://github.com/JohnnyRobs19/AI_Newbies-Upstage-AI-Hackathon/blob/dev_Jon/AINewbiesTourismGPT%20solar_predibase.ipynb)
2. [Uncle_Roger_AINewbiesTourismGPT_solar_predibase.ipynb](https://github.com/JohnnyRobs19/AI_Newbies-Upstage-AI-Hackathon/blob/dev_Jon/Uncle_Roger_AINewbiesTourismGPT_solar_predibase.ipynb)

These notebooks detail our approach to training LLM adapters using data extracted from the Official Jeju Tourism Guidebook (Updated June 2024). LLM adapters are small, trainable components that adjust a large pre-trained language model to specific tasks or datasets without needing to retrain the entire model. By training these adapters, we can customize the model’s responses to better reflect the characteristics and promotional needs of Jeju’s tourism sector.

3. [AI_Newbies Tourism GPT Adapter.zip](https://github.com/JohnnyRobs19/AI_Newbies-Upstage-AI-Hackathon/blob/dev_Jon/AI_Newbies%20Tourism%20GPT%20Adapter.zip)
4. [Uncle Roger AI_Newbies Tourism GPT Adapter.zip](https://github.com/JohnnyRobs19/AI_Newbies-Upstage-AI-Hackathon/blob/dev_Jon/Uncle%20Roger%20AI_Newbies%20Tourism%20GPT%20Adapter.zip)

Inside these adapters, there are 
a. adapter_config.json - This JSON file contains configuration settings for the adapter. It likely specifies how the adapter integrates with the larger model, including settings like the size of the adapter layers, activation functions, and other hyperparameters.
b. adapter_model.safetensors - This is likely a file containing the trained weights of the adapter model. The '.safetensors' extension suggests it's in a format that ensures safe, possibly compressed storage of tensor data.
c. special_tokens_map.json - A JSON file that maps special tokens used by the tokenizer to their respective token IDs. This is important for ensuring that the tokenizer correctly handles unique or non-standard tokens that are significant for the model's training or inference tasks.
d. tokenizer.json - Contains the configuration for the tokenizer, including the vocabulary and rules for splitting and encoding text. This is crucial for preparing input data in a format the model can process.
e. tokenizer.model - The actual tokenizer model file, which is used to tokenize text input for the language model. This may contain the machine learning model or algorithm used for tokenization.
f. tokenizer_config.json - Additional configuration details for the tokenizer, possibly including settings for pre-processing and post-processing of tokens.
g. training_args.bin - A binary file that stores the arguments or parameters used during the training of the adapter. This could include learning rates, batch sizes, number of epochs, and other training-specific settings.
