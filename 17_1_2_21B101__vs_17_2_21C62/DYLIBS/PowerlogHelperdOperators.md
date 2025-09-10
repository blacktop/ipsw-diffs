## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-1787.40.67.0.0
-  __TEXT.__text: 0x1ba0f4
+1787.60.31.0.0
+  __TEXT.__text: 0x1bb0c8
   __TEXT.__auth_stubs: 0x1cc0
-  __TEXT.__objc_methlist: 0xcefc
+  __TEXT.__objc_methlist: 0xcf84
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x22036
-  __TEXT.__oslogstring: 0xfed5
-  __TEXT.__gcc_except_tab: 0x1d80
+  __TEXT.__cstring: 0x22200
+  __TEXT.__oslogstring: 0xffb2
+  __TEXT.__gcc_except_tab: 0x1da8
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3394
+  __TEXT.__unwind_info: 0x33d8
   __TEXT.__objc_classname: 0xada
-  __TEXT.__objc_methname: 0x2cab0
+  __TEXT.__objc_methname: 0x2cc38
   __TEXT.__objc_methtype: 0x2582
-  __TEXT.__objc_stubs: 0x1b980
+  __TEXT.__objc_stubs: 0x1baa0
   __DATA_CONST.__got: 0x6f0
-  __DATA_CONST.__const: 0x3f50
+  __DATA_CONST.__const: 0x3f78
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_nlclslist: 0x110
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe850
-  __DATA_CONST.__objc_selrefs: 0x8780
-  __DATA_CONST.__objc_arraydata: 0x14280
-  __AUTH_CONST.__cfstring: 0x2da00
+  __DATA_CONST.__objc_const: 0xe8b0
+  __DATA_CONST.__objc_selrefs: 0x87e0
+  __DATA_CONST.__objc_arraydata: 0x142d0
+  __AUTH_CONST.__cfstring: 0x2dc80
   __AUTH_CONST.__objc_intobj: 0x2580
-  __AUTH_CONST.__objc_dictobj: 0x2dc8
+  __AUTH_CONST.__objc_dictobj: 0x2df0
   __AUTH_CONST.__objc_const: 0x26d0
-  __AUTH_CONST.__const: 0x15c0
+  __AUTH_CONST.__const: 0x15e0
   __AUTH_CONST.__objc_doubleobj: 0xac0
-  __AUTH_CONST.__objc_arrayobj: 0x2868
+  __AUTH_CONST.__objc_arrayobj: 0x2880
   __AUTH_CONST.__auth_got: 0xe78
   __AUTH.__objc_data: 0x820
   __AUTH.__data: 0x5a0
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x700
   __DATA.__objc_superrefs: 0x290
-  __DATA.__objc_ivar: 0x1028
+  __DATA.__objc_ivar: 0x1030
   __DATA.__data: 0x650
-  __DATA.__bss: 0x2e00
+  __DATA.__bss: 0x2e10
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 035A0AD6-0732-3CD4-A579-ADD7E1387194
-  Functions: 7887
-  Symbols:   25911
-  CStrings:  20496
+  UUID: 0F474EAB-B51C-346E-8F24-12EC15BA2796
+  Functions: 7905
+  Symbols:   25967
+  CStrings:  20559
 
Symbols:
+ +[PLDisplayAgent dcpSubFrameMap]
+ +[PLLocationAgent entryEventForwardDefinitionGnssSession]
+ +[PLSMCAgent parsePMUEvents:]
+ +[PLSMCAgent reportPMUEventsToCA:]
+ -[PLDisplayAgent getIOMFBSubFrameMap]
+ -[PLLocationAgent gnssSessionListener]
+ -[PLLocationAgent logEventForwardGnssSession:]
+ -[PLLocationAgent setGnssSessionListener:]
+ -[PLPowerMetricMonitorService _parseDCPSwapStats:]
+ -[PLPowerMetricMonitorService _setUpIOReporting].cold.3
+ -[PLPowerMetricMonitorService dcpSwapStats]
+ -[PLPowerMetricMonitorService setDcpSwapStats:]
+ GCC_except_table70
+ _OBJC_IVAR_$_PLLocationAgent._gnssSessionListener
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._dcpSwapStats
+ ___22-[PLDisplayAgent init]_block_invoke.1358
+ ___22-[PLDisplayAgent init]_block_invoke.1358.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke.1358.cold.2
+ ___22-[PLDisplayAgent init]_block_invoke.1358.cold.3
+ ___22-[PLDisplayAgent init]_block_invoke.1358.cold.4
+ ___22-[PLDisplayAgent init]_block_invoke.1369
+ ___22-[PLDisplayAgent init]_block_invoke.1373
+ ___22-[PLDisplayAgent init]_block_invoke.1377
+ ___22-[PLDisplayAgent init]_block_invoke.1383
+ ___22-[PLDisplayAgent init]_block_invoke.1383.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke.1383.cold.2
+ ___22-[PLDisplayAgent init]_block_invoke.1401
+ ___22-[PLDisplayAgent init]_block_invoke.1409
+ ___22-[PLDisplayAgent init]_block_invoke_2.1360
+ ___22-[PLDisplayAgent init]_block_invoke_2.1379
+ ___22-[PLDisplayAgent init]_block_invoke_2.1379.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke_2.1379.cold.2
+ ___22-[PLDisplayAgent init]_block_invoke_2.1395
+ ___22-[PLDisplayAgent init]_block_invoke_2.1412
+ ___32+[PLDisplayAgent dcpSubFrameMap]_block_invoke
+ ___34+[PLSMCAgent reportPMUEventsToCA:]_block_invoke
+ ___37-[PLDisplayAgent getIOMFBSubFrameMap]_block_invoke
+ ___38-[PLLocationAgent resyncActiveClients]_block_invoke.599
+ ___40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1539
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.3951
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.3958
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.3954
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.3961
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1430
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1446
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1459
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1459.cold.1
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1459.cold.2
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1466
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1472
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1449
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1460
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1477
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1477.cold.1
+ ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.1937
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.391
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.391.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.415
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.415.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.429
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.429.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.441
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.441.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.447
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.447.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.457
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.457.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.457.cold.2
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.464
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.469
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.469.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.481
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.481.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.489
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.489.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.499
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.499.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.504
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.504.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.512
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.512.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.517
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.517.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.525
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.525.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.533
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.533.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.392
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.416
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.430
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.442
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.458
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.470
+ ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.578
+ ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.584
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.541.cold.1
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.555
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.561
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.567
+ ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.1985
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.639
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.646
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.649
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.655
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.661
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.667
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.674
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.680
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.686
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.692
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.698
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.699
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.702
+ ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke.333
+ ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke.351
+ ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke.351.cold.1
+ ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke_2.341
+ ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke_3.349
+ ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.1994
+ ___50-[PLPowerMetricMonitorService _parseDCPSwapStats:]_block_invoke
+ ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.766
+ ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.776
+ ___56-[PLLocationAgent logEventForwardTechStatus_withLimiter]_block_invoke.575
+ ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.609
+ ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.615
+ ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.621
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1662
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1669
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1680
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1680.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1691
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1691.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1692
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1692.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1693
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1693.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1694
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1694.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1695
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1695.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1696
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1696.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1696.cold.2
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1703
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1703.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1708
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1712
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1712.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1737
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1738
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1738.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1675
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1687
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1704
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1731
+ ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4214
+ ___73-[PLLocationAgent closeOpenEntryForClient:withOpenEntry:withTimeStopped:]_block_invoke.631
+ ___block_descriptor_37_e5_v8?0l
+ ___block_literal_global.1779
+ ___block_literal_global.1781
+ ___block_literal_global.1783
+ ___block_literal_global.1791
+ ___block_literal_global.1830
+ ___block_literal_global.1832
+ ___block_literal_global.1834
+ ___block_literal_global.1875
+ ___block_literal_global.353
+ ___block_literal_global.408
+ __unnamed_array_storage.1152
+ __unnamed_array_storage.1153
+ __unnamed_array_storage.1161
+ __unnamed_array_storage.1162
+ __unnamed_array_storage.1169
+ __unnamed_array_storage.1172
+ __unnamed_array_storage.1292
+ __unnamed_array_storage.1444
+ __unnamed_array_storage.1445
+ __unnamed_array_storage.1457
+ __unnamed_array_storage.1860
+ __unnamed_array_storage.1863
+ __unnamed_array_storage.287
+ __unnamed_array_storage.2916
+ __unnamed_array_storage.2934
+ __unnamed_array_storage.2935
+ __unnamed_array_storage.300
+ __unnamed_array_storage.301
+ __unnamed_array_storage.308
+ __unnamed_array_storage.314
+ __unnamed_array_storage.315
+ __unnamed_array_storage.331
+ __unnamed_array_storage.339
+ __unnamed_array_storage.346
+ __unnamed_array_storage.347
+ __unnamed_array_storage.377
+ __unnamed_array_storage.388
+ __unnamed_array_storage.389
+ __unnamed_array_storage.4005
+ __unnamed_array_storage.4044
+ __unnamed_array_storage.4122
+ __unnamed_array_storage.413
+ __unnamed_array_storage.4200
+ __unnamed_array_storage.438
+ __unnamed_array_storage.479
+ __unnamed_array_storage.496
+ __unnamed_array_storage.497
+ __unnamed_array_storage.502
+ __unnamed_array_storage.510
+ __unnamed_array_storage.514
+ __unnamed_array_storage.522
+ __unnamed_array_storage.523
+ __unnamed_array_storage.530
+ __unnamed_array_storage.531
+ __unnamed_array_storage.615
+ __unnamed_array_storage.621
+ __unnamed_array_storage.630
+ __unnamed_array_storage.639
+ __unnamed_array_storage.648
+ __unnamed_array_storage.657
+ __unnamed_array_storage.666
+ __unnamed_array_storage.675
+ __unnamed_array_storage.684
+ _dcpSubFrameMap.onceToken
+ _dcpSubFrameMap.subFrameMap
+ _getIOMFBSubFrameMap.onceToken
+ _getIOMFBSubFrameMap.subFrameMap
+ _handleBrightnessClientNotification:withValue:.classDebugEnabled.1736
+ _handleBrightnessClientNotification:withValue:.defaultOnce.1735
+ _init.classDebugEnabled.1368
+ _init.defaultOnce.1367
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.classDebugEnabled.546
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.defaultOnce.545
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.638
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.645
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.648
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.654
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.660
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.666
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.673
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.679
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.685
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.691
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.697
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.637
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.644
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.647
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.653
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.659
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.665
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.672
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.678
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.684
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.690
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.696
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.classDebugEnabled.463
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.defaultOnce.462
+ _kPLLocationAgentEventForwardGnssSession
+ _kPRearNits_block_invoke_2.classDebugEnabled.1400
+ _kPRearNits_block_invoke_2.defaultOnce.1399
+ _kPRearNits_block_invoke_3.classDebugEnabled.1465
+ _kPRearNits_block_invoke_3.defaultOnce.1464
+ _kPRearNits_block_invoke_4.classDebugEnabled.1661
+ _kPRearNits_block_invoke_4.classDebugEnabled.1668
+ _kPRearNits_block_invoke_4.defaultOnce.1660
+ _kPRearNits_block_invoke_4.defaultOnce.1667
+ _logEventBackwardHeatMap.classDebugEnabled.3953
+ _logEventBackwardHeatMap.classDebugEnabled.3960
+ _logEventBackwardHeatMap.defaultOnce.3952
+ _logEventBackwardHeatMap.defaultOnce.3959
+ _logEventForwardALSLux:.classDebugEnabled.1538
+ _logEventForwardALSLux:.defaultOnce.1537
+ _logEventForwardClientStatuswithPayload:.classDebugEnabled.608
+ _logEventForwardClientStatuswithPayload:.classDebugEnabled.614
+ _logEventForwardClientStatuswithPayload:.classDebugEnabled.620
+ _logEventForwardClientStatuswithPayload:.defaultOnce.607
+ _logEventForwardClientStatuswithPayload:.defaultOnce.613
+ _logEventForwardClientStatuswithPayload:.defaultOnce.619
+ _logEventForwardTechStatus.classDebugEnabled.577
+ _logEventForwardTechStatus.classDebugEnabled.583
+ _logEventForwardTechStatus.defaultOnce.576
+ _logEventForwardTechStatus.defaultOnce.582
+ _logEventPointClientStatus.classDebugEnabled.554
+ _logEventPointClientStatus.classDebugEnabled.560
+ _logEventPointClientStatus.classDebugEnabled.566
+ _logEventPointClientStatus.defaultOnce.553
+ _logEventPointClientStatus.defaultOnce.559
+ _logEventPointClientStatus.defaultOnce.565
+ _modelDisplayPowerFromIOMFB:.classDebugEnabled.1984
+ _modelDisplayPowerFromIOMFB:.defaultOnce.1983
+ _modelDynamicDisplayPower:.classDebugEnabled.1936
+ _modelDynamicDisplayPower:.defaultOnce.1935
+ _modelDynamicDisplayPowerFromAPL:.classDebugEnabled.1993
+ _modelDynamicDisplayPowerFromAPL:.defaultOnce.1992
+ _objc_msgSend$_parseDCPSwapStats:
+ _objc_msgSend$dcpSubFrameMap
+ _objc_msgSend$dcpSwapStats
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$entryEventForwardDefinitionGnssSession
+ _objc_msgSend$getIOMFBSubFrameMap
+ _objc_msgSend$logEventForwardGnssSession:
+ _objc_msgSend$parsePMUEvents:
+ _objc_msgSend$setDcpSwapStats:
+ _objc_msgSend$setDisplayFPS:
+ _resyncActiveClients.classDebugEnabled.598
+ _resyncActiveClients.defaultOnce.597
+ _updateClientsLocationInfo:.classDebugEnabled.701
+ _updateClientsLocationInfo:.defaultOnce.700
+ _updateLocationDistributionEvents.classDebugEnabled.765
+ _updateLocationDistributionEvents.classDebugEnabled.775
+ _updateLocationDistributionEvents.defaultOnce.764
+ _updateLocationDistributionEvents.defaultOnce.774
- -[PLDisplayAgent getSubFrameMap]
- GCC_except_table68
- ___22-[PLDisplayAgent init]_block_invoke.1355
- ___22-[PLDisplayAgent init]_block_invoke.1355.cold.1
- ___22-[PLDisplayAgent init]_block_invoke.1355.cold.2
- ___22-[PLDisplayAgent init]_block_invoke.1355.cold.3
- ___22-[PLDisplayAgent init]_block_invoke.1355.cold.4
- ___22-[PLDisplayAgent init]_block_invoke.1366
- ___22-[PLDisplayAgent init]_block_invoke.1370
- ___22-[PLDisplayAgent init]_block_invoke.1374
- ___22-[PLDisplayAgent init]_block_invoke.1380
- ___22-[PLDisplayAgent init]_block_invoke.1380.cold.1
- ___22-[PLDisplayAgent init]_block_invoke.1380.cold.2
- ___22-[PLDisplayAgent init]_block_invoke.1398
- ___22-[PLDisplayAgent init]_block_invoke.1406
- ___22-[PLDisplayAgent init]_block_invoke_2.1357
- ___22-[PLDisplayAgent init]_block_invoke_2.1376
- ___22-[PLDisplayAgent init]_block_invoke_2.1376.cold.1
- ___22-[PLDisplayAgent init]_block_invoke_2.1376.cold.2
- ___22-[PLDisplayAgent init]_block_invoke_2.1392
- ___22-[PLDisplayAgent init]_block_invoke_2.1409
- ___32-[PLDisplayAgent getSubFrameMap]_block_invoke
- ___38-[PLLocationAgent resyncActiveClients]_block_invoke.585
- ___40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1533
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.3948
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.3955
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.3951
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.3958
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1427
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1443
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1456
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1456.cold.1
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1456.cold.2
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1463
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1469
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1446
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1457
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1474
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1474.cold.1
- ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.1931
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.382
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.382.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.397
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.397.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.420
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.420.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.432
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.432.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.438
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.438.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.448
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.448.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.448.cold.2
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.455
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.460
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.460.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.472
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.472.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.480
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.480.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.490
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.490.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.495
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.495.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.503
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.503.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.511
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.511.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.519
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.519.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.383
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.398
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.421
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.433
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.440
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.461
- ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.564
- ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.570
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.527
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.527.cold.1
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.533
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.553
- ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.1979
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.625
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.632
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.635
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.641
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.647
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.653
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.660
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.666
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.672
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.678
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.684
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.685
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.688
- ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke.330
- ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke_2.338
- ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke_3.346
- ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.1988
- ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.752
- ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.762
- ___56-[PLLocationAgent logEventForwardTechStatus_withLimiter]_block_invoke.561
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.595
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.601
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.607
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1656
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1663
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1668
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1668.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1685
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1685.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1686
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1686.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1687
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1687.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1688
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1688.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1689
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1689.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1690
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1690.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1690.cold.2
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1697
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1697.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1702
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1706
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1706.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1731
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1732
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1732.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1669
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1681
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1698
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1725
- ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4211
- ___73-[PLLocationAgent closeOpenEntryForClient:withOpenEntry:withTimeStopped:]_block_invoke.617
- ___block_literal_global.1761
- ___block_literal_global.1763
- ___block_literal_global.1765
- ___block_literal_global.1785
- ___block_literal_global.1824
- ___block_literal_global.1826
- ___block_literal_global.1828
- ___block_literal_global.1869
- ___block_literal_global.401
- __unnamed_array_storage.1137
- __unnamed_array_storage.1138
- __unnamed_array_storage.1146
- __unnamed_array_storage.1147
- __unnamed_array_storage.1154
- __unnamed_array_storage.1157
- __unnamed_array_storage.1289
- __unnamed_array_storage.1441
- __unnamed_array_storage.1442
- __unnamed_array_storage.1454
- __unnamed_array_storage.1857
- __unnamed_array_storage.290
- __unnamed_array_storage.291
- __unnamed_array_storage.2912
- __unnamed_array_storage.2913
- __unnamed_array_storage.2931
- __unnamed_array_storage.2932
- __unnamed_array_storage.297
- __unnamed_array_storage.305
- __unnamed_array_storage.327
- __unnamed_array_storage.335
- __unnamed_array_storage.336
- __unnamed_array_storage.337
- __unnamed_array_storage.367
- __unnamed_array_storage.368
- __unnamed_array_storage.394
- __unnamed_array_storage.4002
- __unnamed_array_storage.4041
- __unnamed_array_storage.4119
- __unnamed_array_storage.418
- __unnamed_array_storage.4197
- __unnamed_array_storage.429
- __unnamed_array_storage.430
- __unnamed_array_storage.458
- __unnamed_array_storage.469
- __unnamed_array_storage.470
- __unnamed_array_storage.477
- __unnamed_array_storage.492
- __unnamed_array_storage.493
- __unnamed_array_storage.500
- __unnamed_array_storage.516
- __unnamed_array_storage.517
- __unnamed_array_storage.618
- __unnamed_array_storage.627
- __unnamed_array_storage.636
- __unnamed_array_storage.645
- __unnamed_array_storage.663
- __unnamed_array_storage.681
- _getSubFrameMap.onceToken
- _getSubFrameMap.subFrameMap
- _handleBrightnessClientNotification:withValue:.classDebugEnabled.1730
- _handleBrightnessClientNotification:withValue:.defaultOnce.1729
- _init.classDebugEnabled.1365
- _init.defaultOnce.1364
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.classDebugEnabled.532
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.defaultOnce.531
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.624
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.631
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.634
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.640
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.646
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.652
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.659
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.665
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.671
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.677
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.683
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.623
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.630
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.633
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.639
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.645
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.651
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.658
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.664
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.670
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.676
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.682
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.classDebugEnabled.454
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.defaultOnce.453
- _kPRearNits_block_invoke_2.classDebugEnabled.1397
- _kPRearNits_block_invoke_2.defaultOnce.1396
- _kPRearNits_block_invoke_3.classDebugEnabled.1462
- _kPRearNits_block_invoke_3.defaultOnce.1461
- _kPRearNits_block_invoke_4.classDebugEnabled.1655
- _kPRearNits_block_invoke_4.classDebugEnabled.1662
- _kPRearNits_block_invoke_4.defaultOnce.1654
- _kPRearNits_block_invoke_4.defaultOnce.1661
- _logEventBackwardHeatMap.classDebugEnabled.3950
- _logEventBackwardHeatMap.classDebugEnabled.3957
- _logEventBackwardHeatMap.defaultOnce.3949
- _logEventBackwardHeatMap.defaultOnce.3956
- _logEventForwardALSLux:.classDebugEnabled.1532
- _logEventForwardALSLux:.defaultOnce.1531
- _logEventForwardClientStatuswithPayload:.classDebugEnabled.594
- _logEventForwardClientStatuswithPayload:.classDebugEnabled.600
- _logEventForwardClientStatuswithPayload:.classDebugEnabled.606
- _logEventForwardClientStatuswithPayload:.defaultOnce.593
- _logEventForwardClientStatuswithPayload:.defaultOnce.599
- _logEventForwardClientStatuswithPayload:.defaultOnce.605
- _logEventForwardTechStatus.classDebugEnabled.563
- _logEventForwardTechStatus.classDebugEnabled.569
- _logEventForwardTechStatus.defaultOnce.562
- _logEventForwardTechStatus.defaultOnce.568
- _logEventPointClientStatus.classDebugEnabled.540
- _logEventPointClientStatus.classDebugEnabled.546
- _logEventPointClientStatus.classDebugEnabled.552
- _logEventPointClientStatus.defaultOnce.539
- _logEventPointClientStatus.defaultOnce.545
- _logEventPointClientStatus.defaultOnce.551
- _modelDisplayPowerFromIOMFB:.classDebugEnabled.1978
- _modelDisplayPowerFromIOMFB:.defaultOnce.1977
- _modelDynamicDisplayPower:.classDebugEnabled.1930
- _modelDynamicDisplayPower:.defaultOnce.1929
- _modelDynamicDisplayPowerFromAPL:.classDebugEnabled.1987
- _modelDynamicDisplayPowerFromAPL:.defaultOnce.1986
- _objc_msgSend$getSubFrameMap
- _resyncActiveClients.classDebugEnabled.584
- _resyncActiveClients.defaultOnce.583
- _updateClientsLocationInfo:.classDebugEnabled.687
- _updateClientsLocationInfo:.defaultOnce.686
- _updateLocationDistributionEvents.classDebugEnabled.751
- _updateLocationDistributionEvents.classDebugEnabled.761
- _updateLocationDistributionEvents.defaultOnce.750
- _updateLocationDistributionEvents.defaultOnce.760
CStrings:
+ "\x0f\v\x11\x11\x13"
+ "!/\a"
+ "AirDropSession Unknown/Other AirDropSession State %@"
+ "BUCK0_THERMAL_THROTTLE"
+ "BUCK1_THERMAL_THROTTLE"
+ "ContactsUI.MonogramPosterExtension"
+ "DisplayStateExtended"
+ "EDRHeadroom"
+ "Failed to post %s : %d"
+ "Failed to subscribe to IOReport DCP swap"
+ "GdXjx1ixZYvN9Gg8iSf68A"
+ "GnssSession"
+ "GroupName"
+ "InterfaceChanged"
+ "PMU events: %llu -> %@"
+ "PerfPowerServices is ready to receive Background Processing Payload"
+ "Posted %s"
+ "Received GnssSession XPC with payload=%@"
+ "T@\"PLIOReportStats\",&,N,V_dcpSwapStats"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_gnssSessionListener"
+ "VDDMAIN_PRE_SHDN"
+ "VDDMAIN_UVWARN0"
+ "VDDMAIN_UVWARN1"
+ "VDD_BOOST_UVWARN0"
+ "_dcpSwapStats"
+ "_gnssSessionListener"
+ "_parseDCPSwapStats:"
+ "com.apple.ContactsUI.MonogramPosterExtension"
+ "com.apple.ContinuityCaptureShieldUI"
+ "com.apple.continuitycaptured"
+ "com.apple.perfpowerservices.reportfeaturestatus"
+ "com.apple.power.pmuevents"
+ "dcpSubFrameMap"
+ "dcpSwapStats"
+ "dictionaryWithCapacity:"
+ "entryEventForwardDefinitionGnssSession"
+ "eventStatus"
+ "getIOMFBSubFrameMap"
+ "gnssSessionListener"
+ "logEventForwardGnssSession:"
+ "parsePMUEvents:"
+ "reportPMUEventsToCA:"
+ "setDcpSwapStats:"
+ "setDisplayFPS:"
+ "setGnssSessionListener:"
+ "subframes(%d)"
+ "swap"
- "\x0f\v\x11\x11\x12"
- "!/\x06"
- "Unknown/Other AirDropSession State %@"
- "getSubFrameMap"

```
