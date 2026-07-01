## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.im4p/exclave_roottask`

```diff

-  __TEXT.__text: 0x4b9a14
+  __TEXT.__text: 0x4b7f14
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__const: 0xedbe0
   __TEXT.__cstring: 0x3a98c

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x78
-  __TEXT.__eh_frame: 0x1cdac
+  __TEXT.__eh_frame: 0x1ccfc
   __DATA.__data: 0xbe90
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 17669
+  Functions: 17670
   Symbols:   27
   CStrings:  5884
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __DATA.__data : content changed
~ __DATA.__mod_init_func : content changed
~ __DATA.__auth_ptr : content changed
~ __DATA.__const : content changed
~ __DATA.__got : content changed
~ __DATA.__common : content changed
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CR_-ugDwFCiSlHSFUDnftUpraf-pItwcmVp580Q/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.6.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8165)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7639)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2581)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2696)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7236)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6254)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2110)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/6A334D4E-A319-4BC3-9422-0604B09A0E03/TemporaryDirectory.G1X4QM/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5129)"
- "/AppleInternal/Library/BuildRoots/4~CRUaugBziDNMasPqmYa6Ki2h5A2WSRXBCy3qlIM/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.6.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8165)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7639)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2581)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2696)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7236)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6254)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2110)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/4850E7F7-8A53-4E0E-99C3-6C75BFC1E619/TemporaryDirectory.U2KN7o/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5129)"

```
