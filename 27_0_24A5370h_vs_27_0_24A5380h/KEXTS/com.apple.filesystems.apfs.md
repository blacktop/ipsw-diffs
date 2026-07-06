## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

   __TEXT.__const: 0x94c
-  __TEXT.__cstring: 0x4f8b7
-  __TEXT_EXEC.__text: 0x150aa8
-  __TEXT_EXEC.__auth_stubs: 0x22f0
+  __TEXT.__cstring: 0x4fc39
+  __TEXT_EXEC.__text: 0x150f10
+  __TEXT_EXEC.__auth_stubs: 0x2330
   __DATA.__data: 0x75c
   __DATA.__bss: 0xd80
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x6890
-  __DATA_CONST.__kalloc_type: 0x54c0
+  __DATA_CONST.__kalloc_type: 0x5440
   __DATA_CONST.__kalloc_var: 0x2bc0
   __DATA_CONST.__assert: 0x14
-  __DATA_CONST.__auth_got: 0x1178
+  __DATA_CONST.__auth_got: 0x1198
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2390
+  Functions: 2399
   Symbols:   0
-  CStrings:  6926
+  CStrings:  6946
 
Sections:
~ __TEXT.__const : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__assert : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
CStrings:
+ "!\"crypto key pool is not supported for class\\n\""
+ "%s:%d: %s Grafting %s which is a clone of %s, share its blockmap lut\n"
+ "%s:%d: %s can't allocate metadata %lld host free %llu in-flight allocations %lld\n"
+ "%s:%d: %s can't reserve metadata %lld host free %llu in-flight allocations %lld\n"
+ "%s:%d: %s checking for existing proposed vek\n"
+ "%s:%d: %s cluster_push() after msync failed with %d on ino(%llu)\n"
+ "%s:%d: %s commit failed, err = %d (will retry on next boot)\n"
+ "%s:%d: %s commit succeeded\n"
+ "%s:%d: %s failed to allocate buffer for deferred commit\n"
+ "%s:%d: %s failed to clean-up proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to commit proposed wvek record, err = 0x%x (%d more retries)\n"
+ "%s:%d: %s failed to enter tx to store proposed wvek record, err = %d\n"
+ "%s:%d: %s failed to enter tx to update wvek record, err = %d\n"
+ "%s:%d: %s failed to flush tx storing proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to get vek blob state, err = 0x%x\n"
+ "%s:%d: %s failed to load volume class keys, error = %x\n"
+ "%s:%d: %s failed to look up vek, err = %d\n"
+ "%s:%d: %s failed to recover existing proposed vek, err = %d\n"
+ "%s:%d: %s failed to recover vek before first-unlock\n"
+ "%s:%d: %s failed to store proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to unwrap vek, err = 0x%x\n"
+ "%s:%d: %s failed to update wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s found existing proposed wvek record in nx keybag (from previous failure)\n"
+ "%s:%d: %s mount force firmlinks\n"
+ "%s:%d: %s no commit pending\n"
+ "%s:%d: %s no existing proposed vek to recover\n"
+ "%s:%d: %s oid %lld xid %lld error freeing stale deletion record %d\n"
+ "%s:%d: %s oid %lld xid %lld paddr 0x%llx ov_flags 0x%x error freeing stale entry location %d\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "%s:%d: %s received migrated vek during unwrap\n"
+ "%s:%d: %s remove stale mapping oid %lld xid %lld\n"
+ "%s:%d: %s remove stale mapping oid %lld xid %lld failed: %d\n"
+ "%s:%d: %s scheduled deferred commit\n"
+ "%s:%d: %s successfully loaded volume class keys\n"
+ "%s:%d: %s successfully recovered existing proposed vek\n"
+ "%s:%d: evicting cached vek for volume %s\n"
+ "%s:%d: failed to lookup existing proposed wvek record in nx keybag, err = %d\n"
+ "11212221111111222222222211111111111111222222122212222222221222222222221221121121122222222222222222112222222221222212212"
+ "1121222111111122222222221111222222222211122222111122112221111221122211112211222111122112221111221122211112211222111122112122122122222111111122222211122211111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222221111121121112222222111112122222112122222222222222222222222222212222122222222222112222112211111111111221122122122222211222212122222222122222221222222222111111111111111122221121222211222222112212222221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221"
+ "2026/06/30"
+ "2121222222118"
+ "21:00:16"
+ "3283.0.9.502.1"
+ "Jun 30 2026"
+ "apfs-3283.0.9.502.1"
+ "apfs->apfs_vek.wvek == ((void*)0)"
+ "apfs->apfs_vek.wvek == wvek"
+ "apfs_keycache_delete_for_uuid"
+ "apfs_vek_commit_cb"
+ "apfs_vek_commit_enter"
+ "apfs_vek_commit_internal"
+ "apfs_vek_unwrap"
+ "com.apple.private.apfs.force-firmlink-stitch"
+ "kb"
+ "wvek->data"
+ "wvek->len <= 512"
- "%s:%d: %s APFS_DEBUG_OP_GET_FILE_DSTREAMS is not supported in grafts\n"
- "%s:%d: %s APFS_DEBUG_OP_GET_FILE_EXTS is not supported in grafts\n"
- "%s:%d: %s Bad overlap %lld, %lld to range %lld, %lld\n"
- "%s:%d: %s Bootcache inodes tree is NULL, cannot ignore boot files\n"
- "%s:%d: %s Grafting a clone, share blockmap lut with %s\n"
- "%s:%d: %s No defrag state for dstream in dstreams tree %lld\n"
- "%s:%d: %s Not a pure overlap %lld, %lld to range %lld, %lld, in newer xid (%lld > %lld) \n"
- "%s:%d: %s bad ranges returned from extent_update_range_to_evict %lld %lld\n"
- "%s:%d: %s can't allocate metadata block(s) allocations_not_yet_updated_on_host %lld raw free space %llu (desired_count %lld)\n"
- "%s:%d: %s can't reserve metadata block(s) allocations_not_yet_updated_on_host %lld raw free space %llu (count %lld)\n"
- "%s:%d: %s could not locate snap meta of snapshot xid %llu\n"
- "%s:%d: %s dstream %lld pext tree is NULL\n"
- "%s:%d: %s dstream Ids do not match %lld != %lld\n"
- "%s:%d: %s dstream_pext_tree_create failed with error %d\n"
- "%s:%d: %s extent_update_range_to_evict failed: %d - %s\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to delete dstream pext tree, error: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "%s:%d: %s failed to get iocount on graft inode, error %d\n"
- "%s:%d: %s tree_lookup for dstream %lld failed with error %d\n"
- "%s:%d: failed to add proposed wvek record in nx keybag, err = %d\n"
- "%s:%d: failed to clean-up proposed wvek record in nx keybag, err = %d\n"
- "%s:%d: failed to commit proposed wvek record, err = 0x%x (%d more retries)\n"
- "%s:%d: failed to get vek blob state, err = 0x%x\n"
- "%s:%d: failed to unwrap volume key, err = 0x%x\n"
- "%s:%d: failed to update wvek record in nx keybag, err = %d\n"
- "1121222111111122222222221111111111111122222212221222222222122222222222122112112112222222222222222211222222222122111221221"
- "112122211111112222222222111122222222221112222211112211222111122112221111221122211112211222111122112221111221122211112211212212212222211111112222221112221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122222111112112111222222211111212222222222222222222222222221222212222222222211222211221111111111122112212212222221122221212222222122222221222222222111111111111111122221121222211222222112212222221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221"
- "19:34:25"
- "2026/06/18"
- "212122222118"
- "3283"
- "Jun 18 2026"
- "apfs-3283"
- "apfs_commit_update_volume_key"
- "apfs_find_graft_state_by_graft_private_id"
- "dstream_pext_tree_create"
- "dstream_pext_tree_lookup_overlap"
- "dstream_should_ignore"
- "extent_update_range_to_evict"
- "nx_keybag_lookup_vek"
- "site.struct aks_fv_data_s"

```
