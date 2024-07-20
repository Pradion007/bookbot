# Defined functions
def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)
    
def char_count(text):
    # for each character in {text}, make it lowercase if it is not defined as whitespace then added to list of characters the text is made up of
    characters = [char.lower() for char in text if not char.isspace()]
   
    char_dict = {} # initialize empty dictionary to hold char -> count as key -> value
    
    for char in characters: # for every item in characters list, if it's in dictionary, +=1 to value, otherwise set value = 1
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_char_data(num_char):
    list_data = []
    
    for char in num_char:
        temp_dict = {"character": char, "count": num_char[char]} # creates temp dictionary of key -> value pair, for each pair in count dict
        list_data.append(temp_dict) 
    
    # sorting function defined
    def sort_on_count(num_char):
        return num_char["count"]
    
    # sort list in descending order
    list_data.sort(reverse=True, key=sort_on_count)
    
    return list_data

# Prints book report for chosen book
def book_report(book_choice):

    book_path = str(book_choice) # should convert choice of book into string path
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_char = char_count(text) # gets initial character data, passed to sort function as num_char = {}
    sorted_char_data = sort_char_data(num_char)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in this document")
    
    # Print sorted character data
    for item in sorted_char_data:
        print(f"The '{item['character']} character was found {item['count']} times")
                
    print(f"--- End report of {book_path} ---")    

def book_list():

    return book_choice
# book_list should show users the list of books they can get a report on 
book_list()

# book_report would then take their input from book_choice and print the report
book_report
