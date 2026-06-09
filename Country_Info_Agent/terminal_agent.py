from agent import run_agent


print("Country Agent Started")
print("Type exit to quit")


while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    response = run_agent(user)

    print("Agent:", response)