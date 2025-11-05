## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-657.80.3.0.0
-  __TEXT.__text: 0x3690c
-  __TEXT.__auth_stubs: 0x630
+715.100.22.0.0
+  __TEXT.__text: 0x3ab50
+  __TEXT.__auth_stubs: 0x710
   __TEXT.__const: 0x5b5
-  __TEXT.__cstring: 0x7bff
+  __TEXT.__cstring: 0x965f
   __TEXT.__dof_magmalloc: 0xa96
-  __TEXT.__unwind_info: 0x8e8
+  __TEXT.__unwind_info: 0x928
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x6d0
-  __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x670
+  __DATA_CONST.__const: 0x738
+  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__const: 0x6d0
   __AUTH.__data: 0x128
   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0xe9
   __DATA.__crash_info: 0x40
+  __DATA.__bss: 0x2191
   __DATA.__common: 0x68
-  __DATA.__bss: 0x2171
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__common: 0x1bc
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 1480B446-99F7-3757-9D4E-5BA3014A2726
-  Functions: 798
-  Symbols:   1208
-  CStrings:  735
+  UUID: 9E4556E4-8822-3111-A801-02066E2FDEBC
+  Functions: 859
+  Symbols:   1330
+  CStrings:  847
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _ZAP_GO_DOWN
+ ____BUG_IN_CLIENT_OF_LIBMALLOC_POINTER_BEING_FREED_WAS_NOT_ALLOCATED
+ ____xzm_introspect_tiny_chunk_blocks_block_invoke
+ ___copy_helper_block_8_32r
+ ___copy_helper_block_8_32r40r
+ ___destroy_helper_block_8_32r
+ ___destroy_helper_block_8_32r40r
+ __block_descriptor_tmp.154
+ __block_descriptor_tmp.16
+ __block_descriptor_tmp.162
+ __block_descriptor_tmp.190
+ __block_descriptor_tmp.195
+ __block_descriptor_tmp.224
+ __block_descriptor_tmp.227
+ __block_descriptor_tmp.230
+ __block_descriptor_tmp.231
+ __block_descriptor_tmp.34
+ __block_descriptor_tmp.48
+ __block_literal_global.226
+ __block_literal_global.229
+ __malloc_check_secure_allocator_process_enablement
+ __xzm_chunk_batch_list_push
+ __xzm_free_not_found
+ __xzm_introspect_enumerate_thread_caches
+ __xzm_malloc_zone_malloc_entry
+ __xzm_malloc_zone_malloc_type_calloc_entry
+ __xzm_print_block_invoke.137
+ __xzm_print_block_invoke.157
+ __xzm_print_block_invoke.163
+ __xzm_print_block_invoke.191
+ __xzm_print_block_invoke.35
+ __xzm_reclaim_id_cache_init
+ __xzm_reclaim_is_reusable
+ __xzm_reclaim_mark_used_locked
+ __xzm_segment_group_cache_mark_free
+ __xzm_segment_group_cache_mark_used
+ __xzm_segment_group_segment_span_free_coalesce
+ __xzm_segment_group_span_mark_free
+ __xzm_segment_group_span_mark_smaller
+ __xzm_segment_group_span_mark_used
+ __xzm_thread_cache_create_and_malloc
+ __xzm_xzone_batch_small_push
+ __xzm_xzone_find_and_malloc_from_tiny_chunk
+ __xzm_xzone_free_tiny
+ __xzm_xzone_madvise_batch
+ __xzm_xzone_madvise_tiny_chunk
+ __xzm_xzone_malloc_tiny_or_early
+ __xzm_xzone_thread_cache_destructor
+ __xzm_xzone_thread_cache_fill_and_malloc
+ __xzm_xzone_thread_cache_malloc_corrupt
+ __xzm_xzone_thread_cache_record_and_malloc_outlined
+ __xzm_xzone_tiny_chunks_mark_empty
+ _mach_error_string
+ _mach_vm_copy
+ _mach_vm_reclaim_is_reusable
+ _mach_vm_reclaim_query_state
+ _mach_vm_reclaim_ring_allocate
+ _mach_vm_reclaim_ring_capacity
+ _mach_vm_reclaim_ring_flush
+ _mach_vm_reclaim_ring_resize
+ _mach_vm_reclaim_round_capacity
+ _mach_vm_reclaim_try_cancel
+ _mach_vm_reclaim_try_enter
+ _mach_vm_reclaim_update_kernel_accounting
+ _malloc_allows_internal_security_4test
+ _malloc_register_stack_logger.cold.1
+ _malloc_zone_malloc_with_options_np_outlined.cold.1
+ _pthread_key_init_np
+ _pthread_self
+ _sanitizer_malloc_type_calloc
+ _sanitizer_malloc_type_malloc
+ _sanitizer_malloc_type_malloc_noalign_with_options
+ _sanitizer_malloc_type_malloc_with_options
+ _sanitizer_malloc_type_memalign
+ _sanitizer_malloc_type_realloc
+ _sanitizer_malloc_with_options
+ _xzm_chunk_mark_free
+ _xzm_chunk_mark_used
+ _xzm_malloc_large_huge.cold.1
+ _xzm_malloc_large_huge.cold.2
+ _xzm_reclaim_buffer
+ _xzm_reclaim_force_sync
+ _xzm_reclaim_id_cache_init.cold.1
+ _xzm_reclaim_init
+ _xzm_reclaim_is_reusable.cold.1
+ _xzm_reclaim_mark_free
+ _xzm_reclaim_mark_free_locked
+ _xzm_reclaim_mark_used
+ _xzm_reclaim_mark_used_locked.cold.1
+ _xzm_reclaim_mark_used_locked.cold.2
+ _xzm_reclaim_sync_and_resize
+ _xzm_segment_group_find_and_allocate_chunk.cold.1
+ _xzm_segment_group_segment_span_free_coalesce.cold.1
+ _xzm_segment_group_segment_span_free_coalesce.cold.2
+ _xzm_segment_group_segment_span_free_coalesce.cold.3
+ _xzm_segment_group_segment_span_free_coalesce.cold.4
+ _xzm_xzone_chunk_free.cold.4
+ _xzm_xzone_chunk_madvise_free_slices.cold.1
+ _xzm_xzone_find_and_malloc_from_tiny_chunk.cold.1
+ _xzm_xzone_madvise_batch.cold.1
+ _xzm_xzone_madvise_batch.cold.2
+ _xzm_xzone_madvise_batch.cold.3
+ _xzm_xzone_madvise_batch.cold.4
+ _xzm_xzone_thread_cache_destructor.cold.1
+ _xzm_xzone_thread_cache_destructor.cold.2
+ _xzm_xzone_thread_cache_destructor.cold.3
+ _xzm_xzone_thread_cache_destructor.cold.4
+ allocate.cold.9
+ malloc_default_purgeable_zone.cold.1
+ malloc_set_thread_options.cold.1
+ malloc_type_aligned_alloc.cold.1
+ malloc_zone_batch_free.cold.1
+ nanov2_allocate_outlined.cold.1
+ nanov2_configure.cold.1
+ nanov2_print.cold.1
+ nanov2_ptr_in_use_enumerator.cold.2
+ nanov2_statistics.cold.2
+ pgm_free.cold.1
+ pgm_free_definite_size.cold.1
+ pgm_size.cold.1
+ sanitizer_malloc_type_calloc.cold.1
+ sanitizer_malloc_type_malloc_noalign_with_options.cold.1
+ sanitizer_malloc_type_malloc_with_options.cold.1
+ sanitizer_malloc_type_memalign.cold.1
+ sanitizer_malloc_type_realloc.cold.1
+ sanitizer_malloc_type_realloc.cold.2
+ xzm_chunk_mark_free.cold.1
+ xzm_chunk_mark_used.cold.1
+ xzm_main_malloc_zone_create.cold.9
+ xzm_malloc_zone_destroy.cold.3
+ xzm_malloc_zone_destroy.cold.4
+ xzm_malloc_zone_free_definite_size_slow.cold.3
+ xzm_metapool_alloc.cold.2
+ xzm_reclaim_force_sync.cold.1
+ xzm_reclaim_force_sync.cold.2
+ xzm_reclaim_mark_free_locked.cold.1
+ xzm_reclaim_mark_free_locked.cold.2
+ xzm_reclaim_sync_and_resize.cold.1
+ xzm_segment_group_alloc_chunk.cold.3
+ xzm_segment_group_try_realloc_large_chunk.cold.1
- __block_descriptor_tmp.107
- __block_descriptor_tmp.133
- __block_descriptor_tmp.138
- __block_descriptor_tmp.166
- __block_descriptor_tmp.169
- __block_descriptor_tmp.172
- __block_descriptor_tmp.173
- __block_descriptor_tmp.32
- __block_descriptor_tmp.44
- __block_literal_global.168
- __block_literal_global.171
- __xzm_mds_stores_process_config
- __xzm_print_block_invoke.102
- __xzm_print_block_invoke.108
- __xzm_print_block_invoke.134
- __xzm_print_block_invoke.33
- __xzm_segment_group_alloc_segment_and_chunk
- __xzm_segment_group_clear_chunk
- _set_tiny_meta_header_in_use
- _xzm_free.cold.1
- sanitizer_calloc.cold.1
- sanitizer_malloc.cold.1
- sanitizer_memalign.cold.1
- sanitizer_realloc.cold.1
- sanitizer_realloc.cold.2
CStrings:
+ " \n"
+ "                \"allocs\": \"%llu\" \n"
+ "                \"chunk\": \"%p\", \n"
+ "                \"chunk_start\": \"%p\", \n"
+ "                \"contentions\": \"%llu\", \n"
+ "                \"free_count\": \"0x%llx\", \n"
+ "                \"head\": \"0x%llx\", \n"
+ "                \"head\": \"EMPTY\" \n"
+ "                \"head\": \"NOT_CACHED\", \n"
+ "                \"head_seqno\": \"0x%llx\", \n"
+ "                \"seqno\": \"0x%llx\" \n"
+ "                \"timestamp\": \"%llu\", \n"
+ "                \"xz_idx\": %d, \n"
+ "            \"%d\": {\n"
+ "            \"address\": \"%p\", \n"
+ "            \"behavior\": %u, \n"
+ "            \"id\": %u, \n"
+ "            \"size\": %u, \n"
+ "        \"batch_count\": %u, \n"
+ "        \"busy\": %llu, \n"
+ "        \"early_budget\": %u, \n"
+ "        \"head\": %llu, \n"
+ "        \"segment_group_id\": %d, \n"
+ "        \"slice_metadata\": \"%p\", \n"
+ "        \"tail\": %llu \n"
+ "        \"thread\": \"%p\",\n"
+ "        \"xz_caches\": {\n"
+ "        { \n"
+ "        }"
+ "    \"buffer_len\": %llu, \n"
+ "    \"entries\": [ \n"
+ "    \"indices\": { \n"
+ "    \"last_accounting_given_to_kernel\": %llu, \n"
+ "    \"max_len\": %llu, \n"
+ "    \"va_in_buffer\": %llu, \n"
+ "    ] \n"
+ "    } \n"
+ "    }, \n"
+ "\"batch_size\": %u, \n"
+ "\"defer_small\": %s, \n"
+ "\"defer_tiny\": %s, \n"
+ "\"ptr_bucket_count\": %d, \n"
+ "\"range_group_count\": %u, \n"
+ "\"reclaim_buffer\": { \n"
+ "\"segment_group_count\": %u, \n"
+ "\"segment_group_ids_count\": %u, \n"
+ "\"thread_cache_activation_contentions\": %lu, \n"
+ "\"thread_cache_activation_period\": %lu, \n"
+ "\"thread_cache_activation_time\": %llu, \n"
+ "\"thread_cache_enabled\": %s, \n"
+ "\"thread_caches\": [ \n"
+ "%s    \"reclaim_id\": %llu, \n"
+ "%s    \"reclaim_id\": -1, \n"
+ "AllowInternalSecurityPolicy"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - cookie, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - free count, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - inconsistent walk, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - linkage, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny local freelist, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny remote freelist, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: failed to allocate malloc metadata, out of virtual address space, client likely has a memory leak"
+ "BUG IN CLIENT OF LIBMALLOC: pointer zone mismatch, client may be passing the wrong malloc zone"
+ "BUG IN LIBMALLOC: Attempt to check for deferred reclamation on non-chunk slice"
+ "BUG IN LIBMALLOC: Failed to overwrite malloc metadata"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5651)"
+ "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/../xzone/xzone_inline_internal.h:190)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2004)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2003)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2105)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:136)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_start < ptr_start || data_start >= ptr_start + ptr_reservation_size\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1057)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:215)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:253)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:388)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:390)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:148)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:281)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:290)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:399)"
+ "BUG IN LIBMALLOC: malloc assertion \"leaf_table\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:64)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:781)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5026)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1443)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5700)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1080)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3976)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5786)"
+ "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6380)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:779)"
+ "BUG IN LIBMALLOC: pthread_key_init_np failed"
+ "DISABLED"
+ "Deferred reclamation cannot be used for xzones without large\n"
+ "ENABLED"
+ "Failed to allocate segment from range group - out of space\n"
+ "GroupSessionService"
+ "Huge cache requires deferred reclamation for large.\n"
+ "IMTranscoderAgent"
+ "Internal Security Policy: %d\n"
+ "MallocAllowInternalSecurity"
+ "MallocDeferredReclaim"
+ "MallocDeferredReclaim must be one of 0,1 - got %ld\n"
+ "MallocDeferredReclaimBufferCount"
+ "MallocDeferredReclaimBufferMaxCount"
+ "MallocProbGuardLeftAlignPercentage"
+ "MallocXzoneBatchSize"
+ "MallocXzoneDeferLarge"
+ "MallocXzoneDeferLarge must be one of 0,1 - got %ld\n"
+ "MallocXzoneDeferSmall"
+ "MallocXzoneDeferSmall must be one of 0,1 - got %ld\n"
+ "MallocXzoneDeferTiny"
+ "MallocXzoneDeferTiny must be one of 0,1 - got %ld\n"
+ "MallocXzoneHugeCacheSize"
+ "MallocXzonePerClusterSegmentGroups"
+ "MallocXzonePerClusterSegmentGroups must be 0 or 1.\n"
+ "MallocXzoneSmallThrashLimitSize"
+ "MallocXzoneSmallThrashThreshold"
+ "MallocXzoneThreadCacheActivationContentions"
+ "MallocXzoneThreadCacheActivationPeriod"
+ "MallocXzoneThreadCacheActivationTime"
+ "MallocXzoneThreadCaching"
+ "MallocXzoneThreadCaching must be one of 0,1 - got %ld\n"
+ "Messages"
+ "Screen Sharing"
+ "SecureAllocator_ThreadCaching"
+ "XZM Config:\n\tData Only: %d\n\tGuards Enabled: %d\n\tScribble: %d\n\tTiny/Small Batch Max: %d\n\tDefer Tiny: %d\n\tDefer Small: %d\n\tDefer Large: %d\n\tHuge Cache Size: %d\n\tReclaim Buffer Count: %u/%u (%s)\n\tRanges (ptr addr/size/data addr/size): 0x%llx/%lu/0x%llx/%lu\n\tInitial Slot Config: %s\n\tMax Slot Config: %s\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tTiny Thrash Threshold: %llu ms\n\tSmall Thrash Threshold: %llu ms, %llu bytes\n\tThread Caching: %s (%u allocs, %u contentions, %llu ms)\n\tPointer Bucket Count: %lu\n"
+ "], \n"
+ "disabled"
+ "enabled"
+ "i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
+ "i24@?0Q8^{xzm_thread_cache_s={?=^{xzm_thread_cache_s}^^{xzm_thread_cache_s}}^{xzm_main_malloc_zone_s}^{_opaque_pthread_t}Q[0(xzm_xzone_thread_cache_u={?=^{xzm_slice_s}*(?={?=SSSS}(xzm_xzone_thread_cache_atomic_meta_u={?=SS}I)Q)}{?=QQSSI})]}16"
+ "i32@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
+ "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{os_unfair_lock_s=I}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCQQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"
+ "keychainsharingmessagingd"
+ "malloc_zone_malloc_with_options: reserved TSD bit set\n"
+ "malloc_zone_malloc_with_options: unsupported options 0x%llx\n"
+ "sanitizer_malloc_with_options: unsupported options 0x%llx\n"
+ "thread cache slab"
+ "vm.reclaim.enabled"
+ "xzm: failed to initialize deferred reclamation buffer [%d] %s\n"
+ "xzm: unsupported value for MallocXzoneHugeCacheSize (%ld)"
- "\"defer_xzones\": %s, \n"
- "%ld, counter=%d\n*** invariant broken for %p this tiny msize=%d - size is too large\n"
- "*** error at %p msize for in_use is %d\n"
- "*** error for object %p: pointer being realloc'd was not allocated\n"
- "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist"
- "BUG IN CLIENT OF LIBMALLOC: pointer being reallocated with wrong zone"
- "BUG IN LIBMALLOC: Failed to allocate malloc metadata"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4039)"
- "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < UINT32_MAX\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/../xzone/xzone_inline_internal.h:190)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1766)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1765)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1870)"
- "BUG IN LIBMALLOC: malloc assertion \"data_start < ptr_start || data_start >= ptr_start + ptr_reservation_size\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:866)"
- "BUG IN LIBMALLOC: malloc assertion \"leaf_table\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:68)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:559)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3472)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1114)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:2724)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:805)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4172)"
- "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4732)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:557)"
- "Failed to allocate segment - out of space\n"
- "SecureAllocator_process_MTLCompilerService"
- "XZM Config:\n\tData Only: %d\n\tGuards Enabled: %d\n\tScribble: %d\n\tRanges (ptr addr/size/data addr/size): 0x%llx/%lu/0x%llx/%lu\n\tInitial Slot Config: %s\n\tMax Slot Config: %s\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tPointer Bucket Count: %lu\n"
- "i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
- "i32@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
- "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
- "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{os_unfair_lock_s=I}}{?=(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)})S^{xzm_segment_group_s}QQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"
- "mds_stores"

```
