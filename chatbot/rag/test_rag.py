from .query_rag import query_rag
from langchain_ollama import OllamaLLM
EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'true' or 'false')
Does the actual response match the expected response?
"""

def test_franchise_concepts():
    assert query_and_validate(
        question="What is the definition of a franchise business model?",
        expected_response="A franchise is a business model where a company (franchisor) grants rights to other businesses (franchisees) to use their brand, systems, and processes in exchange for fees and royalties.",
    )

def test_franchise_requirements():
    assert query_and_validate(
        question="What are the main requirements to become a franchisee?",
        expected_response="The main requirements typically include initial capital investment, franchise fees, meeting franchisor's standards, and following the established business model.",
    )

def query_and_validate(question: str, expected_response: str):
    response_text = query_rag(question)[0]
    prompt = EVAL_PROMPT.format(
        expected_response=expected_response,
        actual_response=response_text
    )
    model = OllamaLLM(model="mistral")
    evaluation_results_str = model.invoke(prompt)
    evaluation_results_str_cleaned = evaluation_results_str.strip().lower()
    print(prompt)

    if "true" in evaluation_results_str_cleaned:
        print("\033[92m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return True
    elif "false" in evaluation_results_str_cleaned:
        print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return False
    else:
        raise ValueError(f"Invalid evaluation result. Cannot determine if 'true' or 'false'.")