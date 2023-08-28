from translate import Translator

# PRACTICE for THE USAGE OF file io and translate library
# reads English text from file and translates to below far east languages

def get_translated_text(txt_en, lang_choice) -> str:
    modes_ISO639_1 = {"japanese":"ja","korean":"zh","chinese":"ch"}
    translator = Translator(to_lang=modes_ISO639_1[lang_choice])
    # return translated text
    return translator.translate(txt_en)


def get_file_data(file_name):
    # get text data from file
    try:
        with open(file_name,"r") as file_obj:
            return file_obj.read()

    except FileNotFoundError:
        print("OOPS! the file does not exist!")

print("Provide a file that has English text and let me translate it to one of the far east languages below:")
print("Japanese,Chinese,Korean")
file_name = input("your text file name: ")
lang_choice = input("your language choice: ").lower()

translated_text = get_translated_text(get_file_data(file_name),lang_choice)
print("---translating---")
print(f"translation of text written in file {file_name} to {lang_choice} is {translated_text}")