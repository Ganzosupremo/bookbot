def get_book(path:str) -> str:
    with open(path) as f:
        return f.read()

def count_words(book:str) -> int:
    return len(book.split())

def count_single_words(book:str) -> dict:
    character_dic = {}
    words = book.split()
    
    for word in words:
        lowered_word = word.lower()
        for c in lowered_word:
            if c in character_dic:
                character_dic[c] += 1
            else:
                character_dic[c] = 1
        
    return character_dic
    
    
def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(chars_dict:dict) -> list:
    sorted_list = []
    for c in chars_dict:
        sorted_list.append({"char":c,"num":chars_dict[c]})
    sorted_list.sort(reverse=True,key=sort_on)
    
    return sorted_list

def create_report(book_path:str):
    print(f"------- Begin Report of {book_path} --------")
    contents = get_book(book_path)
    words_in_book = count_words(contents)
    char_in_book = count_single_words(contents)
    char_sorted_list = dict_to_sorted_list(char_in_book)
    
    print(f"They were {words_in_book} words found in the book...")
    
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

        
    print("------ That's the End of the Report -------")        

def main() -> None:
    book_path = "books/frankenstein.txt"
    create_report(book_path,)
        

main()