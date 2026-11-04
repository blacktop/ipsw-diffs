## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__auth_ptr`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.40.37.0.0
-  __TEXT.__text: 0x5fcc0c
+1777.60.14.0.1
+  __TEXT.__text: 0x600680
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0x50f61
-  __TEXT.__const: 0x124124
-  __TEXT.__swift5_typeref: 0x1452c
-  __TEXT.__swift5_reflstr: 0x13528
-  __TEXT.__swift5_assocty: 0x7d10
-  __TEXT.__swift5_fieldmd: 0x1ce0c
-  __TEXT.__constg_swiftt: 0x28b08
+  __TEXT.__cstring: 0x51791
+  __TEXT.__const: 0x124e94
+  __TEXT.__swift5_typeref: 0x14564
+  __TEXT.__swift5_reflstr: 0x135b8
+  __TEXT.__swift5_assocty: 0x7d40
+  __TEXT.__swift5_fieldmd: 0x1cf64
+  __TEXT.__constg_swiftt: 0x28bfc
   __TEXT.__swift5_protos: 0x998
-  __TEXT.__swift5_proto: 0x3e98
-  __TEXT.__swift5_types: 0x2524
-  __TEXT.__swift5_types2: 0x60
+  __TEXT.__swift5_proto: 0x3ebc
+  __TEXT.__swift5_types: 0x2534
+  __TEXT.__swift5_types2: 0x64
   __TEXT.__swift5_builtin: 0x15b8
   __TEXT.__swift5_capture: 0x1068
   __TEXT.__objc_methtype: 0x111
   __TEXT.__swift5_mpenum: 0x3b8
-  __TEXT.__swift_as_entry: 0x9b4
-  __TEXT.__swift_as_ret: 0xb2c
-  __TEXT.__swift_as_cont: 0x1224
+  __TEXT.__swift_as_entry: 0x9bc
+  __TEXT.__swift_as_ret: 0xb34
+  __TEXT.__swift_as_cont: 0x1234
   __TEXT.__oslogstring: 0xf3
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xb8
-  __TEXT.__eh_frame: 0x36060
+  __TEXT.__eh_frame: 0x35fc0
   __DATA.__TIGHTBEAM_VT: 0x8a0
   __DATA.__TIGHTBEAM: 0x238
-  __DATA.__const: 0x3e7a8
-  __DATA.__data: 0x191a0
+  __DATA.__const: 0x3ea98
+  __DATA.__data: 0x19238
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1a84b
-  __DATA.__auth_ptr: 0x2498
+  __DATA.__ENDPOINTS: 0x1b291
+  __DATA.__auth_ptr: 0x24a8
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x380
   __DATA.__MMIOREGS: 0x795

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__common: 0x72a
+  __DATA.__common: 0x71a
   __PDATA.__auth_ptr: 0x280
-  __PDATA.__const: 0x6810
+  __PDATA.__const: 0x6910
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0

   __DATA_CONST.__mod_term_func: 0x0
   Functions: 657
   Symbols:   1
-  CStrings:  7442
+  CStrings:  7488
 
Functions:
~ sub_802453c : 427588 -> 432240
~ sub_808cb80 -> sub_808ddac : 173984 -> 174524
~ sub_80b7498 -> sub_80b88e0 : 232 -> 224
~ sub_80bb3e0 -> sub_80bc820 : 141072 -> 140336
~ sub_8178afc -> sub_8179c5c : 85264 -> 82544
~ sub_818d80c -> sub_818decc : 973012 -> 983364
~ sub_827c8a0 -> sub_827f7d0 : 15180 -> 15228
~ sub_828053c -> sub_828349c : 290032 -> 291080
~ sub_82c9230 -> sub_82cc5a8 : 409764 -> 410304
~ sub_83333c8 -> sub_833695c : 6108 -> 6104
~ sub_84d8f04 -> sub_84dc494 : 17764 -> 17788
~ sub_8595d1c -> sub_85992c4 : 406796 -> 408024
~ sub_85f9228 -> sub_85fcc9c : 4008 -> 4004
CStrings:
+ " LCD conversion type not supported right now"
+ " type for nits -> DBV conversion"
+ "!ctx->used"
+ "(addr - base) % slot_size == 0"
+ "(map[idx / FREE_MAP_WORD_BITS] & bit) == 0"
+ "*** error for object %p: %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.3.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.3.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "Could not find or convert field nits-to-dbv-conversion-type in EDT"
+ "Direct nits -> DBV (log) conversion"
+ "Direct nits -> DBV (quad) conversion"
+ "Formula based conversion"
+ "Found nits-to-dbv-conversion-type field value in EDT: "
+ "I14@?0{easm_space_destroyxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
+ "I14@?0{easm_space_remapxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
+ "I24@?0Q8@?<I@?{easm_space_remapxnucontentregion__result_s=C(?={easm_failure_s=CS})}>16"
+ "I28@?0Q8I16@?<I@?{easm_space_destroyxnucontentregion__result_s=C(?={easm_failure_s=CS})}>20"
+ "Invalid backlight calibration data size or format"
+ "MFM double free"
+ "Missing required configuration for DirectNitsQuad in exbright EDT node"
+ "Nits -> DBV conversion loaded from EDT: "
+ "No EDT to read configuration from for DirectNitsQuad"
+ "No EXBright node to read configuration from for DirectNitsQuad"
+ "No backlight-exbright/backlight node to read configuration from for DirectNitsQuad"
+ "Parsed DirectNitsQuad LCD configuration: "
+ "Power assertion held: "
+ "TB_FATAL: invalid result returned from destroyXnuContentRegion (%s:%d)\n"
+ "TB_FATAL: invalid result returned from remapXnuContentRegion (%s:%d)\n"
+ "Table based conversion"
+ "Unknown nits-to-dbv-conversion-type field value: "
+ "addr - base < populated_bytes"
+ "addr >= base"
+ "carveout_permanent_kib"
+ "carveout_reclaimable_kib"
+ "carveout_total_kib"
+ "cl4_allocations_kib"
+ "destroyXnuContentRegion"
+ "free to already-freed small chunk (likely double-free)"
+ "free to empty or invalid freelist chunk (likely double-free)"
+ "free_map_acquire"
+ "free_map_release"
+ "idx < populated_slots"
+ "initialize_thread_context"
+ "invalid MFM address"
+ "ipc_buffer_free_map != NULL"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8886)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8314)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7858)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2217)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5346)"
+ "nits-to-dbv-conversion-type"
+ "not an allocated MFM block"
+ "release_thread_context"
+ "remapXnuContentRegion"
+ "slot_index"
+ "thread_context_free_map != NULL"
+ "v14@?0{easm_space_destroyxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
+ "v14@?0{easm_space_remapxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
+ "vas__easm_destroy_xnu_content_region"
+ "vas__easm_remap_xnu_content_region"
- "*** error for object %p: pointer being freed was not allocated\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "BUG IN CLIENT OF LIBMALLOC (%llu): MTE tag mismatch"
- "BUG IN CLIENT OF LIBMALLOC (%llu): double free detected"
- "BUG IN CLIENT OF LIBMALLOC (%llu): invalid address"
- "BUG IN CLIENT OF LIBMALLOC (%llu): not an allocated block"
- "free to empty or invalid chunk detected (likely double-free)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8903)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8331)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7872)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6854)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2216)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5356)"
```
