## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

-2236.102.1.0.0
-  __TEXT.__text: 0x16f8
+2236.122.2.0.0
+  __TEXT.__text: 0x17a4
   __TEXT.__auth_stubs: 0x320
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0xa1e
+  __TEXT.__cstring: 0xac3
   __TEXT.__unwind_info: 0x98
   __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x20

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: F3FD68C6-E2D3-3762-8C3F-0C756B7571BF
+  UUID: D5A01CD3-AAAD-3BB9-81BB-36C8983B198C
   Functions: 18
   Symbols:   57
-  CStrings:  71
+  CStrings:  75
 
CStrings:
+ "%s:%d: failed to look up hw.osenvironment: %s(%d)\n"
+ "%s:%d: os environment is darwinos-ramdisk, skipping ExclaveOS grafting\n"
+ "boot_is_darwinos_ramdisk"
+ "hw.osenvironment"

```
