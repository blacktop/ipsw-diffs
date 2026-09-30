## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-406.0.0.0.0
-  __TEXT.__text: 0x91dec
-  __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x5514
+409.0.0.0.0
+  __TEXT.__text: 0x922d4
+  __TEXT.__auth_stubs: 0x1110
+  __TEXT.__objc_methlist: 0x552c
   __TEXT.__const: 0x8c4
   __TEXT.__oslogstring: 0x14066
-  __TEXT.__cstring: 0xcd6e
-  __TEXT.__gcc_except_tab: 0xc78
+  __TEXT.__cstring: 0xcdfe
+  __TEXT.__gcc_except_tab: 0xc84
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x341
   __TEXT.__swift5_fieldmd: 0x98

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x24
-  __TEXT.__swift5_capture: 0x1b8
+  __TEXT.__swift5_capture: 0x1c8
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x60
   __TEXT.__unwind_info: 0x1d48
   __TEXT.__eh_frame: 0x8d0
   __TEXT.__objc_classname: 0xcbd
-  __TEXT.__objc_methname: 0xf24d
+  __TEXT.__objc_methname: 0xf2b6
   __TEXT.__objc_methtype: 0x2987
-  __TEXT.__objc_stubs: 0xc480
-  __DATA_CONST.__got: 0x1068
+  __TEXT.__objc_stubs: 0xc4c0
+  __DATA_CONST.__got: 0x1090
   __DATA_CONST.__const: 0x2630
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3760
+  __DATA_CONST.__objc_selrefs: 0x3770
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x890
-  __AUTH_CONST.__const: 0xba0
-  __AUTH_CONST.__cfstring: 0x8220
+  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__const: 0xbc8
+  __AUTH_CONST.__cfstring: 0x8280
   __AUTH_CONST.__objc_const: 0xfc90
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 73656D29-CC01-396D-A658-24ECB97DC889
-  Functions: 3107
-  Symbols:   10050
-  CStrings:  6256
+  UUID: AAFB9023-E95B-3560-B042-15195567BE9F
+  Functions: 3111
+  Symbols:   10061
+  CStrings:  6264
 
Symbols:
+ -[CDPDOctagonTrustProxyImpl _retryableFetchAllEscrowRecordWithContext:completion:]
+ -[CDPDOctagonTrustProxyImpl _retryableFetchEscrowRecordWithContext:completion:]
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1915
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1915.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1916
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1916.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1979
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1979.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1979.cold.2
+ ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.96
+ ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.93
+ ___79-[CDPDCircleController _joinCircleFallbackWithResult:ignoreBackups:completion:]_block_invoke.57
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.1980
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1982
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1982.cold.1
+ ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.97
+ ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.88
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.98
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.98.cold.1
+ ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.94
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.99
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.99.cold.1
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e45_v24?0"OTEscrowCheckCallResult"8"NSError"16lr56l8s32l8s40l8r64l8s48l8
+ ___block_literal_global.1052
+ ___block_literal_global.1081
+ ___block_literal_global.1884
+ ___block_literal_global.1896
+ ___block_literal_global.1912
+ ___block_literal_global.1984
+ ___block_literal_global.496
+ ___block_literal_global.813
+ ___block_literal_global.824
+ ___block_literal_global.925
+ ___block_literal_global.972
+ _block_copy_helper.100
+ _block_copy_helper.111
+ _block_copy_helper.90
+ _block_descriptor.102
+ _block_descriptor.113
+ _block_descriptor.92
+ _block_destroy_helper.101
+ _block_destroy_helper.112
+ _block_destroy_helper.91
+ _kAAAnalyticsRecordViabilityState
+ _kCDPAnalyticsCdpdConnectionInvalidated
+ _kCDPAnalyticsCliqueCreationStart
+ _kCDPAnalyticsEscrowCheckEvent
+ _kCDPAnalyticsFetchEscrowRecordsStartEvent
+ _objc_msgSend$_retryableFetchAllEscrowRecordWithContext:completion:
+ _objc_msgSend$_retryableFetchEscrowRecordWithContext:completion:
+ _objectdestroy.33Tm
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1906
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1906.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1907
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1907.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1970
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1970.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.1970.cold.2
- ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.94
- ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.91
- ___79-[CDPDCircleController _joinCircleFallbackWithResult:ignoreBackups:completion:]_block_invoke.56
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.1971
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1973
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.1973.cold.1
- ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.95
- ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.86
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.96
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.96.cold.1
- ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.92
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.97
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.97.cold.1
- ___block_descriptor_64_e8_32s40bs48r56r_e45_v24?0"OTEscrowCheckCallResult"8"NSError"16lr48l8s32l8r56l8s40l8
- ___block_literal_global.1043
- ___block_literal_global.1072
- ___block_literal_global.1875
- ___block_literal_global.1887
- ___block_literal_global.1903
- ___block_literal_global.1975
- ___block_literal_global.487
- ___block_literal_global.804
- ___block_literal_global.815
- ___block_literal_global.916
- ___block_literal_global.963
- _block_copy_helper.106
- _block_copy_helper.85
- _block_copy_helper.95
- _block_descriptor.108
- _block_descriptor.87
- _block_descriptor.97
- _block_destroy_helper.107
- _block_destroy_helper.86
- _block_destroy_helper.96
- _objectdestroy.28Tm
CStrings:
+ "_retryableFetchAllEscrowRecordWithContext:completion:"
+ "_retryableFetchEscrowRecordWithContext:completion:"
+ "com.apple.security.escrowPasscodeCacheAvailable"
+ "com.apple.security.escrowPasscodeEnableCacheFlow"
+ "com.apple.security.escrowRepairOperation"

```
