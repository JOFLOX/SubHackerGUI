# Simple Substitution Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

from simpleSubHackerFunction import hackSimpleSub, decryptWithCipherletterMapping


def simpleSubHacking():
    message = '''YIF QFMZRW QFYV ECFMD ZPCVMRZW NMD ZVEJB TXCDD UMJN DIFEFMDZ CD MQ ZKCEYFCJMYR NCW JCSZR EXCHZ UNMXZ NZ UCDRJ XYYSMRT M EYIFZW DYVZ VYFZ UMRZ CRW NZ DZJJXZW GCHS MR NMD HNCMF QCHZ JMXJZW IE JYUCFWD JNZ DIR '''
            # '''Our friend from Paris examined his empty glass with surprise,as if evaporation had taken place while he wasnt looking.I poured some more wine and he settled back in his chair,face tilted up towards the sun
    message.lower()
    print('Hacking...')
    letterMapping = hackSimpleSub(message)

    # Display the results to the user:
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    print(hackedMessage)


if __name__ == '__main__':
    simpleSubHacking()
