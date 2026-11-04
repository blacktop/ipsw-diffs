## exclave_roottask

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_roottask`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
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

-1490.40.28.0.0
-  __TEXT.__text: 0x4eadd0
+1490.60.7.0.0
+  __TEXT.__text: 0x4ecb64
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__const: 0xf28a0
-  __TEXT.__cstring: 0x3d93c
-  __TEXT.__swift5_typeref: 0xd07c
-  __TEXT.__swift5_capture: 0x155c
+  __TEXT.__const: 0xf28e0
+  __TEXT.__cstring: 0x3daec
+  __TEXT.__swift5_typeref: 0xd104
+  __TEXT.__swift5_capture: 0x15c4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0xb37c
+  __TEXT.__swift5_reflstr: 0xb3ec
   __TEXT.__swift5_assocty: 0x7448
-  __TEXT.__swift5_fieldmd: 0x126d8
-  __TEXT.__constg_swiftt: 0x16528
-  __TEXT.__swift5_builtin: 0xed8
+  __TEXT.__swift5_fieldmd: 0x12724
+  __TEXT.__constg_swiftt: 0x16580
+  __TEXT.__swift5_builtin: 0xeec
   __TEXT.__swift5_mpenum: 0x534
   __TEXT.__swift5_protos: 0x49c
   __TEXT.__swift5_proto: 0x2ecc
-  __TEXT.__swift5_types: 0x15a8
+  __TEXT.__swift5_types: 0x15ac
   __TEXT.__swift5_types2: 0x58
   __TEXT.__objc_methtype: 0x246
   __TEXT.__swift_as_entry: 0x230

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x80
-  __TEXT.__eh_frame: 0x222c4
-  __DATA.__data: 0xcf70
+  __TEXT.__eh_frame: 0x22434
+  __DATA.__data: 0xcfe8
   __DATA.__shared_cache: 0x70
   __DATA.__mod_init_func: 0x58
-  __DATA.__auth_ptr: 0x1178
-  __DATA.__const: 0x358c8
+  __DATA.__auth_ptr: 0x1188
+  __DATA.__const: 0x35a30
   __DATA.__ENDPOINTS: 0xa46
   __DATA.__DEVICETREE: 0x30
   __DATA.__got: 0x190

   __PDATA.__shared_cache: 0x0
   Functions: 841
   Symbols:   29
-  CStrings:  6111
+  CStrings:  6120
 
Functions:
~ sub_c0067ec0 -> sub_c0067be0 : 236888 -> 238880
~ sub_c00b53c8 -> sub_c00b58b0 : 37340 -> 37644
~ sub_c00be5a4 -> sub_c00bebbc : 1700 -> 1676
~ sub_c00c2f18 -> sub_c00c3518 : 20044 -> 20140
~ sub_c00c8dfc -> sub_c00c945c : 17228 -> 17224
~ sub_c00d60b0 -> sub_c00d670c : 111744 -> 113456
~ sub_c012b768 -> sub_c012c474 : 59152 -> 63060
~ sub_c0139e78 -> sub_c013bac8 : 96760 -> 96968
~ sub_c01519e8 -> sub_c0153708 : 216 -> 184
~ sub_c0159088 -> sub_c015ad88 : 481208 -> 481224
~ sub_c0375b4c -> sub_c037785c : 9488 -> 9496
~ sub_c0382794 -> sub_c03844ac : 1220 -> 1192
~ sub_c0382d7c -> sub_c0384a78 : 184 -> 156
~ sub_c0446ff0 -> sub_c0448cd0 : 7972 -> 7964
~ sub_c0490340 -> sub_c0492018 : 1512 -> 1508
~ sub_c0490928 -> sub_c04925fc : 7592 -> 7580
~ sub_c04c6f4c -> sub_c04c8c14 : 19624 -> 19528
~ sub_c04dc548 -> sub_c04de1b0 : 59152 -> 59452
~ sub_c04eac58 -> sub_c04ec9ec : 4984 -> 4988
CStrings:
+ "*** error for object %p: %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.3.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "ERROR: remap xnu content at "
+ "Failed to destroy xnu content "
+ "Failed to remap xnu content "
+ "I14@?0{easm_space_destroyxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
+ "I14@?0{easm_space_remapxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
+ "I24@?0Q8@?<I@?{easm_space_remapxnucontentregion__result_s=C(?={easm_failure_s=CS})}>16"
+ "I28@?0Q8I16@?<I@?{easm_space_destroyxnucontentregion__result_s=C(?={easm_failure_s=CS})}>20"
+ "MFM double free"
+ "destroyXnuContentRegion"
+ "free to already-freed small chunk (likely double-free)"
+ "free to empty or invalid freelist chunk (likely double-free)"
+ "invalid MFM address"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8886)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8314)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7858)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2217)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5346)"
+ "not an allocated MFM block"
+ "remapXnuContentRegion"
+ "xnu content mapped at "
- "*** error for object %p: pointer being freed was not allocated\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
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
