## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-  __TEXT.__text: 0x46fb0
+  __TEXT.__text: 0x46fd0
   __TEXT.__const: 0x6ff
   __TEXT.__cstring: 0xb9d1
   __TEXT.__dof_magmalloc: 0xa96

   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0xc0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x213d
+  __DATA.__bss: 0x212d
   __DATA.__common: 0x64
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0xa1
+  __DATA_DIRTY.__bss: 0xb8
   __DATA_DIRTY.__common: 0x22c
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libcorecrypto.dylib
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__dof_magmalloc : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__auth_got : content changed
~ __AUTH.__data : content changed
~ __AUTH.__v_zone : content changed
~ __DATA.__data : content changed
Functions:
~ _nanov2_allocate_new_region : 276 -> 280
~ _tiny_batch_malloc : 260 -> 248
~ _malloc_common_value_for_key : 152 -> 128
~ _malloc_zone_unregister : 444 -> 448
~ _xzm_reclaim_mark_free_locked : 304 -> 320
~ _xzm_segment_group_try_realloc_huge_chunk : 972 -> 984
~ _malloc_common_strstr : 112 -> 92
~ __malloc_allow_internal_security_policy : 180 -> 184
~ _large_debug_print : 692 -> 684
~ _small_check_region : 964 -> 948
~ _malloc_config_from_input : 1172 -> 1184
~ _mfm_initialize : 300 -> 292
~ _mfm_alloc : 1100 -> 1092
~ _xzm_segment_group_segment_foreach_span : 372 -> 412
~ ____xzm_introspect_enumerate_block_invoke_2 : 1852 -> 1892
~ _main_image_has_section : 252 -> 244
~ _nanov2_ptr_in_use_enumerator : 1456 -> 1472
~ _xzm_main_malloc_zone_create : 10056 -> 10048
~ __xzm_malloc_large_huge : 1776 -> 1784
~ __xzm_xzone_malloc_small : 3172 -> 3124
~ __xzm_gzone_free_slot : 948 -> 940
~ __xzm_xzone_free_to_chunk : 148 -> 204
~ _medium_check_region : 924 -> 908
~ _tiny_in_use_enumerator : 1032 -> 1040
~ _tiny_zero_corruption_abort : 1032 -> 1028
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:981)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7524)"
+ "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:195)"
+ "BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:8293)"
+ "BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:719)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2731)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2730)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2905)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7834)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:969)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:159)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:458)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_start < ptr_start || data_start >= ptr_start + ptr_reservation_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1486)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:283)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:324)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:340)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:342)"
+ "BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7726)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:176)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:365)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:403)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:412)"
+ "BUG IN LIBMALLOC: malloc assertion \"leaf_table\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:64)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:995)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:995)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1035)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6830)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2584)"
+ "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:990)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1034)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:971)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:474)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:660)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:737)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7584)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2197)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5336)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.d9DgzM/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:993)"
- "BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:981)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7516)"
- "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:195)"
- "BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:8284)"
- "BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:719)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2724)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2723)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2897)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7826)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:963)"
- "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:159)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:458)"
- "BUG IN LIBMALLOC: malloc assertion \"data_start < ptr_start || data_start >= ptr_start + ptr_reservation_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1480)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:278)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:319)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:335)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:337)"
- "BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7718)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:171)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:360)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:397)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:406)"
- "BUG IN LIBMALLOC: malloc assertion \"leaf_table\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:64)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:960)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:989)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1029)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6822)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2584)"
- "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:984)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1028)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:965)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:474)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:660)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:737)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7576)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2197)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5328)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ah09a2/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:958)"

```
