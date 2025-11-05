## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Versions/A/Sentry`

```diff

-1.20.38.0.0
-  __TEXT.__text: 0x1cadc
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x1468
-  __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x1d35
-  __TEXT.__oslogstring: 0x2e3a
-  __TEXT.__gcc_except_tab: 0x4e8
-  __TEXT.__unwind_info: 0x6b0
-  __TEXT.__objc_classname: 0x367
-  __TEXT.__objc_methname: 0x4846
-  __TEXT.__objc_methtype: 0xd84
-  __TEXT.__objc_stubs: 0x3420
-  __DATA_CONST.__got: 0x398
+1.20.42.0.0
+  __TEXT.__text: 0x1e1b8
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x1778
+  __TEXT.__const: 0x174
+  __TEXT.__cstring: 0x1ea0
+  __TEXT.__oslogstring: 0x2fad
+  __TEXT.__gcc_except_tab: 0x540
+  __TEXT.__unwind_info: 0x730
+  __TEXT.__objc_classname: 0x386
+  __TEXT.__objc_methname: 0x4951
+  __TEXT.__objc_methtype: 0xda6
+  __TEXT.__objc_stubs: 0x3500
+  __DATA_CONST.__got: 0x3a8
   __DATA_CONST.__const: 0x200
-  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1000
-  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_selrefs: 0x1140
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x380
-  __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0x1cc0
-  __AUTH_CONST.__objc_const: 0x3548
+  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__const: 0xb60
+  __AUTH_CONST.__cfstring: 0x1e80
+  __AUTH_CONST.__objc_const: 0x31f0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x1e0
+  __AUTH.__objc_data: 0x960
+  __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0x3e8
-  __DATA.__bss: 0x218
+  __DATA.__bss: 0x238
   __DATA.__common: 0x59
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/Versions/A/DiagnosticRequest
   - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
   - /System/Library/PrivateFrameworks/PerformanceAnalysis.framework/Versions/A/PerformanceAnalysis

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: C2770632-5841-3528-8CC3-D65583DF021F
-  Functions: 712
-  Symbols:   1940
-  CStrings:  1656
+  UUID: F1BA2311-894A-37B1-80C0-6707A661E8D6
+  Functions: 760
+  Symbols:   2024
+  CStrings:  1707
 
Symbols:
+ +[STYDeviceInfo isMemoryConstrained].cold.1
+ +[STYDeviceInfo osBuild].cold.1
+ +[STYDiagCollectorLogger sharedLogger].cold.1
+ +[STYDiagnosticUploader sharedDiagnosticUploader].cold.1
+ +[STYDirectories inFlightDirectory].cold.1
+ +[STYDirectories pendingDirectory].cold.1
+ +[STYDirectories sysdiagnoseDirectory].cold.1
+ +[STYFrameworkHelper sharedHelper].cold.1
+ +[STYPerformanceChecker sharedPerfChecker].cold.1
+ +[STYScenarioReportLogger sharedLogger].cold.1
+ +[STYSentryDiagnosticsHelper saveTailspin:reason:includeSignposts:includeLogs:startTime:endTime:symbolicate:error:].cold.3
+ +[STYSentryDiagnosticsHelper saveTailspin:reason:includeSignposts:includeLogs:startTime:endTime:symbolicate:error:].cold.4
+ +[STYSignpostsMonitor sharedMonitor].cold.1
+ +[STYUserScenarioCache sharedCache].cold.1
+ -[STYIOPMNotificationMonitor init].cold.1
+ -[STYSignpostStreamingStatistics .cxx_destruct]
+ -[STYSignpostStreamingStatistics _emitTelemetryLockedEndTime:]
+ -[STYSignpostStreamingStatistics _resetLocked]
+ -[STYSignpostStreamingStatistics addSignpost:]
+ -[STYSignpostStreamingStatistics dealloc]
+ -[STYSignpostStreamingStatistics emitTelemetry]
+ -[STYSignpostStreamingStatistics init]
+ -[STYSignpostsMonitor setStreamingStatistics:]
+ -[STYSignpostsMonitor streamingStatistics]
+ GCC_except_table121
+ GCC_except_table140
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table219
+ GCC_except_table224
+ GCC_except_table226
+ GCC_except_table239
+ GCC_except_table39
+ GCC_except_table45
+ OBJC_IVAR_$_STYSignpostStreamingStatistics._machAbsTimeStart
+ OBJC_IVAR_$_STYSignpostStreamingStatistics._periodicTimer
+ OBJC_IVAR_$_STYSignpostStreamingStatistics._queue
+ OBJC_IVAR_$_STYSignpostStreamingStatistics._sigtermSource
+ OBJC_IVAR_$_STYSignpostStreamingStatistics._subsystemDict
+ OBJC_IVAR_$_STYSignpostStreamingStatistics._totalCount
+ OBJC_IVAR_$_STYSignpostsMonitor._streamingStatistics
+ STYDiagnosticsLog.cold.1
+ STYDiagnosticsUploadLog.cold.1
+ STYDirectoryLog.cold.1
+ STYMachAbsoluteTimeToMilliseconds.cold.1
+ STYMachAbsoluteTimeToSeconds.cold.1
+ STYMillisecondsToMachAbsoluteTime.cold.1
+ STYSecondsToMachAbsoluteTime.cold.1
+ STYWakeDebuggingSignposts.cold.1
+ STYWakeFromDarkWakeSignposts.cold.1
+ STYWakeFromSleepSignposts.cold.1
+ STYWakeFromStandbySignposts.cold.1
+ STYWakeLog.cold.1
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_STYSignpostStreamingStatistics
+ _OBJC_METACLASS_$_STYSignpostStreamingStatistics
+ _STYMachAbsoluteTimeToMilliseconds
+ _STYMachAbsoluteTimeToSeconds
+ _STYMillisecondsToMachAbsoluteTime
+ _STYSecondsToMachAbsoluteTime
+ _TSPDumpOptions_EndTimestamp
+ __38-[STYSignpostStreamingStatistics init]_block_invoke.61
+ __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.175
+ __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.182
+ __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.188
+ __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.176
+ __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.183
+ __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.189
+ __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_3.184
+ __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_3.190
+ __46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.470
+ __46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.475
+ __46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.476
+ __50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.371
+ __50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.372
+ __MergedGlobals
+ __OBJC_$_INSTANCE_METHODS_STYSignpostStreamingStatistics
+ __OBJC_$_INSTANCE_VARIABLES_STYSignpostStreamingStatistics
+ __OBJC_CLASS_RO_$_STYSignpostStreamingStatistics
+ __OBJC_METACLASS_RO_$_STYSignpostStreamingStatistics
+ ___38-[STYSignpostStreamingStatistics init]_block_invoke
+ ___46-[STYSignpostStreamingStatistics addSignpost:]_block_invoke
+ ___47-[STYSignpostStreamingStatistics emitTelemetry]_block_invoke
+ ___MachToSeconds_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___block_descriptor_48_e8_32r40w_e5_v8?0l
+ ___copy_helper_block_e8_32r40w
+ ___destroy_helper_block_e8_32r40w
+ ___timebaseConversionFactor_block_invoke
+ ___udivti3
+ __block_literal_global.159
+ __block_literal_global.162
+ __block_literal_global.165
+ __block_literal_global.169
+ __block_literal_global.465
+ __block_literal_global.542
+ __dispatch_source_type_signal
+ __startMonitoringSystemConditions_block_invoke.cold.1
+ _dispatch_block_create_with_qos_class
+ _dispatch_source_cancel
+ _objc_msgSend$addSignpost:
+ _objc_msgSend$avoidGeneratingTailspinsForAppLaunches
+ _objc_msgSend$emitTelemetry
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$isSyntheticIntervalEvent
+ _objc_msgSend$setStreamingStatistics:
+ _objc_msgSend$streamingStatistics
+ _timebaseConversionFactor
+ getLock.cold.1
+ getReporter.cold.1
+ machCtsTimeToMs.cold.1
+ monitorThermalPressure.cold.1
+ timebaseConversionFactor.cold.1
+ timebaseConversionFactor.onceToken
+ timebaseConversionFactor.timebaseConversion
- GCC_except_table102
- GCC_except_table123
- GCC_except_table141
- GCC_except_table143
- GCC_except_table20
- GCC_except_table202
- GCC_except_table207
- GCC_except_table209
- GCC_except_table222
- GCC_except_table28
- _OUTLINED_FUNCTION_13
- _TSPDumpOptions_MaxTimestamp
- __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.105
- __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.112
- __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.118
- __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.106
- __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.113
- __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.119
- __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_3.114
- __39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_3.120
- __46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.396
- __46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.399
- __46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.400
- __50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.297
- __50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.298
- __block_literal_global.100
- __block_literal_global.391
- __block_literal_global.90
- __block_literal_global.93
- __block_literal_global.96
CStrings:
+ "%@:%@"
+ "@\"STYSignpostStreamingStatistics\""
+ "Emitting com.apple.Sentry.SignpostStreaming telemetry %@"
+ "Emitting com.apple.Sentry.SignpostStreaming.SubsystemCategory telemetry %@"
+ "Failed to close fd for tailspin file %@"
+ "Failed to open fd for tailspin file %@"
+ "No signposts, and only monitoring for less than a minute, not emitting telemetry"
+ "STYSignpostStreamingStatistics"
+ "T@\"STYSignpostStreamingStatistics\",&,V_streamingStatistics"
+ "[Signpost: %@] Deferring app launch tailspin to special app launch monitoring "
+ "_machAbsTimeStart"
+ "_periodicTimer"
+ "_sigtermSource"
+ "_streamingStatistics"
+ "_subsystemDict"
+ "_totalCount"
+ "addSignpost:"
+ "com.apple.Sentry.SignpostStreaming"
+ "com.apple.Sentry.SignpostStreaming.PendingTelemetry"
+ "com.apple.Sentry.SignpostStreaming.SubsystemCategory"
+ "com.apple.sentry.signpostsMonitor.SignpostStreamingStatistics"
+ "emitTelemetry"
+ "initWithFormat:"
+ "isSyntheticIntervalEvent"
+ "largest_sc"
+ "largest_sc_count"
+ "largest_sc_rate"
+ "largest_signpost"
+ "largest_signpost_count"
+ "largest_signpost_rate"
+ "sc"
+ "sc_count"
+ "sc_rate"
+ "setStreamingStatistics:"
+ "signpost_count"
+ "signpost_rate"
+ "streamingStatistics"

```
