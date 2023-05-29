import tkinter as tk
import pyperclip
from simpleSubHackerFunction import hackSimpleSub, decryptWithCipherletterMapping

#freq anal: https://studio.code.org/s/frequency_analysis/lessons/1/levels/1

#sub have too many possible keys so we cant use simple brute force
#get word pattern ex: HGHHU -> PUPPY
#cipher mapping using table H G H H U
#                           P U P P Y
#                           M O M M Y
#                              ...

#return list {'A': [], 'B', ['U','Y'],....}

"""
Overview of the Hacking Process
Hacking the simple substitution cipher is pretty easy using word patterns. We can summarize the major steps of the
   1. Find the word pattern for each cipherword in the ciphertext.
   2. Find the English word candidates that each cipherword could decrypt to.
   3. Create a dictionary showing potential decryption letters for each cipherletter to act as the cipherletter mappin
    4. Combine the cipherletter mappings into a single mapping, which we'll call an intersected mapping.
    5. Remove any solved cipherletters from the combined mapping.
    6. Decrypt the ciphertext with the solved cipherletters.

"""

"""YIF QFMZRW QFYV ECFMD ZPCVMRZW NMD ZVEJB TXCDD UMJN DIFEFMDZ CD MQ ZKCEYFCJMYR NCW JCSZR EXCHZ UNMXZ NZ UCDRJ XYYSMRT M EYIFZW DYVZ VYFZ UMRZ CRW NZ DZJJXZW GCHS MR NMD HNCMF QCHZ JMXJZW IE JYUCFWD JNZ DIR """
"""Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm"""
def hack_simple_substitution():
    message = input_text.get("1.0", tk.END)
    message = message.lower()

    print('Hacking...')
    letterMapping = hackSimpleSub(message)

    # Display the results to the user
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, hackedMessage)
    pyperclip.copy(hackedMessage)


# Create the main window
window = tk.Tk()
window.title("Simple Substitution Cipher Hacker")
window.geometry("600x400")

# Create input label and text box
input_label = tk.Label(window, text="Enter Ciphertext:")
input_label.pack()
input_text = tk.Text(window, height=5)
input_text.pack()

# Create hack button
hack_button = tk.Button(window, text="Hack", command=hack_simple_substitution)
hack_button.pack()

# Create output label and text box
output_label = tk.Label(window, text="Hacked Message:")
output_label.pack()
output_text = tk.Text(window, height=5)
output_text.pack()

# Start the main GUI loop
window.mainloop()
