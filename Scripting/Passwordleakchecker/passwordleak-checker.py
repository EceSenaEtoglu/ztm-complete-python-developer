import requests
import hashlib


def request_api_data(query_char):
    """requests data from https://haveibeenpwned.com"""

    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')
    return res


def get_pass_leaks_count(res_txt, searched_tail):
    """given response text from API and a password's data (hashed tail) returns how many
    times that password has been leaked"""
    # eliminate \n  chars from API response
    lines = res_txt.splitlines()

    # added O(1) look up
    # create dict with tail as key, value as leak count
    hash_dict = {}

    for line in lines:
        tail, leak = line.split(":")
        hash_dict[tail] = int(leak)

    # return the leak count if exists
    # else return 0
    if searched_tail in hash_dict:
        return hash_dict[searched_tail]

    return 0


def pwned_api_check(password):
    """given a password returns how many times it has been leaked"""
    #  hashes the function with sha1 function
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # the API used asks for the head
    first5_char, tail = sha1password[:5], sha1password[5:]

    # get the response from API
    response = request_api_data(first5_char)

    # return leak count
    return get_pass_leaks_count(response.text, tail)


def get_password_data(filename):
    try:
        password_lst = []
        with open(filename, "r") as file:
            for line in file:
                # eliminate \n,\r chars coming from file
                password_lst.append(line.rstrip("\n,\r"))

        if len(password_lst) != 0:
            return password_lst
        else:
            print(f"{filename} has no data. What are you trying to do?")
            print("This will be reported.")

    except FileNotFoundError:
        print(f'file named {filename} couldn\'t be found\nPlease check your file and run again')


def main(password_lst):

    if password_lst:

        # loop through passwords
        # calculate how many times each pass has been leaked
        for i in range(len(password_lst)):

            print("\nCALCULATING...")
            leak_count = pwned_api_check(password_lst[i])
            print("DONE\n")
            msg = f'According to data I\'ve got from https://haveibeenpwned.com/, password numbered {i + 1}\n' \
                  f'Has been detected in data breach {leak_count} times.'

            if leak_count == 0:
                print(f"{msg}")

            elif leak_count < 8:
                print(f"Hmm {msg}")

            else:
                print(f"OH NO!\n{msg}")


if __name__ == "__main__":

    try:
        print("As my friend Root says:\"You'd be amazed at how much information is being collected every day\"")
        print("Command lines can be scary. Let's increase the security and do this thing via file")
        print("\nLoading the system...\n")
        file_name = input("Enter the file's name that has the password(s) line by line: ")
        main(get_password_data(file_name))

    except:
        print("Sorry. Something went wrong, I'm not sure why...")
