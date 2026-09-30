## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1547.40.20.0.0
-  __TEXT.__text: 0x49fc8
+1547.60.16.0.0
+  __TEXT.__text: 0x4af00
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x41c4
-  __TEXT.__cstring: 0x274e
-  __TEXT.__const: 0x12b8
+  __TEXT.__objc_methlist: 0x439c
+  __TEXT.__cstring: 0x27de
+  __TEXT.__const: 0x12c0
   __TEXT.__gcc_except_tab: 0x508
-  __TEXT.__oslogstring: 0x1b91
+  __TEXT.__oslogstring: 0x1bbd
   __TEXT.__swift5_typeref: 0x390
   __TEXT.__constg_swiftt: 0x2f0
-  __TEXT.__swift5_reflstr: 0x485
-  __TEXT.__swift5_fieldmd: 0x4e0
+  __TEXT.__swift5_reflstr: 0x4e9
+  __TEXT.__swift5_fieldmd: 0x504
   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1968
+  __TEXT.__unwind_info: 0x19a8
   __TEXT.__eh_frame: 0x4d0
-  __TEXT.__objc_classname: 0x6e4
-  __TEXT.__objc_methname: 0x7257
-  __TEXT.__objc_methtype: 0x1e3c
-  __TEXT.__objc_stubs: 0x5700
-  __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x1520
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __TEXT.__objc_classname: 0x705
+  __TEXT.__objc_methname: 0x7439
+  __TEXT.__objc_methtype: 0x1f0d
+  __TEXT.__objc_stubs: 0x5920
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0x1548
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d10
+  __DATA_CONST.__objc_selrefs: 0x1da8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x178
   __AUTH_CONST.__auth_got: 0x708
-  __AUTH_CONST.__const: 0x27c0
-  __AUTH_CONST.__cfstring: 0x3760
-  __AUTH_CONST.__objc_const: 0x7020
+  __AUTH_CONST.__const: 0x2800
+  __AUTH_CONST.__cfstring: 0x3860
+  __AUTH_CONST.__objc_const: 0x73e0
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH.__objc_data: 0x218
+  __AUTH.__objc_data: 0x2b8
   __AUTH.__data: 0x2f0
-  __DATA.__objc_ivar: 0x364
+  __DATA.__objc_ivar: 0x38c
   __DATA.__data: 0x968
   __DATA.__bss: 0x2350
   __DATA_DIRTY.__objc_data: 0x12b8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 8E3C0031-63FE-3FA0-83DA-9C7956532262
-  Functions: 2436
-  Symbols:   6561
-  CStrings:  2691
+  UUID: B971E0B7-B0D4-3CAF-A9E7-E0BD4DDDEE9E
+  Functions: 2476
+  Symbols:   6695
+  CStrings:  2747
 
Symbols:
+ +[KTIDSDataURI supportsSecureCoding]
+ +[KTQueryOptions supportsSecureCoding]
+ +[KTVerificationInfo decodeKTOptsData:]
+ -[KTIDSData ktOpts]
+ -[KTIDSData setKtOpts:]
+ -[KTIDSDataURI .cxx_destruct]
+ -[KTIDSDataURI description]
+ -[KTIDSDataURI encodeWithCoder:]
+ -[KTIDSDataURI idsData]
+ -[KTIDSDataURI initWithCoder:]
+ -[KTIDSDataURI initWithIDSData:ktResponse:]
+ -[KTIDSDataURI ktResponse]
+ -[KTIDSDataURI setIdsData:]
+ -[KTIDSDataURI setKtResponse:]
+ -[KTNetworkResponse error]
+ -[KTNetworkResponse queryTime]
+ -[KTNetworkResponse setError:]
+ -[KTNetworkResponse setQueryTime:]
+ -[KTNetworkResponse setType:]
+ -[KTNetworkResponse setUri:]
+ -[KTNetworkResponse type]
+ -[KTNetworkResponse uri]
+ -[KTQueryOptions description]
+ -[KTQueryOptions encodeWithCoder:]
+ -[KTQueryOptions flags]
+ -[KTQueryOptions initWithCoder:]
+ -[KTQueryOptions setFlags:]
+ -[KTQueryOptions setTimeout:]
+ -[KTQueryOptions timeout]
+ -[KTVerificationInfo ktOptsData]
+ -[KTVerificationInfo ktOpts]
+ -[KTVerificationInfo setKtOpts:]
+ -[TransparencyAnalytics logRockwellFailureForEventNamed:withAttributes:]
+ -[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]
+ -[TransparencyDaemon validateURIs:queryOptions:complete:]
+ -[TransparencySFAnalytics logRockwellFailureForEventNamed:withAttributes:]
+ GCC_except_table150
+ GCC_except_table182
+ GCC_except_table215
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table50
+ _OBJC_CLASS_$_KTIDSDataURI
+ _OBJC_CLASS_$_KTQueryOptions
+ _OBJC_IVAR_$_KTIDSData._ktOpts
+ _OBJC_IVAR_$_KTIDSDataURI._idsData
+ _OBJC_IVAR_$_KTIDSDataURI._ktResponse
+ _OBJC_IVAR_$_KTNetworkResponse._error
+ _OBJC_IVAR_$_KTNetworkResponse._queryTime
+ _OBJC_IVAR_$_KTNetworkResponse._type
+ _OBJC_IVAR_$_KTNetworkResponse._uri
+ _OBJC_IVAR_$_KTQueryOptions._flags
+ _OBJC_IVAR_$_KTQueryOptions._timeout
+ _OBJC_IVAR_$_KTVerificationInfo._ktOpts
+ _OBJC_METACLASS_$_KTIDSDataURI
+ _OBJC_METACLASS_$_KTQueryOptions
+ __OBJC_$_CLASS_METHODS_KTIDSDataURI
+ __OBJC_$_CLASS_METHODS_KTQueryOptions
+ __OBJC_$_CLASS_PROP_LIST_KTIDSDataURI
+ __OBJC_$_CLASS_PROP_LIST_KTQueryOptions
+ __OBJC_$_INSTANCE_METHODS_KTIDSDataURI
+ __OBJC_$_INSTANCE_METHODS_KTQueryOptions
+ __OBJC_$_INSTANCE_VARIABLES_KTIDSDataURI
+ __OBJC_$_INSTANCE_VARIABLES_KTQueryOptions
+ __OBJC_$_PROP_LIST_KTIDSDataURI
+ __OBJC_$_PROP_LIST_KTQueryOptions
+ __OBJC_CLASS_PROTOCOLS_$_KTIDSDataURI
+ __OBJC_CLASS_PROTOCOLS_$_KTQueryOptions
+ __OBJC_CLASS_RO_$_KTIDSDataURI
+ __OBJC_CLASS_RO_$_KTQueryOptions
+ __OBJC_METACLASS_RO_$_KTIDSDataURI
+ __OBJC_METACLASS_RO_$_KTQueryOptions
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.527
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.599
+ ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.660
+ ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.457
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.617
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.618
+ ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.496
+ ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.502
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.461
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.462
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.590
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.510
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.510.cold.1
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.513
+ ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.465
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.573
+ ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.499
+ ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.624
+ ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.627
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.556
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.558
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.518
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.520
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.520.cold.1
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.530
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.469
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.475
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.471
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.486
+ ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.505
+ ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.614
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.564
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.533
+ ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke
+ ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke.667
+ ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke.cold.1
+ ___57-[TransparencyDaemon validateURIs:queryOptions:complete:]_block_invoke_2
+ ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.630
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.593
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.642
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2.644
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.570
+ ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.550
+ ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.602
+ ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.567
+ ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.587
+ ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.584
+ ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.536
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.539
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.539.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.544
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.544.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.540
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.545
+ ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.621
+ ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.639
+ ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.561
+ ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.636
+ ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.605
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.608
+ ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke
+ ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.654
+ ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.cold.1
+ ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke_2
+ ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.651
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.611
+ ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.633
+ ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.664
+ ___74-[TransparencySFAnalytics logRockwellFailureForEventNamed:withAttributes:]_block_invoke
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.647
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.648
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.596
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.657
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e46_v24?0"<transparencyd_protocol>"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.134
+ ___block_literal_global.143
+ ___block_literal_global.460
+ ___block_literal_global.474
+ ___block_literal_global.504
+ ___block_literal_global.507
+ ___block_literal_global.517
+ ___block_literal_global.522
+ ___block_literal_global.526
+ ___block_literal_global.529
+ ___block_literal_global.532
+ ___block_literal_global.535
+ ___block_literal_global.538
+ ___block_literal_global.547
+ ___block_literal_global.560
+ ___block_literal_global.563
+ ___block_literal_global.566
+ ___block_literal_global.569
+ ___block_literal_global.575
+ ___block_literal_global.583
+ ___block_literal_global.586
+ ___block_literal_global.589
+ ___block_literal_global.592
+ ___block_literal_global.595
+ ___block_literal_global.598
+ ___block_literal_global.601
+ ___block_literal_global.604
+ ___block_literal_global.607
+ ___block_literal_global.610
+ ___block_literal_global.613
+ ___block_literal_global.616
+ ___block_literal_global.620
+ ___block_literal_global.623
+ ___block_literal_global.626
+ ___block_literal_global.629
+ ___block_literal_global.63
+ ___block_literal_global.632
+ ___block_literal_global.635
+ ___block_literal_global.638
+ ___block_literal_global.641
+ ___block_literal_global.646
+ ___block_literal_global.650
+ ___block_literal_global.653
+ ___block_literal_global.656
+ ___block_literal_global.659
+ ___block_literal_global.663
+ ___block_literal_global.666
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$decodeKTOptsData:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$flags
+ _objc_msgSend$idsData
+ _objc_msgSend$ktOpts
+ _objc_msgSend$ktOptsData
+ _objc_msgSend$ktQuery:application:queryOptions:trace:complete:
+ _objc_msgSend$ktResponse
+ _objc_msgSend$queryTime
+ _objc_msgSend$setFlags:
+ _objc_msgSend$setIdsData:
+ _objc_msgSend$setKtOpts:
+ _objc_msgSend$setKtResponse:
+ _objc_msgSend$setQueryTime:
+ _objc_msgSend$validateURIs:queryOptions:complete:
- -[TransparencyAnalytics logRockwellForEventNamed:withAttributes:]
- -[TransparencySFAnalytics logRockwellForEventNamed:withAttributes:]
- GCC_except_table124
- GCC_except_table156
- GCC_except_table189
- GCC_except_table43
- GCC_except_table44
- GCC_except_table45
- GCC_except_table46
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.453
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.525
- ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.583
- ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.383
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.543
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.544
- ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.422
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.428
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.387
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.388
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.516
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.436
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.436.cold.1
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.439
- ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.391
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.499
- ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.425
- ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.550
- ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.553
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.482
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.484
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.444
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.446
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.446.cold.1
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.456
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.395
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.401
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.397
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.412
- ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.431
- ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.540
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.490
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.459
- ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.556
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.519
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.568
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2.570
- ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.496
- ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.476
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.528
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.493
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.513
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.510
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.462
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.465
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.465.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.470
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.470.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.466
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.471
- ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.547
- ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.565
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.487
- ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.562
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.531
- ___67-[TransparencySFAnalytics logRockwellForEventNamed:withAttributes:]_block_invoke
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.534
- ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.577
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.537
- ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.559
- ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.588
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.573
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.574
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.522
- ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.580
- ___block_literal_global.144
- ___block_literal_global.146
- ___block_literal_global.386
- ___block_literal_global.390
- ___block_literal_global.394
- ___block_literal_global.400
- ___block_literal_global.421
- ___block_literal_global.424
- ___block_literal_global.427
- ___block_literal_global.430
- ___block_literal_global.433
- ___block_literal_global.435
- ___block_literal_global.438
- ___block_literal_global.441
- ___block_literal_global.443
- ___block_literal_global.448
- ___block_literal_global.450
- ___block_literal_global.452
- ___block_literal_global.455
- ___block_literal_global.458
- ___block_literal_global.461
- ___block_literal_global.473
- ___block_literal_global.475
- ___block_literal_global.481
- ___block_literal_global.486
- ___block_literal_global.489
- ___block_literal_global.492
- ___block_literal_global.518
- ___block_literal_global.521
- ___block_literal_global.527
- ___block_literal_global.530
- ___block_literal_global.533
- ___block_literal_global.536
- ___block_literal_global.539
- ___block_literal_global.546
- ___block_literal_global.552
- ___block_literal_global.558
- ___block_literal_global.561
- ___block_literal_global.564
- ___block_literal_global.567
- ___block_literal_global.576
- ___block_literal_global.579
- ___block_literal_global.582
- ___block_literal_global.587
- ___block_literal_global.66
CStrings:
+ "\t"
+ "<KTIDSValidateURI>"
+ "<KTQueryOptions: flags: %08x>"
+ "@\"KTIDSData\""
+ "@\"KTNetworkResponse\""
+ "JSONObjectWithData:options:error:"
+ "KTIDSDataURI"
+ "KTQueryManagerUseBatchQueries"
+ "KTQueryOptions"
+ "Sending validateURIs:queryOptions:complete:"
+ "T@\"KTIDSData\",&,V_idsData"
+ "T@\"KTNetworkResponse\",&,V_ktResponse"
+ "T@\"NSDate\",&,V_queryTime"
+ "T@\"NSDictionary\",&,V_ktOpts"
+ "Ti,V_flags"
+ "Ti,V_type"
+ "_flags"
+ "_idsData"
+ "_ktOpts"
+ "_ktResponse"
+ "_queryTime"
+ "_type"
+ "decodeInt32ForKey:"
+ "decodeKTOptsData:"
+ "encodeInt32:forKey:"
+ "flags"
+ "idsData"
+ "initWithIDSData:ktResponse:"
+ "ktOpts"
+ "ktOptsData"
+ "ktQuery:application:queryOptions:trace:complete:"
+ "ktResponse"
+ "queryTime"
+ "setFlags:"
+ "setIdsData:"
+ "setKtOpts:"
+ "setKtResponse:"
+ "setQueryTime:"
+ "setType:"
+ "v40@0:8@\"NSDictionary\"16@\"KTQueryOptions\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v56@0:8@\"NSSet\"16@\"NSString\"24@\"KTQueryOptions\"32@\"NSString\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "validateURIs:queryOptions:complete:"
+ "x-apple-server-hint"
- "logRockwellForEventNamed:withAttributes:"

```
