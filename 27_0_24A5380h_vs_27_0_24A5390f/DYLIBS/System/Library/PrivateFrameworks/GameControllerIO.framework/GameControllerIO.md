## GameControllerIO

> `/System/Library/PrivateFrameworks/GameControllerIO.framework/GameControllerIO`

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
-  __TEXT.__text: 0x5464
+14.0.21.0.0
+  __TEXT.__text: 0x5428
   __TEXT.__objc_methlist: 0xb54
   __TEXT.__const: 0x8d
   __TEXT.__gcc_except_tab: 0x64

   __AUTH_CONST.__objc_const: 0x1218
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x840
   __DATA.__bss: 0x29
+  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 201
-  Symbols:   664
+  Symbols:   666
   CStrings:  96
 
Symbols:
+ _objc_getProperty
+ _objc_setProperty_atomic
Functions:
~ -[GCGamepadHIDServicePlugin updateHapticMotor:] : 184 -> 156
~ -[GCGamepadHIDServicePlugin enqueueTransient:hapticMotor:] : 168 -> 136
~ -[GCGamepadHIDServicePlugin hapticMotors] : 8 -> 12
~ -[GCGamepadHIDServicePlugin setHapticMotors:] : 12 -> 8
```
