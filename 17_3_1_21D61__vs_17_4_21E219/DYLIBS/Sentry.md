## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

```diff

-1.20.32.2.0
-  __TEXT.__text: 0x10fb4
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0xce8
-  __TEXT.__const: 0x7c
-  __TEXT.__cstring: 0x1416
-  __TEXT.__oslogstring: 0x1a01
-  __TEXT.__gcc_except_tab: 0x258
-  __TEXT.__unwind_info: 0x43c
+1.20.37.0.0
+  __TEXT.__text: 0xfb5c
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0xd00
+  __TEXT.__const: 0x74
+  __TEXT.__cstring: 0x12eb
+  __TEXT.__oslogstring: 0x1bbe
+  __TEXT.__gcc_except_tab: 0x2f0
+  __TEXT.__unwind_info: 0x408
   __TEXT.__objc_classname: 0x192
-  __TEXT.__objc_methname: 0x2f93
-  __TEXT.__objc_methtype: 0x3a9
-  __TEXT.__objc_stubs: 0x22c0
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x510
+  __TEXT.__objc_methname: 0x2d7d
+  __TEXT.__objc_methtype: 0x3bb
+  __TEXT.__objc_stubs: 0x1e80
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x450
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10d0
-  __DATA_CONST.__objc_selrefs: 0xad0
-  __AUTH_CONST.__cfstring: 0x10c0
-  __AUTH_CONST.__const: 0x3a0
+  __DATA_CONST.__objc_const: 0x1120
+  __DATA_CONST.__objc_selrefs: 0x9f8
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x48
+  __AUTH_CONST.__cfstring: 0x1040
+  __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__objc_const: 0x708
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_classrefs: 0x138
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x124
-  __DATA.__data: 0xe0
+  __DATA.__objc_ivar: 0x12c
+  __DATA.__data: 0xe8
   __DATA.__bss: 0x80
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x410
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x49
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: E76CD0AA-2A56-36A6-8233-ADAE8607CDC1
-  Functions: 448
-  Symbols:   1698
-  CStrings:  994
+  UUID: 40403C2D-D5A5-39DC-A15D-B93518F62557
+  Functions: 427
+  Symbols:   1579
+  CStrings:  954
 
Symbols:
+ -[STYSpecialAppLaunchSignpostMonitorHelper enforceAppLaunchThreshold]
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.13
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.14
+ -[STYSpecialAppLaunchSignpostMonitorHelper setEnforceAppLaunchThreshold:]
+ -[STYWorkflowResponsivenessMonitorHelper updateAllowList]
+ -[STYWorkflowResponsivenessMonitorHelper workflowEventCompleted:completedWRTracker:]
+ -[STYWorkflowResponsivenessMonitorHelper workflowIsUnderLimits:]
+ GCC_except_table110
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table17
+ GCC_except_table21
+ GCC_except_table92
+ _OBJC_IVAR_$_STYSpecialAppLaunchSignpostMonitorHelper._defaults
+ _OBJC_IVAR_$_STYSpecialAppLaunchSignpostMonitorHelper._enforceAppLaunchThreshold
+ ___30-[STYSignpostsMonitor disable]_block_invoke_2
+ ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.107
+ ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.108
+ ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.cold.1
+ ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.cold.2
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.419
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.422
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.423
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke_2
+ ___50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.321
+ ___50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.322
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_48_e8_32w40w_e32_v16?0"WRWorkflowEventTracker"8lw32l8w40l8
+ ___block_literal_global.414
+ _kSTYDefaultsEnforceAppLaunchThreshold
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$allowListForDiagnostics
+ _objc_msgSend$cleanupWorkflowResponsivenessDiagnosticsDirectory
+ _objc_msgSend$gatherDiagnosticsIfNeeded
+ _objc_msgSend$initForLiveStreamingWithWorkflow:timeoutQueue:eventCompletionCallback:
+ _objc_msgSend$updateAllowList
+ _objc_msgSend$workflowEventCompleted:completedWRTracker:
+ _objc_msgSend$workflowIsUnderLimits:
- -[STYWorkflowResponsivenessMonitorHelper didEndMonitoring]
- -[STYWorkflowResponsivenessMonitorHelper willStartMonitoring]
- -[STYWorkflowResponsivenessMonitorHelper workflowEventCompleted:overallIntervalStart:overallIntervalEnd:startSignpost:endSignpost:]
- -[STYWorkflowResponsivenessMonitorHelper workflowEventCompleted:overallIntervalStart:overallIntervalEnd:startSignpost:endSignpost:].cold.1
- -[STYWorkflowResponsivenessMonitorHelper workflowEventCompleted:overallIntervalStart:overallIntervalEnd:startSignpost:endSignpost:].cold.2
- -[STYWorkflowResponsivenessMonitorHelper workflowEventCompleted:overallIntervalStart:overallIntervalEnd:startSignpost:endSignpost:].cold.3
- -[STYWorkflowResponsivenessMonitorHelper workflowEventCompleted:overallIntervalStart:overallIntervalEnd:startSignpost:endSignpost:].cold.4
- GCC_except_table109
- GCC_except_table16
- GCC_except_table20
- GCC_except_table91
- _NSFilePosixPermissions
- _NSURLCreationDateKey
- _NSURLIsRegularFileKey
- _NSURLNameKey
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_NSURL
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _SPReportWorkflowResponsivenessDelay
- _WRWorkflowEndMachContTimeNSKey
- _WRWorkflowEndSignpostKey
- _WRWorkflowEndThreadIDKey
- _WRWorkflowEnvironmentKey
- _WRWorkflowNameKey
- _WRWorkflowSignpostCountKey
- _WRWorkflowSignpostDurationSecondsKey
- _WRWorkflowSignpostEmitMachContTimeNSKey
- _WRWorkflowSignpostEmitThreadIDKey
- _WRWorkflowSignpostEmitsListKey
- _WRWorkflowSignpostIntervalBeginMachContTimeNSKey
- _WRWorkflowSignpostIntervalBeginThreadIDKey
- _WRWorkflowSignpostIntervalEndMachContTimeNSKey
- _WRWorkflowSignpostIntervalEndThreadIDKey
- _WRWorkflowSignpostIntervalsListKey
- _WRWorkflowSignpostListKey
- _WRWorkflowSignpostNameKey
- _WRWorkflowSignpostSecondsUntilFirstSignpostKey
- _WRWorkflowSignpostThresholdCountKey
- _WRWorkflowSignpostThresholdDurationSecondsKey
- _WRWorkflowStartMachContTimeNSKey
- _WRWorkflowStartSignpostKey
- _WRWorkflowStartThreadIDKey
- _WRWorkflowThresholdDurationSecondsKey
- ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.104
- ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.105
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.cold.1
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.cold.2
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.cold.3
- ___50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.317
- ___50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.318
- ___61-[STYWorkflowResponsivenessMonitorHelper willStartMonitoring]_block_invoke
- ___61-[STYWorkflowResponsivenessMonitorHelper willStartMonitoring]_block_invoke.410
- ___61-[STYWorkflowResponsivenessMonitorHelper willStartMonitoring]_block_invoke.413
- ___61-[STYWorkflowResponsivenessMonitorHelper willStartMonitoring]_block_invoke.414
- ___block_descriptor_32_e27_B24?0"NSURL"8"NSError"16l
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32s_e27_v16?0"WRSignpostTracker"8ls32l8
- ___block_descriptor_40_e8_32s_e30_v16?0"WRIntervalAndThreads"8ls32l8
- ___block_descriptor_40_e8_32s_e30_v16?0"WRTimestampAndThread"8ls32l8
- ___block_descriptor_48_e8_32s40s_e112_v48?0"WRWorkflowEventTracker"8"WRTimestampAndThread"16"WRTimestampAndThread"24"WRSignpost"32"WRSignpost"40ls32l8s40l8
- ___block_descriptor_52_e8_32s40s_e8_v12?0B8ls32l8s40l8
- ___block_literal_global.404
- ___block_literal_global.486
- ___block_literal_global.491
- ___block_literal_global.504
- ___block_literal_global.507
- ___block_literal_global.90
- ___cleanupWorkflowResponsivenessDirectory_block_invoke
- ___cleanupWorkflowResponsivenessDirectory_block_invoke.cold.1
- ___getTailspinReasonString_block_invoke
- ___getTailspinReasonString_block_invoke_2
- ___getTailspinReasonString_block_invoke_3
- ___makeWorkflowResponsivenessDirectory_block_invoke
- ___makeWorkflowResponsivenessDirectory_block_invoke.cold.1
- ___saveLogsForWorkflow_block_invoke
- ___saveLogsForWorkflow_block_invoke.cold.1
- ___saveLogsForWorkflow_block_invoke.cold.2
- ___saveLogsForWorkflow_block_invoke.cold.3
- ___saveLogsForWorkflow_block_invoke.cold.4
- ___timestamp_block_invoke
- ___workflowResponsivenessDirectory_block_invoke
- _close
- _dispatch_source_cancel
- _ffsctl
- _geteuid
- _makeWorkflowResponsivenessDirectory.onceToken
- _objc_msgSend$URLByAppendingPathComponent:
- _objc_msgSend$allSignpostTrackers
- _objc_msgSend$allSignposts
- _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
- _objc_msgSend$debugDescription
- _objc_msgSend$defaultManager
- _objc_msgSend$diagnosticThresholdCount
- _objc_msgSend$diagnosticThresholdIntervalSeconds
- _objc_msgSend$emits
- _objc_msgSend$end
- _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
- _objc_msgSend$environment
- _objc_msgSend$exceededDiagnosticThreshold
- _objc_msgSend$fileExistsAtPath:
- _objc_msgSend$fileSystemRepresentation
- _objc_msgSend$fileURLWithPath:
- _objc_msgSend$hasDiagnosticThresholdCount
- _objc_msgSend$hasDiagnosticThresholdInterval
- _objc_msgSend$hasOverallDiagnosticThresholdInterval
- _objc_msgSend$hasSuffix:
- _objc_msgSend$initWithFormat:
- _objc_msgSend$initWithWorkflow:eventCompletionCallback:
- _objc_msgSend$intervals
- _objc_msgSend$machContTimeNs
- _objc_msgSend$overallDiagnosticThresholdIntervalSeconds
- _objc_msgSend$path
- _objc_msgSend$perDayTimer
- _objc_msgSend$removeItemAtURL:error:
- _objc_msgSend$resetCounts
- _objc_msgSend$resourceValuesForKeys:error:
- _objc_msgSend$setPerDayTimer:
- _objc_msgSend$setPerPeriodTimer:
- _objc_msgSend$setWorkflowProvider:
- _objc_msgSend$signpost
- _objc_msgSend$start
- _objc_msgSend$stringFromDate:
- _objc_msgSend$threadID
- _objc_msgSend$timeIntervalSinceNow
- _objc_msgSend$timeUntilFirstSignpostNanoseconds
- _objc_msgSend$totalDurationNanoseconds
- _objc_msgSend$workflowEventCompleted:overallIntervalStart:overallIntervalEnd:startSignpost:endSignpost:
- _objc_retain_x27
- _open
- _tailspin_dump_output_with_options
- _timestamp.dateFormatter
- _timestamp.onceToken
- _workflowResponsivenessDirectory
- _workflowResponsivenessDirectory.onceToken
- _workflowResponsivenessDirectory.url
CStrings:
+ "%{public}@ already monitoring"
+ "%{public}@ already not monitoring"
+ "@\"NSUserDefaults\""
+ "App launch threshold enforced"
+ "Retrying"
+ "TB,V_enforceAppLaunchThreshold"
+ "The value of enforceAppLaunchThreshold default is %d"
+ "Workflow %{public}@ already exceeded limits (%d/%d per day, %d/%d per period), not reporting completed event"
+ "Workflow %{public}@ below limits (%d/%d per day, %d/%d per period)"
+ "Workflow %{public}@ event completed, diagnostics were kicked off"
+ "Workflow %{public}@ event completed, gathering diagnostics if needed"
+ "Workflow %{public}@ event completed, no diagnostics were needed"
+ "Workflow %{public}@ hit report limit (%d/%d per day, %d/%d per period), turning off signpost streaming"
+ "Workflow %{public}@ is above limit (%d/%d per day, %d/%d per period), not including in allowlist"
+ "Workflow %{public}@ is below limit (%d/%d per day, %d/%d per period), including in allowlist"
+ "Workflow %{public}@ resetting all counts (was %d/%d per day, %d/%d per period), still above limits"
+ "Workflow %{public}@ resetting all counts (was %d/%d per day, %d/%d per period), turning on signpost streaming"
+ "Workflow %{public}@ resetting all counts (was %d/%d per day, %d/%d per period), was already under limits"
+ "Workflow %{public}@ resetting all counts (was %d/%d per day, %d/%d per period), was already under limits, and is now above limit!"
+ "Workflow %{public}@ resetting per day counts (was %d/%d per day, %d/%d per period), still above limits"
+ "Workflow %{public}@ resetting per day counts (was %d/%d per day, %d/%d per period), turning on signpost streaming"
+ "Workflow %{public}@ resetting per day counts (was %d/%d per day, %d/%d per period), was already under limits"
+ "Workflow %{public}@ resetting per day counts (was %d/%d per day, %d/%d per period), was already under limits, and is now above limit!"
+ "Workflow %{public}@ resetting per period counts (was %d/%d per day, %d/%d per period), still above limits"
+ "Workflow %{public}@ resetting per period counts (was %d/%d per day, %d/%d per period), turning on signpost streaming"
+ "Workflow %{public}@ resetting per period counts (was %d/%d per day, %d/%d per period), was already under limits"
+ "Workflow %{public}@ resetting per period counts (was %d/%d per day, %d/%d per period), was already under limits, and is now above limit!"
+ "_defaults"
+ "_enforceAppLaunchThreshold"
+ "allowListForDiagnostics"
+ "cleanupWorkflowResponsivenessDiagnosticsDirectory"
+ "enforceAppLaunchThreshold"
+ "gatherDiagnosticsIfNeeded"
+ "initForLiveStreamingWithWorkflow:timeoutQueue:eventCompletionCallback:"
+ "setEnforceAppLaunchThreshold:"
+ "updateAllowList"
+ "v16@?0@\"WRWorkflowEventTracker\"8"
+ "workflowEventCompleted:completedWRTracker:"
+ "workflowIsUnderLimits:"
- "%@-%@.%@"
- "/private/var/db/WorkflowResponsiveness/"
- "Also failed to remove tailspin file: %@"
- "B24@?0@\"NSURL\"8@\"NSError\"16"
- "Failed to create tailspin reason string, unable to create UTF8 string from JSON: %@\n"
- "Failed to create tailspin reason string, unable to serialize tailspin reason into JSON: %@ - %@\n"
- "Failed to generate tailspin, could not open file %{public}@"
- "Failed to mark %{public}@ purgeable: %{errno}d"
- "Failed to save tailspin to file: %@"
- "Marked %{public}@ purgeable"
- "Removed %{public}@ successfully, but received error: %{public}@"
- "URLByAppendingPathComponent:"
- "Unable to create folder at %@: %@"
- "Unable to remove %{public}@: %{public}@"
- "WR cleanup: %@ is not a regular file"
- "WR cleanup: %@ is not a tailspin file"
- "WR cleanup: %{public}@ created at %{public}@, removing"
- "WR cleanup: %{public}@ created at %{public}@, skipping"
- "WR cleanup: Error cleaning up workflow responsiveness directory file %@: %@"
- "WR cleanup: No workflow responsiveness directory, no cleanup required"
- "WR cleanup: Unable to create enumerator to clean up workflow responsiveness directory"
- "WR cleanup: Unable to get info about %@"
- "WR cleanup: Unable to get path from %@"
- "Workflow %{public}@ did not exceed any diagnostic thresholds"
- "Workflow %{public}@ exceeded daily log limit (%d logs, %d limit), not reporting"
- "Workflow %{public}@ exceeded overall diagnostic interval threshold (%.3fs > %.3fs)"
- "Workflow %{public}@ exceeded per-period (%ds) log limit (%d logs, %d limit), not reporting"
- "Workflow %{public}@ resetting all counts (%d per day, %d per period)"
- "Workflow %{public}@ resetting per-day count (%d)"
- "Workflow %{public}@ resetting per-period count (%d)"
- "Workflow %{public}@ signpost %{public}@ exceeded diagnostic threshold (%.3fs > %.3fs or %d > %d)"
- "Workflow responsiveness delay detected in %@"
- "allSignpostTrackers"
- "allSignposts"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "debugDescription"
- "defaultManager"
- "diagnosticThresholdCount"
- "diagnosticThresholdIntervalSeconds"
- "emits"
- "end"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "environment"
- "exceededDiagnosticThreshold"
- "fileExistsAtPath:"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "hasDiagnosticThresholdCount"
- "hasDiagnosticThresholdInterval"
- "hasOverallDiagnosticThresholdInterval"
- "hasSuffix:"
- "initWithFormat:"
- "initWithWorkflow:eventCompletionCallback:"
- "intervals"
- "machContTimeNs"
- "must run as root to create directory /private/var/db/WorkflowResponsiveness/ (running as %d)"
- "overallDiagnosticThresholdIntervalSeconds"
- "path"
- "removeItemAtURL:error:"
- "resourceValuesForKeys:error:"
- "saved tailspin file %@ for slow workflow %{public}@"
- "signpost"
- "start"
- "stringFromDate:"
- "tailspin"
- "threadID"
- "timeIntervalSinceNow"
- "timeUntilFirstSignpostNanoseconds"
- "totalDurationNanoseconds"
- "v16@?0@\"WRIntervalAndThreads\"8"
- "v16@?0@\"WRSignpostTracker\"8"
- "v16@?0@\"WRTimestampAndThread\"8"
- "v48@?0@\"WRWorkflowEventTracker\"8@\"WRTimestampAndThread\"16@\"WRTimestampAndThread\"24@\"WRSignpost\"32@\"WRSignpost\"40"
- "workflowEventCompleted:overallIntervalStart:overallIntervalEnd:startSignpost:endSignpost:"
- "yyyy-MM-dd-HHmmss.SSS"

```
