## appprotectiondiagnose

> `/usr/bin/appprotectiondiagnose`

```diff

-46.3.1.0.0
-  __TEXT.__text: 0x158
-  __TEXT.__auth_stubs: 0xc0
+46.4.2.0.0
+  __TEXT.__text: 0x160
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__cstring: 0x2c
   __TEXT.__objc_methname: 0x64
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x68
+  __DATA_CONST.__auth_got: 0x70
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x28

   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 853E8B30-522C-39B3-B20C-2F45669E1D56
+  UUID: 6BC4048E-3C2A-3D3D-84F1-60B929A4131B
   Functions: 1
-  Symbols:   18
+  Symbols:   19
   CStrings:  7
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x8
Functions:
~ sub_100000720 : 344 -> 352

```
