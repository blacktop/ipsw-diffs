## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

```diff

-704.0.1.0.0
-  __TEXT.__text: 0x301b0
+704.0.3.0.0
+  __TEXT.__text: 0x301f0
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__const: 0x112c
-  __TEXT.__cstring: 0x6cbc
+  __TEXT.__cstring: 0x6d18
   __TEXT.__unwind_info: 0x508
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0x50

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 38AABFFD-9AEF-32C3-990E-B738A3485DEF
+  UUID: F31B49E5-ACC0-321B-B319-CA90ED0629C4
   Functions: 471
   Symbols:   138
-  CStrings:  781
+  CStrings:  783
 
Functions:
~ sub_100021ecc : 1012 -> 1020
~ sub_1000222c0 -> sub_1000222c8 : 664 -> 660
~ sub_10002a578 -> sub_10002a57c : 444 -> 448
~ sub_10002d49c -> sub_10002d4a4 : 3476 -> 3532
CStrings:
+ "Physical block size cannot be greater than 16 KiB\n"
+ "Physical block size is not a power of 2\n"

```
