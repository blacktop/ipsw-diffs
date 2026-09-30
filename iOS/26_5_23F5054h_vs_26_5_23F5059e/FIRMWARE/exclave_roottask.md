## exclave_roottask

> `exclave_roottask`

```diff

-1195.120.4.0.0
-  __TEXT.__text: 0x4b7e60
+1195.120.4.0.1
+  __TEXT.__text: 0x4b7e54
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__const: 0xedbe0
   __TEXT.__cstring: 0x3a98c

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: 6053D412-9AED-3E3C-9EAB-A9F10BE71843
+  UUID: 3FD2DC31-1F4E-3E73-BA91-B12FC17A7FFB
   Functions: 17668
   Symbols:   27
   CStrings:  5884
Functions:
~ sub_c01bf7cc : 2664 -> 2676
~ sub_c01c0234 -> sub_c01c0240 : 3208 -> 3220
~ sub_c026e1bc -> sub_c026e1d4 : 1848 -> 1844
~ sub_c02bbe88 -> sub_c02bbe9c : 1796 -> 1772
~ sub_c03580d8 -> sub_c03580d4 : 1408 -> 1420
~ sub_c03589ac -> sub_c03589b4 : 1764 -> 1744
~ sub_c04b8ff0 -> sub_c04b8fe4 : 48 -> 52
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CNHaugBXuBL-XHDtOPWz_INyFaEMU0dGeFIU5fg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"
- "/AppleInternal/Library/BuildRoots/4~CMtnugDDnlNuIUYRbHDGSh3tSOTQoP81zskBdbI/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/DB0E3174-BFA2-40D9-BAB6-80438D31D57A/TemporaryDirectory.CtMuXK/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"

```
