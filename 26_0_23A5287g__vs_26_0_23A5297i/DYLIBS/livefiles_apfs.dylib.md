## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0xbde8c
+2632.0.68.0.3
+  __TEXT.__text: 0xbe258
   __TEXT.__auth_stubs: 0x8f0
   __TEXT.__const: 0x85c0
-  __TEXT.__oslogstring: 0x15b33
+  __TEXT.__oslogstring: 0x15b39
   __TEXT.__cstring: 0x54c5
   __TEXT.__unwind_info: 0xfd8
   __DATA_CONST.__got: 0x40

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 54D618EC-A5C9-3F41-BE21-E9A362710439
-  Functions: 2427
-  Symbols:   5462
+  UUID: C290729E-04BF-39E8-A0DD-551BD8B55074
+  Functions: 2428
+  Symbols:   5466
   CStrings:  2191
 
Symbols:
+ _apfs_dereferenced_phys_extent
+ _apfs_update_purge_stat
Functions:
~ _apfs_update_phys_range : 3176 -> 3328
+ _apfs_dereferenced_phys_extent
~ _remove_extent_of_file : 508 -> 540
~ _decrement_dstream_id_for_deletion : 764 -> 796
~ _fs_remove_xattr_with_nstream_inode : 1184 -> 1180
~ _nx_checkpoint_load_data : 1532 -> 1528
~ _obj_cache_create : 712 -> 768
~ _obj_create_internal : 2232 -> 2228
~ _obj_clone : 804 -> 832
~ _obj_alloc : 2464 -> 2672
~ _obj_init_wakeup : 72 -> 64
~ _obj_get : 3272 -> 3328
~ _obj_get_finish : 380 -> 448
~ _obj_checkpoint_get : 1004 -> 1008
~ _obj_cache_perform_deferred_updates : 308 -> 364
~ _obj_free_list_remove : 116 -> 180
~ _spaceman_iterate_free_extents_internal : 6824 -> 6776
~ _btree_node_get : 556 -> 564
~ _bt_shift_or_split : 8308 -> 8340
~ _bt_lookup_internal : 1568 -> 1584
~ _btree_create_extended : 532 -> 528
~ _btree_get_extended : 752 -> 760
~ _btree_node_copy : 1224 -> 1240
~ _nx_get_evict_mapping_tree : 312 -> 316
CStrings:
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error allocating new physical location %d\n"
+ "%s:%d: %s flags 0x%llx type 0x%x/0x%x error reserving %d blocks of space: %d\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
+ "2632.0.68.0.3"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error allocating new physical location %d\n"
- "%s:%d: %s flags 0x%x type 0x%x/0x%x error reserving %d blocks of space: %d\n"
- "%s:%d: %s oid 0x%llx flags 0x%x type 0x%x/0x%x: attempt to perform async fetch without proper init args\n"
- "2632.0.54.0.2"

```
