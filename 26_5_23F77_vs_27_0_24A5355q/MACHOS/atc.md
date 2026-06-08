## atc

> `/usr/libexec/atc`

```diff

-4025.600.6.0.0
-  __TEXT.__text: 0x46c
-  __TEXT.__auth_stubs: 0x180
+4026.100.55.0.0
+  __TEXT.__text: 0x3c8
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x160
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x34
   __TEXT.__oslogstring: 0xba
   __TEXT.__objc_methname: 0x8f
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0xc8
-  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x30
   __DATA.__objc_selrefs: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 80225DB8-D6A6-3BF3-BE4E-D3DC96761716
+  UUID: 41D37489-BF03-30B8-AD4A-38057EAC7050
   Functions: 3
-  Symbols:   35
+  Symbols:   33
   CStrings:  22
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x22
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
Functions:
~ sub_100000c40 : 636 -> 580
~ sub_100000ebc -> sub_100000e84 : 276 -> 168

```
