from router import route

question = input("Ask your question: ")

print("\n" + "=" * 60)
print("AI Support Agent")
print("=" * 60)

print(route(question))