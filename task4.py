import re
import random
import string


def generate_random_dicts(count_range =(2,100), key_range =(1,5), value_range= (0,100)):
    num_dicts = random.randint(count_range[0],count_range[1])
    dicts = []

    for i in range(num_dicts):
        num_keys = random.randint(key_range[0], key_range[1])
        random_disct = {random.choice(string.ascii_lowercase): random.randint(value_range[0],value_range[1])
                        for i in range(num_keys)}
        dicts.append(random_disct)

    return dicts

random_dicts = generate_random_dicts()
print(random_dicts)

def merge_dicts_with_max_value(dicts):
    merged_dict = {}
    for i,d in enumerate(dicts,start=1):
        for key, value in d.items():
            if key in merged_dict:
                if value > merged_dict[key][0]:
                    merged_dict[key] = (value, i)
            else:
                merged_dict[key] = (value, None)

    result = {f"{key}_{idx}" if idx else key: value
          for key, (value, idx) in merged_dict.items()}

    return result

merged_result = merge_dicts_with_max_value(random_dicts)
print("Merged dict:", merged_result)



text = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

def process_text(text):
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

    return final_text


# Function to capitalize the first letter after a period, colon, or start of the text
def capitalize_after_period_and_colon(text):
    # Capitalize first letter after a period, colon, or the start of the text
    final_text = re.sub(r'(^|\.\s*|\:\s*)([a-z])', lambda match: match.group(1) + match.group(2).upper(), text)
    return final_text


# Function to replace 'iz' with 'is' unless it's surrounded by quotes
def replace_iz_not_in_quotes(text):
    # Replace 'iz' with 'is' unless it's inside quotes
    final_text = re.sub(r'(?<!“)(?<!")(iz)(?!”)(?!")', 'is', text)
    return final_text


# Function to add space after "fix" before the quote (with typographic quotes)
def add_space_after_fix(text):
    # Add a space after "fix" before the quote (with typographic quotes)
    final_text = re.sub(r'(Fix)(?=“)', r'\1 ', text)
    # # Add a space after "fix" before the quote (with typographic quotes)
    # text = re.sub(r'(Fix)(?=“)', r'\1 ', text)
    return final_text


# Function to remove extra whitespaces
def remove_extra_whitespaces(text):
    # Replace multiple consecutive whitespaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove leading and trailing whitespaces
    final_text = text.strip()
    return final_text


# Function to count all whitespace characters, including spaces, tabs, and newlines
def count_whitespaces(text):
    return sum(1 for char in text if char.isspace())


# Apply the processing functions in order
processed_text = process_text(text)
capitalized_text = capitalize_after_period_and_colon(processed_text)
modified_text = replace_iz_not_in_quotes(capitalized_text)
text_with_spaces = add_space_after_fix(modified_text)
final_text_with_single_spaces = remove_extra_whitespaces(text_with_spaces)

# Count the number of whitespace characters in the final processed text
whitespace_count = count_whitespaces(final_text_with_single_spaces)

# Print the modified text and the whitespace count
print("Final text:\n", final_text_with_single_spaces)
print("Number of whitespace:", whitespace_count)