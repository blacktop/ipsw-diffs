## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

-971.0.0.0.5
-  __TEXT.__os_log: 0x1ec7 sha256:34b6066a9743d534ca4d86771fd6b3939676ea68941c2800207da1840e27929e
-  __TEXT.__cstring: 0x299c sha256:71250e8819beec09b2c77364da258a74dfb625fd2c05d599ded54995c6658da4
-  __TEXT.__const: 0x328 sha256:6402913d77cf547ea97f7ab5fbba4afca7b1a301e196e0bb301db3d775dbdea7
-  __TEXT_EXEC.__text: 0x1ffb0 sha256:5543e2f874eb6f3e2b13c04fc931937103d05d38d1de2716ea86cabf85d5986f
+737.120.9.0.0
+  __TEXT.__os_log: 0x1367 sha256:3e9e17a946c7c8e51f4cba1279d0cb61f7fd0e154242564068d602426d4fb008
+  __TEXT.__cstring: 0x2188 sha256:5c03fc160f64d56b397dffb60bb7afd6427f4aa9996e1a3ab616c7c072e5933a
+  __TEXT.__const: 0x2c0 sha256:b6e22b56d0c269e9acaec0f146694ef9b3c54af7d2b9d250882d7c873554d588
+  __TEXT_EXEC.__text: 0x1ae10 sha256:d5a9ba9e2856db51379d951bdedaf4614babea85d17027b08592f99a8485d8b8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x528 sha256:7c9a75b0eb2b1b57690120b94036a9c228a0f1b699834bbff3e2210910b4c129
+  __DATA.__data: 0x528 sha256:cef0b1eca204a26a3d41d7a4c98a3e7683937ed15deebf3bde198a88f3531ee0
   __DATA.__common: 0x130 sha256:e2fc162ed9124452d23c85e81d60a0c228f414c3214a5de635737e25fbd29ac1
   __DATA.__bss: 0x90 sha256:81c611f35bff79491538b2f7cf201c7597a661a5c549633541c62bdc8af1613f
-  __DATA_CONST.__mod_init_func: 0x18 sha256:94c1013c10d6909ac1581518bb958911020f3c47942c393c28cdc2856e3391df
-  __DATA_CONST.__mod_term_func: 0x18 sha256:df5f90fa53f8868488c8587d1fe741555e5f2941676935633f1b6c5c216641e3
-  __DATA_CONST.__const: 0x2228 sha256:832fc50d2433ac57103fcfb4673bbc9b074eb05de220fcddde647499a0075019
-  __DATA_CONST.__kalloc_type: 0xe40 sha256:3c3307c6c1587aabcaf9fec4bff4327ecaafa25a645dd96871288139798391c1
-  __DATA_CONST.__kalloc_var: 0xf0 sha256:1af884f4049b423d488337da75e5f5bfd3d371fac56eef2c78bfe35fd676c571
-  __DATA_CONST.__auth_got: 0x7c8 sha256:7407741b98b8a059d7fd54c3ff5775d881fb868fb5459dede2e796fab2548030
-  __DATA_CONST.__got: 0x80 sha256:36c070c0c1a98a78e0dcc58bf7b89300bd7c1c7e337ae38e9dab0872adb84741
-  __DATA_CONST.__auth_ptr: 0x8 sha256:72771b12fa9c05b761d9c90250919df72fcc0b8b034b4b65e8720f80c089eb4b
-  UUID: A58B86D3-D758-3509-8B93-1CA9BC7A06F7
-  Functions: 459
-  Symbols:   1402
-  CStrings:  511
+  __DATA_CONST.__auth_got: 0x7b0 sha256:99be2ed6829208cfd03154647a1b59b574104ef9d5088380fc61bf9e141e7da9
+  __DATA_CONST.__got: 0x78 sha256:b1011a6fee6e6c1bad23b8349d52094f99a7246c8d2fc657de731d2942f02a39
+  __DATA_CONST.__auth_ptr: 0x8 sha256:1635989ef4e4f2f4f81397a34b3708bfd0079516f2a752a2ebab6d1e3f8adbc7
+  __DATA_CONST.__mod_init_func: 0x18 sha256:5099a8a5ad0b272046660fd32af2b256977a8e5de15d3551b53c346423f78509
+  __DATA_CONST.__mod_term_func: 0x18 sha256:4c5029efd53b965a27e04e74640fc5ecafbe6b9f4c10ad62aaaf93f9d42d15fd
+  __DATA_CONST.__const: 0x2138 sha256:c4c9302b25da08d0353564fdf77a5d271c23c9206fd9cadeae6283034d76def2
+  __DATA_CONST.__kalloc_type: 0xbc0 sha256:d37e662198a4e7f12e7991b5a93d1284c68d89381f780dccdf5f1d55b07d8805
+  __DATA_CONST.__kalloc_var: 0xf0 sha256:97650e47d88ca1308db035bf1bd6d465c131509860c2ac704bd605699c8970d5
+  UUID: C3104FA3-D37A-3B64-845C-960BA2D3D964
+  Functions: 403
+  Symbols:   1278
+  CStrings:  395
 
Symbols:
+ __ZN19AppleLIFSUserClient19methodCreateMappingEPS_PvP25IOExternalMethodArguments
+ __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_189
+ __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_209
+ __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_246
+ __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_974
+ _lifs_get_extent_layout
+ add_sillyrename_entry.kalloc_type_view_1955
+ add_sillyrename_entry.kalloc_type_view_1978
+ cleanup_sillyrename_entries.kalloc_type_view_2068
+ get_lifs_mount_from_node._os_log_fmt.6
+ lifs_create_endio_context.kalloc_type_view_1081
+ lifs_create_node._os_log_fmt
+ lifs_create_node._os_log_fmt.5
+ lifs_create_node.kalloc_type_view_435
+ lifs_create_node.kalloc_type_view_590
+ lifs_destroy_endio_context.kalloc_type_view_1100
+ lifs_endio_thread._os_log_fmt.47
+ lifs_fsync_internal.kalloc_type_view_3800
+ lifs_getattr._os_log_fmt.26
+ lifs_io_strategy_thread._os_log_fmt.45
+ lifs_koio_blockmap._os_log_fmt.33
+ lifs_koio_done.kalloc_type_view_2099
+ lifs_mirror_mount_domount.kalloc_type_view_1165
+ lifs_mirror_mount_domount.kalloc_type_view_1216
+ lifs_mount.kalloc_type_view_622
+ lifs_mount.kalloc_type_view_648
+ lifs_mount.kalloc_type_view_649
+ lifs_mount.kalloc_type_view_821
+ lifs_mount.kalloc_type_view_867
+ lifs_mount.kalloc_type_view_871
+ lifs_mount.kalloc_type_view_875
+ lifs_pack_attrlist_entry._os_log_fmt.25
+ lifs_reclaim_done.kalloc_type_view_4712
+ lifs_req_callback_thread._os_log_fmt.13
+ lifs_request_done._os_log_fmt.5
+ lifs_request_done._os_log_fmt.6
+ lifs_setattr._os_log_fmt.29
+ lifs_setfsattr_done.kalloc_type_view_3728
+ lifs_setfsattr_request._os_log_fmt.4
+ lifs_setup_mount_for_devvp._os_log_fmt.82
+ lifs_setxattr_request._os_log_fmt.9
+ lifs_submit_io.kalloc_type_view_2080
+ lifs_submit_koio.kalloc_type_view_2121
+ lifs_unmount.kalloc_type_view_1010
+ lifs_unmount_dangling_all._os_log_fmt.31
+ lifs_unmount_dangling_all._os_log_fmt.32
+ lifs_unmount_dangling_all.kalloc_type_view_1504
+ lifs_unmount_dangling_all.kalloc_type_view_1525
+ lifs_unmount_dangling_thread.kalloc_type_view_1477
+ lifs_vnop_readdir.kalloc_type_view_2916
+ lifs_vnop_readdir.kalloc_type_view_2918
+ lifs_vnop_reclaim.kalloc_type_view_4756
+ lifs_vnop_reclaim.kalloc_type_view_4810
+ lifs_vnop_strategy.kalloc_type_view_2180
+ lifs_vnop_strategy_done.kalloc_type_view_1945
+ move_sillyrename_entries.kalloc_type_view_2042
- __ZL26lifs_destroy_pooled_bufferP18lifs_pooled_buffer
- __ZL28lifs_buffer_pool_copy_threadPvi
- __ZN18IOMemoryDescriptor16withAddressRangeEyyjP4task
- __ZN19AppleLIFSUserClient12freeUCMountsEv
- __ZN19AppleLIFSUserClient13addMountEntryEjj
- __ZN19AppleLIFSUserClient13getMountIndexEj
- __ZN19AppleLIFSUserClient15methodSeekReplyEPS_PvP25IOExternalMethodArguments
- __ZN19AppleLIFSUserClient16methodGetMappingEPS_PvP25IOExternalMethodArguments
- __ZN19AppleLIFSUserClient19methodKernelUnmountEPS_PvP25IOExternalMethodArguments
- __ZN19AppleLIFSUserClient19methodSetCacheStateEPS_PvP25IOExternalMethodArguments
- __ZN19AppleLIFSUserClient20methodCloneFileReplyEPS_PvP25IOExternalMethodArguments
- __ZN19AppleLIFSUserClient25methodCacheOperationReplyEPS_PvP25IOExternalMethodArguments
- __ZN19AppleLIFSUserClient28methodCreateNamedStreamReplyEPS_PvP25IOExternalMethodArguments
- __ZN19AppleLIFSUserClient28methodLookupNamedStreamReplyEPS_PvP25IOExternalMethodArguments
- __ZN19AppleLIFSUserClient28methodRemoveNamedStreamReplyEPS_PvP25IOExternalMethodArguments
- __ZN25IOWrappedMemoryDescriptor16getCachedMappingEv
- __ZN25IOWrappedMemoryDescriptor7prepareEv
- __ZN25IOWrappedMemoryDescriptor8completeEv
- __ZN25IOWrappedMemoryDescriptorC1Ev
- __ZN25IOWrappedMemoryDescriptornwEm
- __ZZ19lifs_release_bufferE11_os_log_fmt
- __ZZ21lifs_init_buffer_poolE11_os_log_fmt
- __ZZ21lifs_init_buffer_poolE11_os_log_fmt_0
- __ZZ21lifs_init_buffer_poolE11_os_log_fmt_1
- __ZZ21lifs_init_buffer_poolE11_os_log_fmt_2
- __ZZ21lifs_init_buffer_poolE20kalloc_type_view_256
- __ZZ24lifs_destroy_buffer_poolE11_os_log_fmt
- __ZZ24lifs_destroy_buffer_poolE11_os_log_fmt_0
- __ZZ24lifs_destroy_buffer_poolE11_os_log_fmt_1
- __ZZ24lifs_destroy_buffer_poolE11_os_log_fmt_2
- __ZZ24lifs_destroy_buffer_poolE11_os_log_fmt_3
- __ZZ24lifs_destroy_buffer_poolE11_os_log_fmt_4
- __ZZ24lifs_destroy_buffer_poolE11_os_log_fmt_5
- __ZZ24lifs_destroy_buffer_poolE11_os_log_fmt_6
- __ZZ24lifs_destroy_buffer_poolE11_os_log_fmt_7
- __ZZ24lifs_destroy_buffer_poolE20kalloc_type_view_356
- __ZZ24lifs_destroy_buffer_poolE20kalloc_type_view_411
- __ZZ25lifs_get_buffer_from_poolE11_os_log_fmt
- __ZZ29lifs_copy_upl_to_buffer_asyncE20kalloc_type_view_498
- __ZZ29lifs_wait_for_copy_completionE20kalloc_type_view_548
- __ZZ30lifs_get_user_task_from_clientE11_os_log_fmt
- __ZZ30lifs_get_user_task_from_clientE11_os_log_fmt_0
- __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_198
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE11_os_log_fmt
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE11_os_log_fmt_0
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE11_os_log_fmt_1
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE11_os_log_fmt_2
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE11_os_log_fmt_3
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE11_os_log_fmt_4
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE11_os_log_fmt_5
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE11_os_log_fmt_6
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE11_os_log_fmt_7
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE19kalloc_type_view_37
- __ZZL25lifs_create_pooled_bufferP16lifs_buffer_pooljP4taskPP18lifs_pooled_bufferE20kalloc_type_view_157
- __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_218
- __ZZL26lifs_destroy_pooled_bufferP18lifs_pooled_bufferE11_os_log_fmt
- __ZZL26lifs_destroy_pooled_bufferP18lifs_pooled_bufferE20kalloc_type_view_186
- __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_255
- __ZZN19AppleLIFSUserClient12freeUCMountsEvE21kalloc_type_view_1878
- __ZZN19AppleLIFSUserClient13addMountEntryEjjE21kalloc_type_view_1888
- __ZZN19AppleLIFSUserClient16methodGetMappingEPS_PvP25IOExternalMethodArgumentsE11_os_log_fmt
- __ZZN19AppleLIFSUserClient16methodGetMappingEPS_PvP25IOExternalMethodArgumentsE11_os_log_fmt_0
- __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE21kalloc_type_view_1015
- _iokit_make_ident_port
- _kernel_task
- _lifs_acquire_io_lock
- _lifs_apply_cache_action
- _lifs_cache_close_request
- _lifs_cache_close_send
- _lifs_cache_open_request
- _lifs_cache_open_send
- _lifs_cache_upgrade_request
- _lifs_cache_upgrade_send
- _lifs_clear_io_lock_override
- _lifs_convert_extent_type
- _lifs_copy_upl_to_buffer_async
- _lifs_create_named_stream_request
- _lifs_create_namedstream_node
- _lifs_create_namedstream_send
- _lifs_create_node_ext
- _lifs_destroy_buffer_pool
- _lifs_get_buffer_from_pool
- _lifs_get_process_audit_token
- _lifs_get_user_task_from_client
- _lifs_init_buffer_pool
- _lifs_iterate_extents
- _lifs_lookup_named_stream_request
- _lifs_lookup_namedstream_send
- _lifs_read_wrapped_request_async
- _lifs_read_wrapped_send
- _lifs_release_buffer
- _lifs_release_io_lock
- _lifs_remove_named_stream_request
- _lifs_remove_namedstream_send
- _lifs_seek_request
- _lifs_seek_send
- _lifs_uc_add_mount
- _lifs_upgrade_io_lock
- _lifs_vnop_getnamedstream
- _lifs_vnop_makenamedstream
- _lifs_vnop_removenamedstream
- _lifs_vnop_strategy_done_pooled
- _lifs_wait_for_copy_completion
- _lifs_write_wrapped_request_async
- _lifs_write_wrapped_send
- _vfs_context_copy_audit_token
- _vnop_getnamedstream_desc
- _vnop_makenamedstream_desc
- _vnop_removenamedstream_desc
- add_sillyrename_entry.kalloc_type_view_2081
- add_sillyrename_entry.kalloc_type_view_2104
- cleanup_sillyrename_entries.kalloc_type_view_2202
- get_lifs_mount_from_node._os_log_fmt.5
- lifs_cache_request_handle_error._os_log_fmt
- lifs_copy_from_pooled_buffer_to_upl._os_log_fmt
- lifs_create_endio_context.kalloc_type_view_991
- lifs_create_named_stream_request._os_log_fmt
- lifs_create_node_ext._os_log_fmt
- lifs_create_node_ext._os_log_fmt.35
- lifs_create_node_ext.kalloc_type_view_450
- lifs_create_node_ext.kalloc_type_view_611
- lifs_destroy_endio_context.kalloc_type_view_1010
- lifs_endio_thread._os_log_fmt.48
- lifs_fsync_internal.kalloc_type_view_3952
- lifs_get_extent_layout._os_log_fmt
- lifs_getattr._os_log_fmt.28
- lifs_io_strategy_thread._os_log_fmt.46
- lifs_koio_blockmap._os_log_fmt.35
- lifs_koio_done.kalloc_type_view_2087
- lifs_lookup_named_stream_request._os_log_fmt
- lifs_mirror_mount_domount.kalloc_type_view_1229
- lifs_mirror_mount_domount.kalloc_type_view_1280
- lifs_mount.kalloc_type_view_655
- lifs_mount.kalloc_type_view_681
- lifs_mount.kalloc_type_view_682
- lifs_mount.kalloc_type_view_861
- lifs_mount.kalloc_type_view_907
- lifs_mount.kalloc_type_view_911
- lifs_mount.kalloc_type_view_915
- lifs_pack_attrlist_entry._os_log_fmt.24
- lifs_query_mountpoint._os_log_fmt.80
- lifs_query_mountpoint._os_log_fmt.85
- lifs_read_wrapped_request_async._os_log_fmt
- lifs_readdir_cached._os_log_fmt
- lifs_reclaim_done.kalloc_type_view_4947
- lifs_remove_named_stream_request._os_log_fmt
- lifs_req_callback_thread._os_log_fmt.19
- lifs_request_done._os_log_fmt.8
- lifs_request_done._os_log_fmt.9
- lifs_seek_request._os_log_fmt
- lifs_setattr._os_log_fmt.31
- lifs_setfsattr_done.kalloc_type_view_3879
- lifs_setup_mount_for_devvp._os_log_fmt.86
- lifs_setxattr_request._os_log_fmt.12
- lifs_submit_io._os_log_fmt
- lifs_submit_io.kalloc_type_view_2069
- lifs_submit_koio.kalloc_type_view_2109
- lifs_unmount._os_log_fmt.23
- lifs_unmount._os_log_fmt.24
- lifs_unmount.kalloc_type_view_1061
- lifs_unmount_dangling_all._os_log_fmt.33
- lifs_unmount_dangling_all._os_log_fmt.34
- lifs_unmount_dangling_all.kalloc_type_view_1557
- lifs_unmount_dangling_all.kalloc_type_view_1578
- lifs_unmount_dangling_thread.kalloc_type_view_1530
- lifs_vnop_clonefile._os_log_fmt.30
- lifs_vnop_makenamedstream._os_log_fmt
- lifs_vnop_readdir.kalloc_type_view_3110
- lifs_vnop_readdir.kalloc_type_view_3112
- lifs_vnop_reclaim.kalloc_type_view_4991
- lifs_vnop_reclaim.kalloc_type_view_5045
- lifs_vnop_strategy.kalloc_type_view_2203
- lifs_vnop_strategy_done.kalloc_type_view_1797
- lifs_vnop_strategy_done_pooled._os_log_fmt
- lifs_vnop_strategy_done_pooled._os_log_fmt.38
- lifs_wait_req_completion_with_params._os_log_fmt
- lifs_wait_req_completion_with_params._os_log_fmt.13
- lifs_wait_req_completion_with_params._os_log_fmt.14
- lifs_wait_req_completion_with_params._os_log_fmt.15
- lifs_write_wrapped_request_async._os_log_fmt
- move_sillyrename_entries.kalloc_type_view_2176
CStrings:
+ "111222222222222222222222222222222222222222222222223322221222222222222222121111111112222222222222222122222221122"
+ "11211223222222222222"
+ "121111121222121211111111111112222222"
+ "2222222222222222222222222222222222222222222222222222222222222222221111222111222211222222222222222222222222222222212121221122222"
- "%s%s"
- "%s() failed, err: %d\n"
- "%s: Got LIFS_DIRCACHE_LIMIT_REACHED with offset > 0, but no matching cookie entry was found"
- "%s: No LiveFS file handle provided\n"
- "%s: No mount reference in file handle\n"
- "%s: Not privileged (no fsmodule entitlement)\n"
- "%s: OSDynamicCast failed, client_object is not AppleLIFSUserClient"
- "%s: Unsupported extent clone policy [%d]"
- "%s: all %u volume(s) unmounted successfully\n"
- "%s: caller lacks fsmodule entitlement\n"
- "%s: caught a signal, returning %d"
- "%s: client_object %p is not an AppleLIFSUserClient\n"
- "%s: fail to create stream node [%d]"
- "%s: failed to unmount all volumes, unmounted %u of %u volume(s)\n"
- "%s: got %d from msleep, returning EIO"
- "%s: got error (%d) trying to increment iocount\n"
- "%s: incorrect extent (type %d range [%llu:%u]) returned for write operation"
- "%s: invalid mount_reference 0 at index %u\n"
- "%s: invalid volume count %u\n"
- "%s: kernel unmount successful for mount_ref %llu\n"
- "%s: lifs_apply_cache_action failed with error %d\n"
- "%s: lifs_create_namedstream_send()                         failed, err: %d\n"
- "%s: lifs_lookup_namedstream_send()                         failed, err: %d\n"
- "%s: lifs_remove_namedstream_send()                         failed, err: %d\n"
- "%s: lifs_seek_send() failed, err: %d\n"
- "%s: msleep says it got wakeup, but request not done, going back to sleep"
- "%s: no lifsnode found for fh\n"
- "%s: no mount found for mount_ref %llu (idx %u)\n"
- "%s: registered mount_reference %u -> mount_index %u for IOUC %p\n"
- "%s: returning user task %p from client %p"
- "%s: set cache state for vnode %p (ref:%u -> idx:%u mode:%d coherency:%d action:%d)\n"
- "%s: timed out, returning %d"
- "%s: triggering kernel unmount for %u volume(s) with flags 0x%x\n"
- "%s: triggering vfs_unmountbyfsid for mount_ref %llu (mount %p)\n"
- "%s: unknown or unauthorized mount_reference %u\n"
- "%s: vfs_unmountbyfsid for mount_ref %llu returned error %d\n"
- "%s: vnode %p isn't a regular file or a directory\n"
- "%s:inline_data:   forcefully releasing buffer[%u] in state %d"
- "%s:inline_data: Cached mapping is NULL!"
- "%s:inline_data: Clearing user_task reference for mount %p"
- "%s:inline_data: Destroying buffer pool for mount %p"
- "%s:inline_data: Inline data proprties initialized for mount %p"
- "%s:inline_data: No buffer pool found for release"
- "%s:inline_data: No pooled buffer found, continue"
- "%s:inline_data: UPL copy failed %d, using default submit IO"
- "%s:inline_data: all buffers destroyed"
- "%s:inline_data: all buffers successfully released"
- "%s:inline_data: async copy thread stopped and work queue drained"
- "%s:inline_data: buffer pool init failed %d, disabling inline data"
- "%s:inline_data: buffer pool initialized: %u buffers, %lu MB total (async copy thread started)"
- "%s:inline_data: buffer-to-UPL copy failed: %d"
- "%s:inline_data: buffer[%u] created: kern_addr=%p user_addr=%llx port=%p size=%lu"
- "%s:inline_data: buffer[%u] still in active list during pool destroy (state=%d)"
- "%s:inline_data: copy failed for buffer[%u]: error %d"
- "%s:inline_data: createMappingInTask failed %d for buffer %u"
- "%s:inline_data: creating buffer pool: %u buffers x %lu bytes"
- "%s:inline_data: destroying %u buffers from free list"
- "%s:inline_data: destroying buffer pool"
- "%s:inline_data: destroying buffer[%u] in state %d (expected FREE)"
- "%s:inline_data: failed to create buffer %u, error %d"
- "%s:inline_data: failed to start copy thread, error %d"
- "%s:inline_data: getCachedMapping returned NULL for buffer %u"
- "%s:inline_data: iokit_make_ident_port failed for buffer %u"
- "%s:inline_data: new IOWrappedMemoryDescriptor failed for buffer %u"
- "%s:inline_data: pool exhausted: free=%u allocated=%u"
- "%s:inline_data: prepare failed %d for buffer %u"
- "%s:inline_data: releasing buffer[%u] in unexpected state %d (expected READY)"
- "%s:inline_data: timed out waiting for %u buffers to be released - forcing cleanup"
- "%s:inline_data: vm_allocate failed %d for buffer %u"
- "%s:inline_data: waiting for %u buffers to be released"
- "%s:inline_data: withAddressRange failed for buffer %u"
- "%s:inline_data: wrapped_desc->init failed for buffer %u"
- "/..namedfork/rsrc"
- "111212222"
- "1112222222222222222222222222222222222222222222222233222212222222222222221211111111122222222222222221121222222211222"
- "112"
- "1121121223222222222222"
- "11212111"
- "1211111212221212111111111111122222222211"
- "1212111"
- "221111122112222"
- "222222222222222222222222222222222222222222222222222222222222222222211112221112222112222222222222222222222222222222121212211222222"
- "NO-NAME"
- "_N_INACTIVE"
- "addMountEntry"
- "com.apple.ResourceFork"
- "lifs_buffer_pool_copy"
- "lifs_buffer_pool_copy_thread"
- "lifs_cache_close_send"
- "lifs_cache_open_send"
- "lifs_cache_upgrade_send"
- "lifs_copy_from_pooled_buffer_to_upl"
- "lifs_create_named_stream_request"
- "lifs_create_pooled_buffer"
- "lifs_destroy_buffer_pool"
- "lifs_destroy_pooled_buffer"
- "lifs_get_buffer_from_pool"
- "lifs_get_extent_layout"
- "lifs_get_user_task_from_client"
- "lifs_init_buffer_pool"
- "lifs_lookup_named_stream_request"
- "lifs_read_wrapped_request_async"
- "lifs_readdir_cached"
- "lifs_release_buffer"
- "lifs_remove_named_stream_request"
- "lifs_seek_request"
- "lifs_submit_io"
- "lifs_uc_add_mount"
- "lifs_vnop_makenamedstream"
- "lifs_vnop_strategy_done_pooled"
- "lifs_wait_for_copy_completion"
- "lifs_wait_req_completion_with_params"
- "lifs_write_wrapped_request_async"
- "methodGetMapping"
- "methodKernelUnmount"
- "methodSetCacheState"
- "site.lifs_buffer_pool_t"
- "site.lifs_copy_work_t"
- "site.lifs_pooled_buffer_t"
- "site.struct lifs_uc_mount_entry"

```
