import csv
import os

csv_file = '/Users/khalidaitelmaati/Desktop/scrapy-master/psychology-theme-main/pinterest_all_pins.csv'
temp_file = csv_file + '.tmp'

with open(csv_file, 'r', encoding='utf-8') as f_in, open(temp_file, 'w', encoding='utf-8', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    header = next(reader)
    # Add Alt Text column
    header.insert(4, 'Alt Text')
    writer.writerow(header)
    
    for row in reader:
        title = row[1]
        alt_text = f'A graphic design featuring the text "{title}" with a calming, psychological background. The image promotes an educational article on leafanoo.com about mental health, psychology, and emotional well-being.'
        
        # row structure: 0=Article, 1=Title, 2=Description, 3=Link, 4=Board, 5=Prompt
        row.insert(4, alt_text)
        writer.writerow(row)

os.replace(temp_file, csv_file)
print("Added Alt Text column to CSV!")
