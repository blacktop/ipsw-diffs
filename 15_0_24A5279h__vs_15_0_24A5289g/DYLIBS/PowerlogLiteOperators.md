## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/Versions/A/PowerlogLiteOperators`

```diff

-2308.0.35.0.0
-  __TEXT.__text: 0x1fe878
-  __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0xbbd8
+2308.0.53.0.0
+  __TEXT.__text: 0x1ff42c
+  __TEXT.__auth_stubs: 0x2420
+  __TEXT.__objc_methlist: 0xbc38
   __TEXT.__const: 0xd60
   __TEXT.__swift5_typeref: 0x33e
   __TEXT.__constg_swiftt: 0x1ac
   __TEXT.__swift5_reflstr: 0x179
   __TEXT.__swift5_fieldmd: 0x200
-  __TEXT.__cstring: 0x58230
+  __TEXT.__cstring: 0x58302
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x20
-  __TEXT.__oslogstring: 0x84eb
+  __TEXT.__oslogstring: 0x8617
   __TEXT.__swift5_capture: 0x80
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
   __TEXT.__gcc_except_tab: 0x20cc
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x2ec0
+  __TEXT.__unwind_info: 0x2ec8
   __TEXT.__eh_frame: 0x620
   __TEXT.__objc_classname: 0x693
-  __TEXT.__objc_methname: 0x27685
+  __TEXT.__objc_methname: 0x277fd
   __TEXT.__objc_methtype: 0x18ae
-  __TEXT.__objc_stubs: 0x17820
+  __TEXT.__objc_stubs: 0x178c0
   __DATA_CONST.__got: 0xba0
-  __DATA_CONST.__const: 0x3630
+  __DATA_CONST.__const: 0x3670
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_nlclslist: 0x178
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c00
+  __DATA_CONST.__objc_selrefs: 0x7c40
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x5ad0
-  __AUTH_CONST.__auth_got: 0x1220
+  __AUTH_CONST.__auth_got: 0x1228
   __AUTH_CONST.__auth_ptr: 0x260
   __AUTH_CONST.__const: 0x2e08
-  __AUTH_CONST.__cfstring: 0x47c80
-  __AUTH_CONST.__objc_const: 0xd5b8
+  __AUTH_CONST.__cfstring: 0x47d80
+  __AUTH_CONST.__objc_const: 0xd5e8
   __AUTH_CONST.__objc_intobj: 0x4b60
   __AUTH_CONST.__objc_dictobj: 0x22b0
   __AUTH_CONST.__objc_arrayobj: 0xea0
-  __AUTH_CONST.__objc_doubleobj: 0xbb0
+  __AUTH_CONST.__objc_doubleobj: 0xba0
   __AUTH.__objc_data: 0xba0
   __AUTH.__data: 0xae8
-  __DATA.__objc_ivar: 0xd30
+  __DATA.__objc_ivar: 0xd34
   __DATA.__data: 0x518
   __DATA.__bss: 0x2740
   __DATA.__common: 0x180

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5706
-  Symbols:   12177
-  CStrings:  12822
+  Functions: 5715
+  Symbols:   12200
+  CStrings:  12832
 
Symbols:
+ +[PLAudioAgent entryEventForwardDefinitionHapticsPrewarmCount]
+ +[PLBatteryAgent entryEventBackwardDefinitionChargingLimit]
+ -[PLAudioAgent hapticsPrewarmCountListener]
+ -[PLAudioAgent logEventForwardHapticsPrewarmCount:]
+ -[PLAudioAgent setHapticsPrewarmCountListener:]
+ -[PLBatteryAgent getGaugingMitigationDict]
+ -[PLBatteryAgent handleGaugingMitigationStateCallback:]
+ -[PLBatteryAgent logEventBackwardChargingLimit]
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table225
+ GCC_except_table230
+ GCC_except_table235
+ GCC_except_table236
+ GCC_except_table241
+ GCC_except_table282
+ GCC_except_table288
+ GCC_except_table370
+ _IOPSGaugingMitigationGetState
+ __22-[PLBatteryAgent init]_block_invoke.3082
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
+ __29-[PLWifiAgent findWifiDevice]_block_invoke.632
+ __29-[PLWifiAgent findWifiDevice]_block_invoke.638
+ __29-[PLWifiAgent findWifiDevice]_block_invoke.644
+ __29-[PLWifiAgent findWifiDevice]_block_invoke.650
+ __32-[PLBatteryAgent aggdTimerFired]_block_invoke.4129
+ __32-[PLBatteryAgent getIOPSDevices]_block_invoke.3243
+ __32-[PLBatteryAgent getIOPSDevices]_block_invoke.3249
+ __33-[PLBatteryAgent cancelEALogging]_block_invoke.3234
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.769
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.775
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.811
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.827
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.839
+ __33-[PLWifiAgent setWiFiAWDLDevice:]_block_invoke.620
+ __35-[PLBatteryAgent handlePPMCallback]_block_invoke.3536
+ __36-[PLBatteryAgent logBaselineToAggD:]_block_invoke.4145
+ __36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.1282
+ __39-[PLAudioAgent setupAVSystemController]_block_invoke.135
+ __39-[PLAudioAgent setupAVSystemController]_block_invoke.139
+ __39-[PLWifiAgent initOperatorDependancies]_block_invoke.679
+ __39-[PLWifiAgent initOperatorDependancies]_block_invoke.687
+ __39-[PLWifiAgent initOperatorDependancies]_block_invoke.699
+ __39-[PLWifiAgent initOperatorDependancies]_block_invoke.716
+ __39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.680
+ __39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.691
+ __40-[PLBatteryAgent logPortControllerInfo:]_block_invoke.4525
+ __40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.993
+ __41-[PLBatteryAgent setupBatterySubsampling]_block_invoke.4488
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3323
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3339
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3371
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3385
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3434
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3456
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3465
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3469
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3474
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3480
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3487
+ __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3494
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
+ __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4610
+ __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.4604
+ __42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.3670
+ __43-[PLBatteryAgent logEventBackwardKioskMode]_block_invoke.3789
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4618
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4619
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4620
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4621
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4622
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4625
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4626
+ __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4669
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1014
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1020
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1026
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1032
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1038
+ __51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.753
+ __53-[PLBatteryAgent logEventBackwardBatteryWithRawData:]_block_invoke.3823
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4359
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4364
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4369
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4372
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4375
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4378
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4360
+ __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4365
+ __55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.945
+ __55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.954
+ __56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.981
+ __57-[AudioDevice handleAudioDevicePropertyChange:addresses:]_block_invoke.430
+ __59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3211
+ __59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3225
+ __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.867
+ __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.873
+ __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.936
+ __71-[PLWifiAgent logEventBackwardWifiPropertiesMac:withNetworkProperties:]_block_invoke.1056
+ __71-[PLWifiAgent logEventBackwardWifiPropertiesMac:withNetworkProperties:]_block_invoke.1205
+ __78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.747
+ __block_literal_global.1803
+ __block_literal_global.1810
+ __block_literal_global.212
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
+ __block_literal_global.742
+ _kPLAudioAgentEventForwardNameHapticsPrewarmCount
+ _kPLBatteryAgentEventBackwardNameChargingLimit
+ _kPLBatteryAgentStringLastDOD0Update
+ _kPLBatteryAgentStringLastFullChargeDate
+ _kPLBatteryAgentStringLastFullChargeReq
+ _kPLBatteryAgentStringLastQMaxUpdate
+ _kPLBatteryAgentStringLastQualQMaxDate
+ _kPLBatteryAgentStringLastQualQmaxDODValue
+ _objc_msgSend$entryEventBackwardDefinitionChargingLimit
+ _objc_msgSend$entryEventForwardDefinitionHapticsPrewarmCount
+ _objc_msgSend$getGaugingMitigationDict
+ _objc_msgSend$handleGaugingMitigationStateCallback:
+ _objc_msgSend$logEventBackwardChargingLimit
- GCC_except_table133
- GCC_except_table217
- GCC_except_table226
- GCC_except_table227
- GCC_except_table232
- GCC_except_table233
- GCC_except_table278
- GCC_except_table280
- GCC_except_table365
- __22-[PLBatteryAgent init]_block_invoke.3061
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
- __29-[PLWifiAgent findWifiDevice]_block_invoke.634
- __29-[PLWifiAgent findWifiDevice]_block_invoke.640
- __29-[PLWifiAgent findWifiDevice]_block_invoke.646
- __29-[PLWifiAgent findWifiDevice]_block_invoke.652
- __32-[PLBatteryAgent aggdTimerFired]_block_invoke.4106
- __32-[PLBatteryAgent getIOPSDevices]_block_invoke.3222
- __32-[PLBatteryAgent getIOPSDevices]_block_invoke.3228
- __33-[PLBatteryAgent cancelEALogging]_block_invoke.3213
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.771
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.777
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.813
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.829
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.841
- __33-[PLWifiAgent setWiFiAWDLDevice:]_block_invoke.622
- __35-[PLBatteryAgent handlePPMCallback]_block_invoke.3513
- __36-[PLBatteryAgent logBaselineToAggD:]_block_invoke.4122
- __36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.1284
- __39-[PLAudioAgent setupAVSystemController]_block_invoke.132
- __39-[PLAudioAgent setupAVSystemController]_block_invoke.136
- __39-[PLWifiAgent initOperatorDependancies]_block_invoke.681
- __39-[PLWifiAgent initOperatorDependancies]_block_invoke.689
- __39-[PLWifiAgent initOperatorDependancies]_block_invoke.701
- __39-[PLWifiAgent initOperatorDependancies]_block_invoke.718
- __39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.682
- __39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.693
- __40-[PLBatteryAgent logPortControllerInfo:]_block_invoke.4502
- __40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.995
- __41-[PLBatteryAgent setupBatterySubsampling]_block_invoke.4465
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3297
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3302
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3350
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3364
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3413
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3427
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3435
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3444
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3453
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3459
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3466
- __42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3473
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
- __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4587
- __42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.4581
- __42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.3647
- __43-[PLBatteryAgent logEventBackwardKioskMode]_block_invoke.3766
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4595
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4596
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4597
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4598
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4599
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4602
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4603
- __45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4646
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1016
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1022
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1028
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1034
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1040
- __51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.755
- __53-[PLBatteryAgent logEventBackwardBatteryWithRawData:]_block_invoke.3800
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4329
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4332
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4336
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4341
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4346
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4349
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4337
- __55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4342
- __55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.947
- __55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.956
- __56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.983
- __57-[AudioDevice handleAudioDevicePropertyChange:addresses:]_block_invoke.420
- __59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3190
- __59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3204
- __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.869
- __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.875
- __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.938
- __71-[PLWifiAgent logEventBackwardWifiPropertiesMac:withNetworkProperties:]_block_invoke.1058
- __71-[PLWifiAgent logEventBackwardWifiPropertiesMac:withNetworkProperties:]_block_invoke.1207
- __78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.749
- __block_literal_global.1789
- __block_literal_global.209
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
- __block_literal_global.744
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLButtonAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLIOReportAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLIOReportAgentIOReportStats.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLMacCPUGPUAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLPeripheralAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLVideoAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLIdentityServicesAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLNetworkAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLProcessNetworkAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLBluetoothAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLLocationAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLWifiAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLApplicationAgentMac.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLConfigAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLFSEventAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLHomeKitAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLMDNSAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPerformanceAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPowerAssertionAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPushAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScheduledWakeAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLWindowServerAgent.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDebugService.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetService.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetServiceDAS.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLTestService.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
+ "ChargingLimit"
+ "HapticsPrewarmCount"
+ "MulticastRxBytes"
+ "bandsUeccCrossTempHisto"
+ "com.apple.system.powersources.gaugingmitigation"
+ "lastDOD0Update"
+ "lastFullChargeDate"
+ "lastFullChargeReq"
+ "lastQMaxUpdate"
+ "lastQualQMaxDate"
+ "lastQualQmaxDODValue"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLButtonAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLIOReportAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLIOReportAgentIOReportStats.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLMacCPUGPUAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLPeripheralAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLVideoAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLIdentityServicesAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLNetworkAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLProcessNetworkAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLBluetoothAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLLocationAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLWifiAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLApplicationAgentMac.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLConfigAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLFSEventAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLHomeKitAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLMDNSAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPerformanceAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPowerAssertionAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPushAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScheduledWakeAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLWindowServerAgent.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDebugService.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetService.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetServiceDAS.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLTestService.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
- "MulticastRxKBytes"

```
