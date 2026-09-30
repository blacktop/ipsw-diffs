## pboard

> `/usr/libexec/pboard`

```diff

-3302.1.400.0.0
-  __TEXT.__text: 0x288
-  __TEXT.__auth_stubs: 0xe0
+3423.0.0.0.0
+  __TEXT.__text: 0x284
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x6f
+  __TEXT.__cstring: 0x56
   __TEXT.__oslogstring: 0x6c
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x70
+  __DATA_CONST.__auth_got: 0x68
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 3AAF0E6E-3F3C-318A-963D-B1BDD398DCC0
+  UUID: C82B1466-CB98-3366-B412-7231738F134F
   Functions: 4
-  Symbols:   18
+  Symbols:   17
   CStrings:  9
 
Symbols:
+ _setenv
- _CFRunLoopRun
- __os_feature_enabled_impl
Functions:
~ sub_100003b10 -> sub_100000698 : 324 -> 320
~ sub_100003c54 -> sub_1000007d8 : 132 -> 124
~ sub_100003d1c -> sub_100000898 : 124 -> 132
CStrings:
+ "1"
+ "IIOEnableOOP"
- "CFPasteboardVerification"
- "CoreFoundation"

```
