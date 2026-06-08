## fsck

> `/sbin/fsck`

```diff

-757.0.0.0.0
-  __TEXT.__text: 0x1890
+766.0.0.0.0
+  __TEXT.__text: 0x1894
   __TEXT.__auth_stubs: 0x320
   __TEXT.__cstring: 0x554
   __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__cfstring: 0x20
   __DATA.__data: 0x4
   __DATA.__common: 0x68
   __DATA.__bss: 0x20

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: E3757D38-775C-326C-8AF6-4D0068B1F4B7
+  UUID: 9BAB1C38-7E2D-32F4-84BA-7DF2C35A43D0
   Functions: 23
   Symbols:   60
   CStrings:  68
Functions:
~ sub_100001dd0 : 316 -> 320

```
