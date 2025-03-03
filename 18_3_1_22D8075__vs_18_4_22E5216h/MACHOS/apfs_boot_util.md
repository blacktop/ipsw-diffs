## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x343c
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x144f
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x2c0
+2332.100.75.502.1
+  __TEXT.__text: 0x364c
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x1557
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x2c8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__cfstring: 0x60

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 32
-  Symbols:   99
-  CStrings:  164
+  Functions: 30
+  Symbols:   100
+  CStrings:  173
 
Symbols:
+ _APFSGetExclavePath
CStrings:
+ "%s:%d: failed to get tag %d registration base path: %s (%d)\n"
+ "%s:%d: tag %d is already registered but at unexpected path %s (expected %s\n)"
+ "%s:%d: tag %d is already registered, skipping exclaveOS graft\n"
+ "sha3_256"
+ "sha3_256_4k"
+ "sha3_384"
+ "sha3_384_4k"
+ "sha3_512"
+ "sha3_512_4k"

```
