# scripts/generate_insights.py
import os
import json
import random

def get_integrated_data(source_dir="data"):
    """
    Placeholder to simulate loading integrated data from the pipeline.
    """
    print("Loading integrated data...")
    # In a real scenario, this would load data from a database or data lake.
    # For now, we'll use a mock data structure.
    mock_data = {
        "performance_metrics": {
            "cac": 45.50,
            "roas": 3.8,
            "conversion_rate": 0.025
        },
        "top_campaigns": [
            {"name": "Q4 Push", "spend": 5000, "conversions": 110},
            {"name": "Fall Sale", "spend": 3000, "conversions": 80}
        ]
    }
    print("Data loaded.")
    return mock_data

def call_llm_api(prompt, data):
    """
    Simulates calling a large language model API to get insights.
    """
    print(f"Calling LLM with prompt: '{prompt[:50]}...'")
    # Mocked LLM responses based on role
    insights = {
        "Brand Marketer": f"The 'Q4 Push' campaign is getting high conversions ({data['top_campaigns'][0]['conversions']}) but could have its messaging refined to improve brand sentiment.",
        "Media Buyer": f"The ROAS is strong at {data['performance_metrics']['roas']}, but the CAC of ${data['performance_metrics']['cac']} is high. Consider reallocating 15% of budget from 'Fall Sale' to 'Q4 Push'.",
        "Analyst": f"The overall conversion rate is {data['performance_metrics']['conversion_rate']*100}%. There is a weak correlation between ad spend and conversion rate for the 'Fall Sale' campaign.",
        "Designer": "The 'Fall Sale' campaign's creative has a 20% lower CTR than 'Q4 Push'. A/B testing new visuals for 'Fall Sale' is recommended."
    }
    # Return a random insight for demonstration
    role = random.choice(list(insights.keys()))
    return {"role": role, "insight": insights[role]}

def main():
    """Main function to generate insights."""
    print("--- Starting AI Insight Generation ---")
    
    # Load the prompt library to use as a base for analysis
    # In a real app, this would be more sophisticated.
    with open("docs/workflows/Prompt-Library.md", "r") as f:
        prompts = f.read()
    
    print("Loaded prompt library.")

    data = get_integrated_data()
    
    generated_insights = []
    for i in range(4): # Generate one insight for each role
        insight = call_llm_api("Analyze this data and provide an insight.", data)
        generated_insights.append(insight)
        print(f"Generated insight for {insight['role']}: {insight['insight']}")

    # Store insights
    output_file = "generated_insights.json"
    with open(output_file, "w") as f:
        json.dump(generated_insights, f, indent=2)

    print(f"Successfully generated and stored insights in {output_file}")
    print("--- AI Insight Generation Finished ---")

if __name__ == "__main__":
    main() 