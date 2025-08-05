## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.0.72.0.0
-  __TEXT.__text: 0x778980
-  __TEXT.__auth_stubs: 0x48b0
-  __TEXT.__objc_methlist: 0x21b0c
-  __TEXT.__const: 0x5c698
+9.0.76.0.0
+  __TEXT.__text: 0x70565c
+  __TEXT.__auth_stubs: 0x4900
+  __TEXT.__objc_methlist: 0x21b6c
+  __TEXT.__const: 0x587c8
   __TEXT.__dlopen_cstrs: 0x98b
-  __TEXT.__cstring: 0x2a764
-  __TEXT.__swift5_typeref: 0x5a6b
-  __TEXT.__swift5_reflstr: 0x30e4
+  __TEXT.__cstring: 0x2a92e
+  __TEXT.__swift5_typeref: 0x5aad
+  __TEXT.__swift5_reflstr: 0x3124
   __TEXT.__swift5_assocty: 0xe88
-  __TEXT.__constg_swiftt: 0x4714
+  __TEXT.__constg_swiftt: 0x4750
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_fieldmd: 0x3f3c
+  __TEXT.__swift5_fieldmd: 0x3f70
   __TEXT.__swift5_proto: 0xe60
-  __TEXT.__swift5_types: 0x524
+  __TEXT.__swift5_types: 0x528
   __TEXT.__swift_as_entry: 0x628
   __TEXT.__swift_as_ret: 0x748
-  __TEXT.__swift5_capture: 0x2c50
+  __TEXT.__swift5_capture: 0x2c70
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0xb8
-  __TEXT.__oslogstring: 0x2ec9c
-  __TEXT.__gcc_except_tab: 0x5c54
+  __TEXT.__oslogstring: 0x2edd0
+  __TEXT.__gcc_except_tab: 0x5c2c
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0xfd58
-  __TEXT.__eh_frame: 0x12518
-  __TEXT.__objc_classname: 0x3ede
-  __TEXT.__objc_methname: 0x4330c
-  __TEXT.__objc_methtype: 0x77c8
-  __TEXT.__objc_stubs: 0x2dcc0
-  __DATA_CONST.__got: 0x19a0
-  __DATA_CONST.__const: 0xbfd8
-  __DATA_CONST.__objc_classlist: 0x13e0
+  __TEXT.__unwind_info: 0xfd60
+  __TEXT.__eh_frame: 0x12468
+  __TEXT.__objc_classname: 0x3f0d
+  __TEXT.__objc_methname: 0x434b0
+  __TEXT.__objc_methtype: 0x77f1
+  __TEXT.__objc_stubs: 0x2dd40
+  __DATA_CONST.__got: 0x19a8
+  __DATA_CONST.__const: 0xbfe8
+  __DATA_CONST.__objc_classlist: 0x13e8
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x420
+  __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec78
-  __DATA_CONST.__objc_protorefs: 0x200
+  __DATA_CONST.__objc_selrefs: 0xecb0
+  __DATA_CONST.__objc_protorefs: 0x210
   __DATA_CONST.__objc_superrefs: 0xc90
   __DATA_CONST.__objc_arraydata: 0x578
-  __AUTH_CONST.__auth_got: 0x2470
-  __AUTH_CONST.__const: 0x2cb58
-  __AUTH_CONST.__cfstring: 0x21980
-  __AUTH_CONST.__objc_const: 0x3abd0
+  __AUTH_CONST.__auth_got: 0x2498
+  __AUTH_CONST.__const: 0x2af88
+  __AUTH_CONST.__cfstring: 0x219e0
+  __AUTH_CONST.__objc_const: 0x3ad40
   __AUTH_CONST.__objc_intobj: 0xc48
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x8ce0
-  __AUTH.__data: 0x1dd0
-  __DATA.__objc_ivar: 0x1864
-  __DATA.__data: 0x69b0
-  __DATA.__bss: 0x17e79
-  __DATA.__common: 0xb68
+  __AUTH.__objc_data: 0x8b88
+  __AUTH.__data: 0x1e08
+  __DATA.__objc_ivar: 0x1868
+  __DATA.__data: 0x6990
+  __DATA.__bss: 0x174f9
+  __DATA.__common: 0xb60
   __DATA_DIRTY.__objc_ivar: 0x69c
-  __DATA_DIRTY.__objc_data: 0x5968
-  __DATA_DIRTY.__data: 0x1f58
-  __DATA_DIRTY.__bss: 0x3860
-  __DATA_DIRTY.__common: 0x78
+  __DATA_DIRTY.__objc_data: 0x5ac0
+  __DATA_DIRTY.__data: 0x2080
+  __DATA_DIRTY.__bss: 0x41e0
+  __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0C95B0D3-69F1-32A5-AC8D-EE7ABA7D79CA
-  Functions: 24228
-  Symbols:   50010
-  CStrings:  24910
+  UUID: AC162F89-4539-3D65-934B-CC7D0A1D86D0
+  Functions: 24269
+  Symbols:   50062
+  CStrings:  24949
 
Symbols:
+ +[AMSMetrics _createURLSessionPromiseWith:]
+ +[AMSMetrics _urlSessionPromiseWith:]
+ -[AMSMetrics _configureAccountIdentifierForEvent:andActiveAccount:]
+ -[AMSMetrics _determineFlushStrategyWithDataSource:topic:urlSession:]
+ -[AMSMetricsEvent disableAccountIdentifierAutoDecoration]
+ -[AMSMetricsEvent setDisableAccountIdentifierAutoDecoration:]
+ -[AMSPaymentSheetPerformanceMetrics pageRequestTime]
+ -[AMSPaymentSheetPerformanceMetrics setPageRequestTime:]
+ -[AMSPaymentSheetRequest delegatePurchaseRequest]
+ -[AMSPaymentSheetRequest setDelegatePurchaseRequest:]
+ -[AMSPaymentSheetTask _configureWatchDelegateAuthContentItemsForPaymentRequest:]
+ GCC_except_table43
+ GCC_except_table64
+ GCC_except_table70
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table84
+ _AMSDelegatePurchaseRequestUserInfoKey
+ _AMSMetricsEventKeyDisableAccountIdentifierAutoDecoration
+ _OBJC_CLASS_$_OS_dispatch_source
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._pageRequestTime
+ _OBJC_IVAR_$_AMSPaymentSheetRequest._delegatePurchaseRequest
+ __DATA__TtC18AppleMediaServices13ShutdownState
+ __IVARS__TtC18AppleMediaServices13ShutdownState
+ __METACLASS_DATA__TtC18AppleMediaServices13ShutdownState
+ __OBJC_$_PROTOCOL_REFS_OS_dispatch_source
+ __OBJC_$_PROTOCOL_REFS_OS_dispatch_source_signal
+ __OBJC_LABEL_PROTOCOL_$_OS_dispatch_source
+ __OBJC_LABEL_PROTOCOL_$_OS_dispatch_source_signal
+ __OBJC_PROTOCOL_$_OS_dispatch_source
+ __OBJC_PROTOCOL_$_OS_dispatch_source_signal
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke.148
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke.152
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke_2.149
+ ___37+[AMSMetrics _urlSessionPromiseWith:]_block_invoke
+ ___37-[AMSMetrics _flushDataSource:topic:]_block_invoke
+ ___43+[AMSMetrics _createURLSessionPromiseWith:]_block_invoke
+ ___43+[AMSMetrics _createURLSessionPromiseWith:]_block_invoke_2
+ ___44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.159
+ ___44-[AMSPaymentSheetTask _performInProcessTask]_block_invoke.226
+ ___44-[AMSPaymentSheetTask _performInProcessTask]_block_invoke.236
+ ___47-[AMSCookieDatabase cookiePropertiesWithError:]_block_invoke.146
+ ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.155
+ ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.157
+ ___59-[AMSPaymentSheetTask _configurePSD2Decoration:completion:]_block_invoke.272
+ ___62-[AMSPaymentSheetTask _dismissPaymentAuthorizationController:]_block_invoke.291
+ ___62-[AMSPurchaseTask _buySignatureJSONWithFinalizedBlindedItems:]_block_invoke
+ ___76+[AMSCookieDatabase cleanUpCookieDatabasesWithValidIdentifiers:fileManager:]_block_invoke.108
+ ___82-[AMSPaymentSheetTask paymentAuthorizationController:didAuthorizePayment:handler:]_block_invoke.312
+ ___95-[AMSPurchaseProtocolHandler handleCompletionWithTask:metrics:decodedObject:completionHandler:]_block_invoke.74
+ ___95-[AMSPurchaseProtocolHandler handleCompletionWithTask:metrics:decodedObject:completionHandler:]_block_invoke.87
+ ___block_descriptor_56_e8_32s40s48s_e35_"AMSPromise"16?0"AMSURLSession"8ls32l8s40l8s48l8
+ ___block_literal_global.108
+ ___block_literal_global.114
+ ___block_literal_global.131
+ ___block_literal_global.175
+ ___block_literal_global.383
+ ___swift_assignWithCopy_strong
+ ___swift_assignWithTake_strong
+ ___swift_destroy_strong
+ ___swift_initWithCopy_strong
+ _flat unique So25OS_dispatch_source_signal_p
+ _get_type_metadata 15Synchronization6AtomicVySbG.25
+ _objc_msgSend$_configureAccountIdentifierForEvent:andActiveAccount:
+ _objc_msgSend$_createURLSessionPromiseWith:
+ _objc_msgSend$_determineFlushStrategyWithDataSource:topic:urlSession:
+ _objc_msgSend$_urlSessionPromiseWith:
+ _objc_msgSend$disableAccountIdentifierAutoDecoration
+ _objc_msgSend$pageRequestTime
+ _objc_msgSend$purchase:willProcessResponse:
+ _symbolic _____ 18AppleMediaServices13ShutdownStateC
+ _symbolic ______p So25OS_dispatch_source_signalP
+ _symbolic _____ySbG 15Synchronization6AtomicV
+ _symbolic _____yt______pIeggIrzo_ 18AppleMediaServices25PrivateIdentifiersServiceC s5ErrorP
+ _symbolic _____yt______pIggIrzo_ 18AppleMediaServices25PrivateIdentifiersServiceC s5ErrorP
- -[AMSMetrics _configureAccountIdentifierForEvent:]
- -[AMSMetrics _determineFlushStrategyWithDataSource:topic:]
- -[AMSPurchaseTask _filterFormattedBlindedData:]
- GCC_except_table63
- GCC_except_table80
- _OBJC_IVAR_$_AMSMetrics._urlSessionLock
- ___24-[AMSMetrics URLSession]_block_invoke
- ___36-[AMSMetrics _processOperationQueue]_block_invoke.139
- ___36-[AMSMetrics _processOperationQueue]_block_invoke.144
- ___36-[AMSMetrics _processOperationQueue]_block_invoke_2.140
- ___44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.151
- ___44-[AMSPaymentSheetTask _performInProcessTask]_block_invoke.223
- ___44-[AMSPaymentSheetTask _performInProcessTask]_block_invoke.233
- ___47-[AMSCookieDatabase cookiePropertiesWithError:]_block_invoke.143
- ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.147
- ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.149
- ___59-[AMSPaymentSheetTask _configurePSD2Decoration:completion:]_block_invoke.269
- ___62-[AMSPaymentSheetTask _dismissPaymentAuthorizationController:]_block_invoke.285
- ___76+[AMSCookieDatabase cleanUpCookieDatabasesWithValidIdentifiers:fileManager:]_block_invoke.105
- ___82-[AMSPaymentSheetTask paymentAuthorizationController:didAuthorizePayment:handler:]_block_invoke.309
- ___95-[AMSPurchaseProtocolHandler handleCompletionWithTask:metrics:decodedObject:completionHandler:]_block_invoke.72
- ___95-[AMSPurchaseProtocolHandler handleCompletionWithTask:metrics:decodedObject:completionHandler:]_block_invoke.85
- ___97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.141
- ___97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.142
- ___97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.145
- ___97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.147
- ___block_descriptor_64_e8_32s40s48s56s_e48_v24?0"AMSEngagementEnqueueResult"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.132
- ___block_literal_global.167
- ___block_literal_global.377
- _block_copy_helper.42
- _block_descriptor.44
- _block_destroy_helper.43
- _objc_msgSend$_configureAccountIdentifierForEvent:
- _objc_msgSend$_determineFlushStrategyWithDataSource:topic:
- _objc_msgSend$_filterFormattedBlindedData:
- _proc_pidpath
- _strnlen
- _symbolic _____yt______pIeggrzo_ 18AppleMediaServices25PrivateIdentifiersServiceC s5ErrorP
- _symbolic _____yt______pIggrzo_ 18AppleMediaServices25PrivateIdentifiersServiceC s5ErrorP
CStrings:
+ "%{public}@ Generating plist formatted updated request body"
+ "%{public}@: [%{public}@] bag passed used is not of type AMSBag: %{public}@"
+ "%{public}@disableAccountIdentifierAutoDecoration property exists in metrics event when posting; removing it."
+ "%{public}@| Error creating URL. dataVaultURL is nil"
+ ") due to shutting down"
+ "AMSPurchaseProtocolHandler: [%{public}@] Calling will process response"
+ "Discarding transaction ("
+ "Error creating URL"
+ "OS_dispatch_source"
+ "OS_dispatch_source_signal"
+ "Received SIGTERM, shutting down"
+ "SubAccountDelegateAuth"
+ "T@\"AMSDelegatePurchaseRequest\",&,N"
+ "T@\"AMSDelegatePurchaseRequest\",&,N,V_delegatePurchaseRequest"
+ "Td,N,V_pageRequestTime"
+ "_TtC18AppleMediaServices13ShutdownState"
+ "_configureAccountIdentifierForEvent:andActiveAccount:"
+ "_configureWatchDelegateAuthContentItemsForPaymentRequest:"
+ "_createURLSessionPromiseWith:"
+ "_delegatePurchaseRequest"
+ "_determineFlushStrategyWithDataSource:topic:urlSession:"
+ "_isShuttingDown"
+ "_pageRequestTime"
+ "_urlSessionPromiseWith:"
+ "delegatePurchaseRequest"
+ "disableAccountIdentifierAutoDecoration"
+ "purchase:willProcessResponse:"
+ "setDelegatePurchaseRequest:"
+ "setDisableAccountIdentifierAutoDecoration:"
+ "sigtermSource"
+ "v32@0:8@\"AMSPurchase\"16@\"NSDictionary\"24"
+ "\x81"
- "%{public}@ Generating plist formated updated request body"
- "_configureAccountIdentifierForEvent:"
- "_determineFlushStrategyWithDataSource:topic:"
- "_filterFormattedBlindedData:"
- "_urlSessionLock"

```
