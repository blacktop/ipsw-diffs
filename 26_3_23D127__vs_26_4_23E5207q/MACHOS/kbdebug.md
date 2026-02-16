## kbdebug

> `/usr/bin/kbdebug`

```diff

-9126.3.5.0.0
-  __TEXT.__text: 0x9e0
-  __TEXT.__auth_stubs: 0x210
+9126.4.20.0.0
+  __TEXT.__text: 0xa2c
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x200
   __TEXT.__objc_methlist: 0x17c
   __TEXT.__const: 0x8

   __TEXT.__objc_classname: 0x31
   __TEXT.__objc_methtype: 0x1bb
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__cfstring: 0x2c0

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6927C2AB-0C68-3151-9021-1A4D4B8AD1AF
+  UUID: B3B9D00B-1376-3A5D-B4C0-332251C25218
   Functions: 23
-  Symbols:   47
+  Symbols:   46
   CStrings:  102
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x22
Functions:
~ sub_100000c68 : 392 -> 404
~ sub_100000f20 -> sub_100000f2c : 192 -> 196
~ sub_1000012ac -> sub_1000012bc : 924 -> 984

```
