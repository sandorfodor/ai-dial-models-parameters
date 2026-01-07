from task.app.main import run

def start():
    print("🤖 Testing GPT-4o with n=3 (3 response choices)")
    print("When prompted, ask: Why is the snow white?")
    print("Then type 'exit' to finish")
    print("📋 Pay attention to the number of choices in the response!")

    run(
        deployment_name='gpt-4o',
        print_request=False,
        print_only_content=False,  # Set to False to see the full response structure
        n=3  # Generate 3 different response choices
    )

    print("🤖 Testing Claude with n=2 (2 response choices)")
    print("When prompted, ask: Why is the snow white?")
    print("Then type 'exit' to finish")
    print("📋 Pay attention to the number of choices in the response!")

    run(
        deployment_name='claude-sonnet-4@20250514',
        print_request=False,
        print_only_content=False,  # Set to False to see the full response structure
        n=2  # Generate 2 different response choices
    )

    print("🤖 Testing Gemini with n=4 (4 response choices)")
    print("When prompted, ask: Why is the snow white?")
    print("Then type 'exit' to finish")
    print("📋 Pay attention to the number of choices in the response!")

    run(
        deployment_name='gemini-2.5-pro',
        print_request=False,
        print_only_content=False,  # Set to False to see the full response structure
        n=4  # Generate 4 different response choices
    )