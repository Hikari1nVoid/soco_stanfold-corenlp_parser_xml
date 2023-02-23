import xml.etree.ElementTree as ET
import csv

Males = ['luke','ted','david','matthew','jake','rick','josh','tony','aaron','michael','nick','george','john']
males_dict = {name: 0 for name in Males}
Females = ['judith','tia','meg','vicky','eva','julie','rita','leah','caroline','cintihia','ariel','macy','lynn','rebecca','cinthia','mara','amy','michelle']
females_dict = {name: 0 for name in Females}
# parse the XML file
tree = ET.parse('groupa.xml')

# get the root element
root = tree.getroot()

# define the tags you want to extract
sentence_tagname = 'sentence'
word_tagname = 'word'
pos_tagname = 'POS'
token_tagname= 'token'
# loop through all <sentence> elements with an 'id' attribute
for sentence_elem in root.iter(sentence_tagname):
    if 'id' in sentence_elem.attrib:
        sentence_id = sentence_elem.attrib['id']
        #print(f"Sentence ID: {sentence_id}")
    for token_elem in sentence_elem.iter(token_tagname):

        # loop through all <word> elements within the current <sentence> element
        for word_elem in sentence_elem.iter(word_tagname):
            word_text = word_elem.text
            #print(f"Word Text: {word_text}")
            break

            # find the <POS> element that is a direct child of the current <word> element
        pos_elem = token_elem.find(pos_tagname)
        if pos_elem is not None:
            pos_text = pos_elem.text
            if pos_text == 'PRP' and word_text in Males:
                males_dict[word_text]+=1
            elif pos_text == 'PRP' and word_text in Females:
                females_dict[word_text]+=1

tree2 = ET.parse('groupb.xml')

# get the root element
root2 = tree2.getroot()
for sentence_elem in root2.iter(sentence_tagname):
    if 'id' in sentence_elem.attrib:
        sentence_id = sentence_elem.attrib['id']
        #print(f"Sentence ID: {sentence_id}")
    for token_elem in sentence_elem.iter(token_tagname):

        # loop through all <word> elements within the current <sentence> element
        for word_elem in sentence_elem.iter(word_tagname):
            word_text = word_elem.text
            #print(f"Word Text: {word_text}")
            break

            # find the <POS> element that is a direct child of the current <word> element
        pos_elem = token_elem.find(pos_tagname)
        if pos_elem is not None:
            pos_text = pos_elem.text
            if pos_text == 'PRP' and word_text in Males:
                males_dict[word_text]+=1
            elif pos_text == 'PRP' and word_text in Females:
                females_dict[word_text]+=1
print(males_dict)
print(females_dict)
print("\n")
mvalues_list = list(males_dict.values())
fmmvalues_list = list(females_dict.values())
print(mvalues_list)
print(fmmvalues_list)
import csv



# open the file in write mode
with open('output.csv', 'w', newline='') as f:
    # create a CSV writer object
    writer = csv.writer(f)
    
    # write the header row
    writer.writerow(['male', 'pronoun'])
    
    # loop through the keys of the dictionaries and write the values to the CSV file
    for key in males_dict:
        if males_dict[key] != 0 :
            writer.writerow([key,males_dict[key]])


    
    # write the header row
    writer.writerow(['female', 'pronoun'])
    
    # loop through the keys of the dictionaries and write the values to the CSV file
    for key in females_dict:
        if females_dict[key] != 0 :
            writer.writerow([key,females_dict[key]])