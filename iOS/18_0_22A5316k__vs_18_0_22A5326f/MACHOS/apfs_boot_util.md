## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

-2311.0.0.0.3
-  __TEXT.__text: 0x2194
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0xeeb
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x58
+2313.0.4.0.7
+  __TEXT.__text: 0x32c8
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__const: 0x40
+  __TEXT.__cstring: 0x13a1
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__cfstring: 0x60
   __DATA.__data: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 19
-  Symbols:   88
-  CStrings:  104
+  Functions: 32
+  Symbols:   98
+  CStrings:  161
 
Symbols:
+ _IOConnectCallStructMethod
+ _IORegistryEntryGetChildIterator
+ _IORegistryEntryGetParentEntry
+ _IOServiceClose
+ _IOServiceOpen
+ ___memmove_chk
+ _free
+ _getgid
+ _getuid
+ _kIOMasterPortDefault
+ _mach_task_self_
+ _strcasecmp
+ _strdup
+ _strncasecmp
+ _strncmp
+ _strnlen
+ _strtok_r
+ _strtoul
+ _strtoull
+ _uuid_generate
+ _uuid_parse
- _APFSVolumeCreate
- _CFDictionaryAddValue
- _CFDictionaryCreateMutable
- _CFDictionarySetValue
- _CFNumberCreate
- _kAPFSVolumeNameKey
- _kAPFSVolumeQuotaSizeKey
- _kAPFSVolumeReserveSizeKey
- _kAPFSVolumeRoleKey
- _kCFTypeDictionaryKeyCallBacks
- _kCFTypeDictionaryValueCallBacks
CStrings:
+ "%!s(MISSING):%!d(MISSING): Skipping overprovisioning checks for recovery boot.\n"
+ "%!s(MISSING):%!d(MISSING): could not open container %!s(MISSING) for volume creation: %!d(MISSING)\n"
+ ","
+ "/dev/"
+ "61706673-7575-6964-0000-766f6c756d00"
+ "61706673-7575-6964-0001-766f6c756d00"
+ "61706673-7575-6964-0002-766f6c756d00"
+ "61706673-7575-6964-0004-766f6c756d00"
+ "61706673-7575-6964-0008-766f6c756d00"
+ "61706673-7575-6964-0010-766f6c756d00"
+ "61706673-7575-6964-0020-766f6c756d00"
+ "61706673-7575-6964-0040-766f6c756d00"
+ "61706673-7575-6964-0080-766f6c756d00"
+ "61706673-7575-6964-00c0-766f6c756d00"
+ "61706673-7575-6964-0100-766f6c756d00"
+ "61706673-7575-6964-0140-766f6c756d00"
+ "61706673-7575-6964-0180-766f6c756d00"
+ "61706673-7575-6964-01c0-766f6c756d00"
+ "61706673-7575-6964-0200-766f6c756d00"
+ "61706673-7575-6964-0240-766f6c756d00"
+ "61706673-7575-6964-0280-766f6c756d00"
+ "61706673-7575-6964-02c0-766f6c756d00"
+ "AppleAPFSContainer"
+ "AppleAPFSContainerScheme"
+ "AppleAPFSMedia"
+ "AppleAPFSSnapshot"
+ "AppleAPFSVolume"
+ "case=insensitive"
+ "case=sensitive"
+ "conformance"
+ "defragment=no"
+ "defragment=yes"
+ "empty_password"
+ "encrypted"
+ "fsindex="
+ "fsquota="
+ "fsreserve="
+ "fssize="
+ "fstree=btree"
+ "gid="
+ "hash="
+ "omap=btree"
+ "omap=ephemeral"
+ "omap=physical"
+ "password="
+ "role="
+ "sealed=yes"
+ "sha256"
+ "sha384"
+ "sha512"
+ "sha512_256"
+ "uid="
+ "untitled"
+ "unwritten"
+ "unwritten=no"
+ "uuid_from_role"
+ "volname="

```
