import time
import codebug
import font


def show_chars(char_data, code_bug):
    for col_index, data in enumerate(char_data):
        code_bug.set_col(col_index, data >> 3)


def get_display_data(list, length, start):
    data = []
    for _  in range(length):
        data.append(list[start % len(list)])
        start += 1
    return data


def get_word_values(word):
    letter_font = font.Font()
    word_values = []
    for char in word:
        word_values.extend(letter_font.get_font(char))
        word_values.append(0)
    return word_values


def main():
    word = 'codecool'
    code_bug = codebug.CodeBug()
    
    word_values = get_word_values(word)
    start_index = 0
    
    while True:
        code_bug.clear_screen()
        display_data = get_display_data(word_values, 5, start_index)
        show_chars(display_data, code_bug)
        time.sleep(0)
        start_index += 1

    



if __name__ == "__main__":
    main()