## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8152.RELEASE.im4p/exclave_roottask`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__chain_fixups`
- `__DATA.__shared_cache`
- `__DATA.__mod_init_func`
- `__DATA.__got`
- `__DATA.__thread_vars`

```diff

-1490.0.21.0.0
-  __TEXT.__text: 0x4ecf10
+1490.40.21.0.0
+  __TEXT.__text: 0x4ef8a8
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__const: 0xf23d0
-  __TEXT.__cstring: 0x3df02
-  __TEXT.__swift5_typeref: 0xcfbc
+  __TEXT.__const: 0xf28a0
+  __TEXT.__cstring: 0x3e252
+  __TEXT.__swift5_typeref: 0xd07c
   __TEXT.__swift5_capture: 0x155c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0xb2ac
-  __TEXT.__swift5_assocty: 0x7208
-  __TEXT.__swift5_fieldmd: 0x12604
-  __TEXT.__constg_swiftt: 0x16410
+  __TEXT.__swift5_reflstr: 0xb37c
+  __TEXT.__swift5_assocty: 0x7448
+  __TEXT.__swift5_fieldmd: 0x126d8
+  __TEXT.__constg_swiftt: 0x16528
   __TEXT.__swift5_builtin: 0xed8
   __TEXT.__swift5_mpenum: 0x534
-  __TEXT.__swift5_protos: 0x494
-  __TEXT.__swift5_proto: 0x2e3c
-  __TEXT.__swift5_types: 0x1590
+  __TEXT.__swift5_protos: 0x49c
+  __TEXT.__swift5_proto: 0x2ecc
+  __TEXT.__swift5_types: 0x15a8
   __TEXT.__swift5_types2: 0x58
-  __TEXT.__objc_methtype: 0x226
+  __TEXT.__objc_methtype: 0x246
   __TEXT.__swift_as_entry: 0x230
   __TEXT.__swift_as_ret: 0x2b0
   __TEXT.__swift_as_cont: 0x4a8

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x80
-  __TEXT.__eh_frame: 0x21e5c
-  __DATA.__data: 0xcf50
+  __TEXT.__eh_frame: 0x221d4
+  __DATA.__data: 0xcf68
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58
-  __DATA.__auth_ptr: 0x1138
-  __DATA.__const: 0x35438
+  __DATA.__auth_ptr: 0x1178
+  __DATA.__const: 0x358b8
   __DATA.__ENDPOINTS: 0xa46
   __DATA.__DEVICETREE: 0x30
   __DATA.__got: 0x190

   __PDATA.__shared_cache: 0x0
   Functions: 836
   Symbols:   29
-  CStrings:  6084
+  CStrings:  6096
 
Functions:
~ sub_c006854c -> sub_c0068440 : 233796 -> 234928
~ sub_c00a3510 -> sub_c00a3870 : 57020 -> 56960
~ sub_c00b143c -> sub_c00b1760 : 13480 -> 13484
~ sub_c00b4a0c -> sub_c00b4d34 : 152 -> 324
~ sub_c00b4e78 -> sub_c00b524c : 37456 -> 37508
~ sub_c00d5e40 -> sub_c00d6248 : 112704 -> 113444
~ sub_c010054c -> sub_c0100c38 : 80768 -> 80776
~ sub_c012c670 -> sub_c012cd64 : 59292 -> 59904
~ sub_c013ae0c -> sub_c013b764 : 97220 -> 97228
~ sub_c0152b48 -> sub_c01534a8 : 184 -> 216
~ sub_c015a1c8 -> sub_c015ab48 : 474496 -> 482760
~ sub_c03071a0 -> sub_c0309b68 : 16432 -> 16424
~ sub_c0348cf8 -> sub_c034b6b8 : 34632 -> 34580
~ sub_c0371d7c -> sub_c0374708 : 1316 -> 1232
~ sub_c03776c4 -> sub_c0379ffc : 9428 -> 9408
~ sub_c037d37c -> sub_c037fca0 : 368 -> 384
~ sub_c038157c -> sub_c0383eb0 : 72 -> 60
~ sub_c038bea0 -> sub_c038e7c8 : 600380 -> 600120
~ sub_c04261f4 -> sub_c0428a18 : 31356 -> 31360
~ sub_c04361c4 -> sub_c04389ec : 9296 -> 9292
~ sub_c04386f0 -> sub_c043af14 : 564 -> 544
~ sub_c0438a68 -> sub_c043b278 : 980 -> 1040
~ sub_c0438eb8 -> sub_c043b704 : 312 -> 328
~ sub_c0438ff0 -> sub_c043b84c : 176 -> 200
~ sub_c04390a0 -> sub_c043b914 : 392 -> 408
~ sub_c0439228 -> sub_c043baac : 56 -> 68
~ sub_c0439288 -> sub_c043bb18 : 688 -> 712
~ sub_c0439538 -> sub_c043bde0 : 844 -> 940
~ sub_c04398b0 -> sub_c043c1b8 : 592 -> 576
~ sub_c0439b00 -> sub_c043c3f8 : 38152 -> 38160
~ sub_c04defdc -> sub_c04e18dc : 56804 -> 56956
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "I14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "I28@?0Q8I16@?<I@?{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}>20"
+ "Invalid key value while decoding result type for unloadMemoryWithFlags"
+ "Invalid key value while decoding result type for unloadWithFlags"
+ "Invalid key value while decoding result type for updateXnuContentWithFlags"
+ "_insecure_random_buf"
+ "invalid rawValue for XnuContentANEFlags: unexpected bits in value, "
+ "invalid rawValue for XnuContentUnloadFlags: unexpected bits in value, "
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:982)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8903)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8331)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7872)"
+ "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6854)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2216)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5356)"
+ "s[0] || s[1]"
+ "unloadWithFlags threw an unexpected error type"
+ "unmapXnuContentRegionWithFlags"
+ "{?=[2Q]}20@?0Q8I16"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
- "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
- "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
```
