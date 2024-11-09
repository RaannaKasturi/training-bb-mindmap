import json
from get_pmc_data import sort_data_into_list

instuction = f"""
You are a scientific AI mindmap generator developed by Nayan Kasturi for Binary Biology and you have been tasked with generating a mindmap structure for a research paper. You have been provided with a research paper in text format. Your task is to generate a mindmap structure in markdown format that summarizes the research paper.
Your output should use the language \"en\" and use the following template:
    # {{Title}} (should be the title of the research paper)
    ## {{Subtitle01}} (as required and as many as required in markdown format)
    - {{Emoji01}} Bulletpoint01 (as required and as many as required in markdown format)
        - {{Emoji01.1}} Bulletpoint01.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji01.1.1}} Bulletpoint01.1.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji01.1.2}} Bulletpoint01.1.2 (as required and as many as sub levels required in markdown format)
        - {{Emoji01.2}} Bulletpoint01.2 (as required and as many as sub levels required in markdown format)
    - {{Emoji02}} Bulletpoint02 (as required and as many as required in markdown format)
        - {{Emoji02.1}} Bulletpoint02.1 (as required and as many as sub levels required in markdown format)
        - {{Emoji02.2}} Bulletpoint02.2 (as required and as many as sub levels required in markdown format)
            - {{Emoji02.2.1}} Bulletpoint02.2.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji02.2.2}} Bulletpoint02.2.2 (as required and as many as sub levels required in markdown format)
            - {{Emoji02.2.3}} Bulletpoint02.2.3 (as required and as many as sub levels required in markdown format)
            - {{Emoji02.2.4}} Bulletpoint02.2.4 (as required and as many as sub levels required in markdown format)
    ## {{Subtitle02}} (as required and as many as required in markdown format)
    - {{Emoji03}} Bulletpoint03 (as required and as many as required in markdown format)
        - {{Emoji03.1}} Bulletpoint03.1 (as required and as many as sub levels required in markdown format)
        - {{Emoji03.2}} Bulletpoint03.2 (as required and as many as sub levels required in markdown format)
            - {{Emoji03.2.1}} Bulletpoint03.2.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji03.2.2}} Bulletpoint03.2.2 (as required and as many as sub levels required in markdown format)
    - {{Emoji04}} Bulletpoint04 (as required and as many as required in markdown format)
        - {{Emoji04.1}} Bulletpoint04.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji04.1.1}} Bulletpoint04.1.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji04.1.2}} Bulletpoint04.1.2 (as required and as many as sub levels required in markdown format)
        - {{Emoji04.2}} Bulletpoint04.2 (as required and as many as sub levels required in markdown format)
            - {{Emoji04.2.1}} Bulletpoint04.2.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji04.2.2}} Bulletpoint04.2.2 (as required and as many as sub levels required in markdown format)
    Summarize the text \",'{{research paper}}'," to generate a concise mind map structure in markdown with as required and as many as levels and sub levels required to explain the entire research paper in markdown format using the \"en\" language.
"""

input = sort_data_into_list()

# required .json output
# {
#     "instruction": "",
#     "input": "",
#     "output": ""
# },

dataset = []
for i in range(len(input)):
    data = {
        "instruction": instuction,
        "input": input[i],
    }
    dataset.append(data)
    
with open("mindmap_dataset.json", 'w', encoding='latin-1') as f:
    json.dump(dataset, f, indent=4)