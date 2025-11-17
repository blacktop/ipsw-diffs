## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1547.60.17.0.1
-  __TEXT.__text: 0x4af00
+1547.60.20.0.0
+  __TEXT.__text: 0x4b2b8
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x439c
-  __TEXT.__cstring: 0x27de
+  __TEXT.__objc_methlist: 0x446c
+  __TEXT.__cstring: 0x27fe
   __TEXT.__const: 0x12c0
   __TEXT.__gcc_except_tab: 0x508
   __TEXT.__oslogstring: 0x1bbd

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x19a8
+  __TEXT.__unwind_info: 0x19b8
   __TEXT.__eh_frame: 0x4d0
-  __TEXT.__objc_classname: 0x705
-  __TEXT.__objc_methname: 0x7439
-  __TEXT.__objc_methtype: 0x1f0d
-  __TEXT.__objc_stubs: 0x5920
+  __TEXT.__objc_classname: 0x724
+  __TEXT.__objc_methname: 0x75ef
+  __TEXT.__objc_methtype: 0x1f31
+  __TEXT.__objc_stubs: 0x5a00
   __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x1548
-  __DATA_CONST.__objc_classlist: 0x208
+  __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1da8
+  __DATA_CONST.__objc_selrefs: 0x1e08
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x180
   __AUTH_CONST.__auth_got: 0x708
   __AUTH_CONST.__const: 0x2800
-  __AUTH_CONST.__cfstring: 0x3860
-  __AUTH_CONST.__objc_const: 0x73e0
+  __AUTH_CONST.__cfstring: 0x38c0
+  __AUTH_CONST.__objc_const: 0x75a8
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH.__objc_data: 0x2b8
+  __AUTH.__objc_data: 0x308
   __AUTH.__data: 0x2f0
-  __DATA.__objc_ivar: 0x38c
+  __DATA.__objc_ivar: 0x3a0
   __DATA.__data: 0x968
   __DATA.__bss: 0x2350
   __DATA_DIRTY.__objc_data: 0x12b8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 820DB50E-6C63-3A15-8F99-19E021DEC633
-  Functions: 2476
-  Symbols:   6695
-  CStrings:  2747
+  UUID: 435DAB75-24A8-31B5-B4A6-CB97B547F620
+  Functions: 2491
+  Symbols:   6747
+  CStrings:  2777
 
Symbols:
+ +[KTVerifierResultQueryPerformance supportsSecureCoding]
+ -[KTIDSData idsServerHint]
+ -[KTIDSData ktOptIn]
+ -[KTIDSData setIdsServerHint:]
+ -[KTIDSData setKtOptIn:]
+ -[KTNetworkResponse initWithUUID:]
+ -[KTNetworkResponse init]
+ -[KTNetworkResponse requestUUID]
+ -[KTNetworkResponse setRequestUUID:]
+ -[KTVerifierResult queryPerformance]
+ -[KTVerifierResult setQueryPerformance:]
+ -[KTVerifierResultQueryPerformance encodeWithCoder:]
+ -[KTVerifierResultQueryPerformance initWithCoder:]
+ -[KTVerifierResultQueryPerformance networkQueryTimeInterval]
+ -[KTVerifierResultQueryPerformance setNetworkQueryTimeInterval:]
+ GCC_except_table154
+ GCC_except_table186
+ GCC_except_table219
+ _OBJC_CLASS_$_KTVerifierResultQueryPerformance
+ _OBJC_IVAR_$_KTIDSData._idsServerHint
+ _OBJC_IVAR_$_KTIDSData._ktOptIn
+ _OBJC_IVAR_$_KTNetworkResponse._requestUUID
+ _OBJC_IVAR_$_KTVerifierResult._queryPerformance
+ _OBJC_IVAR_$_KTVerifierResultQueryPerformance._networkQueryTimeInterval
+ _OBJC_METACLASS_$_KTVerifierResultQueryPerformance
+ __OBJC_$_CLASS_METHODS_KTVerifierResultQueryPerformance
+ __OBJC_$_CLASS_PROP_LIST_KTVerifierResultQueryPerformance
+ __OBJC_$_INSTANCE_METHODS_KTVerifierResultQueryPerformance
+ __OBJC_$_INSTANCE_VARIABLES_KTVerifierResultQueryPerformance
+ __OBJC_$_PROP_LIST_KTVerifierResultQueryPerformance
+ __OBJC_CLASS_PROTOCOLS_$_KTVerifierResultQueryPerformance
+ __OBJC_CLASS_RO_$_KTVerifierResultQueryPerformance
+ __OBJC_METACLASS_RO_$_KTVerifierResultQueryPerformance
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.537
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.609
+ ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.670
+ ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.467
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.627
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.628
+ ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.506
+ ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.512
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.471
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.472
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.600
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.520
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.520.cold.1
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.523
+ ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.475
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.583
+ ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.509
+ ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.634
+ ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.637
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.566
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.568
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.528
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.530
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.530.cold.1
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.540
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.479
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.485
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.481
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.496
+ ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.515
+ ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.624
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.574
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.543
+ ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke.677
+ ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.640
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.603
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.652
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2.654
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.580
+ ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.560
+ ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.612
+ ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.577
+ ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.597
+ ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.594
+ ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.546
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.549
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.549.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.554
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.554.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.550
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.555
+ ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.631
+ ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.649
+ ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.571
+ ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.646
+ ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.615
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.618
+ ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.664
+ ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.661
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.621
+ ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.643
+ ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.674
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.657
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.658
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.606
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.667
+ ___block_literal_global.470
+ ___block_literal_global.478
+ ___block_literal_global.484
+ ___block_literal_global.505
+ ___block_literal_global.508
+ ___block_literal_global.511
+ ___block_literal_global.514
+ ___block_literal_global.519
+ ___block_literal_global.525
+ ___block_literal_global.527
+ ___block_literal_global.534
+ ___block_literal_global.536
+ ___block_literal_global.539
+ ___block_literal_global.545
+ ___block_literal_global.548
+ ___block_literal_global.552
+ ___block_literal_global.557
+ ___block_literal_global.559
+ ___block_literal_global.565
+ ___block_literal_global.570
+ ___block_literal_global.573
+ ___block_literal_global.576
+ ___block_literal_global.579
+ ___block_literal_global.582
+ ___block_literal_global.585
+ ___block_literal_global.593
+ ___block_literal_global.596
+ ___block_literal_global.599
+ ___block_literal_global.602
+ ___block_literal_global.605
+ ___block_literal_global.608
+ ___block_literal_global.611
+ ___block_literal_global.614
+ ___block_literal_global.617
+ ___block_literal_global.630
+ ___block_literal_global.633
+ ___block_literal_global.636
+ ___block_literal_global.639
+ ___block_literal_global.642
+ ___block_literal_global.645
+ ___block_literal_global.648
+ ___block_literal_global.651
+ ___block_literal_global.660
+ ___block_literal_global.669
+ ___block_literal_global.673
+ ___block_literal_global.676
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$idsServerHint
+ _objc_msgSend$initWithUUID:
+ _objc_msgSend$ktOptIn
+ _objc_msgSend$networkQueryTimeInterval
+ _objc_msgSend$requestUUID
+ _objc_msgSend$setIdsServerHint:
+ _objc_msgSend$setKtOptIn:
+ _objc_msgSend$setNetworkQueryTimeInterval:
+ _objc_msgSend$setRequestUUID:
- GCC_except_table150
- GCC_except_table182
- GCC_except_table215
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.527
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.599
- ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.660
- ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.457
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.617
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.618
- ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.496
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.502
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.461
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.462
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.590
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.510
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.510.cold.1
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.513
- ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.465
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.573
- ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.499
- ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.624
- ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.627
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.556
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.558
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.518
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.520
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.520.cold.1
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.530
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.469
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.475
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.471
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.486
- ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.505
- ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.614
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.564
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.533
- ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke.667
- ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.630
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.593
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.642
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2.644
- ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.570
- ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.550
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.602
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.567
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.587
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.584
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.536
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.539
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.539.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.544
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.544.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.540
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.545
- ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.621
- ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.639
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.561
- ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.636
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.605
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.608
- ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.654
- ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.651
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.611
- ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.633
- ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.664
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.647
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.648
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.596
- ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.657
- ___block_literal_global.460
- ___block_literal_global.464
- ___block_literal_global.468
- ___block_literal_global.495
- ___block_literal_global.498
- ___block_literal_global.501
- ___block_literal_global.504
- ___block_literal_global.507
- ___block_literal_global.509
- ___block_literal_global.512
- ___block_literal_global.515
- ___block_literal_global.524
- ___block_literal_global.526
- ___block_literal_global.529
- ___block_literal_global.535
- ___block_literal_global.538
- ___block_literal_global.547
- ___block_literal_global.549
- ___block_literal_global.555
- ___block_literal_global.560
- ___block_literal_global.563
- ___block_literal_global.566
- ___block_literal_global.569
- ___block_literal_global.572
- ___block_literal_global.575
- ___block_literal_global.583
- ___block_literal_global.586
- ___block_literal_global.589
- ___block_literal_global.592
- ___block_literal_global.595
- ___block_literal_global.598
- ___block_literal_global.601
- ___block_literal_global.604
- ___block_literal_global.607
- ___block_literal_global.610
- ___block_literal_global.613
- ___block_literal_global.616
- ___block_literal_global.629
- ___block_literal_global.632
- ___block_literal_global.635
- ___block_literal_global.638
- ___block_literal_global.641
- ___block_literal_global.646
- ___block_literal_global.650
- ___block_literal_global.653
- ___block_literal_global.659
- _objc_msgSend$decodeInt32ForKey:
- _objc_msgSend$encodeInt32:forKey:
- _objc_msgSend$ktOptChangeReason
- _objc_msgSend$setKtOptChangeReason:
CStrings:
+ "\v"
+ "@\"KTVerifierResultQueryPerformance\""
+ "KTVerifierResultQueryPerformance"
+ "T@\"KTVerifierResultQueryPerformance\",&,V_queryPerformance"
+ "T@\"NSNumber\",&,V_ktOptIn"
+ "T@\"NSString\",&,V_idsServerHint"
+ "T@\"NSString\",&,V_requestUUID"
+ "TQ,V_flags"
+ "Td,V_networkQueryTimeInterval"
+ "UUID"
+ "UUIDString"
+ "_idsServerHint"
+ "_ktOptIn"
+ "_networkQueryTimeInterval"
+ "_queryPerformance"
+ "_requestUUID"
+ "idsServerHint"
+ "initWithUUID:"
+ "itunesAccountDeleted"
+ "ktOptIn"
+ "networkQueryTimeInterval"
+ "queryPerformance"
+ "requestUUID"
+ "setIdsServerHint:"
+ "setKtOptIn:"
+ "setNetworkQueryTimeInterval:"
+ "setQueryPerformance:"
+ "setRequestUUID:"
- "\t"
- "Ti,V_flags"
- "decodeInt32ForKey:"
- "encodeInt32:forKey:"

```
