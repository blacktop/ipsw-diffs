## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_boot_util`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x6a88
+3288.41.1.0.0
+  __TEXT.__text: 0x6bfc
   __TEXT.__auth_stubs: 0x880
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2d3a
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__cfstring: 0x320
+  __TEXT.__cstring: 0x2db6
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
+  CStrings:  347
 
Functions:
~ sub_100004844 : 2112 -> 2344
+ sub_100006b90
CStrings:
+ "%s:%d: os environment is darwinos-ramdisk, skipping ExclaveOS grafting\n"
+ "IOMatchCategory"
+ "boot_is_darwinos_ramdisk"
+ "mount_apfs"
```
