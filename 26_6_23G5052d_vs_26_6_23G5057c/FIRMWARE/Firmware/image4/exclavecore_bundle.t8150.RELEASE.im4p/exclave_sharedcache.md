## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.im4p/exclave_sharedcache`

```diff

-  __TEXT.__text: 0xd2bf9c
+  __TEXT.__text: 0xd2c0d4
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__cstring: 0x969d1
-  __TEXT.__const: 0x17fe64
-  __TEXT.__swift5_typeref: 0x2788a
+  __TEXT.__const: 0x17fed4
+  __TEXT.__swift5_typeref: 0x2789a
   __TEXT.__swift5_reflstr: 0x388d8
-  __TEXT.__swift5_assocty: 0xd2c8
-  __TEXT.__swift5_fieldmd: 0x567c4
-  __TEXT.__constg_swiftt: 0x5a15c
+  __TEXT.__swift5_assocty: 0xd2e0
+  __TEXT.__swift5_fieldmd: 0x56850
+  __TEXT.__constg_swiftt: 0x5a194
   __TEXT.__swift5_protos: 0x10dc
-  __TEXT.__swift5_proto: 0x9014
-  __TEXT.__swift5_types: 0x5864
+  __TEXT.__swift5_proto: 0x9020
+  __TEXT.__swift5_types: 0x586c
   __TEXT.__swift5_types2: 0x80
   __TEXT.__swift5_builtin: 0x2544
   __TEXT.__objc_methtype: 0x21f

   __DATA.__TIGHTBEAM_VT: 0x11a0
   __DATA.__TIGHTBEAM: 0x470
   __DATA.__data: 0x45488
-  __DATA.__const: 0xdaa38
+  __DATA.__const: 0xdab80
   __DATA.__mod_init_func: 0x40
   __DATA.__ENDPOINTS: 0x148c0
-  __DATA.__auth_ptr: 0x6e40
+  __DATA.__auth_ptr: 0x6e50
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x2a0
   __DATA.__DARTS: 0x93f

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 50185
+  Functions: 50191
   Symbols:   1
   CStrings:  14252
 
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_types2 : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__chain_fixups : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA.__TIGHTBEAM_VT : content changed
~ __DATA.__data : content changed
~ __DATA.__mod_init_func : content changed
~ __DATA.__shared_cache : content changed
~ __DATA.__got : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
~ __PDATA.__data : content changed
~ __PDATA.__const : content changed
~ __PDATA.__auth_ptr : content changed
~ __PDATA.__bss : content changed
~ __PDATA.__common : content changed
CStrings:
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Fri Jun 26 16:50:51 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
+ "Build Date: Fri Jun 26 16:39:28 PDT 2026"
+ "ExclaveOS Image4 Framework Version 7.0.0: Fri Jun 26 16:50:51 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
+ "Fri Jun 26 17:22:39 PDT 2026"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2586)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2701)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:871)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:897)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:937)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:936)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:873)"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Wed Jun 17 02:31:01 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "Build Date: Wed Jun 17 02:20:26 PDT 2026"
- "ExclaveOS Image4 Framework Version 7.0.0: Wed Jun 17 02:31:01 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "Wed Jun 17 03:01:47 PDT 2026"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2581)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2696)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"

```
