## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-792.80.2.0.0
-  __TEXT.__text: 0x3785c
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__const: 0x4fa
-  __TEXT.__cstring: 0x9a2f
+812.100.27.0.0
+  __TEXT.__text: 0x3accc
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__const: 0x518
+  __TEXT.__cstring: 0xb484
   __TEXT.__dof_magmalloc: 0x912
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__unwind_info: 0x8c0
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x828
-  __AUTH_CONST.__auth_got: 0x398
+  __DATA_CONST.__const: 0xb90
+  __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x520
   __AUTH.__data: 0x128
   __AUTH.__v_zone: 0x4000
-  __DATA.__data: 0xb9
+  __DATA.__data: 0xb8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x216d
+  __DATA.__bss: 0x2155
   __DATA.__common: 0x68
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__common: 0x218
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x70
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libcorecrypto.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: A643AD3A-F242-3041-BE40-A951A67176D4
-  Functions: 832
-  Symbols:   2188
-  CStrings:  866
+  UUID: D28A88AD-D78B-390A-979A-66A9EA539A94
+  Functions: 864
+  Symbols:   2289
+  CStrings:  968
 
Symbols:
+ ___block_descriptor_tmp.201
+ ___block_descriptor_tmp.240
+ ___block_descriptor_tmp.276
+ ___block_descriptor_tmp.279
+ ___block_descriptor_tmp.282
+ ___block_descriptor_tmp.283
+ ___block_descriptor_tmp.38
+ ___block_descriptor_tmp.51
+ ___block_literal_global.278
+ ___block_literal_global.281
+ __malloc_config_check_development_only_env_bool
+ __malloc_progname_needs_mac_26_0_bincompat
+ __xzm_bin_sizes_step2
+ __xzm_browser_process_config
+ __xzm_gzone_alloc_chunk
+ __xzm_gzone_free_all_slots
+ __xzm_gzone_free_all_slots.cold.1
+ __xzm_gzone_free_chunk
+ __xzm_gzone_free_chunk.cold.1
+ __xzm_gzone_free_chunk.cold.2
+ __xzm_gzone_free_slot
+ __xzm_gzone_free_slot.cold.1
+ __xzm_gzone_free_slot.cold.2
+ __xzm_gzone_free_slot.cold.3
+ __xzm_gzone_free_slot.cold.4
+ __xzm_gzone_init_chunk
+ __xzm_gzone_init_chunk.cold.1
+ __xzm_gzone_init_chunk.cold.2
+ __xzm_gzone_init_chunk.cold.3
+ __xzm_gzone_malloc_from_chunk
+ __xzm_gzone_malloc_from_chunk.cold.1
+ __xzm_gzone_malloc_from_chunk.cold.2
+ __xzm_gzone_malloc_from_chunk.cold.3
+ __xzm_gzone_malloc_from_chunk.cold.4
+ __xzm_gzone_realloc
+ __xzm_gzone_reinit_quarantine
+ __xzm_gzone_reinit_quarantine_finish
+ __xzm_initialize_guard_config
+ __xzm_initialize_xzone_data.cold.2
+ __xzm_malloc_large_huge.cold.4
+ __xzm_reclaim_force_sync
+ __xzm_reclaim_force_sync.cold.1
+ __xzm_reclaim_force_sync.cold.2
+ __xzm_segment_group_cache_invalidate
+ __xzm_segment_group_segment_create_guard_page
+ _dyld_get_active_platform
+ _dyld_get_program_sdk_version_token
+ _dyld_version_token_at_least
+ _mach_vm_purgable_control
+ _malloc_config_from_input
+ _memtag_assign_tag_contiguous
+ _mvm_guard
+ _mvm_guard_plat
+ _no_guard_objects_processes
+ _set_tiny_meta_header_in_use
+ _xzm_guard_slot_mark_free
+ _xzm_guard_slot_mark_used
+ _xzm_guard_slot_set_purgeable
+ _xzm_guard_slot_set_purgeable.cold.1
+ _xzm_malloc_zone_destroy.cold.6
+ _xzm_malloc_zone_free_definite_size_slow.cold.3
+ _xzm_malloc_zone_free_definite_size_slow.cold.4
+ _xzm_malloc_zone_free_slow.cold.4
+ _xzm_malloc_zone_free_slow.cold.5
+ _xzm_malloc_zone_malloc_type_realloc_slow.cold.10
+ _xzm_malloc_zone_malloc_type_realloc_slow.cold.11
+ _xzm_malloc_zone_malloc_type_realloc_slow.cold.6
+ _xzm_malloc_zone_malloc_type_realloc_slow.cold.7
+ _xzm_malloc_zone_malloc_type_realloc_slow.cold.8
+ _xzm_malloc_zone_malloc_type_realloc_slow.cold.9
+ _xzm_malloc_zone_size.cold.2
+ _xzm_malloc_zone_try_free_default_slow.cold.3
+ _xzm_malloc_zone_try_free_default_slow.cold.4
+ _xzm_ptr_lookup_4test.cold.3
+ _xzm_realloc.cold.3
+ _xzm_reclaim_mark_free_locked.cold.3
+ _xzm_segment_group_update_guard_chunk
- _ZAP_GO_DOWN
- ___block_descriptor_tmp.174
- ___block_descriptor_tmp.181
- ___block_descriptor_tmp.206
- ___block_descriptor_tmp.239
- ___block_descriptor_tmp.245
- ___block_descriptor_tmp.246
- ___block_descriptor_tmp.37
- ___block_descriptor_tmp.50
- ___block_literal_global.241
- ___block_literal_global.244
- __xzm_bin_sizes
- __xzm_segment_group_segment_create_guard
- __xzm_segment_group_segment_create_guard.cold.1
- __xzm_xzone_block_memtag_retag
- _malloc_nano_on_xzone
- _malloc_nano_on_xzone_override
- _malloc_xzone_enabled
- _malloc_xzone_nano_override
- _memtag_assign_tag
- _purgeable_zone_use_xzm
- _secure_allocator_boot_arg
- _xzm_create_mzones
- _xzm_reclaim_force_sync.cold.1
- _xzm_reclaim_force_sync.cold.2
- _xzm_reclaim_sync_and_resize
- _xzm_reclaim_sync_and_resize.cold.1
- _xzm_segment_group_alloc_chunk.cold.4
CStrings:
+ "            \"density\": %u,\n"
+ "            \"length\": %u,\n"
+ "            \"reuse\": %u\n"
+ "            \"type\": %u,\n"
+ "            { \"count\": %u }"
+ "        \"block_size\": %u,\n"
+ "        \"empty\": %u,\n"
+ "        \"guard_config\": {\n"
+ "        \"guards\": %u,\n"
+ "        \"last_dealloc_ts\": \"%llu\", \n"
+ "        \"on_multi_segment\": %d,\n"
+ "        \"quarantine\": %u,\n"
+ "        \"runq_full\": [\n"
+ "        \"runq_partial\": [\n"
+ "        \"runq_quarantine\": [\n"
+ "        \"slot_slices\": %u,\n"
+ "        \"slot_state\": \"0x%llx\",\n"
+ "        \"tagged\": %d,\n"
+ "        ],\n"
+ "        }\n"
+ "    \"%p\": {\n"
+ "    \"%u\": {\n"
+ "    \"guard_pages_enabled\": %d, \n"
+ "    \"large_chunk_slots\": %d,\n"
+ "    \"large_guard_density\": %d,\n"
+ "    \"large_guard_force_quarantine\": %d,\n"
+ "    \"large_guard_reinit\": %d,\n"
+ "    \"large_guard_reuse\": %d\n"
+ "    \"large_guards_enabled\": %d,\n"
+ "    \"large_max_chunks\": %d,\n"
+ "\"guard_object_config\": {\n"
+ "\"guard_page_config\": {\n"
+ "\"guard_zones\": {\n"
+ "\"multi_segment_size\": %zu, \n"
+ "%s}"
+ "*** can't mprotect(0x0) region for new postlude guard page at %p\n"
+ "*** can't mvm_protect(%u) region at %p with size %lu\n"
+ ",\n"
+ "BUG IN LIBMALLOC: Unexpected guard bitmap state!"
+ "BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:912)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6931)"
+ "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7608)"
+ "BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:677)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2575)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2574)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2688)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7220)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:866)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:135)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:432)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1031)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:214)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:255)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:271)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:273)"
+ "BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7130)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:147)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:296)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:333)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:342)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:977)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:976)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1015)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:838)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:892)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:918)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:932)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:907)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:919)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:906)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6240)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2488)"
+ "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:887)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:931)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:868)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:873)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:872)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:448)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:618)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:695)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6991)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:979)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:978)"
+ "BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1037)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2106)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5125)"
+ "BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1034)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/3A8014AC-2FF5-4201-8206-569ED34889DB/TemporaryDirectory.6eDhjW/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:836)"
+ "ClockFace"
+ "Digital Performer"
+ "ExternalQuickLookSatellite-arm64"
+ "ExternalQuickLookSatellite-x86_64"
+ "FaceTime"
+ "Family"
+ "GroupSessionService"
+ "HashtagImages"
+ "IINA"
+ "Intel"
+ "MTE"
+ "Malloc Config Outputs:\n\tProcess Identity: %u\n\tEnable Xzone Malloc: %d\n\tEnable Nano On Xzone: %d\n\tXzone Enablement Reason: %s\n"
+ "MallocSecureAllocator in environment"
+ "MallocXzoneDataThrashThreshold"
+ "MallocXzoneGuardLarge"
+ "MallocXzoneGuardLargeChunkMax"
+ "MallocXzoneGuardLargeDensity"
+ "MallocXzoneGuardLargeQuarantine"
+ "MallocXzoneGuardLargeReinit"
+ "MallocXzoneGuardLargeReuse"
+ "MallocXzoneGuardLargeSlots"
+ "Messages"
+ "MobileNotes"
+ "QuickLookSatellite"
+ "QuickLookUIService"
+ "Reducing guards for block size %lu from %u:%u:%u to %u:%u:%u!\n"
+ "Reminders"
+ "Safari"
+ "SafariViewService"
+ "Screen Sharing"
+ "SecureAllocator_GuardObjects"
+ "StickersUltra"
+ "ThumbnailExtension_macOS"
+ "Unsupported protect debug flags %u\n"
+ "VTDecoderXPCService"
+ "VTEncoderXPCService"
+ "Web"
+ "Web App"
+ "WebSheet"
+ "WhatIf"
+ "XZM Config:\n\tData Only: %d\n\tAllocation Fronts: %d\n\tGuard Pages: %d (Tiny: %d, %d/%d; Small: %d, %d/%d)\n\tGuard Objects: (Large: %d [%d+%d/%d; max %d, quarantine %u, reinit %d])\n\tScribble: %d\n\tTiny/Small Batch Max: %d\n\tDefer Tiny: %d\n\tDefer Small: %d\n\tDefer Large: %d\n\tHuge Cache Size: %d\n\tHuge Cache Max Entry Bytes: %u\n\tReclaim Buffer Count: %u/%u (%s)\n\tSmall Freelist: %u\n\tData Range: 0x%llx/%lu\n\tPointer Range 1: 0x%llx/%lu\n\tPointer Range 2: 0x%llx/%lu\n\tEarly Allocator: %s\n\tSegment Deallocate: %u\n\tMTE (enabled/data/max size): %d/%d/%llu\n\tInitial Slot Config: %s/%s (Chunk, Size Thresholds: %u, %u)\n\tInitial List Config: %s/%s\n\tList Upgrade Thresholds: %d/%d, %d/%d\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tTiny Thrash Threshold: %llu ms\n\tSmall Thrash Threshold: %llu ms, %llu bytes\n\tData Thrash Threshold: %llu ms\n\tThread Caching: %s (%u allocs, %u contentions, %llu ms)\n\tPointer Bucket Count: %lu\n"
+ "arkitd"
+ "arm64 tvOS"
+ "backboardd"
+ "bridgeOS"
+ "com.apple.Safari.CredentialExtractionHelper"
+ "com.apple.Safari.History"
+ "com.apple.Safari.SandboxBroker"
+ "com.apple.Safari.SearchHelper"
+ "com.apple.SafariFoundation.CredentialProviderExtensionHelper"
+ "com.apple.SafariPlatformSupport.Helper"
+ "com.apple.SafariServices"
+ "com.apple.SafariServices.ExtensionHelper"
+ "com.apple.quicklook.ThumbnailsAgent"
+ "default"
+ "disabled known process"
+ "guard_chunk"
+ "i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}8I16"
+ "i32@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16r*24"
+ "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[0{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB}{?=Q{os_unfair_lock_s=I}CCCC})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)(?=CC)SII(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})}24I32Q36(xzm_gxzone_u=^{xzm_gzone_s}^{xzm_xzone_s})44^{?=QQ}52Q60"
+ "iOS bincompat list"
+ "keychainsharingmessagingd"
+ "launchd_sim"
+ "launchd_sim.debug"
+ "launchd_sim.development"
+ "macOS bincompat list"
+ "multi-segment metadata slab"
+ "multi_segment"
+ "not LP64"
+ "polarisd"
+ "presenced"
+ "prl_client_app"
+ "process feature flag"
+ "quicklookd"
+ "realitycamerad"
+ "tvOS feature flag"
+ "visionOS bincompat list"
+ "wakeboardd"
+ "xbs chroot"
+ "zero-on-free bincompat"
+ "},\n"
- "    \"guards_enabled\": %d, \n"
- "\"guard_config\": {\n"
- "%s}\n"
- "*** can't mvm_protect(%u) region for postlude guard page at %p\n"
- "*** can't mvm_protect(%u) region for prelude guard page at %p\n"
- "*** can't mvm_protect(0x0) region for new postlude guard page at %p\n"
- "BUG IN LIBMALLOC: Failed to mprotect guard page"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5921)"
- "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/../xzone/xzone_inline_internal.h:190)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2301)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2300)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2402)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6119)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:829)"
- "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:136)"
- "BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:994)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:215)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:253)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:390)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:392)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:148)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:281)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:290)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:401)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:940)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:939)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:978)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:774)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:855)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:881)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:895)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:870)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:882)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:869)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5272)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1577)"
- "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:850)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:894)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:831)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:836)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:835)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5978)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:942)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:941)"
- "BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1000)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1194)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4194)"
- "BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:997)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6066)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:772)"
- "MallocNanoOnXzone must be 0 or 1.\n"
- "MallocSecureAllocator must be 0 or 1.\n"
- "MallocSecureAllocatorCreateMzones"
- "MallocSecureAllocatorCreateMzones must be 0 or 1.\n"
- "MallocSecureAllocatorNano"
- "MallocSecureAllocatorNano must be 0 or 1.\n"
- "MallocSecureAllocatorPurgeableZone"
- "MallocSecureAllocatorPurgeableZone must be 0 or 1.\n"
- "SecureAllocator_Nano"
- "SecureAllocator_NanoOnXzone"
- "SecureAllocator_SystemWide"
- "SecureAllocator_ThreadCaching"
- "XZM Config:\n\tData Only: %d\n\tAllocation Fronts: %d\n\tGuards Enabled: %d\n\tScribble: %d\n\tTiny/Small Batch Max: %d\n\tDefer Tiny: %d\n\tDefer Small: %d\n\tDefer Large: %d\n\tHuge Cache Size: %d\n\tHuge Cache Max Entry Bytes: %u\n\tReclaim Buffer Count: %u/%u (%s)\n\tSmall Freelist: %u\n\tData Range: 0x%llx/%lu\n\tPointer Range 1: 0x%llx/%lu\n\tPointer Range 2: 0x%llx/%lu\n\tEarly Allocator: %s\n\tSegment Deallocate: %u\n\tMTE (enabled/data/max size): %d/%d/%llu\n\tInitial Slot Config: %s/%s (Chunk, Size Thresholds: %u, %u)\n\tInitial List Config: %s/%s\n\tList Upgrade Thresholds: %d/%d, %d/%d\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tTiny Thrash Threshold: %llu ms\n\tSmall Thrash Threshold: %llu ms, %llu bytes\n\tThread Caching: %s (%u allocs, %u contentions, %llu ms)\n\tPointer Bucket Count: %lu\n"
- "has_sec_transition"
- "i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
- "i32@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
- "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
- "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SSB})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{os_unfair_lock_s=I}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCCQQIIQCSCCCb1b1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"
- "malloc_secure_allocator must be 0 or 1 - ignored.\n"

```
