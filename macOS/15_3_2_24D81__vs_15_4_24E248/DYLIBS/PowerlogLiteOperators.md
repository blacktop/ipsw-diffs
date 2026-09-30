## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/Versions/A/PowerlogLiteOperators`

```diff

-2308.80.23.0.0
-  __TEXT.__text: 0x202ac4
-  __TEXT.__auth_stubs: 0x23e0
-  __TEXT.__objc_methlist: 0xbca8
-  __TEXT.__const: 0xd60
+2423.100.232.0.0
+  __TEXT.__text: 0x1fe6d8
+  __TEXT.__auth_stubs: 0x23f0
+  __TEXT.__objc_methlist: 0xc1dc
+  __TEXT.__const: 0xe10
   __TEXT.__swift5_typeref: 0x33c
   __TEXT.__constg_swiftt: 0x1ac
   __TEXT.__swift5_reflstr: 0x179
   __TEXT.__swift5_fieldmd: 0x200
-  __TEXT.__cstring: 0x58a38
+  __TEXT.__cstring: 0x5874b
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x20
-  __TEXT.__oslogstring: 0x87fe
+  __TEXT.__oslogstring: 0x9cf6
   __TEXT.__swift5_capture: 0x80
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x1fd8
+  __TEXT.__gcc_except_tab: 0x1f94
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x2e98
-  __TEXT.__eh_frame: 0x608
+  __TEXT.__unwind_info: 0x2d38
+  __TEXT.__eh_frame: 0x5e8
   __TEXT.__objc_classname: 0x690
-  __TEXT.__objc_methname: 0x27a99
-  __TEXT.__objc_methtype: 0x18ae
-  __TEXT.__objc_stubs: 0x174a0
-  __DATA_CONST.__got: 0xb68
-  __DATA_CONST.__const: 0x3748
+  __TEXT.__objc_methname: 0x284d3
+  __TEXT.__objc_methtype: 0x18b2
+  __TEXT.__objc_stubs: 0x17a40
+  __DATA_CONST.__got: 0xb78
+  __DATA_CONST.__const: 0x3798
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_nlclslist: 0x180
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b70
+  __DATA_CONST.__objc_selrefs: 0x7e90
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x340
-  __DATA_CONST.__objc_arraydata: 0x5b50
-  __AUTH_CONST.__auth_got: 0x1208
-  __AUTH_CONST.__const: 0x2e18
-  __AUTH_CONST.__cfstring: 0x48bc0
-  __AUTH_CONST.__objc_const: 0xd858
+  __DATA_CONST.__objc_arraydata: 0x5c78
+  __AUTH_CONST.__auth_got: 0x1210
+  __AUTH_CONST.__const: 0x2fb8
+  __AUTH_CONST.__cfstring: 0x48560
+  __AUTH_CONST.__objc_const: 0xd730
   __AUTH_CONST.__objc_intobj: 0x4bd8
-  __AUTH_CONST.__objc_dictobj: 0x2350
-  __AUTH_CONST.__objc_arrayobj: 0xea0
+  __AUTH_CONST.__objc_dictobj: 0x2490
+  __AUTH_CONST.__objc_arrayobj: 0xed0
   __AUTH_CONST.__objc_doubleobj: 0xbb0
   __AUTH.__objc_data: 0xba0
   __AUTH.__data: 0xae8
-  __DATA.__objc_ivar: 0xd68
+  __DATA.__objc_ivar: 0xdb0
   __DATA.__data: 0x518
-  __DATA.__bss: 0x2760
   __DATA.__common: 0x180
+  __DATA.__bss: 0x2488
   __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 96FA1064-7A62-3B9A-98F1-88BD642D0BD6
-  Functions: 5732
-  Symbols:   12206
-  CStrings:  29050
+  UUID: CF17B517-EF75-31E8-B065-5066A961CD33
+  Functions: 5693
+  Symbols:   12261
+  CStrings:  29253
 
Symbols:
+ +[PLBluetoothAgent entryEventBackwardWakeupVSE]
+ +[PLDisplayAgent dcpSubFrameMap]
+ +[PLPerformanceAgent entryEventPointDefinitionIdleReaper]
+ +[PLPushAgent entryEventPointDefinitionIncomingPushProxyMessages]
+ +[PLPushAgent entryEventPointDefinitionOutgoingPushProxyMessages]
+ +[PLSMCAgent entryEventNoneDefinitionColdBoot]
+ -[PLBluetoothAgent btHCIVSEListener]
+ -[PLBluetoothAgent setBtHCIVSEListener:]
+ -[PLConfigAgent bootArgs]
+ -[PLDisplayAgent HDRHeadroom]
+ -[PLDisplayAgent setHDRHeadroom:]
+ -[PLIOReportMetricsAgent buildCustomSet:]
+ -[PLIOReportMetricsAgent channelDictionaryWithChannelSet:]
+ -[PLIOReportMetricsAgent isDynamicTable:]
+ -[PLIOReportMetricsAgent sampleChannelsCustom]
+ -[PLIOReportMetricsAgent setSampleChannelsCustom:]
+ -[PLPerformanceAgent logEventPointIdleReaper]
+ -[PLPowerAssertionAgent displayOn]
+ -[PLPowerAssertionAgent handleStateChange]
+ -[PLPowerAssertionAgent optimizesSubSecondAssertions]
+ -[PLPowerAssertionAgent pluggedIn]
+ -[PLPowerAssertionAgent setDisplayOn:]
+ -[PLPowerAssertionAgent setOptimizesSubSecondAssertions:]
+ -[PLPowerAssertionAgent setPluggedIn:]
+ -[PLPowerAssertionAgent setStateTracker:]
+ -[PLPowerAssertionAgent stateTracker]
+ -[PLPowerAssertionAgent updateDisplayState]
+ -[PLPowerAssertionAgent updateOptimizeSubSecondAssertions]
+ -[PLPowerAssertionAgent updatePluggedInState]
+ -[PLPushAgent convertMessageProtocol:]
+ -[PLPushAgent handleMessageEvent:isSentEvent:]
+ -[PLPushAgent logPushProxyMessages:forMessageType:]
+ -[PLPushAgent messageReceivedListener]
+ -[PLPushAgent messageSentListener]
+ -[PLPushAgent pushProxyIncomingListener]
+ -[PLPushAgent pushProxyOutgoingListener]
+ -[PLPushAgent setMessageReceivedListener:]
+ -[PLPushAgent setMessageSentListener:]
+ -[PLPushAgent setPushProxyIncomingListener:]
+ -[PLPushAgent setPushProxyOutgoingListener:]
+ -[PLSMCAgent logColdBoot]
+ -[PLSMCMetricsAgent getPowerDeliveryCLVRKeys]
+ -[PLSMCMetricsAgent logPowerDeliveryCLVRKeys]
+ -[PLSMCMetricsAgent logSMCLookUpTable]
+ -[PLSMCMetricsAgent loggedKeysArray]
+ -[PLSMCMetricsAgent loggedPowerDeliveryCLVRKeysArray]
+ -[PLSMCMetricsAgent powerDeliveryCallback]
+ -[PLSMCMetricsAgent powerDeliveryCounter]
+ -[PLSMCMetricsAgent setLoggedKeysArray:]
+ -[PLSMCMetricsAgent setLoggedPowerDeliveryCLVRKeysArray:]
+ -[PLSMCMetricsAgent setPowerDeliveryCounter:]
+ -[PLSMCMetricsAgent writeSMCKey:withValue:]
+ -[PLThermalMonitorService setThermalNotification:]
+ -[PLThermalMonitorService thermalNotification]
+ -[PLVideoAgent cMVideoQueueListener]
+ -[PLVideoAgent logEventBackwardCMVideoQueueWithEntry:]
+ -[PLVideoAgent setCMVideoQueueListener:]
+ -[PLXPCAgent MessageForegroundXPCListener]
+ -[PLXPCAgent logEventEventForwardMessageTranscript:]
+ -[PLXPCAgent logSleepBedtime:]
+ -[PLXPCAgent logSleepWaketime:]
+ -[PLXPCAgent setMessageForegroundXPCListener:]
+ -[PLXPCAgent setSummarizedNotificationEntries:]
+ -[PLXPCAgent summarizedNotificationEntries]
+ -[ProcessMemoryUsage setTimeAtPriorityMATU:]
+ -[ProcessMemoryUsage timeAtPriorityMATU]
+ GCC_except_table189
+ GCC_except_table20
+ GCC_except_table253
+ GCC_except_table259
+ GCC_except_table264
+ GCC_except_table31
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table53
+ OBJC_IVAR_$_PLButtonAgent._batteryLevelChanged
+ OBJC_IVAR_$_ProcessMemoryUsage._timeAtPriorityMATU
+ _PLLogBluetooth
+ _PLLogButton
+ _PLLogConfig
+ _PLLogFSEvent
+ _PLLogLocation
+ _PLLogPerformance
+ _PLLogPeripheral
+ _PLLogSleepWake
+ _PLLogVideo
+ _PLLogWindowServer
+ _SMCWriteKey
+ __22-[PLDisplayAgent init]_block_invoke.1181
+ __22-[PLDisplayAgent init]_block_invoke.1190
+ __22-[PLDisplayAgent init]_block_invoke.1200
+ __22-[PLDisplayAgent init]_block_invoke.1204
+ __22-[PLDisplayAgent init]_block_invoke.1210
+ __22-[PLDisplayAgent init]_block_invoke.1214
+ __22-[PLDisplayAgent init]_block_invoke.1218
+ __22-[PLDisplayAgent init]_block_invoke.1236
+ __22-[PLDisplayAgent init]_block_invoke.1246
+ __22-[PLDisplayAgent init]_block_invoke.1258
+ __22-[PLDisplayAgent init]_block_invoke.1265
+ __22-[PLDisplayAgent init]_block_invoke_2.1230
+ __22-[PLDisplayAgent init]_block_invoke_2.1248
+ __22-[PLDisplayAgent init]_block_invoke_2.1259
+ __23-[PLLocationAgent init]_block_invoke.258
+ __30-[PLCoalitionAgent logToAggd:]_block_invoke.718
+ __30-[PLConfigAgent logEntryToCA:]_block_invoke.368
+ __30-[PLConfigAgent logEntryToCA:]_block_invoke.376
+ __30-[PLConfigAgent logEntryToCA:]_block_invoke.388
+ __33+[PLPushAgent bundleIdFromTopic:]_block_invoke.330
+ __33-[PLNetworkAgent initKernelEvent]_block_invoke.76
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.781
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.787
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.823
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.839
+ __33-[PLWifiAgent logEventPointWake:]_block_invoke.851
+ __34+[PLSMCAgent reportPMUEventsToCA:]_block_invoke.1236
+ __36-[PLPerformanceAgent countMachPort:]_block_invoke.329
+ __37-[PLIOReportAgent logEngagementToCA:]_block_invoke.11442
+ __37-[PLIOReportAgent logEngagementToCA:]_block_invoke.11457
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.532
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.538
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.545
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.554
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.566
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.572
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.578
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.587
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.593
+ __37-[PLPowerAssertionAgent logInterval:]_block_invoke.599
+ __37-[PLPowerAssertionAgent logSnapshot:]_block_invoke.501
+ __37-[PLPowerAssertionAgent logSnapshot:]_block_invoke.510
+ __37-[PLXPCAgent logEventForwardGMSOptIn]_block_invoke.2410
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1033
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1042
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1043
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1050
+ __38-[PLSMCAgent initOperatorDependancies]_block_invoke_2.1051
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1643
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1651
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1659
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1667
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1675
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1683
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1691
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1699
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1707
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1718
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1729
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1740
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1751
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1762
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1773
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1780
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1788
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1793
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1800
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1807
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1815
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1822
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1827
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1837
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1845
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1853
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1858
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1866
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1874
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1884
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1894
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1901
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1911
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1918
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1928
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1938
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1948
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1968
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1978
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1986
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1994
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2004
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2014
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2022
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2032
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2042
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2052
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2062
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2070
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2078
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2083
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2088
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2093
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2098
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2105
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2110
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2115
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2120
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2127
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2134
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2144
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2152
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2160
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2168
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2176
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2181
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2191
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2198
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2208
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2218
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2228
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2238
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2245
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2253
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2261
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2268
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2273
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2280
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2285
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2293
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2298
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2306
+ __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2319
+ __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.101
+ __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.106
+ __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.111
+ __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.121
+ __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.91
+ __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.96
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.190
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.199
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.207
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.215
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.223
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.231
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.233
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.244
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.255
+ __39-[PLPushAgent initOperatorDependancies]_block_invoke.263
+ __40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1457
+ __40-[PLVideoAgent initOperatorDependancies]_block_invoke.147
+ __40-[PLVideoAgent initOperatorDependancies]_block_invoke.155
+ __40-[PLVideoAgent initOperatorDependancies]_block_invoke.163
+ __40-[PLVideoAgent initOperatorDependancies]_block_invoke.171
+ __40-[PLVideoAgent initOperatorDependancies]_block_invoke.179
+ __40-[PLVideoAgent initOperatorDependancies]_block_invoke.187
+ __40-[PLVideoAgent initOperatorDependancies]_block_invoke.197
+ __40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1005
+ __41-[PLConfigAgent initOperatorDependancies]_block_invoke.266
+ __41-[PLConfigAgent initOperatorDependancies]_block_invoke.270
+ __41-[PLIOReportAgent samplePSRChannelsDelta]_block_invoke.11032
+ __41-[PLProcessNetworkAgent didAddNewSource:]_block_invoke.216
+ __41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.1129
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1280
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1281
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1293
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1298
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1299
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1309
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1321
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1332
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1338
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1348
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1359
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1363
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1370
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1300
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1333
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1349
+ __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1364
+ __42-[PLFSEventAgent logLogFileName:withName:]_block_invoke.70
+ __42-[PLNetworkAgent initOperatorDependancies]_block_invoke.110
+ __42-[PLNetworkAgent initOperatorDependancies]_block_invoke.124
+ __42-[PLNetworkAgent initOperatorDependancies]_block_invoke.96
+ __42-[PLWindowServerAgent establishConnection]_block_invoke.92
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1547
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1559
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1574
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1584
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1596
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1608
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1625
+ __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1632
+ __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10597
+ __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10598
+ __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10606
+ __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10618
+ __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10620
+ __43-[PLIOReportAgent initOperatorDependancies]_block_invoke_2.10607
+ __43-[PLIOReportAgent initOperatorDependancies]_block_invoke_2.10621
+ __43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.11396
+ __43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.11402
+ __43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.11409
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.293
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.307
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.315
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.320
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.325
+ __43-[PLLocationAgent initOperatorDependancies]_block_invoke.333
+ __43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.1111
+ __44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.308
+ __44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.323
+ __44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.327
+ __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.435
+ __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.442
+ __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.443
+ __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.453
+ __45-[PLMDNSAgent logEventBackwardClientSummary:]_block_invoke.125
+ __45-[PLPeripheralAgent initOperatorDependancies]_block_invoke.93
+ __45-[PLPeripheralAgent initOperatorDependancies]_block_invoke.94
+ __45-[PLSMCMetricsAgent initOperatorDependancies]_block_invoke.23
+ __46-[PLBluetoothAgent receivedBTStatusUpdateOSX:]_block_invoke.414
+ __46-[PLBluetoothAgent receivedBTStatusUpdateOSX:]_block_invoke.423
+ __46-[PLPerformanceAgent initOperatorDependancies]_block_invoke.212
+ __46-[PLPerformanceAgent initOperatorDependancies]_block_invoke.215
+ __46-[PLPerformanceAgent initOperatorDependancies]_block_invoke.229
+ __46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.247
+ __48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.349
+ __48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.352
+ __48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.308
+ __48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.314
+ __48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.320
+ __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.102
+ __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.105
+ __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.109
+ __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.113
+ __49-[PLCoalitionAgent logCoalitionObjectDifference:]_block_invoke.756
+ __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.154
+ __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.167
+ __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.178
+ __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.187
+ __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.207
+ __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.213
+ __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke_2.179
+ __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke_2.188
+ __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke_2.196
+ __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.188
+ __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.196
+ __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.201
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1026
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1032
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1038
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1044
+ __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1050
+ __50-[PLDisplayAgent logEventForwardLinearBrightness:]_block_invoke.1554
+ __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.157
+ __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.165
+ __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.173
+ __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.183
+ __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.191
+ __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.199
+ __51-[PLThermalMonitorService initOperatorDependancies]_block_invoke.30
+ __51-[PLThermalMonitorService initOperatorDependancies]_block_invoke.43
+ __51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.765
+ __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.381
+ __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.387
+ __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.391
+ __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.401
+ __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke_2.392
+ __54-[PLIOReportAgent processNotificationForChannelGroup:]_block_invoke.10570
+ __55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.957
+ __55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.966
+ __56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.993
+ __58-[PLProcessNetworkAgent logEventBackwardUsageWithOutcome:]_block_invoke.265
+ __58-[PLProcessNetworkAgent logEventBackwardUsageWithOutcome:]_block_invoke.268
+ __61-[PLBluetoothAgent btDeviceConnectionNotification:forDevice:]_block_invoke.408
+ __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.879
+ __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.885
+ __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.948
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1574
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1581
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1586
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1594
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1605
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1606
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1619
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1621
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1625
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1650
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1651
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1587
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1601
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1620
+ __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1644
+ __65-[PLPowerAssertionAgent checkAssertionBufferFullNotificationRate]_block_invoke.428
+ __65-[PLPowerAssertionAgent checkAssertionBufferFullNotificationRate]_block_invoke.435
+ __69-[PLIOReportAgent logEventBackwardIOReportWithDelta:forChannelGroup:]_block_invoke.11361
+ __70-[PLIOReportAgent channelDictionaryWithChannelSet:withMinProcessTime:]_block_invoke.10243
+ __70-[PLIOReportAgent channelDictionaryWithChannelSet:withMinProcessTime:]_block_invoke.10249
+ __71-[PLWifiAgent logEventBackwardWifiPropertiesMac:withNetworkProperties:]_block_invoke.1068
+ __71-[PLWifiAgent logEventBackwardWifiPropertiesMac:withNetworkProperties:]_block_invoke.1217
+ __77-[PLPowerAssertionAgent setAssertionBufferFullNotificationActive:withReason:]_block_invoke.445
+ __77-[PLPowerAssertionAgent setAssertionBufferFullNotificationActive:withReason:]_block_invoke.461
+ __78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.759
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.485
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.579
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.585
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.634
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_2.647
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_3.654
+ __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_4.661
+ __PowerChangedCallback_block_invoke.406
+ __PowerChangedCallback_block_invoke.412
+ __PowerChangedCallback_block_invoke.416
+ __PowerChangedCallback_block_invoke.422
+ __PowerChangedCallback_block_invoke.428
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN12PLProcessCPU12inode_data_tEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEE5resetB8ne190102EPS7_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKyN12PLProcessCPU12inode_data_tEEELi0EEEvPT_
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___32+[PLDisplayAgent dcpSubFrameMap]_block_invoke
+ ___38-[PLSMCMetricsAgent logSMCLookUpTable]_block_invoke
+ ___41-[PLIOReportMetricsAgent buildCustomSet:]_block_invoke
+ ___45-[PLSMCMetricsAgent getPowerDeliveryCLVRKeys]_block_invoke
+ ___45-[PLSMCMetricsAgent logEventPointInstantKeys]_block_invoke
+ ___45-[PLSMCMetricsAgent logPowerDeliveryCLVRKeys]_block_invoke
+ ___58-[PLIOReportMetricsAgent channelDictionaryWithChannelSet:]_block_invoke
+ ___PLLogBluetooth_block_invoke
+ ___PLLogButton_block_invoke
+ ___PLLogConfig_block_invoke
+ ___PLLogFSEvent_block_invoke
+ ___PLLogLocation_block_invoke
+ ___PLLogPerformance_block_invoke
+ ___PLLogPeripheral_block_invoke
+ ___PLLogSleepWake_block_invoke
+ ___PLLogVideo_block_invoke
+ ___PLLogWindowServer_block_invoke
+ ___block_descriptor_37_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e33_v16?0"<SLDataTimelineProcess>"8l
+ ___block_descriptor_48_e8_32r40w_e40_v16?0"<SLDataTimelineServerSnapshot>"8l
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24l
+ ___block_descriptor_49_e8_32s40s_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_57_e8_32s40s48s_e25_i16?0^{__CFDictionary=}8l
+ ___copy_helper_block_e8_32r40w
+ ___destroy_helper_block_e8_32r40w
+ ___strcat_chk
+ ___strcpy_chk
+ ___strncpy_chk
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.1045
+ __block_literal_global.10541
+ __block_literal_global.10626
+ __block_literal_global.10628
+ __block_literal_global.10661
+ __block_literal_global.10797
+ __block_literal_global.10815
+ __block_literal_global.10992
+ __block_literal_global.1143
+ __block_literal_global.1145
+ __block_literal_global.1147
+ __block_literal_global.11481
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
+ __block_literal_global.245
+ __block_literal_global.248
+ __block_literal_global.274
+ __block_literal_global.280
+ __block_literal_global.282
+ __block_literal_global.290
+ __block_literal_global.295
+ __block_literal_global.2950
+ __block_literal_global.303
+ __block_literal_global.311
+ __block_literal_global.316
+ __block_literal_global.324
+ __block_literal_global.326
+ __block_literal_global.358
+ __block_literal_global.38
+ __block_literal_global.445
+ __block_literal_global.478
+ __block_literal_global.49
+ __block_literal_global.495
+ __block_literal_global.7300
+ __block_literal_global.750
+ __block_literal_global.761
+ __block_literal_global.763
+ __block_literal_global.8773
+ __block_literal_global.8784
+ __block_literal_global.88
+ __block_literal_global.96
+ __fakeSleep_block_invoke.361
+ __fakeSleep_block_invoke.373
+ __fakeSleep_block_invoke.377
+ __fakeSleep_block_invoke.385
+ _assistantdProcessName
+ _kPLBluetoothAgentEventBackwardWakeupVSE
+ _kPLPerformanceAgentEventPointIdleReaper
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
+ _kPLVideoAgentEventBackwardCMVideoQueue
+ _kUsageNetworkBtInBytes
+ _kUsageNetworkBtOutBytes
+ _objc_msgSend$HDRHeadroom
+ _objc_msgSend$advertisingDataDescription::
+ _objc_msgSend$buildCustomSet:
+ _objc_msgSend$channelDictionaryWithChannelSet:
+ _objc_msgSend$convertMessageProtocol:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$displayOn
+ _objc_msgSend$entryEventBackwardWakeupVSE
+ _objc_msgSend$entryEventNoneDefinitionColdBoot
+ _objc_msgSend$entryEventPointDefinitionIdleReaper
+ _objc_msgSend$entryEventPointDefinitionIncomingPushProxyMessages
+ _objc_msgSend$entryEventPointDefinitionOutgoingPushProxyMessages
+ _objc_msgSend$getJetsamPriority:
+ _objc_msgSend$getPowerDeliveryCLVRKeys
+ _objc_msgSend$handleMessageEvent:isSentEvent:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$isDynamicTable:
+ _objc_msgSend$logColdBoot
+ _objc_msgSend$logEventBackwardCMVideoQueueWithEntry:
+ _objc_msgSend$logEventEventForwardMessageTranscript:
+ _objc_msgSend$logEventIntervalWakeVSE:
+ _objc_msgSend$logEventPointIdleReaper
+ _objc_msgSend$logPowerDeliveryCLVRKeys
+ _objc_msgSend$logPushProxyMessages:forMessageType:
+ _objc_msgSend$logSMCLookUpTable
+ _objc_msgSend$optimizesSubSecondAssertions
+ _objc_msgSend$pluggedIn
+ _objc_msgSend$powerDeliveryCallback
+ _objc_msgSend$powerDeliveryCounter
+ _objc_msgSend$sampleChannelsCustom
+ _objc_msgSend$setBtHCIVSEListener:
+ _objc_msgSend$setCMVideoQueueListener:
+ _objc_msgSend$setDisplayOn:
+ _objc_msgSend$setHDRHeadroom:
+ _objc_msgSend$setMessageForegroundXPCListener:
+ _objc_msgSend$setMessageReceivedListener:
+ _objc_msgSend$setMessageSentListener:
+ _objc_msgSend$setOptimizesSubSecondAssertions:
+ _objc_msgSend$setPluggedIn:
+ _objc_msgSend$setPowerDeliveryCounter:
+ _objc_msgSend$setPushProxyIncomingListener:
+ _objc_msgSend$setPushProxyOutgoingListener:
+ _objc_msgSend$setTimeAtPriorityMATU:
+ _objc_msgSend$shouldLogEnhancedStats
+ _objc_msgSend$shouldLogMarconi
+ _objc_msgSend$strip
+ _objc_msgSend$timeAtPriorityMATU
+ _objc_msgSend$updateDisplayState
+ _objc_msgSend$updateOptimizeSubSecondAssertions
+ _objc_msgSend$updatePluggedInState
+ _objc_msgSend$writeSMCKey:withValue:
+ _resolveColumnLabels.columnLabel
+ _resolveReadWriteColumnLabels.columnLabel
+ _strchr
+ _strstr
+ initKernelEvent.wakeSrc
- +[PLIOReportAgent entryEventBackwardDefinitionMTPCaptureButton]
- +[PLWifiAgent isNonUDMMac]
- -[PLButtonAgent captureButtonActionListener]
- -[PLButtonAgent logEventBackwardCaptureButtonAction:]
- -[PLButtonAgent setCaptureButtonActionListener:]
- -[PLIOReportMetricsAgent channelDictionaryWithChannelSet:withMinProcessTime:]
- GCC_except_table190
- GCC_except_table22
- GCC_except_table254
- GCC_except_table260
- GCC_except_table265
- GCC_except_table30
- GCC_except_table33
- GCC_except_table35
- GCC_except_table42
- GCC_except_table47
- GCC_except_table49
- GCC_except_table59
- GCC_except_table62
- __22-[PLDisplayAgent init]_block_invoke.1178
- __22-[PLDisplayAgent init]_block_invoke.1187
- __22-[PLDisplayAgent init]_block_invoke.1197
- __22-[PLDisplayAgent init]_block_invoke.1201
- __22-[PLDisplayAgent init]_block_invoke.1207
- __22-[PLDisplayAgent init]_block_invoke.1211
- __22-[PLDisplayAgent init]_block_invoke.1215
- __22-[PLDisplayAgent init]_block_invoke.1233
- __22-[PLDisplayAgent init]_block_invoke.1243
- __22-[PLDisplayAgent init]_block_invoke.1255
- __22-[PLDisplayAgent init]_block_invoke.1262
- __22-[PLDisplayAgent init]_block_invoke_2.1227
- __22-[PLDisplayAgent init]_block_invoke_2.1245
- __22-[PLDisplayAgent init]_block_invoke_2.1256
- __23-[PLLocationAgent init]_block_invoke.263
- __23-[PLLocationAgent init]_block_invoke_2.264
- __27-[PLConfigAgent deviceName]_block_invoke.262
- __30-[PLCoalitionAgent logToAggd:]_block_invoke.698
- __30-[PLConfigAgent logEntryToCA:]_block_invoke.374
- __30-[PLConfigAgent logEntryToCA:]_block_invoke.382
- __30-[PLConfigAgent logEntryToCA:]_block_invoke.394
- __33+[PLPushAgent bundleIdFromTopic:]_block_invoke.274
- __33-[PLFSEventAgent startMonitoring]_block_invoke.45
- __33-[PLNetworkAgent initKernelEvent]_block_invoke.103
- __33-[PLNetworkAgent initKernelEvent]_block_invoke.83
- __33-[PLNetworkAgent initKernelEvent]_block_invoke.89
- __33-[PLNetworkAgent initKernelEvent]_block_invoke.95
- __33-[PLNetworkAgent initKernelEvent]_block_invoke.99
- __33-[PLNetworkAgent initKernelEvent]_block_invoke_2.106
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.784
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.790
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.826
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.842
- __33-[PLWifiAgent logEventPointWake:]_block_invoke.854
- __34+[PLSMCAgent reportPMUEventsToCA:]_block_invoke.1200
- __36-[PLPerformanceAgent countMachPort:]_block_invoke.322
- __36-[PLSleepWakeAgent logSleepEntries:]_block_invoke.184
- __36-[PLSleepWakeAgent logSleepEntries:]_block_invoke.193
- __37-[PLIOReportAgent logEngagementToCA:]_block_invoke.11469
- __37-[PLIOReportAgent logEngagementToCA:]_block_invoke.11484
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.537
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.543
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.550
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.559
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.571
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.577
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.583
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.592
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.598
- __37-[PLPowerAssertionAgent logInterval:]_block_invoke.604
- __37-[PLPowerAssertionAgent logSnapshot:]_block_invoke.506
- __37-[PLPowerAssertionAgent logSnapshot:]_block_invoke.515
- __37-[PLXPCAgent logEventForwardGMSOptIn]_block_invoke.2399
- __38-[PLLocationAgent resyncActiveClients]_block_invoke.433
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1027
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1030
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1037
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke.1044
- __38-[PLSMCAgent initOperatorDependancies]_block_invoke_2.1045
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1648
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1656
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1664
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1672
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1680
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1688
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1696
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1704
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1712
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1723
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1734
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1745
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1756
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1767
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1777
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1785
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1790
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1797
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1804
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1812
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1819
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1824
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1834
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1842
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1850
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1855
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1863
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1873
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1883
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1890
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1900
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1907
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1917
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1927
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1937
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1946
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1967
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1975
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1983
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.1993
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2003
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2011
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2021
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2031
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2041
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2051
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2059
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2067
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2072
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2077
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2082
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2087
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2094
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2099
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2104
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2109
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2116
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2123
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2133
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2141
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2149
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2157
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2165
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2170
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2180
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2187
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2197
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2207
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2217
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2227
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2234
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2242
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2250
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2257
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2262
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2269
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2274
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2282
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2287
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2295
- __38-[PLXPCAgent initOperatorDependancies]_block_invoke.2308
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.107
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.116
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.122
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.131
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.142
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke.98
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke_2.108
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke_2.117
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke_2.123
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke_2.132
- __39-[PLMDNSAgent initOperatorDependancies]_block_invoke_2.99
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.160
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.175
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.183
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.191
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.197
- __39-[PLPushAgent initOperatorDependancies]_block_invoke.208
- __39-[PLPushAgent initOperatorDependancies]_block_invoke_2.192
- __40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1454
- __40-[PLSleepWakeAgent capabilitiesChanged:]_block_invoke.168
- __40-[PLSleepWakeAgent capabilitiesChanged:]_block_invoke.174
- __40-[PLVideoAgent initOperatorDependancies]_block_invoke.138
- __40-[PLVideoAgent initOperatorDependancies]_block_invoke.146
- __40-[PLVideoAgent initOperatorDependancies]_block_invoke.154
- __40-[PLVideoAgent initOperatorDependancies]_block_invoke.162
- __40-[PLVideoAgent initOperatorDependancies]_block_invoke.170
- __40-[PLVideoAgent initOperatorDependancies]_block_invoke.180
- __40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1008
- __41-[PLButtonAgent initOperatorDependancies]_block_invoke.74
- __41-[PLConfigAgent initOperatorDependancies]_block_invoke.282
- __41-[PLConfigAgent initOperatorDependancies]_block_invoke.286
- __41-[PLIOReportAgent samplePSRChannelsDelta]_block_invoke.11059
- __41-[PLProcessNetworkAgent didAddNewSource:]_block_invoke.210
- __41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.1117
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1277
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1278
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1290
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1295
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1296
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1306
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1318
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1329
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1335
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1345
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1356
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1360
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1367
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1297
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1330
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1346
- __42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1361
- __42-[PLFSEventAgent logLogFileName:withName:]_block_invoke.83
- __42-[PLFSEventAgent logLogFileName:withName:]_block_invoke.84
- __42-[PLNetworkAgent initOperatorDependancies]_block_invoke.129
- __42-[PLNetworkAgent initOperatorDependancies]_block_invoke.143
- __42-[PLNetworkAgent initOperatorDependancies]_block_invoke.157
- __42-[PLWindowServerAgent establishConnection]_block_invoke.97
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1544
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1557
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1569
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1579
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1594
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1606
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1623
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1630
- __42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1637
- __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10624
- __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10625
- __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10633
- __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10645
- __43-[PLIOReportAgent initOperatorDependancies]_block_invoke.10647
- __43-[PLIOReportAgent initOperatorDependancies]_block_invoke_2.10634
- __43-[PLIOReportAgent initOperatorDependancies]_block_invoke_2.10648
- __43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.11423
- __43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.11429
- __43-[PLIOReportAgent logEventBackwardMTRAging]_block_invoke.11436
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.305
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.323
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.335
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.344
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.353
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke.361
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.306
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.324
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.336
- __43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.345
- __43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.1105
- __44-[PLBluetoothAgent initOperatorDependancies]_block_invoke.276
- __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.430
- __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.432
- __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.438
- __44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.448
- __44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.412
- __44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.418
- __44-[PLLocationAgent logEventPointClientStatus]_block_invoke.369
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
- __45-[PLMDNSAgent logEventBackwardClientSummary:]_block_invoke.146
- __45-[PLPeripheralAgent initOperatorDependancies]_block_invoke.90
- __45-[PLPeripheralAgent initOperatorDependancies]_block_invoke.91
- __45-[PLSMCMetricsAgent initOperatorDependancies]_block_invoke.22
- __46-[PLBluetoothAgent receivedBTStatusUpdateOSX:]_block_invoke.362
- __46-[PLBluetoothAgent receivedBTStatusUpdateOSX:]_block_invoke.371
- __46-[PLButtonAgent logEventBackwardTrackPadPower]_block_invoke.130
- __46-[PLButtonAgent logEventBackwardTrackPadPower]_block_invoke.148
- __46-[PLButtonAgent logEventBackwardTrackPadPower]_block_invoke.154
- __46-[PLButtonAgent logEventBackwardTrackPadPower]_block_invoke.162
- __46-[PLButtonAgent logEventBackwardTrackPadPower]_block_invoke.168
- __46-[PLPerformanceAgent initOperatorDependancies]_block_invoke.205
- __46-[PLPerformanceAgent initOperatorDependancies]_block_invoke.208
- __46-[PLPerformanceAgent initOperatorDependancies]_block_invoke.222
- __46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.275
- __46-[PLSleepWakeAgent logEventNonePowerNapConfig]_block_invoke.284
- __48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.300
- __48-[PLBluetoothAgent logEventForwardPairedDevices]_block_invoke.303
- __48-[PLIdentityServicesAgent logIDSNetworkEntries:]_block_invoke.274
- __48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.301
- __48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.307
- __48-[PLPerformanceAgent logEventPointJetsamPrority]_block_invoke.313
- __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.110
- __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.117
- __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.121
- __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.127
- __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.130
- __48-[PLWindowServerAgent installTimelineConnection]_block_invoke.136
- __48-[PLWindowServerAgent installTimelineConnection]_block_invoke_2.111
- __48-[PLWindowServerAgent installTimelineConnection]_block_invoke_2.122
- __49-[PLCoalitionAgent logCoalitionObjectDifference:]_block_invoke.736
- __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.159
- __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.172
- __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.183
- __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.197
- __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.212
- __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke.218
- __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke_2.184
- __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke_2.193
- __49-[PLPowerAssertionAgent initOperatorDependancies]_block_invoke_2.201
- __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.182
- __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.190
- __49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.195
- __49-[PLSleepWakeAgent registerForCapabilitiesChange]_block_invoke.214
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1029
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1035
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1041
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1047
- __49-[PLWifiAgent logEventBackwardWifiPropertiesMac:]_block_invoke.1053
- __50-[PLDisplayAgent logEventForwardLinearBrightness:]_block_invoke.1551
- __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.164
- __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.192
- __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.200
- __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke.208
- __51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke_2.172
- __51-[PLSleepWakeAgent logWakeEntries:withCurrentTime:]_block_invoke.197
- __51-[PLSleepWakeAgent registerForUserIdleNotification]_block_invoke.223
- __51-[PLThermalMonitorService initOperatorDependancies]_block_invoke.27
- __51-[PLThermalMonitorService initOperatorDependancies]_block_invoke.40
- __51-[PLWifiAgent logFromLinkChangeCallback:withStats:]_block_invoke.768
- __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.329
- __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.335
- __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.339
- __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke.349
- __52-[PLBluetoothAgent logEventIntervalConnectedDevices]_block_invoke_2.340
- __53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke.296
- __53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke.306
- __53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke.327
- __53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke.334
- __54-[PLIOReportAgent processNotificationForChannelGroup:]_block_invoke.10597
- __55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.960
- __55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.969
- __56-[PLLocationAgent logEventForwardTechStatus_withLimiter]_block_invoke.407
- __56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.996
- __58-[PLLocationAgent logEventForwardClientStatus_withLimiter]_block_invoke.403
- __58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.443
- __58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.449
- __58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.455
- __58-[PLProcessNetworkAgent logEventBackwardUsageWithOutcome:]_block_invoke.293
- __58-[PLProcessNetworkAgent logEventBackwardUsageWithOutcome:]_block_invoke.296
- __61-[PLBluetoothAgent btDeviceConnectionNotification:forDevice:]_block_invoke.356
- __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.882
- __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.888
- __61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.951
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1571
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1578
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1583
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1591
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1602
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1603
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1616
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1618
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1622
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1647
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1648
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1584
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1598
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1617
- __63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1641
- __64-[PLProcessNetworkAgent logEventPointConnectionEvent:forSource:]_block_invoke.241
- __65-[PLPowerAssertionAgent checkAssertionBufferFullNotificationRate]_block_invoke.433
- __65-[PLPowerAssertionAgent checkAssertionBufferFullNotificationRate]_block_invoke.440
- __69-[PLIOReportAgent logEventBackwardIOReportWithDelta:forChannelGroup:]_block_invoke.11388
- __70-[PLIOReportAgent channelDictionaryWithChannelSet:withMinProcessTime:]_block_invoke.10270
- __70-[PLIOReportAgent channelDictionaryWithChannelSet:withMinProcessTime:]_block_invoke.10276
- __71-[PLWifiAgent logEventBackwardWifiPropertiesMac:withNetworkProperties:]_block_invoke.1071
- __71-[PLWifiAgent logEventBackwardWifiPropertiesMac:withNetworkProperties:]_block_invoke.1220
- __75-[PLProcessNetworkAgent timestampNetConnectEntry:withEventType:withSource:]_block_invoke.258
- __75-[PLProcessNetworkAgent timestampNetConnectEntry:withEventType:withSource:]_block_invoke.266
- __77-[PLPowerAssertionAgent setAssertionBufferFullNotificationActive:withReason:]_block_invoke.450
- __77-[PLPowerAssertionAgent setAssertionBufferFullNotificationActive:withReason:]_block_invoke.471
- __78-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:]_block_invoke.762
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.480
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.567
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.574
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.614
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_2.627
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_3.634
- __87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke_4.641
- __PowerChangedCallback_block_invoke.500
- __PowerChangedCallback_block_invoke.506
- __PowerChangedCallback_block_invoke.510
- __PowerChangedCallback_block_invoke.516
- __PowerChangedCallback_block_invoke.522
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN12PLProcessCPU12inode_data_tEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEE5resetB8ne180100EPS7_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKyN12PLProcessCPU12inode_data_tEEELi0EEEvPT_
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___106-[PLApplicationAgent logEventForwardApplicationForDisplayID:withPid:withState:withVisibility:withReasons:]_block_invoke
- ___23-[PLLocationAgent init]_block_invoke_2
- ___26+[PLWifiAgent isNonUDMMac]_block_invoke
- ___27-[PLConfigAgent deviceName]_block_invoke
- ___28-[PLPeripheralAgent initLid]_block_invoke_2
- ___30-[PLConfigAgent getMemorySize]_block_invoke
- ___31-[PLSleepWakeAgent wakeReasons]_block_invoke
- ___32-[PLFSEventAgent stopMonitoring]_block_invoke
- ___33-[PLConfigAgent volumeFreespace:]_block_invoke
- ___33-[PLFSEventAgent startMonitoring]_block_invoke_2
- ___33-[PLNetworkAgent initKernelEvent]_block_invoke_2
- ___34-[PLConfigAgent logDeviceDiskSize]_block_invoke
- ___35-[PLNetworkAgent logEventPointWake]_block_invoke
- ___36-[PLSleepWakeAgent logSleepEntries:]_block_invoke
- ___37-[PLSleepWakeAgent driverWakeReasons]_block_invoke
- ___38-[PLLocationAgent resyncActiveClients]_block_invoke
- ___39-[PLMDNSAgent initOperatorDependancies]_block_invoke_2
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke_2
- ___40-[PLSleepWakeAgent capabilitiesChanged:]_block_invoke
- ___40-[PLVideoAgent initOperatorDependancies]_block_invoke_2
- ___41-[PLSleepWakeAgent wakeReasonsAsNSString]_block_invoke
- ___42-[PLPushAgent checkPushUsage:withPLEntry:]_block_invoke
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2
- ___44-[PLBluetoothAgent initOperatorDependancies]_block_invoke_2
- ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke_2
- ___44-[PLSleepWakeAgent logEventPointKernelState]_block_invoke
- ___45-[PLHomeKitAgent logEventPointHomeKitEvents:]_block_invoke
- ___45-[PLIdentityServicesAgent logCloudMessaging:]_block_invoke
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke_2
- ___46-[PLButtonAgent logEventBackwardTrackPadPower]_block_invoke
- ___46-[PLSleepWakeAgent logEventNonePowerNapConfig]_block_invoke
- ___46-[PLVideoAgent logEventForwardVideoWithEntry:]_block_invoke
- ___47-[PLProcessNetworkAgent compressNetworkBitmap:]_block_invoke
- ___48-[PLIdentityServicesAgent logIDSNetworkEntries:]_block_invoke
- ___48-[PLPeripheralAgent logEventForwardDeviceState:]_block_invoke
- ___48-[PLWindowServerAgent installTimelineConnection]_block_invoke_2
- ___49-[PLSleepWakeAgent registerForCapabilitiesChange]_block_invoke
- ___51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke_2
- ___51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke_3
- ___51-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke_4
- ___51-[PLSleepWakeAgent logWakeEntries:withCurrentTime:]_block_invoke
- ___51-[PLSleepWakeAgent registerForUserIdleNotification]_block_invoke_2
- ___51-[PLVideoAgent logEventBackwardVTSessionWithEntry:]_block_invoke
- ___53-[PLSleepWakeAgent logEventPointCurrentScheduledWake]_block_invoke_2
- ___55-[PLIdentityServicesAgent initTaskOperatorDependancies]_block_invoke_2
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke
- ___59-[PLButtonAgent getValue:inHIDReportBuffer:withBufferSize:]_block_invoke
- ___60-[PLLocationAgent logEventNoneClientStatusDebugWithClients:]_block_invoke_2
- ___64-[PLProcessNetworkAgent logEventPointConnectionEvent:forSource:]_block_invoke
- ___73-[PLLocationAgent closeOpenEntryForClient:withOpenEntry:withTimeStopped:]_block_invoke_2
- ___75-[PLProcessNetworkAgent timestampNetConnectEntry:withEventType:withSource:]_block_invoke
- ___77-[PLIOReportMetricsAgent channelDictionaryWithChannelSet:withMinProcessTime:]_block_invoke
- ___78-[PLLocationAgent updateLocalCacheWithClient:withType:withBundleID:withEntry:]_block_invoke
- ___80-[PLProcessNetworkAgent aggregateAndLogNetworkBitmaps:withStartTime:andEndTime:]_block_invoke
- ___96-[PLWindowServerAgent logEventForwardTimelineInfo:withPID:withnewProcess:withSnapshotTimestamp:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e33_v16?0"<SLDataTimelineProcess>"8l
- ___block_descriptor_49_e8_32s40s_e25_i16?0^{__CFDictionary=}8l
- ___block_descriptor_56_e8_32s40r48w_e40_v16?0"<SLDataTimelineServerSnapshot>"8l
- __block_literal_global.1039
- __block_literal_global.10568
- __block_literal_global.10653
- __block_literal_global.10655
- __block_literal_global.10688
- __block_literal_global.10824
- __block_literal_global.10842
- __block_literal_global.11019
- __block_literal_global.1131
- __block_literal_global.1134
- __block_literal_global.1136
- __block_literal_global.1138
- __block_literal_global.1142
- __block_literal_global.1144
- __block_literal_global.1146
- __block_literal_global.1148
- __block_literal_global.11508
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
- __block_literal_global.226
- __block_literal_global.2297
- __block_literal_global.234
- __block_literal_global.239
- __block_literal_global.247
- __block_literal_global.255
- __block_literal_global.260
- __block_literal_global.268
- __block_literal_global.270
- __block_literal_global.273
- __block_literal_global.2977
- __block_literal_global.364
- __block_literal_global.440
- __block_literal_global.473
- __block_literal_global.500
- __block_literal_global.58
- __block_literal_global.7327
- __block_literal_global.741
- __block_literal_global.743
- __block_literal_global.757
- __block_literal_global.8800
- __block_literal_global.8811
- __fakeSleep_block_invoke.455
- __fakeSleep_block_invoke.467
- __fakeSleep_block_invoke.471
- __fakeSleep_block_invoke.479
- _kPLActiveFreqF1
- _kPLActiveFreqF2
- _kPLActiveFreqlockout
- _kPLBaselineTrackingFreqF1
- _kPLBaselineTrackingFreqF2
- _kPLBaselineTrackingFreqlockout
- _kPLHighLevelStateActive
- _kPLHighLevelStateBaseline
- _kPLIOReportAgentEventBackwardNameMTPCaptureButton
- _kPLPowerAssertionAgentIsCoalesced
- _objc_msgSend$getJetamPriority:
- _objc_msgSend$isNonUDMMac
- _objc_msgSend$logBatteryEntry:
- _objc_msgSend$logDisplayEntry:
- _objc_msgSend$logEventBackwardCaptureButtonAction:
- _objc_msgSend$setCaptureButtonActionListener:
CStrings:
+ "\n%s"
+ " :"
+ "%@ payload is empty"
+ "%@%lu"
+ "%cO: Ops p 0/1/2/3,%cL: SumLatency p 0/1/2/3,%cM: MaxLatency p 0/1/2/3,"
+ "%u %u,"
+ "/%u"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLIOReportAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLIOReportAgentIOReportStats.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLMacCPUGPUAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLBluetoothAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLWifiAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLFSEventAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPerformanceAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPowerAssertionAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScheduledWakeAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDebugService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetServiceDAS.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLTestService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
+ "31011"
+ "@24@0:8^{IOReportGroupChecks=BBBBB}16"
+ "ANS2,MSP0"
+ "ANS2MSP0"
+ "ASPFTLParseBufferToCxt: RD_closedBandEvictBlocks(1222) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: RD_closedBlocksTHHist(1223): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: RD_closedBlocksTHHist(1223): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: RD_openBandEvictBlocks(1221) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: asyncMessageHisto(1367): (#32) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: asyncMessageHisto(1367): Cannot add 32 elements to context"
+ "ASPFTLParseBufferToCxt: bitsPerCell(1285) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: bpHostChokeTime(1295): (#8) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bpHostChokeTime(1295): Cannot add 8 elements to context"
+ "ASPFTLParseBufferToCxt: bpZone2EntryGCTP(1303): (#16) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bpZone2EntryGCTP(1303): Cannot add 16 elements to context"
+ "ASPFTLParseBufferToCxt: bpZone2EntryHW(1296): (#16) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bpZone2EntryHW(1296): Cannot add 16 elements to context"
+ "ASPFTLParseBufferToCxt: bpZone2EntryHostTP(1302): (#16) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bpZone2EntryHostTP(1302): Cannot add 16 elements to context"
+ "ASPFTLParseBufferToCxt: bpZone2EntryTime(1293): (#16) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bpZone2EntryTime(1293): Cannot add 16 elements to context"
+ "ASPFTLParseBufferToCxt: bpZone2ExitGCTP(1305): (#16) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bpZone2ExitGCTP(1305): Cannot add 16 elements to context"
+ "ASPFTLParseBufferToCxt: bpZone2ExitHW(1298): (#16) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bpZone2ExitHW(1298): Cannot add 16 elements to context"
+ "ASPFTLParseBufferToCxt: bpZone2ExitHostTP(1304): (#16) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bpZone2ExitHostTP(1304): Cannot add 16 elements to context"
+ "ASPFTLParseBufferToCxt: bpZone2ExitTime(1294): (#16) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bpZone2ExitTime(1294): Cannot add 16 elements to context"
+ "ASPFTLParseBufferToCxt: crossTempColdEvict(1355) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: crossTempColdHotEvict(1357) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: crossTempHotEvict(1356) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: deviceTempHigh(1272) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: deviceTempLow(1273) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: deviceTempMax(1271) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanEarlyExits(1327) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanFullRounds(1326) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanIgnoredTooFrequent(1368) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanMspEarlyExitRequests(1329) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanMspFullScanRequests(1328) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerLevel(207): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerLevel(207): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerReadLevel(453): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerReadLevel(453): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerWriteLevel(454): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerWriteLevel(454): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: numOfThrottlingLevels(1354) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: numRefreshOnErrNandRefreshPerfOpt(1264) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: numRefreshOnErrNandRefreshPerfOptOpen(1289) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: prefetchNofHits(1323) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: raidBlkParityBands(964) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: raidBlkParitySecs(965) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: realGBBPerDipOfFailingDie(1369): (#8) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: realGBBPerDipOfFailingDie(1369): Cannot add 8 elements to context"
+ "ASPFTLParseBufferToCxt: tempChangedEnterETHisto(1359): (#13) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: tempChangedEnterETHisto(1359): Cannot add 13 elements to context"
+ "ASPFTLParseBufferToCxt: tempChangedHisto(1358): (#13) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: tempChangedHisto(1358): Cannot add 13 elements to context"
+ "ASPFTLParseBufferToCxt: thermalSelfThrottlingEnabled(1349) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: thermalSelfThrottlingSupported(1348) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerLevel(865): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerLevel(865): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerReadLevel(866): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerReadLevel(866): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerWriteLevel(867): (#25) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: timeOfThrottlingPerWriteLevel(867): Cannot add 25 elements to context"
+ "ASPFTLParseBufferToCxt: unhappyVertGC(1345): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: unhappyVertGC(1345): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: unhappyWideGC1(1344): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: unhappyWideGC1(1344): Cannot add 4 elements to context"
+ "ASPMSPParseBufferToCxt: boot_rd_neg_win_hist_all_dies(8264): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: boot_rd_neg_win_hist_all_dies(8264): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_rd_neg_win_hist_ch0_die0(8267): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: boot_rd_neg_win_hist_ch0_die0(8267): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_rd_pos_win_hist_all_dies(8263): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: boot_rd_pos_win_hist_all_dies(8263): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_rd_pos_win_hist_ch0_die0(8266): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: boot_rd_pos_win_hist_ch0_die0(8266): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_rd_sdl_overflow(8261): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: boot_rd_sdl_overflow(8261): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_rd_training_failure(8259): Error adding 3 elements to context"
+ "ASPMSPParseBufferToCxt: boot_rd_training_failure(8259): cfg 3 elements; (3*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_vs_pge_rd_n_c0d0_hist(8283): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: boot_vs_pge_rd_n_c0d0_hist(8283): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_vs_pge_rd_p_c0d0_hist(8282): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: boot_vs_pge_rd_p_c0d0_hist(8282): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_vs_pge_wr_c0d0_hist(8284): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: boot_vs_pge_wr_c0d0_hist(8284): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_wr_sdl_overflow(8262): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: boot_wr_sdl_overflow(8262): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_wr_training_failure(8260): Error adding 3 elements to context"
+ "ASPMSPParseBufferToCxt: boot_wr_training_failure(8260): cfg 3 elements; (3*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_wr_win_hist_all_dies(8265): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: boot_wr_win_hist_all_dies(8265): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: boot_wr_win_hist_ch0_die0(8268): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: boot_wr_win_hist_ch0_die0(8268): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: coge_cache_hit_program(16396): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: coge_cache_hit_program(16396): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: coge_cache_hit_read(16394): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: coge_cache_hit_read(16394): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: coge_cache_miss_program(16397): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: coge_cache_miss_program(16397): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: coge_cache_miss_read(16395): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: coge_cache_miss_read(16395): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: coge_lru_num_of_replacement(16398): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: coge_lru_num_of_replacement(16398): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: coge_lru_num_of_searches(16399): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: coge_lru_num_of_searches(16399): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter145(4303): Error adding 2 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter145(4303): cfg 2 elements; (2*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter146(4304): Error adding 2 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter146(4304): cfg 2 elements; (2*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter147(4305): Error adding 2 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter147(4305): cfg 2 elements; (2*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter148(4306): Error adding 2 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter148(4306): cfg 2 elements; (2*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter149(4307): Error adding 8 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter149(4307): cfg 8 elements; (8*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter150(4308): Error adding 6 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter150(4308): cfg 6 elements; (6*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter151(4309): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter151(4309): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter152(4315): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter152(4315): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter153(4316): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter153(4316): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter154(4317): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter154(4317): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter155(4321): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter155(4321): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter156(4322): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter156(4322): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter157(4323): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter157(4323): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter158(4329): Error adding 8 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter158(4329): cfg 8 elements; (8*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter159(4330): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter159(4330): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter160(4335): Error adding 12 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter160(4335): cfg 12 elements; (12*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter161(4343): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter161(4343): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter162(4344): Error adding 3 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter162(4344): cfg 3 elements; (3*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter163(4346): Error adding 8 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter163(4346): cfg 8 elements; (8*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter164(4347): Error adding 8 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter164(4347): cfg 8 elements; (8*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter165(4348): Error adding 8 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter165(4348): cfg 8 elements; (8*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter166(4349): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter166(4349): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter167(4350): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter167(4350): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter168(4351): Error adding 3 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter168(4351): cfg 3 elements; (3*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter169(4352): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: dspExceptionParameter169(4352): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: initialReadStage11(12331): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: initialReadStage11(12331): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: initialReadStage12(12332): Error adding 8 elements to context"
+ "ASPMSPParseBufferToCxt: initialReadStage12(12332): cfg 8 elements; (8*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: initialReadStage13(12333): Error adding 6 elements to context"
+ "ASPMSPParseBufferToCxt: initialReadStage13(12333): cfg 6 elements; (6*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: msp_number_hw_sram_flips(8258): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: msp_number_hw_sram_flips(8258): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife105(4301): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife105(4301): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife106(4302): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife106(4302): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife107(4310): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife107(4310): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife108(4311): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife108(4311): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife109(4312): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife109(4312): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife110(4313): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife110(4313): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife111(4314): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife111(4314): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife112(4318): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife112(4318): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife113(4319): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife113(4319): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife114(4320): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife114(4320): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife115(4325): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife115(4325): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife116(4326): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife116(4326): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife117(4327): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife117(4327): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife118(4336): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife118(4336): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: nandStageOfLife119(4337): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: nandStageOfLife119(4337): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: num_of_steps_bigger_win(8301): Error adding 7 elements to context"
+ "ASPMSPParseBufferToCxt: num_of_steps_bigger_win(8301): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: num_of_steps_smaller_win(8302): Error adding 7 elements to context"
+ "ASPMSPParseBufferToCxt: num_of_steps_smaller_win(8302): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: periodic_rd_sdl_overflow(8290): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: periodic_rd_sdl_overflow(8290): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: periodic_rd_training_failure(8285): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: periodic_rd_training_failure(8285): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: periodic_rd_training_hist(8294): Error adding 7 elements to context"
+ "ASPMSPParseBufferToCxt: periodic_rd_training_hist(8294): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: periodic_rd_training_latency(8296): Error adding 7 elements to context"
+ "ASPMSPParseBufferToCxt: periodic_rd_training_latency(8296): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: periodic_wr_sdl_overflow(8291): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: periodic_wr_sdl_overflow(8291): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: periodic_wr_training_failure(8286): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: periodic_wr_training_failure(8286): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: periodic_wr_training_hist(8295): Error adding 7 elements to context"
+ "ASPMSPParseBufferToCxt: periodic_wr_training_hist(8295): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: periodic_wr_training_latency(8297): Error adding 7 elements to context"
+ "ASPMSPParseBufferToCxt: periodic_wr_training_latency(8297): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_rd_neg_win_hist_all_dies(8277): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: pge_rd_neg_win_hist_all_dies(8277): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_rd_neg_win_hist_ch0_die0(8280): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: pge_rd_neg_win_hist_ch0_die0(8280): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_rd_pos_win_hist_all_dies(8276): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: pge_rd_pos_win_hist_all_dies(8276): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_rd_pos_win_hist_ch0_die0(8279): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: pge_rd_pos_win_hist_ch0_die0(8279): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_rd_sdl_overflow(8274): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: pge_rd_sdl_overflow(8274): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_rd_training_failure(8272): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: pge_rd_training_failure(8272): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_vs_periodic_rd_n_c0d0_hist(8288): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: pge_vs_periodic_rd_n_c0d0_hist(8288): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_vs_periodic_rd_p_c0d0_hist(8287): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: pge_vs_periodic_rd_p_c0d0_hist(8287): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_vs_periodic_wr_c0d0_hist(8289): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: pge_vs_periodic_wr_c0d0_hist(8289): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_wr_sdl_overflow(8275): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: pge_wr_sdl_overflow(8275): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_wr_training_failure(8273): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: pge_wr_training_failure(8273): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_wr_win_hist_all_dies(8278): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: pge_wr_win_hist_all_dies(8278): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pge_wr_win_hist_ch0_die0(8281): Error adding 5 elements to context"
+ "ASPMSPParseBufferToCxt: pge_wr_win_hist_ch0_die0(8281): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pts_vs_boot_mid_rd_n_c0d0_hist(8270): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: pts_vs_boot_mid_rd_n_c0d0_hist(8270): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pts_vs_boot_mid_rd_p_c0d0_hist(8269): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: pts_vs_boot_mid_rd_p_c0d0_hist(8269): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: pts_vs_boot_mid_wr_c0d0_hist(8271): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: pts_vs_boot_mid_wr_c0d0_hist(8271): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStage111(4324): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: readStage111(4324): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStage112(4331): Error adding 6 elements to context"
+ "ASPMSPParseBufferToCxt: readStage112(4331): cfg 6 elements; (6*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStage113(4333): Error adding 4 elements to context"
+ "ASPMSPParseBufferToCxt: readStage113(4333): cfg 4 elements; (4*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStage114(4334): Error adding 4 elements to context"
+ "ASPMSPParseBufferToCxt: readStage114(4334): cfg 4 elements; (4*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStage115(4338): Error adding 10 elements to context"
+ "ASPMSPParseBufferToCxt: readStage115(4338): cfg 10 elements; (10*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStage116(4341): Error adding 4 elements to context"
+ "ASPMSPParseBufferToCxt: readStage116(4341): cfg 4 elements; (4*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStage117(4342): Error adding 10 elements to context"
+ "ASPMSPParseBufferToCxt: readStage117(4342): cfg 10 elements; (10*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStage118(4345): Error adding 10 elements to context"
+ "ASPMSPParseBufferToCxt: readStage118(4345): cfg 10 elements; (10*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStageFail0(4332): Error adding 8 elements to context"
+ "ASPMSPParseBufferToCxt: readStageFail0(4332): cfg 8 elements; (8*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStageFail1(4339): Error adding 10 elements to context"
+ "ASPMSPParseBufferToCxt: readStageFail1(4339): cfg 10 elements; (10*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: readStageFail2(4340): Error adding 3 elements to context"
+ "ASPMSPParseBufferToCxt: readStageFail2(4340): cfg 3 elements; (3*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: system_temp(8298): Error adding 12 elements to context"
+ "ASPMSPParseBufferToCxt: system_temp(8298): cfg 12 elements; (12*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: temp_diff_150ms(8299): Error adding 12 elements to context"
+ "ASPMSPParseBufferToCxt: temp_diff_150ms(8299): cfg 12 elements; (12*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: temp_diff_1s(8300): Error adding 12 elements to context"
+ "ASPMSPParseBufferToCxt: temp_diff_1s(8300): cfg 12 elements; (12*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: too_frequent_temp_change_rd(8292): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: too_frequent_temp_change_rd(8292): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "ASPMSPParseBufferToCxt: too_frequent_temp_change_wr(8293): Error adding 1 elements to context"
+ "ASPMSPParseBufferToCxt: too_frequent_temp_change_wr(8293): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
+ "BCM"
+ "BTCompanionIn"
+ "BTCompanionOut"
+ "BTWakeupVSE"
+ "BrightnessTransaction"
+ "CM-VIDEOQUEUE"
+ "CMVideoQueue"
+ "Capture Timestamp,"
+ "ColdBoot"
+ "Config - Device upgrade timestamp is %@ and system boot time is %@"
+ "ConversationType"
+ "Could not clear counts for rail mode %d"
+ "Could not set threshold rail mode to %d"
+ "DPE_"
+ "Display state has changed to: %@"
+ "EnableLegacySMC"
+ "F"
+ "FSEvent"
+ "FeatureFlag"
+ "Force Cloud Messaging callback: %@"
+ "HDRHeadroom"
+ "HomeKitEvent callback for PLHomeKitAgent_EventPoint_HomeKitEvents: %@"
+ "HostWakeReport"
+ "HostWakeReport payload: %@"
+ "IDS IncomingPushReceived payload %@"
+ "IDS Local InfraWiFi Request callback: %@"
+ "IDS Local Link callback: %@"
+ "IDS Local Message Received callback: %@"
+ "IDS Local Network Stats callback recieved payload %@"
+ "IDS OutgoingPushSent payload %@"
+ "ISPISPEvents"
+ "IdleReaper"
+ "In updateOptimizeSubSecondAssertions: %d; self.gameMode: %d; self.displayOn: %d; self.pluggedIn: %d "
+ "IncomingProxyMessages"
+ "InstantKeyValues"
+ "InstantLookUpTable"
+ "KeyIndex"
+ "List of power delivery metrics to be logged (count %d): %@"
+ "Log cold boot key with value in volts %@"
+ "LogLevel changed with payload=%@"
+ "Logging Power Delivery CLVR Payload: %@"
+ "Message TranscriptForeground monotonic eventTime: %@"
+ "Message TranscriptForeground payload: %@"
+ "Message::TranscriptForeground"
+ "MessageForegroundXPCListener"
+ "MessageGUID"
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
+ "PLSMCAgent_EventBackward_PowerDeliveryCLVRKeys"
+ "PLVideoAgent::kPLVideoAgentRegistrationCMVideoQueue PlayTimeWC is smaller than one second, skipping this log"
+ "PLVideoAgent::kPLVideoAgentRegistrationCMVideoQueue: payload=%@"
+ "PeerType"
+ "Peripheral"
+ "PluggedIn state has changed to: %d"
+ "Power delivery callback (count %d)"
+ "PowerDeliveryCLVRKeys"
+ "ProcessNetwork"
+ "Protocol"
+ "ProxyCommand"
+ "PushType"
+ "RCS"
+ "RD_closedBlocksTHHist_"
+ "RailMode"
+ "Received ThermalChangeNotification from SMC Agent: %@"
+ "Received messages update, isSentEvent: %@, payload: %@"
+ "ResetData: %@"
+ "SATR"
+ "SMC Metrics: logging SMC Look-up table: %@"
+ "SMS"
+ "SatelliteSMS"
+ "Set the previous update build to last build"
+ "SleepWake"
+ "StageManager toggled: %@"
+ "StatusBarOverride changed with payload=%@"
+ "T@\"NSArray\",&,V_loggedKeysArray"
+ "T@\"NSArray\",&,V_loggedPowerDeliveryCLVRKeysArray"
+ "T@\"NSMutableDictionary\",&,N,V_sampleChannelsCustom"
+ "T@\"NSMutableDictionary\",&,V_summarizedNotificationEntries"
+ "T@\"NSNumber\",&,V_HDRHeadroom"
+ "T@\"PLNSNotificationOperatorComposition\",&,V_thermalNotification"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_MessageForegroundXPCListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_btHCIVSEListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_cMVideoQueueListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_messageReceivedListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_messageSentListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_pushProxyIncomingListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_pushProxyOutgoingListener"
+ "TB,V_displayOn"
+ "TB,V_optimizesSubSecondAssertions"
+ "TB,V_pluggedIn"
+ "TI,V_powerDeliveryCounter"
+ "TQ,V_timeAtPriorityMATU"
+ "TVMD"
+ "TVSL"
+ "TVSR"
+ "TVmS"
+ "Target"
+ "ThermalEntryNotification"
+ "Tp002a"
+ "TranscriptForeground"
+ "TranscriptVisibilityState"
+ "VRTC"
+ "VSERaw"
+ "VSEReasonCode"
+ "VSEReasonString"
+ "VSEType"
+ "WakeEventType"
+ "Writing to %u numeric key failed with %d"
+ "_HDRHeadroom"
+ "_MessageForegroundXPCListener"
+ "_btHCIVSEListener"
+ "_cMVideoQueueListener"
+ "_displayOn"
+ "_loggedKeysArray"
+ "_loggedPowerDeliveryCLVRKeysArray"
+ "_messageReceivedListener"
+ "_messageSentListener"
+ "_optimizesSubSecondAssertions"
+ "_pluggedIn"
+ "_powerDeliveryCounter"
+ "_pushProxyIncomingListener"
+ "_pushProxyOutgoingListener"
+ "_sampleChannelsCustom"
+ "_summarizedNotificationEntries"
+ "_thermalNotification"
+ "_timeAtPriorityMATU"
+ "activeTimeInThrottleZone"
+ "app_time_at_jetsam_priority"
+ "assistantd"
+ "asyncMessageHisto"
+ "asyncMessageHisto_"
+ "bandsGBBTempHisto"
+ "bitsPerCell"
+ "blockScanReadBlockAge"
+ "bootArgs"
+ "boot_rd_neg_win_hist_all_dies_"
+ "boot_rd_neg_win_hist_ch0_die0_"
+ "boot_rd_pos_win_hist_all_dies_"
+ "boot_rd_pos_win_hist_ch0_die0_"
+ "boot_rd_sdl_overflow_"
+ "boot_rd_training_failure_"
+ "boot_vs_pge_rd_n_c0d0_hist_"
+ "boot_vs_pge_rd_p_c0d0_hist_"
+ "boot_vs_pge_wr_c0d0_hist_"
+ "boot_wr_sdl_overflow_"
+ "boot_wr_training_failure_"
+ "boot_wr_win_hist_all_dies_"
+ "boot_wr_win_hist_ch0_die0_"
+ "bpHostChokeTime"
+ "bpHostChokeTime_"
+ "bpZone2EntryGCTP"
+ "bpZone2EntryGCTP_"
+ "bpZone2EntryHW"
+ "bpZone2EntryHW_"
+ "bpZone2EntryHostTP"
+ "bpZone2EntryHostTP_"
+ "bpZone2EntryTime"
+ "bpZone2EntryTime_"
+ "bpZone2ExitGCTP"
+ "bpZone2ExitGCTP_"
+ "bpZone2ExitHW"
+ "bpZone2ExitHW_"
+ "bpZone2ExitHostTP"
+ "bpZone2ExitHostTP_"
+ "bpZone2ExitTime"
+ "bpZone2ExitTime_"
+ "btHCIVSEListener"
+ "buildCustomSet:"
+ "cMVideoQueueListener"
+ "cbdrHPScanHP"
+ "cbdrLastScannedHrHP"
+ "cbdrMPScanHP"
+ "cbdrMPScanMP"
+ "cbdrScanHP"
+ "cbdrScanMP"
+ "cePn"
+ "channelDictionaryWithChannelSet:"
+ "clientStatus XPC with payload=%@"
+ "cmDU"
+ "coge_cache_hit_program_"
+ "coge_cache_hit_read_"
+ "coge_cache_miss_program_"
+ "coge_cache_miss_read_"
+ "coge_lru_num_of_replacement_"
+ "coge_lru_num_of_searches_"
+ "configd"
+ "convertMessageProtocol:"
+ "crossTempColdEvict"
+ "crossTempColdHotEvict"
+ "crossTempHotEvict"
+ "daemon_time_at_jetsam_priority"
+ "dcpSubFrameMap"
+ "deviceTempHigh"
+ "deviceTempLow"
+ "deviceTempMax"
+ "dictionaryWithCapacity:"
+ "disableIdleGC"
+ "displayOn"
+ "dspExceptionParameter145_"
+ "dspExceptionParameter146_"
+ "dspExceptionParameter147_"
+ "dspExceptionParameter148_"
+ "dspExceptionParameter149_"
+ "dspExceptionParameter150_"
+ "dspExceptionParameter151_"
+ "dspExceptionParameter152_"
+ "dspExceptionParameter153_"
+ "dspExceptionParameter154_"
+ "dspExceptionParameter155_"
+ "dspExceptionParameter156_"
+ "dspExceptionParameter157_"
+ "dspExceptionParameter158_"
+ "dspExceptionParameter159_"
+ "dspExceptionParameter160_"
+ "dspExceptionParameter161_"
+ "dspExceptionParameter162_"
+ "dspExceptionParameter163_"
+ "dspExceptionParameter164_"
+ "dspExceptionParameter165_"
+ "dspExceptionParameter166_"
+ "dspExceptionParameter167_"
+ "dspExceptionParameter168_"
+ "dspExceptionParameter169_"
+ "enhancedReadBlockAge"
+ "entryEventBackwardWakeupVSE"
+ "entryEventNoneDefinitionColdBoot"
+ "entryEventPointDefinitionIdleReaper"
+ "entryEventPointDefinitionIncomingPushProxyMessages"
+ "entryEventPointDefinitionOutgoingPushProxyMessages"
+ "getJetsamPriority:"
+ "getPowerDeliveryCLVRKeys"
+ "handleMessageEvent:isSentEvent:"
+ "handleStateChange"
+ "iMessageLite"
+ "iMessageReceived"
+ "iMessageReceived payload: %@"
+ "iMessageSent"
+ "iMessageSent payload: %@"
+ "initialReadStage11_"
+ "initialReadStage12_"
+ "initialReadStage13_"
+ "intersectsSet:"
+ "isDynamicTable:"
+ "kern.bootargs"
+ "logColdBoot"
+ "logEventBackwardCMVideoQueueWithEntry:"
+ "logEventEventForwardMessageTranscript:"
+ "logEventPointIdleReaper"
+ "logPowerDeliveryCLVRKeys"
+ "logPushProxyMessages:forMessageType:"
+ "logSMCLookUpTable"
+ "logSleepBedtime:"
+ "logSleepWaketime:"
+ "logd"
+ "loggedKeysArray"
+ "loggedPowerDeliveryCLVRKeysArray"
+ "maNN"
+ "massScanCurrentState"
+ "massScanEarlyExits"
+ "massScanFullRounds"
+ "massScanIgnoredTooFrequent"
+ "massScanMspEarlyExitRequests"
+ "massScanMspFullScanRequests"
+ "messageReceivedListener"
+ "messageSentListener"
+ "msp_number_hw_sram_flips_"
+ "mxT1"
+ "nandStageOfLife105_"
+ "nandStageOfLife106_"
+ "nandStageOfLife107_"
+ "nandStageOfLife108_"
+ "nandStageOfLife109_"
+ "nandStageOfLife110_"
+ "nandStageOfLife111_"
+ "nandStageOfLife112_"
+ "nandStageOfLife113_"
+ "nandStageOfLife114_"
+ "nandStageOfLife115_"
+ "nandStageOfLife116_"
+ "nandStageOfLife117_"
+ "nandStageOfLife118_"
+ "nandStageOfLife119_"
+ "notifyd"
+ "numOfThrottlingLevels"
+ "numPerfOptionalRefreshes"
+ "numRefreshOnErrNandRefreshPerfOpt"
+ "numRefreshOnErrNandRefreshPerfOptOpen"
+ "num_of_steps_bigger_win_"
+ "num_of_steps_smaller_win_"
+ "optimizesSubSecondAssertions"
+ "performance"
+ "periodic_rd_sdl_overflow_"
+ "periodic_rd_training_failure_"
+ "periodic_rd_training_hist_"
+ "periodic_rd_training_latency_"
+ "periodic_wr_sdl_overflow_"
+ "periodic_wr_training_failure_"
+ "periodic_wr_training_hist_"
+ "periodic_wr_training_latency_"
+ "perstStatFree"
+ "pge_rd_neg_win_hist_all_dies_"
+ "pge_rd_neg_win_hist_ch0_die0_"
+ "pge_rd_pos_win_hist_all_dies_"
+ "pge_rd_pos_win_hist_ch0_die0_"
+ "pge_rd_sdl_overflow_"
+ "pge_rd_training_failure_"
+ "pge_vs_periodic_rd_n_c0d0_hist_"
+ "pge_vs_periodic_rd_p_c0d0_hist_"
+ "pge_vs_periodic_wr_c0d0_hist_"
+ "pge_wr_sdl_overflow_"
+ "pge_wr_training_failure_"
+ "pge_wr_win_hist_all_dies_"
+ "pge_wr_win_hist_ch0_die0_"
+ "pluggedIn"
+ "powerDeliveryCallback"
+ "powerDeliveryCounter"
+ "prefetchNofHits"
+ "prefetchRedundantBufs"
+ "prefetchUsedBufs"
+ "pts_vs_boot_mid_rd_n_c0d0_hist_"
+ "pts_vs_boot_mid_rd_p_c0d0_hist_"
+ "pts_vs_boot_mid_wr_c0d0_hist_"
+ "pushProxyIncomingListener"
+ "pushProxyOutgoingListener"
+ "readStage111_"
+ "readStage112_"
+ "readStage113_"
+ "readStage114_"
+ "readStage115_"
+ "readStage116_"
+ "readStage117_"
+ "readStage118_"
+ "readStageFail0_"
+ "readStageFail1_"
+ "readStageFail2_"
+ "realGBBPerDipOfFailingDie"
+ "realGBBPerDipOfFailingDie_"
+ "regularReadBlockAge"
+ "sampleChannelsCustom"
+ "secInColdHisto"
+ "secInHotHisto"
+ "self.optimizesSubSecondAssertions %d"
+ "setBtHCIVSEListener:"
+ "setCMVideoQueueListener:"
+ "setDisplayOn:"
+ "setHDRHeadroom:"
+ "setLoggedKeysArray:"
+ "setLoggedPowerDeliveryCLVRKeysArray:"
+ "setMessageForegroundXPCListener:"
+ "setMessageReceivedListener:"
+ "setMessageSentListener:"
+ "setOptimizesSubSecondAssertions:"
+ "setPluggedIn:"
+ "setPowerDeliveryCounter:"
+ "setPushProxyIncomingListener:"
+ "setPushProxyOutgoingListener:"
+ "setSampleChannelsCustom:"
+ "setSummarizedNotificationEntries:"
+ "setThermalNotification:"
+ "setTimeAtPriorityMATU:"
+ "strip"
+ "subframes(%d)"
+ "summarizedNotificationEntries"
+ "system_temp_"
+ "tempChangedEnterETHisto"
+ "tempChangedEnterETHisto_"
+ "tempChangedHisto"
+ "tempChangedHisto_"
+ "temp_diff_150ms_"
+ "temp_diff_1s_"
+ "thermalNotification"
+ "thermalSelfThrottlingEnabled"
+ "thermalSelfThrottlingSupported"
+ "timeAtPriorityMATU"
+ "too_frequent_temp_change_rd_"
+ "too_frequent_temp_change_wr_"
+ "unable to retrieve kern.bootargs"
+ "unable to retrieve size of kern.bootargs"
+ "undecodable LE ADV"
+ "unhappyVertGC"
+ "unhappyVertGC_"
+ "unhappyWideGC1"
+ "unhappyWideGC1_"
+ "updateDisplayState"
+ "updateOptimizeSubSecondAssertions"
+ "updatePluggedInState"
+ "writeSMCKey:withValue:"
+ "{IOReportGroupChecks=BBBBB}16@0:8"
- "\t"
- "%4u"
- "%5u"
- "%7u"
- "%u %u"
- "- ASP Snapshot - \n%s\n"
- "-[PLApplicationAgent logEventForwardApplicationForDisplayID:withPid:withState:withVisibility:withReasons:]"
- "-[PLButtonAgent getValue:inHIDReportBuffer:withBufferSize:]"
- "-[PLButtonAgent logEventBackwardTrackPadPower]"
- "-[PLConfigAgent deviceName]"
- "-[PLConfigAgent getMemorySize]"
- "-[PLConfigAgent logDeviceDiskSize]"
- "-[PLConfigAgent volumeFreespace:]"
- "-[PLFSEventAgent logLogFileName:withName:]"
- "-[PLFSEventAgent startMonitoring]_block_invoke"
- "-[PLFSEventAgent startMonitoring]_block_invoke_2"
- "-[PLFSEventAgent stopMonitoring]"
- "-[PLHomeKitAgent logEventPointHomeKitEvents:]"
- "-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke"
- "-[PLIdentityServicesAgent initOperatorDependancies]_block_invoke_3"
- "-[PLIdentityServicesAgent initTaskOperatorDependancies]_block_invoke"
- "-[PLIdentityServicesAgent logCloudMessaging:]"
- "-[PLIdentityServicesAgent logIDSNetworkEntries:]"
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
- "-[PLMDNSAgent initOperatorDependancies]_block_invoke"
- "-[PLNetworkAgent initKernelEvent]"
- "-[PLNetworkAgent initKernelEvent]_block_invoke"
- "-[PLNetworkAgent logEventPointWake]"
- "-[PLPeripheralAgent initLid]_block_invoke"
- "-[PLPeripheralAgent logEventForwardDeviceState:]"
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
- "-[PLVideoAgent initOperatorDependancies]_block_invoke"
- "-[PLVideoAgent logEventBackwardVTSessionWithEntry:]"
- "-[PLVideoAgent logEventForwardVideoWithEntry:]"
- "-[PLWindowServerAgent installTimelineConnection]_block_invoke"
- "-[PLWindowServerAgent installTimelineConnection]_block_invoke_2"
- "-[PLWindowServerAgent logEventForwardTimelineInfo:withPID:withnewProcess:withSnapshotTimestamp:]"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLButtonAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLIOReportAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLIOReportAgentIOReportStats.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLMacCPUGPUAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLPeripheralAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLVideoAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLIdentityServicesAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLNetworkAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Networking/PLProcessNetworkAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLBluetoothAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLLocationAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Radios/PLWifiAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLApplicationAgentMac.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLConfigAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLFSEventAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLHomeKitAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLMDNSAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPerformanceAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPowerAssertionAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLPushAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScheduledWakeAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLWindowServerAgent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDebugService.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetService.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLDuetServiceDAS.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLTestService.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
- "4"
- "@24@0:8^{IOReportGroupChecks=BBB}16"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerLevel(207): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerLevel(207): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerReadLevel(453): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerReadLevel(453): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerWriteLevel(454): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: numOfThrottlingEntriesPerWriteLevel(454): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerLevel(865): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerLevel(865): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerReadLevel(866): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerReadLevel(866): Cannot add 16 elements to context"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerWriteLevel(867): (#16) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: timeOfThrottlingPerWriteLevel(867): Cannot add 16 elements to context"
- "ASPMSPParseBufferToCxt: DYCE1_Decoded_Bitflips(4165): Error adding 15 elements to context"
- "ASPMSPParseBufferToCxt: DYCE1_Decoded_Bitflips(4165): cfg 15 elements; (15*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: DYCE1_Target_Bitflips(4166): Error adding 20 elements to context"
- "ASPMSPParseBufferToCxt: DYCE1_Target_Bitflips(4166): cfg 20 elements; (20*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: DYCE2_Decoded_Bitflips(4167): Error adding 15 elements to context"
- "ASPMSPParseBufferToCxt: DYCE2_Decoded_Bitflips(4167): cfg 15 elements; (15*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: DYCE2_Target_Bitflips(4168): Error adding 20 elements to context"
- "ASPMSPParseBufferToCxt: DYCE2_Target_Bitflips(4168): cfg 20 elements; (20*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: FS1decodedbitflips(4134): Error adding 11 elements to context"
- "ASPMSPParseBufferToCxt: FS1decodedbitflips(4134): cfg 11 elements; (11*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: FS2decodedBitFlips(4120): Error adding 11 elements to context"
- "ASPMSPParseBufferToCxt: FS2decodedBitFlips(4120): cfg 11 elements; (11*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: active_time_bw_pg_acc(16387): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: active_time_bw_pg_acc(16387): cfg 1 elements; (1*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: active_time_bw_pg_hist(8237): Error adding 10 elements to context"
- "ASPMSPParseBufferToCxt: active_time_bw_pg_hist(8237): cfg 10 elements; (10*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: active_time_bw_pg_max(8239): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: active_time_bw_pg_max(8239): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: active_time_bw_pg_min(8238): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: active_time_bw_pg_min(8238): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: active_time_hist(8214): Error adding 5 elements to context"
- "ASPMSPParseBufferToCxt: active_time_hist(8214): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: active_time_hist(8224): Error adding 8 elements to context"
- "ASPMSPParseBufferToCxt: active_time_hist(8224): cfg 8 elements; (8*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: algo_queue_depth(16389): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: algo_queue_depth(16389): cfg 16 elements; (16*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: auto_skip(8217): Error adding 5 elements to context"
- "ASPMSPParseBufferToCxt: auto_skip(8217): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToEOL_LSB(4111): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToEOL_LSB(4111): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToEOL_MSB(4112): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToEOL_MSB(4112): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToEOL_QSB(4162): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToEOL_QSB(4162): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToEOL_USB(4113): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToEOL_USB(4113): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToSOL_LSB(4114): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToSOL_LSB(4114): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToSOL_MSB(4115): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToSOL_MSB(4115): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToSOL_QSB(4163): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToSOL_QSB(4163): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToSOL_USB(4116): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: bdbDynamicMovedToSOL_USB(4116): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: boot_time_low_power(8236): Error adding 7 elements to context"
- "ASPMSPParseBufferToCxt: boot_time_low_power(8236): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: boot_time_normal_power(8235): Error adding 7 elements to context"
- "ASPMSPParseBufferToCxt: boot_time_normal_power(8235): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: channel_halt_latency_hist(16392): Error adding 6 elements to context"
- "ASPMSPParseBufferToCxt: channel_halt_latency_hist(16392): cfg 6 elements; (6*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: channel_halt_max_latency(8256): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: channel_halt_max_latency(8256): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: deepSoft1Decoded(4127): Error adding 10 elements to context"
- "ASPMSPParseBufferToCxt: deepSoft1Decoded(4127): cfg 10 elements; (10*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: e2e_error_count_tmode(8246): Error adding 5 elements to context"
- "ASPMSPParseBufferToCxt: e2e_error_count_tmode(8246): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: extended_rd_window_diff_dist(8248): Error adding 9 elements to context"
- "ASPMSPParseBufferToCxt: extended_rd_window_diff_dist(8248): cfg 9 elements; (9*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: external_etags_usage_hist(8227): Error adding 7 elements to context"
- "ASPMSPParseBufferToCxt: external_etags_usage_hist(8227): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: gps_max_num_of_failures(8222): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: gps_max_num_of_failures(8222): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: gps_num_of_failures_max_overflow(8223): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: gps_num_of_failures_max_overflow(8223): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: higher_die_temperature(8232): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: higher_die_temperature(8232): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: internal_etags_usage_hist(8228): Error adding 4 elements to context"
- "ASPMSPParseBufferToCxt: internal_etags_usage_hist(8228): cfg 4 elements; (4*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: lower_die_temperature(8231): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: lower_die_temperature(8231): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: max_heap_usage(8229): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: max_heap_usage(8229): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: max_heap_usage_v2(8257): Error adding 2 elements to context"
- "ASPMSPParseBufferToCxt: max_heap_usage_v2(8257): cfg 2 elements; (2*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: max_size_open_blocks_list(8221): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: max_size_open_blocks_list(8221): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: mdll_relative_offset(8240): Error adding 5 elements to context"
- "ASPMSPParseBufferToCxt: mdll_relative_offset(8240): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: numOfSensesWereSentDuringMiniAcq(4139): Error adding 3 elements to context"
- "ASPMSPParseBufferToCxt: numOfSensesWereSentDuringMiniAcq(4139): cfg 3 elements; (3*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: numOfSensesWereSentDuringSyndSumAcq(4138): Error adding 5 elements to context"
- "ASPMSPParseBufferToCxt: numOfSensesWereSentDuringSyndSumAcq(4138): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: numOfSlipTracking(4161): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: numOfSlipTracking(4161): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: num_auto_program_cache_terminations(8225): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: num_auto_program_cache_terminations(8225): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: num_idle_die_read_cache_terminate(16393): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: num_idle_die_read_cache_terminate(16393): cfg 1 elements; (1*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: num_pg_events(16388): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: num_pg_events(16388): cfg 1 elements; (1*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: num_pg_regrets(8241): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: num_pg_regrets(8241): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: number_gracefull_read_terminations(16386): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: number_gracefull_read_terminations(16386): cfg 1 elements; (1*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: number_of_dcc_pass_after_retry(8218): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: number_of_dcc_pass_after_retry(8218): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: number_of_read_cache_auto_terminations(8226): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: number_of_read_cache_auto_terminations(8226): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: open_blocks_hist(8212): Error adding 4 elements to context"
- "ASPMSPParseBufferToCxt: open_blocks_hist(8212): cfg 4 elements; (4*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: open_blocks_hist(8220): Error adding 7 elements to context"
- "ASPMSPParseBufferToCxt: open_blocks_hist(8220): cfg 7 elements; (7*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: parallel_slip_drops_hist(8253): Error adding 4 elements to context"
- "ASPMSPParseBufferToCxt: parallel_slip_drops_hist(8253): cfg 4 elements; (4*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: parallel_slip_hist(16390): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: parallel_slip_hist(16390): cfg 16 elements; (16*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: passWithTmodeHard(4096): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: passWithTmodeHard(4096): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: passWithTmodeHard_fast(4099): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: passWithTmodeHard_fast(4099): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: random_read_hit_ratio_hist(8213): Error adding 6 elements to context"
- "ASPMSPParseBufferToCxt: random_read_hit_ratio_hist(8213): cfg 6 elements; (6*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: random_read_hit_ratio_hist(8233): Error adding 6 elements to context"
- "ASPMSPParseBufferToCxt: random_read_hit_ratio_hist(8233): cfg 6 elements; (6*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: random_read_size_ratio(16385): Error adding 5 elements to context"
- "ASPMSPParseBufferToCxt: random_read_size_ratio(16385): cfg 5 elements; (5*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: rd_retraining_failures(8215): Error adding 2 elements to context"
- "ASPMSPParseBufferToCxt: rd_retraining_failures(8215): cfg 2 elements; (2*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: rd_retraining_failures_v2(8249): Error adding 2 elements to context"
- "ASPMSPParseBufferToCxt: rd_retraining_failures_v2(8249): cfg 2 elements; (2*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: rd_window_dist(8247): Error adding 9 elements to context"
- "ASPMSPParseBufferToCxt: rd_window_dist(8247): cfg 9 elements; (9*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: rd_window_dist_single_die(8252): Error adding 9 elements to context"
- "ASPMSPParseBufferToCxt: rd_window_dist_single_die(8252): cfg 9 elements; (9*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassWithFS2_4b(4148): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassWithFS2_4b(4148): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassWithFS2_4b_fast(4122): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassWithFS2_4b_fast(4122): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughDS1(4151): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughDS1(4151): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughDS1_DSP(4160): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughDS1_DSP(4160): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughDS2(4152): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughDS2(4152): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughFS2_2b(4149): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughFS2_2b(4149): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughFS2_2b_fast(4129): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughFS2_2b_fast(4129): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughFS2_4b(4147): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughFS2_4b(4147): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughFS2_4b_fast(4130): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughFS2_4b_fast(4130): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughSyndSumAcquisition_DSP(4157): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readAlgoPassedThroughSyndSumAcquisition_DSP(4157): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readalgoPassWithDS1(4106): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readalgoPassWithDS1(4106): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readalgoPassWithDS1_DSP(4143): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readalgoPassWithDS1_DSP(4143): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readalgoPassWithDS2(4108): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readalgoPassWithDS2(4108): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readalgoPassWithDYCE1(4107): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readalgoPassWithDYCE1(4107): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readalgoPassWithDYCE1_DSP(4144): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readalgoPassWithDYCE1_DSP(4144): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readalgoPassWithDYCE2(4109): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readalgoPassWithDYCE2(4109): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readalgoPassWithEXH(4133): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readalgoPassWithEXH(4133): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: readalgoPassWithEXH_DSP(4142): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: readalgoPassWithEXH_DSP(4142): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: rom_num_hard_resets(8230): Error adding 6 elements to context"
- "ASPMSPParseBufferToCxt: rom_num_hard_resets(8230): cfg 6 elements; (6*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: slipTrackingAfterFs1ForceFailChangedVthInTicksHist(4121): Error adding 4 elements to context"
- "ASPMSPParseBufferToCxt: slipTrackingAfterFs1ForceFailChangedVthInTicksHist(4121): cfg 4 elements; (4*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: spi_image_cw_fetch_duration_acc(8243): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: spi_image_cw_fetch_duration_acc(8243): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: spi_image_cw_fetch_duration_hist(8244): Error adding 5 elements to context"
- "ASPMSPParseBufferToCxt: spi_image_cw_fetch_duration_hist(8244): cfg 5 elements; (5*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: spi_image_overall_duration_acc(8242): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: spi_image_overall_duration_acc(8242): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: spi_num_uses(8245): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: spi_num_uses(8245): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: sys_halt_latency_hist(16391): Error adding 6 elements to context"
- "ASPMSPParseBufferToCxt: sys_halt_latency_hist(16391): cfg 6 elements; (6*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: sys_halt_max_latency(8254): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: sys_halt_max_latency(8254): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: sys_halt_max_latency_opcode(8255): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: sys_halt_max_latency_opcode(8255): cfg 1 elements; (1*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: wr_retraining_failures(8216): Error adding 2 elements to context"
- "ASPMSPParseBufferToCxt: wr_retraining_failures(8216): cfg 2 elements; (2*4) cfg bytes != (%d) buffer bytes"
- "ActiveFreq_F1"
- "ActiveFreq_F2"
- "ActiveFreq_lockout"
- "AppleBCMWLANBusInterfacePCIe"
- "AppleBCMWLANCore"
- "BaselineTrackingFreq_F1"
- "BaselineTrackingFreq_F2"
- "BaselineTrackingFreq_lockout"
- "Button action payload: %@"
- "Button action updated payload: %@"
- "Button::CaptureButtonAction"
- "CacheDepthVsThroughput"
- "CaptureButtonAction"
- "Captured at: %s\n"
- "Cloud Messaging callback: %@"
- "DYCE1_Decoded_Bitflips"
- "DYCE1_Target_Bitflips"
- "DYCE2_Decoded_Bitflips"
- "DYCE2_Target_Bitflips"
- "FS1decodedbitflips"
- "FS2decodedBitFlips"
- "FullPress"
- "Got callback for PLHomeKitAgent_EventPoint_HomeKitEvents: %@"
- "HalfPress"
- "HighLevelState_Active"
- "HighLevelState_Baseline"
- "IDS Incoming Push Received payload %@"
- "IDS Message callback recieved payload %@"
- "IDS Outgoing Push Sent payload %@"
- "InstantKeys"
- "Insufficient space allocated to copy string contents"
- "IsCoalesced"
- "L"
- "Local Message Topic callback: %@"
- "MLC"
- "MTPbuttoncapture"
- "O"
- "PLPushAgent:: apsdConnectedListener with payload=%@"
- "PLPushAgent:: receivedPushListener with payload=%@"
- "PLPushAgent:: sentKeepAliveListener with payload=%@"
- "PLPushAgent:: sentPushListener with payload=%@"
- "SMC Metrics: Unsupported key size %d for SMC key %@."
- "Stage Manager toggled: %@"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"PLXPCListenerOperatorComposition\",&,V_captureButtonActionListener"
- "TouchTimeInterval"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_captureButtonActionListener"
- "active_time_bw_pg_acc"
- "active_time_bw_pg_hist"
- "active_time_bw_pg_max"
- "active_time_bw_pg_min"
- "active_time_hist"
- "algo_queue_depth"
- "auto_skip"
- "balanceProportionBucketsHistogramTlc"
- "bandKill_formatUserExcessive"
- "band_rbo_allocated"
- "bdbDynamicMovedToEOL_LSB"
- "bdbDynamicMovedToEOL_MSB"
- "bdbDynamicMovedToEOL_QSB"
- "bdbDynamicMovedToEOL_USB"
- "bdbDynamicMovedToSOL_LSB"
- "bdbDynamicMovedToSOL_MSB"
- "bdbDynamicMovedToSOL_QSB"
- "bdbDynamicMovedToSOL_USB"
- "boot_time_low_power"
- "boot_time_normal_power"
- "captureButtonActionListener"
- "channel_halt_latency_hist"
- "channel_halt_max_latency"
- "client status XPC with payload=%@"
- "deepSoft1Decoded"
- "dmFlatten"
- "e2e_error_count_tmode"
- "entryEventBackwardDefinitionMTPCaptureButton"
- "extended_rd_window_diff_dist"
- "external_etags_usage_hist"
- "fallbackToWaterfallValidity"
- "gcPDusterSrcFound"
- "gcPDusterSrcInvalidatedByGC"
- "gcPDusterSrcRemoved"
- "getJetamPriority:"
- "gps_max_num_of_failures"
- "gps_num_of_failures_max_overflow"
- "internal_etags_usage_hist"
- "invalid Collection: less than 'count' elements in collection"
- "isNonUDMMac"
- "log level changed with payload=%@"
- "logEventBackwardCaptureButtonAction:"
- "max_heap_usage"
- "max_heap_usage_v2"
- "max_size_open_blocks_list"
- "mdll_relative_offset"
- "network"
- "numOfSensesWereSentDuringMiniAcq"
- "numOfSensesWereSentDuringSyndSumAcq"
- "numOfSlipTracking"
- "num_auto_program_cache_terminations"
- "num_idle_die_read_cache_terminate"
- "num_pg_events"
- "num_pg_regrets"
- "number_gracefull_read_terminations"
- "number_of_dcc_pass_after_retry"
- "number_of_read_cache_auto_terminations"
- "offlineDieCnt"
- "open_blocks_hist"
- "parallel_slip_drops_hist"
- "parallel_slip_hist"
- "passWithTmodeHard"
- "passWithTmodeHard_fast"
- "random_read_hit_ratio_hist"
- "random_read_size_ratio"
- "rd_retraining_failures"
- "rd_retraining_failures_v2"
- "rd_window_dist"
- "rd_window_dist_single_die"
- "readAlgoPassWithFS2_4b"
- "readAlgoPassWithFS2_4b_fast"
- "readAlgoPassedThroughDS1"
- "readAlgoPassedThroughDS1_DSP"
- "readAlgoPassedThroughDS2"
- "readAlgoPassedThroughFS2_2b"
- "readAlgoPassedThroughFS2_2b_fast"
- "readAlgoPassedThroughFS2_4b"
- "readAlgoPassedThroughFS2_4b_fast"
- "readAlgoPassedThroughSyndSumAcquisition_DSP"
- "readalgoPassWithDS1"
- "readalgoPassWithDS1_DSP"
- "readalgoPassWithDS2"
- "readalgoPassWithDYCE1"
- "readalgoPassWithDYCE1_DSP"
- "readalgoPassWithDYCE2"
- "readalgoPassWithEXH"
- "readalgoPassWithEXH_DSP"
- "rom_num_hard_resets"
- "self.gameMode %d"
- "setCaptureButtonActionListener:"
- "slipTrackingAfterFs1ForceFailChangedVthInTicksHist"
- "spi_image_cw_fetch_duration_acc"
- "spi_image_cw_fetch_duration_hist"
- "spi_image_overall_duration_acc"
- "spi_num_uses"
- "status bar changed with payload=%@"
- "sys_halt_latency_hist"
- "sys_halt_max_latency"
- "sys_halt_max_latency_opcode"
- "wr_retraining_failures"
- "{IOReportGroupChecks=BBB}16@0:8"

```
