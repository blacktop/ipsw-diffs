## exclave_roottask

> `exclave_roottask`

```diff

-1195.100.161.0.0
-  __TEXT.__text: 0x4a9d60
+1195.100.161.0.1
+  __TEXT.__text: 0x4a9da0
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__const: 0xedb80
-  __TEXT.__cstring: 0x3a9ac
+  __TEXT.__cstring: 0x3a99c
   __TEXT.__swift5_typeref: 0xc0f2
   __TEXT.__swift5_capture: 0x15d8
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: DBD4728F-6C75-3F4A-9585-38B1CF3C98C2
+  UUID: F1B6B64F-D648-3393-BA6F-DBC77FA431FE
   Functions: 17671
   Symbols:   27
   CStrings:  5882
Functions:
~ sub_c003266c : 336 -> 296
~ sub_c0103410 -> sub_c01033e8 : 1140 -> 1132
~ sub_c010c290 -> sub_c010c260 : 240 -> 224
~ sub_c03bbc14 -> sub_c03bbbd4 : 92 -> 228
~ sub_c03f6bc4 -> sub_c03f6c0c : 408 -> 404
~ sub_c0452d10 -> sub_c0452d54 : 1676 -> 1672
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJplugA13ObP0Crk2MWJvR7Glas3_ok7zfrFmiI/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "CheckedObjCAsyncCompletionHandlerImpl"
+ "checked "
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/97B6F686-D222-4C33-B2DE-55DA3CC4D23E/TemporaryDirectory.74Lz2o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"
- "/AppleInternal/Library/BuildRoots/4~CJITugBKbtsyqNu4p417I2hbwWwE31jYzSsu8kg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "PredefinedObjCAsyncCompletionHandlerImpl"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/297A8DFE-0D10-4BEF-BB2E-239C6A5C772A/TemporaryDirectory.0oGXZv/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"
- "predefined "

```
