import json
from get_llm_data import extract_markdown, get_data

dataset = []
with open("mindmap_dataset.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

for counter, d in enumerate(data[500:1000], 1):
    try:
        print(f"Processing {counter} of {len(data[500:1000])}")
        instruction = d['instruction']
        input_text = d['input']
        fetched_data = get_data(input_text)
        summary = extract_markdown(fetched_data)
        output = summary.replace("\n", "\\n").strip()
        print("Summary Generated for", counter)
        entry = {
            "instruction": instruction,
            "input": input_text,
            "output": output
        }
        dataset.append(entry)
    except Exception as e:
        print(f"Error on entry {counter}: {e}")

print("Writing to final_dataset-1000.json")
with open("final_dataset-1000.json", 'w', encoding='utf-8') as f:
    json.dump(dataset, f, indent=4)

print("Done")
