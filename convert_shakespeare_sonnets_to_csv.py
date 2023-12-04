import csv

with open('sonnets.txt', 'r') as file:
    sonnets = file.read().split('\n\n')

sonnet_list = []

for sonnet_text in sonnets:
    sonnet_lines = sonnet_text.strip().split('\n')
    sonnet_text = ' '.join(sonnet_lines[1:])  # Exclude the first line (Roman numeral title)
    sonnet_list.append({'text': sonnet_text})

with open('shakespeare_sonnets.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write sonnets
    for sonnet in sonnet_list:
        writer.writerow([sonnet['text']])
