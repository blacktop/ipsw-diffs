## newfs_exfat

> `/System/Library/Filesystems/exfat.fs/newfs_exfat`

```diff

-488.120.2.0.0
-  __TEXT.__text: 0x3568
+522.0.0.0.0
+  __TEXT.__text: 0x3540
   __TEXT.__auth_stubs: 0x380
   __TEXT.__const: 0x4a78
-  __TEXT.__cstring: 0xb99
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__cstring: 0xed0
+  __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__cfstring: 0x60
-  __DATA.__data: 0x1883
+  __DATA.__data: 0x1ee3
   __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 2AEF74CC-49F5-3150-BF33-2D2DA1F607A9
+  UUID: DD743D37-111E-3056-9886-D23EF9E0D60C
   Functions: 56
   Symbols:   65
-  CStrings:  91
+  CStrings:  107
 
Functions:
~ sub_100000718 : 1340 -> 1344
~ sub_100000d3c -> sub_100000d40 : 876 -> 872
~ sub_100001480 : 3012 -> 2840
~ sub_100002044 -> sub_100001f98 : 1180 -> 1268
~ sub_1000024e0 -> sub_10000248c : 504 -> 496
~ sub_100002d60 -> sub_100002d04 : 364 -> 348
~ sub_100002ecc -> sub_100002e60 : 424 -> 408
~ sub_100003074 -> sub_100002ff8 : 284 -> 268
~ sub_10000327c -> sub_1000031f0 : 132 -> 136
~ sub_100003300 -> sub_100003278 : 128 -> 132
~ sub_100003ba0 -> sub_100003b1c : 72 -> 164
CStrings:
+ "%s: Can't allocate a wipe FS context object\n"
+ "%s: Given device is not a block device\n"
+ "%s: Sector size was not initialized, setting to default value (%d)\n"
+ "%s: Total sectors was not initialized, setting to default value (%d)\n"
+ "%s: Wipe resource error: %d\n"
+ "%s: device file descriptor is -1, path (%s)\n"
+ "%s: fstat failed, path (%s)\n"
+ "Could not convert name (%s) to precomposed UTF-16 little endian; may be too long\n"
+ "Could not create CFMutableString for volume name\n"
+ "Encountered errors trying to wipe resource\n"
+ "Encountered errors while writing backup boot sector\n"
+ "Encountered errors while writing main boot sector\n"
+ "Failed to allocate temporary buffer\n"
+ "Failed to locate message %d\n"
+ "Failed to start phase, error %s\n"
+ "Format: Check reformat\n"
+ "Format: Check reformat: Failed\n"
+ "Format: Flush data structures\n"
+ "Format: Flush data structures: Failed\n"
+ "Format: Prepare boot region\n"
+ "Format: Prepare boot region: Failed\n"
+ "Format: Preparing\n"
+ "Format: Preparing: Failed\n"
+ "Format: Wipe\n"
+ "Format: Wipe: Failed\n"
+ "Format: Write FAT tables\n"
+ "Format: Write bitmaps\n"
+ "Given volume name (%s) is invalid for this file system\n"
+ "Inconsistent sectors per cluster (%u) and bytes per cluster (%u)\n"
+ "Invalid argument for option -%c: %s\n"
+ "Invalid bytes per cluster (%u); must be a power of two from 512 to 33554432\n"
+ "Invalid bytes per sector (%u); must be a power of two from 512 to 4096\n"
+ "Invalid number of FATs (%u); must be 1 or 2\n"
+ "Invalid number of FATs, or FAT or cluster offset; skipping reformat"
+ "Invalid sectors per cluster (%u); must be a power of two from 1 to 65536\n"
+ "Numeric overflow for option -%c: %s\n"
+ "Partition offset was not initialized , setting to default value (%d)\n"
+ "Sector size (%u) is too large\n"
+ "Sectors per FAT must be non-zero\n"
+ "Sectors per cluster (%u) too large; max is %u\n"
+ "format"
+ "wipefs_alloc(): fd(%d) %s\n"
+ "wipefs_except_blocks(): fd(%d) %s\n"
+ "wipefs_wipe(): fd(%d) %s\n"
- "%s: Sector size was not initialized, setting to default value (%d)"
- "%s: Total sectors was not initialized, setting to default value (%d)"
- "Encountered errors trying to wipe resource"
- "Failed to allocate temporary buffer"
- "Format: Check reformat"
- "Format: Check reformat: Failed"
- "Format: Flush data structures"
- "Format: Flush data structures: Failed"
- "Format: Prepare boot region"
- "Format: Prepare boot region: Failed"
- "Format: Preparing"
- "Format: Preparing: Failed"
- "Format: Wipe"
- "Format: Wipe: Failed"
- "Format: Write FAT tables"
- "Format: Write bitmaps"
- "Inconsistent sectors per cluster (%u) and bytes per cluster (%u)"
- "Invalid argument for option -%c: %s"
- "Invalid number of FATs, or FAT or cluster offset; skipping reformat\n"
- "Numeric overflow for option -%c: %s"
- "Partition offset was not initialized , setting to default value (%d)"
- "Sector size (%u) is too large"
- "Sectors per cluster (%u) too large; max is %u"
- "wipefs_alloc(): fd(%d) %s"
- "wipefs_except_blocks(): fd(%d) %s"
- "wipefs_wipe(): fd(%d) %s"
- "writing backup boot sector"
- "writing main boot sector"

```
