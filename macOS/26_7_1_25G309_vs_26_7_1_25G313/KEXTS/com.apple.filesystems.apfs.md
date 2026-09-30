## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-2811.160.7.701.3
+2811.160.7.702.4
   __TEXT.__const: 0xa28
-  __TEXT.__cstring: 0x5579c
-  __TEXT_EXEC.__text: 0x16631c
+  __TEXT.__cstring: 0x557af
+  __TEXT_EXEC.__text: 0x166678
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x70c
   __DATA_CONST.__auth_got: 0x1310

   __DATA_CONST.__assert: 0x294
   Functions: 2504
   Symbols:   4570
-  CStrings:  7328
+  CStrings:  7329
 
Symbols:
+ _fs_add_xattr.kalloc_type_view_23203
+ _fs_add_xattr.kalloc_type_view_23209
+ _fs_add_xattr.kalloc_type_view_23212
+ _fs_add_xattr.kalloc_type_view_23266
+ _fs_add_xattr.kalloc_type_view_23267
+ apfs_punch_out_ranges_in_fext.kalloc_type_view_21498
+ apfs_punch_out_ranges_in_fext.kalloc_type_view_21505
+ apfs_update_reserved_ranges.kalloc_type_view_21641
+ apfs_update_reserved_ranges.kalloc_type_view_21646
+ arle_alloc_pending_entry.kalloc_type_view_21083
+ bt_merge_up.kalloc_type_view_4588
+ bt_merge_up.kalloc_type_view_4701
+ btree_evict_range.kalloc_type_view_6986
+ btree_evict_range.kalloc_type_view_6993
+ btree_evict_range.kalloc_type_view_7137
+ btree_iterate_nodes.kalloc_type_view_6426
+ btree_iterate_nodes.kalloc_type_view_6575
+ change_crypto_id_prot_class.kalloc_type_view_9842
+ change_crypto_id_prot_class.kalloc_type_view_9908
+ clone_fexts_.kalloc_type_view_14309
+ clone_fexts_.kalloc_type_view_14322
+ clone_fexts_.kalloc_type_view_14380
+ create_new_crypto_state_for_id.kalloc_type_view_7646
+ create_new_crypto_state_for_id.kalloc_type_view_7651
+ create_new_crypto_state_for_id.kalloc_type_view_7671
+ create_sibling_link.kalloc_type_view_11490
+ create_sibling_link.kalloc_type_view_11506
+ dir_rec_alloc_with_hash.kalloc_type_view_11125
+ dir_rec_alloc_with_hash.kalloc_type_view_11131
+ dir_rec_alloc_with_hash.kalloc_type_view_11155
+ dump_extents_of_stream.kalloc_type_view_18573
+ ek_to_crypto_state.kalloc_type_view_33387
+ er_state_allocate_roll_buffers.kalloc_type_view_8183
+ er_state_destroy_obj.kalloc_type_view_8827
+ er_state_free_roll_buffers.kalloc_type_view_8145
+ er_state_obj_create_phys_from_previous_version.kalloc_type_view_8225
+ er_state_upgrade_version.kalloc_type_view_8378
+ extent_evict_range.kalloc_type_view_25925
+ extent_evict_range.kalloc_type_view_26025
+ fext_collector.kalloc_type_view_14075
+ fext_collector_cleanup.kalloc_type_view_14050
+ fext_collector_reset.kalloc_type_view_14039
+ free_linkids.kalloc_type_view_11682
+ fs_get_xattr_ext.kalloc_type_view_23307
+ fs_get_xattr_ext.kalloc_type_view_23327
+ fs_init_bootcache_inodes_dstreams_info.kalloc_type_view_27878
+ fs_iterate_snapshots.kalloc_type_view_27091
+ fs_iterate_snapshots.kalloc_type_view_27138
+ fs_map_file_offset_ext.kalloc_type_view_22053
+ fs_map_file_offset_ext.kalloc_type_view_22085
+ fs_map_file_offset_ext.kalloc_type_view_22146
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23404
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23420
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23441
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23561
+ icp_new_crypto.kalloc_type_view_7965
+ icp_new_crypto.kalloc_type_view_7975
+ icp_new_crypto.kalloc_type_view_7977
+ icp_new_crypto.kalloc_type_view_8011
+ icp_new_crypto.kalloc_type_view_8036
+ icp_new_crypto.kalloc_type_view_8051
+ insert_linkid.kalloc_type_view_11630
+ jobj_allocate.kalloc_type_view_2662
+ jobj_allocate.kalloc_type_view_2666
+ jobj_allocate.kalloc_type_view_2672
+ jobj_allocate.kalloc_type_view_2676
+ jobj_allocate.kalloc_type_view_2682
+ jobj_allocate.kalloc_type_view_2685
+ jobj_allocate.kalloc_type_view_2688
+ jobj_allocate.kalloc_type_view_2698
+ jobj_allocate.kalloc_type_view_2701
+ jobj_allocate.kalloc_type_view_2711
+ jobj_allocate.kalloc_type_view_2714
+ jobj_allocate.kalloc_type_view_2723
+ jobj_allocate.kalloc_type_view_2726
+ jobj_allocate.kalloc_type_view_2729
+ jobj_release.kalloc_type_view_2751
+ jobj_release.kalloc_type_view_2754
+ jobj_release.kalloc_type_view_2757
+ jobj_release.kalloc_type_view_2766
+ jobj_release.kalloc_type_view_2769
+ jobj_release.kalloc_type_view_2786
+ jobj_release.kalloc_type_view_2789
+ jobj_release.kalloc_type_view_2806
+ jobj_release.kalloc_type_view_2816
+ jobj_release.kalloc_type_view_2820
+ jobj_release.kalloc_type_view_2826
+ legacy_get_ek.kalloc_type_view_34842
+ lookup_unfoldable_name_iterator.kalloc_type_view_18002
+ lookup_unfoldable_name_iterator.kalloc_type_view_18008
+ lookup_unfoldable_name_iterator.kalloc_type_view_18020
+ simple_remove_xattr.kalloc_type_view_23346
+ simple_remove_xattr.kalloc_type_view_23359
+ xattr_cloner.kalloc_type_view_16641
+ xattr_cloner.kalloc_type_view_16684
+ xattr_ek_to_crypto_state.kalloc_type_view_34035
- _fs_add_xattr.kalloc_type_view_23180
- _fs_add_xattr.kalloc_type_view_23186
- _fs_add_xattr.kalloc_type_view_23189
- _fs_add_xattr.kalloc_type_view_23243
- _fs_add_xattr.kalloc_type_view_23244
- apfs_punch_out_ranges_in_fext.kalloc_type_view_21475
- apfs_punch_out_ranges_in_fext.kalloc_type_view_21482
- apfs_update_reserved_ranges.kalloc_type_view_21618
- apfs_update_reserved_ranges.kalloc_type_view_21623
- arle_alloc_pending_entry.kalloc_type_view_21060
- bt_merge_up.kalloc_type_view_4552
- bt_merge_up.kalloc_type_view_4665
- btree_evict_range.kalloc_type_view_6950
- btree_evict_range.kalloc_type_view_6957
- btree_evict_range.kalloc_type_view_7101
- btree_iterate_nodes.kalloc_type_view_6390
- btree_iterate_nodes.kalloc_type_view_6539
- change_crypto_id_prot_class.kalloc_type_view_9835
- change_crypto_id_prot_class.kalloc_type_view_9901
- clone_fexts_.kalloc_type_view_14302
- clone_fexts_.kalloc_type_view_14315
- clone_fexts_.kalloc_type_view_14373
- create_new_crypto_state_for_id.kalloc_type_view_7639
- create_new_crypto_state_for_id.kalloc_type_view_7644
- create_new_crypto_state_for_id.kalloc_type_view_7664
- create_sibling_link.kalloc_type_view_11483
- create_sibling_link.kalloc_type_view_11499
- dir_rec_alloc_with_hash.kalloc_type_view_11118
- dir_rec_alloc_with_hash.kalloc_type_view_11124
- dir_rec_alloc_with_hash.kalloc_type_view_11148
- dump_extents_of_stream.kalloc_type_view_18550
- ek_to_crypto_state.kalloc_type_view_33363
- er_state_allocate_roll_buffers.kalloc_type_view_8176
- er_state_destroy_obj.kalloc_type_view_8820
- er_state_free_roll_buffers.kalloc_type_view_8138
- er_state_obj_create_phys_from_previous_version.kalloc_type_view_8218
- er_state_upgrade_version.kalloc_type_view_8371
- extent_evict_range.kalloc_type_view_25901
- extent_evict_range.kalloc_type_view_26001
- fext_collector.kalloc_type_view_14061
- fext_collector_cleanup.kalloc_type_view_14043
- fext_collector_reset.kalloc_type_view_14032
- free_linkids.kalloc_type_view_11675
- fs_get_xattr_ext.kalloc_type_view_23284
- fs_get_xattr_ext.kalloc_type_view_23304
- fs_init_bootcache_inodes_dstreams_info.kalloc_type_view_27854
- fs_iterate_snapshots.kalloc_type_view_27067
- fs_iterate_snapshots.kalloc_type_view_27114
- fs_map_file_offset_ext.kalloc_type_view_22030
- fs_map_file_offset_ext.kalloc_type_view_22062
- fs_map_file_offset_ext.kalloc_type_view_22100
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23381
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23397
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23418
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23538
- icp_new_crypto.kalloc_type_view_7958
- icp_new_crypto.kalloc_type_view_7968
- icp_new_crypto.kalloc_type_view_7970
- icp_new_crypto.kalloc_type_view_8004
- icp_new_crypto.kalloc_type_view_8029
- icp_new_crypto.kalloc_type_view_8044
- insert_linkid.kalloc_type_view_11623
- jobj_allocate.kalloc_type_view_2652
- jobj_allocate.kalloc_type_view_2655
- jobj_allocate.kalloc_type_view_2665
- jobj_allocate.kalloc_type_view_2669
- jobj_allocate.kalloc_type_view_2675
- jobj_allocate.kalloc_type_view_2678
- jobj_allocate.kalloc_type_view_2681
- jobj_allocate.kalloc_type_view_2684
- jobj_allocate.kalloc_type_view_2687
- jobj_allocate.kalloc_type_view_2697
- jobj_allocate.kalloc_type_view_2707
- jobj_allocate.kalloc_type_view_2716
- jobj_allocate.kalloc_type_view_2719
- jobj_allocate.kalloc_type_view_2722
- jobj_release.kalloc_type_view_2744
- jobj_release.kalloc_type_view_2747
- jobj_release.kalloc_type_view_2750
- jobj_release.kalloc_type_view_2755
- jobj_release.kalloc_type_view_2759
- jobj_release.kalloc_type_view_2768
- jobj_release.kalloc_type_view_2779
- jobj_release.kalloc_type_view_2785
- jobj_release.kalloc_type_view_2809
- jobj_release.kalloc_type_view_2813
- jobj_release.kalloc_type_view_2819
- legacy_get_ek.kalloc_type_view_34818
- lookup_unfoldable_name_iterator.kalloc_type_view_17987
- lookup_unfoldable_name_iterator.kalloc_type_view_17993
- lookup_unfoldable_name_iterator.kalloc_type_view_18001
- simple_remove_xattr.kalloc_type_view_23323
- simple_remove_xattr.kalloc_type_view_23336
- xattr_cloner.kalloc_type_view_16634
- xattr_cloner.kalloc_type_view_16677
- xattr_ek_to_crypto_state.kalloc_type_view_34011
Functions:
~ _jobj_validate_key_val : 656 -> 680
~ _fs_lookup_name_with_parent_id : 732 -> 756
~ _lookup_unfoldable_name_iterator : 620 -> 624
~ _fs_obj_clone_name_checked : 2956 -> 2960
~ _btree_node_compact : 1316 -> 1748
~ _spaceman_modify_bits : 3784 -> 3840
~ _spaceman_resize : 7156 -> 7168
~ _spaceman_iterate_free_extents_internal : 6864 -> 6940
~ _spaceman_alloc_iterate_chunks : 4756 -> 4984
CStrings:
+ "2026/09/17"
+ "2811.160.7.702.4"
+ "apfs-2811.160.7.702.4"
+ "btree_node_compact"
- "2026/08/21"
- "2811.160.7.701.3"
- "apfs-2811.160.7.701.3"
```
