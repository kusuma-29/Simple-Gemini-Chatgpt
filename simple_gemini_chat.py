import google.generativeai as genai

API_KEY = "AIzaSyCOv3D4jjJ52s8Fv6RGNgefiM_I7nkBncw"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()

while True:
    user_input = input("🧑 You: ")
    if user_input.lower() == "exit":
        break

    prompt = (
        f"You are a helpful assistant. Respond to the user's message in plain text, "
        f"without using markdown, formatting symbols (like **, ##, ```, or code blocks), "
        f"and keep it under 400 words:\n{user_input}"
    )

    response = chat.send_message(prompt)
    print("🤖 Gemini:", response.text.strip())
