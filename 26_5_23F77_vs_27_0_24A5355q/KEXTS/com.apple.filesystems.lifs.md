## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

-737.120.9.0.0
-  __TEXT.__os_log: 0x1385
-  __TEXT.__cstring: 0x21a0
-  __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1acbc
+971.0.0.0.5
+  __TEXT.__os_log: 0x1ee5
+  __TEXT.__cstring: 0x29be
+  __TEXT.__const: 0x338
+  __TEXT_EXEC.__text: 0x20220
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x528
-  __DATA.__common: 0x130
+  __DATA.__data: 0x578
+  __DATA.__common: 0x138
   __DATA.__bss: 0x90
-  __DATA_CONST.__auth_got: 0x7b0
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x16b8
-  __DATA_CONST.__kalloc_type: 0xbc0
+  __DATA_CONST.__const: 0x1768
+  __DATA_CONST.__kalloc_type: 0xe40
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 0FF9D563-5968-3F92-8F67-31CC6CF09E36
-  Functions: 402
+  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_ptr: 0x8
+  UUID: ED9691DC-A4F4-3499-937B-4415F5B44867
+  Functions: 460
   Symbols:   0
-  CStrings:  398
+  CStrings:  516
 
CStrings:
+ "%s%s"
+ "%s() failed, err: %d\n"
+ "%s: Got LIFS_DIRCACHE_LIMIT_REACHED with offset > 0, but no matching cookie entry was found"
+ "%s: No LiveFS file handle provided\n"
+ "%s: No mount reference in file handle\n"
+ "%s: Not privileged (no fsmodule entitlement)\n"
+ "%s: OSDynamicCast failed, client_object is not AppleLIFSUserClient"
+ "%s: Unsupported extent clone policy [%d]"
+ "%s: all %u volume(s) unmounted successfully\n"
+ "%s: caller lacks fsmodule entitlement\n"
+ "%s: caught a signal, returning %d"
+ "%s: client_object %p is not an AppleLIFSUserClient\n"
+ "%s: fail to create stream node [%d]"
+ "%s: failed to unmount all volumes, unmounted %u of %u volume(s)\n"
+ "%s: got %d from msleep, returning EIO"
+ "%s: got error (%d) trying to increment iocount\n"
+ "%s: incorrect extent (type %d range [%llu:%u]) returned for write operation"
+ "%s: invalid mount_reference 0 at index %u\n"
+ "%s: invalid volume count %u\n"
+ "%s: kernel unmount successful for mount_ref %llu\n"
+ "%s: lifs_apply_cache_action failed with error %d\n"
+ "%s: lifs_create_namedstream_send()                         failed, err: %d\n"
+ "%s: lifs_lookup_namedstream_send()                         failed, err: %d\n"
+ "%s: lifs_remove_namedstream_send()                         failed, err: %d\n"
+ "%s: lifs_seek_send() failed, err: %d\n"
+ "%s: msleep says it got wakeup, but request not done, going back to sleep"
+ "%s: no lifsnode found for fh\n"
+ "%s: no mount found for mount_ref %llu (idx %u)\n"
+ "%s: registered mount_reference %u -> mount_index %u for IOUC %p\n"
+ "%s: returning user task %p from client %p"
+ "%s: set cache state for vnode %p (ref:%u -> idx:%u mode:%d coherency:%d action:%d)\n"
+ "%s: timed out, returning %d"
+ "%s: triggering kernel unmount for %u volume(s) with flags 0x%x\n"
+ "%s: triggering vfs_unmountbyfsid for mount_ref %llu (mount %p)\n"
+ "%s: unknown or unauthorized mount_reference %u\n"
+ "%s: vfs_unmountbyfsid for mount_ref %llu returned error %d\n"
+ "%s: vnode %p isn't a regular file or a directory\n"
+ "%s:inline_data:   forcefully releasing buffer[%u] in state %d"
+ "%s:inline_data: Cached mapping is NULL!"
+ "%s:inline_data: Clearing user_task reference for mount %p"
+ "%s:inline_data: Destroying buffer pool for mount %p"
+ "%s:inline_data: Inline data proprties initialized for mount %p"
+ "%s:inline_data: No buffer pool found for release"
+ "%s:inline_data: No pooled buffer found, continue"
+ "%s:inline_data: UPL copy failed %d, using default submit IO"
+ "%s:inline_data: all buffers destroyed"
+ "%s:inline_data: all buffers successfully released"
+ "%s:inline_data: async copy thread stopped and work queue drained"
+ "%s:inline_data: buffer pool init failed %d, disabling inline data"
+ "%s:inline_data: buffer pool initialized: %u buffers, %lu MB total (async copy thread started)"
+ "%s:inline_data: buffer-to-UPL copy failed: %d"
+ "%s:inline_data: buffer[%u] created: kern_addr=%p user_addr=%llx port=%p size=%lu"
+ "%s:inline_data: buffer[%u] still in active list during pool destroy (state=%d)"
+ "%s:inline_data: copy failed for buffer[%u]: error %d"
+ "%s:inline_data: createMappingInTask failed %d for buffer %u"
+ "%s:inline_data: creating buffer pool: %u buffers x %lu bytes"
+ "%s:inline_data: destroying %u buffers from free list"
+ "%s:inline_data: destroying buffer pool"
+ "%s:inline_data: destroying buffer[%u] in state %d (expected FREE)"
+ "%s:inline_data: failed to create buffer %u, error %d"
+ "%s:inline_data: failed to start copy thread, error %d"
+ "%s:inline_data: getCachedMapping returned NULL for buffer %u"
+ "%s:inline_data: iokit_make_ident_port failed for buffer %u"
+ "%s:inline_data: new IOWrappedMemoryDescriptor failed for buffer %u"
+ "%s:inline_data: pool exhausted: free=%u allocated=%u"
+ "%s:inline_data: prepare failed %d for buffer %u"
+ "%s:inline_data: releasing buffer[%u] in unexpected state %d (expected READY)"
+ "%s:inline_data: timed out waiting for %u buffers to be released - forcing cleanup"
+ "%s:inline_data: vm_allocate failed %d for buffer %u"
+ "%s:inline_data: waiting for %u buffers to be released"
+ "%s:inline_data: withAddressRange failed for buffer %u"
+ "%s:inline_data: wrapped_desc->init failed for buffer %u"
+ "._%s"
+ "/..namedfork/rsrc"
+ "111212222"
+ "1112222222222222222222222222222222222222222222222233222212222222222222221211111111122222222222222221121222222211222"
+ "112"
+ "1121121223222222222222"
+ "11212111"
+ "1211111212221212111111111111122222222211"
+ "1212111"
+ "221111122112222"
+ "222222222222222222222222222222222222222222222222222222222222222222211112221112222112222222222222222222222222222222121212211222222"
+ "I"
+ "NO-NAME"
+ "_N_INACTIVE"
+ "addMountEntry"
+ "force_vfs_xattr_emulation"
+ "lifs_buffer_pool_copy"
+ "lifs_buffer_pool_copy_thread"
+ "lifs_cache_close_send"
+ "lifs_cache_open_send"
+ "lifs_cache_upgrade_send"
+ "lifs_copy_from_pooled_buffer_to_upl"
+ "lifs_create_named_stream_request"
+ "lifs_create_pooled_buffer"
+ "lifs_destroy_buffer_pool"
+ "lifs_destroy_pooled_buffer"
+ "lifs_get_buffer_from_pool"
+ "lifs_get_extent_layout"
+ "lifs_get_user_task_from_client"
+ "lifs_init_buffer_pool"
+ "lifs_lookup_named_stream_request"
+ "lifs_read_wrapped_request_async"
+ "lifs_readdir_cached"
+ "lifs_release_buffer"
+ "lifs_remove_named_stream_request"
+ "lifs_seek_request"
+ "lifs_submit_io"
+ "lifs_uc_add_mount"
+ "lifs_vnop_makenamedstream"
+ "lifs_vnop_strategy_done_pooled"
+ "lifs_wait_for_copy_completion"
+ "lifs_wait_req_completion_with_params"
+ "lifs_write_wrapped_request_async"
+ "methodGetMapping"
+ "methodKernelUnmount"
+ "methodSetCacheState"
+ "site.lifs_buffer_pool_t"
+ "site.lifs_copy_work_t"
+ "site.lifs_pooled_buffer_t"
+ "site.struct lifs_uc_mount_entry"
- "111222222222222222222222222222222222222222222222223322221222222222222222121111111112222222222222222122222221122"
- "11211223222222222222"
- "121111121222121211111111111112222222"
- "2222222222222222222222222222222222222222222222222222222222222222221111222111222211222222222222222222222222222222212121221122222"

```
