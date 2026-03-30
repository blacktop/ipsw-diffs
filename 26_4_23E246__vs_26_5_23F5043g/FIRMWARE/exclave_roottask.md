## exclave_roottask

> `exclave_roottask`

```diff

-1195.100.161.0.1
-  __TEXT.__text: 0x4a9ad8
+1195.120.3.0.0
+  __TEXT.__text: 0x4a9a2c
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__const: 0xedb30
-  __TEXT.__cstring: 0x3a9bc
+  __TEXT.__cstring: 0x3a92c
   __TEXT.__swift5_typeref: 0xc0f2
   __TEXT.__swift5_capture: 0x15d8
   __TEXT.__swift5_entry: 0x8

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x78
-  __TEXT.__eh_frame: 0x1cecc
+  __TEXT.__eh_frame: 0x1ce84
   __DATA.__data: 0xbd78
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: 31C300AA-FF7A-330E-B552-41B9204A9B26
-  Functions: 17674
+  UUID: 5700B02E-9EA7-3D27-B69A-16DCA3F54042
+  Functions: 17675
   Symbols:   27
-  CStrings:  5883
+  CStrings:  5882
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CLZhugARwQC1FMpP4XPqjmLslVJFFFvqxogVxIk/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/B40150B8-99EE-4AA7-82ED-2E3E6F3E2844/TemporaryDirectory.912AWt/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"
- "/AppleInternal/Library/BuildRoots/4~CKc6ugBFCtwaINnCO_AFUeP5AO1JGqyfId5QTp4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "WARNING: destroying a span that still has spanmap contents (type %u). The PMM won't be informed of these slots' deletion but we still delete the slots.\n"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4126B4E3-15C8-423C-B64B-D42014DDE99F/TemporaryDirectory.Mib9dC/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"

```
