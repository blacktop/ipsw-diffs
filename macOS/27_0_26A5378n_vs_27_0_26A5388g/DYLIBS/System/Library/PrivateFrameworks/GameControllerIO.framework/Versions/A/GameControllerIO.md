## GameControllerIO

> `/System/Library/PrivateFrameworks/GameControllerIO.framework/Versions/A/GameControllerIO`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-14.0.19.0.0
-  __TEXT.__text: 0x5d7c
+14.0.21.0.0
+  __TEXT.__text: 0x5d38
   __TEXT.__objc_methlist: 0xb84
   __TEXT.__const: 0x95
   __TEXT.__gcc_except_tab: 0x64

   __AUTH_CONST.__objc_const: 0x12d8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x110
   __DATA.__data: 0x840
   __DATA.__bss: 0x29
+  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 217
-  Symbols:   687
+  Symbols:   689
   CStrings:  104
 
Symbols:
+ _objc_getProperty
+ _objc_setProperty_atomic
Functions:
~ -[GCGamepadHIDServicePlugin updateHapticMotor:] : 204 -> 172
~ -[GCGamepadHIDServicePlugin enqueueTransient:hapticMotor:] : 184 -> 148
~ -[GCGamepadHIDServicePlugin hapticMotors] : 8 -> 12
~ -[GCGamepadHIDServicePlugin setHapticMotors:] : 12 -> 8
```
