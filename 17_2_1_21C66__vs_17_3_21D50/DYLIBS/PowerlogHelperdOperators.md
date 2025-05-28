## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-1787.60.31.0.0
-  __TEXT.__text: 0x1bb0c8
+1787.80.12.0.0
+  __TEXT.__text: 0x1bcd44
   __TEXT.__auth_stubs: 0x1cc0
-  __TEXT.__objc_methlist: 0xcf84
+  __TEXT.__objc_methlist: 0xd074
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x22200
-  __TEXT.__oslogstring: 0xffb2
+  __TEXT.__cstring: 0x222dd
+  __TEXT.__oslogstring: 0xff3a
   __TEXT.__gcc_except_tab: 0x1da8
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x33d8
-  __TEXT.__objc_classname: 0xada
-  __TEXT.__objc_methname: 0x2cc38
+  __TEXT.__unwind_info: 0x33f4
+  __TEXT.__objc_classname: 0xaef
+  __TEXT.__objc_methname: 0x2ce56
   __TEXT.__objc_methtype: 0x2582
-  __TEXT.__objc_stubs: 0x1baa0
+  __TEXT.__objc_stubs: 0x1bcc0
   __DATA_CONST.__got: 0x6f0
-  __DATA_CONST.__const: 0x3f78
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __DATA_CONST.__const: 0x3fd0
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_nlclslist: 0x110
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe8b0
-  __DATA_CONST.__objc_selrefs: 0x87e0
-  __DATA_CONST.__objc_arraydata: 0x142d0
-  __AUTH_CONST.__cfstring: 0x2dc80
+  __DATA_CONST.__objc_const: 0xea58
+  __DATA_CONST.__objc_selrefs: 0x8870
+  __DATA_CONST.__objc_arraydata: 0x142f0
+  __AUTH_CONST.__cfstring: 0x2dee0
   __AUTH_CONST.__objc_intobj: 0x2580
-  __AUTH_CONST.__objc_dictobj: 0x2df0
-  __AUTH_CONST.__objc_const: 0x26d0
+  __AUTH_CONST.__objc_dictobj: 0x2e18
+  __AUTH_CONST.__objc_const: 0x2718
   __AUTH_CONST.__const: 0x15e0
   __AUTH_CONST.__objc_doubleobj: 0xac0
   __AUTH_CONST.__objc_arrayobj: 0x2880
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0xe78
-  __AUTH.__objc_data: 0x820
+  __AUTH.__objc_data: 0x870
   __AUTH.__data: 0x5a0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x700
+  __DATA.__objc_classrefs: 0x708
   __DATA.__objc_superrefs: 0x290
-  __DATA.__objc_ivar: 0x1030
+  __DATA.__objc_ivar: 0x104c
   __DATA.__data: 0x650
   __DATA.__bss: 0x2e10
   __DATA.__common: 0x68

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 7905
-  Symbols:   25967
-  CStrings:  14699
+  Functions: 7921
+  Symbols:   26035
+  CStrings:  14751
 
Symbols:
+ +[PLLocationAgent entryEventPointDefinitionMotionPacket]
+ +[PLUtilities coalitionIDForPid:]
+ -[PLCoalitionSample bytesread]
+ -[PLCoalitionSample byteswritten]
+ -[PLCoalitionSample description]
+ -[PLCoalitionSample gpuTime]
+ -[PLCoalitionSample instructions]
+ -[PLCoalitionSample setBytesread:]
+ -[PLCoalitionSample setByteswritten:]
+ -[PLCoalitionSample setGpuTime:]
+ -[PLCoalitionSample setInstructions:]
+ -[PLLocationAgent logEventPointMotionPacket:]
+ -[PLLocationAgent motionPacketListener]
+ -[PLLocationAgent setMotionPacketListener:]
+ -[PLPowerMetricMonitorService _sampleCoalitions]
+ -[PLPowerMetricMonitorService setTrackedProcesses:]
+ -[PLPowerMetricMonitorService trackedProcesses]
+ -[PLProcessMetadata coalitionID]
+ -[PLProcessMetadata coalitionSample]
+ -[PLProcessMetadata description]
+ -[PLProcessMetadata setCoalitionID:]
+ -[PLProcessMetadata setCoalitionSample:]
+ GCC_except_table101
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table73
+ GCC_except_table88
+ _OBJC_CLASS_$_PLCoalitionSample
+ _OBJC_IVAR_$_PLCoalitionSample._bytesread
+ _OBJC_IVAR_$_PLCoalitionSample._byteswritten
+ _OBJC_IVAR_$_PLCoalitionSample._gpuTime
+ _OBJC_IVAR_$_PLCoalitionSample._instructions
+ _OBJC_IVAR_$_PLLocationAgent._motionPacketListener
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._trackedProcesses
+ _OBJC_IVAR_$_PLProcessMetadata._coalitionID
+ _OBJC_IVAR_$_PLProcessMetadata._coalitionSample
+ _OBJC_METACLASS_$_PLCoalitionSample
+ __OBJC_$_INSTANCE_METHODS_PLCoalitionSample
+ __OBJC_$_INSTANCE_VARIABLES_PLCoalitionSample
+ __OBJC_$_PROP_LIST_PLCoalitionSample
+ __OBJC_CLASS_RO_$_PLCoalitionSample
+ __OBJC_METACLASS_RO_$_PLCoalitionSample
+ ___157-[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:canRequestWhileBatteryGaugeIsRunning:minRequestInterval:block:]_block_invoke_2.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke.1400
+ ___22-[PLDisplayAgent init]_block_invoke.1400.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke.1400.cold.2
+ ___22-[PLDisplayAgent init]_block_invoke.1400.cold.3
+ ___22-[PLDisplayAgent init]_block_invoke.1400.cold.4
+ ___22-[PLDisplayAgent init]_block_invoke.1411
+ ___22-[PLDisplayAgent init]_block_invoke.1415
+ ___22-[PLDisplayAgent init]_block_invoke.1419
+ ___22-[PLDisplayAgent init]_block_invoke.1425
+ ___22-[PLDisplayAgent init]_block_invoke.1425.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke.1425.cold.2
+ ___22-[PLDisplayAgent init]_block_invoke.1443
+ ___22-[PLDisplayAgent init]_block_invoke.1451
+ ___22-[PLDisplayAgent init]_block_invoke_2.1402
+ ___22-[PLDisplayAgent init]_block_invoke_2.1421
+ ___22-[PLDisplayAgent init]_block_invoke_2.1421.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke_2.1421.cold.2
+ ___22-[PLDisplayAgent init]_block_invoke_2.1437
+ ___22-[PLDisplayAgent init]_block_invoke_2.1454
+ ___38-[PLLocationAgent resyncActiveClients]_block_invoke.616
+ ___40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1581
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1488
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1501
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1501.cold.1
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1501.cold.2
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1508
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1514
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1491
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1502
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1519
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1519.cold.1
+ ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.1979
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.403
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.403.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.418
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.418.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.427
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.427.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.453
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.453.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.459
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.459.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.469.cold.2
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.476
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.493
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.493.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.501
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.501.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.511
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.511.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.516
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.516.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.524
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.524.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.529
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.529.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.534
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.534.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.542
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.542.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.550
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.550.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.404
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.419
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.428
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.454
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.461
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.482
+ ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.595
+ ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.601
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.558
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.558.cold.1
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.564
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.572
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.578
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.584
+ ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.2027
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.656
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.663
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.666
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.672
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.678
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.684
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.691
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.697
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.703
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.709
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.715
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.716
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.719
+ ___48-[PLPowerMetricMonitorService _sampleCoalitions]_block_invoke
+ ___48-[PLPowerMetricMonitorService _sampleCoalitions]_block_invoke.cold.1
+ ___48-[PLPowerMetricMonitorService _sampleCoalitions]_block_invoke.cold.2
+ ___48-[PLPowerMetricMonitorService _sampleCoalitions]_block_invoke.cold.3
+ ___48-[PLPowerMetricMonitorService _sampleCoalitions]_block_invoke.cold.4
+ ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.2036
+ ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.783
+ ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.793
+ ___56-[PLLocationAgent logEventForwardTechStatus_withLimiter]_block_invoke.592
+ ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.626
+ ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.632
+ ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.638
+ ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.195
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1704
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1711
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1716
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1716.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1722
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1722.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1733
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1733.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1734
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1734.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1735
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1735.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1736
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1736.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1737.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1738.cold.2
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1745
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1745.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1750
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1754
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1754.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1779
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1780
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1780.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1717
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1729
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1746
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1773
+ ___64-[PLPowerMetricMonitorService addMonitoredProcessWithPID:error:]_block_invoke.cold.4
+ ___73-[PLLocationAgent closeOpenEntryForClient:withOpenEntry:withTimeStopped:]_block_invoke.648
+ ___76-[PLPowerMetricMonitorService _collectMetricsWithTimeout:completionHandler:]_block_invoke_3
+ ___76-[PLPowerMetricMonitorService _collectMetricsWithTimeout:completionHandler:]_block_invoke_3.cold.1
+ ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.194
+ ___block_descriptor_40_e8_32s_e44_v32?0"NSNumber"8"PLProcessMetadata"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e44_v32?0"NSNumber"8"PLProcessMetadata"16^B24ls32l8s40l8
+ ___block_literal_global.1809
+ ___block_literal_global.1811
+ ___block_literal_global.1813
+ ___block_literal_global.1815
+ ___block_literal_global.1817
+ ___block_literal_global.1819
+ ___block_literal_global.1821
+ ___block_literal_global.1823
+ ___block_literal_global.1825
+ ___block_literal_global.1833
+ ___block_literal_global.1872
+ ___block_literal_global.1874
+ ___block_literal_global.1876
+ ___block_literal_global.1917
+ ___block_literal_global.457
+ __unnamed_array_storage.1486
+ __unnamed_array_storage.1487
+ __unnamed_array_storage.1499
+ __unnamed_array_storage.1902
+ __unnamed_array_storage.1905
+ __unnamed_array_storage.358
+ __unnamed_array_storage.400
+ __unnamed_array_storage.401
+ __unnamed_array_storage.416
+ __unnamed_array_storage.424
+ __unnamed_array_storage.450
+ __unnamed_array_storage.451
+ __unnamed_array_storage.490
+ __unnamed_array_storage.491
+ __unnamed_array_storage.498
+ __unnamed_array_storage.499
+ __unnamed_array_storage.513
+ __unnamed_array_storage.521
+ __unnamed_array_storage.527
+ __unnamed_array_storage.532
+ __unnamed_array_storage.539
+ __unnamed_array_storage.540
+ __unnamed_array_storage.548
+ __unnamed_array_storage.663
+ __unnamed_array_storage.681
+ __unnamed_array_storage.717
+ __unnamed_array_storage.735
+ __unnamed_array_storage.744
+ __unnamed_array_storage.753
+ _handleBrightnessClientNotification:withValue:.classDebugEnabled.1778
+ _handleBrightnessClientNotification:withValue:.defaultOnce.1777
+ _init.classDebugEnabled.1410
+ _init.defaultOnce.1409
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.classDebugEnabled.563
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.defaultOnce.562
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.655
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.662
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.665
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.671
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.677
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.683
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.690
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.696
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.702
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.708
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.714
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.654
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.661
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.664
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.670
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.676
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.682
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.689
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.695
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.701
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.707
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.713
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.classDebugEnabled.475
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.defaultOnce.474
+ _kPLLocationAgentEventPointNameMotionPacket
+ _kPRearNits_block_invoke_2.classDebugEnabled.1442
+ _kPRearNits_block_invoke_2.defaultOnce.1441
+ _kPRearNits_block_invoke_3.classDebugEnabled.1507
+ _kPRearNits_block_invoke_3.defaultOnce.1506
+ _kPRearNits_block_invoke_4.classDebugEnabled.1703
+ _kPRearNits_block_invoke_4.classDebugEnabled.1710
+ _kPRearNits_block_invoke_4.defaultOnce.1702
+ _kPRearNits_block_invoke_4.defaultOnce.1709
+ _logEventForwardALSLux:.classDebugEnabled.1580
+ _logEventForwardALSLux:.defaultOnce.1579
+ _logEventForwardClientStatuswithPayload:.classDebugEnabled.625
+ _logEventForwardClientStatuswithPayload:.classDebugEnabled.631
+ _logEventForwardClientStatuswithPayload:.classDebugEnabled.637
+ _logEventForwardClientStatuswithPayload:.defaultOnce.624
+ _logEventForwardClientStatuswithPayload:.defaultOnce.630
+ _logEventForwardClientStatuswithPayload:.defaultOnce.636
+ _logEventForwardTechStatus.classDebugEnabled.594
+ _logEventForwardTechStatus.classDebugEnabled.600
+ _logEventForwardTechStatus.defaultOnce.593
+ _logEventForwardTechStatus.defaultOnce.599
+ _logEventPointClientStatus.classDebugEnabled.571
+ _logEventPointClientStatus.classDebugEnabled.577
+ _logEventPointClientStatus.classDebugEnabled.583
+ _logEventPointClientStatus.defaultOnce.570
+ _logEventPointClientStatus.defaultOnce.576
+ _logEventPointClientStatus.defaultOnce.582
+ _modelDisplayPowerFromIOMFB:.classDebugEnabled.2026
+ _modelDisplayPowerFromIOMFB:.defaultOnce.2025
+ _modelDynamicDisplayPower:.classDebugEnabled.1978
+ _modelDynamicDisplayPower:.defaultOnce.1977
+ _modelDynamicDisplayPowerFromAPL:.classDebugEnabled.2035
+ _modelDynamicDisplayPowerFromAPL:.defaultOnce.2034
+ _objc_msgSend$_sampleCoalitions
+ _objc_msgSend$bytesread
+ _objc_msgSend$byteswritten
+ _objc_msgSend$coalitionIDForPid:
+ _objc_msgSend$coalitionSample
+ _objc_msgSend$entryEventPointDefinitionMotionPacket
+ _objc_msgSend$fullProcessNameForPid:
+ _objc_msgSend$gpuTime
+ _objc_msgSend$instructions
+ _objc_msgSend$logEventPointMotionPacket:
+ _objc_msgSend$setBytesRead:
+ _objc_msgSend$setBytesWritten:
+ _objc_msgSend$setBytesread:
+ _objc_msgSend$setByteswritten:
+ _objc_msgSend$setCoalitionSample:
+ _objc_msgSend$setCpuInstructions:
+ _objc_msgSend$setGpuTime:
+ _objc_msgSend$setInstructions:
+ _objc_msgSend$setWifiAWDLRange:
+ _objc_msgSend$setWifiAWDLStatus:
+ _objc_msgSend$wifiAWDLRange
+ _objc_msgSend$wifiAWDLStatus
+ _resyncActiveClients.classDebugEnabled.615
+ _resyncActiveClients.defaultOnce.614
+ _updateClientsLocationInfo:.classDebugEnabled.718
+ _updateClientsLocationInfo:.defaultOnce.717
+ _updateLocationDistributionEvents.classDebugEnabled.782
+ _updateLocationDistributionEvents.classDebugEnabled.792
+ _updateLocationDistributionEvents.defaultOnce.781
+ _updateLocationDistributionEvents.defaultOnce.791
- -[PLPowerMetricMonitorService _parseApplicationMetricsFromEntry:].cold.2
- -[PLPowerMetricMonitorService _parseCoalitionMetricsFromEntry:]
- -[PLPowerMetricMonitorService _parseCoalitionMetricsFromEntry:].cold.1
- -[PLPowerMetricMonitorService _parseCoalitionMetricsFromEntry:].cold.2
- -[PLPowerMetricMonitorService _parseCoalitionMetricsFromEntry:].cold.3
- -[PLPowerMetricMonitorService _parseCoalitionMetricsFromEntry:].cold.4
- -[PLPowerMetricMonitorService _parseCoalitionMetricsFromEntry:].cold.5
- -[PLPowerMetricMonitorService _parseLocationMetricsFromEntry:].cold.3
- -[PLPowerMetricMonitorService _parseLocationMetricsFromEntry:].cold.4
- -[PLPowerMetricMonitorService _parseProcessNetworkMetricsFromEntry:].cold.2
- -[PLPowerMetricMonitorService _parseProcessNetworkMetricsFromEntry:].cold.3
- -[PLPowerMetricMonitorService setTrackedProcess:]
- -[PLPowerMetricMonitorService trackedProcess]
- GCC_except_table31
- GCC_except_table35
- GCC_except_table70
- GCC_except_table75
- _OBJC_IVAR_$_PLPowerMetricMonitorService._trackedProcess
- ___22-[PLDisplayAgent init]_block_invoke.1358
- ___22-[PLDisplayAgent init]_block_invoke.1358.cold.1
- ___22-[PLDisplayAgent init]_block_invoke.1358.cold.2
- ___22-[PLDisplayAgent init]_block_invoke.1358.cold.3
- ___22-[PLDisplayAgent init]_block_invoke.1358.cold.4
- ___22-[PLDisplayAgent init]_block_invoke.1369
- ___22-[PLDisplayAgent init]_block_invoke.1373
- ___22-[PLDisplayAgent init]_block_invoke.1377
- ___22-[PLDisplayAgent init]_block_invoke.1383
- ___22-[PLDisplayAgent init]_block_invoke.1383.cold.1
- ___22-[PLDisplayAgent init]_block_invoke.1383.cold.2
- ___22-[PLDisplayAgent init]_block_invoke.1401
- ___22-[PLDisplayAgent init]_block_invoke.1409
- ___22-[PLDisplayAgent init]_block_invoke_2.1360
- ___22-[PLDisplayAgent init]_block_invoke_2.1379
- ___22-[PLDisplayAgent init]_block_invoke_2.1379.cold.1
- ___22-[PLDisplayAgent init]_block_invoke_2.1379.cold.2
- ___22-[PLDisplayAgent init]_block_invoke_2.1395
- ___22-[PLDisplayAgent init]_block_invoke_2.1412
- ___38-[PLLocationAgent resyncActiveClients]_block_invoke.599
- ___40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1539
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1430
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1446
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1459
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1459.cold.1
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1459.cold.2
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1466
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1449
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1460
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1477
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1477.cold.1
- ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.1937
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.391
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.391.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.406
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.406.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.415
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.415.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.429
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.429.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.447
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.447.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.457
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.457.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.457.cold.2
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.464
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.489
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.489.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.499
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.499.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.504
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.504.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.512
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.512.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.517
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.517.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.525
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.525.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.533
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.533.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.392
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.407
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.416
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.430
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.449
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.458
- ___43-[PLPowerMetricMonitorService _setUpAgents]_block_invoke_10
- ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.578
- ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.584
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.541
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.541.cold.1
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.547
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.555
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.561
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.567
- ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.1985
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.639
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.646
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.649
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.655
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.661
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.667
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.674
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.680
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.686
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.692
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.698
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.699
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.702
- ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.1994
- ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.766
- ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.776
- ___56-[PLLocationAgent logEventForwardTechStatus_withLimiter]_block_invoke.575
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.609
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.615
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.621
- ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.149
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1662
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1669
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1674
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1674.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1680
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1680.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1691
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1691.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1692
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1692.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1693
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1693.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1694
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1694.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1695
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1695.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1696
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1696.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1696.cold.2
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1703
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1703.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1708
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1712
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1712.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1675
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1687
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1704
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1731
- ___73-[PLLocationAgent closeOpenEntryForClient:withOpenEntry:withTimeStopped:]_block_invoke.631
- ___76-[PLPowerMetricMonitorService _collectMetricsWithTimeout:completionHandler:]_block_invoke_2.cold.1
- ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.148
- ___block_literal_global.1767
- ___block_literal_global.1769
- ___block_literal_global.1771
- ___block_literal_global.1773
- ___block_literal_global.1775
- ___block_literal_global.1777
- ___block_literal_global.1779
- ___block_literal_global.1781
- ___block_literal_global.1783
- ___block_literal_global.1791
- ___block_literal_global.1830
- ___block_literal_global.1832
- ___block_literal_global.1834
- ___block_literal_global.1875
- ___block_literal_global.408
- __unnamed_array_storage.1292
- __unnamed_array_storage.1444
- __unnamed_array_storage.1445
- __unnamed_array_storage.1457
- __unnamed_array_storage.1860
- __unnamed_array_storage.1863
- __unnamed_array_storage.377
- __unnamed_array_storage.403
- __unnamed_array_storage.404
- __unnamed_array_storage.413
- __unnamed_array_storage.496
- __unnamed_array_storage.497
- __unnamed_array_storage.501
- __unnamed_array_storage.502
- __unnamed_array_storage.510
- __unnamed_array_storage.523
- __unnamed_array_storage.530
- __unnamed_array_storage.615
- __unnamed_array_storage.621
- __unnamed_array_storage.630
- __unnamed_array_storage.639
- __unnamed_array_storage.648
- __unnamed_array_storage.666
- __unnamed_array_storage.675
- __unnamed_array_storage.684
- _handleBrightnessClientNotification:withValue:.classDebugEnabled.1736
- _handleBrightnessClientNotification:withValue:.defaultOnce.1735
- _init.classDebugEnabled.1368
- _init.defaultOnce.1367
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.classDebugEnabled.546
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.defaultOnce.545
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.638
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.645
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.648
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.654
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.660
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.666
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.673
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.679
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.685
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.691
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.697
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.637
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.644
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.647
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.653
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.659
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.665
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.672
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.678
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.684
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.690
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.696
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.classDebugEnabled.463
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.defaultOnce.462
- _kPRearNits_block_invoke_2.classDebugEnabled.1400
- _kPRearNits_block_invoke_2.defaultOnce.1399
- _kPRearNits_block_invoke_3.classDebugEnabled.1465
- _kPRearNits_block_invoke_3.defaultOnce.1464
- _kPRearNits_block_invoke_4.classDebugEnabled.1661
- _kPRearNits_block_invoke_4.classDebugEnabled.1668
- _kPRearNits_block_invoke_4.defaultOnce.1660
- _kPRearNits_block_invoke_4.defaultOnce.1667
- _logEventForwardALSLux:.classDebugEnabled.1538
- _logEventForwardALSLux:.defaultOnce.1537
- _logEventForwardClientStatuswithPayload:.classDebugEnabled.608
- _logEventForwardClientStatuswithPayload:.classDebugEnabled.614
- _logEventForwardClientStatuswithPayload:.classDebugEnabled.620
- _logEventForwardClientStatuswithPayload:.defaultOnce.607
- _logEventForwardClientStatuswithPayload:.defaultOnce.613
- _logEventForwardClientStatuswithPayload:.defaultOnce.619
- _logEventForwardTechStatus.classDebugEnabled.577
- _logEventForwardTechStatus.classDebugEnabled.583
- _logEventForwardTechStatus.defaultOnce.576
- _logEventForwardTechStatus.defaultOnce.582
- _logEventPointClientStatus.classDebugEnabled.554
- _logEventPointClientStatus.classDebugEnabled.560
- _logEventPointClientStatus.classDebugEnabled.566
- _logEventPointClientStatus.defaultOnce.553
- _logEventPointClientStatus.defaultOnce.559
- _logEventPointClientStatus.defaultOnce.565
- _modelDisplayPowerFromIOMFB:.classDebugEnabled.1984
- _modelDisplayPowerFromIOMFB:.defaultOnce.1983
- _modelDynamicDisplayPower:.classDebugEnabled.1936
- _modelDynamicDisplayPower:.defaultOnce.1935
- _modelDynamicDisplayPowerFromAPL:.classDebugEnabled.1993
- _modelDynamicDisplayPowerFromAPL:.defaultOnce.1992
- _objc_msgSend$_parseCoalitionMetricsFromEntry:
- _objc_msgSend$setEnergyCost:
- _objc_msgSend$setEnergyOverhead:
- _objc_msgSend$setTrackedProcess:
- _objc_msgSend$trackedProcess
- _resyncActiveClients.classDebugEnabled.598
- _resyncActiveClients.defaultOnce.597
- _updateClientsLocationInfo:.classDebugEnabled.701
- _updateClientsLocationInfo:.defaultOnce.700
- _updateLocationDistributionEvents.classDebugEnabled.765
- _updateLocationDistributionEvents.classDebugEnabled.775
- _updateLocationDistributionEvents.defaultOnce.764
- _updateLocationDistributionEvents.defaultOnce.774
CStrings:
+ "\x0f\v\x11\x11\x14"
+ "\x12\x13"
+ "%@ (%d) bundle=%@ cid=<%llu>"
+ "%llu inst, %llu r, %llu w, %llu g"
+ "%s monitoring %@"
+ "@\"PLCoalitionSample\""
+ "Already monitoring process"
+ "Attempting to monitor multiple times"
+ "CPU_Inst"
+ "Disk_Read"
+ "Disk_Write"
+ "Metric collection timed out after %.2f seconds"
+ "MotionPacket"
+ "Not currently tracking a PID"
+ "Not tracking pid %@"
+ "PLCoalitionSample"
+ "Received MotionPacket XPC with payload=%@"
+ "T@\"NSMutableDictionary\",&,N,V_trackedProcesses"
+ "T@\"PLCoalitionSample\",&,V_coalitionSample"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_motionPacketListener"
+ "TQ,V_bytesread"
+ "TQ,V_byteswritten"
+ "TQ,V_gpuTime"
+ "TQ,V_instructions"
+ "_bytesread"
+ "_byteswritten"
+ "_coalitionSample"
+ "_gpuTime"
+ "_instructions"
+ "_motionPacketListener"
+ "_sampleCoalitions"
+ "aabParamsUpdateReason"
+ "alternativeE0a"
+ "alternativeE0b"
+ "alternativeE1"
+ "alternativeE2"
+ "alternativeL0a"
+ "alternativeL0b"
+ "alternativeL1"
+ "alternativeL2"
+ "alternativeThirdSlope"
+ "coalitionIDForPid:"
+ "coalitionSample"
+ "diffing against %@"
+ "entryEventPointDefinitionMotionPacket"
+ "failed to sample coalitions for %@"
+ "gpuTime"
+ "ignoring callback from %@"
+ "inactiveLength"
+ "inactiveStart"
+ "initial sample"
+ "instructions"
+ "logEventPointMotionPacket:"
+ "motionPacketListener"
+ "nitsDelta"
+ "nitsDeltaAlternative"
+ "nonWaking"
+ "sampling coalitions for %@ -> %@"
+ "setBytesRead:"
+ "setBytesWritten:"
+ "setBytesread:"
+ "setByteswritten:"
+ "setCoalitionSample:"
+ "setCpuInstructions:"
+ "setGpuTime:"
+ "setInstructions:"
+ "setMotionPacketListener:"
+ "setWifiAWDLRange:"
+ "setWifiAWDLStatus:"
+ "v32@?0@\"NSNumber\"8@\"PLProcessMetadata\"16^B24"
+ "wifiAWDLRange"
+ "wifiAWDLStatus"
- "\x0f\v\x11\x11\x13"
- "%s: Input coalition info does not have bundleID info. bundleId=%@, entry=%@"
- "%s: No matching PID. Tracked PID is %i, but received application PID is %i"
- "%s: Received coalition data for tracked process. bundleId=%@, entry=%@"
- "%s: Received network data for PID that is not being tracked"
- "%s: This process is not tracked. bundleId=%@, entry=%@"
- "%s: coalitionEntry=%@"
- "-[PLPowerMetricMonitorService _parseApplicationMetricsFromEntry:]"
- "-[PLPowerMetricMonitorService _parseCoalitionMetricsFromEntry:]"
- "@\"PLProcessMetadata\""
- "Already monitoring a process"
- "Attempting to monitor multiple PIDs"
- "Energy_Cost"
- "Energy_Overhead"
- "Metric collection timed out after %f seconds"
- "T@\"PLProcessMetadata\",&,N,V_trackedProcess"
- "_parseCoalitionMetricsFromEntry:"
- "_trackedProcess"
- "setEnergyCost:"
- "setEnergyOverhead:"
- "setTrackedProcess:"
- "trackedProcess"

```
