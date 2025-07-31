

alphabet_dict = {
    "a" : "ᔑ",
    "b" : "ʖ",
    "c" : "ᓵ",
    "d" : "↸",
    "e" : "ᒷ",
    "f" : "⎓",
    "g" : "⊣",
    "h" : "⍑",
    "i" : "╎",
    "o" : "𝙹",
    "u" : "⚍",
    "r" : "∷",
    "t" : "ℸ",
    "y" : "||",
    "p" : "!¡",
    "s" : "ᓭ",
    "j" : "⋮",
    "k" : "ꖌ",
    "l" : "ꖎ",
    "m" : "ᒲ",
    "n" : "リ",
    "v" : "⍊",
    "x" : "̇/",
    "z" : "⨅",

}

def main():
    input_string = input("Type the sentence you want to translate:")
    new_string = []
    for char in input_string:
        if char in alphabet_dict:
            new_string.append(alphabet_dict[char])
    print("".join(new_string))


main()


