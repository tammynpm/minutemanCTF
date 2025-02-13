MAPPING = {
    "0": "\u03e1",
    "1": "\u0395",
    "2": "\u02db",
    "3": "\u0324",
    "4": "_",
    "5": "\u0311",
    "6": "\u02d0",
    "7": "\u0082",
    "8": "\u0274",
    "9": "\u00b4",
    "a": "\u0118",
    "b": "\u02d6",
    "c": "\u025a",
    "d": "\u0090",
    "e": "\u016b",
    "f": "\u0365",
    "g": "\u025a",
    "h": "y",
    "i": "\u036f",
    "j": "\u00c9",
    "k": "\u027e",
    "l": "\u02a4",
    "m": "\u0109",
    "n": "\u0104",
    "o": "\u02c0",
    "p": "\u0188",
    "q": "\u0259",
    "r": "\u0219",
    "s": "\u00bb",
    "t": "\u02ba",
    "u": "\u03d8",
    "v": "\u0339",
    "w": "\u010b",
    "x": "\u0175",
    "y": "\u037e",
    "z": "\u0316",
    "A": "\u011f",
    "B": "u",
    "C": "\u0384",
    "D": "\u03b0",
    "E": "\u0341",
    "F": "l",
    "G": "\u01d2",
    "H": "\u02c0",
    "I": "h",
    "J": "Q",
    "K": "\u036c",
    "L": "\u01d4",
    "M": "\u010e",
    "N": "\u021a",
    "O": "\u02b1",
    "P": "\u00b8",
    "Q": "\u0092",
    "R": "\u01dd",
    "S": "\u02d5",
    "T": "\u009a",
    "U": "\u025d",
    "V": "\u00bc",
    "W": "\u02ac",
    "X": "\u001b",
    "Y": "\u00c5",
    "Z": "\u03e5",
    "!": "Q",
    "\"": "\u030c",
    "#": "P",
    "$": "/",
    "%": "\u01f7",
    "&": "\u019c",
    "'": "\u01bc",
    "(": "\u0372",
    ")": "\u01fd",
    "*": "\u0134",
    "+": "\u02b7",
    ",": "<",
    "-": "\u02dd",
    ".": "\u017a",
    "/": "\u01ee",
    ":": "?",
    ";": "\u0129",
    "<": "\u0092",
    "=": "\u0080",
    ">": "\u0114",
    "?": "\u0335",
    "@": "\u00e9",
    "[": "\u036e",
    "\\": "s",
    "]": "\u03bf",
    "^": "\u0081",
    "_": "\u037c",
    "`": "\u036c",
    "{": "\u031f",
    "|": "\u014a",
    "}": "\u00fb",
    "~": "\u00b3",
    " ": "\u0248",
    "\t": "\u0016",
    "\n": "\u032c",
    "\r": "\u0290",
    "\u000b": "\u00d6",
    "\f": "\u001a"
}

FLAG = list(open("encrypted_flag.txt").read())

reversedict = dict()
for key in MAPPING:
    val = MAPPING[key]
    reversedict[val] = key
for i in range(len(FLAG)):
    char = FLAG[i]
    FLAG[i] = reversedict[char]

FLAG = "".join(FLAG)

print(FLAG)