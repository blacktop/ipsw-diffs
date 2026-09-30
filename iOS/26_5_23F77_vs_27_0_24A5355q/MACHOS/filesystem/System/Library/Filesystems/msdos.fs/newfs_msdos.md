## newfs_msdos

> `/System/Library/Filesystems/msdos.fs/newfs_msdos`

```diff

-788.100.31.0.0
-  __TEXT.__text: 0x353c sha256:f14d174ed259f6e0253d12adcec0722f026d5c92e0bc91fbe818d6a9a4f2ddc6
-  __TEXT.__auth_stubs: 0x2f0 sha256:a1350bbd9c49fa2c901b2ab7868dc06ac09241595d94b35dbe8e555aa074d2bd
+844.0.0.0.0
+  __TEXT.__text: 0x302c sha256:b4b7d4db38dc221979646fe7da3cbdbc28a569524063eebb7061e6d72f2f4147
+  __TEXT.__auth_stubs: 0x330 sha256:c60b36b9b57961b55723ac4e2e99d87db304a9736d965c1395e70f18c741b223
   __TEXT.__const: 0x10 sha256:4a914b37dac62f78c8880445b8f41367492036e7327251385173dda2e273e212
-  __TEXT.__cstring: 0xf7e sha256:9e568ce963a76b71db6fab02f62fa23fb96b33921642992047547629ce279a0e
-  __TEXT.__unwind_info: 0xb8 sha256:e8712392beab656a6303eabf16fe650ac1739d315d858e41b66ef0f826a6e24c
-  __DATA_CONST.__auth_got: 0x178 sha256:21cb9ec0cab6dbbd0dd690a1be06d604b8444a21a62640231797633979f093d9
-  __DATA_CONST.__got: 0x30 sha256:76a5e7f6ac222eeef11df722c089e525fc00e7f96bf0f62986c0c71246048c81
-  __DATA_CONST.__const: 0x30 sha256:e0d4cb7d448034bf6a1e62f6b13de0d5bb980fbc73486a42337f0835d0c0c14f
-  __DATA_CONST.__cfstring: 0xa0 sha256:3a4b55da0d27ea8cfbec35e1e154408748acc16f837b998fcf42e774f8680174
-  __DATA.__data: 0x490 sha256:a7ab1f7c872ea7dad083987a930643a8abed37ac9fda88cecd5b05b19127f99c
+  __TEXT.__cstring: 0x10ce sha256:e32d9c469eec240f66ae18059f4c468d03bee3185490334557b04cf58b9d1ed1
+  __TEXT.__unwind_info: 0xb8 sha256:ed8e54c79a200199e589a88e6773a9d93a11c1fd31dd987e0cbd7efe69f52f93
+  __DATA_CONST.__cfstring: 0xa0 sha256:fd54e9b5624404c261c47566ebb4d63f8fdbf65f0766a1b1ac506bc5ee426934
+  __DATA_CONST.__auth_got: 0x198 sha256:f1b0a2b6da4733fe63fecb0e84baf3428296e136873dde76e8f84e945b7a58c1
+  __DATA_CONST.__got: 0x30 sha256:dde3c53e2b751e23b8adda31d3aeaf482ec33fca35a07c77d614dbec3265906e
+  __DATA.__data: 0xcd0 sha256:275c48931411be5ef5ae8ef9b841dc0fd40ab97334c0bbe1ecf939240ecfd7c6
   __DATA.__common: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
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
