## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-812.100.31.0.0
-  __TEXT.__text: 0x3ace4
+812.160.3.0.0
+  __TEXT.__text: 0x3ad1c
   __TEXT.__auth_stubs: 0x770
   __TEXT.__const: 0x51b
   __TEXT.__cstring: 0xb484

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 722EE5FA-44F7-3568-9313-74D5D67AE51C
+  UUID: F8486E44-434B-302A-B443-1F4E4BC57DFF
   Functions: 864
   Symbols:   2289
   CStrings:  968
Functions:
~ _xzm_realloc : 1324 -> 1352
~ __xzm_malloc_large_huge : 1728 -> 1736
~ __xzm_initialize_xzone_data : 1156 -> 1088
~ ___xzm_print_block_invoke_5 : 1356 -> 1416
~ _xzm_malloc_zone_malloc_type_realloc_slow : 4224 -> 4252
CStrings:
+ "        \"user_slices\": %u,\n"
+ "BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:912)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6945)"
+ "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7639)"
+ "BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:677)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2582)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2581)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2696)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7236)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:866)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:135)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:432)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1031)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:214)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:255)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:271)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:273)"
+ "BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7144)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:147)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:296)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:333)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:342)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:977)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:976)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1015)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:838)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:892)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:918)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:932)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:907)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:919)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:906)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6254)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2492)"
+ "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:887)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:931)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:868)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:873)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:872)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:448)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:618)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:695)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7005)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:979)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:978)"
+ "BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1037)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2110)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5129)"
+ "BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1034)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/4F6E5E15-947F-45B4-B720-CFB3D27C4013/TemporaryDirectory.ccyq4G/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:836)"
- "        \"slot_slices\": %u,\n"
- "BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:912)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6934)"
- "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7613)"
- "BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:677)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2575)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2574)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2688)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7225)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:866)"
- "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:135)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:432)"
- "BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1031)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:214)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:255)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:271)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:273)"
- "BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7133)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:147)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:296)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:333)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:342)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:977)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:976)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1015)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:838)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:892)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:918)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:932)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:907)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:919)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:906)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6243)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2488)"
- "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:887)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:931)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:868)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:873)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:872)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:448)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:618)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:695)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6994)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:979)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:978)"
- "BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1037)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2106)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5125)"
- "BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1034)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/01F6C1F0-6121-4A01-AE7F-BBAF05FAA027/TemporaryDirectory.vCOnk7/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:836)"

```
