## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/A/AppStoreDaemon`

```diff

-11.0.51.0.0
-  __TEXT.__text: 0x573b0
+11.0.56.0.0
+  __TEXT.__text: 0x58468
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x76e8
-  __TEXT.__cstring: 0xf0b8
+  __TEXT.__objc_methlist: 0x7968
+  __TEXT.__cstring: 0xf125
   __TEXT.__const: 0x1c0
   __TEXT.__swift5_typeref: 0xe
   __TEXT.__constg_swiftt: 0x28

   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xb7c
   __TEXT.__oslogstring: 0x2770
-  __TEXT.__unwind_info: 0x1a78
-  __TEXT.__objc_classname: 0x1378
-  __TEXT.__objc_methname: 0x106c8
-  __TEXT.__objc_methtype: 0x2910
-  __TEXT.__objc_stubs: 0x5840
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__objc_classlist: 0x508
+  __TEXT.__unwind_info: 0x1b00
+  __TEXT.__objc_classname: 0x13c1
+  __TEXT.__objc_methname: 0x10a84
+  __TEXT.__objc_methtype: 0x29bb
+  __TEXT.__objc_stubs: 0x5920
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__objc_classlist: 0x520
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33f0
+  __DATA_CONST.__objc_selrefs: 0x34c8
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__auth_ptr: 0x58
   __AUTH_CONST.__const: 0x1f30
-  __AUTH_CONST.__cfstring: 0x3de0
-  __AUTH_CONST.__objc_const: 0x13970
+  __AUTH_CONST.__cfstring: 0x3f40
+  __AUTH_CONST.__objc_const: 0x13e90
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0xc40
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0xc74
   __DATA.__data: 0x1038
   __DATA.__bss: 0x300
   __DATA.__common: 0x150

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3281
-  Symbols:   6768
-  CStrings:  836
+  Functions: 3332
+  Symbols:   6874
+  CStrings:  847
 
Symbols:
+ +[ASDAlertAction actionWithTitle:]
+ +[ASDAlertAction actionWithTitle:style:]
+ +[ASDAlertAction supportsSecureCoding]
+ +[ASDAlertPresentationRequest requestWithTitle:message:]
+ +[ASDAlertPresentationRequest supportsSecureCoding]
+ +[ASDAlertPresentationResult supportsSecureCoding]
+ -[ASDAlertAction .cxx_destruct]
+ -[ASDAlertAction encodeWithCoder:]
+ -[ASDAlertAction identifier]
+ -[ASDAlertAction initWithCoder:]
+ -[ASDAlertAction initWithTitle:]
+ -[ASDAlertAction initWithTitle:style:]
+ -[ASDAlertAction setStyle:]
+ -[ASDAlertAction setTitle:]
+ -[ASDAlertAction style]
+ -[ASDAlertAction title]
+ -[ASDAlertPresentationRequest .cxx_destruct]
+ -[ASDAlertPresentationRequest actions]
+ -[ASDAlertPresentationRequest addActionWithTitle:]
+ -[ASDAlertPresentationRequest addActionWithTitle:style:]
+ -[ASDAlertPresentationRequest encodeWithCoder:]
+ -[ASDAlertPresentationRequest iconBundlePath]
+ -[ASDAlertPresentationRequest icon]
+ -[ASDAlertPresentationRequest initWithCoder:]
+ -[ASDAlertPresentationRequest initWithTitle:message:]
+ -[ASDAlertPresentationRequest logKey]
+ -[ASDAlertPresentationRequest message]
+ -[ASDAlertPresentationRequest setActions:]
+ -[ASDAlertPresentationRequest setIcon:]
+ -[ASDAlertPresentationRequest setIconBundlePath:]
+ -[ASDAlertPresentationRequest setLogKey:]
+ -[ASDAlertPresentationRequest setMessage:]
+ -[ASDAlertPresentationRequest setStyle:]
+ -[ASDAlertPresentationRequest setTitle:]
+ -[ASDAlertPresentationRequest style]
+ -[ASDAlertPresentationRequest title]
+ -[ASDAlertPresentationResult .cxx_destruct]
+ -[ASDAlertPresentationResult encodeWithCoder:]
+ -[ASDAlertPresentationResult error]
+ -[ASDAlertPresentationResult initWithCoder:]
+ -[ASDAlertPresentationResult initWithError:]
+ -[ASDAlertPresentationResult initWithSelectedActionIdentifier:]
+ -[ASDAlertPresentationResult isSelectedAction:]
+ -[ASDAlertPresentationResult selectedActionIdentifier]
+ -[ASDPurchaseManager purchaseBatchWithItemMetadata:additionalBuyParams:withResultHandler:]
+ -[ASDViewPresentationRequest .cxx_destruct]
+ -[ASDViewPresentationRequest configuration]
+ -[ASDViewPresentationRequest initWithViewIdentifier:configuration:]
+ OBJC_IVAR_$_ASDAlertAction._identifier
+ OBJC_IVAR_$_ASDAlertAction._style
+ OBJC_IVAR_$_ASDAlertAction._title
+ OBJC_IVAR_$_ASDAlertPresentationRequest._actions
+ OBJC_IVAR_$_ASDAlertPresentationRequest._icon
+ OBJC_IVAR_$_ASDAlertPresentationRequest._iconBundlePath
+ OBJC_IVAR_$_ASDAlertPresentationRequest._logKey
+ OBJC_IVAR_$_ASDAlertPresentationRequest._message
+ OBJC_IVAR_$_ASDAlertPresentationRequest._style
+ OBJC_IVAR_$_ASDAlertPresentationRequest._title
+ OBJC_IVAR_$_ASDAlertPresentationResult._error
+ OBJC_IVAR_$_ASDAlertPresentationResult._selectedActionIdentifier
+ OBJC_IVAR_$_ASDViewPresentationRequest._configuration
+ _ASDViewConfigurationKeyAppIconPath
+ _ASDViewConfigurationKeyAppName
+ _ASDViewConfigurationKeyAppSize
+ _OBJC_CLASS_$_ASDAlertAction
+ _OBJC_CLASS_$_ASDAlertPresentationRequest
+ _OBJC_CLASS_$_ASDAlertPresentationResult
+ _OBJC_METACLASS_$_ASDAlertAction
+ _OBJC_METACLASS_$_ASDAlertPresentationRequest
+ _OBJC_METACLASS_$_ASDAlertPresentationResult
+ __OBJC_$_CLASS_METHODS_ASDAlertAction
+ __OBJC_$_CLASS_METHODS_ASDAlertPresentationRequest
+ __OBJC_$_CLASS_METHODS_ASDAlertPresentationResult
+ __OBJC_$_CLASS_PROP_LIST_ASDAlertAction
+ __OBJC_$_CLASS_PROP_LIST_ASDAlertPresentationRequest
+ __OBJC_$_CLASS_PROP_LIST_ASDAlertPresentationResult
+ __OBJC_$_INSTANCE_METHODS_ASDAlertAction
+ __OBJC_$_INSTANCE_METHODS_ASDAlertPresentationRequest
+ __OBJC_$_INSTANCE_METHODS_ASDAlertPresentationResult
+ __OBJC_$_INSTANCE_VARIABLES_ASDAlertAction
+ __OBJC_$_INSTANCE_VARIABLES_ASDAlertPresentationRequest
+ __OBJC_$_INSTANCE_VARIABLES_ASDAlertPresentationResult
+ __OBJC_$_PROP_LIST_ASDAlertAction
+ __OBJC_$_PROP_LIST_ASDAlertPresentationRequest
+ __OBJC_$_PROP_LIST_ASDAlertPresentationResult
+ __OBJC_CLASS_PROTOCOLS_$_ASDAlertAction
+ __OBJC_CLASS_PROTOCOLS_$_ASDAlertPresentationRequest
+ __OBJC_CLASS_PROTOCOLS_$_ASDAlertPresentationResult
+ __OBJC_CLASS_RO_$_ASDAlertAction
+ __OBJC_CLASS_RO_$_ASDAlertPresentationRequest
+ __OBJC_CLASS_RO_$_ASDAlertPresentationResult
+ __OBJC_METACLASS_RO_$_ASDAlertAction
+ __OBJC_METACLASS_RO_$_ASDAlertPresentationRequest
+ __OBJC_METACLASS_RO_$_ASDAlertPresentationResult
+ ___90-[ASDPurchaseManager purchaseBatchWithItemMetadata:additionalBuyParams:withResultHandler:]_block_invoke
+ ___90-[ASDPurchaseManager purchaseBatchWithItemMetadata:additionalBuyParams:withResultHandler:]_block_invoke_2
+ ___90-[ASDPurchaseManager purchaseBatchWithItemMetadata:additionalBuyParams:withResultHandler:]_block_invoke_3
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_AppStoreDaemon
+ _objc_msgSend$UUID
+ _objc_msgSend$addActionWithTitle:style:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$initWithTitle:
+ _objc_msgSend$initWithTitle:message:
+ _objc_msgSend$initWithTitle:style:
+ _objc_msgSend$purchaseBatchWithItemMetadata:additionalBuyParams:withReplyHandler:
CStrings:
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:156 : Unsupported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:162 : Unsupported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:167 : Unsupported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:172 : Unsupported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:102 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:106 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:112 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:116 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:120 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:136 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:140 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:148 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:48 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:52 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:58 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:62 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:66 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:70 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:76 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:80 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:84 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:88 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:94 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:98 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:19 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:23 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:27 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:17 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:21 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:25 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:29 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:33 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:37 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:38 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCompleteCoordinatorsRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCompleteCoordinatorsRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:36 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:42 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:48 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:52 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:56 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDownloadQueueRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDownloadQueueRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDEphemeralRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:21 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:27 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoUpdateRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestResponse_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestResponse_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:46 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:50 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManager_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManager_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:46 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:50 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:36 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerJobMetadata_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerJobMetadata_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerJobMetadata_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerJobMetadata_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerRequest_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerResponse_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerResponse_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsResponse_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsResponse_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersonalizationStore_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:46 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:50 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPushCacheDeleteUpdateRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPushCacheDeleteUpdateRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:36 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:36 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestResponse_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestResponse_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequest_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRollableLog_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRollableLog_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateWatchApps_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateWatchApps_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore_macOS.m:169 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore_macOS.m:200 : Not supported on macOS"
+ "actions"
+ "appName"
+ "appSize"
+ "icon"
+ "iconBundlePath"
+ "iconPath"
+ "identifier"
+ "message"
+ "selectedActionIdentifier"
+ "style"
+ "title"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:156 : Unsupported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:162 : Unsupported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:167 : Unsupported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:172 : Unsupported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:102 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:106 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:112 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:116 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:120 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:136 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:140 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:148 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:48 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:52 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:58 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:62 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:66 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:70 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:76 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:80 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:84 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:88 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:94 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:98 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:19 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:23 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:27 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:17 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:21 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:25 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:29 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:33 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:37 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:38 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCompleteCoordinatorsRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCompleteCoordinatorsRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:36 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:42 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:48 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:52 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:56 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDownloadQueueRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDownloadQueueRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDEphemeralRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:21 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:27 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoUpdateRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestResponse_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestResponse_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:46 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:50 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManager_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManager_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:46 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:50 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:36 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerJobMetadata_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerJobMetadata_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerJobMetadata_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerJobMetadata_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerRequest_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerResponse_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobSchedulerResponse_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsResponse_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsResponse_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersonalizationStore_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:46 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:50 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPushCacheDeleteUpdateRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPushCacheDeleteUpdateRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:36 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:36 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestResponse_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestResponse_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequest_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRollableLog_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRollableLog_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateWatchApps_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateWatchApps_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore_macOS.m:169 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore_macOS.m:200 : Not supported on macOS"

```
