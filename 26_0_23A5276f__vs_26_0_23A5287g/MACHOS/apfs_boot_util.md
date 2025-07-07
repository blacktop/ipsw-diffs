## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

-2632.0.36.0.1
-  __TEXT.__text: 0x3688
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__cstring: 0x157c
+2632.0.54.0.2
+  __TEXT.__text: 0x3a3c
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__cstring: 0x175f
   __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x2c8
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__cfstring: 0x60

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: 865E7A24-CEF3-30D9-A1A8-496AF41926E3
-  Functions: 30
-  Symbols:   100
-  CStrings:  177
+  UUID: BCEAA0CD-F8F0-360C-BC36-AF702A13E646
+  Functions: 33
+  Symbols:   102
+  CStrings:  188
 
Symbols:
+ _mkdir
+ _rmdir
CStrings:
+ "%s:%d: Cannot open directory on %s: %s\n"
+ "%s:%d: Cannot set protection class on %s: %s\n"
+ "%s:%d: Register tag %d on path %s\n"
+ "%s:%d: Skipping the registration of the exclaves writable storage\n"
+ "%s:%d: failed to create path %s (%s)\n"
+ "%s:%d: failed to register the exclaves writable storage path %s for tag %d (%s)\n"
+ "%s:%d: failed to stat path %s (%s)\n"
+ "%s:%d: successfully registered tag %d at %s\n"
+ "/private/var/.exclave/"
+ "Register exclave RW main tag"
+ "create_and_register_exclave_path_if_needed"

```
