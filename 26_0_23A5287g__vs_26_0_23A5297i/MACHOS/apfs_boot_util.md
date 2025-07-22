## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0x3a3c
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__cstring: 0x175f
+2632.0.68.0.3
+  __TEXT.__text: 0x3b24
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__cstring: 0x187e
   __TEXT.__const: 0x20
   __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__cfstring: 0x60
+  __DATA_CONST.__cfstring: 0x80
   __DATA.__data: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: BCEAA0CD-F8F0-360C-BC36-AF702A13E646
-  Functions: 33
-  Symbols:   102
-  CStrings:  188
+  UUID: 8EBCE48D-718D-31BB-AE6C-442129E788B6
+  Functions: 34
+  Symbols:   105
+  CStrings:  194
 
Symbols:
+ _CFDataGetBytes
+ _CFDataGetLength
+ _IORegistryEntryFromPath
CStrings:
+ "%s:%d: Skipping the registration of the exclaves writable storage because we're not running in regular OS environment\n"
+ "IODeviceTree:/filesystems/fstab"
+ "error: unable to find OS environment entry in device tree plane"
+ "error: unable to find filesystems node in device tree plane"
+ "os_env_type"

```
