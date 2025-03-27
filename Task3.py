import re

text = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
# Convert text to lowercase
normalized_text = text.lower()

# Split the text into sentences based on periods
sentences = normalized_text.split('.')

# Check if there is a part before a colon and treat it as the first "sentence"
colon_split = normalized_text.split(':', 1)
if len(colon_split) > 1:
    first_part = colon_split[0].strip()
    # Add the first part before the colon as the first sentence if it's not empty
    sentences = [first_part] + sentences

# Extract the last word of each sentence
last_words = [sentence.strip().split()[-1] for sentence in sentences if sentence.strip()]

# Create a new sentence from the last words of each sentence
last_words_sentence = ' '.join(last_words) + '.'


# Add the new sentence to the end of the original text
final_text = normalized_text.strip() + '\n' + last_words_sentence

# Function to capitalize the first letter after a period, colon, or start of the text
def capitalize_after_period_and_colon(text):
    # Capitalize first letter after a period, colon, or the start of the text
    text = re.sub(r'(^|\.\s*|\:\s*)([a-z])', lambda match: match.group(1) + match.group(2).upper(), text)
    return text
# Apply the function to the normalized text
capitalized_text = capitalize_after_period_and_colon(final_text)

# Function to replace 'iz' with 'is' unless it's surrounded by quotes
def replace_iz_not_in_quotes(text):
    # Replace 'iz' with 'is' unless it's inside quotes
    text = re.sub(r'(?<!“)(?<!")(iz)(?!”)(?!")', 'is', text)
    return text

# Apply the function to the normalized text
modified_text = replace_iz_not_in_quotes(capitalized_text)

# Function to add space after "fix" before a quote

def add_space_after_fix(text):
    # Add a space after "fix" before the quote (with typographic quotes)
    text = re.sub(r'(Fix)(?=“)', r'\1 ', text)
    return text
new_text = add_space_after_fix(modified_text)


# Function to remove extra whitespaces
def remove_extra_whitespaces(text):
    # Replace multiple consecutive whitespaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove leading and trailing whitespaces
    text = text.strip()
    return text

# Apply the function to remove extra whitespaces
final_text_with_single_spaces = remove_extra_whitespaces(new_text)

# Function to count all whitespace characters, including spaces, tabs, and newlines
def count_whitespaces(text):
    return sum(1 for char in text if char.isspace())

# Count the number of whitespace characters in the modified text
whitespace_count = count_whitespaces(final_text_with_single_spaces)

# Print the modified text
print("Final text:\n", final_text_with_single_spaces)
print("Number of whitespace:", whitespace_count)



