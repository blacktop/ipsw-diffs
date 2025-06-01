## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

-308.80.4.0.0
-  __TEXT.__text: 0x73e6c
+316.100.13.0.0
+  __TEXT.__text: 0x74600
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x5464
-  __TEXT.__cstring: 0x4e1b
-  __TEXT.__oslogstring: 0xe843
-  __TEXT.__gcc_except_tab: 0xb48
-  __TEXT.__const: 0x158
+  __TEXT.__objc_methlist: 0x547c
+  __TEXT.__cstring: 0x4ece
+  __TEXT.__oslogstring: 0xe8bb
+  __TEXT.__gcc_except_tab: 0xb60
+  __TEXT.__const: 0x160
   __TEXT.__ustring: 0x8
-  __TEXT.diag_actions: 0x4706
-  __TEXT.__unwind_info: 0x1478
+  __TEXT.diag_actions: 0x4925
+  __TEXT.__unwind_info: 0x1494
   __TEXT.__objc_classname: 0x926
-  __TEXT.__objc_methname: 0xdf2f
-  __TEXT.__objc_methtype: 0x1f15
-  __TEXT.__objc_stubs: 0x9e40
+  __TEXT.__objc_methname: 0xdfff
+  __TEXT.__objc_methtype: 0x1f33
+  __TEXT.__objc_stubs: 0x9ea0
   __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x2510
+  __DATA_CONST.__const: 0x2700
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xaba8
-  __DATA_CONST.__objc_selrefs: 0x32f8
-  __DATA_CONST.__objc_arraydata: 0x5c0
+  __DATA_CONST.__objc_selrefs: 0x3310
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x3a0
+  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_arraydata: 0x608
   __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x66c0
+  __AUTH_CONST.__cfstring: 0x6760
   __AUTH_CONST.__objc_const: 0x1c50
   __AUTH_CONST.__objc_dictobj: 0x4d8
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x408
+  __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x790
   __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x3a0
-  __DATA.__objc_superrefs: 0x1d8
   __DATA.__objc_ivar: 0x664
-  __DATA.__data: 0xb18
+  __DATA.__data: 0xb28
   __DATA.__bss: 0x1f8
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x138

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C5D2E47A-95F8-3884-BF39-193CAF4930C6
-  Functions: 2119
-  Symbols:   7803
-  CStrings:  5713
+  UUID: 630EB113-9253-372C-A83E-80AFBBF5C78D
+  Functions: 2125
+  Symbols:   7830
+  CStrings:  5734
 
Symbols:
+ -[DiagnosticCaseManager _predicatesForCasesMatchingDomain:type:subtype:process:withinLast:]
+ -[DiagnosticCaseManager countOfCasesMatchingDomain:type:subtype:process:groupCaseIDIsPresent:withinLast:reply:]
+ -[DiagnosticsServiceImpl _checkRateLimitForConnection:signature:reply:]
+ GCC_except_table151
+ ___103-[DiagCollectionClient collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.73
+ ___103-[DiagCollectionClient collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.78
+ ___103-[DiagCollectionClient collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.83
+ ___103-[DiagCollectionClient collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke_2.79
+ ___103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.716
+ ___103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.717
+ ___106-[DiagnosticsServiceImpl startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.148
+ ___106-[DiagnosticsServiceImpl startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.149
+ ___111-[DiagnosticCaseManager countOfCasesMatchingDomain:type:subtype:process:groupCaseIDIsPresent:withinLast:reply:]_block_invoke
+ ___41-[DiagCollectionClient setupXPCInterface]_block_invoke.63
+ ___49-[DiagnosticCaseManager isAdmissible:dampenedBy:]_block_invoke.647
+ ___53-[DiagnosticCaseManager payloadsForSignatures:reply:]_block_invoke.731
+ ___55-[CloudKitUploadController registerLogUploadActivities]_block_invoke.245
+ ___55-[DiagnosticCaseManager _updateCaseStatisticsWithCase:]_block_invoke.656
+ ___57-[CloudKitUploadController registerCaseSummaryActivities]_block_invoke.248
+ ___57-[CloudKitUploadController submitCaseSummaries:activity:]_block_invoke.242
+ ___60-[DiagnosticsServiceImpl addToSession:events:payload:reply:]_block_invoke.153
+ ___63-[DiagCollectionClient moveDiagnosticFilesToDestination:reply:]_block_invoke.69
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.696
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.698
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.706
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.710
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.712
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.707
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.711
+ ___68-[CloudKitUploadController filterCasesPendingUpload:activity:reply:]_block_invoke.84
+ ___68-[CloudKitUploadController filterCasesPendingUpload:activity:reply:]_block_invoke.86
+ ___68-[CloudKitUploadController filterCasesPendingUpload:activity:reply:]_block_invoke.93
+ ___70-[DiagnosticCaseManager requestGroupCaseIdentifierForSignature:reply:]_block_invoke.648
+ ___71-[DiagnosticsServiceImpl _checkRateLimitForConnection:signature:reply:]_block_invoke
+ ___71-[DiagnosticsServiceImpl _checkRateLimitForConnection:signature:reply:]_block_invoke.124
+ ___71-[DiagnosticsServiceImpl requestGroupCaseIdentifierForSignature:reply:]_block_invoke.156
+ ___71-[DiagnosticsServiceImpl requestGroupCaseIdentifierForSignature:reply:]_block_invoke.157
+ ___74-[DiagnosticsServiceImpl addSignatureContentForSession:key:content:reply:]_block_invoke.155
+ ___81-[DiagnosticsServiceImpl triggerRemoteSessionForSignature:groupIdentifier:reply:]_block_invoke.163
+ ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.674
+ ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.675
+ ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.678
+ ___89-[TCPDumpProbe startTCPDumpWithDuration:destinationPath:tcpDumpStarted:tcpDumpCompleted:]_block_invoke.190
+ ___96-[CloudKitUploadController operationCompletedWithID:savedRecords:deletedRecords:error:activity:]_block_invoke.178
+ ___99-[DiagnosticsServiceImpl snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.140
+ ___99-[DiagnosticsServiceImpl snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.144
+ ___block_descriptor_40_e8_32bs_e8_v16?0q8ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72bs_e8_v12?0B8ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72bs80r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r80l8s72l8
+ ___block_literal_global.65
+ ___block_literal_global.715
+ __checkRateLimitForConnection:signature:reply:.lastCleanedAt
+ __unnamed_array_storage.178
+ __unnamed_array_storage.184
+ __unnamed_array_storage.185
+ __unnamed_array_storage.224
+ __unnamed_array_storage.494
+ __unnamed_array_storage.500
+ __unnamed_array_storage.506
+ __unnamed_array_storage.510
+ __unnamed_array_storage.514
+ __unnamed_array_storage.523
+ __unnamed_array_storage.526
+ __unnamed_array_storage.527
+ __unnamed_array_storage.530
+ __unnamed_array_storage.531
+ _kNetDiagOptPcapBufferSize
+ _kSymptomDiagnosticErrorInvalidSignature
+ _objc_msgSend$_checkRateLimitForConnection:signature:reply:
+ _objc_msgSend$_predicatesForCasesMatchingDomain:type:subtype:process:withinLast:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$countOfCasesMatchingDomain:type:subtype:process:groupCaseIDIsPresent:withinLast:reply:
- -[DiagnosticsServiceImpl _checkRateLimitForConnection:]
- ___103-[DiagCollectionClient collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.72
- ___103-[DiagCollectionClient collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.74
- ___103-[DiagCollectionClient collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.81
- ___103-[DiagCollectionClient collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke_2.78
- ___103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.698
- ___103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.699
- ___106-[DiagnosticsServiceImpl startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.142
- ___41-[DiagCollectionClient setupXPCInterface]_block_invoke.62
- ___49-[DiagnosticCaseManager isAdmissible:dampenedBy:]_block_invoke.629
- ___53-[DiagnosticCaseManager payloadsForSignatures:reply:]_block_invoke.713
- ___55-[CloudKitUploadController registerLogUploadActivities]_block_invoke.244
- ___55-[DiagnosticCaseManager _updateCaseStatisticsWithCase:]_block_invoke.638
- ___55-[DiagnosticsServiceImpl _checkRateLimitForConnection:]_block_invoke
- ___57-[CloudKitUploadController registerCaseSummaryActivities]_block_invoke.247
- ___57-[CloudKitUploadController submitCaseSummaries:activity:]_block_invoke.241
- ___60-[DiagnosticsServiceImpl addToSession:events:payload:reply:]_block_invoke.146
- ___63-[DiagCollectionClient moveDiagnosticFilesToDestination:reply:]_block_invoke.68
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.678
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.680
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.688
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.692
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.694
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.689
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.693
- ___68-[CloudKitUploadController filterCasesPendingUpload:activity:reply:]_block_invoke.83
- ___68-[CloudKitUploadController filterCasesPendingUpload:activity:reply:]_block_invoke.85
- ___68-[CloudKitUploadController filterCasesPendingUpload:activity:reply:]_block_invoke.92
- ___70-[DiagnosticCaseManager requestGroupCaseIdentifierForSignature:reply:]_block_invoke.630
- ___71-[DiagnosticsServiceImpl requestGroupCaseIdentifierForSignature:reply:]_block_invoke.149
- ___74-[DiagnosticsServiceImpl addSignatureContentForSession:key:content:reply:]_block_invoke.148
- ___81-[DiagnosticsServiceImpl triggerRemoteSessionForSignature:groupIdentifier:reply:]_block_invoke.155
- ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.656
- ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.657
- ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.660
- ___89-[TCPDumpProbe startTCPDumpWithDuration:destinationPath:tcpDumpStarted:tcpDumpCompleted:]_block_invoke.189
- ___96-[CloudKitUploadController operationCompletedWithID:savedRecords:deletedRecords:error:activity:]_block_invoke.177
- ___99-[DiagnosticsServiceImpl snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.139
- ___block_literal_global.64
- ___block_literal_global.697
- __checkRateLimitForConnection:.lastCleanedAt
- __unnamed_array_storage.170
- __unnamed_array_storage.223
- __unnamed_array_storage.491
- __unnamed_array_storage.492
- __unnamed_array_storage.495
- __unnamed_array_storage.496
- __unnamed_array_storage.505
- __unnamed_array_storage.508
- __unnamed_array_storage.512
- _objc_msgSend$_checkRateLimitForConnection:
CStrings:
+ " Not"
+ "%K != NULL"
+ "API was called with an invalid signature (signature fields exceed length limits)"
+ "Adding predicate for caseGroupID being non-NULL"
+ "Bad API usage"
+ "Component Crash"
+ "DiagnosticsService: API rate limit check for client: %d signature:%@"
+ "DiagnosticsService:%s overriding rate limit for group case"
+ "QRAllocbindTimeout"
+ "T@\"NSString\",?,R,C"
+ "_checkRateLimitForConnection:signature:reply:"
+ "_predicatesForCasesMatchingDomain:type:subtype:process:withinLast:"
+ "arrayByAddingObject:"
+ "countOfCasesMatchingDomain:type:subtype:process:groupCaseIDIsPresent:withinLast:reply:"
+ "pcapbuffersize"
+ "v12@?0B8"
+ "v16@?0q8"
+ "v68@0:8@16@24@32@40B48d52@?60"
- "DiagnosticsService: API rate limit check for client: %d"
- "_checkRateLimitForConnection:"

```
