import json
import sys

MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"rules": []}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def add_rule(new_rule):
    memory = load_memory()
    memory["rules"].append(new_rule)
    save_memory(memory)
    print(f"✅ Rule added: {new_rule}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Please provide a rule as an argument.")
    else:
        rule = " ".join(sys.argv[1:])
        add_rule(rule)