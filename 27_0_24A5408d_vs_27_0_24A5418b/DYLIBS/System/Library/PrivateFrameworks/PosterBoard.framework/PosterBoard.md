## PosterBoard

> `/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`

```diff

-355.0.5.0.0
-  __TEXT.__text: 0x279c78
-  __TEXT.__objc_methlist: 0xefbc
-  __TEXT.__const: 0x7314
+355.0.8.0.0
+  __TEXT.__text: 0x27a4d0
+  __TEXT.__objc_methlist: 0xf03c
+  __TEXT.__const: 0x7324
   __TEXT.__gcc_except_tab: 0x4c60
-  __TEXT.__cstring: 0x14745
-  __TEXT.__oslogstring: 0x1ea9a
+  __TEXT.__cstring: 0x148a5
+  __TEXT.__oslogstring: 0x1eaca
   __TEXT.__dlopen_cstrs: 0x2c6
   __TEXT.__ustring: 0xe
   __TEXT.__swift5_typeref: 0x8a56

   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift_as_cont: 0xe0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6d10
+  __TEXT.__unwind_info: 0x6d30
   __TEXT.__eh_frame: 0x1a38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x52a8
-  __DATA_CONST.__objc_classlist: 0x750
+  __DATA_CONST.__const: 0x52d0
+  __DATA_CONST.__objc_classlist: 0x758
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x6d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9ce8
+  __DATA_CONST.__objc_selrefs: 0x9d38
   __DATA_CONST.__objc_protorefs: 0x2d0
-  __DATA_CONST.__objc_superrefs: 0x3e0
+  __DATA_CONST.__objc_superrefs: 0x3e8
   __DATA_CONST.__objc_arraydata: 0x140
-  __DATA_CONST.__got: 0x1db8
-  __AUTH_CONST.__const: 0x9350
-  __AUTH_CONST.__cfstring: 0xc4c0
-  __AUTH_CONST.__objc_const: 0x3e268
+  __DATA_CONST.__got: 0x1dc8
+  __AUTH_CONST.__const: 0x9370
+  __AUTH_CONST.__cfstring: 0xc5c0
+  __AUTH_CONST.__objc_const: 0x3e398
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x2468
-  __AUTH.__objc_data: 0x3bf0
+  __AUTH_CONST.__auth_got: 0x2470
+  __AUTH.__objc_data: 0x3c40
   __AUTH.__data: 0xff0
-  __DATA.__objc_ivar: 0x1090
+  __DATA.__objc_ivar: 0x109c
   __DATA.__data: 0x6360
-  __DATA.__bss: 0x2f48
+  __DATA.__bss: 0x2f58
   __DATA.__common: 0x130
   __DATA_DIRTY.__objc_data: 0x6e98
   __DATA_DIRTY.__data: 0x1548

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10929
-  Symbols:   15185
-  CStrings:  4016
+  Functions: 10945
+  Symbols:   15222
+  CStrings:  4026
 
Symbols:
+ +[PBFPosterSnapshotThrottlePolicy new]
+ +[PBFPosterSnapshotThrottlePolicy policyForProvider:]
+ -[PBFPosterSnapshotManager _test_installProviderTrackers:enqueuePUIRequests:andRunKickoff:]
+ -[PBFPosterSnapshotThrottlePolicy captureTimeoutInterval]
+ -[PBFPosterSnapshotThrottlePolicy description]
+ -[PBFPosterSnapshotThrottlePolicy initWithMaximumConcurrentSnapshotters:captureTimeoutInterval:requestTimeoutInterval:]
+ -[PBFPosterSnapshotThrottlePolicy init]
+ -[PBFPosterSnapshotThrottlePolicy maximumConcurrentSnapshotters]
+ -[PBFPosterSnapshotThrottlePolicy requestTimeoutInterval]
+ _OBJC_CLASS_$_PBFPosterSnapshotThrottlePolicy
+ _OBJC_CLASS_$_PUIPosterSnapshotHostConfigurationDescriptor
+ _OBJC_IVAR_$_PBFPosterSnapshotThrottlePolicy._captureTimeoutInterval
+ _OBJC_IVAR_$_PBFPosterSnapshotThrottlePolicy._maximumConcurrentSnapshotters
+ _OBJC_IVAR_$_PBFPosterSnapshotThrottlePolicy._requestTimeoutInterval
+ _OBJC_METACLASS_$_PBFPosterSnapshotThrottlePolicy
+ _PBFPosterSnapshotDefaultRequestTimeoutInterval
+ _PRWidgetSnapshotRenderSessionTimeoutIsSufficient
+ __OBJC_$_CLASS_METHODS_PBFPosterSnapshotThrottlePolicy
+ __OBJC_$_INSTANCE_METHODS_PBFPosterSnapshotThrottlePolicy
+ __OBJC_$_INSTANCE_VARIABLES_PBFPosterSnapshotThrottlePolicy
+ __OBJC_$_PROP_LIST_PBFPosterSnapshotThrottlePolicy
+ __OBJC_CLASS_RO_$_PBFPosterSnapshotThrottlePolicy
+ __OBJC_METACLASS_RO_$_PBFPosterSnapshotThrottlePolicy
+ ___53+[PBFPosterSnapshotThrottlePolicy policyForProvider:]_block_invoke
+ ___91-[PBFPosterSnapshotManager _test_installProviderTrackers:enqueuePUIRequests:andRunKickoff:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s_e36_v16?0"<PRUISPosterSceneSettings>"8ls32l8s40l8s48l8
+ ___block_descriptor_40_e8_32s_e59_v32?0"NSString"8"PBFPosterSnapshotProviderTracker"16^B24ls32l8
+ _objc_msgSend$appendDouble:withName:decimalPrecision:
+ _objc_msgSend$captureTimeoutInterval
+ _objc_msgSend$copyWithCaptureTimeoutInterval:
+ _objc_msgSend$initWithMaximumConcurrentSnapshotters:captureTimeoutInterval:requestTimeoutInterval:
+ _objc_msgSend$initWithOutputDescriptor:sceneDescriptor:attachments:analysis:host:
+ _objc_msgSend$maximumConcurrentSnapshotters
+ _objc_msgSend$policyForProvider:
+ _objc_msgSend$pui_setRenderSessionTimeoutInterval:
+ _objc_msgSend$requestTimeoutInterval
+ _objc_msgSend$snapshotOutOfProcessHostConfigurationDescriptor
+ _policyForProvider:.onceToken
+ _policyForProvider:.policiesByProvider
- ___block_descriptor_89_e8_32s40s_e36_v16?0"<PRUISPosterSceneSettings>"8ls32l8s40l8
- _objc_msgSend$initWithOutputDescriptor:sceneDescriptor:attachments:analysis:
CStrings:
+ "PRWidgetSnapshotRenderSessionTimeoutIsSufficient(captureTimeoutInterval)"
+ "captureTimeoutInterval"
+ "captureTimeoutInterval > 0"
+ "com.apple.WidgetFace.WidgetFaceExtension"
+ "maximumConcurrentSnapshotters"
+ "maximumConcurrentSnapshotters > 0"
+ "requestTimeoutInterval"
+ "requestTimeoutInterval > captureTimeoutInterval"
+ "throttling snapshots for provider %{public}@: %{public}@"
+ "v32@?0@\"NSString\"8@\"PBFPosterSnapshotProviderTracker\"16^B24"
```
