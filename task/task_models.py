from task.app.main import run

def start(): 
    print("🤖 Testing GPT-4o")
    print("When prompted, ask: What LLMs can do?")
    print("Then type 'exit' to finish")

    run(
        deployment_name='gpt-4o',
        print_request=False,
        print_only_content=True,
    )


    print("🤖 Testing Claude")
    print("When prompted, ask: What LLMs can do?")
    print("Then type 'exit' to finish")

    run(
        deployment_name='claude-sonnet-4@20250514',
        print_request=False,
        print_only_content=True,
    )


    print("🤖 Testing Gemini")
    print("When prompted, ask: What LLMs can do?")
    print("Then type 'exit' to finish")

    run(
        deployment_name='gemini-2.5-pro',
        print_request=False,
        print_only_content=True,
    )