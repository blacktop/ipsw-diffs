## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

 2964.2.4.0.0
-  __TEXT.__text: 0x1bd948
-  __TEXT.__auth_stubs: 0x1b80
-  __TEXT.__objc_methlist: 0xea90
+  __TEXT.__text: 0x1be62c
+  __TEXT.__auth_stubs: 0x1b90
+  __TEXT.__objc_methlist: 0xeaa8
   __TEXT.__const: 0x6a8
-  __TEXT.__cstring: 0x22f2f
-  __TEXT.__oslogstring: 0x1268e
+  __TEXT.__cstring: 0x231c8
+  __TEXT.__oslogstring: 0x1271f
   __TEXT.__gcc_except_tab: 0x2728
   __TEXT.__ustring: 0x10
   __TEXT.__unwind_info: 0x36f8
   __TEXT.__objc_classname: 0xc05
-  __TEXT.__objc_methname: 0x31432
+  __TEXT.__objc_methname: 0x31488
   __TEXT.__objc_methtype: 0x27d0
-  __TEXT.__objc_stubs: 0x1eae0
+  __TEXT.__objc_stubs: 0x1eb20
   __DATA_CONST.__got: 0xea0
-  __DATA_CONST.__const: 0x43b0
+  __DATA_CONST.__const: 0x43d0
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x98b8
+  __DATA_CONST.__objc_selrefs: 0x98c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x14990
-  __AUTH_CONST.__auth_got: 0xdd8
+  __AUTH_CONST.__auth_got: 0xde0
   __AUTH_CONST.__const: 0x1860
-  __AUTH_CONST.__cfstring: 0x30c40
+  __AUTH_CONST.__cfstring: 0x31100
   __AUTH_CONST.__objc_const: 0x12848
   __AUTH_CONST.__objc_intobj: 0x2778
   __AUTH_CONST.__objc_dictobj: 0x3430

   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
+  - /System/Library/PrivateFrameworks/Centauri.framework/Centauri
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 016A520B-CB3A-3CDF-AC67-A9A1E1D4B35E
-  Functions: 7806
-  Symbols:   26432
-  CStrings:  22179
+  UUID: C7A0887A-9F1A-3028-870E-485F5FDE1A4A
+  Functions: 7812
+  Symbols:   26451
+  CStrings:  22261
 
Symbols:
+ +[PLWifiAgent entryEventBackwardDefinitionControlCPUPowerStats]
+ -[PLWifiAgent logEventBackwardControlCPUPowerStats]
+ -[PLWifiAgent logEventBackwardControlCPUPowerStats].cold.1
+ -[PLWifiAgent logEventBackwardControlCPUPowerStats].cold.2
+ -[PLWifiAgent logEventForwardModuleInfo].cold.5
+ -[PLWifiAgent logEventForwardModuleInfo].cold.6
+ GCC_except_table47
+ _CENGetPowerStats
+ ___22-[PLBatteryAgent init]_block_invoke.3352
+ ___22-[PLBatteryAgent init]_block_invoke.3356
+ ___22-[PLBatteryAgent init]_block_invoke_2.3378
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5105
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5114
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5123
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5132
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5138
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5144
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5150
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5159
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5165
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5171
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.878
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.884
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.890
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.896
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.902
+ ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2685
+ ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2688
+ ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4792
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3476
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3482
+ ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3467
+ ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5184
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1021
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1027
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1066
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1082
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.1094
+ ___33-[PLWifiAgent setWiFiAWDLDevice:]_block_invoke.866
+ ___36-[PLWifiAgent setWiFiHotspotDevice:]_block_invoke.857
+ ___36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.2622
+ ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3845
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.934
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.942
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.942.cold.1
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.950
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.950.cold.1
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.951
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.959
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.959.cold.1
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.972
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.972.cold.1
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.935
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.935.cold.1
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.946
+ ___40-[PLWifiAgent logEventForwardAWDLState:]_block_invoke.1289
+ ___40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1248
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4180
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4187
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4183
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4190
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3554
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3560
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3560.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3576
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3609
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3669
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3669.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3669.cold.2
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3669.cold.3
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3686
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3686.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3697
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3701
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3701.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3709
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3709.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3716
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3725
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3731
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3738
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3738.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3745
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3745.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3759
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3759.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3764
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3764.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3771
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3794
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3836
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3561
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3606
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3621
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3693
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3710
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3720
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3728
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3739
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3746
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3802
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3810
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3818
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3822
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3826
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_7.3830
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5335
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5335.cold.1
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5335.cold.2
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5343
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5337
+ ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.4051
+ ___43-[PLWifiAgent logEventForwardHotspotState:]_block_invoke.1298
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5375
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5375.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5376
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5376.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5377
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5377.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5418
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1343
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1349
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1357
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1363
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5360
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5361
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5365
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5365.cold.1
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5365.cold.2
+ ___51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.1005
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5048
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5048.cold.1
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5052
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5052.cold.1
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5057
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5061
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5053
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5058
+ ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1200
+ ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1209
+ ___56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.1236
+ ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3447
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1122
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1128
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1191
+ ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4443
+ ___75-[PLBatteryAgent showOrHideTLCNotification:meetsTLCNotificationConditions:]_block_invoke.3419
+ ___78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.999
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2505
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2517
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2526
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2532
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2538
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2544
+ ___block_literal_global.3393
+ ___block_literal_global.3406
+ ___block_literal_global.3421
+ ___block_literal_global.3522
+ ___block_literal_global.3579
+ ___block_literal_global.3623
+ ___block_literal_global.3632
+ ___block_literal_global.3641
+ ___block_literal_global.3653
+ ___block_literal_global.3766
+ ___block_literal_global.3838
+ ___block_literal_global.3844
+ ___block_literal_global.3854
+ ___block_literal_global.4495
+ ___block_literal_global.4748
+ ___block_literal_global.4760
+ ___block_literal_global.4810
+ ___block_literal_global.5309
+ ___block_literal_global.5370
+ ___block_literal_global.752
+ ___block_literal_global.757
+ ___block_literal_global.770
+ ___block_literal_global.961
+ ___block_literal_global.969
+ _cancelEALogging.classDebugEnabled.3466
+ _cancelEALogging.defaultOnce.3465
+ _findWifiDevice.classDebugEnabled.877
+ _findWifiDevice.classDebugEnabled.883
+ _findWifiDevice.classDebugEnabled.889
+ _findWifiDevice.classDebugEnabled.895
+ _findWifiDevice.classDebugEnabled.901
+ _findWifiDevice.defaultOnce.876
+ _findWifiDevice.defaultOnce.882
+ _findWifiDevice.defaultOnce.888
+ _findWifiDevice.defaultOnce.894
+ _findWifiDevice.defaultOnce.900
+ _getIOPSDevices.classDebugEnabled.3475
+ _getIOPSDevices.classDebugEnabled.3481
+ _getIOPSDevices.defaultOnce.3474
+ _getIOPSDevices.defaultOnce.3480
+ _initOperatorDependancies.classDebugEnabled.3719
+ _initOperatorDependancies.classDebugEnabled.3730
+ _initOperatorDependancies.defaultOnce.3718
+ _initOperatorDependancies.defaultOnce.3729
+ _kPLBB24B
+ _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3351
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3350
+ _kPLBatteryAgentStringUserType_block_invoke_12.classDebugEnabled.5342
+ _kPLBatteryAgentStringUserType_block_invoke_12.defaultOnce.5341
+ _kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3553
+ _kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3552
+ _kPLWifiAgentEventBackwardNameControlCPUPowerStats
+ _kPLWifiAgentEventForwardWifiAssist_block_invoke_4.classDebugEnabled.1004
+ _kPLWifiAgentEventForwardWifiAssist_block_invoke_4.defaultOnce.1003
+ _logEventBackwardHeatMap.classDebugEnabled.4182
+ _logEventBackwardHeatMap.classDebugEnabled.4189
+ _logEventBackwardHeatMap.defaultOnce.4181
+ _logEventBackwardHeatMap.defaultOnce.4188
+ _logEventBackwardWifiProperties:.classDebugEnabled.1342
+ _logEventBackwardWifiProperties:.classDebugEnabled.1348
+ _logEventBackwardWifiProperties:.classDebugEnabled.1356
+ _logEventBackwardWifiProperties:.classDebugEnabled.1362
+ _logEventBackwardWifiProperties:.defaultOnce.1341
+ _logEventBackwardWifiProperties:.defaultOnce.1347
+ _logEventBackwardWifiProperties:.defaultOnce.1355
+ _logEventBackwardWifiProperties:.defaultOnce.1361
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2504
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2516
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2525
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2531
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2537
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2543
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2503
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2515
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2524
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2530
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2536
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2542
+ _logEventForwardAWDLState:.classDebugEnabled.1288
+ _logEventForwardAWDLState:.defaultOnce.1287
+ _logEventForwardHotspotState:.classDebugEnabled.1297
+ _logEventForwardHotspotState:.defaultOnce.1296
+ _logEventForwardModuleInfo.classDebugEnabled.1247
+ _logEventForwardModuleInfo.defaultOnce.1246
+ _logEventIntervalGasGauge.classDebugEnabled.4050
+ _logEventIntervalGasGauge.defaultOnce.4049
+ _logEventNoneBatteryConfigWithRawData:.classDebugEnabled.5060
+ _logEventNoneBatteryConfigWithRawData:.defaultOnce.5059
+ _logEventPointWake:.classDebugEnabled.1020
+ _logEventPointWake:.classDebugEnabled.1026
+ _logEventPointWake:.classDebugEnabled.1065
+ _logEventPointWake:.classDebugEnabled.1081
+ _logEventPointWake:.classDebugEnabled.1093
+ _logEventPointWake:.defaultOnce.1019
+ _logEventPointWake:.defaultOnce.1025
+ _logEventPointWake:.defaultOnce.1064
+ _logEventPointWake:.defaultOnce.1080
+ _logEventPointWake:.defaultOnce.1092
+ _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.1121
+ _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.1127
+ _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.1190
+ _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.1120
+ _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.1126
+ _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.1189
+ _logEventPointWakeLink:withParams:toEntry:.classDebugEnabled.1235
+ _logEventPointWakeLink:withParams:toEntry:.defaultOnce.1234
+ _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1199
+ _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1208
+ _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1198
+ _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1207
+ _modelWiFiPower:.classDebugEnabled.2684
+ _modelWiFiPower:.classDebugEnabled.2687
+ _modelWiFiPower:.defaultOnce.2683
+ _modelWiFiPower:.defaultOnce.2686
+ _objc_msgSend$entryEventBackwardDefinitionControlCPUPowerStats
+ _objc_msgSend$logEventBackwardControlCPUPowerStats
+ _setWiFiAWDLDevice:.classDebugEnabled.865
+ _setWiFiAWDLDevice:.defaultOnce.864
+ _setWiFiHotspotDevice:.classDebugEnabled.856
+ _setWiFiHotspotDevice:.defaultOnce.855
+ _setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3458
+ _setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3457
+ _wifiManufacturerQuery.classDebugEnabled.2621
+ _wifiManufacturerQuery.defaultOnce.2620
+ _xFlags.classDebugEnabled.5104
+ _xFlags.classDebugEnabled.5113
+ _xFlags.classDebugEnabled.5122
+ _xFlags.classDebugEnabled.5131
+ _xFlags.classDebugEnabled.5137
+ _xFlags.classDebugEnabled.5143
+ _xFlags.classDebugEnabled.5149
+ _xFlags.classDebugEnabled.5158
+ _xFlags.classDebugEnabled.5164
+ _xFlags.classDebugEnabled.5170
+ _xFlags.defaultOnce.5103
+ _xFlags.defaultOnce.5112
+ _xFlags.defaultOnce.5121
+ _xFlags.defaultOnce.5130
+ _xFlags.defaultOnce.5136
+ _xFlags.defaultOnce.5142
+ _xFlags.defaultOnce.5148
+ _xFlags.defaultOnce.5157
+ _xFlags.defaultOnce.5163
+ _xFlags.defaultOnce.5169
- GCC_except_table36
- ___22-[PLBatteryAgent init]_block_invoke.3349
- ___22-[PLBatteryAgent init]_block_invoke.3353
- ___22-[PLBatteryAgent init]_block_invoke_2.3375
- ___24-[PLBatteryAgent xFlags]_block_invoke.5102
- ___24-[PLBatteryAgent xFlags]_block_invoke.5111
- ___24-[PLBatteryAgent xFlags]_block_invoke.5120
- ___24-[PLBatteryAgent xFlags]_block_invoke.5129
- ___24-[PLBatteryAgent xFlags]_block_invoke.5135
- ___24-[PLBatteryAgent xFlags]_block_invoke.5141
- ___24-[PLBatteryAgent xFlags]_block_invoke.5147
- ___24-[PLBatteryAgent xFlags]_block_invoke.5156
- ___24-[PLBatteryAgent xFlags]_block_invoke.5162
- ___24-[PLBatteryAgent xFlags]_block_invoke.5168
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.776
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.782
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.788
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.794
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.800
- ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2577
- ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2580
- ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4789
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3473
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3479
- ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3464
- ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5181
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.919
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.925
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.964
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.980
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.992
- ___33-[PLWifiAgent setWiFiAWDLDevice:]_block_invoke.764
- ___36-[PLWifiAgent setWiFiHotspotDevice:]_block_invoke.755
- ___36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.2511
- ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3842
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.832
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.840
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.840.cold.1
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.848
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.848.cold.1
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.849
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.857
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.857.cold.1
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.870
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.870.cold.1
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.833
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.833.cold.1
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.844
- ___40-[PLWifiAgent logEventForwardAWDLState:]_block_invoke.1178
- ___40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1146
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4177
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4184
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4180
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4187
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3551
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3557
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3557.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3573
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3606
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3666
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3666.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3666.cold.2
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3666.cold.3
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3683
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3683.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3694
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3698
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3698.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3706
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3706.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3713
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3722
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3728
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3735
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3735.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3742
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3742.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3756
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3756.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3761
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3761.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3768
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3791
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3833
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3558
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3603
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3618
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3690
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3707
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3717
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3725
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3736
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3743
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3799
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3807
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3815
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3819
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3823
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_7.3827
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5332
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5332.cold.1
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5332.cold.2
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5340
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5334
- ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.4048
- ___43-[PLWifiAgent logEventForwardHotspotState:]_block_invoke.1187
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5368
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5369
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5370
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5372.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5373.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5374.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5415
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1232
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1238
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1246
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1252
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5357
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5358
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5362
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5362.cold.1
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5362.cold.2
- ___51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.903
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5045
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5045.cold.1
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5049
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5049.cold.1
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5054
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5058
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5050
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5055
- ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1098
- ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1107
- ___56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.1134
- ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3444
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1020
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1026
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1089
- ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4440
- ___75-[PLBatteryAgent showOrHideTLCNotification:meetsTLCNotificationConditions:]_block_invoke.3416
- ___78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.897
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2394
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2406
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2415
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2421
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2427
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2433
- ___block_literal_global.3390
- ___block_literal_global.3403
- ___block_literal_global.3418
- ___block_literal_global.3519
- ___block_literal_global.3576
- ___block_literal_global.3620
- ___block_literal_global.3629
- ___block_literal_global.3638
- ___block_literal_global.3650
- ___block_literal_global.3763
- ___block_literal_global.3835
- ___block_literal_global.3841
- ___block_literal_global.3851
- ___block_literal_global.4492
- ___block_literal_global.4745
- ___block_literal_global.4757
- ___block_literal_global.4807
- ___block_literal_global.5306
- ___block_literal_global.5367
- ___block_literal_global.749
- ___block_literal_global.751
- ___block_literal_global.758
- ___block_literal_global.859
- ___block_literal_global.966
- _cancelEALogging.classDebugEnabled.3463
- _cancelEALogging.defaultOnce.3462
- _findWifiDevice.classDebugEnabled.775
- _findWifiDevice.classDebugEnabled.781
- _findWifiDevice.classDebugEnabled.787
- _findWifiDevice.classDebugEnabled.793
- _findWifiDevice.classDebugEnabled.799
- _findWifiDevice.defaultOnce.774
- _findWifiDevice.defaultOnce.780
- _findWifiDevice.defaultOnce.786
- _findWifiDevice.defaultOnce.792
- _findWifiDevice.defaultOnce.798
- _getIOPSDevices.classDebugEnabled.3472
- _getIOPSDevices.classDebugEnabled.3478
- _getIOPSDevices.defaultOnce.3471
- _getIOPSDevices.defaultOnce.3477
- _initOperatorDependancies.classDebugEnabled.3716
- _initOperatorDependancies.classDebugEnabled.3724
- _initOperatorDependancies.defaultOnce.3715
- _initOperatorDependancies.defaultOnce.3723
- _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3348
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3347
- _kPLBatteryAgentStringUserType_block_invoke_12.classDebugEnabled.5339
- _kPLBatteryAgentStringUserType_block_invoke_12.defaultOnce.5338
- _kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3550
- _kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3549
- _kPLWifiAgentEventForwardWifiAssist_block_invoke_4.classDebugEnabled.902
- _kPLWifiAgentEventForwardWifiAssist_block_invoke_4.defaultOnce.901
- _logEventBackwardHeatMap.classDebugEnabled.4179
- _logEventBackwardHeatMap.classDebugEnabled.4186
- _logEventBackwardHeatMap.defaultOnce.4178
- _logEventBackwardHeatMap.defaultOnce.4185
- _logEventBackwardWifiProperties:.classDebugEnabled.1231
- _logEventBackwardWifiProperties:.classDebugEnabled.1237
- _logEventBackwardWifiProperties:.classDebugEnabled.1245
- _logEventBackwardWifiProperties:.classDebugEnabled.1251
- _logEventBackwardWifiProperties:.defaultOnce.1230
- _logEventBackwardWifiProperties:.defaultOnce.1236
- _logEventBackwardWifiProperties:.defaultOnce.1244
- _logEventBackwardWifiProperties:.defaultOnce.1250
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2393
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2405
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2414
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2420
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2426
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2432
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2392
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2404
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2413
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2419
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2425
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2431
- _logEventForwardAWDLState:.classDebugEnabled.1177
- _logEventForwardAWDLState:.defaultOnce.1176
- _logEventForwardHotspotState:.classDebugEnabled.1186
- _logEventForwardHotspotState:.defaultOnce.1185
- _logEventForwardModuleInfo.classDebugEnabled.1145
- _logEventForwardModuleInfo.defaultOnce.1144
- _logEventIntervalGasGauge.classDebugEnabled.4047
- _logEventIntervalGasGauge.defaultOnce.4046
- _logEventNoneBatteryConfigWithRawData:.classDebugEnabled.5057
- _logEventNoneBatteryConfigWithRawData:.defaultOnce.5056
- _logEventPointWake:.classDebugEnabled.918
- _logEventPointWake:.classDebugEnabled.924
- _logEventPointWake:.classDebugEnabled.963
- _logEventPointWake:.classDebugEnabled.979
- _logEventPointWake:.classDebugEnabled.991
- _logEventPointWake:.defaultOnce.917
- _logEventPointWake:.defaultOnce.923
- _logEventPointWake:.defaultOnce.962
- _logEventPointWake:.defaultOnce.978
- _logEventPointWake:.defaultOnce.990
- _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.1019
- _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.1025
- _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.1088
- _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.1018
- _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.1024
- _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.1087
- _logEventPointWakeLink:withParams:toEntry:.classDebugEnabled.1133
- _logEventPointWakeLink:withParams:toEntry:.defaultOnce.1132
- _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1097
- _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1106
- _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1096
- _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1105
- _modelWiFiPower:.classDebugEnabled.2576
- _modelWiFiPower:.classDebugEnabled.2579
- _modelWiFiPower:.defaultOnce.2575
- _modelWiFiPower:.defaultOnce.2578
- _setWiFiAWDLDevice:.classDebugEnabled.763
- _setWiFiAWDLDevice:.defaultOnce.762
- _setWiFiHotspotDevice:.classDebugEnabled.754
- _setWiFiHotspotDevice:.defaultOnce.753
- _setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3455
- _setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3454
- _wifiManufacturerQuery.classDebugEnabled.2510
- _wifiManufacturerQuery.defaultOnce.2509
- _xFlags.classDebugEnabled.5101
- _xFlags.classDebugEnabled.5110
- _xFlags.classDebugEnabled.5119
- _xFlags.classDebugEnabled.5128
- _xFlags.classDebugEnabled.5134
- _xFlags.classDebugEnabled.5140
- _xFlags.classDebugEnabled.5146
- _xFlags.classDebugEnabled.5155
- _xFlags.classDebugEnabled.5161
- _xFlags.classDebugEnabled.5167
- _xFlags.defaultOnce.5100
- _xFlags.defaultOnce.5109
- _xFlags.defaultOnce.5118
- _xFlags.defaultOnce.5127
- _xFlags.defaultOnce.5133
- _xFlags.defaultOnce.5139
- _xFlags.defaultOnce.5145
- _xFlags.defaultOnce.5154
- _xFlags.defaultOnce.5160
- _xFlags.defaultOnce.5166
CStrings:
+ "1452-5026"
+ "AwakeCount"
+ "AwakeDuration"
+ "AwakeL3Count"
+ "AwakeL3Duration"
+ "BTMainIdleDuration"
+ "BTPHY2GIdleDuration"
+ "BTPHY5GIdleDuration"
+ "BTScanIdleDuration"
+ "BTSecondaryIdleDuration"
+ "CCPUIdleDuration"
+ "Call to fetch Control CPU stats was successful."
+ "ControlCPUPowerStats"
+ "DeepSleepCount"
+ "DeepSleepDuration"
+ "Error: Call to fetch Control CPU stats failed."
+ "PCIeL0Duration"
+ "PCIeL0EntryCount"
+ "PCIeL1Dot1Duration"
+ "PCIeL1Dot1EntryCount"
+ "PCIeL1Dot2Duration"
+ "PCIeL1Dot2EntryCount"
+ "PCIeL1Duration"
+ "PCIeL1EntryCount"
+ "PCIeL3Duration"
+ "PCIeL3EntryCount"
+ "V=u"
+ "WarmSleepCount"
+ "WarmSleepDuration"
+ "WiFi Chipset is an empty string."
+ "WiFi Chipset: %@"
+ "WiFiLMAC2GIdleDuration"
+ "WiFiLMAC5GIdleDuration"
+ "WiFiLMACCommonIdleDuration"
+ "WiFiPHY2GIdleDuration"
+ "WiFiPHY5GIdleDuration"
+ "WiFiRXIdleDuration"
+ "WiFiScanIdleDuration"
+ "WiFiTXIdleDuration"
+ "WiFiUMACIdleDuration"
+ "WifiChipset"
+ "bb24B"
+ "entryEventBackwardDefinitionControlCPUPowerStats"
+ "logEventBackwardControlCPUPowerStats"

```
