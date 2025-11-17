import google.generativeai as genai
import json
from datetime import datetime

genai.configure(api_key="your-api-key-here")
model = genai.GenerativeModel('gemini-pro')

def classify_bug(bug_description):
    prompt = f"""You are an expert game QA analyst. Classify this bug report:

Bug Description: {bug_description}

Provide classification in this exact JSON format (no markdown, just JSON):
{{
    "severity": "Critical/High/Medium/Low",
    "type": "Gameplay/UI/Performance/Audio/Network/Other",
    "priority": "P0/P1/P2/P3",
    "suggested_steps": "Brief reproduction steps"
}}"""
    
    try:
        response = model.generate_content(prompt)
        result = response.text.replace("```json", "").replace("```", "").strip()
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def save_to_file(bug_description, classification):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("bug_reports.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"Timestamp: {timestamp}\nBug Description: {bug_description}\nAI Classification:\n{classification}\n")

def main():
    print("🎮 AI-Powered Bug Classifier (Powered by Google Gemini)")
    print("="*60)
    
    while True:
        print("\nEnter bug description (or 'quit' to exit):")
        bug_input = input("> ")
        
        if bug_input.lower() == 'quit':
            print("✅ Thanks for using Bug Classifier!")
            print("📝 Check bug_reports.txt for complete history.")
            break
        
        if not bug_input.strip():
            print("⚠️  Please enter a valid bug description.")
            continue
        
        print("\n🔍 Analyzing bug with Gemini AI...")
        classification = classify_bug(bug_input)
        print("\n✅ Classification Result:")
        print(classification)
        save_to_file(bug_input, classification)
        print("\n📝 Result saved to bug_reports.txt")

if __name__ == "__main__":
    main()
