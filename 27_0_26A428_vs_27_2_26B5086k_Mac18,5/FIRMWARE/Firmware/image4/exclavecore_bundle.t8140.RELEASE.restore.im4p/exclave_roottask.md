## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8140.RELEASE.restore.im4p/exclave_roottask`

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
-  __TEXT.__text: 0x4ef144
+1490.40.21.0.0
+  __TEXT.__text: 0x4f1ad0
   __TEXT.__lcxx_override: 0xe4
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
-  __TEXT.__eh_frame: 0x21de4
-  __DATA.__data: 0xcf50
+  __TEXT.__eh_frame: 0x2215c
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

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 19276
+  Functions: 19309
   Symbols:   29
-  CStrings:  6084
+  CStrings:  6096
 
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
