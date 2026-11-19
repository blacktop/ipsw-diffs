## libUniversalAccess.dylib

> `/usr/lib/libUniversalAccess.dylib`

```diff

-778.1.1.0.0
+780.3.6.0.0
   __TEXT.__text: 0x3fac
   __TEXT.__objc_methlist: 0x8c
   __TEXT.__const: 0x90
Symbols:
+ +[UAIOHIDUtilities isCurrentSessionOnConsole]
+ _objc_msgSend$isCurrentSessionOnConsole
- +[UAIOHIDUtilities _isCurrentSessionOnConsole]
- _objc_msgSend$_isCurrentSessionOnConsole
Functions:
~ +[UAIOHIDUtilities _isCurrentSessionOnConsole] -> +[UAIOHIDUtilities _setIOHIDEventSystemClientValue:forProperty:error:] : 100 -> 192
~ +[UAIOHIDUtilities _setIOHIDEventSystemClientValue:forProperty:error:] -> +[UAIOHIDUtilities _createIOHIDEventSystemClientWithError:] : 192 -> 416
~ +[UAIOHIDUtilities _createIOHIDEventSystemClientWithError:] -> +[UAIOHIDUtilities setNumberValue:forProperty:error:] : 416 -> 348
~ +[UAIOHIDUtilities setNumberValue:forProperty:error:] -> +[UAIOHIDUtilities enableIOHIDEventSystemClientCache] : 348 -> 16
~ +[UAIOHIDUtilities enableIOHIDEventSystemClientCache] -> +[UAIOHIDUtilities disableIOHIDEventSystemClientCache] : 16 -> 56
~ +[UAIOHIDUtilities disableIOHIDEventSystemClientCache] -> +[UAIOHIDUtilities getBoolValueForProperty:error:] : 56 -> 212
~ +[UAIOHIDUtilities getBoolValueForProperty:error:] -> +[UAIOHIDUtilities getNumberValueForProperty:error:] : 212 -> 152
~ +[UAIOHIDUtilities getNumberValueForProperty:error:] -> +[UAIOHIDUtilities isCurrentSessionOnConsole] : 152 -> 100
```
