import random
import string

def generate_random_dicts():
    # Generate a random number of dictionaries (between 2 and 10)
    num_dicts = random.randint(2,10)
    dicts = []

    for _ in range(num_dicts):
        # Generate a random number of keys (between 2 and 5) for each dictionary
        num_keys = random.randint(2,5)
        random_dict = {}

        for _ in range(num_keys):
            key = random.choice(string.ascii_lowercase)
            random_dict[key] = random.randint(0,100)

        dicts.append(random_dict)
    return dicts

def merge_dicts(dict_list):
    merged_dict={}
    key_tracker={}

    for i, d in enumerate(dict_list, 1): # Enumerate starts from 1 for dict numbering
        for key,value in d.items():
            if key in merged_dict:
                # If key exists, check if the new value is greater than stored value
                if value > merged_dict[key]:
                    merged_dict[key] = value
                    key_tracker[key] = i # Track which dictionary had the max value
            else:
                # If key does not exist, add it directly
                merged_dict[key] = value
                key_tracker[key] = i

    # Rename keys based on dictionary number if there were duplicates
    final_dict = {f"{key}_{key_tracker[key]}" if list(key_tracker.values()).count(key_tracker[key]) > 1 else key: value
                for key, value in merged_dict.items()}

    return final_dict

if __name__ == "__main__":
    random_dicts = generate_random_dicts()
    print("Generate list of dictionaries:", random_dicts)
    merged_result = merge_dicts(random_dicts)
    print("Merged dictionary:", merged_result)