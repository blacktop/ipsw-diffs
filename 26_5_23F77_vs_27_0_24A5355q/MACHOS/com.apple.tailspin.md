## com.apple.tailspin

> `/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin`

```diff

-250.2.0.0.0
-  __TEXT.__text: 0x65c
-  __TEXT.__auth_stubs: 0x240
+262.0.0.0.0
+  __TEXT.__text: 0x620
+  __TEXT.__auth_stubs: 0x230
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x8c
   __TEXT.__oslogstring: 0xfe
   __TEXT.__objc_methname: 0x5a
-  __TEXT.__unwind_info: 0x70
-  __DATA.__auth_got: 0x128
-  __DATA.__got: 0x18
+  __TEXT.__unwind_info: 0x78
   __DATA.__const: 0x48
   __DATA.__cfstring: 0x40
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x28
   __DATA.__crash_info: 0x148
+  __DATA.__auth_got: 0x120
+  __DATA.__got: 0x18
   __DATA.__bss: 0x410
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 72351F66-D5EE-3F1E-B286-19A2AAF152D0
+  UUID: 58F1B4D7-F658-3A1B-B230-A20EF3D42919
   Functions: 7
-  Symbols:   47
+  Symbols:   46
   CStrings:  22
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x8
- _objc_autoreleaseReturnValue
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ _init_tailspin : 1188 -> 1160
~ sub_d0c -> sub_cf0 : 84 -> 68
~ sub_d60 -> sub_d34 : 112 -> 96

```
