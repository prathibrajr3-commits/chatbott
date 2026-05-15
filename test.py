import google.generativeai as genai
genai.configure(api_key="AIzaSyAUDrvPP36Gl3ECZlo5UdnXCrqqlBXfGHc")
models=genai.list_models()

for model in models:
    print(model.name)
    print(model.supported_generation_methods)
    print("-------------------")