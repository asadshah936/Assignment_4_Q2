from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, OpenAIChatCompletionsModel,set_tracing_disabled

api_key="AIzaSyDkt2PqE_yNwG-U0vc0TSbr4ujT8SfkkmQ",
model = "gemini-2.5-flash"

external_client= AsyncOpenAI(
    api_key=api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)
set_default_openai_client(external_client)
set_tracing_disabled(True)
llm_model= OpenAIChatCompletionsModel(
    model=model,
    openai_client=external_client,
)
agent=Agent(
    name="Asad",
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
    model=llm_model
)

def main():
    result = Runner.run_sync(agent, "What is AI?")
    print(result.final_output)
