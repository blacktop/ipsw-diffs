## com.apple.Home.appremoval

> `/System/Library/AppRemovalServices/com.apple.Home.appremoval.xpc/com.apple.Home.appremoval`

```diff

-1136.4.14.0.0
-  __TEXT.__text: 0x6dc
-  __TEXT.__auth_stubs: 0x170
+1166.5.2.1.3
+  __TEXT.__text: 0x71c
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x17c
   __TEXT.__objc_classname: 0x61

   __TEXT.__cstring: 0x8e
   __TEXT.__oslogstring: 0xb1
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xc0
+  __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x80

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1103BE3B-8253-3523-A11C-81688B297F3A
+  UUID: 5B8A6B75-ED02-39C5-A4F4-EF22081F62F1
   Functions: 8
-  Symbols:   45
+  Symbols:   43
   CStrings:  86
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ sub_100000b88 : 112 -> 116
~ _main : 92 -> 96
~ _os_log_appremoval : 68 -> 84
~ sub_100000ce0 -> sub_100000cf8 : 640 -> 644
~ sub_100000f60 -> sub_100000f7c : 564 -> 584
~ sub_100001194 -> sub_1000011c4 : 188 -> 204

```
