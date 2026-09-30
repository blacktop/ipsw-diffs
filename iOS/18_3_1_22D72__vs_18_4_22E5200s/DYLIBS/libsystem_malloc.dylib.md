## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-657.80.3.0.0
-  __TEXT.__text: 0x31f64
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__const: 0x4fc
-  __TEXT.__cstring: 0x76ac
+715.100.17.0.0
+  __TEXT.__text: 0x34b38
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__const: 0x50c
+  __TEXT.__cstring: 0x86ae
   __TEXT.__dof_magmalloc: 0x912
-  __TEXT.__unwind_info: 0x800
+  __TEXT.__unwind_info: 0x870
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x6b0
-  __AUTH_CONST.__auth_got: 0x350
+  __DATA_CONST.__const: 0x6f0
+  __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__const: 0x520
   __AUTH.__data: 0x128
   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0xb9
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x418d
+  __DATA.__bss: 0x215d
   __DATA.__common: 0x58
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__common: 0x1f0
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0x88
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  Functions: 790
-  Symbols:   1021
-  CStrings:  705
+  Functions: 825
+  Symbols:   1106
+  CStrings:  777
 
Symbols:
+ _mach_error_string
+ _mach_vm_reclaim_is_reusable
+ _mach_vm_reclaim_query_state
+ _mach_vm_reclaim_ring_allocate
+ _mach_vm_reclaim_ring_capacity
+ _mach_vm_reclaim_ring_flush
+ _mach_vm_reclaim_ring_resize
+ _mach_vm_reclaim_round_capacity
+ _mach_vm_reclaim_try_cancel
+ _mach_vm_reclaim_try_enter
+ _malloc_allows_internal_security_4test
+ _pthread_key_init_np
+ _pthread_self
- _mach_vm_reclaim_is_available
- _mach_vm_reclaim_is_reclaimed
- _mach_vm_reclaim_mark_free
- _mach_vm_reclaim_mark_free_with_id
- _mach_vm_reclaim_mark_used
- _mach_vm_reclaim_ringbuffer_init
- _mach_vm_reclaim_synchronize
CStrings:
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
+ "            \"id\": %u, \n"
+ "        \"batch_count\": %u, \n"
+ "        \"early_budget\": %u, \n"
+ "        \"segment_group_id\": %d, \n"
+ "        \"slice_metadata\": \"%p\", \n"
+ "        \"thread\": \"%p\",\n"
+ "        \"xz_caches\": {\n"
+ "    \"max_len\": %llu, \n"
+ "    } \n"
+ "\"batch_size\": %u, \n"
+ "\"defer_small\": %s, \n"
+ "\"defer_tiny\": %s, \n"
+ "\"ptr_bucket_count\": %d, \n"
+ "\"range_group_count\": %u, \n"
+ "\"segment_group_count\": %u, \n"
+ "\"segment_group_ids_count\": %u, \n"
+ "\"thread_cache_activation_contentions\": %lu, \n"
+ "\"thread_cache_activation_period\": %lu, \n"
+ "\"thread_cache_activation_time\": %llu, \n"
+ "\"thread_cache_enabled\": %s, \n"
+ "\"thread_caches\": [ \n"
+ "AllowInternalSecurityPolicy"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - cookie"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - free count"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - inconsistent walk"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - linkage"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny local freelist"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny remote freelist"
+ "BUG IN LIBMALLOC: Attempt to check for deferred reclamation on non-chunk slice"
+ "BUG IN LIBMALLOC: Failed to overwrite malloc metadata"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5645)"
+ "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/../xzone/xzone_inline_internal.h:190)"
+ "BUG IN LIBMALLOC: malloc assertion \"(start_address >= left_void.min_address && end_address + XZM_RANGE_SEPARATION <= left_void.max_address) || (start_address >= right_void.min_address + XZM_RANGE_SEPARATION && start_address + XZM_POINTER_RANGE_SIZE <= right_void.max_address)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:891)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2004)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2003)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2105)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:136)"
+ "BUG IN LIBMALLOC: malloc assertion \"candidate_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:866)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:215)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:253)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:388)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:390)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:148)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:281)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:290)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:399)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:803)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:802)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:781)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5020)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1443)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5694)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:860)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:805)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:804)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1080)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3974)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5780)"
+ "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6374)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:779)"
+ "BUG IN LIBMALLOC: pthread_key_init_np failed"
+ "DISABLED"
+ "ENABLED"
+ "Failed to allocate segment from range group - out of space\n"
+ "Internal Security Policy: %d\n"
+ "LetsGoClient"
+ "MallocAllowInternalSecurity"
+ "MallocDeferredReclaimBufferCount"
+ "MallocDeferredReclaimBufferMaxCount"
+ "MallocXzoneBatchSize"
+ "MallocXzoneDeferLarge must be one of 0,1 - got %ld\n"
+ "MallocXzoneDeferSmall"
+ "MallocXzoneDeferSmall must be one of 0,1 - got %ld\n"
+ "MallocXzoneDeferTiny"
+ "MallocXzoneDeferTiny must be one of 0,1 - got %ld\n"
+ "MallocXzonePerClusterSegmentGroups"
+ "MallocXzonePerClusterSegmentGroups must be 0 or 1.\n"
+ "MallocXzoneSmallThrashLimitSize"
+ "MallocXzoneSmallThrashThreshold"
+ "MallocXzoneThreadCacheActivationContentions"
+ "MallocXzoneThreadCacheActivationPeriod"
+ "MallocXzoneThreadCacheActivationTime"
+ "MallocXzoneThreadCaching"
+ "MallocXzoneThreadCaching must be one of 0,1 - got %ld\n"
+ "SecureAllocator_ThreadCaching"
+ "Unable to set up reclaim buffer, disabling large cache [%d] %s\n"
+ "XZM Config:\n\tData Only: %d\n\tGuards Enabled: %d\n\tScribble: %d\n\tTiny/Small Batch Max: %d\n\tDefer Tiny: %d\n\tDefer Small: %d\n\tDefer Large: %d\n\tHuge Cache Size: %d\n\tReclaim Buffer Count: %u/%u (%s)\n\tRanges (ptr addr/size/data addr/size): 0x%llx/%lu/0x%llx/%lu\n\tInitial Slot Config: %s\n\tMax Slot Config: %s\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tTiny Thrash Threshold: %llu ms\n\tSmall Thrash Threshold: %llu ms, %llu bytes\n\tThread Caching: %s (%u allocs, %u contentions, %llu ms)\n\tPointer Bucket Count: %lu\n"
+ "], \n"
+ "disabled"
+ "enabled"
+ "i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
+ "i24@?0Q8^{xzm_thread_cache_s={?=^{xzm_thread_cache_s}^^{xzm_thread_cache_s}}^{xzm_main_malloc_zone_s}^{_opaque_pthread_t}Q[0(xzm_xzone_thread_cache_u={?=^{xzm_slice_s}*(?={?=SSSS}(xzm_xzone_thread_cache_atomic_meta_u={?=SS}I)Q)}{?=QQSSI})]}16"
+ "i32@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
+ "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
+ "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}^vQ[256(xzm_xzone_slice_metadata_u=Q^{xzm_slice_s})][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}{?=(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b13b20}{?=Q}Q)SS})(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}^{xzm_slice_s}I{os_unfair_lock_s=I}}{?=(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)(xzm_chunk_list_head_u=(?={?=b47b16b1}{?=b47b10b6b1})Q)})SCQQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"
+ "malloc_zone_malloc_with_options: reserved TSD bit set\n"
+ "malloc_zone_malloc_with_options: unsupported options 0x%llx\n"
+ "sanitizer_malloc_with_options: unsupported options 0x%llx\n"
+ "thread cache slab"
+ "vm.reclaim.enabled"
+ "xzm: failed to initialize deferred reclamation buffer [%d] %s\n"
- "            \"flags\": \"0x%x\" \n"
- "            \"index\": %u, \n"
- "        \"reclaim_id\": %llu, \n"
- "        \"reclaim_id\": -1, \n"
- "    \"buffer\": \"%p\", \n"
- "\"defer_xzones\": %s, \n"
- "%ld, counter=%d\n*** invariant broken for %p this tiny msize=%d - size is too large\n"
- "*** error at %p msize for in_use is %d\n"
- "*** error for object %p: pointer being realloc'd was not allocated\n"
- "BUG IN LIBMALLOC: mach_vm_reclaim_mark_free_with_id failed"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4039)"
- "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/../xzone/xzone_inline_internal.h:190)"
- "BUG IN LIBMALLOC: malloc assertion \"(start_address >= left_void.min_address && end_address + XZM_RANGE_SEPARATION <= left_void.max_address) || (start_address >= right_void.min_address + XZM_RANGE_SEPARATION && start_address + XZM_POINTER_RANGE_SIZE <= right_void.max_address)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:700)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1766)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1765)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1870)"
- "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < XZM_RECLAIM_ID_COUNT\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:141)"
- "BUG IN LIBMALLOC: malloc assertion \"candidate_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:675)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:612)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:611)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:559)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3472)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1114)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4085)"
- "BUG IN LIBMALLOC: malloc assertion \"right_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:669)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:614)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:613)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:2724)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:805)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4172)"
- "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4732)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:557)"
- "Failed to allocate segment - out of space\n"
- "Unable to set up reclaim buffer (%d) - disabling large cache\n"
- "XZM Config:\n\tData Only: %d\n\tGuards Enabled: %d\n\tScribble: %d\n\tDefer Large: %d\n\tDefer Xzones: %d\n\tHuge cache size: %d\n\tReclaim Max Threshold: %lli%s\n\tRanges (ptr addr/size/data addr/size): 0x%llx/%lu/0x%llx/%lu\n\tInitial Slot Config: %s\n\tMax Slot Config: %s\n\tSlot Upgrade Thresholds: %d/%d, %d/%d\n\tPointer Bucket Count: %lu\n"
- "i20@?0^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}8I16"
- "i32@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16r*24"
- "i44@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36"
- "i68@?0Q8^{xzm_segment_s=^{xzm_segment_group_s}IIIC{?=^{xzm_segment_s}^^{xzm_segment_s}}Q^v[256Q][256{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}]}16^{xzm_slice_s=(?={?=II{os_unfair_lock_s=I}C}(xzm_chunk_atomic_meta_u={?=b11b11b6b1b1b1b7b13b13}{?=Q}Q))(?={?=^{xzm_slice_s}^^{xzm_slice_s}}{?=^{xzm_slice_s}}[2^{xzm_slice_s}])(xzm_chunk_bits_u={?=b4b1b1b1b1}C)CSII}24I32Q36^{xzm_xzone_s=(?={?={?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{?=^{xzm_slice_s}}{os_unfair_lock_s=I}}{?=(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)(xzm_chunk_list_head_u={?=b47b16b1}Q)})S^{xzm_segment_group_s}QQIICSCCb1{xzm_xzone_guard_config_s=CC}}44^{?=QQ}52Q60"
- "mds_stores"
- "vm.reclaim_max_threshold"
- "xzm: failed to initialize deferred reclamation buffer (%d)\n"

```
