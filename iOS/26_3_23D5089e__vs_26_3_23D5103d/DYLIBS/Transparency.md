## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1547.80.7.0.0
-  __TEXT.__text: 0x4b09c
+1547.80.8.0.0
+  __TEXT.__text: 0x4ae94
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x4484
+  __TEXT.__objc_methlist: 0x4470
   __TEXT.__cstring: 0x27fe
   __TEXT.__const: 0x12c0
   __TEXT.__gcc_except_tab: 0x508
-  __TEXT.__oslogstring: 0x1bc7
+  __TEXT.__oslogstring: 0x1ba2
   __TEXT.__swift5_typeref: 0x390
   __TEXT.__constg_swiftt: 0x2f0
   __TEXT.__swift5_reflstr: 0x4e9

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x19a8
+  __TEXT.__unwind_info: 0x1998
   __TEXT.__eh_frame: 0x4d0
   __TEXT.__objc_classname: 0x724
-  __TEXT.__objc_methname: 0x7644
+  __TEXT.__objc_methname: 0x760f
   __TEXT.__objc_methtype: 0x1f3e
-  __TEXT.__objc_stubs: 0x5a20
+  __TEXT.__objc_stubs: 0x5a00
   __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x1570
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e18
+  __DATA_CONST.__objc_selrefs: 0x1e08
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x180
   __AUTH_CONST.__auth_got: 0x708
-  __AUTH_CONST.__const: 0x27e0
+  __AUTH_CONST.__const: 0x27c0
   __AUTH_CONST.__cfstring: 0x38c0
-  __AUTH_CONST.__objc_const: 0x75a8
+  __AUTH_CONST.__objc_const: 0x75a0
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x308
   __AUTH.__data: 0x2f0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 6922A9FE-F5E0-3FA0-8B33-B6973241331D
-  Functions: 2489
-  Symbols:   6744
-  CStrings:  2779
+  UUID: A0772C31-0965-32AF-A8FC-EBEC385718D8
+  Functions: 2484
+  Symbols:   6732
+  CStrings:  2776
 
Symbols:
+ GCC_except_table182
+ GCC_except_table215
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.534
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.606
+ ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.664
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.624
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.625
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.597
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.517
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.517.cold.1
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.520
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.580
+ ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.631
+ ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.634
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.563
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.565
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.525
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.527
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.527.cold.1
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.537
+ ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.512
+ ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.621
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.571
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.540
+ ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.637
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.600
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.577
+ ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.557
+ ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.609
+ ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.574
+ ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.594
+ ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.591
+ ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.543
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.546
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.546.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.551
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.551.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.547
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.552
+ ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.628
+ ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.646
+ ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.568
+ ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.643
+ ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.612
+ ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke.671
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke.649
+ ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke_2.651
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.615
+ ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.658
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.618
+ ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.640
+ ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.668
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.654
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.655
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.603
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.661
+ ___block_literal_global.516
+ ___block_literal_global.524
+ ___block_literal_global.529
+ ___block_literal_global.531
+ ___block_literal_global.533
+ ___block_literal_global.549
+ ___block_literal_global.554
+ ___block_literal_global.556
+ ___block_literal_global.562
+ ___block_literal_global.567
+ ___block_literal_global.590
+ ___block_literal_global.627
+ ___block_literal_global.653
+ ___block_literal_global.657
+ ___block_literal_global.667
- -[TransparencyDaemon transparencyFetchSelf:]
- GCC_except_table186
- GCC_except_table219
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.537
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.609
- ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.667
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.627
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.628
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.512
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.cold.1
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke_2
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.600
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.520
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.520.cold.1
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.523
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.583
- ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.634
- ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.637
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.566
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.568
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.528
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.530
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.530.cold.1
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.540
- ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.515
- ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.624
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.574
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.543
- ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.640
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.603
- ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.580
- ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.560
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.612
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.577
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.597
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.594
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.546
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.549
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.549.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.554
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.554.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.550
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.555
- ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.631
- ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.649
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.571
- ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.646
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.615
- ___67-[TransparencyDaemon validateURIs:queryOptions:traceUUID:complete:]_block_invoke.674
- ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke.652
- ___68-[TransparencyDaemon networkKTQuery:application:traceUUID:complete:]_block_invoke_2.654
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.618
- ___70-[TransparencyDaemon ktQuery:application:queryOptions:trace:complete:]_block_invoke.661
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.621
- ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.643
- ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.671
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.657
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.658
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.606
- ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.664
- ___block_literal_global.517
- ___block_literal_global.525
- ___block_literal_global.527
- ___block_literal_global.532
- ___block_literal_global.534
- ___block_literal_global.548
- ___block_literal_global.552
- ___block_literal_global.557
- ___block_literal_global.559
- ___block_literal_global.565
- ___block_literal_global.585
- ___block_literal_global.626
- ___block_literal_global.651
- ___block_literal_global.656
- ___block_literal_global.666
- ___block_literal_global.673
- _objc_msgSend$transparencyTriggerFetchSelf:
CStrings:
- "Sending transparencyTriggerFetchSelf"
- "transparencyFetchSelf:"
- "transparencyTriggerFetchSelf:"

```
