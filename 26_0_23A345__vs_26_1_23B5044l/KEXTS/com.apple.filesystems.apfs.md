## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-2632.2.1.0.0
+2632.40.6.0.1
   __TEXT.__const: 0xa18
-  __TEXT.__cstring: 0x4c596
-  __TEXT_EXEC.__text: 0x159a78
+  __TEXT.__cstring: 0x4c5ad
+  __TEXT_EXEC.__text: 0x159b14
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x638
-  __DATA.__bss: 0xcb0
+  __DATA.__data: 0x640
+  __DATA.__bss: 0xca8
   __DATA_CONST.__auth_got: 0x1150
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__kalloc_type: 0x4f00
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: 519B216A-E204-33C7-B6D9-D95EA7805079
+  UUID: E2B5221D-C75E-3779-9665-D6383A28F387
   Functions: 2319
   Symbols:   0
-  CStrings:  6589
+  CStrings:  6590
 
Functions:
~ _doc_id_tree_destroy : 1200 -> 1204
~ _child_size_calculator_cb : 1104 -> 1108
~ _purge_files_with_ino : 2488 -> 2496
~ __collect_purgeable_files_cb : 1136 -> 1140
~ __remove_offline_purgeable_file : 1664 -> 1668
~ sub_fffffe000adbc394 -> sub_fffffe000ae8699c : 76 -> 80
~ __clear_purgeable_files_cb : 1696 -> 1700
~ __get_bulk_purgeable_info_cb : 1384 -> 1388
~ __fixup_purgeable_recs_cb : 820 -> 824
~ __get_purgeable_stats_cb : 2180 -> 2184
~ __get_purgeable_extents_cb : 952 -> 956
~ _cancel_purge : 544 -> 548
~ _apfs_do_scan_for_fragmentation : 1312 -> 1320
~ _apfs_scan_for_fragmentation_cb : 472 -> 476
~ sub_fffffe000add4f7c -> sub_fffffe000ae9f5ac : 1016 -> 1020
~ sub_fffffe000add56b4 -> sub_fffffe000ae9fce8 : 1340 -> 1344
~ sub_fffffe000adea020 -> sub_fffffe000aeb4658 : 1392 -> 1396
~ _pfkur_roll_all_inodes_continuation -> sub_fffffe000aeebbc4 : 1124 -> 1128
~ sub_fffffe000ae22ea8 -> sub_fffffe000aeed4e8 : 116 -> 120
~ sub_fffffe000ae22f1c -> sub_fffffe000aeed560 : 112 -> 116
~ sub_fffffe000ae2ea38 -> sub_fffffe000aef9080 : 176 -> 180
~ _spec_telem_info_iterate : 1988 -> 1992
~ _nx_block_out_physical_range_internal : 5636 -> 5660
~ _nx_check_snapshots_data_location : 1732 -> 1740
~ _nx_evict_omap_tree : 1344 -> 1348
~ sub_fffffe000ae41d80 -> sub_fffffe000af0c3f4 : 864 -> 868
~ _nx_evict_physical_tree_in_snap : 2808 -> 2812
~ _purgatory_cleaner_wakeup : 280 -> 284
~ _apfs_cleanup_purgatory_continuation : 10556 -> 10576
~ _kbn_handler_continuation : 1316 -> 1320
~ sub_fffffe000ae54ac4 -> sub_fffffe000af1f15c : 304 -> 308
~ _handle_wait_for_snapshot_deletion : 936 -> 944
~ _handle_wait_for_reaper : 752 -> 756
~ _do_iterative_file_extent_removal : 1684 -> 1692
~ __remove_extents_of_file_cb : 1852 -> 1856
~ _fs_delete_inode_with_name : 1084 -> 1088
~ _extent_remover_callback : 900 -> 904
~ _fs_map_file_offset_ext : 6264 -> 6120
~ _fs_evict_range_internal : 460 -> 464
~ _dstream_evict_scanner : 1272 -> 1280
~ _dstream_evict_scanner_internal : 1588 -> 1592
~ _extent_evict_scanner : 5744 -> 5748
~ _evict_map_range : 3108 -> 3112
~ _purgatory_cleaner_cb : 736 -> 740
~ _fixup_thread_wrapper : 4716 -> 4724
~ _apfs_stop_bg_work : 296 -> 304
~ _apfs_fsinfo_iterate_fsroot_wrapper : 172 -> 176
~ _btree_evict_range : 2224 -> 2252
~ _omap_evict_range_mappings : 3188 -> 3192
~ sub_fffffe000aee19dc -> sub_fffffe000afac058 : 244 -> 248
~ _dir_stats_op_ext : 1380 -> 1384
~ __setup_dir_stats_cb : 2720 -> 2724
~ _dir_stats_moved : 4772 -> 4776
CStrings:
+ "2025/09/16"
+ "20:22:54"
+ "20:22:55"
+ "2632.40.6.0.1"
+ "Sep 16 2025"
+ "apfs-2632.40.6.0.1"
+ "apfs_stop_bg_work_ext"
- "2025/08/26"
- "20:16:49"
- "2632.2.1"
- "Aug 26 2025"
- "apfs-2632.2.1"
- "apfs_stop_bg_work"

```
