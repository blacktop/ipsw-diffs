## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-1851.102.4.0.0
-  __TEXT.__text: 0x1c2858
-  __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0xd21c
-  __TEXT.__const: 0x468
-  __TEXT.__cstring: 0x2276d
-  __TEXT.__oslogstring: 0x103a0
-  __TEXT.__gcc_except_tab: 0x1da8
+1851.120.59.0.0
+  __TEXT.__text: 0x1c47f8
+  __TEXT.__auth_stubs: 0x1d00
+  __TEXT.__objc_methlist: 0xd2c4
+  __TEXT.__const: 0x478
+  __TEXT.__cstring: 0x22a02
+  __TEXT.__oslogstring: 0x10608
+  __TEXT.__gcc_except_tab: 0x1dc4
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3444
-  __TEXT.__objc_classname: 0xaf1
-  __TEXT.__objc_methname: 0x2d4c8
-  __TEXT.__objc_methtype: 0x2593
-  __TEXT.__objc_stubs: 0x1bfc0
+  __TEXT.__unwind_info: 0x3480
+  __TEXT.__objc_classname: 0xaf2
+  __TEXT.__objc_methname: 0x2d6f4
+  __TEXT.__objc_methtype: 0x261a
+  __TEXT.__objc_stubs: 0x1c100
   __DATA_CONST.__got: 0x708
-  __DATA_CONST.__const: 0x4030
+  __DATA_CONST.__const: 0x4068
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_nlclslist: 0x110
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xec38
-  __DATA_CONST.__objc_selrefs: 0x8998
+  __DATA_CONST.__objc_const: 0xecf8
+  __DATA_CONST.__objc_selrefs: 0x8a20
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x708
   __DATA_CONST.__objc_superrefs: 0x290
-  __DATA_CONST.__objc_arraydata: 0x143a8
-  __AUTH_CONST.__cfstring: 0x2e620
+  __DATA_CONST.__objc_arraydata: 0x14438
+  __AUTH_CONST.__cfstring: 0x2ea20
   __AUTH_CONST.__objc_intobj: 0x25c8
   __AUTH_CONST.__objc_dictobj: 0x2e90
   __AUTH_CONST.__objc_const: 0x2718
-  __AUTH_CONST.__const: 0x1640
-  __AUTH_CONST.__objc_doubleobj: 0xac0
-  __AUTH_CONST.__objc_arrayobj: 0x28c8
+  __AUTH_CONST.__const: 0x1680
+  __AUTH_CONST.__objc_doubleobj: 0xae0
+  __AUTH_CONST.__objc_arrayobj: 0x2940
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xe88
+  __AUTH_CONST.__auth_got: 0xe98
   __AUTH.__objc_data: 0x820
   __AUTH.__data: 0x5a0
-  __DATA.__objc_ivar: 0x1074
-  __DATA.__data: 0x650
-  __DATA.__bss: 0x2dc8
+  __DATA.__objc_ivar: 0x107c
+  __DATA.__data: 0x658
+  __DATA.__bss: 0x2de8
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x348
+  __DATA_DIRTY.__bss: 0x350
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 7990
-  Symbols:   26217
-  CStrings:  14887
+  Functions: 8026
+  Symbols:   26319
+  CStrings:  14958
 
Symbols:
+ +[PLSMCAgent entryEventBackwardDefinitionDisplayPowerKeys]
+ +[PLSMCAgent supportsOLEDDisplayPower]
+ +[PLUtilities cleanLaunchdApplicationMacOS:]
+ +[PLUtilities cleanLaunchdName:]
+ +[PLUtilities cleanLaunchdName:].cold.1
+ -[PLCoalitionSample cpuTime]
+ -[PLCoalitionSample setCpuTime:]
+ -[PLPowerMetricMonitorService _batteryGaugeServiceDidBecomeInactive].cold.2
+ -[PLPowerMetricMonitorService _computeCPUCostWithCPUTicks:]
+ -[PLPowerMetricMonitorService _computeCPUCostWithCPUTicks:].cold.1
+ -[PLPowerMetricMonitorService addMonitoredProcessesWithPIDs:error:]
+ -[PLPowerMetricMonitorService collectMetricsOnDemand]
+ -[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]
+ -[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:].cold.1
+ -[PLSMCAgent displayAccumulatedKeys]
+ -[PLSMCAgent getPowerEntryFromSample:lastSample:withEntryKey:]
+ -[PLSMCAgent lastDisplayAccumlatedSample]
+ -[PLSMCAgent setLastDisplayAccumlatedSample:]
+ -[ProcessMemoryUsage processLaunchdName]
+ -[ProcessMemoryUsage setProcessLaunchdName:]
+ GCC_except_table112
+ GCC_except_table53
+ GCC_except_table99
+ _OBJC_IVAR_$_PLCoalitionSample._cpuTime
+ _OBJC_IVAR_$_PLSMCAgent._lastDisplayAccumlatedSample
+ _OBJC_IVAR_$_ProcessMemoryUsage._processLaunchdName
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.701
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.707
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.713
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.719
+ ___29-[PLWifiAgent findWifiDevice]_block_invoke.725
+ ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2330
+ ___31-[PLSMCAgent sampleKey:forKey:]_block_invoke.602
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.840
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.846
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.882
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.898
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.910
+ ___33-[PLWifiAgent setWiFiAWDLDevice:]_block_invoke.689
+ ___36-[PLSMCAgent displayAccumulatedKeys]_block_invoke
+ ___36-[PLWifiAgent setWiFiHotspotDevice:]_block_invoke.680
+ ___36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.2264
+ ___38+[PLSMCAgent supportsOLEDDisplayPower]_block_invoke
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.770
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.770.cold.1
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.771
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.779
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.779.cold.1
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.792
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.792.cold.1
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.755
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.755.cold.1
+ ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.766
+ ___40-[PLWifiAgent logEventForwardAWDLState:]_block_invoke.1096
+ ___40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1064
+ ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.614
+ ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.620
+ ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.626
+ ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.1987
+ ___43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.592
+ ___43-[PLWifiAgent logEventForwardHotspotState:]_block_invoke.1105
+ ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.2035
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1144
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1150
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1158
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1164
+ ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.2044
+ ___51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.824
+ ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke
+ ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.209
+ ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.209.cold.1
+ ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.cold.1
+ ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.cold.2
+ ___53-[PLProcessMonitorAgent logEventPointFreezerDemotion]_block_invoke.575
+ ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1016
+ ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1025
+ ___56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.1052
+ ___58-[PLProcessMonitorAgent logEventIntervalKernelTaskMonitor]_block_invoke.637
+ ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.208
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1007
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.938
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.944
+ ___62-[PLSMCAgent getPowerEntryFromSample:lastSample:withEntryKey:]_block_invoke
+ ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke
+ ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.215
+ ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.215.cold.1
+ ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.cold.1
+ ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.cold.2
+ ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.cold.3
+ ___78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.818
+ ___81-[PLProcessMonitorAgent logEventBackwardProcessExitHistogram:withStats:withDate:]_block_invoke.612
+ ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.207
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2159
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2171
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2180
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2186
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2192
+ ___99-[PLProcessMonitorAgent logEventPointProcessExit:excludeProcesses:withStats:withDate:withNowInSec:]_block_invoke.529
+ ___99-[PLProcessMonitorAgent logEventPointProcessExit:excludeProcesses:withStats:withDate:withNowInSec:]_block_invoke_2.548
+ ___block_descriptor_50_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_literal_global.1884
+ ___block_literal_global.1925
+ ___block_literal_global.347
+ ___block_literal_global.359
+ ___block_literal_global.383
+ ___block_literal_global.389
+ ___block_literal_global.391
+ ___block_literal_global.396
+ ___block_literal_global.403
+ ___block_literal_global.405
+ ___block_literal_global.412
+ ___block_literal_global.415
+ ___block_literal_global.418
+ ___block_literal_global.426
+ ___block_literal_global.431
+ ___block_literal_global.440
+ ___block_literal_global.448
+ ___block_literal_global.457
+ ___block_literal_global.478
+ ___block_literal_global.497
+ ___block_literal_global.606
+ ___block_literal_global.634
+ ___block_literal_global.645
+ ___block_literal_global.665
+ ___block_literal_global.667
+ ___block_literal_global.678
+ ___block_literal_global.683
+ ___block_literal_global.696
+ ___block_literal_global.745
+ ___block_literal_global.747
+ ___block_literal_global.749
+ ___block_literal_global.751
+ ___block_literal_global.753
+ ___block_literal_global.755
+ ___block_literal_global.761
+ ___block_literal_global.763
+ ___block_literal_global.765
+ ___block_literal_global.767
+ ___block_literal_global.769
+ ___block_literal_global.772
+ ___block_literal_global.774
+ ___block_literal_global.781
+ ___block_literal_global.883
+ ___stringIsUUID_block_invoke
+ __unnamed_array_storage.1207
+ __unnamed_array_storage.1212
+ __unnamed_array_storage.1215
+ __unnamed_array_storage.1216
+ __unnamed_array_storage.1225
+ __unnamed_array_storage.1234
+ __unnamed_array_storage.1243
+ __unnamed_array_storage.1252
+ __unnamed_array_storage.1261
+ __unnamed_array_storage.1270
+ __unnamed_array_storage.1279
+ __unnamed_array_storage.1288
+ __unnamed_array_storage.1297
+ __unnamed_array_storage.1306
+ __unnamed_array_storage.1315
+ __unnamed_array_storage.1324
+ __unnamed_array_storage.1333
+ __unnamed_array_storage.1342
+ __unnamed_array_storage.1351
+ __unnamed_array_storage.1354
+ __unnamed_array_storage.1355
+ __unnamed_array_storage.1391
+ __unnamed_array_storage.1400
+ __unnamed_array_storage.1409
+ __unnamed_array_storage.1418
+ __unnamed_array_storage.1427
+ __unnamed_array_storage.1436
+ __unnamed_array_storage.1445
+ __unnamed_array_storage.1454
+ __unnamed_array_storage.1463
+ __unnamed_array_storage.1472
+ __unnamed_array_storage.1475
+ __unnamed_array_storage.1476
+ __unnamed_array_storage.1485
+ __unnamed_array_storage.1494
+ __unnamed_array_storage.1503
+ __unnamed_array_storage.1512
+ __unnamed_array_storage.1521
+ __unnamed_array_storage.1534
+ __unnamed_array_storage.1543
+ __unnamed_array_storage.1552
+ __unnamed_array_storage.1582
+ __unnamed_array_storage.1592
+ __unnamed_array_storage.1601
+ __unnamed_array_storage.1604
+ __unnamed_array_storage.1614
+ __unnamed_array_storage.1623
+ __unnamed_array_storage.1626
+ __unnamed_array_storage.1640
+ __unnamed_array_storage.1649
+ __unnamed_array_storage.1652
+ __unnamed_array_storage.1653
+ __unnamed_array_storage.1662
+ __unnamed_array_storage.1671
+ __unnamed_array_storage.1674
+ __unnamed_array_storage.1684
+ __unnamed_array_storage.1693
+ __unnamed_array_storage.1702
+ __unnamed_array_storage.1711
+ __unnamed_array_storage.1720
+ __unnamed_array_storage.1729
+ __unnamed_array_storage.1732
+ __unnamed_array_storage.1733
+ __unnamed_array_storage.1742
+ __unnamed_array_storage.1760
+ __unnamed_array_storage.1769
+ __unnamed_array_storage.1778
+ __unnamed_array_storage.1787
+ __unnamed_array_storage.1805
+ __unnamed_array_storage.1814
+ __unnamed_array_storage.1823
+ __unnamed_array_storage.1859
+ __unnamed_array_storage.1862
+ __unnamed_array_storage.1872
+ __unnamed_array_storage.1881
+ __unnamed_array_storage.1899
+ __unnamed_array_storage.1902
+ __unnamed_array_storage.1903
+ __unnamed_array_storage.1910
+ __unnamed_array_storage.1921
+ __unnamed_array_storage.1930
+ __unnamed_array_storage.1939
+ __unnamed_array_storage.1948
+ __unnamed_array_storage.1957
+ __unnamed_array_storage.1975
+ __unnamed_array_storage.1984
+ __unnamed_array_storage.1990
+ __unnamed_array_storage.1999
+ __unnamed_array_storage.2003
+ __unnamed_array_storage.2140
+ __unnamed_array_storage.2143
+ __unnamed_array_storage.2149
+ __unnamed_array_storage.2152
+ __unnamed_array_storage.355
+ __unnamed_array_storage.356
+ _dispatch_semaphore_signal
+ _displayAccumulatedKeys.accumulatedKeys
+ _displayAccumulatedKeys.onceToken
+ _findWifiDevice.classDebugEnabled.700
+ _findWifiDevice.classDebugEnabled.706
+ _findWifiDevice.classDebugEnabled.712
+ _findWifiDevice.classDebugEnabled.718
+ _findWifiDevice.classDebugEnabled.724
+ _findWifiDevice.defaultOnce.699
+ _findWifiDevice.defaultOnce.705
+ _findWifiDevice.defaultOnce.711
+ _findWifiDevice.defaultOnce.717
+ _findWifiDevice.defaultOnce.723
+ _guiPrefix
+ _kPLSMCAgentEventBackwardDisplayPowerKeys
+ _kPLWifiAgentEventForwardWifiAssist_block_invoke_4.classDebugEnabled.823
+ _kPLWifiAgentEventForwardWifiAssist_block_invoke_4.defaultOnce.822
+ _logEventBackwardProcessExitHistogram:withStats:withDate:.classDebugEnabled.611
+ _logEventBackwardProcessExitHistogram:withStats:withDate:.defaultOnce.610
+ _logEventBackwardWifiProperties:.classDebugEnabled.1143
+ _logEventBackwardWifiProperties:.classDebugEnabled.1149
+ _logEventBackwardWifiProperties:.classDebugEnabled.1157
+ _logEventBackwardWifiProperties:.classDebugEnabled.1163
+ _logEventBackwardWifiProperties:.defaultOnce.1142
+ _logEventBackwardWifiProperties:.defaultOnce.1148
+ _logEventBackwardWifiProperties:.defaultOnce.1156
+ _logEventBackwardWifiProperties:.defaultOnce.1162
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2158
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2170
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2179
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2185
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2191
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2157
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2169
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2178
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2184
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2190
+ _logEventForwardAWDLState:.classDebugEnabled.1095
+ _logEventForwardAWDLState:.defaultOnce.1094
+ _logEventForwardHotspotState:.classDebugEnabled.1104
+ _logEventForwardHotspotState:.defaultOnce.1103
+ _logEventForwardModuleInfo.classDebugEnabled.1063
+ _logEventForwardModuleInfo.defaultOnce.1062
+ _logEventIntervalKernelTaskMonitor.classDebugEnabled.636
+ _logEventIntervalKernelTaskMonitor.defaultOnce.635
+ _logEventPointWake:.classDebugEnabled.839
+ _logEventPointWake:.classDebugEnabled.845
+ _logEventPointWake:.classDebugEnabled.881
+ _logEventPointWake:.classDebugEnabled.897
+ _logEventPointWake:.classDebugEnabled.909
+ _logEventPointWake:.defaultOnce.838
+ _logEventPointWake:.defaultOnce.844
+ _logEventPointWake:.defaultOnce.880
+ _logEventPointWake:.defaultOnce.896
+ _logEventPointWake:.defaultOnce.908
+ _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.1006
+ _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.937
+ _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.943
+ _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.1005
+ _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.936
+ _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.942
+ _logEventPointWakeLink:withParams:toEntry:.classDebugEnabled.1051
+ _logEventPointWakeLink:withParams:toEntry:.defaultOnce.1050
+ _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1015
+ _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1024
+ _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1014
+ _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1023
+ _macAppPrefix
+ _modelDisplayPowerFromIOMFB:.classDebugEnabled.2034
+ _modelDisplayPowerFromIOMFB:.defaultOnce.2033
+ _modelDynamicDisplayPower:.classDebugEnabled.1986
+ _modelDynamicDisplayPower:.defaultOnce.1985
+ _modelDynamicDisplayPowerFromAPL:.classDebugEnabled.2043
+ _modelDynamicDisplayPowerFromAPL:.defaultOnce.2042
+ _modelWiFiPower:.classDebugEnabled.2329
+ _modelWiFiPower:.defaultOnce.2328
+ _objc_msgSend$addMonitoredProcessWithPID:error:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$cleanLaunchdApplicationMacOS:
+ _objc_msgSend$cleanLaunchdName:
+ _objc_msgSend$collectMetricsOnSnapshotWithError:
+ _objc_msgSend$entryEventBackwardDefinitionDisplayPowerKeys
+ _objc_msgSend$isSupersetOfSet:
+ _objc_msgSend$processLaunchdName
+ _objc_msgSend$setCpuTime:
+ _objc_msgSend$setProcessLaunchdName:
+ _objc_msgSend$supportsOLEDDisplayPower
+ _objc_msgSend$updateMetrics:forPid:
+ _pidPrefix
+ _readKeyViaOSAccum:toOutput:.classDebugEnabled.613
+ _readKeyViaOSAccum:toOutput:.classDebugEnabled.619
+ _readKeyViaOSAccum:toOutput:.classDebugEnabled.625
+ _readKeyViaOSAccum:toOutput:.defaultOnce.612
+ _readKeyViaOSAccum:toOutput:.defaultOnce.618
+ _readKeyViaOSAccum:toOutput:.defaultOnce.624
+ _sampleKey:forKey:.classDebugEnabled.601
+ _sampleKey:forKey:.defaultOnce.600
+ _setWiFiAWDLDevice:.classDebugEnabled.688
+ _setWiFiAWDLDevice:.defaultOnce.687
+ _setWiFiHotspotDevice:.classDebugEnabled.679
+ _setWiFiHotspotDevice:.defaultOnce.678
+ _stringIsUUID.hexChars
+ _stringIsUUID.onceToken
+ _supportsOLEDDisplayPower.onceToken
+ _supportsOLEDDisplayPower.ret
+ _systemPrefix
+ _uikitAppPrefix
+ _userPrefix
+ _wifiManufacturerQuery.classDebugEnabled.2263
+ _wifiManufacturerQuery.defaultOnce.2262
+ _xpc_get_service_name_from_pid
- -[ProcessMemoryUsage coalitionLaunchdName]
- -[ProcessMemoryUsage setCoalitionLaunchdName:]
- GCC_except_table103
- GCC_except_table28
- _OBJC_IVAR_$_ProcessMemoryUsage._coalitionLaunchdName
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.684
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.690
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.696
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.702
- ___29-[PLWifiAgent findWifiDevice]_block_invoke.708
- ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2264
- ___31-[PLSMCAgent sampleKey:forKey:]_block_invoke.566
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.823
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.829
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.865
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.881
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.893
- ___33-[PLWifiAgent setWiFiAWDLDevice:]_block_invoke.672
- ___36-[PLWifiAgent setWiFiHotspotDevice:]_block_invoke.663
- ___36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.2198
- ___37+[PLUtilities exitWithReason:action:]_block_invoke_9
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.737
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.745
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.745.cold.1
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.753
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.753.cold.1
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.775
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke.775.cold.1
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.738
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.738.cold.1
- ___39-[PLWifiAgent initOperatorDependancies]_block_invoke_2.749
- ___40-[PLWifiAgent logEventForwardAWDLState:]_block_invoke.1079
- ___40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1047
- ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.578
- ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.584
- ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.590
- ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.1985
- ___43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.556
- ___43-[PLWifiAgent logEventForwardHotspotState:]_block_invoke.1088
- ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.2033
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1127
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1133
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1141
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1147
- ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.2042
- ___51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.807
- ___53-[PLProcessMonitorAgent logEventPointFreezerDemotion]_block_invoke.569
- ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1008
- ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.999
- ___56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.1035
- ___58-[PLProcessMonitorAgent logEventIntervalKernelTaskMonitor]_block_invoke.631
- ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.203
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.921
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.927
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.990
- ___78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.801
- ___81-[PLProcessMonitorAgent logEventBackwardProcessExitHistogram:withStats:withDate:]_block_invoke.606
- ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.202
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2093
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2105
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2114
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2120
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2126
- ___99-[PLProcessMonitorAgent logEventPointProcessExit:excludeProcesses:withStats:withDate:withNowInSec:]_block_invoke.526
- ___99-[PLProcessMonitorAgent logEventPointProcessExit:excludeProcesses:withStats:withDate:withNowInSec:]_block_invoke_2.542
- ___block_descriptor_49_e8_32s_e19_"NSDictionary"8?0ls32l8
- ___block_literal_global.1878
- ___block_literal_global.1923
- ___block_literal_global.321
- ___block_literal_global.365
- ___block_literal_global.377
- ___block_literal_global.407
- ___block_literal_global.414
- ___block_literal_global.419
- ___block_literal_global.423
- ___block_literal_global.427
- ___block_literal_global.430
- ___block_literal_global.433
- ___block_literal_global.436
- ___block_literal_global.439
- ___block_literal_global.444
- ___block_literal_global.449
- ___block_literal_global.458
- ___block_literal_global.465
- ___block_literal_global.466
- ___block_literal_global.475
- ___block_literal_global.515
- ___block_literal_global.598
- ___block_literal_global.603
- ___block_literal_global.639
- ___block_literal_global.662
- ___block_literal_global.664
- ___block_literal_global.675
- ___block_literal_global.680
- ___block_literal_global.684
- ___block_literal_global.709
- ___block_literal_global.711
- ___block_literal_global.713
- ___block_literal_global.715
- ___block_literal_global.717
- ___block_literal_global.723
- ___block_literal_global.725
- ___block_literal_global.727
- ___block_literal_global.729
- ___block_literal_global.731
- ___block_literal_global.734
- ___block_literal_global.764
- __unnamed_array_storage.1190
- __unnamed_array_storage.1195
- __unnamed_array_storage.1198
- __unnamed_array_storage.1199
- __unnamed_array_storage.1208
- __unnamed_array_storage.1217
- __unnamed_array_storage.1226
- __unnamed_array_storage.1235
- __unnamed_array_storage.1244
- __unnamed_array_storage.1253
- __unnamed_array_storage.1271
- __unnamed_array_storage.1280
- __unnamed_array_storage.1289
- __unnamed_array_storage.1298
- __unnamed_array_storage.1307
- __unnamed_array_storage.1316
- __unnamed_array_storage.1325
- __unnamed_array_storage.1334
- __unnamed_array_storage.1337
- __unnamed_array_storage.1338
- __unnamed_array_storage.1347
- __unnamed_array_storage.1356
- __unnamed_array_storage.1365
- __unnamed_array_storage.1374
- __unnamed_array_storage.1383
- __unnamed_array_storage.1410
- __unnamed_array_storage.1419
- __unnamed_array_storage.1428
- __unnamed_array_storage.1437
- __unnamed_array_storage.1446
- __unnamed_array_storage.1455
- __unnamed_array_storage.1458
- __unnamed_array_storage.1459
- __unnamed_array_storage.1468
- __unnamed_array_storage.1477
- __unnamed_array_storage.1486
- __unnamed_array_storage.1495
- __unnamed_array_storage.1504
- __unnamed_array_storage.1513
- __unnamed_array_storage.1516
- __unnamed_array_storage.1517
- __unnamed_array_storage.1526
- __unnamed_array_storage.1535
- __unnamed_array_storage.1538
- __unnamed_array_storage.1539
- __unnamed_array_storage.1548
- __unnamed_array_storage.1557
- __unnamed_array_storage.1560
- __unnamed_array_storage.1573
- __unnamed_array_storage.1574
- __unnamed_array_storage.1586
- __unnamed_array_storage.1587
- __unnamed_array_storage.1596
- __unnamed_array_storage.1608
- __unnamed_array_storage.1618
- __unnamed_array_storage.1663
- __unnamed_array_storage.1667
- __unnamed_array_storage.1676
- __unnamed_array_storage.1685
- __unnamed_array_storage.1694
- __unnamed_array_storage.1703
- __unnamed_array_storage.1712
- __unnamed_array_storage.1721
- __unnamed_array_storage.1748
- __unnamed_array_storage.1757
- __unnamed_array_storage.1766
- __unnamed_array_storage.1775
- __unnamed_array_storage.1793
- __unnamed_array_storage.1797
- __unnamed_array_storage.1806
- __unnamed_array_storage.1815
- __unnamed_array_storage.1833
- __unnamed_array_storage.1836
- __unnamed_array_storage.1837
- __unnamed_array_storage.1846
- __unnamed_array_storage.1855
- __unnamed_array_storage.1873
- __unnamed_array_storage.1891
- __unnamed_array_storage.1900
- __unnamed_array_storage.1909
- __unnamed_array_storage.1911
- __unnamed_array_storage.1918
- __unnamed_array_storage.1933
- __unnamed_array_storage.1936
- __unnamed_array_storage.1937
- __unnamed_array_storage.2036
- __unnamed_array_storage.2037
- __unnamed_array_storage.2073
- __unnamed_array_storage.2074
- __unnamed_array_storage.2077
- __unnamed_array_storage.2083
- __unnamed_array_storage.327
- __unnamed_array_storage.774
- _findWifiDevice.classDebugEnabled.683
- _findWifiDevice.classDebugEnabled.689
- _findWifiDevice.classDebugEnabled.695
- _findWifiDevice.classDebugEnabled.701
- _findWifiDevice.classDebugEnabled.707
- _findWifiDevice.defaultOnce.682
- _findWifiDevice.defaultOnce.688
- _findWifiDevice.defaultOnce.694
- _findWifiDevice.defaultOnce.700
- _findWifiDevice.defaultOnce.706
- _kPLWifiAgentEventForwardWifiAssist_block_invoke_4.classDebugEnabled.806
- _kPLWifiAgentEventForwardWifiAssist_block_invoke_4.defaultOnce.805
- _logEventBackwardProcessExitHistogram:withStats:withDate:.classDebugEnabled.605
- _logEventBackwardProcessExitHistogram:withStats:withDate:.defaultOnce.604
- _logEventBackwardWifiProperties:.classDebugEnabled.1126
- _logEventBackwardWifiProperties:.classDebugEnabled.1132
- _logEventBackwardWifiProperties:.classDebugEnabled.1140
- _logEventBackwardWifiProperties:.classDebugEnabled.1146
- _logEventBackwardWifiProperties:.defaultOnce.1125
- _logEventBackwardWifiProperties:.defaultOnce.1131
- _logEventBackwardWifiProperties:.defaultOnce.1139
- _logEventBackwardWifiProperties:.defaultOnce.1145
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2092
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2104
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2113
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2119
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2125
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2091
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2103
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2112
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2118
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2124
- _logEventForwardAWDLState:.classDebugEnabled.1078
- _logEventForwardAWDLState:.defaultOnce.1077
- _logEventForwardHotspotState:.classDebugEnabled.1087
- _logEventForwardHotspotState:.defaultOnce.1086
- _logEventForwardModuleInfo.classDebugEnabled.1046
- _logEventForwardModuleInfo.defaultOnce.1045
- _logEventIntervalKernelTaskMonitor.classDebugEnabled.630
- _logEventIntervalKernelTaskMonitor.defaultOnce.629
- _logEventPointWake:.classDebugEnabled.822
- _logEventPointWake:.classDebugEnabled.828
- _logEventPointWake:.classDebugEnabled.864
- _logEventPointWake:.classDebugEnabled.880
- _logEventPointWake:.classDebugEnabled.892
- _logEventPointWake:.defaultOnce.821
- _logEventPointWake:.defaultOnce.827
- _logEventPointWake:.defaultOnce.863
- _logEventPointWake:.defaultOnce.879
- _logEventPointWake:.defaultOnce.891
- _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.920
- _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.926
- _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.989
- _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.919
- _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.925
- _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.988
- _logEventPointWakeLink:withParams:toEntry:.classDebugEnabled.1034
- _logEventPointWakeLink:withParams:toEntry:.defaultOnce.1033
- _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1007
- _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.998
- _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1006
- _logEventPointWakePNO:withParams:toEntry:.defaultOnce.997
- _modelDisplayPowerFromIOMFB:.classDebugEnabled.2032
- _modelDisplayPowerFromIOMFB:.defaultOnce.2031
- _modelDynamicDisplayPower:.classDebugEnabled.1984
- _modelDynamicDisplayPower:.defaultOnce.1983
- _modelDynamicDisplayPowerFromAPL:.classDebugEnabled.2041
- _modelDynamicDisplayPowerFromAPL:.defaultOnce.2040
- _modelWiFiPower:.classDebugEnabled.2263
- _modelWiFiPower:.defaultOnce.2262
- _objc_msgSend$coalitionLaunchdName
- _objc_msgSend$setCoalitionLaunchdName:
- _readKeyViaOSAccum:toOutput:.classDebugEnabled.577
- _readKeyViaOSAccum:toOutput:.classDebugEnabled.583
- _readKeyViaOSAccum:toOutput:.classDebugEnabled.589
- _readKeyViaOSAccum:toOutput:.defaultOnce.576
- _readKeyViaOSAccum:toOutput:.defaultOnce.582
- _readKeyViaOSAccum:toOutput:.defaultOnce.588
- _sampleKey:forKey:.classDebugEnabled.565
- _sampleKey:forKey:.defaultOnce.564
- _setWiFiAWDLDevice:.classDebugEnabled.671
- _setWiFiAWDLDevice:.defaultOnce.670
- _setWiFiHotspotDevice:.classDebugEnabled.662
- _setWiFiHotspotDevice:.defaultOnce.661
- _wifiManufacturerQuery.classDebugEnabled.2197
- _wifiManufacturerQuery.defaultOnce.2196
CStrings:
+ "\x0f\x01\x12"
+ "%s: CPU Cost=%f"
+ "-[PLPowerMetricMonitorService _computeCPUCostWithCPUTicks:]"
+ "-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke"
+ "0123456789ABCDEFabcdef"
+ "@\"PPSMetricCollection\"16@0:8"
+ "@\"PPSMetricCollection\"24@0:8^@16"
+ "@\"PPSMetricCollection\"32@0:8@\"NSArray\"16^@24"
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "@60@0:8^{coalition_resource_usage=QQQQQQQQQQQQQQQQQQQQQQQQ[7Q]QQQQQQQ}16@24@32@40Q48B56"
+ "BroadcastRXDuration"
+ "CACHED_OPS_RX_DURATION_IBSS"
+ "CACHED_OPS_RX_DURATION_MBSS"
+ "CACHED_OPS_RX_DURATION_OBSS"
+ "CACHED_RX_DURATION_BROADCAST"
+ "CACHED_RX_DURATION_MULTICAST"
+ "DisplayPowerKeys"
+ "Error while trying to addMonitoredProcessWithPID: %@"
+ "IBSSRXDuration"
+ "INSTANT_OPS_RX_DURATION_IBSS"
+ "INSTANT_OPS_RX_DURATION_MBSS"
+ "INSTANT_OPS_RX_DURATION_OBSS"
+ "INSTANT_RX_DURATION_BROADCAST"
+ "INSTANT_RX_DURATION_MULTICAST"
+ "MBSSRXDuration"
+ "MulticastRXDuration"
+ "OBSSRXDuration"
+ "PLBatteryGaugeService became inactive; mode is updateOnSnapshot so we should have already ended with error"
+ "PPSMetricMonitorMode is not PPSMetricMonitorModeUpdateOnSnapshot"
+ "SBAP"
+ "T@\"NSDictionary\",&,V_lastDisplayAccumlatedSample"
+ "T@\"NSString\",&,V_processLaunchdName"
+ "TAOC"
+ "TIOP"
+ "TPSP"
+ "TQ,V_cpuTime"
+ "TTDb"
+ "TVB1"
+ "TVB2"
+ "TVB3"
+ "TVB4"
+ "TVBL"
+ "Timed out while trying to collect metrics"
+ "_computeCPUCostWithCPUTicks:"
+ "_cpuTime"
+ "_lastDisplayAccumlatedSample"
+ "_processLaunchdName"
+ "addMonitoredProcessesWithPIDs:error:"
+ "application."
+ "characterSetWithCharactersInString:"
+ "cleanLaunchdApplicationMacOS:"
+ "cleanLaunchdName:"
+ "cleanLaunchdName: Unknown launchd service name: %@"
+ "collectMetricsOnDemand"
+ "collectMetricsOnDemand called without start monitoring"
+ "collectMetricsOnDemand dispatch_semaphore_signal"
+ "collectMetricsOnDemand mode is not PPSMetricMonitorModeUpdateOnDemand"
+ "collectMetricsOnSnapshot called without start monitoring"
+ "collectMetricsOnSnapshot dispatch_semaphore_signal"
+ "collectMetricsOnSnapshotWithError:"
+ "displayAccumulatedKeys"
+ "entryEventBackwardDefinitionDisplayPowerKeys"
+ "ftD0"
+ "getPowerEntryFromSample:lastSample:withEntryKey:"
+ "gui/"
+ "isSupersetOfSet:"
+ "is_mac_app"
+ "lastDisplayAccumlatedSample"
+ "pid/"
+ "processLaunchdName"
+ "setCpuTime:"
+ "setLastDisplayAccumlatedSample:"
+ "setProcessLaunchdName:"
+ "supportsOLEDDisplayPower"
+ "system/"
+ "updateMetrics:forPid:"
+ "user/"
- "\x0f\x12"
- "%@KernelTimePowerlog_%f%@"
- "@60@0:8^{coalition_resource_usage=QQQQQQQQQQQQQQQQQQQQQQQQ[7Q]QQQQQQ}16@24@32@40Q48B56"
- "T@\"NSString\",&,V_coalitionLaunchdName"
- "_coalitionLaunchdName"
- "coalitionLaunchdName"
- "com.apple.power.error.kernelTimeDB"
- "kPLExitReasonDescKernelTime"
- "kernelTimeDB"
- "setCoalitionLaunchdName:"

```
