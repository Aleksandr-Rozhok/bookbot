def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    def count_words(file):
        return len(file.split())

    def count_chars(file):
        list_of_chars = list(file.lower())
        dict_of_result = {}

        for char in list_of_chars:
            if char in dict_of_result:
                dict_of_result[char] += 1
            else:
                dict_of_result[char] = 1
        
        return dict_of_result
    
    def sort_on(dict):
        return dict["count"]

    def sort_dict(dict):
        list_of_dict_with_chars = []

        for key, val in dict.items():
            if key.isalpha():
                list_of_dict_with_chars.append({"letter": key, "count": val})
        
        list_of_dict_with_chars.sort(reverse=True, key=sort_on)
        return list_of_dict_with_chars

    def send_report():
        num_of_words = count_words(file_contents)
        num_of_chars = count_chars(file_contents)
        list_of_data = sort_dict(num_of_chars)

        print(f"--- Begin report of books/frankenstein.txt --- \n{num_of_words} words found in the document\n")
        
        for item in list_of_data:
            print(f"The {item['letter']} character was found {item['count']} times")
        
        print("--- End report ---")

    send_report()

main()