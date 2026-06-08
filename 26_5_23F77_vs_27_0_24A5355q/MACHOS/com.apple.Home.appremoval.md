## com.apple.Home.appremoval

> `/System/Library/AppRemovalServices/com.apple.Home.appremoval.xpc/com.apple.Home.appremoval`

```diff

-1166.6.7.1.1
-  __TEXT.__text: 0x71c
-  __TEXT.__auth_stubs: 0x150
+1216.4.0.1.11
+  __TEXT.__text: 0x6a0
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x17c
   __TEXT.__objc_classname: 0x61

   __TEXT.__cstring: 0x8e
   __TEXT.__oslogstring: 0xb1
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_const: 0x308
   __DATA.__objc_selrefs: 0x160
   __DATA.__objc_data: 0xa0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 338F0FDC-18A1-3BAF-8AB5-6364BCDF7637
+  UUID: 38C0D66F-3A98-369E-A987-E21133361AD9
   Functions: 8
-  Symbols:   43
+  Symbols:   45
   CStrings:  86
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
Functions:
~ sub_100000b88 : 116 -> 112
~ _main : 96 -> 92
~ _os_log_appremoval : 84 -> 68
~ sub_100000cf8 -> sub_100000ce0 : 644 -> 576
~ sub_100000f7c -> sub_100000f20 : 584 -> 568
~ sub_1000011c4 -> sub_100001158 : 204 -> 188

```
