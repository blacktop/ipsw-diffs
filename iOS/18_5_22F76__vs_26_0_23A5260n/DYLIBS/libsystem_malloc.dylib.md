## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-715.120.13.0.0
-  __TEXT.__text: 0x34c50
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__const: 0x50c
-  __TEXT.__cstring: 0x8970
+778.0.0.0.0
+  __TEXT.__text: 0x36904
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__const: 0x4ea
+  __TEXT.__cstring: 0x96ae
   __TEXT.__dof_magmalloc: 0x912
   __TEXT.__unwind_info: 0x878
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x6f0
-  __AUTH_CONST.__auth_got: 0x378
+  __DATA_CONST.__const: 0x768
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x520
   __AUTH.__data: 0x128
   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0xb9
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x215d
-  __DATA.__common: 0x58
-  __DATA_DIRTY.__data: 0x20
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x216d
+  __DATA.__common: 0x60
+  __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__common: 0x1f0
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0x78
   - /usr/lib/system/libcompiler_rt.dylib
+  - /usr/lib/system/libcorecrypto.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_blocks.dylib
   - /usr/lib/system/libsystem_c.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: B6554432-3BBE-3AC9-870D-779DCA3F0CB4
-  Functions: 825
-  Symbols:   2152
-  CStrings:  786
+  UUID: DBC396D5-1594-3CF3-848E-3A6EC5C8831D
+  Functions: 838
+  Symbols:   2183
+  CStrings:  843
 
Symbols:
+ ____xzm_introspect_freelist_chunk_blocks_block_invoke
+ ___block_descriptor_tmp.170
+ ___block_descriptor_tmp.177
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.204
+ ___block_descriptor_tmp.235
+ ___block_descriptor_tmp.238
+ ___block_descriptor_tmp.241
+ ___block_descriptor_tmp.242
+ ___block_descriptor_tmp.37
+ ___block_descriptor_tmp.50
+ ___block_literal_global.237
+ ___block_literal_global.240
+ ___mfm_block_mark_free
+ __xzm_chunk_list_slot_push
+ __xzm_initialize_xzone_data.cold.1
+ __xzm_reclaim_mark_free
+ __xzm_reclaim_mark_used
+ __xzm_xzone_find_and_malloc_from_freelist_chunk
+ __xzm_xzone_find_and_malloc_from_freelist_chunk.cold.1
+ __xzm_xzone_free_freelist
+ __xzm_xzone_freelist_chunk_block_is_free_slow
+ __xzm_xzone_freelist_chunks_mark_empty
+ __xzm_xzone_madvise_freelist_chunk
+ __xzm_xzone_malloc_freelist_outlined
+ __xzm_xzone_malloc_from_empty_freelist_chunk
+ __xzm_xzone_malloc_from_empty_freelist_chunk.cold.1
+ __xzm_xzone_malloc_from_freelist_chunk
+ __xzm_xzone_malloc_from_freelist_chunk.cold.1
+ __xzm_xzone_malloc_small_freelist
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha256_di
+ _get_tiny_meta_header_offset
+ _malloc_memorystatus_mask_resource_exception_handling
+ _xzm_main_malloc_zone_init_range_groups.cold.11
+ _xzm_main_malloc_zone_init_range_groups.cold.12
+ _xzm_main_malloc_zone_init_range_groups.cold.13
+ _xzm_main_malloc_zone_init_range_groups.cold.14
+ _xzm_main_malloc_zone_init_range_groups.cold.15
+ _xzm_main_malloc_zone_init_range_groups.cold.16
+ _xzm_main_malloc_zone_init_range_groups.cold.17
+ _xzm_main_malloc_zone_init_range_groups.cold.18
+ _xzm_main_malloc_zone_init_range_groups.cold.19
+ _xzm_main_malloc_zone_init_range_groups.cold.20
+ _xzm_main_malloc_zone_init_range_groups.cold.21
+ _xzm_main_malloc_zone_init_range_groups.cold.22
+ _xzm_main_malloc_zone_init_range_groups.cold.23
+ _xzm_main_malloc_zone_init_range_groups.cold.24
+ _xzm_malloc_zone_destroy.cold.5
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- ____xzm_introspect_tiny_chunk_blocks_block_invoke
- ___block_descriptor_tmp.152
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.184
- ___block_descriptor_tmp.186
- ___block_descriptor_tmp.215
- ___block_descriptor_tmp.218
- ___block_descriptor_tmp.221
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.34
- ___block_descriptor_tmp.47
- ___block_literal_global.217
- ___block_literal_global.220
- __malloc_check_secure_allocator_process_enablement
- __xzm_xzone_find_and_malloc_from_tiny_chunk
- __xzm_xzone_find_and_malloc_from_tiny_chunk.cold.1
- __xzm_xzone_free_tiny
- __xzm_xzone_madvise_tiny_chunk
- __xzm_xzone_malloc_from_empty_tiny_chunk
- __xzm_xzone_malloc_from_empty_tiny_chunk.cold.1
- __xzm_xzone_malloc_from_tiny_chunk
- __xzm_xzone_malloc_from_tiny_chunk.cold.1
- __xzm_xzone_malloc_tiny_outlined
- __xzm_xzone_tiny_chunk_block_is_free_slow
- __xzm_xzone_tiny_chunks_mark_empty
- _env_bool
- _get_tiny_meta_header
- _xzm_main_malloc_zone_create.cold.9
- _xzm_reclaim_mark_free
- _xzm_reclaim_mark_used
CStrings:
+ "                \"operations\": %lu,\n"
+ "        \"chunk_count\": %llu, \n"
+ "        \"direction\": \"%s\"\n"
+ "        \"front\": %d, \n"
+ "        \"list_config\": \"%s\",\n"
+ "        \"range_group\": \"%p\", \n"
+ "        \"remaining\": %zu, \n"
+ "        \"skip_addr\": \"%p\", \n"
+ "        \"skip_size\": %zu, \n"
+ "    \"busy\": %llu, \n"
+ "    \"head\": %llu, \n"
+ "    \"last_sample_abs\": %llu, \n"
+ "    \"reclaimable_bytes\": %llu, \n"
+ "    \"reclaimable_bytes_min\": %llu, \n"
+ "    \"sampling_period_abs\": %llu, \n"
+ "    \"tail\": %llu \n"
+ "\"allocation_front_count\": %u, \n"
+ "\"chunk_threshold\": %u, \n"
+ "\"deallocate_segment\": %s, \n"
+ "\"initial_slot_config\": %d, \n"
+ "\"max_list_config\": %d, \n"
+ "\"segment_group_front_count\": %u, \n"
+ "\"slot_initial_threshold\": %u, \n"
+ "\"use_early_alloc\": %s, \n"
+ "AudioConverterService"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5902)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2291)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2290)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2392)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6100)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:819)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:984)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:392)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:401)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:930)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:929)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:968)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:784)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:845)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:871)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:885)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:860)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:872)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:859)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5253)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1616)"
+ "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:840)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:884)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:821)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:826)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:825)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5959)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:932)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:931)"
+ "BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:990)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1233)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4191)"
+ "BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:987)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6047)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:782)"
+ "BUG IN LIBMALLOC: unsupported allocation front count"
+ "MallocEnableMSLAtLimitWarning"
+ "MallocSmallFreelist"
+ "MallocXzoneAllocationFronts"
+ "MallocXzoneHasRanges"
+ "MallocXzoneHugeCacheMaxEntryBytes"
+ "MallocXzoneInitialChunkThreshold"
+ "MallocXzoneInitialSlotThreshold"
+ "MallocXzoneListConfig"
+ "MallocXzoneListUpgradePeriod"
+ "MallocXzoneListUpgradeThreshold"
+ "MallocXzoneListUpgradeThresholdCluster"
+ "MallocXzoneListUpgradeThresholdSingle"
+ "MallocXzoneMaxListConfig"
+ "MallocXzoneSegmentDeallocate"
+ "ReportCrash"
+ "Unsupported MallocXzoneAllocationFronts\n"
+ "XZM Config:\n\tData Only: %d\n\tAllocation Fronts: %d\n\tGuards Enabled: %d\n\tScribble: %d\n\tTiny/Small Batch Max: %d\n\tDefer Tiny: %d\n\tDefer Small: %d\n\tDefer Large: %d\n\tHuge Cache Size: %d\n\tHuge Cache Max Entry Bytes: %u\n\tReclaim Buffer Count: %u/%u (%s)\n\tSmall Freelist: %u\n\tData Range: 0x%llx/%lu\n\tPointer Range 1: 0x%llx/%lu\n\tPointer Range 2: 0x%llx/%lu\n\tEarly Allocator: %s\n\tSegment Deallocate: %u\n\tInitial Slot Config: %s/%s (Chunk, Size Thresholds: %u, %u)\n\tInitial List Config: %s/%s\n\tList Upgrade Thresholds: %d/%d, %d/%d\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tTiny Thrash Threshold: %llu ms\n\tSmall Thrash Threshold: %llu ms, %llu bytes\n\tThread Caching: %s (%u allocs, %u contentions, %llu ms)\n\tPointer Bucket Count: %lu\n"
+ "com.apple.WebKit.GPU.Development"
+ "com.apple.WebKit.Networking.Development"
+ "com.apple.WebKit.WebContent.CaptivePortal.Development"
+ "com.apple.WebKit.WebContent.Development"
+ "down"
+ "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{os_unfair_lock_s=I}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCCQQIIQCSCCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"
+ "pointer"
+ "small_freelist_chunk"
+ "up"
+ "xzm: unsupported value for MallocXzoneHugeCacheMaxEntryBytes (%ld)"
+ "xzone malloc front random"
- "        \"busy\": %llu, \n"
- "        \"head\": %llu, \n"
- "        \"remaining\": %zu\n"
- "        \"tail\": %llu \n"
- "    \"indices\": { \n"
- "    \"last_accounting_given_to_kernel\": %llu, \n"
- "    \"va_in_buffer\": %llu, \n"
- "    }, \n"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5651)"
- "BUG IN LIBMALLOC: malloc assertion \"(start_address >= left_void.min_address && end_address + XZM_RANGE_SEPARATION <= left_void.max_address) || (start_address >= right_void.min_address + XZM_RANGE_SEPARATION && start_address + XZM_POINTER_RANGE_SIZE <= right_void.max_address)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:923)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2036)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2035)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2137)"
- "BUG IN LIBMALLOC: malloc assertion \"candidate_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:898)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:388)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:399)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:835)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:834)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:781)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5026)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1443)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5700)"
- "BUG IN LIBMALLOC: malloc assertion \"right_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:892)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:837)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:836)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1080)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3976)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5786)"
- "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6380)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:779)"
- "XZM Config:\n\tData Only: %d\n\tGuards Enabled: %d\n\tScribble: %d\n\tTiny/Small Batch Max: %d\n\tDefer Tiny: %d\n\tDefer Small: %d\n\tDefer Large: %d\n\tHuge Cache Size: %d\n\tReclaim Buffer Count: %u/%u (%s)\n\tRanges (ptr addr/size/data addr/size): 0x%llx/%lu/0x%llx/%lu\n\tEarly Allocator: %s\n\tInitial Slot Config: %s\n\tMax Slot Config: %s\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tTiny Thrash Threshold: %llu ms\n\tSmall Thrash Threshold: %llu ms, %llu bytes\n\tThread Caching: %s (%u allocs, %u contentions, %llu ms)\n\tPointer Bucket Count: %lu\n"
- "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{os_unfair_lock_s=I}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCQQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"

```
