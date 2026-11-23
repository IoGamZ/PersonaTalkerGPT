from groq import Groq                              
#Import depending on what AI brand and model being used. 
#In this project, Groq was used to test and run the program.
#Make sure to install correct AI requests sechduel...
#IN THIS PROJECT "!pip install groq requests schedule" was used

GROQ_API_KEY = "INPUT VALID API KEY HERE"   #Change this depending on the AI being used
MODEL        = "llama-3.1-8b-instant"                                       #Change this based off the model of the AI beind used

client = Groq(api_key=GROQ_API_KEY)

def ask(question):
    reply = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": question}],
    )
    return reply.choices[0].message.content

Query = str(input("Input your query here:   "))
print(ask(Query))        


#Learning temperatures
reply = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Invent a name for a pet dragon."}],          #Question
    temperature=1.0,   # temperature shows how random the program can be
    #In instance, if temperature is around 0 - 0.3, reponse are more consistant and grounded
    #While temperature 0.4-0.8 reponse are more fresh and contain nuance yet still staying coherent.
    #Lastly, temperature 1 picks less likely words. Being more imaginative but less coherent and can lead to hallucination
)

print(reply.choices[0].message.content)          #Can be replaced with input variable

#Creating Personality 
SYSTEM_PROMPT = "You are a nerd. Answer every question as if you know everything."

def ask_with_personality(question):
    reply = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": question},
        ],
    )
    return reply.choices[0].message.content

P_Query = str(input("Ask anything with a nerd personality:  "))
print(ask_with_personality(P_Query))


#Retaining memory
messages = [{"role": "system", "content": SYSTEM_PROMPT}]  # uses your personality from above

while True:
    user_text = input("You: ")
    if user_text.strip().lower() in ("quit", "exit"):
        break
    messages.append({"role": "user", "content": user_text})  # "append" makes it remember
    reply = client.chat.completions.create(model=MODEL, messages=messages)
    answer = reply.choices[0].message.content                
    messages.append({"role": "assistant", "content": answer})
    print("Bot:", answer)