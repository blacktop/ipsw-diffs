## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-3288.2.1.0.0
-  __TEXT.__text: 0x3898
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__cstring: 0x1843
+3288.40.13.0.0
+  __TEXT.__text: 0x3924
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__cstring: 0x185e
   __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__cfstring: 0x80
-  __DATA_CONST.__auth_got: 0x2f0
+  __TEXT.__unwind_info: 0x100
+  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__data: 0x8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 34
-  Symbols:   105
-  CStrings:  189
+  Functions: 35
+  Symbols:   106
+  CStrings:  191
 
Symbols:
+ _CFEqual
Functions:
~ sub_100003a54 : 112 -> 140
+ sub_100003ae0
CStrings:
+ "IOMatchCategory"
+ "mount_apfs"
```
