## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

```diff

-3283.0.13.501.1
+3288.1.3.0.0
   __TEXT.__const: 0xa00
-  __TEXT.__cstring: 0x54fb4
-  __TEXT_EXEC.__text: 0x165000
+  __TEXT.__cstring: 0x54fb1
+  __TEXT_EXEC.__text: 0x164bf8
   __TEXT_EXEC.__auth_stubs: 0x2630
   __DATA.__data: 0x764
   __DATA.__bss: 0xb90

   __DATA_CONST.__auth_got: 0x1318
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2507
-  Symbols:   4573
-  CStrings:  7323
+  Functions: 2502
+  Symbols:   4569
+  CStrings:  7317
 
Symbols:
+ _decrement_dstream_id_for_deletion_ex
+ _fs_add_xattr.kalloc_type_view_23450
+ _fs_add_xattr.kalloc_type_view_23456
+ _fs_add_xattr.kalloc_type_view_23459
+ _fs_add_xattr.kalloc_type_view_23513
+ _fs_add_xattr.kalloc_type_view_23514
+ _size_tracking_untrack_inode
+ apfs_find_gaps_in_rangelist.kalloc_type_view_12125
+ apfs_flush_allocated_unwritten_ranges.kalloc_type_view_14138
+ apfs_io_common.kalloc_type_view_18737
+ apfs_io_common.kalloc_type_view_18775
+ apfs_io_common.kalloc_type_view_18786
+ apfs_io_common.kalloc_type_view_18804
+ apfs_io_common.kalloc_type_view_18822
+ apfs_io_common.kalloc_type_view_18842
+ apfs_io_common.kalloc_type_view_18869
+ apfs_io_common.kalloc_type_view_18952
+ apfs_io_common.kalloc_type_view_18973
+ apfs_io_common.kalloc_type_view_18984
+ apfs_io_common.kalloc_type_view_19002
+ apfs_io_common.kalloc_type_view_19021
+ apfs_io_common.kalloc_type_view_19034
+ apfs_io_common.kalloc_type_view_19055
+ apfs_io_common.kalloc_type_view_19067
+ apfs_io_common.kalloc_type_view_19074
+ apfs_punch_out_ranges_in_fext.kalloc_type_view_21745
+ apfs_punch_out_ranges_in_fext.kalloc_type_view_21752
+ apfs_release_io_context.kalloc_type_view_18462
+ apfs_update_reserved_ranges.kalloc_type_view_21888
+ apfs_update_reserved_ranges.kalloc_type_view_21893
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19723
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19736
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19793
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19817
+ arle_alloc_pending_entry.kalloc_type_view_21331
+ btree_evict_range.kalloc_type_view_7005
+ btree_evict_range.kalloc_type_view_7012
+ btree_evict_range.kalloc_type_view_7156
+ btree_iterate_nodes.kalloc_type_view_6445
+ btree_iterate_nodes.kalloc_type_view_6594
+ change_crypto_id_prot_class.kalloc_type_view_9813
+ change_crypto_id_prot_class.kalloc_type_view_9879
+ clone_fs.kalloc_type_view_2455
+ clone_fs.kalloc_type_view_2475
+ create_new_crypto_state_for_id.kalloc_type_view_7570
+ create_new_crypto_state_for_id.kalloc_type_view_7575
+ create_new_crypto_state_for_id.kalloc_type_view_7595
+ create_sibling_link.kalloc_type_view_11676
+ create_sibling_link.kalloc_type_view_11692
+ dir_rec_alloc_with_hash.kalloc_type_view_11311
+ dir_rec_alloc_with_hash.kalloc_type_view_11317
+ dir_rec_alloc_with_hash.kalloc_type_view_11341
+ dstream_evict_range.evict_pause_count
+ dump_extents_of_stream.kalloc_type_view_18833
+ ek_to_crypto_state.kalloc_type_view_32945
+ er_state_allocate_roll_buffers.kalloc_type_view_8191
+ er_state_destroy_obj.kalloc_type_view_8830
+ er_state_free_roll_buffers.kalloc_type_view_8153
+ er_state_obj_create_phys_from_previous_version.kalloc_type_view_8233
+ er_state_upgrade_version.kalloc_type_view_8386
+ extent_evict_range.kalloc_type_view_26228
+ extent_evict_range.kalloc_type_view_26328
+ fext_collector.kalloc_type_view_14435
+ fext_collector.kalloc_type_view_14442
+ fext_collector_cleanup.kalloc_type_view_14405
+ fext_collector_reset.kalloc_type_view_14394
+ free_linkids.kalloc_type_view_11868
+ fs_calculate_snapshot_range_space_usage.kalloc_type_view_2133
+ fs_calculate_snapshot_range_space_usage.kalloc_type_view_2205
+ fs_get_shared_extents.kalloc_type_view_2238
+ fs_get_shared_extents.kalloc_type_view_2316
+ fs_get_xattr_ext.kalloc_type_view_23554
+ fs_get_xattr_ext.kalloc_type_view_23574
+ fs_iterate_snapshots.kalloc_type_view_27139
+ fs_iterate_snapshots.kalloc_type_view_27186
+ fs_map_file_offset_ext.kalloc_type_view_22300
+ fs_map_file_offset_ext.kalloc_type_view_22332
+ fs_map_file_offset_ext.kalloc_type_view_22370
+ fs_map_file_offset_ext.kalloc_type_view_22393
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23657
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23679
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23700
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23864
+ handle_snapshot_lookup.kalloc_type_view_9525
+ handle_xdstream_obj_id.kalloc_type_view_13145
+ handle_xdstream_obj_id.kalloc_type_view_13168
+ icp_new_crypto.kalloc_type_view_7971
+ icp_new_crypto.kalloc_type_view_7985
+ icp_new_crypto.kalloc_type_view_8019
+ icp_new_crypto.kalloc_type_view_8044
+ icp_new_crypto.kalloc_type_view_8059
+ insert_linkid.kalloc_type_view_11816
+ jobj_allocate.kalloc_type_view_2673
+ jobj_allocate.kalloc_type_view_2676
+ jobj_allocate.kalloc_type_view_2680
+ jobj_allocate.kalloc_type_view_2686
+ jobj_allocate.kalloc_type_view_2690
+ jobj_allocate.kalloc_type_view_2696
+ jobj_allocate.kalloc_type_view_2699
+ jobj_allocate.kalloc_type_view_2702
+ jobj_allocate.kalloc_type_view_2705
+ jobj_allocate.kalloc_type_view_2708
+ jobj_allocate.kalloc_type_view_2712
+ jobj_allocate.kalloc_type_view_2715
+ jobj_allocate.kalloc_type_view_2718
+ jobj_allocate.kalloc_type_view_2725
+ jobj_allocate.kalloc_type_view_2728
+ jobj_allocate.kalloc_type_view_2737
+ jobj_allocate.kalloc_type_view_2740
+ jobj_allocate.kalloc_type_view_2743
+ jobj_release.kalloc_type_view_2765
+ jobj_release.kalloc_type_view_2768
+ jobj_release.kalloc_type_view_2771
+ jobj_release.kalloc_type_view_2776
+ jobj_release.kalloc_type_view_2780
+ jobj_release.kalloc_type_view_2783
+ jobj_release.kalloc_type_view_2789
+ jobj_release.kalloc_type_view_2796
+ jobj_release.kalloc_type_view_2800
+ jobj_release.kalloc_type_view_2803
+ jobj_release.kalloc_type_view_2806
+ jobj_release.kalloc_type_view_2813
+ jobj_release.kalloc_type_view_2820
+ jobj_release.kalloc_type_view_2830
+ jobj_release.kalloc_type_view_2834
+ jobj_release.kalloc_type_view_2840
+ legacy_get_ek.kalloc_type_view_34380
+ lookup_purgeable_drec_as_record.kalloc_type_view_1340
+ lookup_unfoldable_name_iterator.kalloc_type_view_18439
+ lookup_unfoldable_name_iterator.kalloc_type_view_18445
+ lookup_unfoldable_name_iterator.kalloc_type_view_18453
+ nx_unmount_internal.kalloc_type_view_1820
+ orphan_snap_check_iterator.kalloc_type_view_1923
+ purge_files_with_ino.kalloc_type_view_8372
+ purge_files_with_ino.kalloc_type_view_8382
+ purge_files_with_ino.kalloc_type_view_8625
+ purge_single_file.kalloc_type_view_10891
+ purge_single_file.kalloc_type_view_10895
+ purge_single_file.kalloc_type_view_10897
+ purge_single_file.kalloc_type_view_10936
+ purge_single_file.kalloc_type_view_10937
+ simple_remove_xattr.kalloc_type_view_23593
+ simple_remove_xattr.kalloc_type_view_23606
+ update_parent_xattr.kalloc_type_view_20766
+ update_parent_xattr.kalloc_type_view_20896
+ xattr_cloner.kalloc_type_view_17074
+ xattr_cloner.kalloc_type_view_17123
+ xattr_ek_to_crypto_state.kalloc_type_view_33593
- _apfs_ep_query_ttl
- _crypto_cache_query
- _crypto_obj_query
- _decrement_dstream_id_for_deletion
- _ephemeral_policy_query_fill_stats
- _fs_add_xattr.kalloc_type_view_23431
- _fs_add_xattr.kalloc_type_view_23437
- _fs_add_xattr.kalloc_type_view_23440
- _fs_add_xattr.kalloc_type_view_23494
- _fs_add_xattr.kalloc_type_view_23495
- _fs_tx_calc_total_space_required
- _spaceman_device_info
- apfs_find_gaps_in_rangelist.kalloc_type_view_12124
- apfs_flush_allocated_unwritten_ranges.kalloc_type_view_14143
- apfs_io_common.kalloc_type_view_18736
- apfs_io_common.kalloc_type_view_18774
- apfs_io_common.kalloc_type_view_18785
- apfs_io_common.kalloc_type_view_18803
- apfs_io_common.kalloc_type_view_18821
- apfs_io_common.kalloc_type_view_18841
- apfs_io_common.kalloc_type_view_18868
- apfs_io_common.kalloc_type_view_18951
- apfs_io_common.kalloc_type_view_18972
- apfs_io_common.kalloc_type_view_18983
- apfs_io_common.kalloc_type_view_19001
- apfs_io_common.kalloc_type_view_19020
- apfs_io_common.kalloc_type_view_19033
- apfs_io_common.kalloc_type_view_19054
- apfs_io_common.kalloc_type_view_19066
- apfs_io_common.kalloc_type_view_19073
- apfs_punch_out_ranges_in_fext.kalloc_type_view_21726
- apfs_punch_out_ranges_in_fext.kalloc_type_view_21733
- apfs_release_io_context.kalloc_type_view_18461
- apfs_update_reserved_ranges.kalloc_type_view_21869
- apfs_update_reserved_ranges.kalloc_type_view_21874
- apfs_vnop_getattrlistbulk.kalloc_type_view_19722
- apfs_vnop_getattrlistbulk.kalloc_type_view_19735
- apfs_vnop_getattrlistbulk.kalloc_type_view_19792
- apfs_vnop_getattrlistbulk.kalloc_type_view_19816
- arle_alloc_pending_entry.kalloc_type_view_21312
- btree_evict_range.kalloc_type_view_7003
- btree_evict_range.kalloc_type_view_7010
- btree_evict_range.kalloc_type_view_7154
- btree_iterate_nodes.kalloc_type_view_6443
- btree_iterate_nodes.kalloc_type_view_6592
- change_crypto_id_prot_class.kalloc_type_view_9811
- change_crypto_id_prot_class.kalloc_type_view_9877
- clone_fs.kalloc_type_view_2448
- clone_fs.kalloc_type_view_2468
- create_new_crypto_state_for_id.kalloc_type_view_7568
- create_new_crypto_state_for_id.kalloc_type_view_7573
- create_new_crypto_state_for_id.kalloc_type_view_7593
- create_sibling_link.kalloc_type_view_11674
- create_sibling_link.kalloc_type_view_11690
- dir_rec_alloc_with_hash.kalloc_type_view_11309
- dir_rec_alloc_with_hash.kalloc_type_view_11315
- dir_rec_alloc_with_hash.kalloc_type_view_11339
- dump_extents_of_stream.kalloc_type_view_18814
- ek_to_crypto_state.kalloc_type_view_32906
- er_state_allocate_roll_buffers.kalloc_type_view_8189
- er_state_destroy_obj.kalloc_type_view_8828
- er_state_free_roll_buffers.kalloc_type_view_8151
- er_state_obj_create_phys_from_previous_version.kalloc_type_view_8231
- er_state_upgrade_version.kalloc_type_view_8384
- extent_evict_range.kalloc_type_view_26209
- extent_evict_range.kalloc_type_view_26309
- fext_collector.kalloc_type_view_14433
- fext_collector.kalloc_type_view_14440
- fext_collector_cleanup.kalloc_type_view_14403
- fext_collector_reset.kalloc_type_view_14392
- free_linkids.kalloc_type_view_11866
- fs_calculate_snapshot_range_space_usage.kalloc_type_view_2126
- fs_calculate_snapshot_range_space_usage.kalloc_type_view_2198
- fs_get_shared_extents.kalloc_type_view_2231
- fs_get_shared_extents.kalloc_type_view_2309
- fs_get_xattr_ext.kalloc_type_view_23535
- fs_get_xattr_ext.kalloc_type_view_23555
- fs_iterate_snapshots.kalloc_type_view_27100
- fs_iterate_snapshots.kalloc_type_view_27147
- fs_map_file_offset_ext.kalloc_type_view_22281
- fs_map_file_offset_ext.kalloc_type_view_22313
- fs_map_file_offset_ext.kalloc_type_view_22351
- fs_map_file_offset_ext.kalloc_type_view_22374
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23638
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23660
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23681
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23845
- handle_snapshot_lookup.kalloc_type_view_9489
- handle_xdstream_obj_id.kalloc_type_view_13109
- handle_xdstream_obj_id.kalloc_type_view_13132
- icp_new_crypto.kalloc_type_view_7969
- icp_new_crypto.kalloc_type_view_7981
- icp_new_crypto.kalloc_type_view_8017
- icp_new_crypto.kalloc_type_view_8042
- icp_new_crypto.kalloc_type_view_8057
- insert_linkid.kalloc_type_view_11814
- jobj_allocate.kalloc_type_view_2671
- jobj_allocate.kalloc_type_view_2674
- jobj_allocate.kalloc_type_view_2678
- jobj_allocate.kalloc_type_view_2684
- jobj_allocate.kalloc_type_view_2688
- jobj_allocate.kalloc_type_view_2694
- jobj_allocate.kalloc_type_view_2697
- jobj_allocate.kalloc_type_view_2700
- jobj_allocate.kalloc_type_view_2703
- jobj_allocate.kalloc_type_view_2706
- jobj_allocate.kalloc_type_view_2710
- jobj_allocate.kalloc_type_view_2713
- jobj_allocate.kalloc_type_view_2716
- jobj_allocate.kalloc_type_view_2723
- jobj_allocate.kalloc_type_view_2726
- jobj_allocate.kalloc_type_view_2735
- jobj_allocate.kalloc_type_view_2738
- jobj_allocate.kalloc_type_view_2741
- jobj_release.kalloc_type_view_2763
- jobj_release.kalloc_type_view_2766
- jobj_release.kalloc_type_view_2769
- jobj_release.kalloc_type_view_2774
- jobj_release.kalloc_type_view_2778
- jobj_release.kalloc_type_view_2781
- jobj_release.kalloc_type_view_2787
- jobj_release.kalloc_type_view_2794
- jobj_release.kalloc_type_view_2798
- jobj_release.kalloc_type_view_2801
- jobj_release.kalloc_type_view_2804
- jobj_release.kalloc_type_view_2811
- jobj_release.kalloc_type_view_2818
- jobj_release.kalloc_type_view_2828
- jobj_release.kalloc_type_view_2832
- jobj_release.kalloc_type_view_2838
- legacy_get_ek.kalloc_type_view_34341
- lookup_purgeable_drec_as_record.kalloc_type_view_1335
- lookup_unfoldable_name_iterator.kalloc_type_view_18420
- lookup_unfoldable_name_iterator.kalloc_type_view_18426
- lookup_unfoldable_name_iterator.kalloc_type_view_18434
- nx_unmount_internal.kalloc_type_view_1819
- orphan_snap_check_iterator.kalloc_type_view_1916
- purge_files_with_ino.kalloc_type_view_8328
- purge_files_with_ino.kalloc_type_view_8338
- purge_files_with_ino.kalloc_type_view_8581
- purge_single_file.kalloc_type_view_10847
- purge_single_file.kalloc_type_view_10851
- purge_single_file.kalloc_type_view_10853
- purge_single_file.kalloc_type_view_10892
- purge_single_file.kalloc_type_view_10893
- simple_remove_xattr.kalloc_type_view_23574
- simple_remove_xattr.kalloc_type_view_23587
- update_parent_xattr.kalloc_type_view_20765
- update_parent_xattr.kalloc_type_view_20895
- xattr_cloner.kalloc_type_view_17055
- xattr_cloner.kalloc_type_view_17104
- xattr_ek_to_crypto_state.kalloc_type_view_33554
CStrings:
+ "%s:%d: %s (dstream_id %lld, flags %x) made %u evictions retries number of blocks to evict %llu, number of evicted blocks till now %llu\n"
+ "%s:%d: %s (dstream_id %lld, flags %x) throttled-pause fired %u times,number of blocks to evict %llu, number of evicted blocks till now %llu\n"
+ "%s:%d: %s _OP_GET_FILE_DSTREAMS requires the get-dstreams entitlement\n"
+ "%s:%d: %s _OP_GET_FILE_EXTS requires the get-file-exts entitlement\n"
+ "%s:%d: %s done processing snap xid %llu (err %d)\n"
+ "%s:%d: %s failed to find attribution tag record with s_hash <%llu> for already-tagged ino!\n"
+ "%s:%d: extent exceeds checksums buf, idx 0x%llx, len 0x%llx, left 0x%llx\n"
+ "%s:%d: extent exceeds rolled buf, idx 0x%llx, extent_size 0x%llx, buf_size 0x%lx\n"
+ "%s:%d: extent exceeds unrolled buf, idx 0x%llx, len 0x%llx, left 0x%llx\n"
+ "2026/08/11"
+ "21:40:29"
+ "3288.1.3"
+ "Aug 11 2026"
+ "apfs-3288.1.3"
+ "com.apple.private.apfs.get-dstreams"
+ "com.apple.private.apfs.get-file-exts"
+ "decrement_dstream_id_for_deletion_ex"
- " or UNWRITTEN fexts"
- "%s:%d: %s Did not find snap meta in the jhash\n"
- "%s:%d: %s Failed to locate apfs of fsindex %llu, error %d\n"
- "%s:%d: %s Invalid fsoid, for fsindex %llu\n"
- "%s:%d: %s Looking for snapmeta in jhash, fsindex %llu, snapshot_xid %llu\n"
- "%s:%d: %s Snap meta found in jhash\n"
- "%s:%d: %s done processing snap xid %llu\n"
- "%s:%d: %s failed to update existing file info attribution tag record for s_hash <%llu> with <%s> <%d>\n"
- "%s:%d: %s ino %llu, prealloced region %llu+%llu is not covered by a file range%s, covered %llu+%llu, offset %llu\n"
- "%s:%d: %s nx_panic_on_corruption restored to %d\n"
- "%s:%d: %s nx_panic_on_corruption set to false\n"
- "%s:%d: %s nx_panic_on_cp_corruption restored to %d\n"
- "%s:%d: %s nx_panic_on_cp_corruption set to false\n"
- "%s:%d: %s preallocated range %llu+%zu is not covered by UNWRITTEN fexts, error %d\n"
- "2026/07/14"
- "21:20:25"
- "21:20:26"
- "3283.0.13.501.1"
- "Jul 14 2026"
- "apfs-3283.0.13.501.1"
- "check_snap_meta_devt"
- "decrement_dstream_id_for_deletion"
- "ttl"
```
