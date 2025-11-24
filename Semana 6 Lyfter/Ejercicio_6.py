def sort_hyphenated_words(text):
    words=text.split("-")              #1 Split the string into a list (using "-" as separator)
    words.sort()                       #2 Sort the list alphabetically
    sorted_text = "-".join(words)      #3 Join the list back into a string with "-"
    return sorted_text


result = sort_hyphenated_words("alex-actor-music-festival-electronic-loop-phone")
print(result)



#List: It's like a row of boxes, each containing a word.

#split: Cuts the string and puts each part in a box (list).

#sort: Arranges the boxes in alphabetical order.

#join: Joins the boxes back together into a single string, using the separator you specify (-).