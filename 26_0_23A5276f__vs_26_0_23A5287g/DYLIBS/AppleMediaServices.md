## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.0.61.0.0
-  __TEXT.__text: 0x76db7c
+9.0.67.0.0
+  __TEXT.__text: 0x76dd58
   __TEXT.__auth_stubs: 0x48f0
-  __TEXT.__objc_methlist: 0x219ec
-  __TEXT.__const: 0x5c538
+  __TEXT.__objc_methlist: 0x21b04
+  __TEXT.__const: 0x5c578
   __TEXT.__dlopen_cstrs: 0x937
-  __TEXT.__cstring: 0x2a2ce
-  __TEXT.__swift5_typeref: 0x5a65
-  __TEXT.__swift5_reflstr: 0x30e4
+  __TEXT.__cstring: 0x2a4ee
+  __TEXT.__swift5_typeref: 0x5a6b
+  __TEXT.__swift5_reflstr: 0x3104
   __TEXT.__swift5_assocty: 0xe88
-  __TEXT.__constg_swiftt: 0x46d8
+  __TEXT.__constg_swiftt: 0x4714
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_fieldmd: 0x3f2c
+  __TEXT.__swift5_fieldmd: 0x3f48
   __TEXT.__swift5_proto: 0xe60
-  __TEXT.__swift5_types: 0x520
+  __TEXT.__swift5_types: 0x524
   __TEXT.__swift_as_entry: 0x628
   __TEXT.__swift_as_ret: 0x748
-  __TEXT.__swift5_capture: 0x2c00
+  __TEXT.__swift5_capture: 0x2c50
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0xb8
-  __TEXT.__oslogstring: 0x2eb8d
-  __TEXT.__gcc_except_tab: 0x5c08
+  __TEXT.__oslogstring: 0x2eb6a
+  __TEXT.__gcc_except_tab: 0x5bc8
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0xf8e8
-  __TEXT.__eh_frame: 0x1236c
+  __TEXT.__unwind_info: 0x101a8
+  __TEXT.__eh_frame: 0x12454
   __TEXT.__objc_classname: 0x3ee0
-  __TEXT.__objc_methname: 0x430c5
-  __TEXT.__objc_methtype: 0x77cd
-  __TEXT.__objc_stubs: 0x2dae0
-  __DATA_CONST.__got: 0x19a8
+  __TEXT.__objc_methname: 0x4321a
+  __TEXT.__objc_methtype: 0x77fe
+  __TEXT.__objc_stubs: 0x2db80
+  __DATA_CONST.__got: 0x19a0
   __DATA_CONST.__const: 0xbf40
-  __DATA_CONST.__objc_classlist: 0x13d8
+  __DATA_CONST.__objc_classlist: 0x13e0
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec10
+  __DATA_CONST.__objc_selrefs: 0xec40
   __DATA_CONST.__objc_protorefs: 0x200
   __DATA_CONST.__objc_superrefs: 0xc90
   __DATA_CONST.__objc_arraydata: 0x508
   __AUTH_CONST.__auth_got: 0x2490
-  __AUTH_CONST.__const: 0x2b668
-  __AUTH_CONST.__cfstring: 0x215e0
-  __AUTH_CONST.__objc_const: 0x3aae0
+  __AUTH_CONST.__const: 0x2ba28
+  __AUTH_CONST.__cfstring: 0x21740
+  __AUTH_CONST.__objc_const: 0x3aca0
   __AUTH_CONST.__objc_intobj: 0xc48
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x8c20
-  __AUTH.__data: 0x1da0
-  __DATA.__objc_ivar: 0x184c
-  __DATA.__data: 0x6990
+  __AUTH.__objc_data: 0x8ce0
+  __AUTH.__data: 0x1de0
+  __DATA.__objc_ivar: 0x1860
+  __DATA.__data: 0x69f0
   __DATA.__bss: 0x17e79
-  __DATA.__common: 0xb68
+  __DATA.__common: 0xb18
   __DATA_DIRTY.__objc_ivar: 0x6b4
   __DATA_DIRTY.__objc_data: 0x5968
-  __DATA_DIRTY.__data: 0x1f48
+  __DATA_DIRTY.__data: 0x1f58
   __DATA_DIRTY.__bss: 0x3840
   __DATA_DIRTY.__common: 0x78
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6C3F0C86-794D-373F-B867-C439E1E4F0DD
-  Functions: 24169
-  Symbols:   49877
-  CStrings:  24828
+  UUID: 5A96913B-A12B-3FE0-A0B6-899C728176B1
+  Functions: 24221
+  Symbols:   49975
+  CStrings:  24867
 
Symbols:
+ +[AMSEngagementAppEventFilterModel _safeValueForKeyPath:inObject:]
+ +[AMSEngagementAppEventFilterModel _valuesForCustomKeyPath:inObject:]
+ +[AMSHTTPArchiveMetrics supportsSecureCoding]
+ +[AMSHTTPArchiveTransactionMetrics supportsSecureCoding]
+ -[AMSEngagementRequest mediaClientIdentifier]
+ -[AMSEngagementRequest setMediaClientIdentifier:]
+ -[AMSHTTPArchiveMetrics encodeWithCoder:]
+ -[AMSHTTPArchiveMetrics initWithCoder:]
+ -[AMSHTTPArchiveTaskInfo taskMetrics]
+ -[AMSHTTPArchiveTransactionMetrics encodeWithCoder:]
+ -[AMSHTTPArchiveTransactionMetrics initWithCoder:]
+ -[AMSMetrics URLSession]
+ -[AMSMetricsFigaroFlushTask initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:maxBatchSizeOverride:urlSession:postBatchBlock:]
+ -[AMSMetricsFigaroFlushTask initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:urlSession:]
+ -[AMSPaymentSheetResult paymentMethodType]
+ -[AMSPaymentSheetResult setPaymentMethodType:]
+ -[_PaymentSheetState paymentMethodType]
+ -[_PaymentSheetState setPaymentMethodType:]
+ GCC_except_table51
+ GCC_except_table77
+ _OBJC_CLASS_$_AMSEmptyUsernameMigrator
+ _OBJC_IVAR_$_AMSEngagementRequest._mediaClientIdentifier
+ _OBJC_IVAR_$_AMSHTTPArchiveTaskInfo._taskMetrics
+ _OBJC_IVAR_$_AMSMetrics._URLSession
+ _OBJC_IVAR_$_AMSMetrics._urlSessionLock
+ _OBJC_IVAR_$_AMSPaymentSheetResult._paymentMethodType
+ _OBJC_IVAR_$__PaymentSheetState._paymentMethodType
+ _OBJC_METACLASS_$_AMSEmptyUsernameMigrator
+ __CLASS_METHODS_AMSEmptyUsernameMigrator
+ __DATA_AMSEmptyUsernameMigrator
+ __INSTANCE_METHODS_AMSEmptyUsernameMigrator
+ __IVARS__TtC18AppleMediaServicesP33_68239C40601534D7947471707625281632DeveloperSilentAuthTokenDelegate
+ __METACLASS_DATA_AMSEmptyUsernameMigrator
+ __OBJC_$_CLASS_METHODS_AMSHTTPArchiveMetrics
+ __OBJC_$_CLASS_METHODS_AMSHTTPArchiveTransactionMetrics
+ __OBJC_$_CLASS_PROP_LIST_AMSHTTPArchiveMetrics
+ __OBJC_$_CLASS_PROP_LIST_AMSHTTPArchiveTransactionMetrics
+ __OBJC_CLASS_PROTOCOLS_$_AMSHTTPArchiveMetrics
+ __OBJC_CLASS_PROTOCOLS_$_AMSHTTPArchiveTransactionMetrics
+ __PROTOCOLS__TtC18AppleMediaServicesP33_53E9BFD2965C81AFBEDE880E2C1BF3BA30AutoBugCaptureCallbackDelegate.45
+ __PROTOCOLS__TtC18AppleMediaServicesP33_53E9BFD2965C81AFBEDE880E2C1BF3BA42AutoBugCaptureReporterContinuationDelegate.39
+ ___162-[AMSMetricsFigaroFlushTask initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:urlSession:]_block_invoke
+ ___24-[AMSMetrics URLSession]_block_invoke
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke.87
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke.92
+ ___36-[AMSMetrics _processOperationQueue]_block_invoke_2.88
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.156
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.157
+ ___40-[AMSMetricsFigaroFlushTask _postBatch:]_block_invoke.128
+ ___44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.99
+ ___44-[AMSPaymentSheetTask _performInProcessTask]_block_invoke.223
+ ___44-[AMSPaymentSheetTask _performInProcessTask]_block_invoke.233
+ ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.97
+ ___56-[AMSMetricsFigaroFlushTask _nextBatchWithConfig:topic:]_block_invoke.103
+ ___56-[AMSMetricsFigaroFlushTask _nextBatchWithConfig:topic:]_block_invoke.94
+ ___59-[AMSPaymentSheetTask _configurePSD2Decoration:completion:]_block_invoke.269
+ ___62-[AMSPaymentSheetTask _dismissPaymentAuthorizationController:]_block_invoke.285
+ ___62-[AMSPaymentSheetTask _dismissPaymentAuthorizationController:]_block_invoke.288
+ ___82-[AMSPaymentSheetTask paymentAuthorizationController:didAuthorizePayment:handler:]_block_invoke.308
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.115
+ ___block_literal_global.176
+ ___block_literal_global.181
+ ___block_literal_global.77
+ _block_copy_helper.125
+ _block_copy_helper.143
+ _block_copy_helper.170
+ _block_copy_helper.51
+ _block_descriptor.127
+ _block_descriptor.145
+ _block_descriptor.172
+ _block_descriptor.53
+ _block_destroy_helper.126
+ _block_destroy_helper.144
+ _block_destroy_helper.171
+ _block_destroy_helper.52
+ _objc_msgSend$_safeValueForKeyPath:inObject:
+ _objc_msgSend$_valuesForCustomKeyPath:inObject:
+ _objc_msgSend$engagement:didUpdateRequest:presentationAction:placement:serviceType:
+ _objc_msgSend$initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:maxBatchSizeOverride:urlSession:postBatchBlock:
+ _objc_msgSend$initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:urlSession:
+ _objc_msgSend$mediaClientIdentifier
+ _objc_msgSend$migrateEmptyUsernames
+ _symbolic _____ 18AppleMediaServices21EmptyUsernameMigratorC
- -[AMSMetricsFigaroFlushTask initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:]
- -[AMSMetricsFigaroFlushTask initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:maxBatchSizeOverride:postBatchBlock:]
- GCC_except_table68
- _OBJC_CLASS_$_NSURLSessionTaskMetrics
- _OBJC_IVAR_$_AMSHTTPArchiveTaskInfo._metrics
- __PROTOCOLS__TtC18AppleMediaServicesP33_53E9BFD2965C81AFBEDE880E2C1BF3BA30AutoBugCaptureCallbackDelegate.41
- __PROTOCOLS__TtC18AppleMediaServicesP33_53E9BFD2965C81AFBEDE880E2C1BF3BA42AutoBugCaptureReporterContinuationDelegate.35
- ___151-[AMSMetricsFigaroFlushTask initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:]_block_invoke
- ___36-[AMSMetrics _processOperationQueue]_block_invoke.85
- ___36-[AMSMetrics _processOperationQueue]_block_invoke.90
- ___36-[AMSMetrics _processOperationQueue]_block_invoke_2.86
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.154
- ___40-[AMSMetricsFigaroFlushTask _postBatch:]_block_invoke.131
- ___44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.97
- ___44-[AMSPaymentSheetTask _performInProcessTask]_block_invoke.217
- ___44-[AMSPaymentSheetTask _performInProcessTask]_block_invoke.227
- ___50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.93
- ___56-[AMSMetricsFigaroFlushTask _nextBatchWithConfig:topic:]_block_invoke.106
- ___56-[AMSMetricsFigaroFlushTask _nextBatchWithConfig:topic:]_block_invoke.97
- ___59-[AMSPaymentSheetTask _configurePSD2Decoration:completion:]_block_invoke.263
- ___62-[AMSPaymentSheetTask _dismissPaymentAuthorizationController:]_block_invoke.279
- ___62-[AMSPaymentSheetTask _dismissPaymentAuthorizationController:]_block_invoke.282
- ___66+[AMSEngagementAppEventFilterModel matchEvent:toFilter:withCache:]_block_invoke
- ___82-[AMSPaymentSheetTask paymentAuthorizationController:didAuthorizePayment:handler:]_block_invoke.302
- ___block_descriptor_64_e8_32s40s48r_e25_v32?0"NSString"816^B24ls32l8s40l8r48l8
- ___block_literal_global.109
- ___block_literal_global.113
- ___block_literal_global.167
- ___block_literal_global.75
- _block_copy_helper.121
- _block_copy_helper.139
- _block_copy_helper.166
- _block_descriptor.123
- _block_descriptor.141
- _block_descriptor.168
- _block_destroy_helper.122
- _block_destroy_helper.140
- _block_destroy_helper.167
- _objc_msgSend$initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:
- _objc_msgSend$initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:maxBatchSizeOverride:postBatchBlock:
CStrings:
+ "@\"AMSHTTPArchiveMetrics\""
+ "@76@0:8@\"<AMSMetricsDataSource>\"16@\"<AMSBagProtocol>\"24Q32Q40@\"NSString\"48B56Q60@\"AMSURLSession\"68"
+ "@76@0:8@16@24Q32Q40@48B56Q60@68"
+ "@92@0:8@16@24Q32Q40@48B56Q60@68@76@?84"
+ "AMSEmptyUsernameMigrator"
+ "AppleMediaServices.DeveloperSilentAuthTokenDelegate"
+ "AutoBugCaptureReport.SendSnapshotFromXPC"
+ "Could not find iCloud account for iTunes account:"
+ "Error fetching iTunes accounts:"
+ "Failed to create diagnostic reporter with queue:"
+ "Malformed key path with unclosed bracket: %{public}@"
+ "T@\"AMSHTTPArchiveMetrics\",R,N,V_taskMetrics"
+ "T@\"NSString\",&,N,V_mediaClientIdentifier"
+ "T@\"NSURLSessionTaskMetrics\",R,N"
+ "["
+ "_mediaClientIdentifier"
+ "_safeValueForKeyPath:inObject:"
+ "_urlSessionLock"
+ "_valuesForCustomKeyPath:inObject:"
+ "engagement:didUpdateRequest:presentationAction:placement:serviceType:"
+ "initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:maxBatchSizeOverride:urlSession:postBatchBlock:"
+ "initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:urlSession:"
+ "kCodingKeyApsRelayAttempted"
+ "kCodingKeyApsRelaySucceeded"
+ "kCodingKeyFetchStartDate"
+ "kCodingKeyRequestStartDate"
+ "kCodingKeyResourceFetchType"
+ "kCodingKeyResponse"
+ "kCodingKeyResponseEndDate"
+ "kCodingKeyTaskMetrics"
+ "kCodingKeyTransactionMetrics"
+ "mediaClientIdentifier"
+ "migrateEmptyUsernames"
+ "setMediaClientIdentifier:"
- "%{public}@ [%{public}@]: Event is not key value coding-compliant for the key %{public}@"
- "@68@0:8@\"<AMSMetricsDataSource>\"16@\"<AMSBagProtocol>\"24Q32Q40@\"NSString\"48B56Q60"
- "@68@0:8@16@24Q32Q40@48B56Q60"
- "@84@0:8@16@24Q32Q40@48B56Q60@68@?76"
- "T@\"NSURLSessionTaskMetrics\",R,N,V_metrics"
- "initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:"
- "initWithDataSource:bag:maxRequestCount:maxEventsPerBatch:topic:includeMMeClientInfoAndDeviceHeaders:metricsSigningFlavour:maxBatchSizeOverride:postBatchBlock:"

```
