## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-  __TEXT.__text: 0x3ad44
+  __TEXT.__text: 0x3ad48
   __TEXT.__auth_stubs: 0x770
   __TEXT.__const: 0x51b
   __TEXT.__cstring: 0xb484
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__dof_magmalloc : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__auth_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __AUTH.__v_zone : content changed
~ __DATA.__data : content changed
Functions:
~ _xzm_segment_group_try_realloc_huge_chunk : 1112 -> 1116
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2587)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2586)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2701)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:871)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1036)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:219)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:260)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:276)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:278)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:152)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:301)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:338)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:347)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:982)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:981)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1020)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:897)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:923)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:937)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:912)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:924)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:911)"
+ "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:892)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:936)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:873)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:878)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:877)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:984)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:983)"
+ "BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1042)"
+ "BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1039)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2582)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2581)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:2696)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:866)"
- "BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1031)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:214)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:255)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:271)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:273)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:147)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:296)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:333)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:342)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:977)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:976)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1015)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:892)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:918)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:932)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:907)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:919)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:906)"
- "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:887)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:931)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:868)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:873)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:872)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:979)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:978)"
- "BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1037)"
- "BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_segment.c:1034)"

```
