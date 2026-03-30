## exclave_sharedcache

> `exclave_sharedcache`

```diff

-1148.102.2.0.0
-  __TEXT.__text: 0x5c2638
+1148.120.3.0.1
+  __TEXT.__text: 0x5c2798
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__cstring: 0x488d1
-  __TEXT.__const: 0x112d64
+  __TEXT.__cstring: 0x48841
+  __TEXT.__const: 0x112e94
   __TEXT.__swift5_typeref: 0x11e54
   __TEXT.__swift5_reflstr: 0xf428
   __TEXT.__swift5_assocty: 0x7460
   __TEXT.__swift5_fieldmd: 0x17df0
   __TEXT.__constg_swiftt: 0x22edc
   __TEXT.__swift5_protos: 0x83c
-  __TEXT.__swift5_proto: 0x3618
+  __TEXT.__swift5_proto: 0x361c
   __TEXT.__swift5_types: 0x1e84
   __TEXT.__swift5_types2: 0x44
   __TEXT.__swift5_builtin: 0x1360

   __DATA.__const: 0x374f0
   __DATA.__mod_init_func: 0x40
   __DATA.__ENDPOINTS: 0x13957
-  __DATA.__auth_ptr: 0x1f88
+  __DATA.__auth_ptr: 0x1f90
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x268
   __DATA.__MMIOREGS: 0x795

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: FA272EF1-5954-3A3B-981A-0BBD968B9E3E
-  Functions: 23482
+  UUID: 4E653837-74AD-3093-80AB-90D1730B90D2
+  Functions: 23485
   Symbols:   1
-  CStrings:  6782
+  CStrings:  6781
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CLZhugARwQC1FMpP4XPqjmLslVJFFFvqxogVxIk/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CLZkugDIgXosMXCLDAB4SlfkvjPrDlbO-msn0fY/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CLZnugCyjNwvvI7F5R7vPnDC78n1m9FWSIvS7SI/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
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
- "/AppleInternal/Library/BuildRoots/4~CKdBugDpDb1f62stbsiRpO2tTtx56OZ6w_7SkBY/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CKdDugBXDMZz_Zxp1t6BVFjiTb28D9115blvm7U/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.4.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
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
