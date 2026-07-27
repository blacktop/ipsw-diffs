## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__dof_magmalloc`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__AUTH.__v_zone`
- `__DATA.__data`

```diff

-812.160.4.0.0
-  __TEXT.__text: 0x41aa8
+812.160.5.0.0
+  __TEXT.__text: 0x41ab8
   __TEXT.__auth_stubs: 0x7a0
   __TEXT.__const: 0x5bc
   __TEXT.__cstring: 0xb90a
Functions:
~ _xzm_segment_group_try_realloc_huge_chunk : 1060 -> 1076
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:912)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6945)"
+ "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7639)"
+ "BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:677)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2587)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2586)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2701)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7236)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:871)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:135)"
+ "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:432)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_start < ptr_start || data_start >= ptr_start + ptr_reservation_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1389)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:219)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:260)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:276)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:278)"
+ "BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7144)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:152)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:301)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:338)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:347)"
+ "BUG IN LIBMALLOC: malloc assertion \"leaf_table\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:63)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:838)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:897)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:937)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6254)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2492)"
+ "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:892)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:936)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:873)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:448)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:618)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:695)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7005)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2110)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5129)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fBGNXH/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:836)"
- "BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:912)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6945)"
- "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7639)"
- "BUG IN LIBMALLOC: malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:677)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2582)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2581)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2696)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7236)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:866)"
- "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:135)"
- "BUG IN LIBMALLOC: malloc assertion \"chunk->xzc_empty_count\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:432)"
- "BUG IN LIBMALLOC: malloc assertion \"data_start < ptr_start || data_start >= ptr_start + ptr_reservation_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1384)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:214)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:255)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:271)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:273)"
- "BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7144)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:147)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:296)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:333)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:342)"
- "BUG IN LIBMALLOC: malloc assertion \"leaf_table\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:63)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:838)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:892)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:932)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6254)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2492)"
- "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:887)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:931)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:868)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:448)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:618)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:695)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7005)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2110)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5129)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.r5KWPJ/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:836)"
```
