sentence = input("Enter a sentence: ")
# word_list = 
print(f"This sentence has {len(sentence.split())} words")

dig_count = sum(1 for ch in sentence if ch.isdigit())
up_count = sum(1 for ch in sentence if ch.isupper())
low_count = sum(1 for ch in sentence if ch.islower())

print(f"This sentence has {dig_count} digits, {up_count} uppercase letters, and {low_count} lowercase letters.")
