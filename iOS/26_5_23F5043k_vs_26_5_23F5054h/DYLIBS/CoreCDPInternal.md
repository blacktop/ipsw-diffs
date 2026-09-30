## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-416.575.3.0.0
-  __TEXT.__text: 0x95f3c
+416.575.6.0.0
+  __TEXT.__text: 0x96260
   __TEXT.__auth_stubs: 0x1160
   __TEXT.__objc_methlist: 0x565c
   __TEXT.__const: 0x830
-  __TEXT.__oslogstring: 0x1480e
-  __TEXT.__cstring: 0xd625
+  __TEXT.__oslogstring: 0x1481e
+  __TEXT.__cstring: 0xd6e5
   __TEXT.__gcc_except_tab: 0xc70
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x385

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__unwind_info: 0x1f68
-  __TEXT.__eh_frame: 0x930
+  __TEXT.__eh_frame: 0x958
   __TEXT.__objc_classname: 0xdbd
-  __TEXT.__objc_methname: 0xfa5f
+  __TEXT.__objc_methname: 0xfa8f
   __TEXT.__objc_methtype: 0x2aa7
-  __TEXT.__objc_stubs: 0xcc80
-  __DATA_CONST.__got: 0x1090
+  __TEXT.__objc_stubs: 0xcce0
+  __DATA_CONST.__got: 0x10b8
   __DATA_CONST.__const: 0x2598
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38c0
+  __DATA_CONST.__objc_selrefs: 0x38d8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0x8c0
   __AUTH_CONST.__const: 0xab0
-  __AUTH_CONST.__cfstring: 0x8da0
+  __AUTH_CONST.__cfstring: 0x8e20
   __AUTH_CONST.__objc_const: 0x100b0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 106B9AE0-B406-3AFF-A154-B8DB55DB1334
-  Functions: 3150
-  Symbols:   10396
-  CStrings:  6495
+  UUID: 1FBB6B53-E3E0-3C55-A31A-B232BA8BD87E
+  Functions: 3151
+  Symbols:   10400
+  CStrings:  6506
 
Symbols:
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2195
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2195.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2196
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2196.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2259
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2259.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2259.cold.2
+ ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.83
+ ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.55
+ ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.55.cold.1
+ ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.55.cold.2
+ ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.80
+ ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke.72
+ ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke_2.73
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2260
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2262
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2262.cold.1
+ ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.84
+ ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.75
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.85
+ ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.85.cold.1
+ ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.59
+ ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.61
+ ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.81
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.86
+ ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.86.cold.1
+ ___block_literal_global.1058
+ ___block_literal_global.1069
+ ___block_literal_global.1173
+ ___block_literal_global.1220
+ ___block_literal_global.1255
+ ___block_literal_global.1332
+ ___block_literal_global.1361
+ ___block_literal_global.2176
+ ___block_literal_global.2192
+ ___block_literal_global.2264
+ _kCDPAnalyticsADPHealingPCSEvent
+ _kCDPAnalyticsPDPBlobGenerationEvent
+ _kCDPAnalyticsPDPBlobGenerationStartEvent
+ _kCDPAnalyticsPDPHealth
+ _kCDPAnalyticsPDPState
+ _objc_msgSend$applyTelemetryFromCDPContext:
+ _objc_msgSend$isActivePDPState
+ _objc_msgSend$setPdpHealth:
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2183
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2183.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2184
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2184.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2247
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2247.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2247.cold.2
- ___65-[CDPDClientHandler attemptToEscrowPreRecord:context:completion:]_block_invoke.82
- ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.52
- ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.52.cold.1
- ___73-[CDPDClientHandler deviceEscrowRecordRecoverableWithContext:completion:]_block_invoke.52.cold.2
- ___73-[CDPDClientHandler shouldPerformRepairForContext:forceFetch:completion:]_block_invoke.79
- ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke.69
- ___80-[CDPDClientHandler startCircleApplicationApprovalServerWithContext:completion:]_block_invoke_2.70
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2248
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2250
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2250.cold.1
- ___83-[CDPDClientHandler localSecretChangedTo:secretType:context:uiProvider:completion:]_block_invoke.83
- ___85-[CDPDClientHandler _startObservingConnectionStateForRepairWithStateMachine:context:]_block_invoke.74
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.84
- ___85-[CDPDClientHandler finishOfflineLocalSecretChangeWithContext:uiProvider:completion:]_block_invoke.84.cold.1
- ___85-[CDPDClientHandler handleCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.56
- ___85-[CDPDClientHandler repairCloudDataProtectionStateWithContext:uiProvider:completion:]_block_invoke.58
- ___86-[CDPDClientHandler shouldPerformAuthenticatedRepairForContext:forceFetch:completion:]_block_invoke.80
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.85
- ___89-[CDPDClientHandler finishCyrusFlowAfterTermsAgreementWithContext:uiProvider:completion:]_block_invoke.85.cold.1
- ___block_literal_global.1046
- ___block_literal_global.1057
- ___block_literal_global.1161
- ___block_literal_global.1208
- ___block_literal_global.1243
- ___block_literal_global.1320
- ___block_literal_global.1349
- ___block_literal_global.2152
- ___block_literal_global.2180
- ___block_literal_global.2252
CStrings:
+ "CDPDStateMachine: PDP intermission eligibility check passed (state: %lu)"
+ "applyTelemetryFromCDPContext:"
+ "com.apple.appleaccount.cdpHealthCheckFinish"
+ "com.apple.appleaccount.cdpHealthCheckStart"
+ "com.apple.appleaccount.pdpHealthCheckFinish"
+ "com.apple.appleaccount.pdpHealthCheckStart"
+ "com.apple.security.escrowRepairGenerateRecordPasscodeChanged"
+ "com.apple.security.escrowRepairGenerateRecordPasscodeUnlocked"
+ "isActivePDPState"
+ "setPdpHealth:"
- "CDPDStateMachine: PDP intermission eligibility check passed"
- "com.apple.security.escrowRepairOperationPasscodeChanged"
- "com.apple.security.escrowRepairOperationPasscodeUnlocked"

```
