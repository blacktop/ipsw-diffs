## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1547.0.24.0.0
-  __TEXT.__text: 0x49970
+1547.0.28.0.0
+  __TEXT.__text: 0x49a20
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x4134
+  __TEXT.__objc_methlist: 0x414c
   __TEXT.__cstring: 0x26fe
   __TEXT.__const: 0x11b0
   __TEXT.__gcc_except_tab: 0x508

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1958
+  __TEXT.__unwind_info: 0x1960
   __TEXT.__eh_frame: 0x4d0
   __TEXT.__objc_classname: 0x6e3
   __TEXT.__objc_methname: 0x7105

   __AUTH_CONST.__auth_got: 0x708
   __AUTH_CONST.__const: 0x27c0
   __AUTH_CONST.__cfstring: 0x36e0
-  __AUTH_CONST.__objc_const: 0x6f60
+  __AUTH_CONST.__objc_const: 0x6f90
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x218
   __AUTH.__data: 0x2f0
-  __DATA.__objc_ivar: 0x354
+  __DATA.__objc_ivar: 0x358
   __DATA.__data: 0x978
   __DATA.__bss: 0x2350
   __DATA_DIRTY.__objc_data: 0x12b8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 9B16A315-DB1B-38B1-830E-84BB6296422A
-  Functions: 2424
-  Symbols:   6528
+  UUID: 660AE45A-020C-31EB-81F5-7FA2D24B453F
+  Functions: 2426
+  Symbols:   6533
   CStrings:  2670
 
Symbols:
+ -[TransparencyIDSRegistrationRequest setTraceUUID:]
+ -[TransparencyIDSRegistrationRequest traceUUID]
+ GCC_except_table124
+ GCC_except_table156
+ GCC_except_table189
+ _OBJC_IVAR_$_TransparencyIDSRegistrationRequest._traceUUID
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.453
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.525
+ ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.583
+ ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.383
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.543
+ ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.544
+ ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.422
+ ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.428
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.387
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.388
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.516
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.436
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.436.cold.1
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.439
+ ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.391
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.499
+ ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.425
+ ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.550
+ ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.553
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.482
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.484
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.444
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.446
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.446.cold.1
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.456
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.395
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.401
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.397
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.412
+ ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.431
+ ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.540
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.490
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.459
+ ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.556
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.519
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.568
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2.570
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.496
+ ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.476
+ ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.528
+ ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.493
+ ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.513
+ ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.510
+ ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.462
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.465
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.465.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.470
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.470.cold.1
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.466
+ ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.471
+ ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.547
+ ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.565
+ ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.487
+ ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.562
+ ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.531
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.534
+ ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.577
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.537
+ ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.559
+ ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.588
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.573
+ ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.574
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.522
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.580
+ ___block_literal_global.394
+ ___block_literal_global.400
+ ___block_literal_global.421
+ ___block_literal_global.424
+ ___block_literal_global.427
+ ___block_literal_global.430
+ ___block_literal_global.433
+ ___block_literal_global.435
+ ___block_literal_global.438
+ ___block_literal_global.441
+ ___block_literal_global.443
+ ___block_literal_global.450
+ ___block_literal_global.452
+ ___block_literal_global.455
+ ___block_literal_global.458
+ ___block_literal_global.461
+ ___block_literal_global.468
+ ___block_literal_global.473
+ ___block_literal_global.475
+ ___block_literal_global.481
+ ___block_literal_global.486
+ ___block_literal_global.489
+ ___block_literal_global.492
+ ___block_literal_global.495
+ ___block_literal_global.498
+ ___block_literal_global.501
+ ___block_literal_global.509
+ ___block_literal_global.512
+ ___block_literal_global.515
+ ___block_literal_global.518
+ ___block_literal_global.521
+ ___block_literal_global.524
+ ___block_literal_global.527
+ ___block_literal_global.530
+ ___block_literal_global.533
+ ___block_literal_global.536
+ ___block_literal_global.539
+ ___block_literal_global.546
+ ___block_literal_global.549
+ ___block_literal_global.552
+ ___block_literal_global.555
+ ___block_literal_global.558
+ ___block_literal_global.561
+ ___block_literal_global.564
+ ___block_literal_global.567
+ ___block_literal_global.576
+ ___block_literal_global.579
+ ___block_literal_global.582
+ ___block_literal_global.587
- GCC_except_table154
- GCC_except_table187
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.449
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.521
- ___40-[TransparencyDaemon ktRepair:complete:]_block_invoke.579
- ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.379
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke.539
- ___44-[TransparencyDaemon setOSVersion:complete:]_block_invoke_2.540
- ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.418
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.424
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.383
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.384
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.512
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.432
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.432.cold.1
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.435
- ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.387
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.495
- ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.421
- ___48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.546
- ___49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.549
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.478
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.480
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.440
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.442
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.442.cold.1
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.452
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.391
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.397
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.393
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.408
- ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.427
- ___55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.536
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.486
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.455
- ___58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.552
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.515
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.564
- ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2.566
- ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.492
- ___59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.472
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.524
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.489
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.509
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.506
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.458
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.461
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.461.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.466
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.466.cold.1
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.462
- ___61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.467
- ___63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.543
- ___63-[TransparencyDaemon successInfoForElement:samples:completion:]_block_invoke.561
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.483
- ___63-[TransparencyDaemon triggerReportAndMaybeOptInWithCompletion:]_block_invoke.558
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.527
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.530
- ___72-[TransparencyDaemon networkKTQuery:application:trace:timeout:complete:]_block_invoke.573
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.533
- ___73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.555
- ___74-[TransparencyDaemon validateIDSData:ktQueryData:ktResponseData:complete:]_block_invoke.584
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke.569
- ___76-[TransparencyDaemon networkKTQuery:application:traceUUID:timeout:complete:]_block_invoke_2.570
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.518
- ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.576
- ___block_literal_global.382
- ___block_literal_global.396
- ___block_literal_global.417
- ___block_literal_global.420
- ___block_literal_global.423
- ___block_literal_global.426
- ___block_literal_global.429
- ___block_literal_global.431
- ___block_literal_global.434
- ___block_literal_global.437
- ___block_literal_global.439
- ___block_literal_global.444
- ___block_literal_global.446
- ___block_literal_global.451
- ___block_literal_global.454
- ___block_literal_global.457
- ___block_literal_global.460
- ___block_literal_global.469
- ___block_literal_global.471
- ___block_literal_global.477
- ___block_literal_global.482
- ___block_literal_global.485
- ___block_literal_global.488
- ___block_literal_global.491
- ___block_literal_global.494
- ___block_literal_global.497
- ___block_literal_global.505
- ___block_literal_global.508
- ___block_literal_global.511
- ___block_literal_global.514
- ___block_literal_global.517
- ___block_literal_global.520
- ___block_literal_global.523
- ___block_literal_global.526
- ___block_literal_global.529
- ___block_literal_global.532
- ___block_literal_global.535
- ___block_literal_global.538
- ___block_literal_global.545
- ___block_literal_global.548
- ___block_literal_global.551
- ___block_literal_global.554
- ___block_literal_global.557
- ___block_literal_global.560
- ___block_literal_global.563
- ___block_literal_global.568
- ___block_literal_global.575
- ___block_literal_global.578
- ___block_literal_global.583
CStrings:
+ "\""
- "!"

```
