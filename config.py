from dotenv import dotenv_values

_values = dotenv_values()

OPENAI_API_KEY = _values["OPENAI_API_KEY"]
