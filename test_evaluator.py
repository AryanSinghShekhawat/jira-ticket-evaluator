from src.evaluator import evaluate_ticket_pr

print("🧪 Testing GitHub PR fetch...")
result = evaluate_ticket_pr("PROJ-123", "https://github.com/langchain-ai/langgraph/pull/100")

print("\n✅ RESULT:")
print(result)
