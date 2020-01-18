from progress.bar import Bar
from riddle import Riddle
import time

_exposedData = input("Enter Text to Encrypt: ")
_encryptedText = None
_encryptionStatus = "ENCRYPTING"

bar = Bar('Encrypting', max=20)
for i in range(20):
    time.sleep(.25)
    bar.next()
bar.finish()

_riddle = Riddle(key=27)
_encryptedText = _riddle.encrypt(obj=_exposedData)

print("\nEncrypted Data:\n\n",_encryptedText,"\n")
input('Press ENTER to Continue')