## appprotectiondiagnose

> `/usr/bin/appprotectiondiagnose`

```diff

-46.4.3.0.0
-  __TEXT.__text: 0x160
-  __TEXT.__auth_stubs: 0xd0
+54.0.0.0.0
+  __TEXT.__text: 0x158
+  __TEXT.__auth_stubs: 0xc0
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__cstring: 0x2c
   __TEXT.__objc_methname: 0x64
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x70
-  __DATA_CONST.__got: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x68
+  __DATA_CONST.__got: 0x18
   __DATA.__objc_selrefs: 0x28
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B780B740-C8D9-3E39-B40C-68FB024DF162
+  UUID: 1BC87F9D-6A36-3DC4-9171-CEA4A7EC07AF
   Functions: 1
-  Symbols:   19
+  Symbols:   18
   CStrings:  7
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x23
Functions:
~ sub_100000720 : 352 -> 344

```
