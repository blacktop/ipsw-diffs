## exclave_roottask

> `exclave_roottask`

```diff

-1195.120.4.0.1
-  __TEXT.__text: 0x4b7e54
+1195.160.5.0.0
+  __TEXT.__text: 0x4b9a14
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__const: 0xedbe0
   __TEXT.__cstring: 0x3a98c

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x78
-  __TEXT.__eh_frame: 0x1ccfc
+  __TEXT.__eh_frame: 0x1cdac
   __DATA.__data: 0xbe90
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: 02BB8E2C-2ABF-3727-AAF4-2CCCC3E109D2
-  Functions: 17668
+  UUID: 46190F96-8079-33F5-8857-7E988E3786F4
+  Functions: 17669
   Symbols:   27
   CStrings:  5884
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CPcYugBpxL6NPt4lHYTfkYTHGcwEUDOtMEMGXYg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.6.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8165)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7639)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2581)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2696)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7236)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6254)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2110)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/21BBE43E-48EE-4673-8045-642140E630D2/TemporaryDirectory.uftR4a/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5129)"
- "/AppleInternal/Library/BuildRoots/4~CNpgugDt6TcCZQtcm_yHFmMdDEvaL-W1C6QCUb0/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/3DA88B1C-9BF3-4643-83BE-EF8659159395/TemporaryDirectory.Ue0jk5/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"

```
