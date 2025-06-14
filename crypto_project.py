def enigma_light():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]

    e = dict(zip(keys, values))
    d = dict(zip(values, keys))

    msg = input("Enter your secret message: ")
    mode = input("Crypto mode - encode (e) or decode (d): ")

    if mode == 'e':
        new_msg = ''.join([e[letter] for letter in msg])
    elif mode == 'd':
        new_msg = ''.join([d[letter] for letter in msg])
    else:
        return "Invalid mode selected."

    print("Result:", new_msg.capitalize())

enigma_light()
