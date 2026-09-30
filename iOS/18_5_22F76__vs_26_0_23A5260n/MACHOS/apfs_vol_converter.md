## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x57240
-  __TEXT.__auth_stubs: 0x9e0
+2632.0.15.0.1
+  __TEXT.__text: 0x57a50
+  __TEXT.__auth_stubs: 0x9d0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x11894
+  __TEXT.__cstring: 0x11ac6
   __TEXT.__const: 0x2c0
-  __TEXT.__gcc_except_tab: 0x570
-  __TEXT.__unwind_info: 0xb98
-  __DATA_CONST.__auth_got: 0x4f8
+  __TEXT.__gcc_except_tab: 0x5cc
+  __TEXT.__unwind_info: 0xb90
+  __DATA_CONST.__auth_got: 0x4f0
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xa68
+  __DATA_CONST.__const: 0xb20
   __DATA_CONST.__cfstring: 0xb00
-  __DATA.__data: 0x378
+  __DATA.__data: 0x380
   __DATA.__bss: 0x64
   __DATA.__common: 0xf84
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 0842D1CD-E2FB-3C1B-9998-458AF8E1F587
-  Functions: 837
-  Symbols:   183
-  CStrings:  1665
+  UUID: 22266911-1176-3B77-9DC1-A6C16BF72BBE
+  Functions: 841
+  Symbols:   182
+  CStrings:  1674
 
Symbols:
+ __ZnwmSt19__type_descriptor_t
+ _strstr
- _CFStringCreateWithCString
- __Znwm
- _uuid_is_null
CStrings:
+ "\tClearPurgeIno: cleared INODE_IS_PURGEABLE on ino %llu in purgeableInoSet\n"
+ "\tOnInsertPurgeRec: removed ino %llu from purgeableInoSet\n"
+ "\tOnPostMoveObj: added ino %llu to purgeableInoSet\n"
+ "%s:%d: %s Fusion is not supported anymore\n"
+ "%s:%d: %s couldn't enter transaction to set apfs_fixup_flags, %d\n"
+ "%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s fs_alloc_count mismatch: fs root nodes %lld extent %lld omap %lld snap_meta %lld doc_id %lld prev_doc_id %lld fext: %lld clonegroup: %lld pfkur: %lld er: %lld udata: %lld fs_alloc_count %lld != count %lld\n"
+ "%s:%d: %s set apfs_fixup_flags to %#llx\n"
+ "%s:%d: %s superblock container size %lld greater than device size %lld\n"
+ "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s<->superblock mismatch on fusion uuid\n"
+ "%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
+ "%s:%d: locking id %llu, which is already locked by this thread\n"
+ "%s:%u Err: Failed to insert matching PurgeRec for ino %llu into %s: %u\n"
+ "%s:%u Err: Failed to insert new purgeable record on %s, ino %llu dstream %llu - file ID didn't match; new %llu != old %llu\n"
+ "%s:%u Err: Failed to remove ino %llu from purgeableInoSet\n"
+ "%s:%u Err: update_jobj for j_inode_t %llu into source failed: %u\n"
+ "%s:%u Err: update_jobj for j_inode_t %llu into target failed: %u\n"
+ "%s:%u Warn: Warning: The volume path %s won't work with encrypted volumes, use rdisk instead\n"
+ "... Can't find a purgeable inode for purgeable drec on either source or target - removing purgeable drec %llu\n"
+ "2632.0.15.0.1"
+ "ClearPurgeInosWithoutPurgeRec"
+ "OnInsertPurgeRec"
+ "Post-move: ClearPurgeInosWithoutPurgeRec"
+ "PurgeInos cleared  : %zu\n"
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
- "%s:%d: failed to open connection for multikey crypto i/o on device %s: %s\n"
- "%s:%d: tier2 device initialization failed: %d\n"
- "%s:%u Err: Failed to insert PurgeRec for ino %llu into %s: %u\n"
- "... Can't find an inode for purgeable drec on either source or target - removing purgeable drec %llu\n"
- "2332.120.31.0.2"
- "failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
- "multiKeyEncryption"
- "nx-fusion-mt-lock"
- "nx_rc_allocation_lock"
- "nx_reaper_add"
- "omap_set"

```
