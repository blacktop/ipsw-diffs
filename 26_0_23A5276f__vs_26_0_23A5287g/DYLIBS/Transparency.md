## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1547.0.12.0.0
-  __TEXT.__text: 0x4882c
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x3f00
-  __TEXT.__cstring: 0x26be
+1547.0.24.0.0
+  __TEXT.__text: 0x49970
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_methlist: 0x4134
+  __TEXT.__cstring: 0x26fe
   __TEXT.__const: 0x11b0
   __TEXT.__gcc_except_tab: 0x508
   __TEXT.__oslogstring: 0x1b91

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1908
+  __TEXT.__unwind_info: 0x1958
   __TEXT.__eh_frame: 0x4d0
-  __TEXT.__objc_classname: 0x698
-  __TEXT.__objc_methname: 0x6eb4
-  __TEXT.__objc_methtype: 0x1dd7
-  __TEXT.__objc_stubs: 0x5460
+  __TEXT.__objc_classname: 0x6e3
+  __TEXT.__objc_methname: 0x7105
+  __TEXT.__objc_methtype: 0x1e25
+  __TEXT.__objc_stubs: 0x5660
   __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x1518
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __DATA_CONST.__const: 0x1520
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c28
+  __DATA_CONST.__objc_selrefs: 0x1cd0
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x150
-  __AUTH_CONST.__auth_got: 0x700
-  __AUTH_CONST.__const: 0x27a0
-  __AUTH_CONST.__cfstring: 0x3660
-  __AUTH_CONST.__objc_const: 0x6ae0
+  __DATA_CONST.__objc_superrefs: 0x168
+  __AUTH_CONST.__auth_got: 0x708
+  __AUTH_CONST.__const: 0x27c0
+  __AUTH_CONST.__cfstring: 0x36e0
+  __AUTH_CONST.__objc_const: 0x6f60
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH.__objc_data: 0x128
+  __AUTH.__objc_data: 0x218
   __AUTH.__data: 0x2f0
-  __DATA.__objc_ivar: 0x32c
-  __DATA.__data: 0x918
+  __DATA.__objc_ivar: 0x354
+  __DATA.__data: 0x978
   __DATA.__bss: 0x2350
   __DATA_DIRTY.__objc_data: 0x12b8
   __DATA_DIRTY.__data: 0x38

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 84B36B52-B410-3A65-8CC6-B3C1AEF09E66
-  Functions: 2383
-  Symbols:   6384
-  CStrings:  2624
+  UUID: 9B16A315-DB1B-38B1-830E-84BB6296422A
+  Functions: 2424
+  Symbols:   6528
+  CStrings:  2670
 
Symbols:
+ +[KTValidatePeersQuery supportsSecureCoding]
+ +[KTValidatePeersResponse supportsSecureCoding]
+ +[TransparencyAnalytics privacyURI:]
+ -[KTIDSData setTraceUUID:]
+ -[KTIDSData traceUUID]
+ -[KTURI .cxx_destruct]
+ -[KTURI initWithIDSURL:application:]
+ -[KTURI ktURIVRF]
+ -[KTURI ktURI]
+ -[KTURI redactedDescription]
+ -[KTURI setKtURI:]
+ -[KTURI setKtURIVRF:]
+ -[KTValidatePeersQuery .cxx_destruct]
+ -[KTValidatePeersQuery application]
+ -[KTValidatePeersQuery encodeWithCoder:]
+ -[KTValidatePeersQuery fetchNow]
+ -[KTValidatePeersQuery initWithApplication:peers:]
+ -[KTValidatePeersQuery initWithCoder:]
+ -[KTValidatePeersQuery setApplication:]
+ -[KTValidatePeersQuery setFetchNow:]
+ -[KTValidatePeersQuery setTraceUUID:]
+ -[KTValidatePeersQuery setUriToVerificationInfo:]
+ -[KTValidatePeersQuery traceUUID]
+ -[KTValidatePeersQuery uriToVerificationInfo]
+ -[KTValidatePeersResponse .cxx_destruct]
+ -[KTValidatePeersResponse application]
+ -[KTValidatePeersResponse encodeWithCoder:]
+ -[KTValidatePeersResponse initWithApplication:results:]
+ -[KTValidatePeersResponse initWithCoder:]
+ -[KTValidatePeersResponse results]
+ -[KTValidatePeersResponse setApplication:]
+ -[KTValidatePeersResponse setResults:]
+ -[KTValidatePeersResponse setTraceUUID:]
+ -[KTValidatePeersResponse traceUUID]
+ -[KTVerifier validatePeers:completionBlock:]
+ -[TransparencySettings clearKTSignaturePolicy]
+ -[TransparencySettings ktSignaturePolicy]
+ GCC_except_table154
+ GCC_except_table162
+ GCC_except_table167
+ GCC_except_table177
+ GCC_except_table187
+ GCC_except_table88
+ _CFPreferencesSetAppValue
+ _OBJC_CLASS_$_KTURI
+ _OBJC_CLASS_$_KTValidatePeersQuery
+ _OBJC_CLASS_$_KTValidatePeersResponse
+ _OBJC_IVAR_$_KTIDSData._traceUUID
+ _OBJC_IVAR_$_KTURI._ktURI
+ _OBJC_IVAR_$_KTURI._ktURIVRF
+ _OBJC_IVAR_$_KTValidatePeersQuery._application
+ _OBJC_IVAR_$_KTValidatePeersQuery._fetchNow
+ _OBJC_IVAR_$_KTValidatePeersQuery._traceUUID
+ _OBJC_IVAR_$_KTValidatePeersQuery._uriToVerificationInfo
+ _OBJC_IVAR_$_KTValidatePeersResponse._application
+ _OBJC_IVAR_$_KTValidatePeersResponse._results
+ _OBJC_IVAR_$_KTValidatePeersResponse._traceUUID
+ _OBJC_METACLASS_$_KTURI
+ _OBJC_METACLASS_$_KTValidatePeersQuery
+ _OBJC_METACLASS_$_KTValidatePeersResponse
+ __OBJC_$_CLASS_METHODS_KTValidatePeersQuery
+ __OBJC_$_CLASS_METHODS_KTValidatePeersResponse
+ __OBJC_$_CLASS_PROP_LIST_KTValidatePeersQuery
+ __OBJC_$_CLASS_PROP_LIST_KTValidatePeersResponse
+ __OBJC_$_INSTANCE_METHODS_KTURI
+ __OBJC_$_INSTANCE_METHODS_KTValidatePeersQuery
+ __OBJC_$_INSTANCE_METHODS_KTValidatePeersResponse
+ __OBJC_$_INSTANCE_VARIABLES_KTURI
+ __OBJC_$_INSTANCE_VARIABLES_KTValidatePeersQuery
+ __OBJC_$_INSTANCE_VARIABLES_KTValidatePeersResponse
+ __OBJC_$_PROP_LIST_KTRedactedDescription
+ __OBJC_$_PROP_LIST_KTURI
+ __OBJC_$_PROP_LIST_KTValidatePeersQuery
+ __OBJC_$_PROP_LIST_KTValidatePeersResponse
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_KTRedactedDescription
+ __OBJC_$_PROTOCOL_METHOD_TYPES_KTRedactedDescription
+ __OBJC_CLASS_PROTOCOLS_$_KTURI
+ __OBJC_CLASS_PROTOCOLS_$_KTValidatePeersQuery
+ __OBJC_CLASS_PROTOCOLS_$_KTValidatePeersResponse
+ __OBJC_CLASS_RO_$_KTURI
+ __OBJC_CLASS_RO_$_KTValidatePeersQuery
+ __OBJC_CLASS_RO_$_KTValidatePeersResponse
+ __OBJC_LABEL_PROTOCOL_$_KTRedactedDescription
+ __OBJC_METACLASS_RO_$_KTURI
+ __OBJC_METACLASS_RO_$_KTValidatePeersQuery
+ __OBJC_METACLASS_RO_$_KTValidatePeersResponse
+ __OBJC_PROTOCOL_$_KTRedactedDescription
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.449
+ ___35-[KTVerifier clearPeerCache:error:]_block_invoke.192
+ ___35-[KTVerifier clearPeerCache:error:]_block_invoke_2.193
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.521
+ ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.579
+ ___44-[KTVerifier ignoreFailureForResults:error:]_block_invoke.143
+ ___44-[KTVerifier ignoreFailureForResults:error:]_block_invoke_2.144
+ ___44-[KTVerifier validatePeers:completionBlock:]_block_invoke
+ ___44-[KTVerifier validatePeers:completionBlock:]_block_invoke.126
+ ___44-[KTVerifier validatePeers:completionBlock:]_block_invoke.cold.1
+ ___44-[KTVerifier validatePeers:completionBlock:]_block_invoke_2
+ ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.379
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.539
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.540
+ ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.418
+ ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.424
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.383
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.384
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.512
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.432
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.432.cold.1
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.435
+ ___46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.154
+ ___46-[KTVerifier markFailureSeenForResults:error:]_block_invoke.139
+ ___46-[KTVerifier markFailureSeenForResults:error:]_block_invoke_2.140
+ ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.387
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.495
+ ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.421
+ ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.546
+ ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.549
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.478
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.480
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.440
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.442
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.442.cold.1
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.452
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.391
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.397
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.393
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.408
+ ___51-[KTVerifier initiateQueryForUris:completionBlock:]_block_invoke.135
+ ___51-[KTVerifier initiateQueryForUris:completionBlock:]_block_invoke_2.136
+ ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.427
+ ___55-[KTVerifier getDisplayStatusForResults:isSelfOptedIn:]_block_invoke.183
+ ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.536
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.486
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.455
+ ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.552
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.515
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.564
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2.566
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.492
+ ___59-[KTVerifier getCachedValidatePeerResults:completionBlock:]_block_invoke.129
+ ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.472
+ ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.524
+ ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.489
+ ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.509
+ ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.506
+ ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.458
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.461
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.461.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.466
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.466.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.462
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.467
+ ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.543
+ ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.561
+ ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.483
+ ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.558
+ ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.527
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.530
+ ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.573
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.533
+ ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.555
+ ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.584
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.569
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.570
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.518
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.576
+ ___block_literal_global.131
+ ___block_literal_global.138
+ ___block_literal_global.142
+ ___block_literal_global.148
+ ___block_literal_global.156
+ ___block_literal_global.181
+ ___block_literal_global.189
+ ___block_literal_global.191
+ ___block_literal_global.382
+ ___block_literal_global.386
+ ___block_literal_global.390
+ ___block_literal_global.417
+ ___block_literal_global.423
+ ___block_literal_global.426
+ ___block_literal_global.429
+ ___block_literal_global.431
+ ___block_literal_global.434
+ ___block_literal_global.437
+ ___block_literal_global.439
+ ___block_literal_global.444
+ ___block_literal_global.446
+ ___block_literal_global.448
+ ___block_literal_global.451
+ ___block_literal_global.454
+ ___block_literal_global.457
+ ___block_literal_global.460
+ ___block_literal_global.469
+ ___block_literal_global.471
+ ___block_literal_global.477
+ ___block_literal_global.482
+ ___block_literal_global.485
+ ___block_literal_global.488
+ ___block_literal_global.491
+ ___block_literal_global.494
+ ___block_literal_global.497
+ ___block_literal_global.517
+ ___block_literal_global.520
+ ___block_literal_global.523
+ ___block_literal_global.526
+ ___block_literal_global.529
+ ___block_literal_global.532
+ ___block_literal_global.535
+ ___block_literal_global.538
+ ___block_literal_global.542
+ ___block_literal_global.545
+ ___block_literal_global.557
+ ___block_literal_global.560
+ ___block_literal_global.563
+ ___block_literal_global.568
+ ___block_literal_global.572
+ ___block_literal_global.575
+ ___block_literal_global.578
+ ___block_literal_global.583
+ _kTransparencyFlagSignaturePolicy
+ _objc_msgSend$addApplicationPrefixForIdentifier:uri:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$fetchNow
+ _objc_msgSend$hasInternalDiagnostics
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$ktURI
+ _objc_msgSend$ktURIVRF
+ _objc_msgSend$privacyURI:
+ _objc_msgSend$results
+ _objc_msgSend$setFetchNow:
+ _objc_msgSend$setResults:
+ _objc_msgSend$setTraceUUID:
+ _objc_msgSend$setUriToVerificationInfo:
+ _objc_msgSend$traceUUID
+ _objc_msgSend$uriToVerificationInfo
+ _objc_msgSend$validatePeers:completionBlock:
- GCC_except_table115
- GCC_except_table147
- GCC_except_table158
- GCC_except_table163
- GCC_except_table173
- GCC_except_table180
- GCC_except_table86
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.425
- ___35-[KTVerifier clearPeerCache:error:]_block_invoke.189
- ___35-[KTVerifier clearPeerCache:error:]_block_invoke_2.190
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.497
- ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.555
- ___44-[KTVerifier ignoreFailureForResults:error:]_block_invoke.140
- ___44-[KTVerifier ignoreFailureForResults:error:]_block_invoke_2.141
- ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.355
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.515
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.516
- ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.394
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.400
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.359
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.360
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.488
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.408
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.408.cold.1
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.411
- ___46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.151
- ___46-[KTVerifier markFailureSeenForResults:error:]_block_invoke.136
- ___46-[KTVerifier markFailureSeenForResults:error:]_block_invoke_2.137
- ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.363
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.471
- ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.397
- ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.522
- ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.525
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.454
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.456
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.416
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.418
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.418.cold.1
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.428
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.367
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.373
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.369
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.384
- ___51-[KTVerifier initiateQueryForUris:completionBlock:]_block_invoke.132
- ___51-[KTVerifier initiateQueryForUris:completionBlock:]_block_invoke_2.133
- ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.403
- ___55-[KTVerifier getDisplayStatusForResults:isSelfOptedIn:]_block_invoke.180
- ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.512
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.462
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.431
- ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.528
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.491
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.540
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2.542
- ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.468
- ___59-[KTVerifier getCachedValidatePeerResults:completionBlock:]_block_invoke.126
- ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.448
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.500
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.465
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.485
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.482
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.434
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.437
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.437.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.442
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.442.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.438
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.443
- ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.519
- ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.537
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.459
- ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.534
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.503
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.506
- ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.549
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.509
- ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.531
- ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.560
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.545
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.546
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.494
- ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.552
- ___block_literal_global.150
- ___block_literal_global.178
- ___block_literal_global.183
- ___block_literal_global.188
- ___block_literal_global.358
- ___block_literal_global.362
- ___block_literal_global.366
- ___block_literal_global.372
- ___block_literal_global.393
- ___block_literal_global.399
- ___block_literal_global.402
- ___block_literal_global.405
- ___block_literal_global.407
- ___block_literal_global.410
- ___block_literal_global.413
- ___block_literal_global.415
- ___block_literal_global.422
- ___block_literal_global.424
- ___block_literal_global.427
- ___block_literal_global.430
- ___block_literal_global.433
- ___block_literal_global.436
- ___block_literal_global.440
- ___block_literal_global.445
- ___block_literal_global.447
- ___block_literal_global.453
- ___block_literal_global.458
- ___block_literal_global.461
- ___block_literal_global.467
- ___block_literal_global.470
- ___block_literal_global.473
- ___block_literal_global.481
- ___block_literal_global.484
- ___block_literal_global.487
- ___block_literal_global.490
- ___block_literal_global.493
- ___block_literal_global.496
- ___block_literal_global.499
- ___block_literal_global.502
- ___block_literal_global.518
- ___block_literal_global.521
- ___block_literal_global.524
- ___block_literal_global.527
- ___block_literal_global.530
- ___block_literal_global.533
- ___block_literal_global.536
- ___block_literal_global.539
- ___block_literal_global.544
- ___block_literal_global.559
CStrings:
+ "KTRedactedDescription"
+ "KTURI"
+ "KTValidatePeersQuery"
+ "KTValidatePeersResponse"
+ "T@\"NSData\",&,V_ktURIVRF"
+ "T@\"NSDictionary\",&,V_results"
+ "T@\"NSDictionary\",&,V_uriToVerificationInfo"
+ "T@\"NSString\",&,V_ktURI"
+ "T@\"NSString\",&,V_traceUUID"
+ "TB,V_fetchNow"
+ "_fetchNow"
+ "_ktURI"
+ "_ktURIVRF"
+ "_results"
+ "_traceUUID"
+ "_uriToVerificationInfo"
+ "clearKTSignaturePolicy"
+ "dataUsingEncoding:"
+ "fetchNow"
+ "initWithApplication:peers:"
+ "initWithApplication:results:"
+ "initWithIDSURL:application:"
+ "keyEnumerator"
+ "ktSignaturePolicy"
+ "ktURI"
+ "ktURIVRF"
+ "overrideSignaturePolicy"
+ "privacyURI:"
+ "redactedDescription"
+ "results"
+ "setFetchNow:"
+ "setKtURI:"
+ "setKtURIVRF:"
+ "setResults:"
+ "setTraceUUID:"
+ "setUriToVerificationInfo:"
+ "uriToVerificationInfo"
+ "v32@0:8@\"KTValidatePeersQuery\"16@?<v@?@\"KTValidatePeersResponse\"@\"NSError\">24"
+ "validatePeers:completionBlock:"

```
