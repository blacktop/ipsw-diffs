## com.apple.filesystems.apfs

> `com.apple.filesystems.apfs`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-3283.0.9.501.1
+3283.0.13.501.1
   __TEXT.__const: 0xa00
-  __TEXT.__cstring: 0x54be1
-  __TEXT_EXEC.__text: 0x164344
-  __TEXT_EXEC.__auth_stubs: 0x2600
+  __TEXT.__cstring: 0x54fb4
+  __TEXT_EXEC.__text: 0x165000
+  __TEXT_EXEC.__auth_stubs: 0x2630
   __DATA.__data: 0x764
   __DATA.__bss: 0xb90
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__kalloc_type: 0x6040
   __DATA_CONST.__kalloc_var: 0x2c60
   __DATA_CONST.__assert: 0x294
-  __DATA_CONST.__auth_got: 0x1300
+  __DATA_CONST.__auth_got: 0x1318
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2504
-  Symbols:   4567
-  CStrings:  7307
+  Functions: 2507
+  Symbols:   4573
+  CStrings:  7323
 
Symbols:
+ __ZL8get_apfsjP2nxPP4apfs
+ __ZZ21delta_teardown_threadPviE22kalloc_type_view_10079
+ __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13473
+ __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13483
+ __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13505
+ __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_8957
+ __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_9074
+ __ZZN15AppleAPFSVolume27asyncCryptoReadFinishHelperEP24multikey_crypto_io_entryPyE21kalloc_type_view_9113
+ __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14947
+ __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14950
+ __ZZN18AppleAPFSContainer19deltaCreateTeardownEP18delta_create_ctx_tE21kalloc_type_view_7913
+ __ZZN18AppleAPFSContainer20deltaRestoreTeardownEP19delta_restore_ctx_tE21kalloc_type_view_8107
+ __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14768
+ __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14799
+ __ZZN19AppleAPFSUserClient19methodKeyCacheEvictEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11879
+ __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11292
+ __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11316
+ __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11418
+ __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11447
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10738
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10746
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10747
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10748
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10813
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10816
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10825
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10828
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10836
+ __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10839
+ __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10093
+ __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10103
+ _apfs_should_relax_unwritten_flush
+ _apfs_zerofill_chunk_cb
+ _cluster_update_range_with_callback
+ _cluster_zero
+ _fext_valid
+ _fs_add_xattr.kalloc_type_view_23431
+ _fs_add_xattr.kalloc_type_view_23437
+ _fs_add_xattr.kalloc_type_view_23440
+ _fs_add_xattr.kalloc_type_view_23494
+ _fs_add_xattr.kalloc_type_view_23495
+ _insert_fext
+ _ubc_upl_maxbufsize
+ _update_fext
+ apfs_check_snapshots_extents.kalloc_type_view_2795
+ apfs_check_snapshots_extents.kalloc_type_view_2889
+ apfs_drop_allocated_unwritten_ranges.kalloc_type_view_16829
+ apfs_drop_rangelist_entries.kalloc_type_view_9355
+ apfs_drop_rangelist_entry.kalloc_type_view_9298
+ apfs_find_gaps_in_rangelist.kalloc_type_view_12124
+ apfs_flush_allocated_unwritten_ranges.kalloc_type_view_14143
+ apfs_flush_allocated_unwritten_ranges.kalloc_type_view_14230
+ apfs_io_common.kalloc_type_view_18774
+ apfs_io_common.kalloc_type_view_18785
+ apfs_io_common.kalloc_type_view_18803
+ apfs_io_common.kalloc_type_view_18821
+ apfs_io_common.kalloc_type_view_18841
+ apfs_io_common.kalloc_type_view_18868
+ apfs_io_common.kalloc_type_view_18951
+ apfs_io_common.kalloc_type_view_18972
+ apfs_io_common.kalloc_type_view_18983
+ apfs_io_common.kalloc_type_view_19001
+ apfs_io_common.kalloc_type_view_19020
+ apfs_io_common.kalloc_type_view_19033
+ apfs_io_common.kalloc_type_view_19054
+ apfs_io_common.kalloc_type_view_19066
+ apfs_io_common.kalloc_type_view_19073
+ apfs_iodone.kalloc_type_view_18215
+ apfs_iodone.kalloc_type_view_18254
+ apfs_locked_ids_destroy.kalloc_type_view_158
+ apfs_locked_ids_init.kalloc_type_view_144
+ apfs_punch_out_ranges_in_fext.kalloc_type_view_21726
+ apfs_punch_out_ranges_in_fext.kalloc_type_view_21733
+ apfs_record_intention_to_allocate.kalloc_type_view_9238
+ apfs_release_all_reserved_space.kalloc_type_view_4592
+ apfs_release_io_context.kalloc_type_view_18452
+ apfs_release_io_context.kalloc_type_view_18461
+ apfs_trim_ranges_in_region.kalloc_type_view_17442
+ apfs_update_ranges_on_allocation.kalloc_type_view_17533
+ apfs_update_reserved_ranges.kalloc_type_view_21869
+ apfs_update_reserved_ranges.kalloc_type_view_21874
+ apfs_vnop_blockmap.kalloc_type_view_17867
+ apfs_vnop_blockmap.kalloc_type_view_18148
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19722
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19735
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19792
+ apfs_vnop_getattrlistbulk.kalloc_type_view_19816
+ apfs_vnop_readdir.kalloc_type_view_16455
+ apfs_vnop_readdir.kalloc_type_view_16477
+ apfs_vnop_readdir.kalloc_type_view_16569
+ apfs_vnop_readdir.kalloc_type_view_16579
+ apfs_vnop_readdir.kalloc_type_view_16600
+ arle_alloc_pending_entry.kalloc_type_view_21312
+ btree_evict_range.kalloc_type_view_7003
+ btree_evict_range.kalloc_type_view_7010
+ btree_evict_range.kalloc_type_view_7154
+ btree_iterate_nodes.kalloc_type_view_6443
+ btree_iterate_nodes.kalloc_type_view_6592
+ change_crypto_id_prot_class.kalloc_type_view_9811
+ change_crypto_id_prot_class.kalloc_type_view_9877
+ create_new_crypto_state_for_id.kalloc_type_view_7568
+ create_new_crypto_state_for_id.kalloc_type_view_7573
+ create_new_crypto_state_for_id.kalloc_type_view_7593
+ create_sibling_link.kalloc_type_view_11674
+ create_sibling_link.kalloc_type_view_11690
+ dir_rec_alloc_with_hash.kalloc_type_view_11309
+ dir_rec_alloc_with_hash.kalloc_type_view_11315
+ dir_rec_alloc_with_hash.kalloc_type_view_11339
+ dump_extents_of_stream.kalloc_type_view_18814
+ ek_to_crypto_state.kalloc_type_view_32906
+ er_state_allocate_roll_buffers.kalloc_type_view_8189
+ er_state_destroy_obj.kalloc_type_view_8828
+ er_state_free_roll_buffers.kalloc_type_view_8151
+ er_state_obj_create_phys_from_previous_version.kalloc_type_view_8231
+ er_state_upgrade_version.kalloc_type_view_8384
+ extent_evict_range.kalloc_type_view_26209
+ extent_evict_range.kalloc_type_view_26309
+ fext_collector.kalloc_type_view_14433
+ fext_collector.kalloc_type_view_14440
+ fext_collector_cleanup.kalloc_type_view_14403
+ fext_collector_reset.kalloc_type_view_14392
+ free_linkids.kalloc_type_view_11866
+ fs_get_xattr_ext.kalloc_type_view_23535
+ fs_get_xattr_ext.kalloc_type_view_23555
+ fs_iterate_snapshots.kalloc_type_view_27100
+ fs_iterate_snapshots.kalloc_type_view_27147
+ fs_map_file_offset_ext.kalloc_type_view_22313
+ fs_map_file_offset_ext.kalloc_type_view_22351
+ fs_map_file_offset_ext.kalloc_type_view_22374
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23638
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23660
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23681
+ fs_remove_xattr_with_nstream_inode.kalloc_type_view_23845
+ graft_blockmap_lut_clone.kalloc_type_view_989
+ graft_blockmap_lut_create.kalloc_type_view_903
+ graft_blockmap_lut_release.kalloc_type_view_1105
+ icp_new_crypto.kalloc_type_view_7969
+ icp_new_crypto.kalloc_type_view_7981
+ icp_new_crypto.kalloc_type_view_7983
+ icp_new_crypto.kalloc_type_view_8017
+ icp_new_crypto.kalloc_type_view_8042
+ icp_new_crypto.kalloc_type_view_8057
+ insert_linkid.kalloc_type_view_11814
+ jobj_allocate.kalloc_type_view_2671
+ jobj_allocate.kalloc_type_view_2674
+ jobj_allocate.kalloc_type_view_2688
+ jobj_allocate.kalloc_type_view_2703
+ jobj_allocate.kalloc_type_view_2706
+ jobj_allocate.kalloc_type_view_2713
+ jobj_allocate.kalloc_type_view_2716
+ jobj_allocate.kalloc_type_view_2723
+ jobj_allocate.kalloc_type_view_2726
+ jobj_allocate.kalloc_type_view_2735
+ jobj_allocate.kalloc_type_view_2738
+ jobj_allocate.kalloc_type_view_2741
+ jobj_release.kalloc_type_view_2763
+ jobj_release.kalloc_type_view_2766
+ jobj_release.kalloc_type_view_2769
+ jobj_release.kalloc_type_view_2774
+ jobj_release.kalloc_type_view_2781
+ jobj_release.kalloc_type_view_2787
+ jobj_release.kalloc_type_view_2794
+ jobj_release.kalloc_type_view_2798
+ jobj_release.kalloc_type_view_2801
+ jobj_release.kalloc_type_view_2804
+ jobj_release.kalloc_type_view_2811
+ jobj_release.kalloc_type_view_2818
+ jobj_release.kalloc_type_view_2828
+ jobj_release.kalloc_type_view_2832
+ jobj_release.kalloc_type_view_2838
+ legacy_get_ek.kalloc_type_view_34341
+ lookup_unfoldable_name_iterator.kalloc_type_view_18420
+ lookup_unfoldable_name_iterator.kalloc_type_view_18426
+ lookup_unfoldable_name_iterator.kalloc_type_view_18434
+ nx_block_out_physical_range_internal.kalloc_type_view_4281
+ nx_block_out_physical_range_internal.kalloc_type_view_4335
+ nx_block_out_physical_range_internal.kalloc_type_view_4491
+ nx_debug_unfree_blocked_out_range.kalloc_type_view_3288
+ nx_debug_unfree_blocked_out_range.kalloc_type_view_3362
+ nx_get_minimal_size.kalloc_type_view_5092
+ nx_get_minimal_size.kalloc_type_view_5200
+ simple_remove_xattr.kalloc_type_view_23574
+ simple_remove_xattr.kalloc_type_view_23587
+ update_parent_xattr.kalloc_type_view_20765
+ update_parent_xattr.kalloc_type_view_20895
+ xattr_cloner.kalloc_type_view_17055
+ xattr_cloner.kalloc_type_view_17104
+ xattr_ek_to_crypto_state.kalloc_type_view_33554
- __ZL8get_apfsiP2nxPP4apfs
- __ZZ21delta_teardown_threadPviE22kalloc_type_view_10072
- __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13466
- __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13476
- __ZZL23apfs_keycache_operationPKh13apfs_key_typeiPP3cpxbE22kalloc_type_view_13498
- __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_8950
- __ZZN15AppleAPFSVolume15asyncCryptoReadEP18AppleAPFSContaineryyPyaybE21kalloc_type_view_9067
- __ZZN15AppleAPFSVolume27asyncCryptoReadFinishHelperEP24multikey_crypto_io_entryPyE21kalloc_type_view_9106
- __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14940
- __ZZN18AppleAPFSContainer16lockerDataGetSetEb9klckr_ctxPhyP4taskE22kalloc_type_view_14943
- __ZZN18AppleAPFSContainer19deltaCreateTeardownEP18delta_create_ctx_tE21kalloc_type_view_7906
- __ZZN18AppleAPFSContainer20deltaRestoreTeardownEP19delta_restore_ctx_tE21kalloc_type_view_8100
- __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14761
- __ZZN18AppleAPFSContainer27containerGetKeyLockerRangesEjj9klckr_ctxyPjP20vol_keylocker_rangesE22kalloc_type_view_14792
- __ZZN19AppleAPFSUserClient19methodKeyCacheEvictEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11872
- __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11285
- __ZZN19AppleAPFSUserClient24methodDeltaCreatePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11309
- __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11411
- __ZZN19AppleAPFSUserClient25methodDeltaRestorePrepareEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_11440
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10731
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10732
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10733
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10741
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10806
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10809
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10818
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10821
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10829
- __ZZN19AppleAPFSUserClient28methodVolumeAddUpdateRecordsEPS_PvP25IOExternalMethodArgumentsE22kalloc_type_view_10832
- __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10086
- __ZZN19AppleAPFSUserClient4stopEP9IOServiceE22kalloc_type_view_10096
- _apfs_io_lock_extending_write_to_exclusive
- _fext_assert_fext
- _fs_add_xattr.kalloc_type_view_23359
- _fs_add_xattr.kalloc_type_view_23365
- _fs_add_xattr.kalloc_type_view_23368
- _fs_add_xattr.kalloc_type_view_23422
- _fs_add_xattr.kalloc_type_view_23423
- apfs_check_snapshots_extents.kalloc_type_view_2754
- apfs_check_snapshots_extents.kalloc_type_view_2848
- apfs_drop_allocated_unwritten_ranges.kalloc_type_view_16506
- apfs_drop_rangelist_entries.kalloc_type_view_9354
- apfs_drop_rangelist_entry.kalloc_type_view_9297
- apfs_find_gaps_in_rangelist.kalloc_type_view_12123
- apfs_flush_allocated_unwritten_ranges.kalloc_type_view_13818
- apfs_flush_allocated_unwritten_ranges.kalloc_type_view_13899
- apfs_io_common.kalloc_type_view_18406
- apfs_io_common.kalloc_type_view_18444
- apfs_io_common.kalloc_type_view_18455
- apfs_io_common.kalloc_type_view_18473
- apfs_io_common.kalloc_type_view_18491
- apfs_io_common.kalloc_type_view_18511
- apfs_io_common.kalloc_type_view_18538
- apfs_io_common.kalloc_type_view_18621
- apfs_io_common.kalloc_type_view_18642
- apfs_io_common.kalloc_type_view_18653
- apfs_io_common.kalloc_type_view_18671
- apfs_io_common.kalloc_type_view_18690
- apfs_io_common.kalloc_type_view_18703
- apfs_io_common.kalloc_type_view_18724
- apfs_io_common.kalloc_type_view_18743
- apfs_iodone.kalloc_type_view_17885
- apfs_iodone.kalloc_type_view_17924
- apfs_locked_ids_destroy.kalloc_type_view_150
- apfs_locked_ids_init.kalloc_type_view_136
- apfs_punch_out_ranges_in_fext.kalloc_type_view_21656
- apfs_punch_out_ranges_in_fext.kalloc_type_view_21663
- apfs_record_intention_to_allocate.kalloc_type_view_9237
- apfs_release_all_reserved_space.kalloc_type_view_4591
- apfs_release_io_context.kalloc_type_view_18122
- apfs_release_io_context.kalloc_type_view_18131
- apfs_trim_ranges_in_region.kalloc_type_view_17119
- apfs_update_ranges_on_allocation.kalloc_type_view_17210
- apfs_update_reserved_ranges.kalloc_type_view_21799
- apfs_update_reserved_ranges.kalloc_type_view_21804
- apfs_vnop_blockmap.kalloc_type_view_17544
- apfs_vnop_blockmap.kalloc_type_view_17818
- apfs_vnop_getattrlistbulk.kalloc_type_view_19392
- apfs_vnop_getattrlistbulk.kalloc_type_view_19405
- apfs_vnop_getattrlistbulk.kalloc_type_view_19462
- apfs_vnop_getattrlistbulk.kalloc_type_view_19486
- apfs_vnop_readdir.kalloc_type_view_16132
- apfs_vnop_readdir.kalloc_type_view_16154
- apfs_vnop_readdir.kalloc_type_view_16246
- apfs_vnop_readdir.kalloc_type_view_16256
- apfs_vnop_readdir.kalloc_type_view_16277
- arle_alloc_pending_entry.kalloc_type_view_21242
- btree_evict_range.kalloc_type_view_6995
- btree_evict_range.kalloc_type_view_7002
- btree_evict_range.kalloc_type_view_7146
- btree_iterate_nodes.kalloc_type_view_6435
- btree_iterate_nodes.kalloc_type_view_6584
- change_crypto_id_prot_class.kalloc_type_view_9741
- change_crypto_id_prot_class.kalloc_type_view_9807
- create_new_crypto_state_for_id.kalloc_type_view_7552
- create_new_crypto_state_for_id.kalloc_type_view_7557
- create_new_crypto_state_for_id.kalloc_type_view_7577
- create_sibling_link.kalloc_type_view_11604
- create_sibling_link.kalloc_type_view_11620
- dir_rec_alloc_with_hash.kalloc_type_view_11239
- dir_rec_alloc_with_hash.kalloc_type_view_11245
- dir_rec_alloc_with_hash.kalloc_type_view_11269
- dump_extents_of_stream.kalloc_type_view_18744
- ek_to_crypto_state.kalloc_type_view_32834
- er_state_allocate_roll_buffers.kalloc_type_view_8173
- er_state_destroy_obj.kalloc_type_view_8812
- er_state_free_roll_buffers.kalloc_type_view_8135
- er_state_obj_create_phys_from_previous_version.kalloc_type_view_8215
- er_state_upgrade_version.kalloc_type_view_8368
- extent_evict_range.kalloc_type_view_26137
- extent_evict_range.kalloc_type_view_26237
- fext_collector.kalloc_type_view_14363
- fext_collector.kalloc_type_view_14370
- fext_collector_cleanup.kalloc_type_view_14333
- fext_collector_reset.kalloc_type_view_14322
- free_linkids.kalloc_type_view_11796
- fs_get_xattr_ext.kalloc_type_view_23463
- fs_get_xattr_ext.kalloc_type_view_23483
- fs_iterate_snapshots.kalloc_type_view_27028
- fs_iterate_snapshots.kalloc_type_view_27075
- fs_map_file_offset_ext.kalloc_type_view_22211
- fs_map_file_offset_ext.kalloc_type_view_22243
- fs_map_file_offset_ext.kalloc_type_view_22304
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23566
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23588
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23609
- fs_remove_xattr_with_nstream_inode.kalloc_type_view_23773
- graft_blockmap_lut_clone.kalloc_type_view_984
- graft_blockmap_lut_create.kalloc_type_view_898
- graft_blockmap_lut_release.kalloc_type_view_1100
- icp_new_crypto.kalloc_type_view_7953
- icp_new_crypto.kalloc_type_view_7965
- icp_new_crypto.kalloc_type_view_7967
- icp_new_crypto.kalloc_type_view_8001
- icp_new_crypto.kalloc_type_view_8026
- icp_new_crypto.kalloc_type_view_8041
- insert_linkid.kalloc_type_view_11744
- jobj_allocate.kalloc_type_view_2655
- jobj_allocate.kalloc_type_view_2658
- jobj_allocate.kalloc_type_view_2662
- jobj_allocate.kalloc_type_view_2668
- jobj_allocate.kalloc_type_view_2672
- jobj_allocate.kalloc_type_view_2681
- jobj_allocate.kalloc_type_view_2687
- jobj_allocate.kalloc_type_view_2690
- jobj_allocate.kalloc_type_view_2707
- jobj_allocate.kalloc_type_view_2719
- jobj_allocate.kalloc_type_view_2722
- jobj_allocate.kalloc_type_view_2725
- jobj_release.kalloc_type_view_2747
- jobj_release.kalloc_type_view_2750
- jobj_release.kalloc_type_view_2753
- jobj_release.kalloc_type_view_2758
- jobj_release.kalloc_type_view_2762
- jobj_release.kalloc_type_view_2765
- jobj_release.kalloc_type_view_2771
- jobj_release.kalloc_type_view_2782
- jobj_release.kalloc_type_view_2785
- jobj_release.kalloc_type_view_2788
- jobj_release.kalloc_type_view_2795
- jobj_release.kalloc_type_view_2802
- jobj_release.kalloc_type_view_2812
- jobj_release.kalloc_type_view_2816
- jobj_release.kalloc_type_view_2822
- legacy_get_ek.kalloc_type_view_34269
- lookup_unfoldable_name_iterator.kalloc_type_view_18350
- lookup_unfoldable_name_iterator.kalloc_type_view_18356
- lookup_unfoldable_name_iterator.kalloc_type_view_18364
- nx_block_out_physical_range_internal.kalloc_type_view_4236
- nx_block_out_physical_range_internal.kalloc_type_view_4290
- nx_block_out_physical_range_internal.kalloc_type_view_4446
- nx_debug_unfree_blocked_out_range.kalloc_type_view_3243
- nx_debug_unfree_blocked_out_range.kalloc_type_view_3317
- nx_get_minimal_size.kalloc_type_view_5047
- nx_get_minimal_size.kalloc_type_view_5155
- simple_remove_xattr.kalloc_type_view_23502
- simple_remove_xattr.kalloc_type_view_23515
- update_parent_xattr.kalloc_type_view_20435
- update_parent_xattr.kalloc_type_view_20565
- xattr_cloner.kalloc_type_view_16985
- xattr_cloner.kalloc_type_view_17034
- xattr_ek_to_crypto_state.kalloc_type_view_33482
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s head RMW failed (%d) for ino %llu @ [%lld, %lld)\n"
+ "%s:%d: %s ino %llu, failed to update cluster range, %llu+%llu, fsize %llu, error %d\n"
+ "%s:%d: %s ino %llu, failed to zero-fill range, %llu+%llu, fsize %llu, error %d\n"
+ "%s:%d: %s ino %llu: fs_map_file_offset() returned %llu:%llu (%llu) but that does not cover %llu:%llu (map_flags 0x%x; dstream %llu/%llu\n"
+ "%s:%d: %s invalid zero-fill range for ino %llu, start %llu, length %llu, fsize %llu\n"
+ "%s:%d: %s partial unwritten coverage for ino %llu, page [%lld, %lld), range [%llu, %llu)\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "%s:%d: %s tail RMW failed (%d) for ino %llu @ [%lld, %lld)\n"
+ "%s:%d: %s ubc_create_upl failed for ino %llu @ [%lld, %lld)\n"
+ "%s:%d: %s zero-fill bitmap alloc failed for ino %llu, pages %u\n"
+ "%s:%d: Failed to fetch BSD name, (temp name is %s), dangling mounts will not be unmounted\n"
+ "%s:%d: Failed to start unmount dangling thread for container %s, error %d"
+ "%s:%d: obj is NULL or not apfs object!\n"
+ "(fext_valid(fext, apfs_get_block_size(apfs)))"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SU3QMB/Sources/apfs/kext/apfs_filter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SU3QMB/Sources/apfs/kext/apfs_vnops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SU3QMB/Sources/apfs/nx/jobj.c"
+ "2026/07/14"
+ "21:20:25"
+ "21:20:26"
+ "3283.0.13.501.1"
+ "Jul 14 2026"
+ "apfs-3283.0.13.501.1"
+ "apfs_sanity_check"
+ "apfs_zerofill_chunk_cb"
+ "apfs_zerofill_unwritten_range"
+ "fext_valid(fext, apfs_get_block_size(apfs))"
- "\"ino %lld: fs_map_file_offset() returned %lld:%lld (%lld) but that does not cover %lld:%lld (map_flags 0x%x; dstream %lld/%lld\\n\" @%s:%d"
- "%s:%d: %s cluster_push() after msync failed with %d on ino(%llu)\n"
- "%s:%d: Failed to start unmount dangling thread, error %d"
- "%s:%d: obj is NULL or not apfs object!"
- "(fext_sanitize(fext))"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RMChuP/Sources/apfs/kext/apfs_filter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RMChuP/Sources/apfs/kext/apfs_vnops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RMChuP/Sources/apfs/nx/jobj.c"
- "2026/06/30"
- "20:59:21"
- "3283.0.9.501.1"
- "Jun 30 2026"
- "apfs-3283.0.9.501.1"
```
