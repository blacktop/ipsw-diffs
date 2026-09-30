## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2632.0.54.0.2
-  __TEXT.__text: 0x4fee0
+2632.0.68.0.3
+  __TEXT.__text: 0x500c0
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__const: 0x8410
-  __TEXT.__cstring: 0xdde2
+  __TEXT.__cstring: 0xdde8
   __TEXT.__oslogstring: 0xb0e
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__unwind_info: 0x918

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: AB78A6B1-D8EF-35B0-B218-28FD886127CB
+  UUID: 3140C128-5875-3D95-8D08-A648700C550D
   Functions: 807
   Symbols:   1760
   CStrings:  1443
Functions:
~ _btree_node_get : 564 -> 572
~ _bt_lookup_internal : 1556 -> 1572
~ _btree_create_extended : 532 -> 528
~ _btree_get_extended : 752 -> 760
~ _btree_node_copy : 1032 -> 1048
~ _spaceman_iterate_free_extents_internal : 5812 -> 5888
~ _spaceman_check_allocation_status_internal : 1384 -> 1388
~ _nx_check : 12052 -> 12092
~ _obj_cache_create : 708 -> 764
~ _obj_create_internal : 1868 -> 1812
~ _obj_clone : 800 -> 828
~ _obj_alloc : 2604 -> 2648
~ _obj_init_wakeup : 72 -> 64
~ _obj_get : 3264 -> 3320
~ _obj_get_finish : 380 -> 448
~ _obj_checkpoint_get : 1000 -> 1004
~ _obj_cache_perform_deferred_updates : 304 -> 360
~ _obj_free_list_remove : 116 -> 180
~ _nx_get_evict_mapping_tree : 320 -> 324
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
