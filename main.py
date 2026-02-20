import os
from dotenv import load_dotenv
import scaledown

# 1. Load the .env file
load_dotenv()

# 2. Get the key from environment
# Make sure the name matches your .env file exactly
api_key = os.getenv("SCALEDOWN_API_KEY")

if not api_key:
    print("❌ Error: SCALEDOWN_API_KEY not found in .env file.")
else:
    try:
        # 3. Initialize ScaleDown
        # We pass 'api_key' directly as a variable here
        sd = scaledown.ScaleDown(api_key)
        print("✅ ScaleDown initialized successfully using your .env key!")
        
        # Now you can use 'sd' to compress your admission requirements
    except Exception as e:
        print(f"❌ Initialization failed: {e}")
        
# Define our directory paths
INPUT_DIR = "./raw_university_data"
OUTPUT_DIR = "./buckets_of_truth"
print("Available actions:", [method for method in dir(sd) if not method.startswith('_')])
import os

# Get the absolute path of the folder where main.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Link the data folders to that BASE_DIR
INPUT_DIR = os.path.join(BASE_DIR, "raw_university_data")
OUTPUT_DIR = os.path.join(BASE_DIR, "buckets_of_truth")

# This block will now automatically create the folders if you forget!
if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR)
    print(f"📁 Created missing input folder at: {INPUT_DIR}")
    print("👉 Please drop your university .txt files in there and run again.")

# Create the output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def run_admissions_assistant():
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".txt"):
            print(f"🚀 Bucketing: {filename}...")
            
            # Read the file
            with open(os.path.join(INPUT_DIR, filename), 'r', encoding='utf-8') as f:
                raw_content = f.read()

            # Execute the pipeline
            result = sd.optimize_with_pipeline(
                raw_content, 
                "Extract Hard Gates, Narrative Themes, and Logistics."
            )

            # Fix: Access the dictionary using a key instead of an attribute
            # We use .get() as a safety net in case the key name varies
            compressed_data = result.get('final_content') or result.get('content') or str(result)

            # Save the file
            output_file = os.path.join(OUTPUT_DIR, f"bucketed_{filename}")
            with open(output_file, 'w', encoding='utf-8') as f_out:
                f_out.write(compressed_data)
       

    print("\n✅ All programs processed successfully, Sanskar!")

if __name__ == "__main__":
    run_admissions_assistant()