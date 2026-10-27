## com.apple.filesystems.tmpfs

> `com.apple.filesystems.tmpfs`

```diff

-94.0.0.0.0
+94.40.4.0.0
   __TEXT.__cstring: 0x4b7
   __TEXT.__const: 0x40
-  __TEXT.__os_log: 0x20a
-  __TEXT_EXEC.__text: 0x9808
-  __TEXT_EXEC.__auth_stubs: 0x640
+  __TEXT.__os_log: 0x19e
+  __TEXT_EXEC.__text: 0x9910
+  __TEXT_EXEC.__auth_stubs: 0x650
   __DATA.__data: 0x180
   __DATA.__bss: 0x8
   __DATA.__common: 0x420
   __DATA_CONST.__const: 0x4e0
   __DATA_CONST.__kalloc_type: 0x480
-  __DATA_CONST.__auth_got: 0x320
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0x20
-  Functions: 152
-  Symbols:   363
-  CStrings:  46
+  Functions: 153
+  Symbols:   364
+  CStrings:  44
 
Symbols:
+ _tmpfs_commit_upl_after_error
+ _ubc_upl_abort_range
+ tmpfs_alloc_dirent.kalloc_type_view_499
+ tmpfs_alloc_dirent.kalloc_type_view_504
+ tmpfs_alloc_dirent.kalloc_type_view_510
+ tmpfs_alloc_node.kalloc_type_view_269
+ tmpfs_alloc_node.kalloc_type_view_326
+ tmpfs_extent_free.kalloc_type_view_2183
+ tmpfs_extents_insert.kalloc_type_view_2143
+ tmpfs_free_dirent.kalloc_type_view_552
+ tmpfs_free_links.kalloc_type_view_2498
+ tmpfs_free_node.kalloc_type_view_411
+ tmpfs_node_add_xattr.kalloc_type_view_1885
+ tmpfs_node_add_xattr.kalloc_type_view_1895
+ tmpfs_node_remove_xattr.kalloc_type_view_1924
+ tmpfs_remove_link_origin.kalloc_type_view_2467
+ tmpfs_update_link_origin.kalloc_type_view_2444
- tmpfs_alloc_dirent.kalloc_type_view_512
- tmpfs_alloc_dirent.kalloc_type_view_517
- tmpfs_alloc_dirent.kalloc_type_view_523
- tmpfs_alloc_node.kalloc_type_view_282
- tmpfs_alloc_node.kalloc_type_view_339
- tmpfs_extent_free.kalloc_type_view_2196
- tmpfs_extents_insert.kalloc_type_view_2156
- tmpfs_free_dirent.kalloc_type_view_565
- tmpfs_free_links.kalloc_type_view_2499
- tmpfs_free_node.kalloc_type_view_424
- tmpfs_initialize_region._os_log_fmt
- tmpfs_node_add_xattr.kalloc_type_view_1898
- tmpfs_node_add_xattr.kalloc_type_view_1908
- tmpfs_node_remove_xattr.kalloc_type_view_1937
- tmpfs_remove_link_origin.kalloc_type_view_2468
- tmpfs_update_link_origin.kalloc_type_view_2445
Functions:
~ _tmpfs_getattr : 1104 -> 1116
~ _tmpfs_setattr : 644 -> 656
~ _tmpfs_read : 920 -> 940
~ _tmpfs_write : 1416 -> 1488
~ _tmpfs_pagein : 284 -> 280
~ _tmpfs_pageout : 844 -> 848
+ _tmpfs_commit_upl_after_error
~ _tmpfs_initialize_region : 556 -> 376
~ _tmpfs_pagein_range : 976 -> 956
~ _tmpfs_trim_paged_out : 340 -> 412
~ _tmpfs_fhtovp : 292 -> 356
CStrings:
- "error %d mapping UPL, upl_f_offset %llu, upl_len %d\n"
- "error %d unmapping UPL, upl_f_offset %llu, upl_len %d\n"
```
