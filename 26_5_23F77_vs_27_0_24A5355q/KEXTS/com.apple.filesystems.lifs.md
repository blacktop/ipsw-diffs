## com.apple.filesystems.lifs

> `com.apple.filesystems.lifs`

```diff

-737.120.9.0.0
-  __TEXT.__os_log: 0x1385 sha256:8e49bc6217c2adcfd7b936f6d3d67a253e1e5ae04366f7f3d1830d88381ffe87
-  __TEXT.__cstring: 0x21a0 sha256:4e227649d06286644f579a1438167c864081b5cb3197ffc396a8d1e66857c024
-  __TEXT.__const: 0x2c0 sha256:b6e22b56d0c269e9acaec0f146694ef9b3c54af7d2b9d250882d7c873554d588
-  __TEXT_EXEC.__text: 0x1acbc sha256:8808ce8d1aa01773a29f59af918bc335ca8df7938de0d0b42f0455f40b47fe58
+971.0.0.0.5
+  __TEXT.__os_log: 0x1ee5 sha256:67e1f0f3e6f4405a6136abdf2811a29bf411c1fa86a2db41ba3f5683d959d692
+  __TEXT.__cstring: 0x29be sha256:13becaa827b61cac20339891e5d52b94adb00354831890663e4ecd686fbe033c
+  __TEXT.__const: 0x338 sha256:fa702de501c337c373daa59db152f191bfa69999eb94ab007496e7cf7c6685bb
+  __TEXT_EXEC.__text: 0x20220 sha256:dea00bbb228b575a6282bb249790aa20e7141889a75587f9103e9fb1dd7cef73
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x528 sha256:29934a1cc08e3027f49ac917f21d1025c24ee9900412fef8b54afca02bf98da4
-  __DATA.__common: 0x130 sha256:e2fc162ed9124452d23c85e81d60a0c228f414c3214a5de635737e25fbd29ac1
+  __DATA.__data: 0x578 sha256:f1c35b55621979d716faf85029081972949eeeab21c36d37cde6cc86d162436b
+  __DATA.__common: 0x138 sha256:6287e17fe5efcb191aec8a2578e685d0a1040a0ab53bd1f02c7f49cc6c8fced7
   __DATA.__bss: 0x90 sha256:81c611f35bff79491538b2f7cf201c7597a661a5c549633541c62bdc8af1613f
-  __DATA_CONST.__auth_got: 0x7b0 sha256:988ba5fe407cb4e9523707e98660293919c22889dda1cec06a9e59ac55b5941d
-  __DATA_CONST.__got: 0x78 sha256:fc9ea1d417c54c45451e5f5a32cae856382fd89abda4b66011ab38cf214f98cd
-  __DATA_CONST.__auth_ptr: 0x8 sha256:efdbfcd9b636393b8330ea016790b1ccb1febaafc24062a27cf4e098eaf47ee0
-  __DATA_CONST.__mod_init_func: 0x18 sha256:a795b8933eb243c7bc7ff93a42004f75724cc487d35d81bd178133307d259a86
-  __DATA_CONST.__mod_term_func: 0x18 sha256:7de13ddacf896e1e7689da5ea2fc3706771f2aa6c0edd26915c6c4e22b497918
-  __DATA_CONST.__const: 0x16b8 sha256:b9e1ae7d542cfc7b54afdf975c3c57d37799073dd7aea424618f8213abd0cfc2
-  __DATA_CONST.__kalloc_type: 0xbc0 sha256:e16a615f363be7ed23162639011ec14cd56030471449ab4f70dfbb21230f9ab1
-  __DATA_CONST.__kalloc_var: 0xf0 sha256:4b45f0faff2a10837b15ac3ca05fd262284678dc8861cacc37fa7633fba78a48
-  UUID: 0FF9D563-5968-3F92-8F67-31CC6CF09E36
-  Functions: 402
+  __DATA_CONST.__mod_init_func: 0x18 sha256:524b8210c6e7e96d305a42abb05683a78bed79cbf5013af8b4f1c7f2131b8323
+  __DATA_CONST.__mod_term_func: 0x18 sha256:4de4097e894e310b64e156a7f1e949929860f54c030452ef4087e9036ba26a29
+  __DATA_CONST.__const: 0x1768 sha256:1445ad7aa55e8c307d019e46e9ce56f751d08782e00a327008f992fb613bae37
+  __DATA_CONST.__kalloc_type: 0xe40 sha256:c58ee4ecb4a7c538bb5265663111fec65ea74a6c69ca38d43c3aa1f0d7d90746
+  __DATA_CONST.__kalloc_var: 0xf0 sha256:eb5f3e52beed23122d1d91a6b747b25cd0db05a2c10f1a48160a947e4587e3cf
+  __DATA_CONST.__auth_got: 0x7d0 sha256:d237b16cc78e0d2d4ed3b2055d4866059dd4b4c2785c0138ea7480c51ab5c3ee
+  __DATA_CONST.__got: 0x80 sha256:00a7f9f3476d6c66be9d711c5c8eaa02813691890394c2606a8b5d43504fd619
+  __DATA_CONST.__auth_ptr: 0x8 sha256:152e1bd0b3971ccd304f445b79977db39a8d43b430cb4bc278e278571ea49464
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
