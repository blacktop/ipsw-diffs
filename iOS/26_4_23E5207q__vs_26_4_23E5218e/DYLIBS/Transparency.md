## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1547.100.130.0.0
-  __TEXT.__text: 0x4ca2c
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x44fc
-  __TEXT.__cstring: 0x27ae
-  __TEXT.__const: 0x136b
+1547.100.135.0.0
+  __TEXT.__text: 0x4d944
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x451c
+  __TEXT.__cstring: 0x27db
+  __TEXT.__const: 0x17f6
   __TEXT.__gcc_except_tab: 0x4ec
   __TEXT.__oslogstring: 0x1bdc
-  __TEXT.__swift5_typeref: 0x390
-  __TEXT.__constg_swiftt: 0x2f0
-  __TEXT.__swift5_reflstr: 0x4e9
+  __TEXT.__swift5_typeref: 0x41d
+  __TEXT.__constg_swiftt: 0x344
+  __TEXT.__swift5_reflstr: 0x4fb
   __TEXT.__swift5_fieldmd: 0x504
-  __TEXT.__swift5_proto: 0x10c
-  __TEXT.__swift5_types: 0x4c
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x19b0
-  __TEXT.__eh_frame: 0x4d0
-  __TEXT.__objc_classname: 0x77b
-  __TEXT.__objc_methname: 0x7810
+  __TEXT.__swift5_proto: 0x158
+  __TEXT.__swift5_types: 0x58
+  __TEXT.__swift5_assocty: 0xf0
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__unwind_info: 0x1a60
+  __TEXT.__eh_frame: 0x600
+  __TEXT.__objc_classname: 0x79b
+  __TEXT.__objc_methname: 0x7840
   __TEXT.__objc_methtype: 0x1f9f
-  __TEXT.__objc_stubs: 0x5b80
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x1598
-  __DATA_CONST.__objc_classlist: 0x210
+  __TEXT.__objc_stubs: 0x5ba0
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x15b8
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e50
+  __DATA_CONST.__objc_selrefs: 0x1e58
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x180
-  __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH_CONST.__const: 0x2800
+  __AUTH_CONST.__auth_got: 0x740
+  __AUTH_CONST.__const: 0x2920
   __AUTH_CONST.__cfstring: 0x3960
-  __AUTH_CONST.__objc_const: 0x7618
+  __AUTH_CONST.__objc_const: 0x76a8
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH.__objc_data: 0x268
+  __AUTH.__objc_data: 0x2b8
   __AUTH.__data: 0x2e8
   __DATA.__objc_ivar: 0x3a8
-  __DATA.__data: 0x988
-  __DATA.__bss: 0x2350
+  __DATA.__data: 0xa08
+  __DATA.__bss: 0x2cd0
   __DATA_DIRTY.__objc_data: 0x1358
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x1b8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 512F3A78-68F3-3354-9AFB-A4B13CA3EF08
-  Functions: 2498
-  Symbols:   6782
-  CStrings:  2797
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: B6492B0F-78F3-38D3-8A98-AE379E536ABF
+  Functions: 2564
+  Symbols:   6814
+  CStrings:  2800
 
Symbols:
+ +[TransparencyXPCConnection cachedConnection:interfaceClass:]
+ +[TransparencyXPCConnectionCache cachedConnection:interface:]
+ GCC_except_table16
+ GCC_except_table25
+ _OBJC_CLASS_$_TransparencyXPCConnectionCache
+ _OBJC_METACLASS_$_TransparencyXPCConnectionCache
+ __OBJC_$_CLASS_METHODS_TransparencyXPCConnectionCache
+ __OBJC_CLASS_RO_$_TransparencyXPCConnectionCache
+ __OBJC_METACLASS_RO_$_TransparencyXPCConnectionCache
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.537
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.609
+ ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.672
+ ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.470
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.627
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.628
+ ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.509
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.474
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.475
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.600
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.520
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.520.cold.1
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.523
+ ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.478
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.583
+ ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.512
+ ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.634
+ ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.637
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.566
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.568
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.528
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.530
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.530.cold.1
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.540
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.482
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.488
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.484
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.499
+ ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.515
+ ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.624
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.574
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.543
+ ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.640
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.603
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
+ ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke.679
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke.657
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke_2.659
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.618
+ ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.666
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.621
+ ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.643
+ ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.676
+ ___76-[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]_block_invoke.652
+ ___76-[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]_block_invoke_2.654
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.662
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.663
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.606
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.669
+ ___block_literal_global.473
+ ___block_literal_global.477
+ ___block_literal_global.481
+ ___block_literal_global.487
+ ___block_literal_global.517
+ ___block_literal_global.525
+ ___block_literal_global.527
+ ___block_literal_global.532
+ ___block_literal_global.534
+ ___block_literal_global.548
+ ___block_literal_global.552
+ ___block_literal_global.557
+ ___block_literal_global.559
+ ___block_literal_global.565
+ ___block_literal_global.585
+ ___block_literal_global.626
+ ___block_literal_global.651
+ ___block_literal_global.656
+ ___block_literal_global.661
+ ___block_literal_global.671
+ ___block_literal_global.678
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_Transparency
+ _associated conformance 12Transparency04CoreA13EnumShimErrorO10Foundation021_ObjectiveCBridgeableE0AAs0E0
+ _associated conformance 12Transparency04CoreA13EnumShimErrorO10Foundation13CustomNSErrorAAs0E0
+ _associated conformance 12Transparency04CoreA13EnumShimErrorO10Foundation15_BridgedNSErrorAA8RawValueSY_s17FixedWidthInteger
+ _associated conformance 12Transparency04CoreA13EnumShimErrorO10Foundation15_BridgedNSErrorAASH
+ _associated conformance 12Transparency04CoreA13EnumShimErrorO10Foundation15_BridgedNSErrorAASY
+ _associated conformance 12Transparency04CoreA13EnumShimErrorO10Foundation15_BridgedNSErrorAaD021_ObjectiveCBridgeableE0
+ _associated conformance 12Transparency04CoreA13EnumShimErrorOSHAASQ
+ _associated conformance 12Transparency04CoreA15ApplicationShimOSHAASQ
+ _associated conformance 12Transparency04CoreA15ApplicationShimOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 12Transparency04CoreA21ServerEnvironmentShimOSHAASQ
+ _associated conformance 12Transparency04CoreA21ServerEnvironmentShimOs12CaseIterableAA8AllCasessADP_Sl
+ _objc_msgSend$cachedConnection:interfaceClass:
+ _swift_allocError
+ _swift_willThrow
+ _symbolic Say_____G 12Transparency04CoreA15ApplicationShimO
+ _symbolic Say_____G 12Transparency04CoreA21ServerEnvironmentShimO
+ _symbolic _____ 12Transparency04CoreA13EnumShimErrorO
+ _symbolic _____ 12Transparency04CoreA15ApplicationShimO
+ _symbolic _____ 12Transparency04CoreA21ServerEnvironmentShimO
+ _symbolic _____Sg 16CoreTransparency13CTApplicationO
+ _symbolic _____Sg 16CoreTransparency19CTServerEnvironmentO
- GCC_except_table15
- GCC_except_table24
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.534
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.606
- ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.669
- ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.467
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.624
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.625
- ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.506
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.471
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.472
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.597
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.517
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.517.cold.1
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.520
- ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.475
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.580
- ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.509
- ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.631
- ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.634
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.563
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.565
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.525
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.527
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.527.cold.1
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.537
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.479
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.485
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.481
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.496
- ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.512
- ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.621
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.571
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.540
- ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.637
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.600
- ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.577
- ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.557
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.609
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.574
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.594
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.591
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.543
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.546
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.546.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.551
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.551.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.547
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.552
- ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.628
- ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.646
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.568
- ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.643
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.612
- ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke.676
- ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke.654
- ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke_2.656
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.615
- ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.663
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.618
- ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.640
- ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.673
- ___76-[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]_block_invoke.649
- ___76-[TransparencyDaemon networkKTPublicKeyBag:queryOptions:traceUUID:complete:]_block_invoke_2.651
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.659
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.660
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.603
- ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.666
- ___block_literal_global.470
- ___block_literal_global.474
- ___block_literal_global.478
- ___block_literal_global.484
- ___block_literal_global.505
- ___block_literal_global.516
- ___block_literal_global.524
- ___block_literal_global.529
- ___block_literal_global.531
- ___block_literal_global.533
- ___block_literal_global.549
- ___block_literal_global.554
- ___block_literal_global.556
- ___block_literal_global.562
- ___block_literal_global.567
- ___block_literal_global.590
- ___block_literal_global.627
- ___block_literal_global.653
- ___block_literal_global.658
- ___block_literal_global.662
- ___block_literal_global.672
CStrings:
+ "Transparency.CoreTransparencyEnumShimError"
+ "TransparencyXPCConnectionCache"
+ "cachedConnection:interfaceClass:"

```
