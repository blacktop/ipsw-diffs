## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_roottask`

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
-  __TEXT.__text: 0x4e7a3c
+1490.40.21.0.0
+  __TEXT.__text: 0x4ea31c
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__const: 0xf23d0
-  __TEXT.__cstring: 0x3d1fc
-  __TEXT.__swift5_typeref: 0xcfbc
+  __TEXT.__const: 0xf28a0
+  __TEXT.__cstring: 0x3d54c
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
-  __TEXT.__eh_frame: 0x21edc
-  __DATA.__data: 0xcf50
+  __TEXT.__eh_frame: 0x22254
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
   Functions: 841
   Symbols:   29
-  CStrings:  6084
+  CStrings:  6096
 
Functions:
~ sub_c0067fa8 -> sub_c0067e9c : 233832 -> 234948
~ sub_c00a2f9c -> sub_c00a32ec : 56912 -> 56852
~ sub_c00b0e5c -> sub_c00b1170 : 13360 -> 13364
~ sub_c00b43b0 -> sub_c00b46c8 : 144 -> 316
~ sub_c00b47f8 -> sub_c00b4bbc : 37292 -> 37340
~ sub_c00d54a0 -> sub_c00d5894 : 111012 -> 111736
~ sub_c00ff244 -> sub_c00ff90c : 78928 -> 78936
~ sub_c012a704 -> sub_c012add4 : 58528 -> 59144
~ sub_c0138ba4 -> sub_c01394dc : 96764 -> 96756
~ sub_c0150718 -> sub_c0151048 : 232 -> 184
~ sub_c0157dc8 -> sub_c01586c8 : 473068 -> 481228
~ sub_c03032d0 -> sub_c0305bb0 : 16392 -> 16384
~ sub_c0344530 -> sub_c0346e08 : 34044 -> 33996
~ sub_c036d218 -> sub_c036fac0 : 1420 -> 1336
~ sub_c0372a44 -> sub_c0375298 : 9496 -> 9488
~ sub_c0378514 -> sub_c037ad60 : 1088 -> 1104
~ sub_c0387194 -> sub_c03899f0 : 600404 -> 600144
~ sub_c0421408 -> sub_c0423b60 : 30344 -> 30348
~ sub_c04337ac -> sub_c0435f08 : 564 -> 544
~ sub_c0433b24 -> sub_c043626c : 988 -> 1048
~ sub_c0433f8c -> sub_c0436710 : 312 -> 328
~ sub_c04340c4 -> sub_c0436858 : 160 -> 184
~ sub_c0434164 -> sub_c0436910 : 412 -> 428
~ sub_c0434300 -> sub_c0436abc : 64 -> 76
~ sub_c0434368 -> sub_c0436b30 : 716 -> 740
~ sub_c0434634 -> sub_c0436e14 : 864 -> 960
~ sub_c0434994 -> sub_c04371d4 : 564 -> 548
~ sub_c0434bc8 -> sub_c04373f8 : 38284 -> 38292
~ sub_c048d1a8 -> sub_c048f9e0 : 1508 -> 1512
~ sub_c04d9354 -> sub_c04dbb90 : 58736 -> 58900
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "I14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "I28@?0Q8I16@?<I@?{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}>20"
+ "Invalid key value while decoding result type for unloadMemoryWithFlags"
+ "Invalid key value while decoding result type for unloadWithFlags"
+ "Invalid key value while decoding result type for updateXnuContentWithFlags"
+ "_insecure_random_buf"
+ "invalid rawValue for XnuContentANEFlags: unexpected bits in value, "
+ "invalid rawValue for XnuContentUnloadFlags: unexpected bits in value, "
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:982)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8903)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8331)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7872)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6854)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2216)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5356)"
+ "s[0] || s[1]"
+ "unloadWithFlags threw an unexpected error type"
+ "unmapXnuContentRegionWithFlags"
+ "{?=[2Q]}20@?0Q8I16"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
```
