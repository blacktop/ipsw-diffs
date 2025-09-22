## StreamingZip

> `/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip`

```diff

-241.0.0.0.0
-  __TEXT.__text: 0x11d68
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x5d4
+244.0.0.0.0
+  __TEXT.__text: 0x121f8
+  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__objc_methlist: 0x604
   __TEXT.__const: 0x16a
-  __TEXT.__gcc_except_tab: 0x26c
-  __TEXT.__cstring: 0x1cc0
-  __TEXT.__oslogstring: 0x3574
-  __TEXT.__unwind_info: 0x248
-  __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methname: 0xea9
-  __TEXT.__objc_methtype: 0x441
-  __TEXT.__objc_stubs: 0xb40
+  __TEXT.__gcc_except_tab: 0x290
+  __TEXT.__cstring: 0x1ccd
+  __TEXT.__oslogstring: 0x362e
+  __TEXT.__unwind_info: 0x270
+  __TEXT.__objc_classname: 0xc9
+  __TEXT.__objc_methname: 0xf13
+  __TEXT.__objc_methtype: 0x46e
+  __TEXT.__objc_stubs: 0xb80
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0xa58
+  __DATA_CONST.__const: 0xad0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x438
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xfa0
-  __AUTH_CONST.__objc_const: 0x6a0
-  __DATA.__objc_ivar: 0x2c
+  __AUTH_CONST.__objc_const: 0x6c0
+  __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x308
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7B52DA40-6236-38EF-BBBE-F330E0CAC459
-  Functions: 150
-  Symbols:   829
-  CStrings:  862
+  UUID: 7E2EDC37-5A14-31BF-9695-DC8217BDEF83
+  Functions: 158
+  Symbols:   854
+  CStrings:  872
 
Symbols:
+ +[SZExtractor(Testing) availableExtractionMemory]
+ +[SZExtractor(Testing) maxAvailableExtractionMemory]
+ -[SZExtractor _runWithLock:]
+ -[SZExtractor setUnzipServiceConnection:]
+ GCC_except_table27
+ GCC_except_table33
+ GCC_except_table48
+ GCC_except_table66
+ GCC_except_table93
+ _OBJC_IVAR_$_SZExtractor._ivarLock
+ __OBJC_$_PROP_LIST_SZExtractor.412
+ __ReserveUpToBytes
+ ___36-[SZExtractor setExtractorDelegate:]_block_invoke
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.163
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.170
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.175
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.176
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.178
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.203
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.204
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.208
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.110
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.114
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.86
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_3
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_4
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ _objc_msgSend$_runWithLock:
+ _objc_msgSend$description
+ _objc_msgSend$setUnzipServiceConnection:
+ _objc_retain_x28
+ _objc_retain_x9
- GCC_except_table36
- GCC_except_table42
- GCC_except_table62
- GCC_except_table85
- __OBJC_$_PROP_LIST_SZExtractor.408
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.154
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.161
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.166
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.167
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.169
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.194
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.195
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.199
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.101
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.106
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.77
- _objc_msgSend$setLastResumptionOffset:
CStrings:
+ "&"
+ "-[SZExtractor setExtractorDelegate:]_block_invoke"
+ "Unable to reserve %zu bytes; %zu available"
+ "Waiting for %zu bytes to become available; %zu currently available"
+ "Waiting for at least %zu bytes to become available; %zu currently available"
+ "_ivarLock"
+ "_runWithLock:"
+ "availableExtractionMemory"
+ "maxAvailableExtractionMemory"
+ "setUnzipServiceConnection:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "-[SZExtractor setExtractorDelegate:]"

```
