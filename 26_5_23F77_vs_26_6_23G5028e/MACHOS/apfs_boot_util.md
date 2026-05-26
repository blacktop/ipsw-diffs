## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x3aac
+2811.160.3.0.0
+  __TEXT.__text: 0x38e8
   __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__cstring: 0x183f
+  __TEXT.__cstring: 0x1843
   __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: B8B6ABE2-1A60-3804-BC31-A4E37F16F9DE
-  Functions: 37
+  UUID: BE15E225-6366-3EFC-98B8-B79E644687AE
+  Functions: 34
   Symbols:   105
   CStrings:  193
 
CStrings:
+ "%s:%d: cannot create directory '%s' - %s(%d)\n"
- "%s:%d: cannot create directory '%s' - %s\n"

```
