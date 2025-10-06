## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-474.0.13.0.0
-  __TEXT.__text: 0x267b0
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__const: 0x624
-  __TEXT.__cstring: 0x5f0f
-  __TEXT.__dof_magmalloc: 0x90d
-  __TEXT.__unwind_info: 0x6bc
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x678
-  __AUTH_CONST.__const: 0x408
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH.__data: 0x100
+521.100.59.0.0
+  __TEXT.__text: 0x2c410
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__const: 0x62c
+  __TEXT.__cstring: 0x722f
+  __TEXT.__dof_magmalloc: 0x912
+  __TEXT.__unwind_info: 0x790
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x788
+  __AUTH_CONST.__const: 0x4d0
+  __AUTH_CONST.__auth_got: 0x338
+  __AUTH.__data: 0xa0
   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0x170
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x48
-  __DATA.__bss: 0x8d
+  __DATA.__bss: 0x65
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__common: 0x1d8
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0xcc
+  __DATA_DIRTY.__common: 0x1e8
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 497FCDB3-4B35-3796-A127-C3D11E4B57B2
-  Functions: 707
-  Symbols:   1548
-  CStrings:  570
+  UUID: F74B80B7-015E-3C57-817C-5BA1A0E0A4FF
+  Functions: 790
+  Symbols:   1721
+  CStrings:  677
 
Symbols:
+ ___block_descriptor_tmp.11
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.116
+ ___block_descriptor_tmp.13
+ ___block_descriptor_tmp.140
+ ___block_descriptor_tmp.143
+ ___block_descriptor_tmp.146
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.2
+ ___block_descriptor_tmp.4
+ ___block_descriptor_tmp.6
+ ___block_descriptor_tmp.78
+ ___block_descriptor_tmp.83
+ ___block_descriptor_tmp.92
+ ___block_literal_global.142
+ ___block_literal_global.145
+ ___ulock_wait
+ ___ulock_wake
+ ___xzm_print_block_invoke_5
+ ___xzm_ptr_in_use_enumerator_block_invoke_4
+ ___xzm_statistics_block_invoke_4
+ __free
+ __malloc_default_reader.cold.1
+ __malloc_type_zone_malloc_with_options_np_outlined
+ __malloc_ulock_self_owner_value
+ __malloc_zone_malloc_with_options_np_outlined
+ __platform_strcpy
+ __posix_memalign
+ __xzm_allocation_slots_do_lock_action
+ __xzm_allocation_slots_do_lock_action.cold.1
+ __xzm_allocation_slots_do_lock_action.cold.2
+ __xzm_chunk_list_pop
+ __xzm_chunk_list_push
+ __xzm_foreach_lock.cold.2
+ __xzm_fork_lock_wait
+ __xzm_free_large_huge
+ __xzm_free_outlined
+ __xzm_ptr_size_outlined
+ __xzm_segment_group_cache_invalidate
+ __xzm_segment_group_cache_mark_free
+ __xzm_segment_group_cache_mark_used
+ __xzm_segment_group_init_segment
+ __xzm_segment_group_init_segment.cold.1
+ __xzm_segment_group_init_segment.cold.2
+ __xzm_segment_group_init_segment.cold.3
+ __xzm_segment_group_segment_slice_split
+ __xzm_segment_group_segment_span_free_coalesce
+ __xzm_segment_group_segment_span_free_coalesce.cold.1
+ __xzm_segment_group_span_mark_free
+ __xzm_segment_group_span_mark_used
+ __xzm_segment_group_split_huge_segment
+ __xzm_segment_table_allocated_at
+ __xzm_segment_table_allocated_at.cold.1
+ __xzm_walk_lock_wait
+ __xzm_xzone_free_block_to_small_chunk
+ __xzm_xzone_malloc_from_tiny_chunk
+ __xzm_xzone_malloc_from_tiny_chunk.cold.1
+ __xzm_xzone_malloc_small
+ __xzm_xzone_malloc_tiny
+ __xzm_xzone_malloc_tiny_outlined
+ __xzm_xzone_tiny_chunk_block_is_free_slow
+ _arc4random_buf
+ _default_zone
+ _get_global_helper_zone
+ _get_wrapped_zone
+ _get_wrapped_zone.cold.1
+ _get_zone_type
+ _get_zone_type.cold.1
+ _insert_msl_lite_zone
+ _mach_vm_reclaim_is_reclaimed
+ _malloc_engaged_secure_allocator
+ _malloc_get_all_zones.cold.1
+ _malloc_get_wrapped_zone
+ _malloc_get_wrapped_zone.cold.1
+ _malloc_set_zone_name.cold.1
+ _malloc_type_zone_malloc_with_options_np
+ _malloc_variant_is_debug_4test
+ _malloc_xzone_nano_override
+ _malloc_zone_malloc_with_options_np
+ _mfmi_read_zone
+ _mfmi_read_zone.cold.1
+ _mvm_allocate_pages_plat
+ _mvm_allocate_plat
+ _mvm_deallocate_pages_plat
+ _mvm_deallocate_plat
+ _mvm_madvise
+ _mvm_madvise_free_plat
+ _mvm_madvise_plat
+ _mvm_protect_plat
+ _nanov2_ptr_in_use_enumerator.cold.1
+ _nanov2_statistics.cold.1
+ _pgm_extract_report_from_corpse.cold.2
+ _pgm_extract_report_from_corpse.cold.3
+ _pgm_extract_report_from_corpse.cold.4
+ _pgm_malloc_with_options
+ _pgm_malloc_with_options.cold.1
+ _purgeable_print_self.cold.1
+ _purgeable_ptr_in_use_enumerator.cold.1
+ _read_zone.cold.1
+ _strcat
+ _strlen
+ _szone_ptr_in_use_enumerator.cold.1
+ _szone_statistics_task.cold.1
+ _xzm_chunk_mark_free
+ _xzm_chunk_mark_free.cold.1
+ _xzm_chunk_mark_used
+ _xzm_chunk_mark_used.cold.1
+ _xzm_main_malloc_zone_init_range_groups.cold.11
+ _xzm_malloc_zone_free_definite_size_slow
+ _xzm_malloc_zone_free_slow
+ _xzm_malloc_zone_free_slow.cold.1
+ _xzm_malloc_zone_malloc_slow
+ _xzm_malloc_zone_malloc_with_options
+ _xzm_malloc_zone_malloc_with_options_slow
+ _xzm_malloc_zone_memalign_slow
+ _xzm_malloc_zone_realloc_slow
+ _xzm_malloc_zone_realloc_slow.cold.1
+ _xzm_malloc_zone_realloc_slow.cold.2
+ _xzm_malloc_zone_try_free_default_slow
+ _xzm_malloc_zone_valloc_slow
+ _xzm_memalign
+ _xzm_metapool_alloc
+ _xzm_metapool_alloc.cold.1
+ _xzm_metapool_free
+ _xzm_metapool_init
+ _xzm_ptr_in_use_enumerator.cold.1
+ _xzm_reclaim_init
+ _xzm_reclaim_is_available
+ _xzm_reclaim_mark_free
+ _xzm_reclaim_mark_used
+ _xzm_segment_group_alloc_chunk.cold.2
+ _xzm_segment_group_try_realloc_huge_chunk
+ _xzm_segment_group_try_realloc_huge_chunk.cold.1
+ _xzm_segment_group_try_realloc_large_chunk
+ _xzm_segment_table_foreach
+ _xzm_statistics.cold.1
- _OUTLINED_FUNCTION_2
- ___block_descriptor_tmp.105
- ___block_descriptor_tmp.107
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.128
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.34
- ___block_descriptor_tmp.36
- ___block_descriptor_tmp.89
- ___block_descriptor_tmp.90
- ___block_literal_global.126
- __calloc_get_size
- __xzm_free.cold.1
- __xzm_free.cold.2
- __xzm_free.cold.3
- __xzm_memalign.cold.1
- __xzm_segment_group_alloc_segment_and_chunk
- __xzm_xzone_malloc.cold.1
- __xzm_xzone_malloc.cold.10
- __xzm_xzone_malloc.cold.11
- __xzm_xzone_malloc.cold.12
- __xzm_xzone_malloc.cold.13
- __xzm_xzone_malloc.cold.14
- __xzm_xzone_malloc.cold.2
- __xzm_xzone_malloc.cold.3
- __xzm_xzone_malloc.cold.4
- __xzm_xzone_malloc.cold.5
- __xzm_xzone_malloc.cold.6
- __xzm_xzone_malloc.cold.7
- __xzm_xzone_malloc.cold.8
- __xzm_xzone_malloc.cold.9
- _create_and_insert_msl_lite_zone
- _diagnose_fault_from_external_process
- _diagnose_fault_from_external_process.cold.1
- _diagnose_fault_from_external_process.cold.2
- _diagnose_fault_from_external_process.cold.3
- _pgm_batch_free
- _pgm_batch_malloc
- _pgm_batch_malloc.cold.1
- _pgm_batch_malloc.cold.2
- _pgm_create_zone.cold.6
- _pgm_diagnose_fault_from_crash_reporter
- _pgm_diagnose_fault_from_crash_reporter.cold.1
- _szone_basic_zone
- _szone_helper_zone
- _xzm_malloc_zone_size.cold.1
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
+ "AegirPoster"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist"
+ "BUG IN CLIENT OF LIBMALLOC: memory corruption of free block"
+ "BUG IN CLIENT OF LIBMALLOC: pointer being reallocated with wrong zone"
+ "BUG IN LIBMALLOC: Failed to allocate malloc metadata"
+ "BUG IN LIBMALLOC: Slice count too large in init_segment"
+ "BUG IN LIBMALLOC: attempting to allocate from chunk of bad kind"
+ "BUG IN LIBMALLOC: attempting to coalesce slice of unexpected type"
+ "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/../xzone/xzone_inline_internal.h:182)"
+ "BUG IN LIBMALLOC: malloc assertion \"(start_address >= left_void.min_address && end_address + XZM_RANGE_SEPARATION <= left_void.max_address) || (start_address >= right_void.min_address + XZM_RANGE_SEPARATION && start_address + XZM_POINTER_RANGE_SIZE <= right_void.max_address)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:568)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1196)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1195)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1276)"
+ "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main(zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3368)"
+ "BUG IN LIBMALLOC: malloc assertion \"boothash_prefix_value <= UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3769)"
+ "BUG IN LIBMALLOC: malloc assertion \"candidate_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:543)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:517)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:480)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:479)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:543)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3118)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:997)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:537)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:482)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:481)"
+ "BUG IN LIBMALLOC: malloc assertion \"size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3072)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:2522)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:710)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3557)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:541)"
+ "BUG IN LIBMALLOC: pointer range initial overwrite failed"
+ "BUG IN LIBMALLOC: pointer range mach_vm_map() overwrite failed"
+ "BUG IN LIBMALLOC: ulock_wait failure"
+ "BUG IN LIBMALLOC: ulock_wake failure"
+ "CollectionsPoster"
+ "Failed to allocate memory at address 0x%lx of size 0x%lx with flags %d\n"
+ "Failed to allocate segment (size=%lu, flags=%x, kr=%d)\n"
+ "Failed to allocate segment - out of space\n"
+ "Failed to deallocate at address %p of size 0x%lx\n"
+ "HardenedRuntime"
+ "MallocDeferredReclaim"
+ "MallocDeferredReclaim must be one of 0,1 - got %ld\n"
+ "MallocSecureAllocatorNano"
+ "MallocSecureAllocatorNano must be 0 or 1.\n"
+ "MallocXzoneHugeCacheSize"
+ "MallocXzoneInitialSlotConfig"
+ "MallocXzonePtrBucketCount"
+ "MallocXzoneSlotUpgradeThresholdCluster"
+ "MallocXzoneSlotUpgradeThresholdSingle"
+ "MobileSafari"
+ "PGM"
+ "Sanitizer"
+ "SecureAllocator_Nano"
+ "SecureAllocator_process_Browser"
+ "SecureAllocator_process_CollectionsPoster"
+ "SecureAllocator_process_aegirposter"
+ "SecureAllocator_process_bash"
+ "SecureAllocator_process_cameracaptured"
+ "SecureAllocator_process_dash"
+ "SecureAllocator_process_find"
+ "SecureAllocator_process_perl"
+ "SecureAllocator_process_python3"
+ "SecureAllocator_process_sh"
+ "SecureAllocator_process_sshd"
+ "SecureAllocator_process_sshd_keygen_wrapper"
+ "SecureAllocator_process_su"
+ "SecureAllocator_process_telnetd"
+ "SecureAllocator_process_time"
+ "SecureAllocator_process_xargs"
+ "SecureAllocator_process_zsh"
+ "Unsupported anywhere allocation at address 0x%lx of size 0x%lx with flags %d\n"
+ "Unsupported unpopulated allocation at address 0x%lx of size 0x%lx with flags %d\n"
+ "Wrapped"
+ "bash"
+ "cameracaptured"
+ "dash"
+ "data"
+ "find"
+ "huge_segment"
+ "i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}8I16"
+ "i24@?0Q8Q16"
+ "i24@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}]}16"
+ "i28@?0Q8Q16C24"
+ "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b3b1b1b1}C)CCII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{os_unfair_lock_s=I}}{?=(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)})S^{xzm_segment_group_s}QQIICCCCb1}44^{?=QQ}52Q60"
+ "malloc_with_options (%p/%llu,%llu): "
+ "metapool metadata slab"
+ "normal_segment"
+ "perl"
+ "pointer_large"
+ "pointer_xzones"
+ "python3"
+ "segment metadata slab"
+ "sh"
+ "sshd"
+ "sshd-keygen-wrapper"
+ "su"
+ "telnetd"
+ "time"
+ "unknown"
+ "unknown slab"
+ "xargs"
+ "xzm: failed to initialize deferred reclamation buffer\n"
+ "xzm: unsupported value for MallocXzoneHugeCacheSize (%ld)"
+ "zsh"
- "        \"free\": \"0x%x\"\n"
- "        \"id\": %d\n"
- "        \"is_zero\": %d,\n"
- "BUG IN LIBMALLOC: Failed to unprotect reserved space for ptr segment"
- "BUG IN LIBMALLOC: attempting to allocation from chunk of bad kind"
- "BUG IN LIBMALLOC: attempting to bump a fully used tiny chunk"
- "BUG IN LIBMALLOC: malloc assertion \"(start_address >= left_void.min_address && end_address + XZM_RANGE_SEPARATION <= left_void.max_address) || (start_address >= right_void.min_address + XZM_RANGE_SEPARATION && start_address + XZM_POINTER_RANGE_SIZE <= right_void.max_address)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:418)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:896)"
- "BUG IN LIBMALLOC: malloc assertion \"_xzm_malloc_zone_is_main(zone)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:2122)"
- "BUG IN LIBMALLOC: malloc assertion \"boothash_prefix_value <= UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:2656)"
- "BUG IN LIBMALLOC: malloc assertion \"candidate_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:393)"
- "BUG IN LIBMALLOC: malloc assertion \"left_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:367)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:327)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:326)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1321)"
- "BUG IN LIBMALLOC: malloc assertion \"right_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:387)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:329)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:328)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1319)"
- "BUG IN LIBMALLOC: support for given alignment not yet implemented"
- "Can't deallocate_pages region at %p\n"
- "Failed to allocate ptr segment - out of space\n"
- "Failed to allocate segment (size=%zu, flags=%x, kr=%d)\n"
- "Failed to deallocate segment %p: %d\n"
- "SecureAllocator_process_WebKit_GPU"
- "SecureAllocator_process_WebKit_Networking"
- "SecureAllocator_process_WebKit_WebContent"
- "i20@?0^{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}8I16"
- "i24@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIIC[256{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}]}16"
- "i36@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIIC[256{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}]}16Q24I32"
- "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIIC[256{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}]}16^{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}24I32Q36"
- "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIIC[256{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}]}16^{xzm_slice_s=II{os_unfair_lock_s=I}CCC{?=^{xzm_slice_s}^^{xzm_slice_s}}(xzm_chunk_bits_u={?=b3b1b1b1}C)II}24I32Q36^{xzm_xzone_s={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{os_unfair_lock_s=I}}S^{xzm_segment_group_s}QICCCCb1}44^{?=QQ}52Q60"

```
