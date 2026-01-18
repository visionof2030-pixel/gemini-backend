from fastapi import Request

@app.post("/ask")
async def ask(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt") or data.get("text") or data.get("message")

        if not prompt:
            return {"error": "prompt is required"}

        genai.configure(api_key=get_api_key())
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)

        return {"answer": response.text}

    except Exception as e:
        return {"error": str(e)}