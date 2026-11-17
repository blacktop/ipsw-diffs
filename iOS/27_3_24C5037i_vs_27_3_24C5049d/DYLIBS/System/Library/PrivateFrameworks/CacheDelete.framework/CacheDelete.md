## CacheDelete

> `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete`

```diff

-904.40.2.0.0
-  __TEXT.__text: 0x35e80
-  __TEXT.__objc_methlist: 0x1884
+904.60.1.0.1
+  __TEXT.__text: 0x36bc0
+  __TEXT.__objc_methlist: 0x18dc
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__const: 0x1f8
-  __TEXT.__gcc_except_tab: 0xd34
-  __TEXT.__cstring: 0x25c4
-  __TEXT.__oslogstring: 0x60bf
-  __TEXT.__unwind_info: 0xc78
+  __TEXT.__gcc_except_tab: 0xd64
+  __TEXT.__cstring: 0x2612
+  __TEXT.__oslogstring: 0x60fb
+  __TEXT.__unwind_info: 0xcb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe30
+  __DATA_CONST.__const: 0xe58
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_selrefs: 0x1180
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x200
   __DATA_CONST.__got: 0x1e8
-  __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x21a0
-  __AUTH_CONST.__objc_const: 0x2388
+  __AUTH_CONST.__const: 0x660
+  __AUTH_CONST.__cfstring: 0x21c0
+  __AUTH_CONST.__objc_const: 0x23b8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x370
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x6e0
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x170
+  __DATA.__objc_ivar: 0x174
   __DATA.__data: 0x4f8
   __DATA_DIRTY.__objc_ivar: 0x2c
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0xc
-  __DATA_DIRTY.__bss: 0x1c0
+  __DATA_DIRTY.__bss: 0x1e8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 815
-  Symbols:   1518
-  CStrings:  889
+  Functions: 830
+  Symbols:   1534
+  CStrings:  892
 
Symbols:
+ +[CDPurgeableResultCache sharedPublicPurgeableResultsCache]
+ -[CDRecentInfo coarsenDiskSpace]
+ -[CDRecentServiceInfo coarsenDiskSpace]
+ -[CDRecentVolumeInfo coarsenDiskSpace]
+ -[CDRecentVolumeInfo reduceToTotals]
+ -[CDRecentVolumeInfo setTotals:]
+ -[CDRecentVolumeInfo totals]
+ GCC_except_table2
+ GCC_except_table9
+ _OBJC_IVAR_$_CDRecentVolumeInfo._totals
+ ___38-[CDRecentVolumeInfo coarsenDiskSpace]_block_invoke
+ ___59+[CDPurgeableResultCache sharedPublicPurgeableResultsCache]_block_invoke
+ ____clientCachedResults_block_invoke
+ ___block_descriptor_40_e8_32bs_e37_v16?0"<CacheDeleteClientProtocol>"8ls32l8
+ ___block_descriptor_57_e8_32s40r48r_e8_v12?0i8lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___publicClientCachedResults_block_invoke
+ __clientCachedResults
+ __registerPurgeableUpdates
+ _coarsenItemizedAmount
+ _publicClientCachedResults
- GCC_except_table15
- GCC_except_table20
- ___block_descriptor_49_e8_32r40r_e8_v12?0i8lr32l8r40l8
- ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
- ___clientCachedResults_block_invoke_2
CStrings:
+ "CACHE_DELETE_PRECOMPUTED_TOTALS"
+ "Exception (%@): Could not decode totals dict for volume: %@"
+ "com.apple.cache_delete.public_purgeable_cache"
```
