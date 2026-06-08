## apfs_stats

> `/System/Library/Filesystems/apfs.fs/apfs_stats`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x24e0
+3277.0.0.0.1
+  __TEXT.__text: 0x256c
   __TEXT.__auth_stubs: 0x410
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x13e3
+  __TEXT.__cstring: 0x1463
   __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x3e0
   __DATA.__bss: 0x29
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: B02E3737-8029-3807-9D79-6239CDADEA4F
+  UUID: 309166A7-FE67-36B2-BB2E-B8DE58A53C63
   Functions: 23
   Symbols:   78
-  CStrings:  150
+  CStrings:  156
 
Functions:
~ sub_1000007d8 : 572 -> 580
~ sub_100000a14 -> sub_100000a1c : 4720 -> 4852
CStrings:
+ "\t\t\tNumber of purgeable files = %llu\n"
+ "\t\t\tSize of purgeable files = %llu\n"
+ "Number of purgeable files"
+ "Total Size of purgeable files"

```
