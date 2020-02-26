#!/usr/bin/env python3
# Custom functions, read individual docstrings

def san_input(prompt = "Input: ", type = None):
    """Generalised sanitised input function.
    
    The function sanitises input by type.
    
    Arguments:
        prompt: default = "Input"
                The text to be displayed to prompt the user to enter data.
        type:   default = None
                options: "int", "alpha_word", "alpha_phrase"
                default option returns the input exactly the same as the native input function.
                'int' checks if the input is an integer, prompting for mistakes, only returning if true.
                'alpha_word' checks if the input is a single word comprising only alphabet letters, prompting for mistakes, only returning if true.
                'alpha_phrase' checks if the input is a phrase comprising only words made up of alphabet letters, prompting for mistakes, only returning if true.
                
                IF THE TYPE IS WRONG the function will return the string "'type' argument incorrect"
        Outputs: Dependent on type."""
    if type == None:
        out = input(prompt)
        return out
    elif type == "int":
        int_loop = True
        while int_loop:
            out = input(prompt)
            try:
                out = int(out)
                return out
                int_loop = False
                break
            except ValueError:
                print("Please enter an integer.")
                continue
    elif type == "alpha_word":
        alpha_word_loop = True
        while alpha_word_loop:
            out = input(prompt)
            if out.isalpha() == True:
                return out
                alpha_word_loop = False
                break
            else:
                for ch in out:
                    if ch.isspace() == True:
                        print("Please enter a single word, only using alphabet characters.")
                    else:
                        print("Please input only alphabet characters.")
                continue
    elif type == "alpha_phrase":
        alpha_phrase_loop = True
        while alpha_phrase_loop:
            out = input(prompt)
            for ch in out:
                if ch.isalpha() == False or ch.isspace() == False:
                    print("Please input only alphabet characters or spaces.")
                    continue
                else:
                    return out
                    alpha_phrase_loop = False
                    break
    else:
        return "'type' argument incorrect"