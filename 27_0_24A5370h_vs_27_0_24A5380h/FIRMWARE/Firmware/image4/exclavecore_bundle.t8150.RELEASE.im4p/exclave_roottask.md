## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.im4p/exclave_roottask`

```diff

-  __TEXT.__text: 0x4e755c
+  __TEXT.__text: 0x4e9a88
   __TEXT.__lcxx_override: 0xe4
-  __TEXT.__const: 0xf2150
-  __TEXT.__cstring: 0x3cafc
-  __TEXT.__swift5_typeref: 0xcecc
+  __TEXT.__const: 0xf2260
+  __TEXT.__cstring: 0x3cbcc
+  __TEXT.__swift5_typeref: 0xcf0c
   __TEXT.__swift5_capture: 0x155c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_reflstr: 0xb26c
   __TEXT.__swift5_assocty: 0x7158
-  __TEXT.__constg_swiftt: 0x162e8
-  __TEXT.__swift5_fieldmd: 0x12528
+  __TEXT.__swift5_fieldmd: 0x1256c
+  __TEXT.__constg_swiftt: 0x16368
   __TEXT.__swift5_builtin: 0xed8
   __TEXT.__swift5_mpenum: 0x534
   __TEXT.__swift5_protos: 0x494
-  __TEXT.__swift5_proto: 0x2dfc
+  __TEXT.__swift5_proto: 0x2e0c
   __TEXT.__swift5_types: 0x1588
-  __TEXT.__swift5_types2: 0x50
+  __TEXT.__swift5_types2: 0x58
   __TEXT.__objc_methtype: 0x226
-  __TEXT.__swift_as_entry: 0x224
-  __TEXT.__swift_as_ret: 0x2a8
-  __TEXT.__swift_as_cont: 0x4a0
+  __TEXT.__swift_as_entry: 0x22c
+  __TEXT.__swift_as_ret: 0x2b0
+  __TEXT.__swift_as_cont: 0x4a8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x80
-  __TEXT.__eh_frame: 0x21a0c
-  __DATA.__data: 0xce70
+  __TEXT.__eh_frame: 0x21dc4
+  __DATA.__data: 0xce60
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58
   __DATA.__auth_ptr: 0x1130
-  __DATA.__const: 0x35578
+  __DATA.__const: 0x35668
   __DATA.__ENDPOINTS: 0xa46
   __DATA.__DEVICETREE: 0x30
-  __DATA.__got: 0x198
+  __DATA.__got: 0x190
   __DATA.__thread_vars: 0x60
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x20
   __DATA.__common: 0x21ff1
-  __DATA.__bss: 0x1bc28
+  __DATA.__bss: 0x1b7e8
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 19197
-  Symbols:   28
-  CStrings:  6035
+  Functions: 19227
+  Symbols:   29
+  CStrings:  6042
 
Sections:
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_reflstr : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__chain_fixups : content changed
~ __DATA.__shared_cache : content changed
~ __DATA.__mod_init_func : content changed
~ __DATA.__auth_ptr : content changed
~ __DATA.__thread_vars : content changed
~ __DATA.__common : content changed
Symbols:
+ _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "Deferred send unsupported"
+ "Invalid configuration"
+ "Message encode failed"
+ "No notification pending"
+ "Notification check-in failed"
+ "Notification receive failed"
+ "Validation failed"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2730)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2905)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:969)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:995)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1035)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:990)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1034)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:971)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
+ "no fixup data for faultable range [%#lx, %#lx) found"
+ "populateAddressSpaceMetadata(asid:bundleComponent:nodes:entryArgs:machoFiles:brokeredCommonResources:brokeredResources:tightbeamResources:)"
+ "rawServiceConnection: message is not backed by a service connection"
+ "write_float_string"
- "Needs one segment with name "
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8856)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8284)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2723)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2897)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7826)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:963)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:989)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1029)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6822)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:984)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:1028)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:965)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5328)"
- "populateAddressSpaceMetadata(asid:bundleComponent:nodes:entryArgs:machoFiles:brokeredCommonResources:brokeredResources:tightbeamResources:ignoredRegionsAddresses:)"
- "serviceConnection: message is not backed by a service connection"
- "write_float"

```
