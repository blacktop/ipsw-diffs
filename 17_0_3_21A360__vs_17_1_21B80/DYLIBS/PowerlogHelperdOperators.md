## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-1775.2.1.0.0
-  __TEXT.__text: 0x1b6ba8
-  __TEXT.__auth_stubs: 0x1c90
-  __TEXT.__objc_methlist: 0xcdec
+1787.40.67.0.0
+  __TEXT.__text: 0x1ba0f4
+  __TEXT.__auth_stubs: 0x1cc0
+  __TEXT.__objc_methlist: 0xcefc
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x21981
-  __TEXT.__oslogstring: 0xfc7f
-  __TEXT.__gcc_except_tab: 0x1d74
+  __TEXT.__cstring: 0x22036
+  __TEXT.__oslogstring: 0xfed5
+  __TEXT.__gcc_except_tab: 0x1d80
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3364
-  __TEXT.__objc_classname: 0xadc
-  __TEXT.__objc_methname: 0x2c364
-  __TEXT.__objc_methtype: 0x256b
-  __TEXT.__objc_stubs: 0x1b160
+  __TEXT.__unwind_info: 0x3394
+  __TEXT.__objc_classname: 0xada
+  __TEXT.__objc_methname: 0x2cab0
+  __TEXT.__objc_methtype: 0x2582
+  __TEXT.__objc_stubs: 0x1b980
   __DATA_CONST.__got: 0x6f0
-  __DATA_CONST.__const: 0x3ee8
+  __DATA_CONST.__const: 0x3f50
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_nlclslist: 0x110
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe7a0
-  __DATA_CONST.__objc_selrefs: 0x8548
-  __DATA_CONST.__objc_arraydata: 0x141f0
-  __AUTH_CONST.__cfstring: 0x2d220
+  __DATA_CONST.__objc_const: 0xe850
+  __DATA_CONST.__objc_selrefs: 0x8780
+  __DATA_CONST.__objc_arraydata: 0x14280
+  __AUTH_CONST.__cfstring: 0x2da00
   __AUTH_CONST.__objc_intobj: 0x2580
-  __AUTH_CONST.__objc_dictobj: 0x2d28
+  __AUTH_CONST.__objc_dictobj: 0x2dc8
   __AUTH_CONST.__objc_const: 0x26d0
   __AUTH_CONST.__const: 0x15c0
-  __AUTH_CONST.__objc_doubleobj: 0xab0
-  __AUTH_CONST.__objc_arrayobj: 0x2850
+  __AUTH_CONST.__objc_doubleobj: 0xac0
+  __AUTH_CONST.__objc_arrayobj: 0x2868
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xe60
+  __AUTH_CONST.__auth_got: 0xe78
   __AUTH.__objc_data: 0x820
   __AUTH.__data: 0x5a0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x6e8
+  __DATA.__objc_classrefs: 0x700
   __DATA.__objc_superrefs: 0x290
-  __DATA.__objc_ivar: 0x101c
+  __DATA.__objc_ivar: 0x1028
   __DATA.__data: 0x650
   __DATA.__bss: 0x2e00
   __DATA.__common: 0x68

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 7845
-  Symbols:   25734
-  CStrings:  14499
+  Functions: 7887
+  Symbols:   25911
+  CStrings:  14656
 
Symbols:
+ +[PLApplicationAgent entryEventForwardDefinitionMotionToWake]
+ +[PLLocationAgent entryEventForwardDefinitionSuppressionManagerClient]
+ +[PLLocationAgent entryEventForwardDefinitionViewObstructed]
+ +[PLUtilities markFileAsPurgeable:withUrgency:]
+ +[PLUtilities markFileAsPurgeable:withUrgency:].cold.1
+ +[PLUtilities numFilesAtPath:]
+ +[PLUtilities numFilesAtPath:].cold.1
+ +[PLUtilities shouldCreateQuarantine]
+ +[PLXPCAgent entryEventForwardDefinitionAirDropSession]
+ -[PLAppTimeService chunkAppsOnScreenAtDate:]
+ -[PLAppTimeService chunkAppsOnScreenAtDate:].cold.1
+ -[PLAppTimeService getWidgetParentAppForBundleID:].cold.2
+ -[PLApplicationAgent logEventForwardMotionToWake:]
+ -[PLApplicationAgent motionToWakeListener]
+ -[PLApplicationAgent setMotionToWakeListener:]
+ -[PLBatteryAgent customConvertBase34ToBase10:]
+ -[PLBatteryAgent customConvertBase34ToBase10:].cold.1
+ -[PLLocationAgent convertClientEvent:]
+ -[PLLocationAgent convertViewObstructedEvent:]
+ -[PLLocationAgent logEventForwardSuppressionManagerClient:]
+ -[PLLocationAgent logEventForwardViewObstructed:]
+ -[PLLocationAgent setSuppressionManagerClientListener:]
+ -[PLLocationAgent setViewObstructedListener:]
+ -[PLLocationAgent suppressionManagerClientListener]
+ -[PLLocationAgent viewObstructedListener]
+ -[PLPowerMetricMonitorService _convertToWattsFromMilliwatts:]
+ -[PLPowerMetricMonitorService _emitPowerSignpostWithMetric:value:]
+ -[PLPowerMetricMonitorService _emitPowerSignpostWithMetric:value:pid:]
+ -[PLPowerMetricMonitorService _parseSMCMetricsFromEntry:]
+ -[PLPowerMetricMonitorService _parseSMCMetricsFromEntry:].cold.1
+ -[PLPowerMetricMonitorService _parseWifiPowerMetricsFromEntry:cacheMetrics:]
+ -[PLPowerMetricMonitorService changeUpdateInterval:]
+ -[PLPowerMetricMonitorService setMetricCollectionTimerUpdateInterval:]
+ -[PLPowerMetricMonitorService setMetricCollectionTimerUpdateInterval:].cold.1
+ -[PLXPCAgent AirDropSessionXPCListener]
+ -[PLXPCAgent convertAirDropSessionState:]
+ -[PLXPCAgent convertAirDropSessionState:].cold.1
+ -[PLXPCAgent logEventForwardAirDropSession:]
+ -[PLXPCAgent setAirDropSessionXPCListener:]
+ GCC_except_table117
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table51
+ GCC_except_table68
+ GCC_except_table75
+ GCC_except_table87
+ _OBJC_CLASS_$_PPSMetricCollection
+ _OBJC_CLASS_$_PPSMetricSample
+ _OBJC_CLASS_$_PPSProcessMetricCollection
+ _OBJC_IVAR_$_PLApplicationAgent._motionToWakeListener
+ _OBJC_IVAR_$_PLLocationAgent._suppressionManagerClientListener
+ _OBJC_IVAR_$_PLLocationAgent._viewObstructedListener
+ _OBJC_IVAR_$_PLXPCAgent._AirDropSessionXPCListener
+ _OUTLINED_FUNCTION_21
+ _PLLogPowerSignpost
+ _PLLogPowerSignpost.log
+ _PLLogPowerSignpost.onceToken
+ ___22-[PLBatteryAgent init]_block_invoke.3159
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.1
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.10
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.2
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.3
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.4
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.5
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.6
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.7
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.8
+ ___22-[PLBatteryAgent init]_block_invoke.3159.cold.9
+ ___22-[PLBatteryAgent init]_block_invoke.3171
+ ___22-[PLBatteryAgent init]_block_invoke.3174
+ ___22-[PLBatteryAgent init]_block_invoke.3197
+ ___22-[PLBatteryAgent init]_block_invoke.3200
+ ___22-[PLBatteryAgent init]_block_invoke.3208
+ ___22-[PLBatteryAgent init]_block_invoke.3208.cold.1
+ ___22-[PLBatteryAgent init]_block_invoke.3208.cold.2
+ ___22-[PLBatteryAgent init]_block_invoke.3214
+ ___22-[PLBatteryAgent init]_block_invoke.3218
+ ___22-[PLBatteryAgent init]_block_invoke_2.3240
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4920
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4929
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4938
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4947
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4953
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4959
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4965
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4974
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4980
+ ___24-[PLBatteryAgent xFlags]_block_invoke.4986
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4829
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4835
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4841
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4847
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4852
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4860
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4866
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4872
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4878
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4884
+ ___30-[PLBatteryAgent gasGaugeRead]_block_invoke_2.4887
+ ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4548
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3343
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3349
+ ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3329
+ ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.4999
+ ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3680
+ ___38-[PLLocationAgent resyncActiveClients]_block_invoke.585
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1869
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1869.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1876
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1876.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1883
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1891
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1891.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1913
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1913.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1918
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1918.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1928
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1928.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1936
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1936.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1944
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1944.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1949
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1949.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1966
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1966.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1971
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1971.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1979
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1979.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1984
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1984.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1994
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1994.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2002
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2002.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2010
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2010.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2017
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2017.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2025
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2025.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2030
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2030.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2035
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2035.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2040
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2040.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2045
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2045.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2053
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2053.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2058
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2058.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2063
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2063.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2073
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2073.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2080
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2080.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2090
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2090.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2098
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2098.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2116
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2116.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2124
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2124.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2131
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2131.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2141
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2141.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2151
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2151.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2159
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2159.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2169
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2169.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2178
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2178.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2187
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2187.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2197
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2197.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2205
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2205.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2213
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2213.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2223
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2223.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2231
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2231.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2239
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2239.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2249
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2249.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2257
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2257.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2267
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2267.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2277
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2277.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2287
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2287.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2295
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2295.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2305
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2305.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2313
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2313.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2321
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2321.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2326
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2326.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2331
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2331.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2348
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2348.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2353
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2353.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2358
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2358.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2363
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2363.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2368
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2368.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2389
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2389.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2399
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2399.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2407
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2407.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2415
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2415.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2423
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2423.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2431
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2431.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2436
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2436.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2446
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2446.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2456
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2456.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2464
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2464.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2472
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2472.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2480
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2480.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2487
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2487.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2495
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2495.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2505
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2505.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2532
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2532.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2542
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2542.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2550
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2550.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2558
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2558.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2566
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2566.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2578
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2578.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2585
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2585.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2590
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2590.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2598
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2598.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2610
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2610.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2620
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2620.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2628
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2628.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2640
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2640.cold.1
+ ___39+[PLUtilities quarantineToPath:action:]_block_invoke
+ ___39+[PLUtilities quarantineToPath:action:]_block_invoke.cold.1
+ ___39+[PLUtilities quarantineToPath:action:]_block_invoke.cold.2
+ ___41-[PLApplicationAgent logInstalledPlugin:]_block_invoke.614
+ ___41-[PLApplicationAgent logInstalledPlugin:]_block_invoke.618
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.3948
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.3955
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.3951
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.3958
+ ___41-[PLBatteryGaugeService DTQueryResponse:]_block_invoke.229
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3421
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3427
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3427.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3443
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3475
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3535
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3535.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3535.cold.2
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3535.cold.3
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3552
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3552.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3563
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3567
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3575
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3575.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3582
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3591
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3597
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3604
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3604.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3611
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3611.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3630
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3630.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3637
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3660
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3428
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3473
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3487
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3559
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3576
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3586
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3594
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3605
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3612
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3664
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5107
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5107.cold.1
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5107.cold.2
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5115
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5109
+ ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.3831
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1732
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1732.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1752
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1752.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1757
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1757.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1767
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1767.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1801
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1801.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1811
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1811.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1818
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1818.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1825
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1825.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1835
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1835.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1843
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1843.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1850
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1850.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.382
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.382.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.397
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.397.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.406
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.406.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.432
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.432.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.438
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.438.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.448
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.448.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.448.cold.2
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.455
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.460
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.460.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.480
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.480.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.490
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.490.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.495
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.495.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.503
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.503.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.511
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.511.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.519
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.519.cold.1
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.383
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.398
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.407
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.421
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.433
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.440
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.449
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.461
+ ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.564
+ ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.570
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.527
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.527.cold.1
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.533
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.541
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.547
+ ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.553
+ ___45-[PLBatteryAgent gasGaugeOpenAndStartLogging]_block_invoke.4820
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5143
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5144
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5145
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5146
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5147
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5147.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5148
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5148.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5149
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5149.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5190
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.625
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.635
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.641
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.647
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.653
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.660
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.666
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.672
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.678
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.684
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.685
+ ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.688
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.361
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.361.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.373
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.387
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.417
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.417.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.423
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.423.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.428
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.428.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.435
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.435.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.442
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.442.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.447
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.447.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.457
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.457.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.464
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.464.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.469
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.469.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.477
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.477.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.485
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.485.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.497
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.510
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.510.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.522
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.522.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.362
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.375
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.388
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.487
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.487.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.487.cold.2
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.511
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.523
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_3.384
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_3.391
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_3.488
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_4.386
+ ___46-[PLApplicationAgent refreshAllAppsAndPlugins]_block_invoke.553
+ ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke.330
+ ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke_2.338
+ ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke_3.346
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5132
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5133
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5137
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5137.cold.1
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5137.cold.2
+ ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.752
+ ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.762
+ ___52-[PLPowerMetricMonitorService changeUpdateInterval:]_block_invoke
+ ___52-[PLPowerMetricMonitorService changeUpdateInterval:]_block_invoke.cold.1
+ ___54-[PLBatteryAgent showOrHideTLCNotification:timeInTLC:]_block_invoke.3281
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4783
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4783.cold.1
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4787
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4787.cold.1
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4792
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4796
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4788
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4793
+ ___56-[PLApplicationAgent createWidgetStatsAccountingEvents:]_block_invoke.566
+ ___56-[PLLocationAgent logEventForwardTechStatus_withLimiter]_block_invoke.561
+ ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.595
+ ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.601
+ ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.607
+ ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3309
+ ___61-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:]_block_invoke.607
+ ___61-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:]_block_invoke.608
+ ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.149
+ ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4211
+ ___73-[PLLocationAgent closeOpenEntryForClient:withOpenEntry:withTimeStopped:]_block_invoke.617
+ ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.148
+ ___PLLogPowerSignpost_block_invoke
+ ___block_descriptor_41_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_literal_global.2100
+ ___block_literal_global.2630
+ ___block_literal_global.3146
+ ___block_literal_global.3255
+ ___block_literal_global.3268
+ ___block_literal_global.3283
+ ___block_literal_global.3334
+ ___block_literal_global.335
+ ___block_literal_global.3389
+ ___block_literal_global.3446
+ ___block_literal_global.3489
+ ___block_literal_global.3498
+ ___block_literal_global.3507
+ ___block_literal_global.3519
+ ___block_literal_global.355
+ ___block_literal_global.361
+ ___block_literal_global.363
+ ___block_literal_global.3632
+ ___block_literal_global.3666
+ ___block_literal_global.3679
+ ___block_literal_global.368
+ ___block_literal_global.373
+ ___block_literal_global.375
+ ___block_literal_global.377
+ ___block_literal_global.381
+ ___block_literal_global.384
+ ___block_literal_global.387
+ ___block_literal_global.390
+ ___block_literal_global.393
+ ___block_literal_global.398
+ ___block_literal_global.401
+ ___block_literal_global.403
+ ___block_literal_global.412
+ ___block_literal_global.420
+ ___block_literal_global.4263
+ ___block_literal_global.429
+ ___block_literal_global.4504
+ ___block_literal_global.4516
+ ___block_literal_global.4566
+ ___block_literal_global.469
+ ___block_literal_global.5081
+ ___block_literal_global.5142
+ ___block_literal_global.807
+ ___block_literal_global.82
+ __unnamed_array_storage.1721
+ __unnamed_array_storage.1722
+ __unnamed_array_storage.1729
+ __unnamed_array_storage.173
+ __unnamed_array_storage.1749
+ __unnamed_array_storage.1750
+ __unnamed_array_storage.1755
+ __unnamed_array_storage.1764
+ __unnamed_array_storage.1765
+ __unnamed_array_storage.1798
+ __unnamed_array_storage.1799
+ __unnamed_array_storage.1808
+ __unnamed_array_storage.1809
+ __unnamed_array_storage.1815
+ __unnamed_array_storage.1816
+ __unnamed_array_storage.1822
+ __unnamed_array_storage.1823
+ __unnamed_array_storage.1832
+ __unnamed_array_storage.1840
+ __unnamed_array_storage.1841
+ __unnamed_array_storage.1847
+ __unnamed_array_storage.1848
+ __unnamed_array_storage.1866
+ __unnamed_array_storage.1867
+ __unnamed_array_storage.1873
+ __unnamed_array_storage.1874
+ __unnamed_array_storage.1880
+ __unnamed_array_storage.1881
+ __unnamed_array_storage.1889
+ __unnamed_array_storage.1910
+ __unnamed_array_storage.1911
+ __unnamed_array_storage.1916
+ __unnamed_array_storage.1925
+ __unnamed_array_storage.1926
+ __unnamed_array_storage.1942
+ __unnamed_array_storage.1946
+ __unnamed_array_storage.1947
+ __unnamed_array_storage.1963
+ __unnamed_array_storage.1968
+ __unnamed_array_storage.1977
+ __unnamed_array_storage.1981
+ __unnamed_array_storage.1992
+ __unnamed_array_storage.1999
+ __unnamed_array_storage.2000
+ __unnamed_array_storage.2007
+ __unnamed_array_storage.2008
+ __unnamed_array_storage.2014
+ __unnamed_array_storage.2022
+ __unnamed_array_storage.2027
+ __unnamed_array_storage.2028
+ __unnamed_array_storage.2032
+ __unnamed_array_storage.2037
+ __unnamed_array_storage.2042
+ __unnamed_array_storage.2050
+ __unnamed_array_storage.2051
+ __unnamed_array_storage.2055
+ __unnamed_array_storage.2056
+ __unnamed_array_storage.2060
+ __unnamed_array_storage.2061
+ __unnamed_array_storage.2077
+ __unnamed_array_storage.2078
+ __unnamed_array_storage.2087
+ __unnamed_array_storage.2088
+ __unnamed_array_storage.2095
+ __unnamed_array_storage.2096
+ __unnamed_array_storage.2113
+ __unnamed_array_storage.2114
+ __unnamed_array_storage.2121
+ __unnamed_array_storage.2122
+ __unnamed_array_storage.2128
+ __unnamed_array_storage.2129
+ __unnamed_array_storage.2138
+ __unnamed_array_storage.2139
+ __unnamed_array_storage.2148
+ __unnamed_array_storage.2149
+ __unnamed_array_storage.2156
+ __unnamed_array_storage.2157
+ __unnamed_array_storage.2166
+ __unnamed_array_storage.2167
+ __unnamed_array_storage.2175
+ __unnamed_array_storage.2176
+ __unnamed_array_storage.2184
+ __unnamed_array_storage.2185
+ __unnamed_array_storage.2194
+ __unnamed_array_storage.2195
+ __unnamed_array_storage.2202
+ __unnamed_array_storage.2203
+ __unnamed_array_storage.2210
+ __unnamed_array_storage.2211
+ __unnamed_array_storage.2212
+ __unnamed_array_storage.2220
+ __unnamed_array_storage.2221
+ __unnamed_array_storage.2229
+ __unnamed_array_storage.2236
+ __unnamed_array_storage.2247
+ __unnamed_array_storage.2254
+ __unnamed_array_storage.2265
+ __unnamed_array_storage.2274
+ __unnamed_array_storage.2275
+ __unnamed_array_storage.2284
+ __unnamed_array_storage.2285
+ __unnamed_array_storage.2292
+ __unnamed_array_storage.2293
+ __unnamed_array_storage.2302
+ __unnamed_array_storage.2303
+ __unnamed_array_storage.2310
+ __unnamed_array_storage.2318
+ __unnamed_array_storage.2319
+ __unnamed_array_storage.2323
+ __unnamed_array_storage.2324
+ __unnamed_array_storage.2328
+ __unnamed_array_storage.2329
+ __unnamed_array_storage.2346
+ __unnamed_array_storage.2350
+ __unnamed_array_storage.2354
+ __unnamed_array_storage.2355
+ __unnamed_array_storage.2360
+ __unnamed_array_storage.2361
+ __unnamed_array_storage.2365
+ __unnamed_array_storage.2366
+ __unnamed_array_storage.2373
+ __unnamed_array_storage.2374
+ __unnamed_array_storage.2378
+ __unnamed_array_storage.2390
+ __unnamed_array_storage.2393
+ __unnamed_array_storage.2397
+ __unnamed_array_storage.2399
+ __unnamed_array_storage.2402
+ __unnamed_array_storage.2405
+ __unnamed_array_storage.2413
+ __unnamed_array_storage.2414
+ __unnamed_array_storage.2420
+ __unnamed_array_storage.2421
+ __unnamed_array_storage.2423
+ __unnamed_array_storage.2428
+ __unnamed_array_storage.2429
+ __unnamed_array_storage.2432
+ __unnamed_array_storage.2433
+ __unnamed_array_storage.2434
+ __unnamed_array_storage.2435
+ __unnamed_array_storage.2438
+ __unnamed_array_storage.2441
+ __unnamed_array_storage.2443
+ __unnamed_array_storage.2447
+ __unnamed_array_storage.2450
+ __unnamed_array_storage.2454
+ __unnamed_array_storage.2456
+ __unnamed_array_storage.2462
+ __unnamed_array_storage.2469
+ __unnamed_array_storage.2470
+ __unnamed_array_storage.2477
+ __unnamed_array_storage.2478
+ __unnamed_array_storage.2484
+ __unnamed_array_storage.2492
+ __unnamed_array_storage.2493
+ __unnamed_array_storage.2502
+ __unnamed_array_storage.2503
+ __unnamed_array_storage.2519
+ __unnamed_array_storage.2525
+ __unnamed_array_storage.2529
+ __unnamed_array_storage.2540
+ __unnamed_array_storage.2548
+ __unnamed_array_storage.2555
+ __unnamed_array_storage.2556
+ __unnamed_array_storage.2557
+ __unnamed_array_storage.2560
+ __unnamed_array_storage.2563
+ __unnamed_array_storage.2569
+ __unnamed_array_storage.2575
+ __unnamed_array_storage.2576
+ __unnamed_array_storage.2587
+ __unnamed_array_storage.2588
+ __unnamed_array_storage.2595
+ __unnamed_array_storage.2596
+ __unnamed_array_storage.2599
+ __unnamed_array_storage.2605
+ __unnamed_array_storage.2607
+ __unnamed_array_storage.2611
+ __unnamed_array_storage.2617
+ __unnamed_array_storage.2625
+ __unnamed_array_storage.2626
+ __unnamed_array_storage.2632
+ __unnamed_array_storage.2637
+ __unnamed_array_storage.2638
+ __unnamed_array_storage.2663
+ __unnamed_array_storage.2664
+ __unnamed_array_storage.2669
+ __unnamed_array_storage.2702
+ __unnamed_array_storage.2708
+ __unnamed_array_storage.2717
+ __unnamed_array_storage.2732
+ __unnamed_array_storage.2738
+ __unnamed_array_storage.2771
+ __unnamed_array_storage.2780
+ __unnamed_array_storage.2789
+ __unnamed_array_storage.2798
+ __unnamed_array_storage.2807
+ __unnamed_array_storage.2816
+ __unnamed_array_storage.2825
+ __unnamed_array_storage.2834
+ __unnamed_array_storage.2840
+ __unnamed_array_storage.2846
+ __unnamed_array_storage.2852
+ __unnamed_array_storage.2858
+ __unnamed_array_storage.2867
+ __unnamed_array_storage.2876
+ __unnamed_array_storage.2885
+ __unnamed_array_storage.2894
+ __unnamed_array_storage.290
+ __unnamed_array_storage.2900
+ __unnamed_array_storage.2906
+ __unnamed_array_storage.291
+ __unnamed_array_storage.2912
+ __unnamed_array_storage.2913
+ __unnamed_array_storage.2915
+ __unnamed_array_storage.2924
+ __unnamed_array_storage.2931
+ __unnamed_array_storage.2932
+ __unnamed_array_storage.2933
+ __unnamed_array_storage.2942
+ __unnamed_array_storage.2957
+ __unnamed_array_storage.297
+ __unnamed_array_storage.305
+ __unnamed_array_storage.3128
+ __unnamed_array_storage.3129
+ __unnamed_array_storage.316
+ __unnamed_array_storage.3180
+ __unnamed_array_storage.327
+ __unnamed_array_storage.3275
+ __unnamed_array_storage.3276
+ __unnamed_array_storage.3288
+ __unnamed_array_storage.3289
+ __unnamed_array_storage.336
+ __unnamed_array_storage.3362
+ __unnamed_array_storage.337
+ __unnamed_array_storage.3394
+ __unnamed_array_storage.3395
+ __unnamed_array_storage.344
+ __unnamed_array_storage.3440
+ __unnamed_array_storage.3441
+ __unnamed_array_storage.3470
+ __unnamed_array_storage.3471
+ __unnamed_array_storage.3484
+ __unnamed_array_storage.3485
+ __unnamed_array_storage.3494
+ __unnamed_array_storage.3495
+ __unnamed_array_storage.3503
+ __unnamed_array_storage.3504
+ __unnamed_array_storage.3515
+ __unnamed_array_storage.3516
+ __unnamed_array_storage.3532
+ __unnamed_array_storage.3533
+ __unnamed_array_storage.3572
+ __unnamed_array_storage.3573
+ __unnamed_array_storage.3622
+ __unnamed_array_storage.3623
+ __unnamed_array_storage.3657
+ __unnamed_array_storage.3658
+ __unnamed_array_storage.367
+ __unnamed_array_storage.368
+ __unnamed_array_storage.394
+ __unnamed_array_storage.398
+ __unnamed_array_storage.4002
+ __unnamed_array_storage.403
+ __unnamed_array_storage.404
+ __unnamed_array_storage.4041
+ __unnamed_array_storage.4119
+ __unnamed_array_storage.415
+ __unnamed_array_storage.4197
+ __unnamed_array_storage.420
+ __unnamed_array_storage.421
+ __unnamed_array_storage.425
+ __unnamed_array_storage.426
+ __unnamed_array_storage.4312
+ __unnamed_array_storage.445
+ __unnamed_array_storage.4498
+ __unnamed_array_storage.454
+ __unnamed_array_storage.455
+ __unnamed_array_storage.461
+ __unnamed_array_storage.462
+ __unnamed_array_storage.466
+ __unnamed_array_storage.467
+ __unnamed_array_storage.477
+ __unnamed_array_storage.478
+ __unnamed_array_storage.492
+ __unnamed_array_storage.493
+ __unnamed_array_storage.500
+ __unnamed_array_storage.501
+ __unnamed_array_storage.5034
+ __unnamed_array_storage.5035
+ __unnamed_array_storage.5041
+ __unnamed_array_storage.5042
+ __unnamed_array_storage.507
+ __unnamed_array_storage.5101
+ __unnamed_array_storage.5102
+ __unnamed_array_storage.5123
+ __unnamed_array_storage.5124
+ __unnamed_array_storage.516
+ __unnamed_array_storage.517
+ __unnamed_array_storage.519
+ __unnamed_array_storage.520
+ __unnamed_array_storage.711
+ __unnamed_array_storage.80
+ __unnamed_array_storage.805
+ _cancelEALogging.classDebugEnabled.3328
+ _cancelEALogging.defaultOnce.3327
+ _close
+ _ffsctl
+ _gasGaugeOpenAndStartLogging.classDebugEnabled.4819
+ _gasGaugeOpenAndStartLogging.defaultOnce.4818
+ _gasGaugeRead.classDebugEnabled.4828
+ _gasGaugeRead.classDebugEnabled.4834
+ _gasGaugeRead.classDebugEnabled.4840
+ _gasGaugeRead.classDebugEnabled.4846
+ _gasGaugeRead.classDebugEnabled.4854
+ _gasGaugeRead.classDebugEnabled.4859
+ _gasGaugeRead.classDebugEnabled.4865
+ _gasGaugeRead.classDebugEnabled.4871
+ _gasGaugeRead.classDebugEnabled.4877
+ _gasGaugeRead.classDebugEnabled.4886
+ _gasGaugeRead.defaultOnce.4827
+ _gasGaugeRead.defaultOnce.4833
+ _gasGaugeRead.defaultOnce.4839
+ _gasGaugeRead.defaultOnce.4845
+ _gasGaugeRead.defaultOnce.4851
+ _gasGaugeRead.defaultOnce.4853
+ _gasGaugeRead.defaultOnce.4858
+ _gasGaugeRead.defaultOnce.4864
+ _gasGaugeRead.defaultOnce.4870
+ _gasGaugeRead.defaultOnce.4876
+ _gasGaugeRead.defaultOnce.4882
+ _gasGaugeRead.defaultOnce.4885
+ _gasGaugeRead.objectForKey.4883
+ _getIOPSDevices.classDebugEnabled.3342
+ _getIOPSDevices.classDebugEnabled.3348
+ _getIOPSDevices.defaultOnce.3341
+ _getIOPSDevices.defaultOnce.3347
+ _handlePPMCallback.defaultOnce.3670
+ _initOperatorDependancies.classDebugEnabled.3585
+ _initOperatorDependancies.classDebugEnabled.3593
+ _initOperatorDependancies.classDebugEnabled.3596
+ _initOperatorDependancies.defaultOnce.3584
+ _initOperatorDependancies.defaultOnce.3592
+ _initOperatorDependancies.defaultOnce.3595
+ _kPLApplicationAgentEventForwardNameHomeScreenPresentation_block_invoke_3.classDebugEnabled.496
+ _kPLApplicationAgentEventForwardNameHomeScreenPresentation_block_invoke_3.defaultOnce.495
+ _kPLApplicationAgentEventForwardNameMotionToWake
+ _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3199
+ _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3213
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3161
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3195
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3198
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3212
+ _kPLBatteryAgentStringUserType_block_invoke.objectForKey.3196
+ _kPLBatteryAgentStringUserType_block_invoke_12.classDebugEnabled.5114
+ _kPLBatteryAgentStringUserType_block_invoke_12.defaultOnce.5113
+ _kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3420
+ _kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3419
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.classDebugEnabled.532
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.defaultOnce.531
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.624
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.634
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.640
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.646
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.652
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.659
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.665
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.671
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.677
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.683
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.623
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.633
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.639
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.645
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.651
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.658
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.664
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.670
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.676
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.682
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.classDebugEnabled.454
+ _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.defaultOnce.453
+ _kPLLocationAgentEventForwardNameSuppressionManagerClient
+ _kPLLocationAgentEventForwardNameViewObstructed
+ _kPLLocationAgentEventForwardSuppressionManagerClientEventKey
+ _kPLLocationAgentEventForwardSuppressionManagerClientNumbersKey
+ _kPLLocationAgentEventForwardSuppressionManagerClientTypeKey
+ _kPLLocationAgentEventForwardViewObstructedVOEventKey
+ _kPLXPCAgentEventForwardNameAirDropSession
+ _logEventBackwardHeatMap.classDebugEnabled.3950
+ _logEventBackwardHeatMap.classDebugEnabled.3957
+ _logEventBackwardHeatMap.defaultOnce.3949
+ _logEventBackwardHeatMap.defaultOnce.3956
+ _logEventForwardClientStatuswithPayload:.classDebugEnabled.594
+ _logEventForwardClientStatuswithPayload:.classDebugEnabled.600
+ _logEventForwardClientStatuswithPayload:.classDebugEnabled.606
+ _logEventForwardClientStatuswithPayload:.defaultOnce.593
+ _logEventForwardClientStatuswithPayload:.defaultOnce.599
+ _logEventForwardClientStatuswithPayload:.defaultOnce.605
+ _logEventForwardTechStatus.classDebugEnabled.563
+ _logEventForwardTechStatus.classDebugEnabled.569
+ _logEventForwardTechStatus.defaultOnce.562
+ _logEventForwardTechStatus.defaultOnce.568
+ _logEventIntervalGasGauge.classDebugEnabled.3830
+ _logEventIntervalGasGauge.defaultOnce.3829
+ _logEventNoneBatteryConfigWithRawData:.classDebugEnabled.4795
+ _logEventNoneBatteryConfigWithRawData:.defaultOnce.4794
+ _logEventPointClientStatus.classDebugEnabled.540
+ _logEventPointClientStatus.classDebugEnabled.546
+ _logEventPointClientStatus.classDebugEnabled.552
+ _logEventPointClientStatus.defaultOnce.539
+ _logEventPointClientStatus.defaultOnce.545
+ _logEventPointClientStatus.defaultOnce.551
+ _logInstalledPlugin:.classDebugEnabled.613
+ _logInstalledPlugin:.classDebugEnabled.620
+ _logInstalledPlugin:.defaultOnce.612
+ _logInstalledPlugin:.defaultOnce.619
+ _objc_msgSend$_convertToWattsFromMilliwatts:
+ _objc_msgSend$_emitPowerSignpostWithMetric:value:
+ _objc_msgSend$_emitPowerSignpostWithMetric:value:pid:
+ _objc_msgSend$_parseSMCMetricsFromEntry:
+ _objc_msgSend$_parseWifiPowerMetricsFromEntry:cacheMetrics:
+ _objc_msgSend$chunkAppsOnScreenAtDate:
+ _objc_msgSend$convertAirDropSessionState:
+ _objc_msgSend$convertClientEvent:
+ _objc_msgSend$convertViewObstructedEvent:
+ _objc_msgSend$cpuCost
+ _objc_msgSend$customConvertBase34ToBase10:
+ _objc_msgSend$displayAPL
+ _objc_msgSend$displayCost
+ _objc_msgSend$displayPower
+ _objc_msgSend$entryEventForwardDefinitionAirDropSession
+ _objc_msgSend$entryEventForwardDefinitionMotionToWake
+ _objc_msgSend$entryEventForwardDefinitionSuppressionManagerClient
+ _objc_msgSend$entryEventForwardDefinitionViewObstructed
+ _objc_msgSend$gpuCost
+ _objc_msgSend$inducedThermalPressure
+ _objc_msgSend$locationCost
+ _objc_msgSend$logEventForwardAirDropSession:
+ _objc_msgSend$logEventForwardMotionToWake:
+ _objc_msgSend$logEventForwardSuppressionManagerClient:
+ _objc_msgSend$logEventForwardViewObstructed:
+ _objc_msgSend$markFileAsPurgeable:withUrgency:
+ _objc_msgSend$networkCost
+ _objc_msgSend$numFilesAtPath:
+ _objc_msgSend$objCType
+ _objc_msgSend$processMetrics
+ _objc_msgSend$sampleWithValue:timestamp:
+ _objc_msgSend$setAirDropSessionXPCListener:
+ _objc_msgSend$setApplicationState:
+ _objc_msgSend$setBatteryPower:
+ _objc_msgSend$setBatteryTemperature:
+ _objc_msgSend$setCellIn:
+ _objc_msgSend$setCellOut:
+ _objc_msgSend$setCellularPower:
+ _objc_msgSend$setChargingRate:
+ _objc_msgSend$setCpuCost:
+ _objc_msgSend$setCpuPower:
+ _objc_msgSend$setDcInputPower:
+ _objc_msgSend$setDisplayAPL:
+ _objc_msgSend$setDisplayCost:
+ _objc_msgSend$setDisplayPower:
+ _objc_msgSend$setDramPower:
+ _objc_msgSend$setEnergyCost:
+ _objc_msgSend$setEnergyOverhead:
+ _objc_msgSend$setGpuCost:
+ _objc_msgSend$setGpuPower:
+ _objc_msgSend$setInducedThermalPressure:
+ _objc_msgSend$setIsSystemPowerAvailableWhileCharging:
+ _objc_msgSend$setLocationCost:
+ _objc_msgSend$setMetricCollectionTimerUpdateInterval:
+ _objc_msgSend$setNetworkCost:
+ _objc_msgSend$setOngoingLocation:
+ _objc_msgSend$setOtherSocPower:
+ _objc_msgSend$setProcessMetrics:
+ _objc_msgSend$setSkinTemperature:
+ _objc_msgSend$setSystemLoadPower:
+ _objc_msgSend$setThermalPressure:
+ _objc_msgSend$setWifiIn:
+ _objc_msgSend$setWifiOut:
+ _objc_msgSend$setWifiPower:
+ _objc_msgSend$shouldCreateQuarantine
+ _objc_msgSend$thermalPressure
+ _objc_msgSend$truncateDB
+ _objc_msgSend$updateWithMetricCollection:
+ _objc_msgSend$value
+ _objc_msgSend$wifiPower
+ _open
+ _refreshAllAppsAndPlugins.classDebugEnabled.555
+ _refreshAllAppsAndPlugins.defaultOnce.554
+ _resyncActiveClients.classDebugEnabled.584
+ _resyncActiveClients.defaultOnce.583
+ _setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3320
+ _setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3319
+ _updateClientsLocationInfo:.classDebugEnabled.687
+ _updateClientsLocationInfo:.defaultOnce.686
+ _updateLocationDistributionEvents.classDebugEnabled.751
+ _updateLocationDistributionEvents.classDebugEnabled.761
+ _updateLocationDistributionEvents.defaultOnce.750
+ _updateLocationDistributionEvents.defaultOnce.760
+ _xFlags.classDebugEnabled.4919
+ _xFlags.classDebugEnabled.4928
+ _xFlags.classDebugEnabled.4937
+ _xFlags.classDebugEnabled.4946
+ _xFlags.classDebugEnabled.4952
+ _xFlags.classDebugEnabled.4958
+ _xFlags.classDebugEnabled.4964
+ _xFlags.classDebugEnabled.4973
+ _xFlags.classDebugEnabled.4979
+ _xFlags.classDebugEnabled.4985
+ _xFlags.defaultOnce.4918
+ _xFlags.defaultOnce.4927
+ _xFlags.defaultOnce.4936
+ _xFlags.defaultOnce.4945
+ _xFlags.defaultOnce.4951
+ _xFlags.defaultOnce.4957
+ _xFlags.defaultOnce.4963
+ _xFlags.defaultOnce.4972
+ _xFlags.defaultOnce.4978
+ _xFlags.defaultOnce.4984
- -[PLBatteryAgent customconvertBase34ToBase10:]
- -[PLBatteryGaugeService emitScoreSignposts:]
- -[PLPowerMetricMonitorService _computeEnergyScoreForProcess].cold.2
- -[PLPowerMetricMonitorService _parseApplicationMetricsFromEntry:].cold.3
- -[PLPowerMetricMonitorService _parseSMCInstantMetricsFromEntry:]
- -[PLPowerMetricMonitorService _parseSMCInstantMetricsFromEntry:].cold.1
- -[PLPowerMetricMonitorService _parseWifiPowerMetricsFromEntry:]
- -[PLPowerMetricMonitorService _sendMetrics].cold.1
- -[PLPowerMetricMonitorService _updateMetricsWithThermalState].cold.1
- -[PLPowerMetricMonitorService metricsAtLastQueryTime]
- -[PLPowerMetricMonitorService setMetricsAtLastQueryTime:]
- GCC_except_table114
- GCC_except_table121
- GCC_except_table126
- GCC_except_table20
- GCC_except_table27
- GCC_except_table39
- GCC_except_table52
- GCC_except_table64
- GCC_except_table71
- GCC_except_table85
- _OBJC_IVAR_$_PLPowerMetricMonitorService._metricsAtLastQueryTime
- _PLBatteryGaugeActivityAggregationKeyNames.keyNames
- _PLBatteryGaugeActivityAggregationKeyNames.onceToken
- ___22-[PLBatteryAgent init]_block_invoke.2979
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.1
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.10
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.2
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.3
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.4
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.5
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.6
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.7
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.8
- ___22-[PLBatteryAgent init]_block_invoke.2979.cold.9
- ___22-[PLBatteryAgent init]_block_invoke.2991
- ___22-[PLBatteryAgent init]_block_invoke.2994
- ___22-[PLBatteryAgent init]_block_invoke.3017
- ___22-[PLBatteryAgent init]_block_invoke.3020
- ___22-[PLBatteryAgent init]_block_invoke.3028
- ___22-[PLBatteryAgent init]_block_invoke.3028.cold.1
- ___22-[PLBatteryAgent init]_block_invoke.3028.cold.2
- ___22-[PLBatteryAgent init]_block_invoke.3034
- ___22-[PLBatteryAgent init]_block_invoke.3038
- ___22-[PLBatteryAgent init]_block_invoke_2.3060
- ___24-[PLBatteryAgent xFlags]_block_invoke.4737
- ___24-[PLBatteryAgent xFlags]_block_invoke.4746
- ___24-[PLBatteryAgent xFlags]_block_invoke.4755
- ___24-[PLBatteryAgent xFlags]_block_invoke.4764
- ___24-[PLBatteryAgent xFlags]_block_invoke.4770
- ___24-[PLBatteryAgent xFlags]_block_invoke.4776
- ___24-[PLBatteryAgent xFlags]_block_invoke.4782
- ___24-[PLBatteryAgent xFlags]_block_invoke.4791
- ___24-[PLBatteryAgent xFlags]_block_invoke.4797
- ___24-[PLBatteryAgent xFlags]_block_invoke.4803
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4646
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4652
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4658
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4664
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4669
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4677
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4683
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4689
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4695
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.4701
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke_2.4704
- ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4365
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3163
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3169
- ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3149
- ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.4816
- ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3500
- ___38-[PLLocationAgent resyncActiveClients]_block_invoke.551
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1852
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1852.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1857
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1857.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1871
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1879
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1879.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1889
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1889.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1894
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1894.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1916
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1916.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1924
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1924.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1932
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1932.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1937
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1937.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1947
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1947.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1954
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1954.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1967
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1967.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1972
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1972.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1982
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1982.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1990
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1990.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1998
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1998.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2005
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2005.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2013
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2013.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2018
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2018.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2023
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2023.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2028
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2028.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2033
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2033.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2041
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2041.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2046
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2046.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2051
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2051.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2061
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2061.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2068
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2068.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2078
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2078.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2086
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2086.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2104
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2104.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2112
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2112.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2119
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2119.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2129
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2129.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2139
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2139.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2147
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2147.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2157
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2157.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2166
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2166.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2175
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2175.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2185
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2185.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2193
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2193.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2201
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2201.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2211
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2211.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2219
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2219.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2227
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2227.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2237
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2237.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2245
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2245.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2255
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2255.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2265
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2265.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2275
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2275.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2283
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2283.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2293
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2293.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2301
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2301.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2309
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2309.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2314
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2314.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2319
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2319.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2324
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2324.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2329
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2329.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2346
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2346.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2351
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2351.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2365
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2365.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2372
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2372.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2390
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2390.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2398
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2398.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2406
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2406.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2414
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2414.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2419
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2419.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2429
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2429.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2439
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2439.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2447
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2447.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2455
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2455.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2463
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2463.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2470
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2470.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2478
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2478.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2488
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2488.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2498
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2498.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2508
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2508.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2533
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2533.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2541
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2541.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2549
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2549.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2556
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2556.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2561
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2561.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2568
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2568.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2581
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2581.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2586
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2586.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2593
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2593.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2611
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2611.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2623
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2623.cold.1
- ___41-[PLApplicationAgent logInstalledPlugin:]_block_invoke.603
- ___41-[PLApplicationAgent logInstalledPlugin:]_block_invoke.607
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.3768
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.3775
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.3771
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.3778
- ___41-[PLBatteryGaugeService DTQueryResponse:]_block_invoke.232
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3241
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3247
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3247.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3263
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3295
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3355
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3355.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3355.cold.2
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3355.cold.3
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3372
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3372.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3383
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3387
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3395
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3395.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3402
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3411
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3417
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3424
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3424.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3431
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3431.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3445
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3445.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3450
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3450.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3457
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3480
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3248
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3293
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3307
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3379
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3396
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3406
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3414
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3425
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3432
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3484
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4924
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4924.cold.1
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4924.cold.2
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.4932
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.4926
- ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.3651
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1720
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1720.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1728
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1728.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1733
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1733.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1755
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1755.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1765
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1765.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1770
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1770.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1799
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1799.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1813
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1813.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1823
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1823.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1831
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1831.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1838
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1838.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.364
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.364.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.379
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.379.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.388
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.388.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.402
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.402.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.414
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.414.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.430
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.430.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.430.cold.2
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.437
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.442
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.442.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.454
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.454.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.462
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.462.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.477
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.477.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.485
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.485.cold.1
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.365
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.380
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.389
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.403
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.415
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.422
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.431
- ___43-[PLLocationAgent initOperatorDependancies]_block_invoke_2.443
- ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.530
- ___44-[PLLocationAgent logEventForwardTechStatus]_block_invoke.536
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.493
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.493.cold.1
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.499
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.507
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.513
- ___44-[PLLocationAgent logEventPointClientStatus]_block_invoke.519
- ___45-[PLBatteryAgent gasGaugeOpenAndStartLogging]_block_invoke.4637
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4960
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4961
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4962
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4963
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4964
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4964.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4965
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4965.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4966
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.4966.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5007
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.591
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.598
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.601
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.607
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.613
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.619
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.626
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.638
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.644
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.650
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.651
- ___45-[PLLocationAgent updateClientsLocationInfo:]_block_invoke.654
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.358
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.358.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.370
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.384
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.414
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.414.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.420
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.420.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.425
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.425.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.432
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.432.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.439
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.439.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.444
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.444.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.454
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.454.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.461
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.461.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.466
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.466.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.474
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.474.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.475
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.499
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.499.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.511
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.511.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.359
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.372
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.385
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.476
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.476.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.476.cold.2
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.500
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.512
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_3.381
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_3.388
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_3.477
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_4.383
- ___46-[PLApplicationAgent refreshAllAppsAndPlugins]_block_invoke.542
- ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke.325
- ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke_2.333
- ___48-[PLDuetServiceDAS initOperatorDependanciesDAS:]_block_invoke_3.341
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.4949
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.4950
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.4954
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.4954.cold.1
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.4954.cold.2
- ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.706
- ___51-[PLLocationAgent updateLocationDistributionEvents]_block_invoke.716
- ___54-[PLBatteryAgent showOrHideTLCNotification:timeInTLC:]_block_invoke.3101
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4600
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4600.cold.1
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4604
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4604.cold.1
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4609
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4613
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4605
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4610
- ___56-[PLApplicationAgent createWidgetStatsAccountingEvents:]_block_invoke.555
- ___56-[PLLocationAgent logEventForwardTechStatus_withLimiter]_block_invoke.527
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.561
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.567
- ___58-[PLLocationAgent logEventForwardClientStatuswithPayload:]_block_invoke.573
- ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3129
- ___61-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:]_block_invoke.596
- ___61-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:]_block_invoke.597
- ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.145
- ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4031
- ___73-[PLLocationAgent closeOpenEntryForClient:withOpenEntry:withTimeStopped:]_block_invoke.583
- ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.144
- ___PLBatteryGaugeActivityAggregationKeyNames_block_invoke
- ___block_literal_global.2088
- ___block_literal_global.2613
- ___block_literal_global.2966
- ___block_literal_global.3075
- ___block_literal_global.3088
- ___block_literal_global.3103
- ___block_literal_global.3154
- ___block_literal_global.3209
- ___block_literal_global.3266
- ___block_literal_global.3309
- ___block_literal_global.3318
- ___block_literal_global.3327
- ___block_literal_global.3339
- ___block_literal_global.334
- ___block_literal_global.3452
- ___block_literal_global.3486
- ___block_literal_global.3499
- ___block_literal_global.354
- ___block_literal_global.360
- ___block_literal_global.362
- ___block_literal_global.367
- ___block_literal_global.372
- ___block_literal_global.374
- ___block_literal_global.376
- ___block_literal_global.380
- ___block_literal_global.383
- ___block_literal_global.386
- ___block_literal_global.389
- ___block_literal_global.392
- ___block_literal_global.397
- ___block_literal_global.402
- ___block_literal_global.4083
- ___block_literal_global.411
- ___block_literal_global.419
- ___block_literal_global.428
- ___block_literal_global.4321
- ___block_literal_global.4333
- ___block_literal_global.437
- ___block_literal_global.4383
- ___block_literal_global.468
- ___block_literal_global.473
- ___block_literal_global.4898
- ___block_literal_global.4959
- ___block_literal_global.79
- ___block_literal_global.804
- __unnamed_array_storage.160
- __unnamed_array_storage.1688
- __unnamed_array_storage.170
- __unnamed_array_storage.1710
- __unnamed_array_storage.1717
- __unnamed_array_storage.1725
- __unnamed_array_storage.1726
- __unnamed_array_storage.1731
- __unnamed_array_storage.1752
- __unnamed_array_storage.1753
- __unnamed_array_storage.1762
- __unnamed_array_storage.1767
- __unnamed_array_storage.1768
- __unnamed_array_storage.1796
- __unnamed_array_storage.1797
- __unnamed_array_storage.1810
- __unnamed_array_storage.1811
- __unnamed_array_storage.1820
- __unnamed_array_storage.1828
- __unnamed_array_storage.1829
- __unnamed_array_storage.1835
- __unnamed_array_storage.1836
- __unnamed_array_storage.1842
- __unnamed_array_storage.1850
- __unnamed_array_storage.1868
- __unnamed_array_storage.1869
- __unnamed_array_storage.1876
- __unnamed_array_storage.1877
- __unnamed_array_storage.1886
- __unnamed_array_storage.1887
- __unnamed_array_storage.1891
- __unnamed_array_storage.1892
- __unnamed_array_storage.1922
- __unnamed_array_storage.1929
- __unnamed_array_storage.1935
- __unnamed_array_storage.1944
- __unnamed_array_storage.1945
- __unnamed_array_storage.1951
- __unnamed_array_storage.1952
- __unnamed_array_storage.1965
- __unnamed_array_storage.1980
- __unnamed_array_storage.1987
- __unnamed_array_storage.1995
- __unnamed_array_storage.1996
- __unnamed_array_storage.2002
- __unnamed_array_storage.2010
- __unnamed_array_storage.2011
- __unnamed_array_storage.2016
- __unnamed_array_storage.2020
- __unnamed_array_storage.2021
- __unnamed_array_storage.2025
- __unnamed_array_storage.2030
- __unnamed_array_storage.2031
- __unnamed_array_storage.2039
- __unnamed_array_storage.2044
- __unnamed_array_storage.2048
- __unnamed_array_storage.2049
- __unnamed_array_storage.2058
- __unnamed_array_storage.2059
- __unnamed_array_storage.2065
- __unnamed_array_storage.2066
- __unnamed_array_storage.2075
- __unnamed_array_storage.2076
- __unnamed_array_storage.2084
- __unnamed_array_storage.2101
- __unnamed_array_storage.2102
- __unnamed_array_storage.2109
- __unnamed_array_storage.2110
- __unnamed_array_storage.2116
- __unnamed_array_storage.2117
- __unnamed_array_storage.2126
- __unnamed_array_storage.2127
- __unnamed_array_storage.2136
- __unnamed_array_storage.2137
- __unnamed_array_storage.2144
- __unnamed_array_storage.2145
- __unnamed_array_storage.2154
- __unnamed_array_storage.2155
- __unnamed_array_storage.2159
- __unnamed_array_storage.2163
- __unnamed_array_storage.2164
- __unnamed_array_storage.2165
- __unnamed_array_storage.2172
- __unnamed_array_storage.2173
- __unnamed_array_storage.2174
- __unnamed_array_storage.2180
- __unnamed_array_storage.2182
- __unnamed_array_storage.2183
- __unnamed_array_storage.2186
- __unnamed_array_storage.2190
- __unnamed_array_storage.2191
- __unnamed_array_storage.2192
- __unnamed_array_storage.2198
- __unnamed_array_storage.2199
- __unnamed_array_storage.2204
- __unnamed_array_storage.2208
- __unnamed_array_storage.2209
- __unnamed_array_storage.2213
- __unnamed_array_storage.2216
- __unnamed_array_storage.2217
- __unnamed_array_storage.2219
- __unnamed_array_storage.2222
- __unnamed_array_storage.2224
- __unnamed_array_storage.2225
- __unnamed_array_storage.2231
- __unnamed_array_storage.2234
- __unnamed_array_storage.2235
- __unnamed_array_storage.2240
- __unnamed_array_storage.2242
- __unnamed_array_storage.2243
- __unnamed_array_storage.2249
- __unnamed_array_storage.2252
- __unnamed_array_storage.2253
- __unnamed_array_storage.2258
- __unnamed_array_storage.2261
- __unnamed_array_storage.2262
- __unnamed_array_storage.2263
- __unnamed_array_storage.2267
- __unnamed_array_storage.2270
- __unnamed_array_storage.2272
- __unnamed_array_storage.2273
- __unnamed_array_storage.2276
- __unnamed_array_storage.2280
- __unnamed_array_storage.2281
- __unnamed_array_storage.2282
- __unnamed_array_storage.2288
- __unnamed_array_storage.2290
- __unnamed_array_storage.2291
- __unnamed_array_storage.2294
- __unnamed_array_storage.2298
- __unnamed_array_storage.2299
- __unnamed_array_storage.2306
- __unnamed_array_storage.2307
- __unnamed_array_storage.2312
- __unnamed_array_storage.2316
- __unnamed_array_storage.2317
- __unnamed_array_storage.2321
- __unnamed_array_storage.2322
- __unnamed_array_storage.2326
- __unnamed_array_storage.2327
- __unnamed_array_storage.2343
- __unnamed_array_storage.2344
- __unnamed_array_storage.2349
- __unnamed_array_storage.2357
- __unnamed_array_storage.2362
- __unnamed_array_storage.2363
- __unnamed_array_storage.2369
- __unnamed_array_storage.2370
- __unnamed_array_storage.2383
- __unnamed_array_storage.2388
- __unnamed_array_storage.2395
- __unnamed_array_storage.2403
- __unnamed_array_storage.2410
- __unnamed_array_storage.2416
- __unnamed_array_storage.2425
- __unnamed_array_storage.2427
- __unnamed_array_storage.2431
- __unnamed_array_storage.2436
- __unnamed_array_storage.2437
- __unnamed_array_storage.2445
- __unnamed_array_storage.2446
- __unnamed_array_storage.2452
- __unnamed_array_storage.2460
- __unnamed_array_storage.2467
- __unnamed_array_storage.2475
- __unnamed_array_storage.2476
- __unnamed_array_storage.2489
- __unnamed_array_storage.2496
- __unnamed_array_storage.2498
- __unnamed_array_storage.2505
- __unnamed_array_storage.2506
- __unnamed_array_storage.2516
- __unnamed_array_storage.2528
- __unnamed_array_storage.2538
- __unnamed_array_storage.2552
- __unnamed_array_storage.2553
- __unnamed_array_storage.2558
- __unnamed_array_storage.2559
- __unnamed_array_storage.2565
- __unnamed_array_storage.2566
- __unnamed_array_storage.2573
- __unnamed_array_storage.2579
- __unnamed_array_storage.2591
- __unnamed_array_storage.2609
- __unnamed_array_storage.2621
- __unnamed_array_storage.2627
- __unnamed_array_storage.2636
- __unnamed_array_storage.2645
- __unnamed_array_storage.2646
- __unnamed_array_storage.2647
- __unnamed_array_storage.2654
- __unnamed_array_storage.2666
- __unnamed_array_storage.2672
- __unnamed_array_storage.2705
- __unnamed_array_storage.2714
- __unnamed_array_storage.2720
- __unnamed_array_storage.2735
- __unnamed_array_storage.2768
- __unnamed_array_storage.2777
- __unnamed_array_storage.285
- __unnamed_array_storage.286
- __unnamed_array_storage.2883
- __unnamed_array_storage.2884
- __unnamed_array_storage.2902
- __unnamed_array_storage.2903
- __unnamed_array_storage.292
- __unnamed_array_storage.2949
- __unnamed_array_storage.299
- __unnamed_array_storage.300
- __unnamed_array_storage.3000
- __unnamed_array_storage.306
- __unnamed_array_storage.3095
- __unnamed_array_storage.3096
- __unnamed_array_storage.3108
- __unnamed_array_storage.3109
- __unnamed_array_storage.314
- __unnamed_array_storage.3182
- __unnamed_array_storage.3214
- __unnamed_array_storage.3215
- __unnamed_array_storage.3260
- __unnamed_array_storage.3261
- __unnamed_array_storage.3290
- __unnamed_array_storage.3291
- __unnamed_array_storage.3304
- __unnamed_array_storage.3305
- __unnamed_array_storage.331
- __unnamed_array_storage.3314
- __unnamed_array_storage.3315
- __unnamed_array_storage.3323
- __unnamed_array_storage.3324
- __unnamed_array_storage.3335
- __unnamed_array_storage.3336
- __unnamed_array_storage.3352
- __unnamed_array_storage.3353
- __unnamed_array_storage.339
- __unnamed_array_storage.3392
- __unnamed_array_storage.3393
- __unnamed_array_storage.342
- __unnamed_array_storage.3442
- __unnamed_array_storage.3443
- __unnamed_array_storage.3477
- __unnamed_array_storage.3478
- __unnamed_array_storage.349
- __unnamed_array_storage.350
- __unnamed_array_storage.361
- __unnamed_array_storage.377
- __unnamed_array_storage.3822
- __unnamed_array_storage.386
- __unnamed_array_storage.3861
- __unnamed_array_storage.3939
- __unnamed_array_storage.399
- __unnamed_array_storage.400
- __unnamed_array_storage.4017
- __unnamed_array_storage.4132
- __unnamed_array_storage.422
- __unnamed_array_storage.423
- __unnamed_array_storage.4315
- __unnamed_array_storage.441
- __unnamed_array_storage.442
- __unnamed_array_storage.451
- __unnamed_array_storage.452
- __unnamed_array_storage.460
- __unnamed_array_storage.463
- __unnamed_array_storage.464
- __unnamed_array_storage.471
- __unnamed_array_storage.472
- __unnamed_array_storage.4851
- __unnamed_array_storage.4852
- __unnamed_array_storage.4858
- __unnamed_array_storage.4859
- __unnamed_array_storage.4918
- __unnamed_array_storage.4919
- __unnamed_array_storage.4940
- __unnamed_array_storage.4941
- __unnamed_array_storage.496
- __unnamed_array_storage.497
- __unnamed_array_storage.684
- __unnamed_array_storage.802
- _cancelEALogging.classDebugEnabled.3148
- _cancelEALogging.defaultOnce.3147
- _gasGaugeOpenAndStartLogging.classDebugEnabled.4636
- _gasGaugeOpenAndStartLogging.defaultOnce.4635
- _gasGaugeRead.classDebugEnabled.4645
- _gasGaugeRead.classDebugEnabled.4651
- _gasGaugeRead.classDebugEnabled.4657
- _gasGaugeRead.classDebugEnabled.4663
- _gasGaugeRead.classDebugEnabled.4671
- _gasGaugeRead.classDebugEnabled.4676
- _gasGaugeRead.classDebugEnabled.4682
- _gasGaugeRead.classDebugEnabled.4688
- _gasGaugeRead.classDebugEnabled.4694
- _gasGaugeRead.classDebugEnabled.4703
- _gasGaugeRead.defaultOnce.4644
- _gasGaugeRead.defaultOnce.4650
- _gasGaugeRead.defaultOnce.4656
- _gasGaugeRead.defaultOnce.4662
- _gasGaugeRead.defaultOnce.4668
- _gasGaugeRead.defaultOnce.4670
- _gasGaugeRead.defaultOnce.4675
- _gasGaugeRead.defaultOnce.4681
- _gasGaugeRead.defaultOnce.4687
- _gasGaugeRead.defaultOnce.4693
- _gasGaugeRead.defaultOnce.4699
- _gasGaugeRead.defaultOnce.4702
- _gasGaugeRead.objectForKey.4700
- _getIOPSDevices.classDebugEnabled.3162
- _getIOPSDevices.classDebugEnabled.3168
- _getIOPSDevices.defaultOnce.3161
- _getIOPSDevices.defaultOnce.3167
- _handlePPMCallback.defaultOnce.3490
- _initOperatorDependancies.classDebugEnabled.3405
- _initOperatorDependancies.classDebugEnabled.3413
- _initOperatorDependancies.classDebugEnabled.3416
- _initOperatorDependancies.defaultOnce.3404
- _initOperatorDependancies.defaultOnce.3412
- _initOperatorDependancies.defaultOnce.3415
- _kPLApplicationAgentEventForwardNameHomeScreenPresentation_block_invoke_3.classDebugEnabled.485
- _kPLApplicationAgentEventForwardNameHomeScreenPresentation_block_invoke_3.defaultOnce.484
- _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3019
- _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3033
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.2981
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3015
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3018
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3032
- _kPLBatteryAgentStringUserType_block_invoke.objectForKey.3016
- _kPLBatteryAgentStringUserType_block_invoke_12.classDebugEnabled.4931
- _kPLBatteryAgentStringUserType_block_invoke_12.defaultOnce.4930
- _kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3240
- _kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3239
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.classDebugEnabled.498
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_11.defaultOnce.497
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.590
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.597
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.600
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.606
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.612
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.618
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.625
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.637
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.643
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.classDebugEnabled.649
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.589
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.596
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.599
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.605
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.611
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.617
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.624
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.636
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.642
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_13.defaultOnce.648
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.classDebugEnabled.436
- _kPLLocationAgentAddProcessesOfInterestNotificationName_block_invoke_9.defaultOnce.435
- _logEventBackwardHeatMap.classDebugEnabled.3770
- _logEventBackwardHeatMap.classDebugEnabled.3777
- _logEventBackwardHeatMap.defaultOnce.3769
- _logEventBackwardHeatMap.defaultOnce.3776
- _logEventForwardClientStatuswithPayload:.classDebugEnabled.560
- _logEventForwardClientStatuswithPayload:.classDebugEnabled.566
- _logEventForwardClientStatuswithPayload:.classDebugEnabled.572
- _logEventForwardClientStatuswithPayload:.defaultOnce.559
- _logEventForwardClientStatuswithPayload:.defaultOnce.565
- _logEventForwardClientStatuswithPayload:.defaultOnce.571
- _logEventForwardTechStatus.classDebugEnabled.529
- _logEventForwardTechStatus.classDebugEnabled.535
- _logEventForwardTechStatus.defaultOnce.528
- _logEventForwardTechStatus.defaultOnce.534
- _logEventIntervalGasGauge.classDebugEnabled.3650
- _logEventIntervalGasGauge.defaultOnce.3649
- _logEventNoneBatteryConfigWithRawData:.classDebugEnabled.4612
- _logEventNoneBatteryConfigWithRawData:.defaultOnce.4611
- _logEventPointClientStatus.classDebugEnabled.506
- _logEventPointClientStatus.classDebugEnabled.512
- _logEventPointClientStatus.classDebugEnabled.518
- _logEventPointClientStatus.defaultOnce.505
- _logEventPointClientStatus.defaultOnce.511
- _logEventPointClientStatus.defaultOnce.517
- _logInstalledPlugin:.classDebugEnabled.602
- _logInstalledPlugin:.classDebugEnabled.609
- _logInstalledPlugin:.defaultOnce.601
- _logInstalledPlugin:.defaultOnce.608
- _objc_msgSend$_parseSMCInstantMetricsFromEntry:
- _objc_msgSend$_parseWifiPowerMetricsFromEntry:
- _objc_msgSend$customconvertBase34ToBase10:
- _objc_msgSend$setMetricsAtLastQueryTime:
- _objc_msgSend$updateWithMetrics:
- _refreshAllAppsAndPlugins.classDebugEnabled.544
- _refreshAllAppsAndPlugins.defaultOnce.543
- _resyncActiveClients.classDebugEnabled.550
- _resyncActiveClients.defaultOnce.549
- _setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3140
- _setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3139
- _updateClientsLocationInfo:.classDebugEnabled.653
- _updateClientsLocationInfo:.defaultOnce.652
- _updateLocationDistributionEvents.classDebugEnabled.705
- _updateLocationDistributionEvents.classDebugEnabled.715
- _updateLocationDistributionEvents.defaultOnce.704
- _updateLocationDistributionEvents.defaultOnce.714
- _xFlags.classDebugEnabled.4736
- _xFlags.classDebugEnabled.4745
- _xFlags.classDebugEnabled.4754
- _xFlags.classDebugEnabled.4763
- _xFlags.classDebugEnabled.4769
- _xFlags.classDebugEnabled.4775
- _xFlags.classDebugEnabled.4781
- _xFlags.classDebugEnabled.4790
- _xFlags.classDebugEnabled.4796
- _xFlags.classDebugEnabled.4802
- _xFlags.defaultOnce.4735
- _xFlags.defaultOnce.4744
- _xFlags.defaultOnce.4753
- _xFlags.defaultOnce.4762
- _xFlags.defaultOnce.4768
- _xFlags.defaultOnce.4774
- _xFlags.defaultOnce.4780
- _xFlags.defaultOnce.4789
- _xFlags.defaultOnce.4795
- _xFlags.defaultOnce.4801
CStrings:
+ "\x0f\v\x11\x11\x12"
+ "\x1f\x0f\a\x1f\x0f\x0f\t!?\r"
+ "!/\x06"
+ "%.6e"
+ "%s interval: %f"
+ "-[PLPowerMetricMonitorService changeUpdateInterval:]_block_invoke"
+ "000"
+ "@\"PPSMetricCollection\""
+ "AirDropSession"
+ "AirDropSession callback: %@"
+ "AirDropSessionXPCListener"
+ "AmbientModeMotionToWake"
+ "AmbientModeMotionToWake payload: %@"
+ "Application_State"
+ "Battery_Power_W"
+ "Battery_Temp_C"
+ "CPU_Cost"
+ "CPU_Power_W"
+ "CPU_Seconds"
+ "Cell_In"
+ "Cell_Out"
+ "Cellular_Power_W"
+ "Charging_Rate_mA"
+ "ContentSize"
+ "DC_Input_Power_W"
+ "DRAM_Power_W"
+ "Display_APL"
+ "Display_Power_W"
+ "Dod0AtQualifiedQmax"
+ "Energy_Cost"
+ "Energy_Overhead"
+ "Failed"
+ "Failed to get num files at path: %@ error: %@"
+ "Failed to mark %@ purgeable - can't open error: %s"
+ "Failed to mark %@ purgeable - flags 0x%llx returned %d (%s)"
+ "FedPdSpecRevision"
+ "FedPwrPolicySt"
+ "FedSnkConfReason"
+ "FedSrcConfReason"
+ "FileSize"
+ "GPU_Cost"
+ "GPU_Power_W"
+ "Induced_Thermal_State"
+ "Interface"
+ "Location_Cost"
+ "Marked %@ purgeable with urgency: %llu"
+ "MotionToWake"
+ "Num files at %@ = %d"
+ "Ongoing_Location"
+ "Other_SoC_Power_W"
+ "PortControllerActiveContractRdo"
+ "PortControllerCapMismatch"
+ "PortControllerDataRoleSwapCount"
+ "PortControllerDataRoleSwapFailCount"
+ "PortControllerElectionFailReason"
+ "PortControllerFwVersion"
+ "PortControllerInpFetEnFailCount"
+ "PortControllerIrqCntAlert"
+ "PortControllerIrqCntAppLd"
+ "PortControllerIrqCntConSrc"
+ "PortControllerIrqCntHrdRst"
+ "PortControllerIrqCntPdStsUpd"
+ "PortControllerIrqCntPlg"
+ "PortControllerIrqCntPwrStsUpd"
+ "PortControllerIrqCntRxIdSop"
+ "PortControllerIrqCntRxRdo"
+ "PortControllerIrqCntRxSnkCap"
+ "PortControllerIrqCntRxSrcCap"
+ "PortControllerIrqCntStsUpd"
+ "PortControllerIrqCntUsb2Plg"
+ "PortControllerIrqCntUsb2Wak"
+ "PortControllerIrqCntUvdmEnum"
+ "PortControllerIrqCntUvdmStsUpd"
+ "PortControllerIrqCntldcm"
+ "PortControllerNEprPDOs"
+ "PortControllerPDst"
+ "PortControllerPortMode"
+ "PortControllerPortPDO0"
+ "PortControllerPortPDO1"
+ "PortControllerPortPDO10"
+ "PortControllerPortPDO11"
+ "PortControllerPortPDO12"
+ "PortControllerPortPDO13"
+ "PortControllerPortPDO14"
+ "PortControllerPortPDO2"
+ "PortControllerPortPDO3"
+ "PortControllerPortPDO4"
+ "PortControllerPortPDO5"
+ "PortControllerPortPDO6"
+ "PortControllerPortPDO7"
+ "PortControllerPortPDO8"
+ "PortControllerPortPDO9"
+ "PortControllerPwrRoleSwapCount"
+ "PortControllerPwrRoleSwapFailCount"
+ "PortControllerShortDetectCount"
+ "PortControllerSrcTypes"
+ "PortControllerSrdoCount"
+ "PortControllerSrdoRetryCount"
+ "PortControllerSrdyCount"
+ "PortControllerSurpriseAckCount"
+ "PortControllerSurpriseNackCount"
+ "PortControllerUvdmStatus"
+ "PortControllerVdoFailCount"
+ "PortControllerWakeFailCount"
+ "Quarantine dst: %@"
+ "Quarantine src: %@"
+ "Screen On: Periodic Update - Updating On Screen time for %@ with %f added seconds"
+ "Screen On: Tried updating On Screen time, but couldn't retrieve apps on screen"
+ "Screen On: Updating On Screen time for %@ with %f added seconds"
+ "Send"
+ "Skin_Temp_C"
+ "SuppressionManager client state change XPC with payload=%@"
+ "SuppressionManagerClient"
+ "SuppressionManagerClientStateChange"
+ "System_Load_Power_W"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_AirDropSessionXPCListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_motionToWakeListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_suppressionManagerClientListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_viewObstructedListener"
+ "T@\"PPSMetricCollection\",&,N,V_cachedMetrics"
+ "T@\"PPSMetricCollection\",&,N,V_metrics"
+ "Thermal_State"
+ "TransferID"
+ "Unknown/Other AirDropSession State %@"
+ "VOEvent"
+ "ViewObstructed"
+ "ViewObstructed state change XPC with payload=%@"
+ "ViewObstructedStateChange"
+ "WiFi_In"
+ "WiFi_Out"
+ "WiFi_Power_W"
+ "_AirDropSessionXPCListener"
+ "_convertToWattsFromMilliwatts:"
+ "_emitPowerSignpostWithMetric:value:"
+ "_emitPowerSignpostWithMetric:value:pid:"
+ "_motionToWakeListener"
+ "_parseSMCMetricsFromEntry:"
+ "_parseWifiPowerMetricsFromEntry:cacheMetrics:"
+ "_suppressionManagerClientListener"
+ "_viewObstructedListener"
+ "changeUpdateInterval:"
+ "chunkAppsOnScreenAtDate:"
+ "clientEvent"
+ "clientNumbers"
+ "clientType"
+ "com.apple.PerfPowerMetricMonitor"
+ "com.apple.PhotosUIPrivate.PhotosAmbientPosterProvider"
+ "convertAirDropSessionState:"
+ "convertClientEvent:"
+ "convertViewObstructedEvent:"
+ "cpuCost"
+ "customConvertBase34ToBase10:"
+ "displayAPL"
+ "displayCost"
+ "displayPower"
+ "entryEventForwardDefinitionAirDropSession"
+ "entryEventForwardDefinitionMotionToWake"
+ "entryEventForwardDefinitionSuppressionManagerClient"
+ "entryEventForwardDefinitionViewObstructed"
+ "gpuCost"
+ "inducedThermalPressure"
+ "locationCost"
+ "logEventForwardAirDropSession:"
+ "logEventForwardMotionToWake:"
+ "logEventForwardSuppressionManagerClient:"
+ "logEventForwardViewObstructed:"
+ "markFileAsPurgeable:withUrgency:"
+ "motionToWakeListener"
+ "networkCost"
+ "numFilesAtPath:"
+ "objCType"
+ "powerMetricMonitorService"
+ "processMetrics"
+ "sampleWithValue:timestamp:"
+ "setAirDropSessionXPCListener:"
+ "setApplicationState:"
+ "setBatteryPower:"
+ "setBatteryTemperature:"
+ "setCellIn:"
+ "setCellOut:"
+ "setCellularPower:"
+ "setChargingRate:"
+ "setCpuCost:"
+ "setCpuPower:"
+ "setDcInputPower:"
+ "setDisplayAPL:"
+ "setDisplayCost:"
+ "setDisplayPower:"
+ "setDramPower:"
+ "setEnergyCost:"
+ "setEnergyOverhead:"
+ "setGpuCost:"
+ "setGpuPower:"
+ "setInducedThermalPressure:"
+ "setIsSystemPowerAvailableWhileCharging:"
+ "setLocationCost:"
+ "setMetricCollectionTimerUpdateInterval:"
+ "setMotionToWakeListener:"
+ "setNetworkCost:"
+ "setOngoingLocation:"
+ "setOtherSocPower:"
+ "setProcessMetrics:"
+ "setSkinTemperature:"
+ "setSuppressionManagerClientListener:"
+ "setSystemLoadPower:"
+ "setThermalPressure:"
+ "setViewObstructedListener:"
+ "setWifiIn:"
+ "setWifiOut:"
+ "setWifiPower:"
+ "should quarantine: %d"
+ "shouldCreateQuarantine"
+ "suppress"
+ "suppressionManagerClientListener"
+ "thermalPressure"
+ "truncateDB"
+ "unsuppress"
+ "updateWithMetricCollection:"
+ "viewObstructedListener"
+ "wifiPower"
+ "{\"metric\":\"%{public}@\",\"value\":%{public}@,\"pid\":%{public}@}"
+ "{\"metric\":\"%{public}@\",\"value\":%{public}@}"
- "\x0f\v\x11\x11"
- "\x1f\x01"
- "\x1f\x0f\a\x1f\x0f\x0f\b!?\r"
- "!/\a"
- "%s: currApplicationState=%d"
- "%s: current ThermalState=%llu, induced ThermalState=%lld"
- "-[PLPowerMetricMonitorService _updateMetricsWithThermalState]"
- "ANE Power"
- "AVE Power"
- "ApplicationState"
- "BatteryGauge"
- "CPU Power"
- "CPUSeconds"
- "Cell"
- "DCS Power"
- "DISP Power"
- "DISPEXT"
- "DISPEXT Power"
- "DRAM Power"
- "DisplayFrames"
- "ECPM"
- "ECPM Power"
- "ECPU"
- "ECPU Power"
- "GPU Combined Power"
- "GPU Power"
- "GPU SRAM"
- "GPU SRAM Power"
- "ISP Power"
- "IsSystemPowerAvailableWhileDrawingPower"
- "MSR Power"
- "Metric Monitor: Score %f, Overhead = %f"
- "Networking"
- "OngoingLocation"
- "Overall"
- "PCIe Port 1 Energy"
- "PCIe Port 1 Power"
- "PCIe Port 2 Energy"
- "PCIe Port 2 Power"
- "PCPM"
- "PCPM Power"
- "PCPU"
- "PCPU Power"
- "PowerMetricMonitorService"
- "SOC_AON Power"
- "SOC_REST Power"
- "Sending metrics: %@"
- "SkinTemp"
- "T@\"NSMutableDictionary\",&,N,V_cachedMetrics"
- "T@\"NSMutableDictionary\",&,N,V_metrics"
- "T@\"NSMutableDictionary\",&,N,V_metricsAtLastQueryTime"
- "ThermalState"
- "ThermalStateInduced"
- "VDEC Power"
- "VENC Power"
- "WiFi"
- "_metricsAtLastQueryTime"
- "_parseSMCInstantMetricsFromEntry:"
- "_parseWifiPowerMetricsFromEntry:"
- "customconvertBase34ToBase10:"
- "emitScoreSignposts:"
- "energyCost"
- "energyOverhead"
- "metricsAtLastQueryTime"
- "powerMetricMonitor"
- "setMetricsAtLastQueryTime:"
- "updateWithMetrics:"
- "{\"Metric\":\"%{public}@\",\"Source\":\"%{public}@\",\"Time\":%{public}.6f,\"Value\":%{public}.6e}"

```
