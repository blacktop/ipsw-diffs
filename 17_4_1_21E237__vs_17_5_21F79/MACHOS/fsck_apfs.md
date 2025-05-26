## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2236.102.1.0.0
-  __TEXT.__text: 0x4b3a8
+2236.122.2.0.0
+  __TEXT.__text: 0x4b888
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__cstring: 0x17bcc
-  __TEXT.__const: 0x812c
+  __TEXT.__cstring: 0x17e87
+  __TEXT.__const: 0x813c
   __TEXT.__unwind_info: 0x9e8
   __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x4d8
+  __DATA_CONST.__const: 0x4e0
   __DATA_CONST.__cfstring: 0x200
   __DATA.__data: 0xec4
   __DATA.__bss: 0x1c7a4

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 815
+  Functions: 816
   Symbols:   158
-  CStrings:  1805
+  CStrings:  1816
 
CStrings:
+ "%s (id %llu): xf %u/%u: %s: inode is expected to be an SAF dir-stats origin\n"
+ "2236.122.2"
+ "INO_EXT_TYPE_SPEC_TELEM_FLAGS"
+ "set missing flag? (0x%x) "
+ "speculative download xattr (id %llu): found outside of an SAF dir stats hierarchy\n"
+ "speculative download xattr (id %llu): invalid flags: 0x%x\n"
+ "speculative download xattr (id %llu): pristine time (%llu) is greater than current time (%llu)\n"
+ "speculative download xattr (id %llu): shouldn't be stream based\n"
+ "speculative download xattr (id %llu): size is too small, actual: %u, minimum: %lu\n"
+ "speculative download xattr (id %llu): unknown flags: %x\n"
+ "speculative download xattr (id %llu): unknown purge reason: %u\n"
+ "speculative download xattr (id %llu): unknown version: %u\n"
- "2236.102.1"

```
