## exclave_sharedcache

> `exclave_sharedcache`

```diff

-1148.120.4.0.0
-  __TEXT.__text: 0x5d5ae0
+1148.120.6.0.0
+  __TEXT.__text: 0x5d5ad4
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__cstring: 0x48ed1
   __TEXT.__const: 0x112ee4

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: BA9CE2A4-7D63-36E4-ABEB-936E77ADC8B2
+  UUID: 3F9C3F8A-2356-358F-8C23-5687567C386A
   Functions: 23500
   Symbols:   1
   CStrings:  6796
Functions:
~ sub_8332e88 : 2664 -> 2676
~ sub_83338f0 -> sub_83338fc : 3208 -> 3220
~ sub_83e42c0 -> sub_83e42d8 : 1848 -> 1844
~ sub_84340d4 -> sub_84340e8 : 1796 -> 1772
~ sub_84d8c2c -> sub_84d8c28 : 1420 -> 1432
~ sub_84d9518 -> sub_84d9520 : 1872 -> 1852
~ sub_85d2fdc -> sub_85d2fd0 : 132 -> 136
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CNHaugBXuBL-XHDtOPWz_INyFaEMU0dGeFIU5fg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CNHbugD4BOXjOBh4Bq-Aszw8X8T8DxIOpx3Hoa4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CNXsugAMiQPZde1wk6gAs4Rcg14Ua9Gf37y3Neg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
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
- "/AppleInternal/Library/BuildRoots/4~CMtougDMNCBwCT_LA-APS-1RJT7Kd-RGC5tSxK0/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CMtsugD0R90n5EEyss868OfsDFtzrldbU-s_1x4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
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
