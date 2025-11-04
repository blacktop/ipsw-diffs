## BrowserEngineKit

> `/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit`

```diff

-7622.1.19.2.0
-  __TEXT.__text: 0x1d09c
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_methlist: 0x1850
-  __TEXT.__const: 0xfe6
-  __TEXT.__cstring: 0xf1b
-  __TEXT.__oslogstring: 0x6cb
-  __TEXT.__swift5_typeref: 0x6dc
+7623.1.11.4.0
+  __TEXT.__text: 0x1eb40
+  __TEXT.__auth_stubs: 0x1170
+  __TEXT.__objc_methlist: 0x1920
+  __TEXT.__const: 0x10c6
+  __TEXT.__cstring: 0x11bb
+  __TEXT.__oslogstring: 0x75b
+  __TEXT.__gcc_except_tab: 0x164
+  __TEXT.__dlopen_cstrs: 0x6a
+  __TEXT.__swift5_typeref: 0x6f0
   __TEXT.__swift5_capture: 0x46c
-  __TEXT.__swift5_fieldmd: 0x57c
-  __TEXT.__constg_swiftt: 0xa38
-  __TEXT.__swift5_reflstr: 0x3d2
+  __TEXT.__swift5_fieldmd: 0x5c0
+  __TEXT.__constg_swiftt: 0xac0
+  __TEXT.__swift5_reflstr: 0x402
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_proto: 0x74
-  __TEXT.__swift5_types: 0x7c
+  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__swift5_types: 0x84
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__unwind_info: 0xad8
   __TEXT.__eh_frame: 0xe50
-  __TEXT.__objc_classname: 0x32e
-  __TEXT.__objc_methname: 0x3b87
-  __TEXT.__objc_methtype: 0xef6
-  __TEXT.__objc_stubs: 0x1280
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x1c8
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__objc_classname: 0x35a
+  __TEXT.__objc_methname: 0x3db4
+  __TEXT.__objc_methtype: 0xf56
+  __TEXT.__objc_stubs: 0x1520
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0x388
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1090
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x838
-  __AUTH_CONST.__const: 0x1078
-  __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x3a60
-  __AUTH.__objc_data: 0x860
-  __AUTH.__data: 0x1d0
-  __DATA.__objc_ivar: 0xa0
-  __DATA.__data: 0x7e8
-  __DATA.__bss: 0x9b0
-  __DATA.__common: 0x40
+  __DATA_CONST.__objc_selrefs: 0x1120
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __AUTH_CONST.__auth_got: 0x8c8
+  __AUTH_CONST.__const: 0x1128
+  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__objc_const: 0x3c70
+  __AUTH.__objc_data: 0x8b0
+  __AUTH.__data: 0x2a0
+  __DATA.__objc_ivar: 0xa8
+  __DATA.__data: 0x868
+  __DATA.__bss: 0xac0
+  __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x8e0
   __DATA_DIRTY.__common: 0x38

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9F91B4B4-3ABA-3621-A164-BE8AFD0685AC
-  Functions: 920
-  Symbols:   1545
-  CStrings:  1000
+  UUID: 1144C4BD-0134-340E-8ABD-7ABC57C394E6
+  Functions: 966
+  Symbols:   1685
+  CStrings:  1052
 
Symbols:
+ +[BEWebContentFilter connectionWithInvalidationHandler:]
+ +[BEWebContentFilter shouldEvaluateURLs]
+ -[BEWebContentFilter .cxx_destruct]
+ -[BEWebContentFilter allowURL:completionHandler:]
+ -[BEWebContentFilter allowURLOnMainThread:completionHandler:]
+ -[BEWebContentFilter browserEngineClient]
+ -[BEWebContentFilter dealloc]
+ -[BEWebContentFilter evaluateURL:completionHandler:]
+ -[BEWebContentFilter setBrowserEngineClient:]
+ -[BEWebContentFilter setXpcConnection:]
+ -[BEWebContentFilter xpcConnection]
+ GCC_except_table0
+ GCC_except_table1
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table2
+ GCC_except_table6
+ GCC_except_table8
+ GCC_except_table9
+ _NSLog
+ _OBJC_CLASS_$_BEWebContentFilter
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$__BEUtil
+ _OBJC_IVAR_$_BEWebContentFilter._browserEngineClient
+ _OBJC_IVAR_$_BEWebContentFilter._xpcConnection
+ _OBJC_METACLASS_$_BEWebContentFilter
+ __Block_object_dispose
+ __DATA__TtC16BrowserEngineKitP33_2B65033DDF6D08FA42FE4B653C780BE229RenderingExtensionFeatureData
+ __IVARS__TtC16BrowserEngineKitP33_2B65033DDF6D08FA42FE4B653C780BE229RenderingExtensionFeatureData
+ __METACLASS_DATA__TtC16BrowserEngineKitP33_2B65033DDF6D08FA42FE4B653C780BE229RenderingExtensionFeatureData
+ __OBJC_$_CLASS_METHODS_BEWebContentFilter
+ __OBJC_$_CLASS_PROP_LIST_BEWebContentFilter
+ __OBJC_$_INSTANCE_METHODS_BEWebContentFilter
+ __OBJC_$_INSTANCE_VARIABLES_BEWebContentFilter
+ __OBJC_$_PROP_LIST_BEWebContentFilter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BEKIntermediaryProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BEKIntermediaryProtocol
+ __OBJC_CLASS_RO_$_BEWebContentFilter
+ __OBJC_LABEL_PROTOCOL_$_BEKIntermediaryProtocol
+ __OBJC_METACLASS_RO_$_BEWebContentFilter
+ __OBJC_PROTOCOL_$_BEKIntermediaryProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_BEKIntermediaryProtocol
+ __Unwind_Resume
+ __ZL34audit_stringWebContentRestrictions
+ __ZSt9terminatev
+ __ZZL30getWCRBrowserEngineClientClassvE9softClass.0
+ __ZZL33WebContentRestrictionsLibraryCorePPcE16frameworkLibrary.0
+ ___40+[BEWebContentFilter shouldEvaluateURLs]_block_invoke
+ ___40+[BEWebContentFilter shouldEvaluateURLs]_block_invoke.11
+ ___49-[BEWebContentFilter allowURL:completionHandler:]_block_invoke
+ ___49-[BEWebContentFilter allowURL:completionHandler:]_block_invoke_2
+ ___49-[BEWebContentFilter allowURL:completionHandler:]_block_invoke_3
+ ___49-[BEWebContentFilter allowURL:completionHandler:]_block_invoke_4
+ ___52-[BEWebContentFilter evaluateURL:completionHandler:]_block_invoke
+ ___52-[BEWebContentFilter evaluateURL:completionHandler:]_block_invoke_2
+ ___52-[BEWebContentFilter evaluateURL:completionHandler:]_block_invoke_3
+ ___61-[BEWebContentFilter allowURLOnMainThread:completionHandler:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ____ZL30getWCRBrowserEngineClientClassv_block_invoke
+ ____ZL30getWCRBrowserEngineClientClassv_block_invoke.cold.1
+ ____ZL33WebContentRestrictionsLibraryCorePPc_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_ea8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_ea8_32bs_e19_v20?0B8"NSData"12ls32l8
+ ___block_descriptor_40_ea8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_ea8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_ea8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
+ ___block_descriptor_48_ea8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_49_ea8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.13
+ ___clang_call_terminate
+ ___cxa_begin_catch
+ ___gxx_personality_v0
+ __sl_dlopen
+ _abort_report_np
+ _associated conformance 16BrowserEngineKit25RenderingExtensionFeatureOSHAASQ
+ _dispatch_async
+ _dispatch_get_global_queue
+ _free
+ _objc_copyWeak
+ _objc_getClass
+ _objc_initWeak
+ _objc_msgSend$addOperationWithBlock:
+ _objc_msgSend$allowURL:withCompletion:
+ _objc_msgSend$allowURLOnMainThread:completionHandler:
+ _objc_msgSend$browserEngineClient
+ _objc_msgSend$checkEligibility
+ _objc_msgSend$connectionWithInvalidationHandler:
+ _objc_msgSend$currentQueue
+ _objc_msgSend$evaluateURL:completionHandler:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$isWebContentFilterEnabled:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$resume
+ _objc_msgSend$setBrowserEngineClient:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setXpcConnection:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$xpcConnection
+ _swift_getErrorValue
+ _symbolic _____ 16BrowserEngineKit25RenderingExtensionFeatureO
+ _symbolic _____ 16BrowserEngineKit29RenderingExtensionFeatureData33_2B65033DDF6D08FA42FE4B653C780BE2LLC
- ___block_literal_global.12
CStrings:
+ "%s"
+ "@\"NSXPCConnection\""
+ "@24@0:8@?16"
+ "BEKIntermediaryProtocol"
+ "BEWebContentFilter"
+ "BEWebContentFilter::shouldEvaluateURLs: Remote proxy error: %@"
+ "T@\"NSXPCConnection\",&,N,V_xpcConnection"
+ "T@,&,N,V_browserEngineClient"
+ "Unable to find class %s"
+ "Unexpected eligibility check error in BEDownloadMonitor init: "
+ "WCRBrowserEngineClient"
+ "_TtC16BrowserEngineKitP33_2B65033DDF6D08FA42FE4B653C780BE229RenderingExtensionFeatureData"
+ "_browserEngineClient"
+ "_xpcConnection"
+ "addOperationWithBlock:"
+ "allowURL:completionHandler:"
+ "allowURL:withCompletion:"
+ "allowURLOnMainThread:completionHandler:"
+ "browserEngineClient"
+ "checkEligibility"
+ "com.apple.web-browser-engine.networking.development"
+ "com.apple.web-browser-engine.rendering.development"
+ "com.apple.web-browser-engine.webcontent.development"
+ "connectionWithInvalidationHandler:"
+ "coreMLFeatureEnabled"
+ "currentQueue"
+ "evaluateURL:completionHandler:"
+ "featureDataLock"
+ "isCoreMLFeatureEnabled %{bool}d"
+ "isMainThread"
+ "isWebContentFilterEnabled:"
+ "local:FeatureCoreMLDisabled"
+ "remoteObjectProxyWithErrorHandler:"
+ "sandbox_enable_local_state_flag failed: errno = %d"
+ "setBrowserEngineClient:"
+ "setCoreMLFeatureEnabled %{bool}d"
+ "setInvalidationHandler:"
+ "setXpcConnection:"
+ "shouldEvaluateURLs"
+ "softlink:r:path:/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v16@?0@\"NSError\"8"
+ "v20@?0B8@\"NSData\"12"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v32@0:8@\"NSURL\"16@?<v@?B@\"NSData\">24"
+ "xpcConnection"

```
