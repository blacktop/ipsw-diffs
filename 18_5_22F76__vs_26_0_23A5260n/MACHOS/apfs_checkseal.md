## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x4f174
-  __TEXT.__auth_stubs: 0x750
+2632.0.15.0.1
+  __TEXT.__text: 0x4ecf4
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__const: 0x510
-  __TEXT.__cstring: 0x10058
-  __TEXT.__unwind_info: 0x8d8
-  __DATA_CONST.__auth_got: 0x3a8
+  __TEXT.__cstring: 0xff5c
+  __TEXT.__unwind_info: 0x8b8
+  __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__const: 0x7b8
   __DATA_CONST.__cfstring: 0x160
   __DATA.__data: 0x368
   __DATA.__common: 0x414

   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: BC06C0E9-A76B-3294-83F1-186AE30F9397
+  UUID: BBFA7405-F507-38F0-A79E-D0E34F36C74E
   Functions: 722
-  Symbols:   131
-  CStrings:  1304
+  Symbols:   130
+  CStrings:  1301
 
Symbols:
- _uuid_is_null
CStrings:
+ "%s:%d: %s Fusion is not supported anymore\n"
+ "%s:%d: %s Incorrect hash digest size for the hash record at offset %lld in data stream %lld: on-disk %d, expected %d\n"
+ "%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n"
+ "%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n"
+ "%s:%d: %s set apfs_fixup_flags to %#llx\n"
+ "%s:%d: %s superblock container size %lld greater than device size %lld\n"
+ "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s<->superblock mismatch on fusion uuid\n"
+ "%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
+ "apfs-clonegroup-lock-mutex"
+ "authapfs_validate_node"
+ "clear_invalid_fixups"
+ "nx_reaper_add_ext"
- "%s:%d: %s Extent offset does not match after remapping: changed from %lld bytes at offset %lld to %lld bytes at offset %lld\n"
- "%s:%d: %s Incorrect hash digest size for the hash record at offset %lld in data stream %lld: expected %d, got %d\n"
- "%s:%d: %s container block size too small for tier2 device block size (%d < %d)\n"
- "%s:%d: %s couldn't read tier2 device superblock of size %d\n"
- "%s:%d: %s failed to set tier2 device: %d\n"
- "%s:%d: %s failed to write superblock to fusion tier2 device block 0: %d\n"
- "%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n"
- "%s:%d: %s superblock container size %lld greater than device size(s) %lld\n"
- "%s:%d: %s tier2 device superblock doesn't agree with main superblock\n"
- "%s:%d: %s xid %lld failed to write superblock to fusion tier2 device block 0: %d\n"
- "%s:%d: %s<->superblock mismatch on fusion uuid, tier2=%d\n"
- "%s:%d: tier2 device initialization failed: %d\n"
- "failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
- "nx-fusion-mt-lock"
- "nx_rc_allocation_lock"
- "nx_reaper_add"
- "omap_set"

```
