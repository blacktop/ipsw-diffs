## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/Versions/A/PowerlogHelperdOperators`

```diff

-2308.0.35.0.0
-  __TEXT.__text: 0xf7104
-  __TEXT.__auth_stubs: 0x1560
-  __TEXT.__objc_methlist: 0x7c8c
+2308.0.53.0.0
+  __TEXT.__text: 0xf7c6c
+  __TEXT.__auth_stubs: 0x1570
+  __TEXT.__objc_methlist: 0x7cb4
   __TEXT.__const: 0x2d4
-  __TEXT.__cstring: 0x13247
-  __TEXT.__oslogstring: 0x7a10
+  __TEXT.__cstring: 0x132ee
+  __TEXT.__oslogstring: 0x7b3c
   __TEXT.__gcc_except_tab: 0x1d84
-  __TEXT.__unwind_info: 0x1de8
+  __TEXT.__unwind_info: 0x1df8
   __TEXT.__objc_classname: 0x577
-  __TEXT.__objc_methname: 0x1b725
+  __TEXT.__objc_methname: 0x1b7ac
   __TEXT.__objc_methtype: 0x1970
-  __TEXT.__objc_stubs: 0x10e20
+  __TEXT.__objc_stubs: 0x10ea0
   __DATA_CONST.__got: 0x8c0
-  __DATA_CONST.__const: 0x2260
+  __DATA_CONST.__const: 0x2298
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_nlclslist: 0xa8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5750
+  __DATA_CONST.__objc_selrefs: 0x5770
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x1eb0
-  __AUTH_CONST.__auth_got: 0xac8
+  __AUTH_CONST.__auth_got: 0xad0
   __AUTH_CONST.__const: 0x25c8
-  __AUTH_CONST.__cfstring: 0x1d720
+  __AUTH_CONST.__cfstring: 0x1d800
   __AUTH_CONST.__objc_const: 0xa080
   __AUTH_CONST.__objc_doubleobj: 0x630
   __AUTH_CONST.__objc_intobj: 0x10f8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4181
-  Symbols:   10398
-  CStrings:  4065
+  Functions: 4192
+  Symbols:   10421
+  CStrings:  4073
 
Symbols:
+ +[PLBatteryAgent entryEventBackwardDefinitionChargingLimit]
+ -[PLBatteryAgent getGaugingMitigationDict]
+ -[PLBatteryAgent getGaugingMitigationDict].cold.1
+ -[PLBatteryAgent getGaugingMitigationDict].cold.2
+ -[PLBatteryAgent handleGaugingMitigationStateCallback:]
+ -[PLBatteryAgent handleGaugingMitigationStateCallback:].cold.1
+ -[PLBatteryAgent initOperatorDependancies].cold.5
+ -[PLBatteryAgent initOperatorDependancies].cold.6
+ -[PLBatteryAgent logEventBackwardChargingLimit]
+ -[PLBatteryAgent logEventBackwardChargingLimit].cold.1
+ GCC_except_table138
+ GCC_except_table144
+ GCC_except_table231
+ GCC_except_table236
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table247
+ GCC_except_table290
+ GCC_except_table296
+ GCC_except_table380
+ _IOPSGaugingMitigationGetState
+ __22-[PLBatteryAgent init]_block_invoke.3082
+ __22-[PLBatteryAgent init]_block_invoke.3082.cold.1
+ __22-[PLBatteryAgent init]_block_invoke.3082.cold.2
+ __22-[PLBatteryAgent init]_block_invoke.3082.cold.3
+ __22-[PLBatteryAgent init]_block_invoke.3082.cold.4
+ __22-[PLBatteryAgent init]_block_invoke.3082.cold.5
+ __22-[PLBatteryAgent init]_block_invoke.3082.cold.6
+ __22-[PLBatteryAgent init]_block_invoke.3088
+ __22-[PLBatteryAgent init]_block_invoke.3098
+ __22-[PLBatteryAgent init]_block_invoke.3101
+ __22-[PLBatteryAgent init]_block_invoke.3114
+ __22-[PLBatteryAgent init]_block_invoke.3117
+ __22-[PLBatteryAgent init]_block_invoke.3126
+ __22-[PLBatteryAgent init]_block_invoke.3132
+ __22-[PLBatteryAgent init]_block_invoke_2.3084
+ __22-[PLBatteryAgent init]_block_invoke_2.3139
+ __24-[PLBatteryAgent xFlags]_block_invoke.4409
+ __24-[PLBatteryAgent xFlags]_block_invoke.4418
+ __24-[PLBatteryAgent xFlags]_block_invoke.4427
+ __24-[PLBatteryAgent xFlags]_block_invoke.4436
+ __24-[PLBatteryAgent xFlags]_block_invoke.4442
+ __24-[PLBatteryAgent xFlags]_block_invoke.4448
+ __24-[PLBatteryAgent xFlags]_block_invoke.4454
+ __24-[PLBatteryAgent xFlags]_block_invoke.4463
+ __24-[PLBatteryAgent xFlags]_block_invoke.4469
+ __24-[PLBatteryAgent xFlags]_block_invoke.4475
+ __32-[PLBatteryAgent aggdTimerFired]_block_invoke.4129
+ __32-[PLBatteryAgent getIOPSDevices]_block_invoke.3243
+ __32-[PLBatteryAgent getIOPSDevices]_block_invoke.3249
+ __33-[PLBatteryAgent cancelEALogging]_block_invoke.3234
+ __35-[PLBatteryAgent handlePPMCallback]_block_invoke.3536
+ __36-[PLBatteryAgent logBaselineToAggD:]_block_invoke.4145
+ __40-[PLBatteryAgent logPortControllerInfo:]_block_invoke.4525
+ __40-[PLBatteryAgent logPortControllerInfo:]_block_invoke.4525.cold.1
+ __41-[PLBatteryAgent setupBatterySubsampling]_block_invoke.4488
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3323
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3323.cold.1
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3339
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3371
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3385
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3434
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3434.cold.1
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3434.cold.2
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3434.cold.3
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3448.cold.1
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3456
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3456.cold.1
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3465
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3469
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3474
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3480
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3487
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3487.cold.1
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3494
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3494.cold.1
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3503
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3525
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3324
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3369
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3388
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3457
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3477
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3488
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3495
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3527
+ __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4602
+ __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4602.cold.1
+ __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4602.cold.2
+ __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4610
+ __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.4604
+ __42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.3670
+ __43-[PLBatteryAgent logEventBackwardKioskMode]_block_invoke.3789
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4618
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4619
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4620
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4621
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4622
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4622.cold.1
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4625
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4625.cold.1
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4626
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4626.cold.1
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4669
+ __53-[PLBatteryAgent logEventBackwardBatteryWithRawData:]_block_invoke.3823
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4359
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4359.cold.1
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4364
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4364.cold.1
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4369
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4372
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4375
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4378
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4360
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4365
+ __59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3211
+ __59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3225
+ __block_literal_global.1803
+ __block_literal_global.1810
+ __block_literal_global.3070
+ __block_literal_global.3154
+ __block_literal_global.3167
+ __block_literal_global.3291
+ __block_literal_global.3342
+ __block_literal_global.3387
+ __block_literal_global.3406
+ __block_literal_global.3418
+ __block_literal_global.3529
+ __block_literal_global.3542
+ __block_literal_global.3838
+ __block_literal_global.4081
+ __block_literal_global.4097
+ __block_literal_global.4150
+ __block_literal_global.4587
+ __block_literal_global.4617
+ _kPLBatteryAgentEventBackwardNameChargingLimit
+ _kPLBatteryAgentStringLastDOD0Update
+ _kPLBatteryAgentStringLastFullChargeDate
+ _kPLBatteryAgentStringLastFullChargeReq
+ _kPLBatteryAgentStringLastQMaxUpdate
+ _kPLBatteryAgentStringLastQualQMaxDate
+ _kPLBatteryAgentStringLastQualQmaxDODValue
+ _objc_msgSend$entryEventBackwardDefinitionChargingLimit
+ _objc_msgSend$getGaugingMitigationDict
+ _objc_msgSend$handleGaugingMitigationStateCallback:
+ _objc_msgSend$logEventBackwardChargingLimit
+ cancelEALogging.classDebugEnabled.3233
+ cancelEALogging.defaultOnce.3232
+ getIOPSDevices.classDebugEnabled.3242
+ getIOPSDevices.classDebugEnabled.3248
+ getIOPSDevices.defaultOnce.3241
+ getIOPSDevices.defaultOnce.3247
+ handlePPMCallback.defaultOnce.3535
+ initOperatorDependancies.classDebugEnabled.3476
+ initOperatorDependancies.classDebugEnabled.3479
+ initOperatorDependancies.defaultOnce.3475
+ initOperatorDependancies.defaultOnce.3478
+ kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3116
+ kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3125
+ kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3087
+ kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3112
+ kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3115
+ kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3124
+ kPLBatteryAgentStringUserType_block_invoke.objectForKey.3113
+ kPLBatteryAgentStringUserType_block_invoke_11.classDebugEnabled.4609
+ kPLBatteryAgentStringUserType_block_invoke_11.defaultOnce.4608
+ kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3317
+ kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3316
+ logEventIntervalGasGauge.classDebugEnabled.3669
+ logEventIntervalGasGauge.defaultOnce.3668
+ logEventNoneBatteryConfigWithRawData:.classDebugEnabled.4377
+ logEventNoneBatteryConfigWithRawData:.defaultOnce.4376
+ setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3224
+ setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3223
+ xFlags.classDebugEnabled.4408
+ xFlags.classDebugEnabled.4417
+ xFlags.classDebugEnabled.4426
+ xFlags.classDebugEnabled.4435
+ xFlags.classDebugEnabled.4441
+ xFlags.classDebugEnabled.4447
+ xFlags.classDebugEnabled.4453
+ xFlags.classDebugEnabled.4462
+ xFlags.classDebugEnabled.4468
+ xFlags.classDebugEnabled.4474
+ xFlags.defaultOnce.4407
+ xFlags.defaultOnce.4416
+ xFlags.defaultOnce.4425
+ xFlags.defaultOnce.4434
+ xFlags.defaultOnce.4440
+ xFlags.defaultOnce.4446
+ xFlags.defaultOnce.4452
+ xFlags.defaultOnce.4461
+ xFlags.defaultOnce.4467
+ xFlags.defaultOnce.4473
- GCC_except_table137
- GCC_except_table143
- GCC_except_table232
- GCC_except_table233
- GCC_except_table238
- GCC_except_table239
- GCC_except_table286
- GCC_except_table288
- GCC_except_table375
- __22-[PLBatteryAgent init]_block_invoke.3061
- __22-[PLBatteryAgent init]_block_invoke.3061.cold.1
- __22-[PLBatteryAgent init]_block_invoke.3061.cold.2
- __22-[PLBatteryAgent init]_block_invoke.3061.cold.3
- __22-[PLBatteryAgent init]_block_invoke.3061.cold.4
- __22-[PLBatteryAgent init]_block_invoke.3061.cold.5
- __22-[PLBatteryAgent init]_block_invoke.3061.cold.6
- __22-[PLBatteryAgent init]_block_invoke.3067
- __22-[PLBatteryAgent init]_block_invoke.3077
- __22-[PLBatteryAgent init]_block_invoke.3080
- __22-[PLBatteryAgent init]_block_invoke.3093
- __22-[PLBatteryAgent init]_block_invoke.3096
- __22-[PLBatteryAgent init]_block_invoke.3105
- __22-[PLBatteryAgent init]_block_invoke.3111
- __22-[PLBatteryAgent init]_block_invoke_2.3063
- __22-[PLBatteryAgent init]_block_invoke_2.3118
- __24-[PLBatteryAgent xFlags]_block_invoke.4386
- __24-[PLBatteryAgent xFlags]_block_invoke.4395
- __24-[PLBatteryAgent xFlags]_block_invoke.4404
- __24-[PLBatteryAgent xFlags]_block_invoke.4413
- __24-[PLBatteryAgent xFlags]_block_invoke.4419
- __24-[PLBatteryAgent xFlags]_block_invoke.4425
- __24-[PLBatteryAgent xFlags]_block_invoke.4431
- __24-[PLBatteryAgent xFlags]_block_invoke.4440
- __24-[PLBatteryAgent xFlags]_block_invoke.4446
- __24-[PLBatteryAgent xFlags]_block_invoke.4452
- __32-[PLBatteryAgent aggdTimerFired]_block_invoke.4106
- __32-[PLBatteryAgent getIOPSDevices]_block_invoke.3222
- __32-[PLBatteryAgent getIOPSDevices]_block_invoke.3228
- __33-[PLBatteryAgent cancelEALogging]_block_invoke.3213
- __35-[PLBatteryAgent handlePPMCallback]_block_invoke.3513
- __36-[PLBatteryAgent logBaselineToAggD:]_block_invoke.4122
- __40-[PLBatteryAgent logPortControllerInfo:]_block_invoke.4502
- __40-[PLBatteryAgent logPortControllerInfo:]_block_invoke.4502.cold.1
- __41-[PLBatteryAgent setupBatterySubsampling]_block_invoke.4465
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3297
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3302
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3302.cold.1
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3350
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3364
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3413
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3413.cold.1
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3413.cold.2
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3413.cold.3
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3427
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3427.cold.1
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3435
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3435.cold.1
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3444
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3453
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3459
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3466
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3466.cold.1
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3473
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3473.cold.1
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3482
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3504
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3303
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3348
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3367
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3436
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3456
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3467
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3474
- __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4579
- __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4579.cold.1
- __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4579.cold.2
- __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4587
- __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.4581
- __42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.3647
- __43-[PLBatteryAgent logEventBackwardKioskMode]_block_invoke.3766
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4595
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4596
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4597
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4598
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4599
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4599.cold.1
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4602
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4602.cold.1
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4603
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4603.cold.1
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4646
- __53-[PLBatteryAgent logEventBackwardBatteryWithRawData:]_block_invoke.3800
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4329
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4332
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4336
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4336.cold.1
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4341
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4341.cold.1
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4346
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4349
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4337
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4342
- __59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3190
- __59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3204
- __block_literal_global.1789
- __block_literal_global.3049
- __block_literal_global.3133
- __block_literal_global.3146
- __block_literal_global.3270
- __block_literal_global.3321
- __block_literal_global.3366
- __block_literal_global.3376
- __block_literal_global.3385
- __block_literal_global.3506
- __block_literal_global.3519
- __block_literal_global.3815
- __block_literal_global.4058
- __block_literal_global.4074
- __block_literal_global.4127
- __block_literal_global.4564
- __block_literal_global.4594
- cancelEALogging.classDebugEnabled.3212
- cancelEALogging.defaultOnce.3211
- getIOPSDevices.classDebugEnabled.3221
- getIOPSDevices.classDebugEnabled.3227
- getIOPSDevices.defaultOnce.3220
- getIOPSDevices.defaultOnce.3226
- handlePPMCallback.defaultOnce.3512
- initOperatorDependancies.classDebugEnabled.3455
- initOperatorDependancies.classDebugEnabled.3458
- initOperatorDependancies.defaultOnce.3454
- initOperatorDependancies.defaultOnce.3457
- kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3095
- kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3104
- kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3066
- kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3091
- kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3094
- kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3103
- kPLBatteryAgentStringUserType_block_invoke.objectForKey.3092
- kPLBatteryAgentStringUserType_block_invoke_11.classDebugEnabled.4586
- kPLBatteryAgentStringUserType_block_invoke_11.defaultOnce.4585
- kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3296
- kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3295
- logEventIntervalGasGauge.classDebugEnabled.3646
- logEventIntervalGasGauge.defaultOnce.3645
- logEventNoneBatteryConfigWithRawData:.classDebugEnabled.4354
- logEventNoneBatteryConfigWithRawData:.defaultOnce.4353
- setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3203
- setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3202
- xFlags.classDebugEnabled.4385
- xFlags.classDebugEnabled.4394
- xFlags.classDebugEnabled.4403
- xFlags.classDebugEnabled.4412
- xFlags.classDebugEnabled.4418
- xFlags.classDebugEnabled.4424
- xFlags.classDebugEnabled.4430
- xFlags.classDebugEnabled.4439
- xFlags.classDebugEnabled.4445
- xFlags.classDebugEnabled.4451
- xFlags.defaultOnce.4384
- xFlags.defaultOnce.4393
- xFlags.defaultOnce.4402
- xFlags.defaultOnce.4411
- xFlags.defaultOnce.4417
- xFlags.defaultOnce.4423
- xFlags.defaultOnce.4429
- xFlags.defaultOnce.4438
- xFlags.defaultOnce.4444
- xFlags.defaultOnce.4450
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLProcessNetworkAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLLocationAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLApplicationAgentMac.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPushAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLUtilities.m"
+ "ChargingLimit"
+ "com.apple.system.powersources.gaugingmitigation"
+ "lastDOD0Update"
+ "lastFullChargeDate"
+ "lastFullChargeReq"
+ "lastQMaxUpdate"
+ "lastQualQMaxDate"
+ "lastQualQmaxDODValue"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLProcessNetworkAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLLocationAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLApplicationAgentMac.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPushAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLUtilities.m"

```
