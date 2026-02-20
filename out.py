import os

OUTPUT_DIR = "./buckets_of_truth"

def verify_objective():
    print(f"{'University File':<30} | {'Status':<10} | {'Key Deadline'}")
    print("-" * 60)
    
    for filename in os.listdir(OUTPUT_DIR):
        if filename.startswith("bucketed_"):
            path = os.path.join(OUTPUT_DIR, filename)
            with open(path, 'r') as f:
                content = f.read().lower()
                
                # Check for our 'Buckets of Truth'
                has_gates = "gate" in content or "gpa" in content
                has_logistics = "deadline" in content or "jan" in content or "nov" in content
                
                status = "✅ PASS" if (has_gates and has_logistics) else "⚠️ INCOMPLETE"
                
                # Simple logic to find a date for the dashboard
                deadline = "Not Found"
                for word in content.split():
                    if "nov" in word or "jan" in word:
                        deadline = word
                
                print(f"{filename:<30} | {status:<10} | {deadline}")

if __name__ == "__main__":
    verify_objective()