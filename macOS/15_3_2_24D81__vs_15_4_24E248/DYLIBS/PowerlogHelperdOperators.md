## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/Versions/A/PowerlogHelperdOperators`

```diff

-2308.80.23.0.0
-  __TEXT.__text: 0xfb75c
+2423.100.232.0.0
+  __TEXT.__text: 0xf9f30
   __TEXT.__auth_stubs: 0x1580
-  __TEXT.__objc_methlist: 0x7dac
-  __TEXT.__const: 0x2e4
-  __TEXT.__cstring: 0x136ea
-  __TEXT.__oslogstring: 0x7d88
-  __TEXT.__gcc_except_tab: 0x1d84
-  __TEXT.__unwind_info: 0x1e28
+  __TEXT.__objc_methlist: 0x82b0
+  __TEXT.__const: 0x304
+  __TEXT.__cstring: 0x125eb
+  __TEXT.__oslogstring: 0x8918
+  __TEXT.__gcc_except_tab: 0x1db4
+  __TEXT.__unwind_info: 0x1f38
   __TEXT.__objc_classname: 0x577
-  __TEXT.__objc_methname: 0x1bb67
-  __TEXT.__objc_methtype: 0x1981
-  __TEXT.__objc_stubs: 0x110a0
-  __DATA_CONST.__got: 0x8c0
-  __DATA_CONST.__const: 0x22d8
+  __TEXT.__objc_methname: 0x1c240
+  __TEXT.__objc_methtype: 0x1982
+  __TEXT.__objc_stubs: 0x11420
+  __DATA_CONST.__got: 0x8d0
+  __DATA_CONST.__const: 0x2370
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_nlclslist: 0xa8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5830
+  __DATA_CONST.__objc_selrefs: 0x5a68
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__objc_arraydata: 0x1eb0
+  __DATA_CONST.__objc_arraydata: 0x1f50
   __AUTH_CONST.__auth_got: 0xad8
-  __AUTH_CONST.__const: 0x2608
-  __AUTH_CONST.__cfstring: 0x1e240
-  __AUTH_CONST.__objc_const: 0xa170
+  __AUTH_CONST.__const: 0x26b8
+  __AUTH_CONST.__cfstring: 0x1e060
+  __AUTH_CONST.__objc_const: 0x9d40
   __AUTH_CONST.__objc_doubleobj: 0x630
-  __AUTH_CONST.__objc_intobj: 0x1110
-  __AUTH_CONST.__objc_dictobj: 0x1770
+  __AUTH_CONST.__objc_intobj: 0x1128
+  __AUTH_CONST.__objc_dictobj: 0x1838
   __AUTH_CONST.__objc_arrayobj: 0xae0
   __AUTH.__objc_data: 0xaa0
-  __DATA.__objc_ivar: 0x9c0
+  __DATA.__objc_ivar: 0x9e8
   __DATA.__data: 0x2d8
-  __DATA.__bss: 0x16d8
+  __DATA.__bss: 0x1290
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 56ACB40D-1CF7-3173-BB02-6F8CB9E9F60D
-  Functions: 4235
-  Symbols:   10503
-  CStrings:  13149
+  UUID: 55B39277-6525-3ED5-9865-34D377794114
+  Functions: 4357
+  Symbols:   10500
+  CStrings:  13219
 
Symbols:
+ +[PLBatteryAgent hasChargingInfoLogging].cold.1
+ +[PLBatteryAgent shouldLogBTM].cold.1
+ +[PLBatteryAgent shouldLogCPMS].cold.1
+ +[PLBatteryAgent shouldLogPPMDebugDetail].cold.1
+ +[PLBatteryAgent supportsxFlags].cold.1
+ +[PLDisplayAgent dcpSubFrameMap]
+ +[PLDisplayAgent shouldLogALSPowerSaved].cold.1
+ +[PLDisplayAgent shouldLogBLR].cold.1
+ +[PLDisplayAgent shouldLogBacklightControl].cold.1
+ +[PLDisplayAgent shouldLogDisplay].cold.1
+ +[PLDisplayAgent shouldLogFromDCP].cold.1
+ +[PLDisplayAgent shouldLogKeyboardBrightness].cold.1
+ +[PLDisplayAgent shouldLogLCD].cold.1
+ +[PLDisplayAgent shouldLogTouch].cold.1
+ +[PLDisplayAgent shouldLogUserBrightness].cold.1
+ +[PLDisplayAgent shouldModelPowerFromAPL].cold.1
+ +[PLDisplayAgent shouldModelPowerFromIOMFB].cold.1
+ +[PLProcessCPUWrapper start].cold.1
+ +[PLProcessMonitorAgent enableThreadStatsLogging].cold.1
+ +[PLPushAgent entryEventPointDefinitionIncomingPushProxyMessages]
+ +[PLPushAgent entryEventPointDefinitionOutgoingPushProxyMessages]
+ +[PLSMCAgent entryEventNoneDefinitionColdBoot]
+ +[PLSMCAgent reportPMUEventsToCA:].cold.1
+ +[PLUtilities AppDeletionEnabled].cold.1
+ +[PLUtilities MavRevStringQuery].cold.1
+ +[PLUtilities OverrideAllowlistEnabled].cold.1
+ +[PLUtilities PreUnlockTelemetryEnabled].cold.1
+ +[PLUtilities SwitchToIncrementalVacuumEnabled].cold.1
+ +[PLUtilities bundleIDFromProcessName:].cold.1
+ +[PLUtilities cleanLaunchdName:].cold.2
+ +[PLUtilities crashReporterKey].cold.1
+ +[PLUtilities devBoardDevice].cold.1
+ +[PLUtilities deviceBootArgs].cold.1
+ +[PLUtilities deviceBootTime].cold.1
+ +[PLUtilities deviceRebooted].cold.1
+ +[PLUtilities getDeviceSoC].cold.1
+ +[PLUtilities getHardwarePerfLevels].cold.1
+ +[PLUtilities getJetsamPriority:]
+ +[PLUtilities getJetsamPriority:].cold.1
+ +[PLUtilities getMachTimebase].cold.1
+ +[PLUtilities getMachbaseTimeRatio].cold.1
+ +[PLUtilities grabSysctlValue:]
+ +[PLUtilities grabSysctlValue:].cold.1
+ +[PLUtilities grabSysctlValue:].cold.2
+ +[PLUtilities hardwareModel].cold.1
+ +[PLUtilities hasBattery].cold.1
+ +[PLUtilities inBUIDemoMode].cold.1
+ +[PLUtilities isFullModeDaemon].cold.1
+ +[PLUtilities isLiteModeDaemon].cold.1
+ +[PLUtilities isPowerlogHelperd].cold.1
+ +[PLUtilities launchdNameToProcessName:].cold.1
+ +[PLUtilities postNotificationName:object:userInfo:].cold.1
+ +[PLUtilities productType].cold.1
+ +[PLUtilities runningAsUser].cold.1
+ +[PLUtilities workQueueForKey:].cold.1
+ +[PLXPCAgent shouldLogiOSWatchOSOnly].cold.1
+ -[PLBatteryAgent logEventNoneBatteryConfigWithRawData:].cold.9
+ -[PLBatteryUIResponderService demoMode].cold.1
+ -[PLBatteryUIResponderService demoPath].cold.1
+ -[PLCameraAgent refreshMacOSCameraDeviceList].cold.3
+ -[PLCoalitionAgent getCPUWeightFromEntry:].cold.1
+ -[PLCoalitionAgent getGPUWeightFromEntry:].cold.1
+ -[PLCoalitionSample cpuEnergy]
+ -[PLCoalitionSample setCpuEnergy:]
+ -[PLDisplayAgent HDRHeadroom]
+ -[PLDisplayAgent getIOMFBSubFrameMap].cold.1
+ -[PLDisplayAgent logEventForwardLinearBrightness:].cold.1
+ -[PLDisplayAgent setHDRHeadroom:]
+ -[PLPowerMetricMonitorService _cancelBrightnessTimer]
+ -[PLPowerMetricMonitorService _parseAverageFPS:]
+ -[PLPowerMetricMonitorService _parseDisplayAZLMetricsFromEntry:cacheMetrics:]
+ -[PLPowerMetricMonitorService _setUpIOReporting].cold.5
+ -[PLPowerMetricMonitorService _startBrightnessTimer]
+ -[PLPowerMetricMonitorService _updateDisplayMetrics]
+ -[PLPowerMetricMonitorService _updateMetricsWithThermalState].cold.1
+ -[PLPowerMetricMonitorService addBrightnessSample]
+ -[PLPowerMetricMonitorService dcpScanoutStats]
+ -[PLPowerMetricMonitorService setDcpScanoutStats:]
+ -[PLPowerMetricMonitorService updateBrightnessMetrics]
+ -[PLPushAgent convertMessageProtocol:]
+ -[PLPushAgent convertMessageProtocol:].cold.1
+ -[PLPushAgent handleMessageEvent:isSentEvent:]
+ -[PLPushAgent handleMessageEvent:isSentEvent:].cold.1
+ -[PLPushAgent logPushProxyMessages:forMessageType:]
+ -[PLPushAgent logPushProxyMessages:forMessageType:].cold.1
+ -[PLPushAgent messageReceivedListener]
+ -[PLPushAgent messageSentListener]
+ -[PLPushAgent pushProxyIncomingListener]
+ -[PLPushAgent pushProxyOutgoingListener]
+ -[PLPushAgent setMessageReceivedListener:]
+ -[PLPushAgent setMessageSentListener:]
+ -[PLPushAgent setPushProxyIncomingListener:]
+ -[PLPushAgent setPushProxyOutgoingListener:]
+ -[PLSMCAgent DRAMVendorKey].cold.1
+ -[PLSMCAgent accumulatedKeys].cold.1
+ -[PLSMCAgent displayAccumulatedKeys].cold.1
+ -[PLSMCAgent fanNoiseKey].cold.1
+ -[PLSMCAgent logColdBoot]
+ -[PLSMCAgent logColdBoot].cold.1
+ -[PLSMCAgent metricMonitorInstantKeys].cold.1
+ -[PLSMCAgent powerAccumulatedKeys].cold.1
+ -[PLSMCAgent powerDeliveryKeys].cold.1
+ -[PLSMCAgent powerDeliveryResetKeys].cold.1
+ -[PLSMCAgent thermalAccumulatedKeys].cold.1
+ -[PLSMCAgent thermalInstantKeys].cold.1
+ -[PLSMCAgent thermalKeys].cold.1
+ -[PLSMCAgent thermalPressureKey].cold.1
+ -[PLXPCAgent MessageForegroundXPCListener]
+ -[PLXPCAgent logEventEventForwardMessageTranscript:]
+ -[PLXPCAgent logEventEventForwardMessageTranscript:].cold.1
+ -[PLXPCAgent logSleepBedtime:]
+ -[PLXPCAgent logSleepWaketime:]
+ -[PLXPCAgent setMessageForegroundXPCListener:]
+ -[PLXPCAgent setSummarizedNotificationEntries:]
+ -[PLXPCAgent summarizedNotificationEntries]
+ -[ProcessMemoryUsage setTimeAtPriorityMATU:]
+ -[ProcessMemoryUsage timeAtPriorityMATU]
+ GCC_except_table115
+ GCC_except_table131
+ GCC_except_table31
+ GCC_except_table42
+ GCC_except_table462
+ GCC_except_table52
+ GCC_except_table56
+ GCC_except_table61
+ GCC_except_table67
+ OBJC_IVAR_$_PLCoalitionSample._cpuEnergy
+ OBJC_IVAR_$_PLDisplayAgent._HDRHeadroom
+ OBJC_IVAR_$_PLPowerMetricMonitorService._dcpScanoutStats
+ OBJC_IVAR_$_PLPushAgent._messageReceivedListener
+ OBJC_IVAR_$_PLPushAgent._messageSentListener
+ OBJC_IVAR_$_PLPushAgent._pushProxyIncomingListener
+ OBJC_IVAR_$_PLPushAgent._pushProxyOutgoingListener
+ OBJC_IVAR_$_PLXPCAgent._MessageForegroundXPCListener
+ OBJC_IVAR_$_PLXPCAgent._summarizedNotificationEntries
+ OBJC_IVAR_$_ProcessMemoryUsage._timeAtPriorityMATU
+ PLLogApplicationMac.cold.1
+ PLLogBH.cold.1
+ PLLogCamera.cold.1
+ PLLogCoalition.cold.1
+ PLLogCommon.cold.1
+ PLLogDisplay.cold.1
+ PLLogLocation.__logObj
+ PLLogLocation.cold.1
+ PLLogLocation.onceToken
+ PLLogNetwork.cold.1
+ PLLogPower.cold.1
+ PLLogPowerMetricMonitor.cold.1
+ PLLogPowerSignpost.cold.1
+ PLLogProcessMonitor.cold.1
+ PLLogPush.cold.1
+ PLLogSMC.cold.1
+ PLLogSQLiteConnection.cold.1
+ PLLogScreenState.cold.1
+ PLLogSleepWake.__logObj
+ PLLogSleepWake.cold.1
+ PLLogSleepWake.onceToken
+ PLLogSoC.cold.1
+ PLLogSubmission.cold.1
+ PLLogXPC.cold.1
+ PLLogZlib.cold.1
+ PowerChangedCallback.classDebugEnabled.405
+ PowerChangedCallback.classDebugEnabled.411
+ PowerChangedCallback.classDebugEnabled.421
+ PowerChangedCallback.classDebugEnabled.427
+ PowerChangedCallback.defaultOnce.404
+ PowerChangedCallback.defaultOnce.410
+ PowerChangedCallback.defaultOnce.420
+ PowerChangedCallback.defaultOnce.426
+ _PLLogLocation
+ _PLLogSleepWake
+ __22-[PLDisplayAgent init]_block_invoke.1181
+ __22-[PLDisplayAgent init]_block_invoke.1190
+ __22-[PLDisplayAgent init]_block_invoke.1190.cold.1
+ __22-[PLDisplayAgent init]_block_invoke.1190.cold.2
+ __22-[PLDisplayAgent init]_block_invoke.1190.cold.3
+ __22-[PLDisplayAgent init]_block_invoke.1190.cold.4
+ __22-[PLDisplayAgent init]_block_invoke.1200
+ __22-[PLDisplayAgent init]_block_invoke.1204
+ __22-[PLDisplayAgent init]_block_invoke.1210
+ __22-[PLDisplayAgent init]_block_invoke.1214
+ __22-[PLDisplayAgent init]_block_invoke.1214.cold.1
+ __22-[PLDisplayAgent init]_block_invoke.1214.cold.2
+ __22-[PLDisplayAgent init]_block_invoke.1218
+ __22-[PLDisplayAgent init]_block_invoke.1218.cold.1
+ __22-[PLDisplayAgent init]_block_invoke.1218.cold.2
+ __22-[PLDisplayAgent init]_block_invoke.1236
+ __22-[PLDisplayAgent init]_block_invoke.1246
+ __22-[PLDisplayAgent init]_block_invoke.1258
+ __22-[PLDisplayAgent init]_block_invoke.1258.cold.1
+ __22-[PLDisplayAgent init]_block_invoke.1258.cold.2
+ __22-[PLDisplayAgent init]_block_invoke.1265
+ __22-[PLDisplayAgent init]_block_invoke_2.1230
+ __22-[PLDisplayAgent init]_block_invoke_2.1248
+ __22-[PLDisplayAgent init]_block_invoke_2.1259
+ __23-[PLLocationAgent init]_block_invoke.258
+ __23-[PLLocationAgent init]_block_invoke.258.cold.1
+ __30-[PLCoalitionAgent logToAggd:]_block_invoke.705
+ __33+[PLPushAgent bundleIdFromTopic:]_block_invoke.330
+ __34+[PLSMCAgent reportPMUEventsToCA:]_block_invoke.1236
+ __37-[PLXPCAgent logEventForwardGMSOptIn]_block_invoke.2410
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1033
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1042
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1042.cold.1
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1042.cold.2
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1042.cold.3
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1042.cold.4
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1043
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1050
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke_2.1051
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1643
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1643.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1651
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1651.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1659
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1659.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1667
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1667.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1675
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1675.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1683
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1683.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1691
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1691.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1699
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1699.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1707
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1707.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1718
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1718.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1729
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1729.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1740
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1740.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1751
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1751.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1762
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1762.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1773
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1773.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1780
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1780.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1788
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1788.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1793
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1793.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1800
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1800.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1807
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1815
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1815.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1822
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1822.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1827
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1827.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1837
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1837.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1845
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1845.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1853
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1853.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1858
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1858.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1866
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1866.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1874
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1874.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1884
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1884.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1894
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1894.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1901
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1901.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1911
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1911.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1918
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1918.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1928
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1928.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1938
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1938.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1948
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1948.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1968
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1968.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1978
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1978.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1986
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1986.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1994
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1994.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2004
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2004.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2014
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2014.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2022
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2022.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2032
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2032.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2042
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2042.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2052
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2052.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2062
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2062.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2070
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2070.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2078
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2078.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2083
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2083.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2088
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2088.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2093
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2093.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2098
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2098.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2105
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2105.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2110
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2110.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2115
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2115.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2120
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2120.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2127
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2127.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2134
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2134.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2144
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2144.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2152
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2152.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2160
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2160.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2168
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2168.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2176
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2176.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2181
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2181.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2191
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2191.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2198
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2198.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2208
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2208.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2218
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2218.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2228
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2228.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2238
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2238.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2245
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2245.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2253
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2253.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2261
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2261.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2268
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2268.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2273
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2273.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2280
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2280.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2285
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2285.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2293
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2293.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2298
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2298.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2306
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2306.cold.1
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2319
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2319.cold.1
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.190
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.190.cold.1
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.199
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.199.cold.1
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.207
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.207.cold.1
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.215
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.215.cold.1
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.223
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.223.cold.1
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.231
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.231.cold.1
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.233
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.244
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.244.cold.1
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.255
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.255.cold.1
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.263
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.263.cold.1
+ __40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1457
+ __41-[PLProcessNetworkAgent didAddNewSource:]_block_invoke.216
+ __41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.1129
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1280
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1281
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1293
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1298
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1299
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1299.cold.1
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1299.cold.2
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1299.cold.3
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1309
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1321
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1332
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1332.cold.1
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1338
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1348
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1348.cold.1
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1359
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1363
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1363.cold.1
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1363.cold.2
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1370
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1300
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1333
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1349
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1364
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1547
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1547.cold.1
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1559
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1559.cold.1
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1574
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1574.cold.1
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1584
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1584.cold.1
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1596
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1596.cold.1
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1608
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1608.cold.1
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1625
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1625.cold.1
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1632
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1632.cold.1
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.293
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.293.cold.1
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.307
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.307.cold.1
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.315
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.315.cold.1
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.320
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.320.cold.1
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.325
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.325.cold.1
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.333
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.333.cold.1
+ __43-[PLPowerMetricMonitorService _setUpAgents]_block_invoke.274
+ __43-[PLPowerMetricMonitorService _setUpAgents]_block_invoke.277
+ __43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.1111
+ __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.440
+ __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.440.cold.1
+ __44-[PLLocationAgent logEventPointClientStatus]_block_invoke.cold.1
+ __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.cold.2
+ __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.cold.3
+ __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.cold.4
+ __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.cold.5
+ __46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.247
+ __46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.247.cold.1
+ __49-[PLCoalitionAgent logCoalitionObjectDifference:]_block_invoke.743
+ __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.188
+ __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.196
+ __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.201
+ __50-[PLDisplayAgent logEventForwardLinearBrightness:]_block_invoke.1554
+ __50-[PLDisplayAgent logEventForwardLinearBrightness:]_block_invoke.1554.cold.1
+ __53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.239
+ __53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.239.cold.1
+ __55-[PLPowerMetricMonitorService initOperatorDependancies]_block_invoke.231
+ __58-[PLProcessNetworkAgent logEventBackwardUsageWithOutcome:]_block_invoke.265
+ __58-[PLProcessNetworkAgent logEventBackwardUsageWithOutcome:]_block_invoke.268
+ __61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.238
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1574
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1581
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1586
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1586.cold.1
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1594
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1594.cold.1
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1605
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1605.cold.1
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1606
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1606.cold.1
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1606.cold.2
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1619
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1619.cold.1
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1621
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1625
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1625.cold.1
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1650
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1651
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1651.cold.1
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1587
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1601
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1620
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1644
+ __65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.245
+ __65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.245.cold.1
+ __76-[PLPowerMetricMonitorService _collectMetricsWithTimeout:completionHandler:]_block_invoke.312
+ __76-[PLPowerMetricMonitorService _collectMetricsWithTimeout:completionHandler:]_block_invoke.314
+ __76-[PLPowerMetricMonitorService _collectMetricsWithTimeout:completionHandler:]_block_invoke.314.cold.1
+ __83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.235
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.472
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.566
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.572
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.621
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_2.634
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_3.641
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_4.648
+ __PowerChangedCallback_block_invoke.406
+ __PowerChangedCallback_block_invoke.412
+ __PowerChangedCallback_block_invoke.416
+ __PowerChangedCallback_block_invoke.416.cold.1
+ __PowerChangedCallback_block_invoke.422
+ __PowerChangedCallback_block_invoke.428
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN12PLProcessCPU12inode_data_tEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEE5resetB8ne190102EPS7_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKyN12PLProcessCPU12inode_data_tEEELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___32+[PLDisplayAgent dcpSubFrameMap]_block_invoke
+ ___48-[PLPowerMetricMonitorService _parseAverageFPS:]_block_invoke
+ ___PLLogLocation_block_invoke
+ ___PLLogSleepWake_block_invoke
+ ___block_descriptor_37_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24l
+ ___block_descriptor_48_e8_32s_e17_v16?0"PLEntry"8l
+ ___block_descriptor_56_e8_32s40r48r_e15_v32?0816^B24l
+ __block_literal_global.1045
+ __block_literal_global.1143
+ __block_literal_global.1145
+ __block_literal_global.1147
+ __block_literal_global.1149
+ __block_literal_global.1151
+ __block_literal_global.1153
+ __block_literal_global.1155
+ __block_literal_global.1193
+ __block_literal_global.1195
+ __block_literal_global.1209
+ __block_literal_global.1232
+ __block_literal_global.1512
+ __block_literal_global.1680
+ __block_literal_global.1682
+ __block_literal_global.1684
+ __block_literal_global.1686
+ __block_literal_global.1688
+ __block_literal_global.1690
+ __block_literal_global.1692
+ __block_literal_global.1694
+ __block_literal_global.1699
+ __block_literal_global.1769
+ __block_literal_global.1771
+ __block_literal_global.1787
+ __block_literal_global.186
+ __block_literal_global.189
+ __block_literal_global.2308
+ __block_literal_global.274
+ __block_literal_global.282
+ __block_literal_global.290
+ __block_literal_global.295
+ __block_literal_global.303
+ __block_literal_global.316
+ __block_literal_global.324
+ __block_literal_global.326
+ __block_literal_global.416
+ __block_literal_global.419
+ __block_literal_global.422
+ __block_literal_global.425
+ __block_literal_global.430
+ __block_literal_global.465
+ __block_literal_global.478
+ __block_literal_global.506
+ __block_literal_global.595
+ __block_literal_global.597
+ __block_literal_global.608
+ __block_literal_global.610
+ __block_literal_global.615
+ __block_literal_global.620
+ __block_literal_global.623
+ __block_literal_global.627
+ __block_literal_global.630
+ __block_literal_global.633
+ __block_literal_global.636
+ __block_literal_global.748
+ __block_literal_global.750
+ __block_literal_global.828
+ __fakeSleep_block_invoke.361
+ __fakeSleep_block_invoke.373
+ __fakeSleep_block_invoke.377
+ __fakeSleep_block_invoke.377.cold.1
+ __fakeSleep_block_invoke.385
+ _assistantdProcessName
+ _kPLBB23C
+ _kPLPushAgentConversationType
+ _kPLPushAgentEventPointIncomingProxyMessages
+ _kPLPushAgentEventPointOutgoingProxyMessages
+ _kPLPushAgentGUIDSubStrLength
+ _kPLPushAgentMessageGUID
+ _kPLPushAgentMessageType
+ _kPLPushAgentProtocol
+ _kPLPushAgentProxyCommand
+ _kPLPushAgentProxyCommandCount
+ _kPLPushAgentPushType
+ _kPLPushAgentSource
+ _kPLPushAgentTarget
+ _kPLSMCAgentEventNoneColdBoot
+ _kUsageNetworkBtInBytes
+ _kUsageNetworkBtOutBytes
+ _memcpy
+ _objc_msgSend$HDRHeadroom
+ _objc_msgSend$_cancelBrightnessTimer
+ _objc_msgSend$_parseAverageFPS:
+ _objc_msgSend$_parseDisplayAPLMetricsFromEntry:cacheMetrics:
+ _objc_msgSend$_parseDisplayAZLMetricsFromEntry:cacheMetrics:
+ _objc_msgSend$_updateDisplayMetrics
+ _objc_msgSend$convertMessageProtocol:
+ _objc_msgSend$cpuEnergy
+ _objc_msgSend$dcpScanoutStats
+ _objc_msgSend$dcpSubFrameMap
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$displayAZL
+ _objc_msgSend$entryEventNoneDefinitionColdBoot
+ _objc_msgSend$entryEventPointDefinitionIncomingPushProxyMessages
+ _objc_msgSend$entryEventPointDefinitionOutgoingPushProxyMessages
+ _objc_msgSend$getJetsamPriority:
+ _objc_msgSend$handleMessageEvent:isSentEvent:
+ _objc_msgSend$logColdBoot
+ _objc_msgSend$logEventEventForwardMessageTranscript:
+ _objc_msgSend$logPushProxyMessages:forMessageType:
+ _objc_msgSend$setDcpScanoutStats:
+ _objc_msgSend$setDisplayAZL:
+ _objc_msgSend$setDisplayFPS:
+ _objc_msgSend$setHDRHeadroom:
+ _objc_msgSend$setMessageForegroundXPCListener:
+ _objc_msgSend$setMessageReceivedListener:
+ _objc_msgSend$setMessageSentListener:
+ _objc_msgSend$setPushProxyIncomingListener:
+ _objc_msgSend$setPushProxyOutgoingListener:
+ _objc_msgSend$setScanoutFPS:
+ _objc_msgSend$setTimeAtPriorityMATU:
+ _objc_msgSend$timeAtPriorityMATU
+ dcpSubFrameMap.onceToken
+ dcpSubFrameMap.subFrameMap
+ fakeSleep.classDebugEnabled.360
+ fakeSleep.classDebugEnabled.372
+ fakeSleep.classDebugEnabled.384
+ fakeSleep.defaultOnce.359
+ fakeSleep.defaultOnce.371
+ fakeSleep.defaultOnce.383
+ handleBrightnessClientNotification:withValue:.classDebugEnabled.1649
+ handleBrightnessClientNotification:withValue:.defaultOnce.1648
+ init.classDebugEnabled.1180
+ init.classDebugEnabled.1199
+ init.defaultOnce.1179
+ init.defaultOnce.1198
+ initOperatorDependancies.classDebugEnabled.1358
+ initOperatorDependancies.defaultOnce.1357
+ kPRearNits_block_invoke_2.classDebugEnabled.1235
+ kPRearNits_block_invoke_2.defaultOnce.1234
+ kPRearNits_block_invoke_3.classDebugEnabled.1264
+ kPRearNits_block_invoke_3.defaultOnce.1263
+ kPRearNits_block_invoke_4.classDebugEnabled.1308
+ kPRearNits_block_invoke_4.classDebugEnabled.1320
+ kPRearNits_block_invoke_4.defaultOnce.1307
+ kPRearNits_block_invoke_4.defaultOnce.1319
+ kPRearNits_block_invoke_7.classDebugEnabled.1369
+ kPRearNits_block_invoke_7.defaultOnce.1368
+ kPRearNits_block_invoke_8.classDebugEnabled.1573
+ kPRearNits_block_invoke_8.classDebugEnabled.1580
+ kPRearNits_block_invoke_8.defaultOnce.1572
+ kPRearNits_block_invoke_8.defaultOnce.1579
+ logCoalitionObjectDifference:.classDebugEnabled.742
+ logCoalitionObjectDifference:.defaultOnce.741
+ logEventForwardALSLux:.classDebugEnabled.1456
+ logEventForwardALSLux:.defaultOnce.1455
+ logHandle.cold.1
+ readKeyViaOSAccum:toOutput:.classDebugEnabled.1128
+ readKeyViaOSAccum:toOutput:.defaultOnce.1127
- +[PLUtilities getJetamPriority:]
- +[PLUtilities getJetamPriority:].cold.1
- -[PLLocationAgent updateLocalCacheWithClient:withType:withBundleID:withEntry:].cold.1
- -[PLPowerMetricMonitorService _parseDCPSwapStats:]
- -[PLProcessNetworkAgent timestampNetConnectEntry:withEventType:withSource:].cold.3
- -[PLSleepWakeAgent capabilitiesChanged:].cold.2
- -[PLSleepWakeAgent capabilitiesChanged:].cold.3
- -[PLSleepWakeAgent logSleepEntries:].cold.3
- -[PLSleepWakeAgent logWakeEntries:withCurrentTime:].cold.2
- GCC_except_table109
- GCC_except_table15
- GCC_except_table30
- GCC_except_table458
- GCC_except_table51
- GCC_except_table59
- GCC_except_table63
- GCC_except_table68
- PowerChangedCallback.classDebugEnabled.499
- PowerChangedCallback.classDebugEnabled.505
- PowerChangedCallback.classDebugEnabled.515
- PowerChangedCallback.classDebugEnabled.521
- PowerChangedCallback.defaultOnce.498
- PowerChangedCallback.defaultOnce.504
- PowerChangedCallback.defaultOnce.514
- PowerChangedCallback.defaultOnce.520
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- __22-[PLDisplayAgent init]_block_invoke.1178
- __22-[PLDisplayAgent init]_block_invoke.1187
- __22-[PLDisplayAgent init]_block_invoke.1187.cold.1
- __22-[PLDisplayAgent init]_block_invoke.1187.cold.2
- __22-[PLDisplayAgent init]_block_invoke.1187.cold.3
- __22-[PLDisplayAgent init]_block_invoke.1187.cold.4
- __22-[PLDisplayAgent init]_block_invoke.1197
- __22-[PLDisplayAgent init]_block_invoke.1201
- __22-[PLDisplayAgent init]_block_invoke.1207
- __22-[PLDisplayAgent init]_block_invoke.1211
- __22-[PLDisplayAgent init]_block_invoke.1211.cold.1
- __22-[PLDisplayAgent init]_block_invoke.1211.cold.2
- __22-[PLDisplayAgent init]_block_invoke.1215
- __22-[PLDisplayAgent init]_block_invoke.1215.cold.1
- __22-[PLDisplayAgent init]_block_invoke.1215.cold.2
- __22-[PLDisplayAgent init]_block_invoke.1233
- __22-[PLDisplayAgent init]_block_invoke.1243
- __22-[PLDisplayAgent init]_block_invoke.1255
- __22-[PLDisplayAgent init]_block_invoke.1255.cold.1
- __22-[PLDisplayAgent init]_block_invoke.1255.cold.2
- __22-[PLDisplayAgent init]_block_invoke.1262
- __22-[PLDisplayAgent init]_block_invoke_2.1227
- __22-[PLDisplayAgent init]_block_invoke_2.1245
- __22-[PLDisplayAgent init]_block_invoke_2.1256
- __23-[PLLocationAgent init]_block_invoke.263
- __23-[PLLocationAgent init]_block_invoke.263.cold.1
- __23-[PLLocationAgent init]_block_invoke_2.264
- __30-[PLCoalitionAgent logToAggd:]_block_invoke.685
- __33+[PLPushAgent bundleIdFromTopic:]_block_invoke.274
- __34+[PLSMCAgent reportPMUEventsToCA:]_block_invoke.1200
- __36-[PLSleepWakeAgent logSleepEntries:]_block_invoke.184
- __36-[PLSleepWakeAgent logSleepEntries:]_block_invoke.193
- __37-[PLXPCAgent logEventForwardGMSOptIn]_block_invoke.2399
- __38-[PLLocationAgent resyncActiveClients]_block_invoke.433
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1027
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1030
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1036.cold.1
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1036.cold.2
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1036.cold.3
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1037
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1044
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke_2.1045
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1648
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1648.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1656
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1656.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1664
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1664.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1672
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1672.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1680
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1680.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1688
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1688.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1696
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1696.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1704
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1704.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1712
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1712.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1723
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1723.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1734
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1734.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1745
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1745.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1756
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1756.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1767
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1767.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1777
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1777.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1785
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1785.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1790
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1790.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1797
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1797.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1804
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1812
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1812.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1819
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1819.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1824
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1824.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1834
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1834.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1842
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1842.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1850
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1850.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1855
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1855.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1863
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1863.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1873
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1873.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1883
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1883.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1890
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1890.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1900
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1900.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1907
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1907.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1917
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1917.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1927
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1927.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1937
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1937.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1946
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1946.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1967
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1967.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1975
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1975.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1983
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1983.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1993
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1993.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2003
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2003.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2011
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2011.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2021
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2021.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2031
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2031.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2041
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2041.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2051
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2051.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2059
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2059.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2067
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2067.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2072
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2072.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2077
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2077.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2082
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2082.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2087
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2087.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2094
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2094.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2099
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2099.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2104
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2104.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2109
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2109.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2116
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2116.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2123
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2123.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2133
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2133.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2141
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2141.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2149
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2149.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2157
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2157.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2165
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2165.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2170
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2170.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2180
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2180.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2187
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2187.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2197
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2197.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2207
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2207.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2217
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2217.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2227
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2227.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2234
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2234.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2242
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2242.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2250
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2250.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2257
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2257.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2262
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2262.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2269
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2269.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2274
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2274.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2282
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2282.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2287
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2287.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2295
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2295.cold.1
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2308
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2308.cold.1
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.160
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.160.cold.1
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.175
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.175.cold.1
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.183
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.183.cold.1
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.191
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.191.cold.1
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.197
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.208
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.208.cold.1
- __39-[PLPushAgent initOperatorDependancies]_block_invoke_2.192
- __40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1454
- __40-[PLSleepWakeAgent capabilitiesChanged:]_block_invoke.168
- __40-[PLSleepWakeAgent capabilitiesChanged:]_block_invoke.174
- __41-[PLProcessNetworkAgent didAddNewSource:]_block_invoke.210
- __41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.1117
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1277
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1278
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1290
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1295
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1296
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1296.cold.1
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1296.cold.2
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1296.cold.3
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1306
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1318
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1329
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1329.cold.1
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1335
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1345
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1345.cold.1
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1356
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1360
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1360.cold.1
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1360.cold.2
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1367
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1297
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1330
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1346
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1361
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1544
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1544.cold.1
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1557
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1557.cold.1
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1569
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1569.cold.1
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1579
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1579.cold.1
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1594
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1594.cold.1
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1606
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1606.cold.1
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1623
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1623.cold.1
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1630
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1630.cold.1
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1637
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1637.cold.1
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.305
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.305.cold.1
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.323
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.323.cold.1
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.335
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.335.cold.1
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.344
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.344.cold.1
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.353
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.353.cold.1
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.361
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.361.cold.1
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.306
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.324
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.336
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.345
- __43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.1105
- __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.430
- __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.430.cold.1
- __44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.412
- __44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.418
- __44-[PLLocationAgent logEventPointClientStatus]_block_invoke.369
- __44-[PLLocationAgent logEventPointClientStatus]_block_invoke.369.cold.1
- __44-[PLLocationAgent logEventPointClientStatus]_block_invoke.375
- __44-[PLLocationAgent logEventPointClientStatus]_block_invoke.383
- __44-[PLLocationAgent logEventPointClientStatus]_block_invoke.389
- __44-[PLLocationAgent logEventPointClientStatus]_block_invoke.395
- __44-[PLSleepWakeAgent logEventPointKernelState]_block_invoke.155
- __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.471
- __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.475
- __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.481
- __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.487
- __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.493
- __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.499
- __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.503
- __45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.506
- __46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.275
- __46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.275.cold.1
- __46-[PLSleepWakeAgent logEventNonePowerNapConfig]_block_invoke.284
- __49-[PLCoalitionAgent logCoalitionObjectDifference:]_block_invoke.723
- __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.182
- __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.190
- __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.195
- __49-[PLSleepWakeAgent registerForCapabilitiesChange]_block_invoke.214
- __50-[PLDisplayAgent logEventForwardLinearBrightness:]_block_invoke.1551
- __50-[PLDisplayAgent logEventForwardLinearBrightness:]_block_invoke.1551.cold.1
- __51-[PLSleepWakeAgent logWakeEntries:withCurrentTime:]_block_invoke.197
- __51-[PLSleepWakeAgent registerForUserIdleNotification]_block_invoke.223
- __53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.234
- __53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.234.cold.1
- __53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke.296
- __53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke.306
- __53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke.327
- __53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke.334
- __55-[PLPowerMetricMonitorService initOperatorDependancies]_block_invoke.226
- __56-[PLLocationAgent logEventForwardTechStatus_withLimiter]_block_invoke.407
- __58-[PLLocationAgent logEventForwardClientStatus_withLimiter]_block_invoke.403
- __58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.443
- __58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.449
- __58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.455
- __58-[PLProcessNetworkAgent logEventBackwardUsageWithOutcome:]_block_invoke.293
- __58-[PLProcessNetworkAgent logEventBackwardUsageWithOutcome:]_block_invoke.296
- __60-[PLLocationAgent logEventNoneClientStatusDebugWithClients:]_block_invoke.cold.1
- __61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.233
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1571
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1578
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1583
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1583.cold.1
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1591
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1591.cold.1
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1602
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1602.cold.1
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1603
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1603.cold.1
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1603.cold.2
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1616
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1616.cold.1
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1618
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1622
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1622.cold.1
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1647
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1648
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1648.cold.1
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1584
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1598
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1617
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1641
- __64-[PLProcessNetworkAgent logEventPointConnectionEvent:forSource:]_block_invoke.241
- __65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.240
- __65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.240.cold.1
- __75-[PLProcessNetworkAgent timestampNetConnectEntry:withEventType:withSource:]_block_invoke.258
- __75-[PLProcessNetworkAgent timestampNetConnectEntry:withEventType:withSource:]_block_invoke.266
- __76-[PLPowerMetricMonitorService _collectMetricsWithTimeout:completionHandler:]_block_invoke.299
- __76-[PLPowerMetricMonitorService _collectMetricsWithTimeout:completionHandler:]_block_invoke.301
- __76-[PLPowerMetricMonitorService _collectMetricsWithTimeout:completionHandler:]_block_invoke.301.cold.1
- __83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.230
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.467
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.554
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.561
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.601
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_2.614
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_3.621
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_4.628
- __PowerChangedCallback_block_invoke.500
- __PowerChangedCallback_block_invoke.506
- __PowerChangedCallback_block_invoke.510
- __PowerChangedCallback_block_invoke.510.cold.1
- __PowerChangedCallback_block_invoke.516
- __PowerChangedCallback_block_invoke.522
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN12PLProcessCPU12inode_data_tEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEE5resetB8ne180100EPS7_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKyN12PLProcessCPU12inode_data_tEEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___106-[PLApplicationAgent logEventForwardApplicationForDisplayID:withPid:withState:withVisibility:withReasons:]_block_invoke
- ___23-[PLLocationAgent init]_block_invoke_2
- ___31-[PLSleepWakeAgent wakeReasons]_block_invoke
- ___36-[PLSleepWakeAgent logSleepEntries:]_block_invoke
- ___37-[PLSleepWakeAgent driverWakeReasons]_block_invoke
- ___38-[PLLocationAgent resyncActiveClients]_block_invoke
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke_2
- ___40-[PLSleepWakeAgent capabilitiesChanged:]_block_invoke
- ___41-[PLSleepWakeAgent wakeReasonsAsNSString]_block_invoke
- ___42+[PLUtilities shouldLogPreUnlockTelemetry]_block_invoke
- ___42-[PLPushAgent checkPushUsage:withPLEntry:]_block_invoke
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2
- ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke_2
- ___44-[PLSleepWakeAgent logEventPointKernelState]_block_invoke
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke_2
- ___46-[PLSleepWakeAgent logEventNonePowerNapConfig]_block_invoke
- ___47-[PLProcessNetworkAgent compressNetworkBitmap:]_block_invoke
- ___49-[PLSleepWakeAgent registerForCapabilitiesChange]_block_invoke
- ___51-[PLSleepWakeAgent logWakeEntries:withCurrentTime:]_block_invoke
- ___51-[PLSleepWakeAgent registerForUserIdleNotification]_block_invoke_2
- ___53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke_2
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke
- ___60-[PLLocationAgent logEventNoneClientStatusDebugWithClients:]_block_invoke_2
- ___64-[PLProcessNetworkAgent logEventPointConnectionEvent:forSource:]_block_invoke
- ___73-[PLLocationAgent closeOpenEntryForClient:withOpenEntry:withTimeStopped:]_block_invoke_2
- ___75-[PLProcessNetworkAgent timestampNetConnectEntry:withEventType:withSource:]_block_invoke
- ___78-[PLLocationAgent updateLocalCacheWithClient:withType:withBundleID:withEntry:]_block_invoke
- ___80-[PLProcessNetworkAgent aggregateAndLogNetworkBitmaps:withStartTime:andEndTime:]_block_invoke
- __block_literal_global.1039
- __block_literal_global.1131
- __block_literal_global.1134
- __block_literal_global.1136
- __block_literal_global.1138
- __block_literal_global.1142
- __block_literal_global.1144
- __block_literal_global.1146
- __block_literal_global.1148
- __block_literal_global.1159
- __block_literal_global.1173
- __block_literal_global.1196
- __block_literal_global.1509
- __block_literal_global.1677
- __block_literal_global.1679
- __block_literal_global.1681
- __block_literal_global.1683
- __block_literal_global.1685
- __block_literal_global.1687
- __block_literal_global.1689
- __block_literal_global.1691
- __block_literal_global.1696
- __block_literal_global.1766
- __block_literal_global.1768
- __block_literal_global.1784
- __block_literal_global.181
- __block_literal_global.184
- __block_literal_global.218
- __block_literal_global.2297
- __block_literal_global.234
- __block_literal_global.247
- __block_literal_global.255
- __block_literal_global.260
- __block_literal_global.268
- __block_literal_global.270
- __block_literal_global.414
- __block_literal_global.418
- __block_literal_global.421
- __block_literal_global.424
- __block_literal_global.427
- __block_literal_global.432
- __block_literal_global.460
- __block_literal_global.482
- __block_literal_global.486
- __block_literal_global.594
- __block_literal_global.596
- __block_literal_global.607
- __block_literal_global.609
- __block_literal_global.614
- __block_literal_global.619
- __block_literal_global.622
- __block_literal_global.626
- __block_literal_global.629
- __block_literal_global.632
- __block_literal_global.635
- __block_literal_global.728
- __block_literal_global.730
- __block_literal_global.747
- __block_literal_global.826
- __fakeSleep_block_invoke.455
- __fakeSleep_block_invoke.467
- __fakeSleep_block_invoke.471
- __fakeSleep_block_invoke.471.cold.1
- __fakeSleep_block_invoke.479
- _fmod
- _objc_msgSend$_parseDCPSwapStats:
- _objc_msgSend$getJetamPriority:
- _objc_msgSend$logBatteryEntry:
- _objc_msgSend$logDisplayEntry:
- aggregateAndLogNetworkBitmaps:withStartTime:andEndTime:.classDebugEnabled
- aggregateAndLogNetworkBitmaps:withStartTime:andEndTime:.defaultOnce
- capabilitiesChanged:.classDebugEnabled
- capabilitiesChanged:.classDebugEnabled.167
- capabilitiesChanged:.classDebugEnabled.173
- capabilitiesChanged:.defaultOnce
- capabilitiesChanged:.defaultOnce.166
- capabilitiesChanged:.defaultOnce.172
- checkPushUsage:withPLEntry:.classDebugEnabled
- checkPushUsage:withPLEntry:.defaultOnce
- compressNetworkBitmap:.classDebugEnabled
- compressNetworkBitmap:.defaultOnce
- driverWakeReasons.classDebugEnabled
- driverWakeReasons.defaultOnce
- fakeSleep.classDebugEnabled.454
- fakeSleep.classDebugEnabled.466
- fakeSleep.classDebugEnabled.478
- fakeSleep.defaultOnce.453
- fakeSleep.defaultOnce.465
- fakeSleep.defaultOnce.477
- handleBrightnessClientNotification:withValue:.classDebugEnabled.1646
- handleBrightnessClientNotification:withValue:.defaultOnce.1645
- init.classDebugEnabled.1177
- init.classDebugEnabled.1196
- init.defaultOnce.1176
- init.defaultOnce.1195
- initOperatorDependancies.classDebugEnabled.1355
- initOperatorDependancies.defaultOnce.1354
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.classDebugEnabled.470
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.classDebugEnabled.474
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.classDebugEnabled.480
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.classDebugEnabled.486
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.classDebugEnabled.492
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.classDebugEnabled.498
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.defaultOnce.469
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.defaultOnce.473
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.defaultOnce.479
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.defaultOnce.485
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.defaultOnce.491
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_10.defaultOnce.497
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_2.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_2.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_3.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_3.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_4.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_4.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_5.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_5.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_6.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_6.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_7.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_7.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_8.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_8.classDebugEnabled.374
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_8.defaultOnce
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_8.defaultOnce.373
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.classDebugEnabled
- kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.defaultOnce
- kPLPushAgentInterruptionSuppression_block_invoke.classDebugEnabled
- kPLPushAgentInterruptionSuppression_block_invoke.defaultOnce
- kPLPushAgentInterruptionSuppression_block_invoke_2.classDebugEnabled
- kPLPushAgentInterruptionSuppression_block_invoke_2.defaultOnce
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_2.classDebugEnabled.295
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_2.classDebugEnabled.305
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_2.classDebugEnabled.326
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_2.defaultOnce.294
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_2.defaultOnce.304
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_2.defaultOnce.325
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_3.classDebugEnabled
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_3.defaultOnce
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_4.classDebugEnabled
- kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_4.defaultOnce
- kPRearNits_block_invoke_2.classDebugEnabled.1232
- kPRearNits_block_invoke_2.defaultOnce.1231
- kPRearNits_block_invoke_3.classDebugEnabled.1261
- kPRearNits_block_invoke_3.defaultOnce.1260
- kPRearNits_block_invoke_4.classDebugEnabled.1305
- kPRearNits_block_invoke_4.classDebugEnabled.1317
- kPRearNits_block_invoke_4.defaultOnce.1304
- kPRearNits_block_invoke_4.defaultOnce.1316
- kPRearNits_block_invoke_7.classDebugEnabled.1366
- kPRearNits_block_invoke_7.defaultOnce.1365
- kPRearNits_block_invoke_8.classDebugEnabled.1570
- kPRearNits_block_invoke_8.classDebugEnabled.1577
- kPRearNits_block_invoke_8.defaultOnce.1569
- kPRearNits_block_invoke_8.defaultOnce.1576
- logCoalitionObjectDifference:.classDebugEnabled.722
- logCoalitionObjectDifference:.defaultOnce.721
- logEventForwardALSLux:.classDebugEnabled.1453
- logEventForwardALSLux:.defaultOnce.1452
- logEventForwardApplicationForDisplayID:withPid:withState:withVisibility:withReasons:.classDebugEnabled
- logEventForwardApplicationForDisplayID:withPid:withState:withVisibility:withReasons:.defaultOnce
- logEventForwardClientStatus_withLimiter.classDebugEnabled
- logEventForwardClientStatus_withLimiter.defaultOnce
- logEventForwardClientStatuswithPayload:.classDebugEnabled
- logEventForwardClientStatuswithPayload:.classDebugEnabled.442
- logEventForwardClientStatuswithPayload:.classDebugEnabled.448
- logEventForwardClientStatuswithPayload:.classDebugEnabled.454
- logEventForwardClientStatuswithPayload:.defaultOnce
- logEventForwardClientStatuswithPayload:.defaultOnce.441
- logEventForwardClientStatuswithPayload:.defaultOnce.447
- logEventForwardClientStatuswithPayload:.defaultOnce.453
- logEventForwardTechStatus.classDebugEnabled
- logEventForwardTechStatus.classDebugEnabled.411
- logEventForwardTechStatus.classDebugEnabled.417
- logEventForwardTechStatus.defaultOnce
- logEventForwardTechStatus.defaultOnce.410
- logEventForwardTechStatus.defaultOnce.416
- logEventForwardTechStatus_withLimiter.classDebugEnabled
- logEventForwardTechStatus_withLimiter.defaultOnce
- logEventNonePowerNapConfig.classDebugEnabled
- logEventNonePowerNapConfig.classDebugEnabled.283
- logEventNonePowerNapConfig.defaultOnce
- logEventNonePowerNapConfig.defaultOnce.282
- logEventPointClientStatus.classDebugEnabled
- logEventPointClientStatus.classDebugEnabled.382
- logEventPointClientStatus.classDebugEnabled.388
- logEventPointClientStatus.classDebugEnabled.394
- logEventPointClientStatus.defaultOnce
- logEventPointClientStatus.defaultOnce.381
- logEventPointClientStatus.defaultOnce.387
- logEventPointClientStatus.defaultOnce.393
- logEventPointConnectionEvent:forSource:.classDebugEnabled
- logEventPointConnectionEvent:forSource:.classDebugEnabled.240
- logEventPointConnectionEvent:forSource:.defaultOnce
- logEventPointConnectionEvent:forSource:.defaultOnce.239
- logEventPointCurrentScheduledWake.classDebugEnabled
- logEventPointCurrentScheduledWake.defaultOnce
- logEventPointKernelState.classDebugEnabled
- logEventPointKernelState.classDebugEnabled.154
- logEventPointKernelState.defaultOnce
- logEventPointKernelState.defaultOnce.153
- logSleepEntries:.classDebugEnabled
- logSleepEntries:.classDebugEnabled.183
- logSleepEntries:.classDebugEnabled.192
- logSleepEntries:.defaultOnce
- logSleepEntries:.defaultOnce.182
- logSleepEntries:.defaultOnce.191
- logWakeEntries:withCurrentTime:.classDebugEnabled
- logWakeEntries:withCurrentTime:.classDebugEnabled.196
- logWakeEntries:withCurrentTime:.defaultOnce
- logWakeEntries:withCurrentTime:.defaultOnce.195
- readKeyViaOSAccum:toOutput:.classDebugEnabled.1116
- readKeyViaOSAccum:toOutput:.defaultOnce.1115
- registerForCapabilitiesChange.classDebugEnabled
- registerForCapabilitiesChange.classDebugEnabled.213
- registerForCapabilitiesChange.defaultOnce
- registerForCapabilitiesChange.defaultOnce.212
- registerForUserIdleNotification.classDebugEnabled
- registerForUserIdleNotification.defaultOnce
- resyncActiveClients.classDebugEnabled
- resyncActiveClients.classDebugEnabled.432
- resyncActiveClients.defaultOnce
- resyncActiveClients.defaultOnce.431
- shouldLogPreUnlockTelemetry.__shouldLogPreUnlockTelemetry
- shouldLogPreUnlockTelemetry.onceToken
- timestampNetConnectEntry:withEventType:withSource:.classDebugEnabled
- timestampNetConnectEntry:withEventType:withSource:.classDebugEnabled.257
- timestampNetConnectEntry:withEventType:withSource:.classDebugEnabled.265
- timestampNetConnectEntry:withEventType:withSource:.defaultOnce
- timestampNetConnectEntry:withEventType:withSource:.defaultOnce.256
- timestampNetConnectEntry:withEventType:withSource:.defaultOnce.264
- updateClientsLocationInfo:.classDebugEnabled
- updateClientsLocationInfo:.classDebugEnabled.505
- updateClientsLocationInfo:.defaultOnce
- updateClientsLocationInfo:.defaultOnce.504
- updateLocalCacheWithClient:withType:withBundleID:withEntry:.classDebugEnabled
- updateLocalCacheWithClient:withType:withBundleID:withEntry:.defaultOnce
- wakeReasons.classDebugEnabled
- wakeReasons.defaultOnce
- wakeReasonsAsNSString.classDebugEnabled
- wakeReasonsAsNSString.defaultOnce
CStrings:
+ "!/\t"
+ "%@ payload is empty"
+ "%@ sysctl value: %u"
+ "%llu inst, %llu r, %llu w, %llu gpuTime, %llu cpuTime, %llu ane, %llu aneTick, %llu cpuEnergy"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLUtilities.m"
+ "BTCompanionIn"
+ "BTCompanionOut"
+ "BrightnessTransaction"
+ "ColdBoot"
+ "ConversationType"
+ "EnableLegacySMC"
+ "Error with MEMORYSTATUS_CMD_GET_PRIORITY_LIST. Size %i and sizeof(entry) %lu"
+ "Failed to subscribe to IOReport DCP scanout"
+ "HDRHeadroom"
+ "IncomingProxyMessages"
+ "Log cold boot key with value in volts %@"
+ "LogLevel changed with payload=%@"
+ "Message TranscriptForeground monotonic eventTime: %@"
+ "Message TranscriptForeground payload: %@"
+ "Message::TranscriptForeground"
+ "MessageForegroundXPCListener"
+ "MessageGUID"
+ "MessageType"
+ "Other Message Protocol logged: %@"
+ "OutgoingProxyMessages"
+ "PC APSD Incoming Proxy Messages"
+ "PC APSD Outgoing Proxy Messages"
+ "PLPushAgent:: PC APSD Connected with payload=%@"
+ "PLPushAgent:: PC APSD DidSendKeepAlive with payload=%@"
+ "PLPushAgent:: PC APSD Incoming Proxy Messages with payload=%@"
+ "PLPushAgent:: PC APSD Message Received with payload=%@"
+ "PLPushAgent:: PC APSD Message Sent with payload=%@"
+ "PLPushAgent:: PC APSD Outgoing Proxy Messages with payload=%@"
+ "ProcessNetwork"
+ "Protocol"
+ "ProxyCommand"
+ "PushType"
+ "RCS"
+ "Received messages update, isSentEvent: %@, payload: %@"
+ "ResetData: %@"
+ "SMS"
+ "SatelliteSMS"
+ "SleepWake"
+ "StatusBarOverride changed with payload=%@"
+ "T@\"NSMutableDictionary\",&,V_summarizedNotificationEntries"
+ "T@\"NSNumber\",&,V_HDRHeadroom"
+ "T@\"PLIOReportStats\",&,N,V_dcpScanoutStats"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_MessageForegroundXPCListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_messageReceivedListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_messageSentListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_pushProxyIncomingListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_pushProxyOutgoingListener"
+ "TQ,V_cpuEnergy"
+ "TQ,V_timeAtPriorityMATU"
+ "TVMD"
+ "TVSL"
+ "TVSR"
+ "TVmS"
+ "Target"
+ "Tp002a"
+ "TranscriptForeground"
+ "TranscriptVisibilityState"
+ "Unable to get %@ sysctl value, defaulting to -1: %{errno}d"
+ "VRTC"
+ "_HDRHeadroom"
+ "_MessageForegroundXPCListener"
+ "_cancelBrightnessTimer"
+ "_cpuEnergy"
+ "_dcpScanoutStats"
+ "_messageReceivedListener"
+ "_messageSentListener"
+ "_parseAverageFPS:"
+ "_parseDisplayAZLMetricsFromEntry:cacheMetrics:"
+ "_pushProxyIncomingListener"
+ "_pushProxyOutgoingListener"
+ "_startBrightnessTimer"
+ "_summarizedNotificationEntries"
+ "_timeAtPriorityMATU"
+ "_updateDisplayMetrics"
+ "addBrightnessSample"
+ "app_time_at_jetsam_priority"
+ "assistantd"
+ "bb23C"
+ "cePn"
+ "clientStatus XPC with payload=%@"
+ "cmDU"
+ "configd"
+ "convertMessageProtocol:"
+ "cpuEnergy"
+ "daemon_time_at_jetsam_priority"
+ "dcpScanoutStats"
+ "dcpSubFrameMap"
+ "dictionaryWithCapacity:"
+ "displayAZL"
+ "entryEventNoneDefinitionColdBoot"
+ "entryEventPointDefinitionIncomingPushProxyMessages"
+ "entryEventPointDefinitionOutgoingPushProxyMessages"
+ "failed to allocate buffer"
+ "getJetsamPriority:"
+ "grabSysctlValue:"
+ "handleMessageEvent:isSentEvent:"
+ "iMessageLite"
+ "iMessageReceived"
+ "iMessageReceived payload: %@"
+ "iMessageSent"
+ "iMessageSent payload: %@"
+ "logColdBoot"
+ "logEventEventForwardMessageTranscript:"
+ "logPushProxyMessages:forMessageType:"
+ "logSleepBedtime:"
+ "logSleepWaketime:"
+ "logd"
+ "maNN"
+ "messageReceivedListener"
+ "messageSentListener"
+ "mxT1"
+ "notifyd"
+ "pushProxyIncomingListener"
+ "pushProxyOutgoingListener"
+ "scanout"
+ "setDcpScanoutStats:"
+ "setDisplayAZL:"
+ "setDisplayFPS:"
+ "setHDRHeadroom:"
+ "setMessageForegroundXPCListener:"
+ "setMessageReceivedListener:"
+ "setMessageSentListener:"
+ "setPushProxyIncomingListener:"
+ "setPushProxyOutgoingListener:"
+ "setScanoutFPS:"
+ "setSummarizedNotificationEntries:"
+ "setTimeAtPriorityMATU:"
+ "subframes(%d)"
+ "summarizedNotificationEntries"
+ "timeAtPriorityMATU"
+ "updateBrightnessMetrics"
+ "{jetsam_priority_info=iBq}20@0:8i16"
- "%llu inst, %llu r, %llu w, %llu gpuTime, %llu cpuTime, %llu ane, %llu aneTick"
- "-[PLApplicationAgent logEventForwardApplicationForDisplayID:withPid:withState:withVisibility:withReasons:]"
- "-[PLLocationAgent initOperatorDependancies]_block_invoke"
- "-[PLLocationAgent init]_block_invoke"
- "-[PLLocationAgent logEventForwardClientStatus_withLimiter]"
- "-[PLLocationAgent logEventForwardClientStatuswithPayload:]"
- "-[PLLocationAgent logEventForwardTechStatus]"
- "-[PLLocationAgent logEventForwardTechStatus_withLimiter]"
- "-[PLLocationAgent logEventNoneClientStatusDebugWithClients:]_block_invoke"
- "-[PLLocationAgent logEventPointClientStatus]_block_invoke"
- "-[PLLocationAgent logEventPointClientStatus]_block_invoke_2"
- "-[PLLocationAgent resyncActiveClients]"
- "-[PLLocationAgent updateClientsLocationInfo:]"
- "-[PLLocationAgent updateClientsLocationInfo:]_block_invoke"
- "-[PLLocationAgent updateClientsLocationInfo:]_block_invoke_2"
- "-[PLLocationAgent updateLocalCacheWithClient:withType:withBundleID:withEntry:]"
- "-[PLProcessNetworkAgent aggregateAndLogNetworkBitmaps:withStartTime:andEndTime:]"
- "-[PLProcessNetworkAgent compressNetworkBitmap:]"
- "-[PLProcessNetworkAgent logEventPointConnectionEvent:forSource:]"
- "-[PLProcessNetworkAgent timestampNetConnectEntry:withEventType:withSource:]"
- "-[PLPushAgent checkPushUsage:withPLEntry:]"
- "-[PLPushAgent initOperatorDependancies]_block_invoke"
- "-[PLSleepWakeAgent capabilitiesChanged:]"
- "-[PLSleepWakeAgent driverWakeReasons]"
- "-[PLSleepWakeAgent logEventNonePowerNapConfig]"
- "-[PLSleepWakeAgent logEventPointCurrentScheduledWake]"
- "-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke"
- "-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke_2"
- "-[PLSleepWakeAgent logEventPointKernelState]"
- "-[PLSleepWakeAgent logSleepEntries:]"
- "-[PLSleepWakeAgent logWakeEntries:withCurrentTime:]"
- "-[PLSleepWakeAgent registerForCapabilitiesChange]"
- "-[PLSleepWakeAgent registerForUserIdleNotification]"
- "-[PLSleepWakeAgent registerForUserIdleNotification]_block_invoke"
- "-[PLSleepWakeAgent wakeReasonsAsNSString]"
- "-[PLSleepWakeAgent wakeReasons]"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLProcessNetworkAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLLocationAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLApplicationAgentMac.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPushAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLUtilities.m"
- "PLPushAgent:: apsdConnectedListener with payload=%@"
- "PLPushAgent:: receivedPushListener with payload=%@"
- "PLPushAgent:: sentKeepAliveListener with payload=%@"
- "PLPushAgent:: sentPushListener with payload=%@"
- "_parseDCPSwapStats:"
- "client status XPC with payload=%@"
- "getJetamPriority:"
- "log level changed with payload=%@"
- "network"
- "status bar changed with payload=%@"
- "{jetsam_priority_info=iB}20@0:8i16"

```
