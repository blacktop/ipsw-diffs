## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_boot_util`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x6a88
+3288.40.13.0.0
+  __TEXT.__text: 0x6b14
   __TEXT.__auth_stubs: 0x880
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2d3a
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__cfstring: 0x320
+  __TEXT.__cstring: 0x2d55
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__auth_got: 0x440
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 69
+  Functions: 70
   Symbols:   154
-  CStrings:  343
+  CStrings:  345
 
Functions:
~ sub_100006aa8 : 112 -> 140
+ sub_100006b34
CStrings:
+ "IOMatchCategory"
+ "mount_apfs"
```
