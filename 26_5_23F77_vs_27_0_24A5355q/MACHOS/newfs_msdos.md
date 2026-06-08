## newfs_msdos

> `/System/Library/Filesystems/msdos.fs/newfs_msdos`

```diff

-788.100.31.0.0
-  __TEXT.__text: 0x353c
-  __TEXT.__auth_stubs: 0x2f0
+844.0.0.0.0
+  __TEXT.__text: 0x302c
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0xf7e
+  __TEXT.__cstring: 0x10ce
   __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x30
   __DATA_CONST.__cfstring: 0xa0
-  __DATA.__data: 0x490
+  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x30
+  __DATA.__data: 0xcd0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: AF87C173-3201-3946-8DD8-229741AE2CA9
+  UUID: 8D8A19CD-44F3-354F-ADC9-8D0C4680F3D8
   Functions: 27
-  Symbols:   56
-  CStrings:  162
+  Symbols:   60
+  CStrings:  169
 
Symbols:
+ _fprintf
+ _free
+ _malloc_type_calloc
+ _printf
+ _strncpy
- _vprintf
CStrings:
+ " bkbs=%u"
+ " bspf=%u rdcl=%"
+ " infs=%u"
+ "%s: %s\n"
+ "%s: %s: Block count wasn't initialized, setting to default value (%llu)\n"
+ "%s: %s: Block size wasn't initialized, setting to default value (%u)\n"
+ "%s: %s: Cannot get block count\n"
+ "%s: %s: Cannot get block size\n"
+ "%s: %s: Cannot get partition offset\n"
+ "%s: %s: Drive is too large, the number of blocks is larger than any FAT FS can support\n"
+ "%s: %s: Partition offset wasn't initialized, setting to default value (%llu)\n"
+ "%s: bad %s\n"
+ "%s: can't read sector %u\n"
+ "%s: can't write boot sector\n"
+ "%s: can't write sector %u\n"
+ "%s: inappropriate file type or format\n"
+ "%s: newfs_exfat should be used for SDXC media\n"
+ "%s: unknown standard format\n"
+ "%s: write: %s\n"
+ "%u clusters too few clusters for FAT%u, need %u\n"
+ "-%c is not a legal FAT%s option\n"
+ "Backup sector would overwrite info sector\n"
+ "Bad OEM string (%s)\n"
+ "Can't allocate a wipe FS context object\n"
+ "Encountered errors trying to wipe resource\n"
+ "FAT%d is impossible for disk size of %lluKiB\n"
+ "FAT%d is impossible with %u sectors\n"
+ "Failed to allocate message buffer"
+ "Failed to locate message %d\n"
+ "Failed to retrieve localized message"
+ "Format device: Checking parameters\n"
+ "Format device: Checking parameters: Failed\n"
+ "Format device: Wiping file system\n"
+ "Format device: Wiping file system: Failed\n"
+ "Format device: Writing file system\n"
+ "Format device: Writing file system: Failed\n"
+ "Given volume name (%s) is invalid for this file system\n"
+ "Invalid FAT type (%s), must be 12/16 or 32\n"
+ "Invalid FAT type: %d\n"
+ "Meta data exceeds file system size\n"
+ "No room for backup sector\n"
+ "No room for info sector\n"
+ "Option %s requires a value\n"
+ "Too few reserved sectors\n"
+ "Too many sectors/FAT for FAT12/16\n"
+ "block size (%u) is not a power of 2\n"
+ "block size (%u) is too large; maximum is %u\n"
+ "block size (%u) is too small; minimum is %u\n"
+ "bytes/sector (%u) is not a power of 2\n"
+ "bytes/sector (%u) is too large; maximum is %u\n"
+ "bytes/sector (%u) is too small; minimum is %u\n"
+ "illegal media descriptor (%#x)\n"
+ "number of FATs (%u) is too large; maximum is %u\n"
+ "physical bytes/sector (%u) is less than logical bytes/sector (%u)\n"
+ "physical bytes/sector (%u) is not a power of 2\n"
+ "sectors/cluster (%u) is not a power of 2\n"
- "\n"
- " bkbs="
- " bspf=%u rdcl=%u"
- " infs="
- "%s: %s"
- "%s: %s: Block count wasn't initialized, setting to default value (%llu)"
- "%s: %s: Block size wasn't initialized, setting to default value (%u)"
- "%s: %s: Cannot get block count"
- "%s: %s: Cannot get block size"
- "%s: %s: Cannot get partition offset"
- "%s: %s: Drive is too large, the number of blocks is larger than any FAT FS can support"
- "%s: %s: Partition offset wasn't initialized, setting to default value (%llu)"
- "%s: bad %s"
- "%s: can't read sector %u"
- "%s: can't write boot sector"
- "%s: can't write sector %u"
- "%s: inappropriate file type or format"
- "%s: newfs_exfat should be used for SDXC media"
- "%s: unknown standard format"
- "%s: write: %s"
- "%u clusters too few clusters for FAT%u, need %u"
- "-%c is not a legal FAT%s option"
- "Encountered errors trying to wipe resource"
- "FAT%d is impossible for disk size of %lluKiB"
- "FAT%d is impossible with %u sectors"
- "Format device: Checking parameters"
- "Format device: Checking parameters: Failed"
- "Format device: Wiping file system"
- "Format device: Wiping file system: Failed"
- "Format device: Writing file system"
- "Format device: Writing file system: Failed"
- "Invalid FAT type: %d"
- "backup sector would overwrite info sector"
- "block size (%u) is not a power of 2"
- "block size (%u) is too large; maximum is %u"
- "block size (%u) is too small; minimum is %u"
- "bytes/sector (%u) is not a power of 2"
- "bytes/sector (%u) is too large; maximum is %u"
- "bytes/sector (%u) is too small; minimum is %u"
- "illegal media descriptor (%#x)"
- "meta data exceeds file system size"
- "no room for backup sector"
- "no room for info sector"
- "number of FATs (%u) is too large; maximum is %u"
- "physical bytes/sector (%u) is less than logical bytes/sector (%u)"
- "physical bytes/sector (%u) is not a power of 2"
- "sectors/cluster (%u) is not a power of 2"
- "too few reserved sectors"
- "too many sectors/FAT for FAT12/16"

```
