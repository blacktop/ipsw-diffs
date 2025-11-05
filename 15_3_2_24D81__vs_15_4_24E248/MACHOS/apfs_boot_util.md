## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_boot_util`

```diff

-2317.81.2.0.0
-  __TEXT.__text: 0x6320
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__cstring: 0x28a7
-  __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x400
-  __DATA_CONST.__got: 0x68
+2332.101.1.0.0
+  __TEXT.__text: 0x6f7c
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x2d32
+  __TEXT.__unwind_info: 0x148
+  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__cfstring: 0x320
   __DATA.__data: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: 7BB7F72A-A1DC-3908-8C24-22CE282B6CE5
-  Functions: 67
-  Symbols:   145
-  CStrings:  322
+  UUID: A1D02E2C-EF6E-37D9-A951-1A7C0B413588
+  Functions: 74
+  Symbols:   152
+  CStrings:  368
 
Symbols:
+ _APFSGetExclavePath
+ _CFBooleanGetValue
+ _IORegistryEntryGetParentIterator
+ _kCFBooleanTrue
+ _mkdir
+ _os_parse_boot_arg_from_buffer_string
+ _sysctlbyname_get_data_np
CStrings:
+ "%s/%s/"
+ "%s:%d: Failed to find IOPlatformExpertDevice\n"
+ "%s:%d: Failed to find an service matching %s\n"
+ "%s:%d: Failed to get %s\n"
+ "%s:%d: Failed to get string from %s\n"
+ "%s:%d: Invalid machine UUID %s\n"
+ "%s:%d: Machine UUID is %s\n"
+ "%s:%d: Register tag %d on path %s\n"
+ "%s:%d: Skipping the registration of the exclaves writable storage\n"
+ "%s:%d: failed to create path %s (%s)\n"
+ "%s:%d: failed to get tag %d registration base path: %s (%d)\n"
+ "%s:%d: failed to register the exclaves writable storage path %s for tag %d (%s)\n"
+ "%s:%d: failed to stat path %s (%s)\n"
+ "%s:%d: successfully registered tag %d at %s\n"
+ "%s:%d: tag %d is already registered but at unexpected path %s (expected %s\n)"
+ "%s:%d: tag %d is already registered, skipping exclaveOS graft\n"
+ "-post-upgrade"
+ "/System/Volumes/Data/.exclave/"
+ "/System/Volumes/iSCPreboot/.exclave/"
+ "Device Characteristics"
+ "Get machine UUID"
+ "IOPlatformExpertDevice"
+ "IOPlatformUUID"
+ "Internal"
+ "Physical Interconnect Location"
+ "Register exclave RW main tag"
+ "Register exclave RW tag"
+ "Removable"
+ "Target Disk Mode"
+ "create_and_register_exclave_path_if_needed"
+ "get_machine_uuid"
+ "image-format-read-only"
+ "kern.bootargs"
+ "sha3_256"
+ "sha3_256_4k"
+ "sha3_384"
+ "sha3_384_4k"
+ "sha3_512"
+ "sha3_512_4k"

```
