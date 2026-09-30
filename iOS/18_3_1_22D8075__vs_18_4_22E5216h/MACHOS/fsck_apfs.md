## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x4bbdc
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__cstring: 0x181df
-  __TEXT.__const: 0x814c
-  __TEXT.__unwind_info: 0xa10
-  __DATA_CONST.__auth_got: 0x468
+2332.100.75.502.1
+  __TEXT.__text: 0x4cb74
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__cstring: 0x187bc
+  __TEXT.__const: 0x8104
+  __TEXT.__unwind_info: 0xa30
+  __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__auth_ptr: 0x48
   __DATA_CONST.__const: 0x560
   __DATA_CONST.__cfstring: 0x200
-  __DATA.__data: 0xec4
-  __DATA.__bss: 0x1c7c4
+  __DATA.__data: 0xed4
+  __DATA.__bss: 0x1c864
   __DATA.__common: 0xab1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 820
-  Symbols:   158
-  CStrings:  1828
+  Functions: 824
+  Symbols:   164
+  CStrings:  1850
 
Symbols:
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
CStrings:
+ "%s (id %llu): invalid dir-stats flags (0x%x) on volume without attribution tags\n"
+ "%s (id %llu): invalid internal_flags (0x%llx) given apfs_fs_flags (0x%llx) PFK bit\n"
+ "%s (id %llu): invalid internal_flags (0x%llx) given volume readonly compatible features (0x%llx)\n"
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "2332.100.75.502.1"
+ "aborting purgeable cross checks - out of memory\n"
+ "can't unmark purgeable (file_id %llu) for cross checks\n"
+ "failed to cross check purgeable inode: %d (%s)\n"
+ "failed to cross check purgeable record: %d (%s)\n"
+ "failed to enqueue purgeable record (file id %llu, atime %llu) for remove\n"
+ "failed to finish pending reads from the bitmap iterator: %d (%s)"
+ "failed to insert purgeable (file_id %llu): %s (%d)\n"
+ "failed to search purgeable record (file id %llu) in the fsck_apfs tree: %d (%s)\n"
+ "fd_dev_hint_flush"
+ "found an orphan purgeable record (atime %llu, file_id %llu)\n"
+ "found orphan/invalid clone mapping (private_id %llu, file_id %llu)\n"
+ "found orphan/invalid purgeable record (file_id %llu, atime %llu)\n"
+ "inode (id %llu): unable to add repair to unmark purgeable: %d (%s)\n"
+ "need to insert missing clone mapping (private_id %llu, file_id %llu)\n"
+ "purgeable inode (id %llu) is missing a purgeable record\n"
+ "purgeable record (atime %llu, file_id %llu) is different than inode atime (%llu)\n"
+ "skipping purgeable cross checks\n"
+ "unable to find inode (id %llu): %d (%s)\n"
+ "unable to init fsroot tree to enque purgeable repairs\n"
- "-"
- "2317.82.1"
- "Unknown"

```
