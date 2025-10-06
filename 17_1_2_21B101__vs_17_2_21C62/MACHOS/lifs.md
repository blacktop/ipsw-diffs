## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-208.42.1.0.0
-  __TEXT.__os_log: 0x10fa
-  __TEXT.__cstring: 0x1c42
+208.60.13.0.2
+  __TEXT.__os_log: 0x1190
+  __TEXT.__cstring: 0x1d00
   __TEXT.__const: 0x270
-  __TEXT_EXEC.__text: 0x18fc8
-  __TEXT_EXEC.__auth_stubs: 0xe90
+  __TEXT_EXEC.__text: 0x19b2c
+  __TEXT_EXEC.__auth_stubs: 0xf10
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x50
-  __DATA_CONST.__auth_got: 0x748
+  __DATA_CONST.__auth_got: 0x788
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x1670
-  __DATA_CONST.__kalloc_type: 0xac0
-  UUID: 63E8F605-DA40-3E4C-8C5A-3842C591D094
-  Functions: 297
-  Symbols:   2739
-  CStrings:  337
+  __DATA_CONST.__const: 0x1688
+  __DATA_CONST.__kalloc_type: 0xb40
+  UUID: 26620D80-27B5-309E-86FA-905D94596194
+  Functions: 302
+  Symbols:   2784
+  CStrings:  352
 
Symbols:
+ __ZN19AppleLIFSUserClient18methodReclaimReplyEPS_PvP25IOExternalMethodArguments
+ __ZZL24lifs_destroy_iouc_volumeP16lifs_iouc_volumeE20kalloc_type_view_263
+ __ZZN19AppleLIFSUserClient10clientDiedEvE20kalloc_type_view_308
+ __ZZN19AppleLIFSUserClient12initWithTaskEP4taskPvjP12OSDictionaryE20kalloc_type_view_194
+ __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_923
+ _lifs_enable_lowspace_sync_write
+ _lifs_reclaim_done
+ _lifs_reclaim_request_async
+ _lifs_sync_call
+ _lifs_update_freespace
+ _thread_call_allocate_with_options
+ _thread_call_cancel_wait
+ _thread_call_enter
+ _thread_call_free
+ _ubc_create_upl
+ _ubc_upl_range_needed
+ _upl_dirty_page
+ _upl_page_present
+ _vfs_isunmount
+ add_sillyrename_entry.kalloc_type_view_1850
+ add_sillyrename_entry.kalloc_type_view_1873
+ cleanup_sillyrename_entries.kalloc_type_view_1962
+ get_lifs_mount_from_node._os_log_fmt.16
+ lifs_create_endio_context.kalloc_type_view_853
+ lifs_create_node._os_log_fmt.11
+ lifs_create_node.kalloc_type_view_469
+ lifs_create_node.kalloc_type_view_622
+ lifs_destroy_endio_context.kalloc_type_view_872
+ lifs_enable_lowspace_sync_write._os_log_fmt
+ lifs_endio_thread._os_log_fmt.65
+ lifs_io_strategy_thread._os_log_fmt.63
+ lifs_koio_done.kalloc_type_view_1835
+ lifs_mirror_mount_domount.kalloc_type_view_1136
+ lifs_mirror_mount_domount.kalloc_type_view_1187
+ lifs_mount.kalloc_type_view_549
+ lifs_mount.kalloc_type_view_575
+ lifs_mount.kalloc_type_view_576
+ lifs_mount.kalloc_type_view_718
+ lifs_mount.kalloc_type_view_754
+ lifs_mount.kalloc_type_view_758
+ lifs_mount.kalloc_type_view_762
+ lifs_query_mountpoint._os_log_fmt
+ lifs_reclaim_done.kalloc_type_view_4103
+ lifs_setup_mount_for_koio._os_log_fmt.103
+ lifs_submit_io.kalloc_type_view_1806
+ lifs_submit_koio.kalloc_type_view_1860
+ lifs_unmount.kalloc_type_view_877
+ lifs_update_freespace._os_log_fmt
+ lifs_vnop_getxattr._os_log_fmt.41
+ lifs_vnop_mkdir._os_log_fmt.33
+ lifs_vnop_mmap._os_log_fmt.26
+ lifs_vnop_pagein._os_log_fmt
+ lifs_vnop_readdir._os_log_fmt.11
+ lifs_vnop_readdir._os_log_fmt.13
+ lifs_vnop_readdir._os_log_fmt.15
+ lifs_vnop_readdir._os_log_fmt.22
+ lifs_vnop_readdir._os_log_fmt.23
+ lifs_vnop_readdir._os_log_fmt.9
+ lifs_vnop_readdir.kalloc_type_view_2529
+ lifs_vnop_readdir.kalloc_type_view_2531
+ lifs_vnop_readdir.kalloc_type_view_2613
+ lifs_vnop_readdir.kalloc_type_view_2615
+ lifs_vnop_reclaim.kalloc_type_view_4147
+ lifs_vnop_reclaim.kalloc_type_view_4199
+ lifs_vnop_strategy.kalloc_type_view_1917
+ lifs_vnop_strategy_done.kalloc_type_view_1670
+ move_sillyrename_entries.kalloc_type_view_1936
+ update_lnode_attr_locked._os_log_fmt
- __ZZL24lifs_destroy_iouc_volumeP16lifs_iouc_volumeE20kalloc_type_view_262
- __ZZN19AppleLIFSUserClient10clientDiedEvE20kalloc_type_view_307
- __ZZN19AppleLIFSUserClient12initWithTaskEP4taskPvjP12OSDictionaryE20kalloc_type_view_193
- __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_909
- _lck_rw_try_lock
- _lifs_flush_async_endio
- add_sillyrename_entry.kalloc_type_view_1838
- add_sillyrename_entry.kalloc_type_view_1861
- cleanup_sillyrename_entries.kalloc_type_view_1950
- get_lifs_mount_from_node._os_log_fmt.15
- lifs_create_endio_context.kalloc_type_view_699
- lifs_create_node._os_log_fmt.10
- lifs_create_node.kalloc_type_view_472
- lifs_create_node.kalloc_type_view_610
- lifs_destroy_endio_context.kalloc_type_view_718
- lifs_endio_thread._os_log_fmt.59
- lifs_io_strategy_thread._os_log_fmt.57
- lifs_koio_done.kalloc_type_view_1678
- lifs_mirror_mount_domount.kalloc_type_view_1124
- lifs_mirror_mount_domount.kalloc_type_view_1175
- lifs_mount.kalloc_type_view_518
- lifs_mount.kalloc_type_view_544
- lifs_mount.kalloc_type_view_545
- lifs_mount.kalloc_type_view_679
- lifs_mount.kalloc_type_view_711
- lifs_mount.kalloc_type_view_715
- lifs_mount.kalloc_type_view_719
- lifs_setup_mount_for_koio._os_log_fmt.100
- lifs_submit_io.kalloc_type_view_1649
- lifs_submit_koio.kalloc_type_view_1703
- lifs_unmount.kalloc_type_view_828
- lifs_vnop_getxattr._os_log_fmt.35
- lifs_vnop_mkdir._os_log_fmt.29
- lifs_vnop_mmap._os_log_fmt.23
- lifs_vnop_mnomap._os_log_fmt
- lifs_vnop_readdir._os_log_fmt.10
- lifs_vnop_readdir._os_log_fmt.12
- lifs_vnop_readdir._os_log_fmt.17
- lifs_vnop_readdir._os_log_fmt.19
- lifs_vnop_readdir._os_log_fmt.6
- lifs_vnop_readdir._os_log_fmt.8
- lifs_vnop_readdir.kalloc_type_view_2354
- lifs_vnop_readdir.kalloc_type_view_2356
- lifs_vnop_readdir.kalloc_type_view_2438
- lifs_vnop_readdir.kalloc_type_view_2440
- lifs_vnop_reclaim.kalloc_type_view_3943
- lifs_vnop_strategy.kalloc_type_view_1760
- lifs_vnop_strategy_done.kalloc_type_view_1513
- move_sillyrename_entries.kalloc_type_view_1924
CStrings:
+ "\"%s: page %d is NOT dirty!\" @%s:%d"
+ "%s: lmp %p freespace 0x%llx"
+ "%s: lmp %p freespace 0x%llx sync write disabled"
+ "%s: lmp %p freespace 0x%llx sync write enabled"
+ "%s: pagein called with UPL created"
+ "%s: pageout called with UPL created"
+ "11122222222222222222222222222222222222222222222222332222122222222222221211111111122222222222222221222222122"
+ "112112232"
+ "122"
+ "22222222222222222222222221111222222222222222222222222222221112222112222222122222222222222222222222221221122"
+ "Unexpected attribute type changed from %d to %d"
+ "_N_f_bavail"
+ "_N_f_bsize"
+ "lifs_enable_lowspace_sync_write"
+ "lifs_query_mountpoint"
+ "lifs_update_freespace"
+ "lifs_vnop_pagein"
+ "site.lifs_reclaim_context_t"
- "11122222222222222222222222222222222222222222222222332222122222222222221211111111122222222222222221222222"
- "11211221"
- "22222222222222222222111122222222222222222222222222222221112222112222222122222222222222222222222221221122"

```
