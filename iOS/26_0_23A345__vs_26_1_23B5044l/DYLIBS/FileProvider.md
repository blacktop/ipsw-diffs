## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-3882.2.1.0.0
-  __TEXT.__text: 0x1327e4
-  __TEXT.__auth_stubs: 0x1d10
-  __TEXT.__objc_methlist: 0xe54c
-  __TEXT.__const: 0x87e
-  __TEXT.__gcc_except_tab: 0xa3b0
-  __TEXT.__cstring: 0x145b2
-  __TEXT.__oslogstring: 0xdc9b
+3882.40.85.502.1
+  __TEXT.__text: 0x132f54
+  __TEXT.__auth_stubs: 0x1d30
+  __TEXT.__objc_methlist: 0xe58c
+  __TEXT.__const: 0x88e
+  __TEXT.__gcc_except_tab: 0xa3f0
+  __TEXT.__cstring: 0x14592
+  __TEXT.__oslogstring: 0xdcd7
   __TEXT.__dlopen_cstrs: 0x79f
   __TEXT.__ustring: 0x21e
   __TEXT.__swift5_typeref: 0xb4

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x5940
+  __TEXT.__unwind_info: 0x5978
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x2045
-  __TEXT.__objc_methname: 0x23e5e
-  __TEXT.__objc_methtype: 0x68b6
-  __TEXT.__objc_stubs: 0x13f20
+  __TEXT.__objc_methname: 0x23f0d
+  __TEXT.__objc_methtype: 0x6910
+  __TEXT.__objc_stubs: 0x13f80
   __DATA_CONST.__got: 0xab8
-  __DATA_CONST.__const: 0x6048
+  __DATA_CONST.__const: 0x6058
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d98
+  __DATA_CONST.__objc_selrefs: 0x6dc8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
-  __AUTH_CONST.__auth_got: 0xe98
-  __AUTH_CONST.__const: 0x1c28
-  __AUTH_CONST.__cfstring: 0x11140
-  __AUTH_CONST.__objc_const: 0x247c8
+  __AUTH_CONST.__auth_got: 0xea8
+  __AUTH_CONST.__const: 0x1c88
+  __AUTH_CONST.__cfstring: 0x11120
+  __AUTH_CONST.__objc_const: 0x247f0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH.__objc_data: 0x500
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x1088
-  __DATA.__data: 0x20c0
-  __DATA.__bss: 0xa80
+  __DATA.__data: 0x20c8
+  __DATA.__bss: 0xac0
   __DATA.__common: 0x39
   __DATA_DIRTY.__objc_data: 0x3ca0
   __DATA_DIRTY.__data: 0x2c1

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: AABE7332-6830-3F64-97E1-E6E6484221F2
-  Functions: 7248
-  Symbols:   23459
-  CStrings:  12280
+  UUID: A0730C42-FB14-3544-8F21-63B056516844
+  Functions: 7269
+  Symbols:   23510
+  CStrings:  12291
 
Symbols:
+ -[FPItemManager _fetchItemForURL:options:completionHandler:]
+ -[FPItemManager _fetchItemForURL:options:completionHandler:].cold.1
+ -[FPItemManager _fetchPathComponentsForURL:synchronously:completionHandler:]
+ -[FPItemManager _fetchPathComponentsForURL:synchronously:completionHandler:].cold.1
+ -[FPItemManager fetchItemForURL:options:completionHandler:]
+ -[FPItemManager itemForURL:options:error:]
+ -[FPItemManager pathComponentsForURL:error:]
+ -[NSXPCConnection(FPAdditions) fp_bundleRecord]
+ GCC_except_table108
+ GCC_except_table77
+ _FPGetQoSValueForClass
+ _FPPrecheckTCCReadAccess
+ __OBJC_$_PROP_LIST_FPXPCAutomaticErrorProxy.106
+ ___42-[FPItemManager itemForURL:options:error:]_block_invoke
+ ___44-[FPItemManager pathComponentsForURL:error:]_block_invoke
+ ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.17
+ ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.17.cold.1
+ ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.19
+ ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.19.cold.1
+ ___60-[FPItemManager _fetchItemForURL:options:completionHandler:]_block_invoke
+ ___67-[FPPendingSetEnumerator enumerateItemsForObserver:startingAtPage:]_block_invoke.440
+ ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke.444
+ ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke_2.447
+ ___76-[FPItemManager _fetchPathComponentsForURL:synchronously:completionHandler:]_block_invoke
+ ___block_descriptor_102_e8_32s40s48s56s64s72r_e17_v16?0"NSError"8lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_114_e8_32s40s48s56s64bs72r80r88w_e22_v16?0"NSInvocation"8ls32l8r72l8s40l8s48l8w88l8s64l8s56l8r80l8
+ ___block_literal_global.193
+ ___block_literal_global.202
+ ___block_literal_global.235
+ ___block_literal_global.258
+ ___block_literal_global.260
+ ___block_literal_global.266
+ ___block_literal_global.413
+ ___block_literal_global.419
+ ___block_literal_global.421
+ ___block_literal_global.429
+ ___block_literal_global.438
+ ___block_literal_global.442
+ ___block_literal_global.446
+ ___block_literal_global.45
+ ___block_literal_global.502
+ ___block_literal_global.584
+ ___block_literal_global.586
+ ___block_literal_global.641
+ ___block_literal_global.95
+ ___fpfs_supports_fsevents_purge_detection_block_invoke
+ ___fpfs_supports_fsevents_purge_detection_block_invoke_2
+ ___fpfs_supports_gutenberg_block_invoke
+ _emitFinalSignPost
+ _forceDeobfuscateFilenames
+ _fp_disableFilenameObsucationInCurrentProcess
+ _fpfs_is_seed_build.is_seed_build
+ _fpfs_supports_fsevents_purge_detection
+ _fpfs_supports_fsevents_purge_detection.cold.1
+ _fpfs_supports_fsevents_purge_detection.cold.2
+ _fpfs_supports_fsevents_purge_detection.enablementFSEvents
+ _fpfs_supports_fsevents_purge_detection.feature_enabled
+ _fpfs_supports_fsevents_purge_detection.once_token
+ _fpfs_supports_fsevents_purge_detection.once_token.36
+ _fpfs_supports_gutenberg
+ _fpfs_supports_gutenberg.cold.1
+ _fpfs_supports_gutenberg.feature_enabled
+ _fpfs_supports_gutenberg.once_token
+ _getQoSValueForThread
+ _kFPBundleRecordAssociatedObjectKey
+ _objc_msgSend$_fetchItemForURL:options:completionHandler:
+ _objc_msgSend$_fetchPathComponentsForURL:synchronously:completionHandler:
+ _objc_msgSend$fp_bundleRecord
+ _objc_msgSend$itemForURL:options:completionHandler:
+ _objc_msgSend$itemForURL:options:error:
+ _pthread_get_qos_class_np
+ _pthread_self
- -[FPItemManager _fetchItemForURL:synchronously:completionHandler:]
- -[FPItemManager _fetchItemForURL:synchronously:skipURLValidation:completionHandler:]
- -[FPItemManager _fetchItemForURL:synchronously:skipURLValidation:completionHandler:].cold.1
- -[FPItemManager fetchPathComponentsForURL:completionHandler:].cold.1
- GCC_except_table100
- GCC_except_table104
- __OBJC_$_PROP_LIST_FPXPCAutomaticErrorProxy.105
- ___34-[FPItemManager itemForURL:error:]_block_invoke
- ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.16
- ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.16.cold.1
- ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.18
- ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.18.cold.1
- ___61-[FPItemManager fetchPathComponentsForURL:completionHandler:]_block_invoke
- ___67-[FPPendingSetEnumerator enumerateItemsForObserver:startingAtPage:]_block_invoke.443
- ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke.447
- ___69-[FPPendingSetEnumerator enumerateChangesForObserver:fromSyncAnchor:]_block_invoke_2.450
- ___84-[FPItemManager _fetchItemForURL:synchronously:skipURLValidation:completionHandler:]_block_invoke
- ___block_descriptor_87_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_99_e8_32s40s48s56bs64r72w_e22_v16?0"NSInvocation"8ls32l8s40l8w72l8s56l8s48l8r64l8
- ___block_literal_global.133
- ___block_literal_global.192
- ___block_literal_global.201
- ___block_literal_global.239
- ___block_literal_global.256
- ___block_literal_global.264
- ___block_literal_global.270
- ___block_literal_global.416
- ___block_literal_global.422
- ___block_literal_global.424
- ___block_literal_global.436
- ___block_literal_global.445
- ___block_literal_global.452
- ___block_literal_global.500
- ___block_literal_global.580
- ___block_literal_global.582
- ___block_literal_global.644
- ___block_literal_global.94
- _objc_msgSend$_fetchItemForURL:synchronously:completionHandler:
- _objc_msgSend$_fetchItemForURL:synchronously:skipURLValidation:completionHandler:
CStrings:
+ "3882.40.85.502.1"
+ "[CRIT] cannot get a temporary URL for domain %@: %@"
+ "_fetchItemForURL:options:completionHandler:"
+ "_fetchPathComponentsForURL:synchronously:completionHandler:"
+ "_test_getDBOptions:completionHandler:"
+ "fetchItemForURL:options:completionHandler:"
+ "fp_bundleRecord"
+ "fsevents"
+ "fseventsPurgeDetection"
+ "gutenberg"
+ "historyPruning"
+ "itemForURL:options:completionHandler:"
+ "itemForURL:options:error:"
+ "pathComponentsForURL:error:"
+ "selector=%{public,signpost.telemetry:string1,name=selector}s"
+ "v32@0:8@\"NSString\"16@?<v@?q@\"NSError\">24"
+ "v40@0:8@\"NSURL\"16Q24@?<v@?@\"FPItem\"@\"NSError\">32"
+ "xpcInfo=%{public,signpost.telemetry:number1,name=xpcInfo}ld"
+ "xpcInfo=%{public,signpost.telemetry:number1,name=xpcInfo}ld enableTelemetry=YES "
- "-[NSFileProviderManager temporaryDirectoryURLWithError:]"
- "3882.2.1"
- "_fetchItemForURL:synchronously:completionHandler:"
- "_fetchItemForURL:synchronously:skipURLValidation:completionHandler:"
- "cannot get a temporary URL for domain %@: %@"
- "enableTelemetry=YES rc=%{public,signpost.telemetry:number1,name=rc}d mainThread=%{public,signpost.telemetry:number2,name=isMainThread}d"
- "query=%{public,signpost.telemetry:string1,name=selector}s"

```
