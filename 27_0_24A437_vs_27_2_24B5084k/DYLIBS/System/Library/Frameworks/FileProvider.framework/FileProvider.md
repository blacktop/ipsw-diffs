## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-4838.0.125.0.0
-  __TEXT.__text: 0x1289a8
-  __TEXT.__objc_methlist: 0xe9dc
-  __TEXT.__const: 0x88a
-  __TEXT.__cstring: 0x14ea2
-  __TEXT.__gcc_except_tab: 0x8b24
+4838.40.53.502.1
+  __TEXT.__text: 0x128a40
+  __TEXT.__objc_methlist: 0xe9f4
+  __TEXT.__const: 0x89a
+  __TEXT.__cstring: 0x14ea3
+  __TEXT.__gcc_except_tab: 0x8b34
   __TEXT.__oslogstring: 0xe394
   __TEXT.__dlopen_cstrs: 0x793
   __TEXT.__ustring: 0x21e

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x6e80
+  __TEXT.__unwind_info: 0x6e88
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6220
+  __DATA_CONST.__const: 0x6228
   __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x70e0
+  __DATA_CONST.__objc_selrefs: 0x70f0
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
   __DATA_CONST.__got: 0xb18
   __AUTH_CONST.__const: 0x1da8
   __AUTH_CONST.__cfstring: 0x115e0
-  __AUTH_CONST.__objc_const: 0x25060
+  __AUTH_CONST.__objc_const: 0x25030
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xeb0
   __AUTH.__objc_data: 0x25f8
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x10d8
+  __DATA.__objc_ivar: 0x10d0
   __DATA.__data: 0x23f0
   __DATA.__common: 0x39
   __DATA_DIRTY.__objc_data: 0x1bf8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7467
-  Symbols:   13845
+  Functions: 7469
+  Symbols:   13849
   CStrings:  4062
 
Symbols:
+ -[FPProviderDomain spotlightIndexName]
+ -[FPProviderDomainChangesReceiver _t_setCachedProviderDomainsByID:]
+ GCC_except_table99
+ _FPSpotlightIndexNamePrefix
+ _fp_bundleRecord.kFPBundleRecordAssociatedObjectKey
+ _fpfs_is_seed_build.is_seed_build
+ _objc_msgSend$spotlightIndexName
- _OBJC_IVAR_$_FPXPCAutomaticErrorProxy._retainCounter
- _OBJC_IVAR_$_FPXPCAutomaticErrorProxy._retainSelfWhileMessageIsPending
- _kFPBundleRecordAssociatedObjectKey
Functions:
~ -[FPXPCAutomaticErrorProxy .cxx_destruct] : 128 -> 116
~ -[FPXPCAutomaticErrorProxy _requestWillBegin:requestID:] : 168 -> 104
~ -[FPXPCAutomaticErrorProxy _requestDidFinish:requestDidFinishBlock:] : 132 -> 28
~ -[FPSpotlightIndexer initWithDomain:log:supportURL:dropIndexDelegate:] : 428 -> 252
- ___58-[FPSpotlightIndexer _indexOneBatchWithCompletionHandler:]_block_invoke.84
+ -[FPProviderDomainChangesReceiver _t_setCachedProviderDomainsByID:]
+ ___58-[FPSpotlightIndexer _indexOneBatchWithCompletionHandler:]_block_invoke.81
~ _fpfs_is_seed_build : 52 -> 56
~ ___fpfs_is_seed_build_block_invoke : 4 -> 16
+ -[FPProviderDomain spotlightIndexName]
~ -[NSXPCConnection(FPAdditions) fp_bundleRecord] : 160 -> 260
CStrings:
+ "4838.40.53.502.1"
+ "com.apple.FileProvider/"
- "4838.0.125"
- "com.apple.FileProvider/%@"
```
