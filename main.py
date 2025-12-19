from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage
from graph.workflow import build_graph
from utils.pdf_loader import load_pdf_text
import os

def run():
    graph = build_graph()

    document_text = None  # holds PDF content

    print("Agentic AI System with CLI PDF Upload")
    print("Commands:")
    print("  upload <pdf_path>  → upload a PDF")
    print("  exit               → quit\n")

    while True:
        user_input = input("User: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        # Handle PDF upload command
        if user_input.lower().startswith("upload "):
            pdf_name = user_input.split("upload ", 1)[1].strip()
            pdf_path = os.path.join("Docs", pdf_name)

            if not os.path.exists(pdf_path):
                print("❌ File not found.\n")
                continue

            try:
                document_text = load_pdf_text(pdf_path)
                print("✅ PDF uploaded and processed successfully.\n")
            except Exception as e:
                print(f"❌ Failed to load PDF: {e}\n")

            continue

        # Invoke agent workflow
        result = graph.invoke(
            {
                "messages": [HumanMessage(content=user_input)],
                "document_text": document_text
            }
        )

        print("Assistant:", result["messages"][-1].content, "\n")

if __name__ == "__main__":
    run()
