## libsystem_malloc_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

-474.0.13.0.0
-  __TEXT.__text: 0x6c2a4
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__const: 0x5fc
-  __TEXT.__cstring: 0xad81
-  __TEXT.__dof_magmalloc: 0x8c2
-  __TEXT.__unwind_info: 0x77c
-  __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0xf8
-  __AUTH_CONST.__const: 0x590
-  __AUTH_CONST.__auth_got: 0x318
-  __AUTH.__data: 0x188
+521.100.59.0.0
+  __TEXT.__text: 0x85534
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__const: 0x604
+  __TEXT.__cstring: 0x1113a
+  __TEXT.__dof_magmalloc: 0x8c7
+  __TEXT.__unwind_info: 0x818
+  __TEXT.__eh_frame: 0x70
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x118
+  __AUTH_CONST.__const: 0x6c0
+  __AUTH_CONST.__auth_got: 0x348
+  __AUTH.__data: 0x128
   __AUTH.__v_zone: 0x4000
-  __DATA.__data: 0xfc
+  __DATA.__data: 0x104
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x21ac
-  __DATA.__common: 0x214
+  __DATA.__bss: 0x21cc
+  __DATA.__common: 0x220
   - /System/DriverKit/usr/lib/system/libcompiler_rt.dylib
   - /System/DriverKit/usr/lib/system/libdyld.dylib
   - /System/DriverKit/usr/lib/system/libsystem_blocks.dylib

   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  UUID: C531D780-C452-324D-9B84-36988054971D
-  Functions: 904
-  Symbols:   1155
-  CStrings:  660
+  UUID: 686DD919-00B8-3A5C-B734-ECD1879731F5
+  Functions: 999
+  Symbols:   1262
+  CStrings:  862
 
Symbols:
+ _XZM_FAST_ALIGNED
+ _XZM_FAST_MOD
+ ___copy_helper_block_8_32r
+ ___destroy_helper_block_8_32r
+ ___ulock_wait
+ ___ulock_wake
+ ___xzm_ptr_in_use_enumerator_block_invoke_4
+ ___xzm_segment_cache_insert
+ ___xzm_segment_cache_remove
+ ___xzm_statistics_block_invoke_4
+ __block_descriptor_tmp.114
+ __block_descriptor_tmp.120
+ __block_descriptor_tmp.130
+ __block_descriptor_tmp.155
+ __block_descriptor_tmp.160
+ __block_descriptor_tmp.185
+ __block_descriptor_tmp.188
+ __block_descriptor_tmp.191
+ __block_descriptor_tmp.192
+ __block_descriptor_tmp.2
+ __block_descriptor_tmp.28
+ __block_descriptor_tmp.30
+ __block_descriptor_tmp.4
+ __block_descriptor_tmp.6
+ __block_literal_global.187
+ __block_literal_global.190
+ __free
+ __malloc_cpu_cluster_number
+ __malloc_get_cluster_from_cpu
+ __malloc_type_zone_malloc_with_options_np_outlined
+ __malloc_ulock_self_owner_value
+ __malloc_zone_malloc_with_options_np_outlined
+ __platform_strcpy
+ __xzm_allocation_slots_do_lock_action
+ __xzm_chunk_list_fork_lock
+ __xzm_chunk_list_fork_unlock
+ __xzm_chunk_list_pop
+ __xzm_chunk_list_push
+ __xzm_corruption_detected
+ __xzm_fork_lock_wait
+ __xzm_free_outlined
+ __xzm_metapool_block_is_allocated
+ __xzm_metapool_should_madvise
+ __xzm_metapool_slab_for_block
+ __xzm_print_block_invoke.115
+ __xzm_print_block_invoke.121
+ __xzm_print_block_invoke.131
+ __xzm_print_block_invoke.156
+ __xzm_ptr_size_outlined
+ __xzm_range_group_bump_alloc_segment
+ __xzm_segment_group_alloc_huge_chunk_from_cache
+ __xzm_segment_group_bzero_chunk
+ __xzm_segment_group_cache_evict
+ __xzm_segment_group_cache_invalidate
+ __xzm_segment_group_cache_mark_free
+ __xzm_segment_group_cache_mark_used
+ __xzm_segment_group_free_huge_chunk_to_cache
+ __xzm_segment_group_init_segment
+ __xzm_segment_group_span_mark_free
+ __xzm_segment_group_span_mark_used
+ __xzm_segment_group_split_huge_segment
+ __xzm_segment_table_allocated_at
+ __xzm_segment_table_freed_at
+ __xzm_small_xzone_lock_all
+ __xzm_tiny_xzone_do_lock_action
+ __xzm_walk_lock_wait
+ __xzm_xzone_allocation_slot_fork_lock
+ __xzm_xzone_allocation_slot_fork_unlock
+ __xzm_xzone_free_block_to_small_chunk
+ __xzm_xzone_free_tiny
+ __xzm_xzone_madvise_tiny_chunk
+ __xzm_xzone_malloc_from_empty_tiny_chunk
+ __xzm_xzone_malloc_from_fresh_tiny_chunk
+ __xzm_xzone_malloc_from_tiny_chunk
+ __xzm_xzone_malloc_small
+ __xzm_xzone_malloc_tiny
+ __xzm_xzone_malloc_tiny_outlined
+ __xzm_xzone_small_chunk_alloc
+ __xzm_xzone_small_chunk_init
+ __xzm_xzone_tiny_chunk_block_is_free_slow
+ __xzm_xzone_tiny_chunk_lock
+ __xzm_xzone_tiny_chunk_unlock
+ __xzm_xzone_upgrade_small_slot_config
+ _arc4random_buf
+ _disable_unsupported_apis
+ _get_global_helper_zone
+ _get_introspection_addr
+ _get_wrapped_zone
+ _get_wrapper_zone_label
+ _get_zone_type
+ _insert_msl_lite_zone
+ _mach_vm_reclaim_is_reclaimed
+ _malloc_engaged_secure_allocator
+ _malloc_get_wrapped_zone
+ _malloc_type_zone_malloc_with_options_np
+ _malloc_variant_is_debug_4test
+ _malloc_xzone_nano_override
+ _malloc_zone_malloc_with_options_np
+ _mvm_allocate_pages_plat
+ _mvm_allocate_plat
+ _mvm_deallocate_pages_plat
+ _mvm_deallocate_plat
+ _mvm_madvise
+ _mvm_madvise_free_plat
+ _mvm_madvise_plat
+ _mvm_protect_plat
+ _ncpuclusters
+ _pgm_malloc_with_options
+ _reader_or_in_memory_fallback
+ _strcat
+ _xzm_chunk_mark_free
+ _xzm_chunk_mark_used
+ _xzm_malloc_zone_free_definite_size_slow
+ _xzm_malloc_zone_free_slow
+ _xzm_malloc_zone_malloc_slow
+ _xzm_malloc_zone_malloc_with_options
+ _xzm_malloc_zone_malloc_with_options_slow
+ _xzm_malloc_zone_memalign_slow
+ _xzm_malloc_zone_realloc_slow
+ _xzm_malloc_zone_try_free_default_slow
+ _xzm_malloc_zone_valloc_slow
+ _xzm_memalign
+ _xzm_metapool_alloc
+ _xzm_metapool_free
+ _xzm_metapool_init
+ _xzm_range_group_free_segment_body
+ _xzm_reclaim_init
+ _xzm_reclaim_is_available
+ _xzm_reclaim_mark_free
+ _xzm_reclaim_mark_used
+ _xzm_segment_group_try_realloc_huge_chunk
+ _xzm_segment_group_try_realloc_large_chunk
+ _xzm_segment_table_foreach
- ___xzm_print_block_invoke_2
- __block_descriptor_tmp.149
- __block_descriptor_tmp.151
- __block_descriptor_tmp.166
- __block_descriptor_tmp.171
- __block_descriptor_tmp.190
- __block_descriptor_tmp.193
- __block_descriptor_tmp.194
- __block_descriptor_tmp.65
- __block_descriptor_tmp.67
- __block_descriptor_tmp.85
- __block_descriptor_tmp.87
- __block_literal_global.192
- __calloc_get_size
- __xzm_print_block_invoke.150
- __xzm_print_block_invoke.167
- __xzm_segment_map_allocated_at
- __xzm_segment_map_freed_at
- __xzm_segment_map_index_of
- __xzm_xzone_chunk_alloc
- __xzm_xzone_chunk_init
- __xzm_xzone_free
- __xzm_xzone_free_block_to_chunk
- __xzm_xzone_upgrade_slot_config
- _check_introspection
- _create_and_insert_msl_lite_zone
- _get_introspection_ptr
- _pgm_batch_free
- _pgm_batch_malloc
- _pgm_diagnose_fault_from_crash_reporter
- _sanitizer_batch_free
- _sanitizer_batch_malloc
- _szone_basic_zone
- _szone_helper_zone
- _xzm_range_group_free_segment
- _xzm_segment_map_foreach
- _xzm_segment_map_query
CStrings:
+ "                \"atomic_value\": \"0x%llx\",\n"
+ "                \"count\": %u, \n"
+ "                \"head\": \"%p\", \n"
+ "                \"max_count\": %u, \n"
+ "                \"max_entry_slices\": %u, \n"
+ "                \"slot_config\": \"%s\",\n"
+ "                \"tail\": \"%p\" \n"
+ "                \"xsc_ptr\": \"0x%llx\",\n"
+ "                \"xsg_locked\": \"0x%llx\",\n"
+ "                \"xsg_waiters\": \"0x%llx\",\n"
+ "        \"alloc_idx\": %u,\n"
+ "        \"body_addr\": \"%p\", \n"
+ "        \"cache_next\": \"%p\", \n"
+ "        \"cache_prev\": \"%p\", \n"
+ "        \"free\": \"0x%x\",\n"
+ "        \"id\": \"%s\"\n"
+ "        \"is_pristine\": %d\n"
+ "        \"meta\": \"0x%llx\",\n"
+ "        \"metadata_addr\": \"%p\", \n"
+ "        \"reclaim_index\": %llu, \n"
+ "        \"segment_cache\": { \n"
+ "        \"segment_group\": \"%p\", \n"
+ "        \"size\": %u \n"
+ "        \"slice_entry_count\": %u \n"
+ "        \"used\": %u, \n"
+ "        \"xca_alloc_head\": \"0x%llx\",\n"
+ "        \"xca_alloc_idx\": \"0x%llx\",\n"
+ "        \"xca_free_count\": \"0x%llx\",\n"
+ "        \"xca_head_seqno\": \"0x%llx\",\n"
+ "        \"xca_on_empty_list\": \"0x%llx\",\n"
+ "        \"xca_on_partial_list\": \"0x%llx\",\n"
+ "        \"xca_seqno\": \"0x%llx\",\n"
+ "        \"xca_walk_locked\": \"0x%llx\",\n"
+ "        } \n"
+ "-"
+ "/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c"
+ "/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist"
+ "BUG IN CLIENT OF LIBMALLOC: memory corruption of free block"
+ "BUG IN CLIENT OF LIBMALLOC: pointer being reallocated with wrong zone"
+ "BUG IN LIBMALLOC: Failed to allocate malloc metadata"
+ "BUG IN LIBMALLOC: Failed to compute metapools size"
+ "BUG IN LIBMALLOC: Failed to map metapool slab"
+ "BUG IN LIBMALLOC: Failed to map segment table"
+ "BUG IN LIBMALLOC: Failed to query vm stats"
+ "BUG IN LIBMALLOC: Failed to rebase metapools"
+ "BUG IN LIBMALLOC: Slice count too large in init_segment"
+ "BUG IN LIBMALLOC: attempting to allocate from chunk of bad kind"
+ "BUG IN LIBMALLOC: attempting to coalesce slice of unexpected type"
+ "BUG IN LIBMALLOC: failed to compute allocation slots size"
+ "BUG IN LIBMALLOC: failed to compute extended segment table size"
+ "BUG IN LIBMALLOC: failed to compute range group size"
+ "BUG IN LIBMALLOC: failed to compute segment group size"
+ "BUG IN LIBMALLOC: failed to compute segment table size"
+ "BUG IN LIBMALLOC: failed to compute xzone array size"
+ "BUG IN LIBMALLOC: failed to rebase segment table"
+ "BUG IN LIBMALLOC: loop in freelist"
+ "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1625)"
+ "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1822)"
+ "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1861)"
+ "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1913)"
+ "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1927)"
+ "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2411)"
+ "BUG IN LIBMALLOC: malloc assertion \"!_xzm_slice_kind_uses_xzones(chunk->xzc_bits.xzcb_kind) || block_index < xz->xz_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2732)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1116)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_has_aligned\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1557)"
+ "BUG IN LIBMALLOC: malloc assertion \"!clear || chunk->xzc_bits.xzcb_is_pristine\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:208)"
+ "BUG IN LIBMALLOC: malloc assertion \"!full_segment || _xzm_segment_start(metadata) == data\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:102)"
+ "BUG IN LIBMALLOC: malloc assertion \"!huge\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:315)"
+ "BUG IN LIBMALLOC: malloc assertion \"!metadata_pool || metadata_pool->xzmp_block_size >= sizeof(struct xzm_metapool_block_s)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:27)"
+ "BUG IN LIBMALLOC: malloc assertion \"!metadata_pool || metadata_pool->xzmp_block_size >= sizeof(struct xzm_metapool_slab_s)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:25)"
+ "BUG IN LIBMALLOC: malloc assertion \"!old_head.xzch_fork_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:290)"
+ "BUG IN LIBMALLOC: malloc assertion \"!old_meta.xca_on_empty_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1371)"
+ "BUG IN LIBMALLOC: malloc assertion \"!old_meta.xca_on_empty_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:432)"
+ "BUG IN LIBMALLOC: malloc assertion \"!old_meta.xca_on_empty_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:510)"
+ "BUG IN LIBMALLOC: malloc assertion \"!old_meta.xca_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1495)"
+ "BUG IN LIBMALLOC: malloc assertion \"!old_meta.xca_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:509)"
+ "BUG IN LIBMALLOC: malloc assertion \"!old_meta.xca_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:692)"
+ "BUG IN LIBMALLOC: malloc assertion \"!old_meta.xca_walk_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2489)"
+ "BUG IN LIBMALLOC: malloc assertion \"!ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1098)"
+ "BUG IN LIBMALLOC: malloc assertion \"!segment || (slice >= segment->xzs_slices && slice < (segment->xzs_slices + segment->xzs_slice_entry_count))\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:253)"
+ "BUG IN LIBMALLOC: malloc assertion \"!span_enumerator || zone_is_main\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_introspect.c:249)"
+ "BUG IN LIBMALLOC: malloc assertion \"!xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2806)"
+ "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:182)"
+ "BUG IN LIBMALLOC: malloc assertion \"(ptr && chunk) || (!ptr && !chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1167)"
+ "BUG IN LIBMALLOC: malloc assertion \"(required_bytes == 0 && huge_chunk == NULL) || (required_bytes > 0 && huge_chunk != NULL)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1246)"
+ "BUG IN LIBMALLOC: malloc assertion \"(slice_count > XZM_LARGE_BLOCK_SIZE_MAX / XZM_SEGMENT_SLICE_SIZE) || (alignment > XZM_ALIGNMENT_MAX)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1494)"
+ "BUG IN LIBMALLOC: malloc assertion \"(start_address >= left_void.min_address && end_address + XZM_RANGE_SEPARATION <= left_void.max_address) || (start_address >= right_void.min_address + XZM_RANGE_SEPARATION && start_address + XZM_POINTER_RANGE_SIZE <= right_void.max_address)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:568)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body % XZM_SEGMENT_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1198)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1196)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)data % XZM_SEGMENT_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:36)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)data < (uintptr_t)segment_end\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:39)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment % XZM_METAPOOL_SEGMENT_ALIGN == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:178)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment % XZM_METAPOOL_SEGMENT_ALIGN == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1197)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1195)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1276)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)slice >= (uintptr_t)segment->xzs_slices\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:270)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)slice_start % XZM_SEGMENT_SLICE_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2000)"
+ "BUG IN LIBMALLOC: malloc assertion \"*reclaim_index != VM_RECLAIM_INDEX_NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:943)"
+ "BUG IN LIBMALLOC: malloc assertion \"*reclaim_index != VM_RECLAIM_INDEX_NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:979)"
+ "BUG IN LIBMALLOC: malloc assertion \"*reclaim_index == VM_RECLAIM_INDEX_NULL || !slice->xzc_bits.xzcb_is_pristine\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:871)"
+ "BUG IN LIBMALLOC: malloc assertion \"*reclaim_index == VM_RECLAIM_INDEX_NULL || !slice->xzc_bits.xzcb_is_pristine\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:897)"
+ "BUG IN LIBMALLOC: malloc assertion \"*reclaim_index == VM_RECLAIM_INDEX_NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:923)"
+ "BUG IN LIBMALLOC: malloc assertion \"*reclaim_index == VM_RECLAIM_INDEX_NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:963)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main(zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3368)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_mem_is_zero(ptr, size)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2040)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_mem_is_zero(ptr, size)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2083)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_metapool_block_is_allocated(mp, blockp)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:195)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_end(segment) == remainder\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1852)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_for_slice(&sg->xzsg_main_ref->xzmz_base, chunk) == segment\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2086)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_for_slice(&sg->xzsg_main_ref->xzmz_base, chunk) == segment\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2180)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_for_slice(&sg->xzsg_main_ref->xzmz_base, span) == segment\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1051)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1179)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1228)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2047)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2075)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2136)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2232)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2240)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_uses_deferred_reclamation(sg)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:918)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_uses_deferred_reclamation(sg)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:933)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_to_segment_table_entry(metadata).xste_val == entry->xste_val\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:108)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(chunk->xzc_bits.xzcb_kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2009)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(chunk->xzc_bits.xzcb_kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:960)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(chunk->xzc_bits.xzcb_kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:976)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1079)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1138)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2022)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_free_span(kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:788)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_free_span(span->xzc_bits.xzcb_kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:919)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_free_span(span->xzc_bits.xzcb_kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:934)"
+ "BUG IN LIBMALLOC: malloc assertion \"adjust <= alignment\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2097)"
+ "BUG IN LIBMALLOC: malloc assertion \"align_pow < UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:215)"
+ "BUG IN LIBMALLOC: malloc assertion \"aligned == ((offs % size) == 0)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:134)"
+ "BUG IN LIBMALLOC: malloc assertion \"alignment % XZM_SEGMENT_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1371)"
+ "BUG IN LIBMALLOC: malloc assertion \"alignment == 0 || (start % alignment) == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1396)"
+ "BUG IN LIBMALLOC: malloc assertion \"alignment == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1498)"
+ "BUG IN LIBMALLOC: malloc assertion \"alignment == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:357)"
+ "BUG IN LIBMALLOC: malloc assertion \"bin < XZM_SPAN_QUEUE_COUNT\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:768)"
+ "BUG IN LIBMALLOC: malloc assertion \"block\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:161)"
+ "BUG IN LIBMALLOC: malloc assertion \"block_index <= xz->xz_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1676)"
+ "BUG IN LIBMALLOC: malloc assertion \"block_offset == XZM_FREE_NULL || block_offset == XZM_FREE_BUMP\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_introspect.c:215)"
+ "BUG IN LIBMALLOC: malloc assertion \"block_ptr % mp->xzmp_block_size == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:170)"
+ "BUG IN LIBMALLOC: malloc assertion \"block_size >= block_align\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:16)"
+ "BUG IN LIBMALLOC: malloc assertion \"body_size % XZM_SEGMENT_SLICE_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1199)"
+ "BUG IN LIBMALLOC: malloc assertion \"boothash_prefix_value <= UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3769)"
+ "BUG IN LIBMALLOC: malloc assertion \"bucket < bin_bucket_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:95)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->xzsc_count < cache->xzsc_max_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:660)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->xzsc_count > 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:652)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->xzsc_max_count > 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1863)"
+ "BUG IN LIBMALLOC: malloc assertion \"candidate_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:543)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1177)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1422)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_enqueued\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1818)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_enqueued\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2373)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_HUGE_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2183)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_HUGE_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:820)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_LARGE_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2091)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:705)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:817)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:827)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:888)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_TINY_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:397)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_TINY_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:646)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_TINY_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:730)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == kind\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2599)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_free == XZM_BLOCK_NULL || chunk->xzc_free == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1555)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_mzone_idx == XZM_MZONE_INDEX_INVALID\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1558)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_used == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1556)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzcs_slice_count == segment->xzs_slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:821)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk_size_out\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:343)"
+ "BUG IN LIBMALLOC: malloc assertion \"current_slot_config < next_slot_config\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:838)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_rg->xzrg_id == XZM_RANGE_GROUP_DATA\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:629)"
+ "BUG IN LIBMALLOC: malloc assertion \"diff % XZM_SEGMENT_SLICE_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2315)"
+ "BUG IN LIBMALLOC: malloc assertion \"diff >= 0 && diff < (ptrdiff_t)XZM_SEGMENT_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:419)"
+ "BUG IN LIBMALLOC: malloc assertion \"diff >= 0 && diff < (ptrdiff_t)_xzm_segment_size(segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:404)"
+ "BUG IN LIBMALLOC: malloc assertion \"entry != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:106)"
+ "BUG IN LIBMALLOC: malloc assertion \"entry != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:83)"
+ "BUG IN LIBMALLOC: malloc assertion \"entry->xste_val == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:689)"
+ "BUG IN LIBMALLOC: malloc assertion \"entry->xste_val == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:85)"
+ "BUG IN LIBMALLOC: malloc assertion \"first <= last\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:916)"
+ "BUG IN LIBMALLOC: malloc assertion \"huge || alignment == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1251)"
+ "BUG IN LIBMALLOC: malloc assertion \"index < (ptrdiff_t)segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:272)"
+ "BUG IN LIBMALLOC: malloc assertion \"kind != XZM_SLICE_KIND_TINY_CHUNK || slice_count == 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1139)"
+ "BUG IN LIBMALLOC: malloc assertion \"last >= first\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:828)"
+ "BUG IN LIBMALLOC: malloc assertion \"last->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_BODY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:853)"
+ "BUG IN LIBMALLOC: malloc assertion \"last->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_BODY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:889)"
+ "BUG IN LIBMALLOC: malloc assertion \"last->xzsl_slice_offset_bytes == (uint32_t)(sizeof(struct xzm_slice_s) * (slice_count - 1))\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:856)"
+ "BUG IN LIBMALLOC: malloc assertion \"last->xzsl_slice_offset_bytes == (uint32_t)(sizeof(struct xzm_slice_s) * (slice_count - 1))\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:891)"
+ "BUG IN LIBMALLOC: malloc assertion \"last_slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1103)"
+ "BUG IN LIBMALLOC: malloc assertion \"last_slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:849)"
+ "BUG IN LIBMALLOC: malloc assertion \"last_slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:885)"
+ "BUG IN LIBMALLOC: malloc assertion \"left >= _xzm_chunk_start(zone, chunk, NULL)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2299)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:517)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:480)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:479)"
+ "BUG IN LIBMALLOC: malloc assertion \"main\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_introspect.c:542)"
+ "BUG IN LIBMALLOC: malloc assertion \"main->xzmz_deferred_reclamation\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:959)"
+ "BUG IN LIBMALLOC: malloc assertion \"main->xzmz_deferred_reclamation\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:975)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_introspect.c:543)"
+ "BUG IN LIBMALLOC: malloc assertion \"meta.xca_free_count <= capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_introspect.c:179)"
+ "BUG IN LIBMALLOC: malloc assertion \"meta.xca_free_count == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_introspect.c:174)"
+ "BUG IN LIBMALLOC: malloc assertion \"metadata_pool || block_size >= sizeof(struct xzm_metapool_slab_s)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:20)"
+ "BUG IN LIBMALLOC: malloc assertion \"new_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2856)"
+ "BUG IN LIBMALLOC: malloc assertion \"new_slice_count <= (XZM_LARGE_BLOCK_SIZE_MAX / XZM_SEGMENT_SLICE_SIZE)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2090)"
+ "BUG IN LIBMALLOC: malloc assertion \"new_slice_count > (XZM_LARGE_BLOCK_SIZE_MAX / XZM_SEGMENT_SLICE_SIZE)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2182)"
+ "BUG IN LIBMALLOC: malloc assertion \"new_slice_count > (XZM_SMALL_BLOCK_SIZE_MAX / XZM_SEGMENT_SLICE_SIZE)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:2088)"
+ "BUG IN LIBMALLOC: malloc assertion \"offs % size == mod\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:124)"
+ "BUG IN LIBMALLOC: malloc assertion \"offset < chunk_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:798)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_head.xzch_fork_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:304)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_meta.xca_alloc_head == XZM_FREE_BUMP\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:538)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_meta.xca_alloc_head == XZM_FREE_MADVISED\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:662)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_meta.xca_alloc_head == XZM_FREE_MADVISING\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1353)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_meta.xca_alloc_head == XZM_FREE_MADVISING\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:451)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_meta.xca_alloc_head == XZM_FREE_NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:503)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_meta.xca_alloc_idx == XZM_SLOT_INDEX_EMPTY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:430)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_meta.xca_alloc_idx == XZM_SLOT_INDEX_EMPTY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:693)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_meta.xca_on_empty_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:691)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_meta.xca_on_partial_list\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:431)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3118)"
+ "BUG IN LIBMALLOC: malloc assertion \"out_slice >= ((xzm_segment_t)((uintptr_t)slice & ~(XZM_METAPOOL_SEGMENT_BLOCK_SIZE - 1)))->xzs_slices\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:536)"
+ "BUG IN LIBMALLOC: malloc assertion \"powerof2(align)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:238)"
+ "BUG IN LIBMALLOC: malloc assertion \"powerof2(alignment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2108)"
+ "BUG IN LIBMALLOC: malloc assertion \"powerof2(block_align)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:15)"
+ "BUG IN LIBMALLOC: malloc assertion \"powerof2(block_size)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:14)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_meta.xasa_gate.xsg_gen == slot_meta.xasa_gate.xsg_gen\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1190)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_meta.xasa_gate.xsg_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1186)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_meta.xasa_gate.xsg_owner == self_owner_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1187)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_meta.xasa_gate.xsg_unused == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1188)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:997)"
+ "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1160)"
+ "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1931)"
+ "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2000)"
+ "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2038)"
+ "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2081)"
+ "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2125)"
+ "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2855)"
+ "BUG IN LIBMALLOC: malloc assertion \"ptr_offset\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2710)"
+ "BUG IN LIBMALLOC: malloc assertion \"ptr_rg->xzrg_id == XZM_RANGE_GROUP_PTR\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:621)"
+ "BUG IN LIBMALLOC: malloc assertion \"rg->xzrg_id == XZM_RANGE_GROUP_DATA\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:289)"
+ "BUG IN LIBMALLOC: malloc assertion \"rg->xzrg_id == XZM_RANGE_GROUP_DATA\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:366)"
+ "BUG IN LIBMALLOC: malloc assertion \"rg->xzrg_id == XZM_RANGE_GROUP_PTR\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:314)"
+ "BUG IN LIBMALLOC: malloc assertion \"right <= (_xzm_chunk_start(zone, chunk, NULL) + (chunk->xzcs_slice_count * XZM_SEGMENT_SLICE_SIZE))\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2310)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:537)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:482)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:481)"
+ "BUG IN LIBMALLOC: malloc assertion \"segindex < XZM_SEGMENT_TABLE_ENTRIES\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:161)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2874)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_kind != XZM_SEGMENT_KIND_HUGE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1019)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_kind != XZM_SEGMENT_KIND_HUGE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1054)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_kind == XZM_SEGMENT_KIND_HUGE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1769)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_kind == XZM_SEGMENT_KIND_HUGE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1959)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_reclaim_index != VM_RECLAIM_INDEX_NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:724)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_reclaim_index == VM_RECLAIM_INDEX_NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:691)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_segment_group == sg\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:812)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_slice_count >= required_slices\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1770)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_used == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1710)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_used == 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1960)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_used == 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:818)"
+ "BUG IN LIBMALLOC: malloc assertion \"segment_addr % size == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:269)"
+ "BUG IN LIBMALLOC: malloc assertion \"self_owner_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1093)"
+ "BUG IN LIBMALLOC: malloc assertion \"sg->xzsg_id == XZM_SEGMENT_GROUP_DATA\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1370)"
+ "BUG IN LIBMALLOC: malloc assertion \"size <= UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:135)"
+ "BUG IN LIBMALLOC: malloc assertion \"size <= UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:160)"
+ "BUG IN LIBMALLOC: malloc assertion \"size <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2008)"
+ "BUG IN LIBMALLOC: malloc assertion \"size <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:36)"
+ "BUG IN LIBMALLOC: malloc assertion \"size == XZM_SEGMENT_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:316)"
+ "BUG IN LIBMALLOC: malloc assertion \"size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3072)"
+ "BUG IN LIBMALLOC: malloc assertion \"slab_size % PAGE_MAX_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:13)"
+ "BUG IN LIBMALLOC: malloc assertion \"slab_size % block_size == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_metapool.c:12)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice >= span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:514)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_BODY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:843)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice->xzc_mzone_idx == XZM_MZONE_INDEX_INVALID\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:865)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice->xzc_mzone_idx == XZM_MZONE_INDEX_INVALID\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:877)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice->xzsl_slice_offset_bytes == (uint32_t)(sizeof(struct xzm_slice_s) * i)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:845)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_count != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1002)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_count != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1140)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_count != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:747)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_count * XZM_SEGMENT_SLICE_SIZE <= XZM_LARGE_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1142)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_count * XZM_SEGMENT_SLICE_SIZE <= XZM_SEGMENT_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:764)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_count <= XZM_SLICES_PER_SEGMENT\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:752)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_count == 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1118)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_count > 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:837)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_count > 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:882)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_index + slice_count - 1 < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1025)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1003)"
+ "BUG IN LIBMALLOC: malloc assertion \"slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1080)"
+ "BUG IN LIBMALLOC: malloc assertion \"slot_config < XZM_SLOT_LAST\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:105)"
+ "BUG IN LIBMALLOC: malloc assertion \"slot_meta.xasa_chunk.xsc_fork_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:990)"
+ "BUG IN LIBMALLOC: malloc assertion \"slot_meta.xasa_gate.xsg_locked\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:912)"
+ "BUG IN LIBMALLOC: malloc assertion \"span <= 32\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:834)"
+ "BUG IN LIBMALLOC: malloc assertion \"span->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_FREE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1052)"
+ "BUG IN LIBMALLOC: malloc assertion \"span->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_FREE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1734)"
+ "BUG IN LIBMALLOC: malloc assertion \"span->xzcs_slice_count == segment->xzs_slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1735)"
+ "BUG IN LIBMALLOC: malloc assertion \"span->xzcs_slice_count > slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1053)"
+ "BUG IN LIBMALLOC: malloc assertion \"sq->xzsq_slice_count >= slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:778)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2522)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:710)"
+ "BUG IN LIBMALLOC: malloc assertion \"vm_addr % XZM_SEGMENT_SLICE_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:161)"
+ "BUG IN LIBMALLOC: malloc assertion \"vm_addr % align == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:255)"
+ "BUG IN LIBMALLOC: malloc assertion \"vm_addr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:254)"
+ "BUG IN LIBMALLOC: malloc assertion \"vm_size % XZM_SEGMENT_SLICE_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:162)"
+ "BUG IN LIBMALLOC: malloc assertion \"xas\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1521)"
+ "BUG IN LIBMALLOC: malloc assertion \"xas->xas_chunk == chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1926)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3557)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz->xz_block_size > XZM_TINY_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3270)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz->xz_slot_config <= zone->xzz_max_slot_config\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1746)"
+ "BUG IN LIBMALLOC: malloc assertion \"xzm_slice_bin8(XZM_SLICES_PER_SEGMENT) < XZM_SPAN_QUEUE_COUNT\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:766)"
+ "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:3868)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_introspect.c:541)"
+ "BUG IN LIBMALLOC: pointer range initial overwrite failed"
+ "BUG IN LIBMALLOC: pointer range mach_vm_map() overwrite failed"
+ "BUG IN LIBMALLOC: ulock_wait failure"
+ "BUG IN LIBMALLOC: ulock_wake failure"
+ "Failed to allocate memory at address 0x%lx of size 0x%lx with flags %d\n"
+ "Failed to allocate segment (size=%lu, flags=%x, kr=%d)\n"
+ "Failed to allocate segment - out of space\n"
+ "Failed to deallocate at address %p of size 0x%lx\n"
+ "Failed to madvise(MADV_ZERO) chunk at %p, error: %d\n"
+ "MallocDeferredReclaim"
+ "MallocDeferredReclaim must be one of 0,1 - got %ld\n"
+ "MallocSecureAllocatorNano"
+ "MallocSecureAllocatorNano must be 0 or 1.\n"
+ "MallocXzoneHugeCacheSize"
+ "MallocXzoneInitialSlotConfig"
+ "MallocXzonePtrBucketCount"
+ "MallocXzoneSlotUpgradeThresholdCluster"
+ "MallocXzoneSlotUpgradeThresholdSingle"
+ "Maximum magazines limited to number of logical CPU clusters (%d)\n"
+ "PGM"
+ "Sanitizer"
+ "Unsupported anywhere allocation at address 0x%lx of size 0x%lx with flags %d\n"
+ "Unsupported unpopulated allocation at address 0x%lx of size 0x%lx with flags %d\n"
+ "Unsupported wrapped zone version: %u\n"
+ "Wrapped"
+ "data"
+ "huge_segment"
+ "i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}8I16"
+ "i24@?0Q8Q16"
+ "i24@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}{qm_trace=*i*i}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}]}16"
+ "i28@?0Q8Q16C24"
+ "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}{qm_trace=*i*i}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}{qm_trace=*i*i}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{os_unfair_lock_s=I}}{?=(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)})S^{xzm_segment_group_s}QQIICCCCb1}44^{?=QQ}52Q60"
+ "malloc_with_options (%p/%llu,%llu): "
+ "metapool metadata slab"
+ "normal_segment"
+ "pointer_large"
+ "pointer_xzones"
+ "segment metadata slab"
+ "unknown slab"
+ "xzm: failed to initialize deferred reclamation buffer\n"
+ "xzm: unsupported value for MallocXzoneHugeCacheSize (%ld)"
- "        \"free\": \"0x%x\"\n"
- "        \"id\": %d\n"
- "        \"is_zero\": %d,\n"
- "BUG IN LIBMALLOC: Failed to deallocate segment"
- "BUG IN LIBMALLOC: Failed to query vm stats for segment"
- "BUG IN LIBMALLOC: Failed to unprotect reserved space for ptr segment"
- "BUG IN LIBMALLOC: attempting to allocation from chunk of bad kind"
- "BUG IN LIBMALLOC: attempting to bump a fully used tiny chunk"
- "BUG IN LIBMALLOC: couldn't find executable_boothash"
- "BUG IN LIBMALLOC: failed to rebase segment map"
- "BUG IN LIBMALLOC: malloc assertion \"!(oldval & bit)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:55)"
- "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:287)"
- "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:522)"
- "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:557)"
- "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:573)"
- "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:587)"
- "BUG IN LIBMALLOC: malloc assertion \"!_xzm_chunk_is_full(zone, xz, chunk)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:915)"
- "BUG IN LIBMALLOC: malloc assertion \"!allow_inner\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:80)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_has_aligned\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:220)"
- "BUG IN LIBMALLOC: malloc assertion \"!clear || chunk->xzc_bits.xzcb_is_zero\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:172)"
- "BUG IN LIBMALLOC: malloc assertion \"!huge\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:198)"
- "BUG IN LIBMALLOC: malloc assertion \"!segment || (slice >= segment->xzs_slices && slice < (segment->xzs_slices + segment->xzs_slice_entry_count))\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:92)"
- "BUG IN LIBMALLOC: malloc assertion \"!span_enumerator || zone_is_main\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1430)"
- "BUG IN LIBMALLOC: malloc assertion \"(oldval & bit)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:71)"
- "BUG IN LIBMALLOC: malloc assertion \"(required_bytes == 0 && huge_chunk == NULL) || (required_bytes > 0 && huge_chunk != NULL)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:853)"
- "BUG IN LIBMALLOC: malloc assertion \"(start_address >= left_void.min_address && end_address + XZM_RANGE_SEPARATION <= left_void.max_address) || (start_address >= right_void.min_address + XZM_RANGE_SEPARATION && start_address + XZM_POINTER_RANGE_SIZE <= right_void.max_address)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:418)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment % XZM_SEGMENT_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:905)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:896)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)slice >= (uintptr_t)segment->xzs_slices\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:483)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main(zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2122)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_mem_is_zero(ptr, size)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:635)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_ptr_segment(span) == segment\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:722)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1287)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1300)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:827)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_segment_group_segment_is_valid(sg, segment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:929)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(chunk->xzc_bits.xzcb_kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1131)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(chunk->xzc_bits.xzcb_kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1251)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:741)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_chunk(kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:795)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_slice_kind_is_free_span(kind)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:563)"
- "BUG IN LIBMALLOC: malloc assertion \"adjust <= alignment\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:675)"
- "BUG IN LIBMALLOC: malloc assertion \"bin < XZM_SPAN_QUEUE_COUNT\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:490)"
- "BUG IN LIBMALLOC: malloc assertion \"block_index <= xz->xz_chunk_capacity\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:335)"
- "BUG IN LIBMALLOC: malloc assertion \"boothash_prefix_value <= UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2656)"
- "BUG IN LIBMALLOC: malloc assertion \"bucket < bin_bucket_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:86)"
- "BUG IN LIBMALLOC: malloc assertion \"candidate_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:393)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk + chunk->xzcs_slice_count > slice\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:211)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk >= _xzm_ptr_segment(slice)->xzs_slices\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:210)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:826)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:967)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_enqueued\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:518)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_enqueued\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:877)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_HUGE_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:595)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:455)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:465)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_bits.xzcb_kind == XZM_SLICE_KIND_SMALL_CHUNK\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:502)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_free == XZM_BLOCK_NULL || chunk->xzc_free == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:218)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_mzone_idx == XZM_MZONE_INDEX_INVALID\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:221)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_used == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:219)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzcs_slice_count < segment->xzs_slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:596)"
- "BUG IN LIBMALLOC: malloc assertion \"diff % XZM_SEGMENT_SLICE_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:831)"
- "BUG IN LIBMALLOC: malloc assertion \"diff >= 0 && diff < (ptrdiff_t)XZM_SEGMENT_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:147)"
- "BUG IN LIBMALLOC: malloc assertion \"diff >= 0 && diff < (ptrdiff_t)XZM_SEGMENT_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:163)"
- "BUG IN LIBMALLOC: malloc assertion \"first <= last\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:530)"
- "BUG IN LIBMALLOC: malloc assertion \"index < (ptrdiff_t)segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:485)"
- "BUG IN LIBMALLOC: malloc assertion \"index < XZM_SEGMENT_MAP_WORDS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:47)"
- "BUG IN LIBMALLOC: malloc assertion \"index < XZM_SEGMENT_MAP_WORDS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:64)"
- "BUG IN LIBMALLOC: malloc assertion \"kind != XZM_SLICE_KIND_TINY_CHUNK || slice_count == 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:796)"
- "BUG IN LIBMALLOC: malloc assertion \"last >= first\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:466)"
- "BUG IN LIBMALLOC: malloc assertion \"last->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_BODY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:628)"
- "BUG IN LIBMALLOC: malloc assertion \"last->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_BODY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:657)"
- "BUG IN LIBMALLOC: malloc assertion \"last->xzsl_slice_offset_bytes == (uint32_t)(sizeof(struct xzm_slice_s) * (slice_count - 1))\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:631)"
- "BUG IN LIBMALLOC: malloc assertion \"last->xzsl_slice_offset_bytes == (uint32_t)(sizeof(struct xzm_slice_s) * (slice_count - 1))\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:659)"
- "BUG IN LIBMALLOC: malloc assertion \"last_slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:624)"
- "BUG IN LIBMALLOC: malloc assertion \"last_slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:653)"
- "BUG IN LIBMALLOC: malloc assertion \"last_slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:765)"
- "BUG IN LIBMALLOC: malloc assertion \"left >= _xzm_chunk_start(zone, chunk, NULL)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:815)"
- "BUG IN LIBMALLOC: malloc assertion \"left_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:367)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:327)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:326)"
- "BUG IN LIBMALLOC: malloc assertion \"main\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1320)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1321)"
- "BUG IN LIBMALLOC: malloc assertion \"mapindex < XZM_SEGMENT_MAP_WORDS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:36)"
- "BUG IN LIBMALLOC: malloc assertion \"offset < chunk_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:437)"
- "BUG IN LIBMALLOC: malloc assertion \"powerof2(alignment)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:686)"
- "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:591)"
- "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:633)"
- "BUG IN LIBMALLOC: malloc assertion \"ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:696)"
- "BUG IN LIBMALLOC: malloc assertion \"rg->xzrg_id == XZM_RANGE_GROUP_DATA\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:181)"
- "BUG IN LIBMALLOC: malloc assertion \"rg->xzrg_id == XZM_RANGE_GROUP_DATA\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:250)"
- "BUG IN LIBMALLOC: malloc assertion \"rg->xzrg_id == XZM_RANGE_GROUP_PTR\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:197)"
- "BUG IN LIBMALLOC: malloc assertion \"rg->xzrg_id == XZM_RANGE_GROUP_PTR\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:453)"
- "BUG IN LIBMALLOC: malloc assertion \"right <= (_xzm_chunk_start(zone, chunk, NULL) + (chunk->xzcs_slice_count * XZM_SEGMENT_SLICE_SIZE))\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:826)"
- "BUG IN LIBMALLOC: malloc assertion \"right_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:387)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:329)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:328)"
- "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_kind != XZM_SEGMENT_KIND_HUGE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:725)"
- "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_kind == XZM_SEGMENT_KIND_HUGE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1207)"
- "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_segment_group == sg\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:587)"
- "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_used == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1183)"
- "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_used == 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1208)"
- "BUG IN LIBMALLOC: malloc assertion \"segment->xzs_used == 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:593)"
- "BUG IN LIBMALLOC: malloc assertion \"segment_addr % XZM_SEGMENT_SIZE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:209)"
- "BUG IN LIBMALLOC: malloc assertion \"sg->xzsg_id == XZM_SEGMENT_GROUP_DATA\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:943)"
- "BUG IN LIBMALLOC: malloc assertion \"size <= XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:30)"
- "BUG IN LIBMALLOC: malloc assertion \"size == XZM_SEGMENT_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:199)"
- "BUG IN LIBMALLOC: malloc assertion \"slice->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_BODY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:618)"
- "BUG IN LIBMALLOC: malloc assertion \"slice->xzc_mzone_idx == XZM_MZONE_INDEX_INVALID\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:640)"
- "BUG IN LIBMALLOC: malloc assertion \"slice->xzc_mzone_idx == XZM_MZONE_INDEX_INVALID\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:645)"
- "BUG IN LIBMALLOC: malloc assertion \"slice->xzsl_slice_offset_bytes == (uint32_t)(sizeof(struct xzm_slice_s) * i)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:620)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:469)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:681)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:797)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count * XZM_SEGMENT_SLICE_SIZE <= XZM_LARGE_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:799)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count * XZM_SEGMENT_SLICE_SIZE <= XZM_SEGMENT_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:486)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count <= XZM_SLICES_PER_SEGMENT\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:474)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count == 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:780)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count > 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:612)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count > 1\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:650)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_count > XZM_LARGE_BLOCK_SIZE_MAX / XZM_SEGMENT_SLICE_SIZE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1015)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_index + slice_count - 1 < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:683)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:682)"
- "BUG IN LIBMALLOC: malloc assertion \"slice_index < segment->xzs_slice_entry_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:742)"
- "BUG IN LIBMALLOC: malloc assertion \"slot_config < XZM_SLOT_LAST\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:96)"
- "BUG IN LIBMALLOC: malloc assertion \"span <= 32\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/../xzone/xzone_inline_internal.h:472)"
- "BUG IN LIBMALLOC: malloc assertion \"span->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_FREE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1188)"
- "BUG IN LIBMALLOC: malloc assertion \"span->xzc_bits.xzcb_kind == XZM_SLICE_KIND_MULTI_FREE\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:723)"
- "BUG IN LIBMALLOC: malloc assertion \"span->xzcs_slice_count == segment->xzs_slice_count - segment->xzs_header_slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:1190)"
- "BUG IN LIBMALLOC: malloc assertion \"span->xzcs_slice_count > slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:724)"
- "BUG IN LIBMALLOC: malloc assertion \"sq->xzsq_slice_count >= slice_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:500)"
- "BUG IN LIBMALLOC: malloc assertion \"vm_addr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:173)"
- "BUG IN LIBMALLOC: malloc assertion \"xas->xas_chunk == chunk\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:586)"
- "BUG IN LIBMALLOC: malloc assertion \"xz->xz_slot_config <= zone->xzz_max_slot_config\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:424)"
- "BUG IN LIBMALLOC: malloc assertion \"xzm_slice_bin8(XZM_SLICES_PER_SEGMENT) < XZM_SPAN_QUEUE_COUNT\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_segment.c:488)"
- "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:2696)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:1319)"
- "BUG IN LIBMALLOC: support for given alignment not yet implemented"
- "Can't deallocate_pages region at %p\n"
- "Failed to allocate ptr segment - out of space\n"
- "Failed to allocate segment (size=%zu, flags=%x, kr=%d)\n"
- "Failed to deallocate segment %p: %d\n"
- "Failed to madvise slice span of len %d at %p, error: %d\n"
- "batch_free(%p, 0x%x)\n"
- "batch_malloc(0x%lx, %p, 0x%x)\n"
- "i20@?0^{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}8I16"
- "i24@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIIC[256{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}]}16"
- "i36@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIIC[256{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}]}16Q24I32"
- "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIIC[256{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}]}16^{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}24I32Q36"
- "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIIC[256{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}]}16^{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}24I32Q36^{xzm_xzone_s={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{os_unfair_lock_s=I}}S^{xzm_segment_group_s}QICCCCb1}44^{?=QQ}52Q60"

```
