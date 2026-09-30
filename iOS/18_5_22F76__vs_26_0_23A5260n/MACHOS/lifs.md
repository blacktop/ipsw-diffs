## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-531.120.18.0.2
-  __TEXT.__os_log: 0x12f9
-  __TEXT.__cstring: 0x217f
+737.0.2.0.1
+  __TEXT.__os_log: 0x13b7
+  __TEXT.__cstring: 0x2203
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1b14c
-  __TEXT_EXEC.__auth_stubs: 0xfa0
+  __TEXT_EXEC.__text: 0x1b9b8
+  __TEXT_EXEC.__auth_stubs: 0xfd0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x90
-  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__auth_got: 0x7e8
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x16a0
+  __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__kalloc_type: 0xbc0
-  UUID: 42A35CBF-86AB-3A79-8ED6-3732A38C86A4
-  Functions: 401
-  Symbols:   3040
-  CStrings:  393
+  __DATA_CONST.__kalloc_var: 0xf0
+  UUID: 8BF620AE-FA7C-319D-B712-0C32C851252F
+  Functions: 406
+  Symbols:   3082
+  CStrings:  402
 
Symbols:
+ __ZN19AppleLIFSUserClient16methodEndIOReplyEPS_PvP25IOExternalMethodArguments
+ __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_188
+ __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_208
+ __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_245
+ __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_973
+ _kalloc_type_var_impl
+ _kfree_type_var_impl
+ _lifs_unmount_dangling_all
+ _lifs_unmount_dangling_thread
+ _lifs_wait_for_device_idle
+ _timevalsub
+ _update_lnode_attr_subset
+ _update_lnode_attr_subset_locked
+ add_sillyrename_entry.kalloc_type_view_1944
+ add_sillyrename_entry.kalloc_type_view_1967
+ cleanup_sillyrename_entries.kalloc_type_view_2057
+ lifs_create_endio_context.kalloc_type_view_1080
+ lifs_create_node.kalloc_type_view_434
+ lifs_create_node.kalloc_type_view_589
+ lifs_destroy_endio_context.kalloc_type_view_1099
+ lifs_fsync_internal.kalloc_type_view_3772
+ lifs_getattr._os_log_fmt.26
+ lifs_koio_done.kalloc_type_view_2088
+ lifs_mirror_mount_domount.kalloc_type_view_1164
+ lifs_mirror_mount_domount.kalloc_type_view_1215
+ lifs_mount.kalloc_type_view_629
+ lifs_mount.kalloc_type_view_655
+ lifs_mount.kalloc_type_view_656
+ lifs_mount.kalloc_type_view_828
+ lifs_mount.kalloc_type_view_874
+ lifs_mount.kalloc_type_view_878
+ lifs_mount.kalloc_type_view_882
+ lifs_reclaim_done.kalloc_type_view_4684
+ lifs_req_callback_thread._os_log_fmt.13
+ lifs_request_done._os_log_fmt.6
+ lifs_setattr._os_log_fmt.29
+ lifs_setfsattr_done.kalloc_type_view_3703
+ lifs_setfsattr_request._os_log_fmt.4
+ lifs_setup_mount_for_devvp._os_log_fmt
+ lifs_setup_mount_for_devvp._os_log_fmt.88
+ lifs_setxattr_request._os_log_fmt.9
+ lifs_submit_io.kalloc_type_view_2069
+ lifs_submit_koio.kalloc_type_view_2110
+ lifs_unmount.kalloc_type_view_1017
+ lifs_unmount_dangling_all._os_log_fmt
+ lifs_unmount_dangling_all._os_log_fmt.31
+ lifs_unmount_dangling_all._os_log_fmt.32
+ lifs_unmount_dangling_all.kalloc_type_view_1521
+ lifs_unmount_dangling_all.kalloc_type_view_1542
+ lifs_unmount_dangling_thread.kalloc_type_view_1494
+ lifs_vnop_readdir.kalloc_type_view_2904
+ lifs_vnop_readdir.kalloc_type_view_2906
+ lifs_vnop_readdir.kalloc_type_view_3001
+ lifs_vnop_readdir.kalloc_type_view_3003
+ lifs_vnop_reclaim.kalloc_type_view_4728
+ lifs_vnop_reclaim.kalloc_type_view_4782
+ lifs_vnop_strategy.kalloc_type_view_2167
+ lifs_vnop_strategy_done.kalloc_type_view_1947
+ move_sillyrename_entries.kalloc_type_view_2031
- __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_187
- __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_207
- __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_244
- __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_972
- _lifs_flush_async_io
- add_sillyrename_entry.kalloc_type_view_1977
- add_sillyrename_entry.kalloc_type_view_2000
- cleanup_sillyrename_entries.kalloc_type_view_2090
- lifs_create_endio_context.kalloc_type_view_1071
- lifs_create_node.kalloc_type_view_470
- lifs_create_node.kalloc_type_view_625
- lifs_destroy_endio_context.kalloc_type_view_1090
- lifs_fsync_internal.kalloc_type_view_3703
- lifs_koio_done.kalloc_type_view_2058
- lifs_mirror_mount_domount.kalloc_type_view_1197
- lifs_mirror_mount_domount.kalloc_type_view_1248
- lifs_mount.kalloc_type_view_614
- lifs_mount.kalloc_type_view_640
- lifs_mount.kalloc_type_view_641
- lifs_mount.kalloc_type_view_811
- lifs_mount.kalloc_type_view_857
- lifs_mount.kalloc_type_view_861
- lifs_mount.kalloc_type_view_865
- lifs_reclaim_done.kalloc_type_view_4615
- lifs_req_callback_thread._os_log_fmt.12
- lifs_request_done._os_log_fmt.4
- lifs_setattr._os_log_fmt.28
- lifs_setfsattr_done.kalloc_type_view_3634
- lifs_setfsattr_request._os_log_fmt.3
- lifs_setup_mount_for_koio._os_log_fmt
- lifs_setup_mount_for_koio._os_log_fmt.84
- lifs_setxattr_request._os_log_fmt.8
- lifs_submit_io.kalloc_type_view_2039
- lifs_submit_koio.kalloc_type_view_2080
- lifs_unmount.kalloc_type_view_999
- lifs_vnop_readdir.kalloc_type_view_2835
- lifs_vnop_readdir.kalloc_type_view_2837
- lifs_vnop_readdir.kalloc_type_view_2932
- lifs_vnop_readdir.kalloc_type_view_2934
- lifs_vnop_reclaim.kalloc_type_view_4659
- lifs_vnop_reclaim.kalloc_type_view_4713
- lifs_vnop_strategy.kalloc_type_view_2137
- lifs_vnop_strategy_done.kalloc_type_view_1903
- move_sillyrename_entries.kalloc_type_view_2064
CStrings:
+ "%s: Got block_size = 0. Using the device's block size instead."
+ "%s: failed to find request for op %u with id %llu"
+ "11112222222222222222"
+ "111222222222222222222222222222222222222222222222223322221222222222222222121111111112222222222222222122222221122"
+ "11211223222222222222"
+ "2222222222222222222222222222222222222222222222222222222222222222221111222111222211222222222222222222222222222222212121221122222"
+ "Failed to allocate fsids buffer."
+ "Failed to start unmount dangling thread, kern_return %d"
+ "Found %d dangling mount(s)."
+ "_O_f_preallocate"
+ "lifs_getattr"
+ "lifs_setup_mount_for_devvp"
+ "lifs_unmount_dangling"
+ "lifs_wait_for_device_idle"
+ "site.fsid_t"
- "%s: failed to find request with id %llu"
- "111122222"
- "11122222222222222222222222222222222222222222222222332222122222222222222121111111112222222222222222122222221122"
- "112112232"
- "2222222222222222222222222111122222222222222222222222222222111222211222222212122222222222222222222222221221122"
- "lifs_setup_mount_for_koio"

```
