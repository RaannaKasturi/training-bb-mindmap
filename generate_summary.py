import json
from get_llm_data import extract_markdown, get_data
import threading
import time
from playsound import playsound

dataset = []
with open("mindmap_dataset.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

for counter, d in enumerate(data[1000:1500], 1):
    try:
        print(f"Processing {counter} of {len(data[1000:1500])}")
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

print("Writing to final_dataset-1500.json")
with open("final_dataset-1500.json", 'w', encoding='utf-8') as f:
    json.dump(dataset, f, indent=4)

def play_sound():
	while not stop_event.is_set():
		time.sleep(5)
		playsound('output.wav')

stop_event = threading.Event()
thread = threading.Thread(target=play_sound)
thread.start()

while True:
	user_input = input("Type 'STOP' to stop the audio: ")
	if user_input.strip().upper() == "STOP":
		stop_event.set()
		thread.join()
		break

print("Done")
