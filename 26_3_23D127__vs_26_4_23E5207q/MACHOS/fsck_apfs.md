## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2632.80.1.0.1
-  __TEXT.__text: 0x53e20
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__cstring: 0x19a34
-  __TEXT.__const: 0x85f8
-  __TEXT.__unwind_info: 0xb58
-  __DATA_CONST.__auth_got: 0x5d0
+2811.100.177.0.1
+  __TEXT.__text: 0x53d5c
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__cstring: 0x19e40
+  __TEXT.__const: 0x8710
+  __TEXT.__unwind_info: 0xb50
+  __DATA_CONST.__auth_got: 0x5e8
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x68
   __DATA_CONST.__const: 0x610
   __DATA_CONST.__cfstring: 0x200
-  __DATA.__data: 0xef0
+  __DATA.__data: 0xee8
   __DATA.__bss: 0x1e1f1
   __DATA.__common: 0xac9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: FD979ED7-8315-321B-A456-5528A198BEC4
-  Functions: 946
-  Symbols:   203
-  CStrings:  1963
+  UUID: EB8D0504-7870-3A95-AC8B-1DE63EDA40E3
+  Functions: 962
+  Symbols:   206
+  CStrings:  1975
 
Symbols:
+ __NSGetExecutablePath
+ ___strlcat_chk
+ _getprogname
+ _raise
- __exit
CStrings:
+ "%s (id %llu): xf %u/%u: %s: SAF dir-stats key found on non origin ino (%llu)\n"
+ "%s (id %llu): xf %u/%u: %s: found purgeable flags xfield even though the file is marked as purgeable\n"
+ "%s (id %llu): xf %u/%u: %s: found purgeable flags xfield on directory without INODE_MARK_CHILD_PURGEABLE flag\n"
+ "%s (id %llu): xf %u/%u: %s: found purgeable flags xfield on file without INODE_WANTS_TO_BE_PURGEABLE flag\n"
+ "%s (id %llu): xf %u/%u: %s: invalid SAF dir_stats_key (%llu)\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_reset: %d; of: 0x%x; nf: 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh! - PBKDF2 calibration maxxed out%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh, Unexpected short PDK len%s\n"
+ "/..namedfork/rsrc"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "2811.100.177.0.1"
+ "INO_EXT_TYPE_SAF_DIR_STATS_KEY"
+ "compressed clonegroup record (group_id %llu, private_id %llu, file_id %llu): has the full clone flag turned on\n"
+ "could not get the current executable path of %s\n"
+ "could not open %s to prevent reclaims: %s\n"
+ "device_is_mounted(%s) failed with error: %s\n"
+ "fv_create_pdk"
+ "inode (id %llu): finder info internal flag is missing\n"
+ "inode (id %llu): finder info internal flag is unexpectedly set\n"
+ "inode (id %llu): security xattr internal flag is unexpectedly set\n"
- "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
- "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_change: %d; cf: 0x%x; of: 0x%x; nf: 0x%x%s\n"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "2632.80.1.0.1"
- "dev_is_mounted(%s) failed with error: %s\n"
- "fd_dev_hint_flush"
- "skipping purgeable cross checks\n"

```
