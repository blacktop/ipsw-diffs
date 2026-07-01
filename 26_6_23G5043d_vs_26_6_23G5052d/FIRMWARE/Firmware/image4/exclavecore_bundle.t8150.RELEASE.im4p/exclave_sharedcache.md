## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.im4p/exclave_sharedcache`

```diff

-  __TEXT.__text: 0xd2dc94
+  __TEXT.__text: 0xd2bf9c
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__cstring: 0x969d1
   __TEXT.__const: 0x17fe64

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x118
-  __TEXT.__eh_frame: 0x736c0
+  __TEXT.__eh_frame: 0x73600
   __DATA.__TIGHTBEAM_VT: 0x11a0
   __DATA.__TIGHTBEAM: 0x470
   __DATA.__data: 0x45488

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 50189
+  Functions: 50185
   Symbols:   1
   CStrings:  14252
 
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__chain_fixups : content changed
~ __DATA.__TIGHTBEAM_VT : content changed
~ __DATA.__TIGHTBEAM : content changed
~ __DATA.__data : content changed
~ __DATA.__const : content changed
~ __DATA.__mod_init_func : content changed
~ __DATA.__auth_ptr : content changed
~ __DATA.__shared_cache : content changed
~ __DATA.__got : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
~ __PDATA.__data : content changed
~ __PDATA.__const : content changed
~ __PDATA.__shared_cache : content changed
~ __PDATA.__auth_ptr : content changed
~ __PDATA.__bss : content changed
~ __PDATA.__common : content changed
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CR_-ugDwFCiSlHSFUDnftUpraf-pItwcmVp580Q/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.6.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CR__ugBD_2wn7uBS1vwaf1dB0EslbVP0rVhVMNU/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.6.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CSAAugCK_ZHMLRFd3QIirJFJdQlWccHlT9Rrj6g/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.6.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Wed Jun 17 02:31:01 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
+ "Build Date: Wed Jun 17 02:20:26 PDT 2026"
+ "ExclaveOS Image4 Framework Version 7.0.0: Wed Jun 17 02:31:01 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
+ "ExclaveSISP-5.602"
+ "Wed Jun 17 03:01:47 PDT 2026"
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
- "/AppleInternal/Library/BuildRoots/4~CRUcugCUjUmhDcPdRUV1Dv0uqSWbRekG02euTxw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.6.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CRUdugBDyzcxsW1w42UuIllhZioKRvykhau5fWc/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.6.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Sun Jun  7 19:36:35 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "Build Date: Sun Jun  7 19:24:47 PDT 2026"
- "ExclaveOS Image4 Framework Version 7.0.0: Sun Jun  7 19:36:35 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "ExclaveSISP-5.601"
- "Sun Jun  7 20:07:32 PDT 2026"
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
