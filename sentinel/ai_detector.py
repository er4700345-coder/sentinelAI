from openai import OpenAI

class AIDetector:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def analyze(self, code_snippet):

        prompt = f"""
        Analyze this code for security vulnerabilities.
        Suggest fixes if needed.

        CODE:
        {code_snippet}
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}]
        )

        return response.choices[0].message.content
