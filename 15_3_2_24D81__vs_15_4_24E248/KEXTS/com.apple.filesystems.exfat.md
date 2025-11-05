## com.apple.filesystems.exfat

> `com.apple.filesystems.exfat`

```diff

-463.60.8.0.0
-  __TEXT.__const: 0xf1
+488.100.10.0.0
+  __TEXT.__const: 0x135
   __TEXT.__cstring: 0x121f
-  __TEXT_EXEC.__text: 0xac38
+  __TEXT_EXEC.__text: 0xae78
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x468
   __DATA.__common: 0x58
   __DATA_CONST.__auth_got: 0x450
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__kalloc_type: 0x640
-  UUID: 2B5523AA-01B9-3666-A5A7-BB36BA87BE41
-  Functions: 165
-  Symbols:   391
+  UUID: 38CD5503-6749-3E2F-A66F-F3F0A32FEF98
+  Functions: 164
+  Symbols:   390
   CStrings:  104
 
Symbols:
- exfat_module_start.cold.1
Functions:
~ _exfat_vfs_unmount : 476 -> 480
~ _exfat_bad_boot_checksum : 148 -> 184
~ _exfat_mount_internal : 1644 -> 1640
~ _exfat_vfs_mount : 472 -> 476
~ _exfat_sort_nodes : 116 -> 108
~ _exfat_lock_four : 128 -> 132
~ _exfat_unlock_four : 128 -> 132
~ _exfat_update_times : 288 -> 296
~ _exfat_dir_iterate : 1060 -> 1088
~ _exfat_system_node_get : 620 -> 608
~ _exfat_name_hash : 64 -> 68
~ _exfat_read_upcase : 668 -> 680
~ _exfat_get_bitmap_file : 176 -> 180
~ _exfat_vnop_readdir : 704 -> 696
~ _exfat_readdir_callback : 548 -> 560
~ _exfat_lookup_callback : 184 -> 220
~ _exfat_lookup_componentname : 404 -> 408
~ _exfat_vnop_remove : 332 -> 340
~ _exfat_vnop_rmdir : 444 -> 452
~ _exfat_vnop_create : 780 -> 788
~ _exfat_vnop_mkdir : 1052 -> 1060
~ _exfat_vnop_symlink : 1324 -> 1360
~ _exfat_vnop_rename : 1436 -> 1460
~ _exfat_vnop_setattr : 708 -> 704
~ _exfat_vnop_pageout : 828 -> 824
~ _exfat_dir_flush : 252 -> 264
~ _exfat_vnop_readlink : 332 -> 336
~ _exfat_vnop_ioctl : 136 -> 144
~ _exfat_fat_init_vol : 384 -> 376
~ _exfat_fat_find_last_cluster : 428 -> 432
~ _exfat_bitmap_mark_free : 436 -> 432
~ _exfat_bitmap_mark_used : 436 -> 432
~ _exfat_extent_insert : 140 -> 136
~ _exfat_file_add_extent : 596 -> 588
~ _exfat_file_extend : 580 -> 588
~ _exfat_file_shrink : 388 -> 380
~ _exfat_timestamp_to_unix : 252 -> 256
~ _exfat_hash_remove : 32 -> 24
~ _exfat_hash_insert : 76 -> 96
~ _exfat_md5_digest : 216 -> 220
~ _exfat_check_link : 532 -> 536
~ _exfat_dir_buf_check : 180 -> 188
~ _exfat_dir_read : 432 -> 436
~ _exfat_checksum_file_set : 88 -> 92
~ _exfat_node_get : 1496 -> 1500
~ _exfat_node_update : 468 -> 500
~ _exfat_file_set_copy_name : 208 -> 464
~ _exfat_file_set_init : 316 -> 340
~ _exfat_file_set_rename : 280 -> 300
- exfat_module_start.cold.1
~ exfat_dir_buf_check.cold.1 : 44 -> 52
~ exfat_dir_buf_check.cold.3 : 52 -> 44

```
