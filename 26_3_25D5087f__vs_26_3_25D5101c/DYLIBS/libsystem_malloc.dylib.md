## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-792.80.1.0.0
+792.80.2.0.0
   __TEXT.__text: 0x3e69c
   __TEXT.__auth_stubs: 0x770
   __TEXT.__const: 0x5a3
-  __TEXT.__cstring: 0xa73a
+  __TEXT.__cstring: 0xa7a0
   __TEXT.__dof_magmalloc: 0xa96
   __TEXT.__unwind_info: 0x940
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__const: 0x848
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x6d0
   __AUTH.__data: 0x128

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: D8130B43-17DE-34FA-AE22-92F5975DF7F6
+  UUID: DB91372F-7CC7-37B6-AEB2-4E233E08CE3F
   Functions: 869
   Symbols:   1360
-  CStrings:  929
+  CStrings:  931
 
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5921)"
+ "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/../xzone/xzone_inline_internal.h:190)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2301)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2300)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2402)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6119)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:829)"
+ "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:136)"
+ "BUG IN LIBMALLOC: malloc assertion \"data_start < ptr_start || data_start >= ptr_start + ptr_reservation_size\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1337)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:215)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:253)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:390)"
+ "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:392)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:148)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:281)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:290)"
+ "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:401)"
+ "BUG IN LIBMALLOC: malloc assertion \"leaf_table\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:64)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:774)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:855)"
+ "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:895)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5272)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1577)"
+ "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:850)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:894)"
+ "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:831)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5978)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1194)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4194)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6066)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/4~CE7uugASUBSDXDoQTlpdjCVzFFBaRJa8rsC_E9A/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:772)"
+ "com.apple.WebKit.WebContent.EnhancedSecurity"
+ "com.apple.WebKit.WebContent.EnhancedSecurity.Development"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5921)"
- "BUG IN LIBMALLOC: malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/../xzone/xzone_inline_internal.h:190)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2301)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2300)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2402)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6119)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:829)"
- "BUG IN LIBMALLOC: malloc assertion \"cache->ric_head < cache->ric_len\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:136)"
- "BUG IN LIBMALLOC: malloc assertion \"data_start < ptr_start || data_start >= ptr_start + ptr_reservation_size\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:1337)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:215)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:253)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:390)"
- "BUG IN LIBMALLOC: malloc assertion \"err == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:392)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:148)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:281)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:290)"
- "BUG IN LIBMALLOC: malloc assertion \"kr == VM_RECLAIM_SUCCESS\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:401)"
- "BUG IN LIBMALLOC: malloc assertion \"leaf_table\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:64)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:774)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:855)"
- "BUG IN LIBMALLOC: malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:895)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5272)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1577)"
- "BUG IN LIBMALLOC: malloc assertion \"range_count == 2\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:850)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:894)"
- "BUG IN LIBMALLOC: malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:831)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5978)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1194)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4194)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6066)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/4~CDyFugAf9V7eEvEFc_TemW5q_FRajTbY1TCGcq0/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_introspect.c:772)"

```
