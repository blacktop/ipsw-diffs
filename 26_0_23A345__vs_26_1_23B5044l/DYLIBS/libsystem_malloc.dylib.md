## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-792.0.2.0.0
-  __TEXT.__text: 0x389e8
+792.40.5.0.0
+  __TEXT.__text: 0x38a04
   __TEXT.__auth_stubs: 0x740
   __TEXT.__const: 0x4fa
-  __TEXT.__cstring: 0x9b97
+  __TEXT.__cstring: 0x9b98
   __TEXT.__dof_magmalloc: 0x912
   __TEXT.__unwind_info: 0x8a8
   __TEXT.__eh_frame: 0x48

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 01256047-5B24-333B-933B-332907DE9410
+  UUID: 6BE0B559-1FC6-36FC-88EE-B9804AD492B3
   Functions: 842
   Symbols:   2218
   CStrings:  874
Functions:
~ __malloc_zone_malloc_with_options_outlined : 624 -> 652
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5916)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2301)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2300)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2402)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6114)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:829)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:994)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:940)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:939)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:978)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:855)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:881)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:895)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:870)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:882)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:869)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5267)"
+ "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:850)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:894)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:831)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:836)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:835)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5973)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:942)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:941)"
+ "BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1000)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4189)"
+ "BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:997)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6061)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5913)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2291)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2290)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2392)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6111)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:819)"
- "BUG IN LIBMALLOC: malloc assertion \"data_span < total_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:984)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:930)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:929)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void_limit <= right_void_min\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:968)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:845)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:871)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:885)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:860)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[0].min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:872)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle > ranges[1].min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:859)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5264)"
- "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:840)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:884)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:821)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address < ranges[1].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:826)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[1].min_address > ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:825)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5970)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:932)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:931)"
- "BUG IN LIBMALLOC: malloc assertion \"starting_space % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:990)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4186)"
- "BUG IN LIBMALLOC: malloc assertion \"usable_space >= ptr_rg_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:987)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6058)"

```
