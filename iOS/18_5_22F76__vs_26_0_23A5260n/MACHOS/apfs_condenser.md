## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x4c4a8
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__cstring: 0xf741
+2632.0.15.0.1
+  __TEXT.__text: 0x4c010
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__cstring: 0xf6bc
   __TEXT.__const: 0x260
-  __TEXT.__unwind_info: 0x808
-  __DATA_CONST.__auth_got: 0x3c0
+  __TEXT.__unwind_info: 0x7e8
+  __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x898
+  __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__cfstring: 0x120
   __DATA.__data: 0x360
   __DATA.__common: 0x41c

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 95CCB166-272B-347E-A001-178E73AB2F77
+  UUID: A90754F2-199F-3B42-98C7-7AF878ED09A0
   Functions: 659
-  Symbols:   134
-  CStrings:  1275
+  Symbols:   133
+  CStrings:  1273
 
Symbols:
- _uuid_is_null
CStrings:
+ "%s:%d: %s Fusion is not supported anymore\n"
+ "%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n"
+ "%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n"
+ "%s:%d: %s set apfs_fixup_flags to %#llx\n"
+ "%s:%d: %s superblock container size %lld greater than device size %lld\n"
+ "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s<->superblock mismatch on fusion uuid\n"
+ "%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
+ "2632.0.15.0.1"
+ "apfs-clonegroup-lock-mutex"
+ "authapfs_validate_node"
+ "clear_invalid_fixups"
+ "nx_reaper_add_ext"
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
- "2332.120.31.0.2"
- "failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
- "nx-fusion-mt-lock"
- "nx_rc_allocation_lock"
- "nx_reaper_add"
- "omap_set"

```
