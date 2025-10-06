## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`

```diff

-341.1.0.0.0
-  __TEXT.__text: 0x9238
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x3b4
-  __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0xf0
-  __TEXT.__cstring: 0x64f
-  __TEXT.__oslogstring: 0x1074
-  __TEXT.__unwind_info: 0x22c
-  __TEXT.__objc_classname: 0xcc
-  __TEXT.__objc_methname: 0xe6e
-  __TEXT.__objc_methtype: 0x1a7
-  __TEXT.__objc_stubs: 0xb20
-  __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x270
-  __DATA_CONST.__objc_classlist: 0x48
+357.0.0.0.0
+  __TEXT.__text: 0x21bf0
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x6e0
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x820
+  __TEXT.__cstring: 0x1e7f
+  __TEXT.__oslogstring: 0x39d0
+  __TEXT.__unwind_info: 0x4a4
+  __TEXT.__objc_classname: 0x115
+  __TEXT.__objc_methname: 0x21cc
+  __TEXT.__objc_methtype: 0x25f
+  __TEXT.__objc_stubs: 0x1a60
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0x580
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x998
-  __DATA_CONST.__objc_selrefs: 0x360
-  __AUTH_CONST.__objc_const: 0x318
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0x238
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0xa8
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0xa4
+  __DATA_CONST.__objc_const: 0x1180
+  __DATA_CONST.__objc_selrefs: 0x788
+  __DATA_CONST.__objc_classrefs: 0x118
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_arraydata: 0x18
+  __AUTH_CONST.__cfstring: 0x1ce0
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__objc_const: 0x3f0
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x128
+  __DATA.__data: 0xc0
+  __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport
+  - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A94F0C1B-3C15-3D71-B2D1-949CB8D4F484
-  Functions: 175
-  Symbols:   689
-  CStrings:  399
+  - /usr/lib/libspindump.dylib
+  - /usr/lib/libtailspin.dylib
+  UUID: ECCBF567-0BF0-3501-A506-14BAB2A86969
+  Functions: 439
+  Symbols:   1547
+  CStrings:  1127
 
Symbols:
+ +[WRDiagnostic diagnosticsForWorkflowName:signpostName:diagnosticDicts:diagnosticsEnabled:checkForOverrides:error:]
+ +[WRDiagnostic diagnosticsWithDict:backupName:error:]
+ +[WRWorkflow allWorkflows].cold.1
+ +[WRWorkflow diagnosticsEnabled].cold.1
+ +[WRWorkflow makeOverridePlistDirectoryWithError:]
+ +[WRWorkflow overridePlistDirectory]
+ +[WRWorkflow telemetryEnabled].cold.1
+ +[WRWorkflow workflowWithName:].cold.1
+ +[WRWorkflow workflowWithName:].cold.2
+ +[WRWorkflow workflowWithPlist:checkForOverrides:error:]
+ +[WRWorkflowEventTracker cleanupWorkflowResponsivenessDiagnosticsDirectory]
+ +[WRWorkflowEventTracker cleanupWorkflowResponsivenessDiagnosticsDirectory].cold.1
+ +[WRWorkflowEventTracker cleanupWorkflowResponsivenessDiagnosticsDirectory].cold.2
+ +[WRWorkflowEventTracker cleanupWorkflowResponsivenessDiagnosticsDirectory].cold.3
+ +[WRWorkflowEventTracker isReservedSignpostName:]
+ +[WRWorkflowEventTracker isReservedWorkflowName:]
+ +[WRWorkflowEventTracker makeWorkflowResponsivenessDirectory]
+ +[WRWorkflowEventTracker workflowResponsivenessDirectory]
+ -[WRDiagnostic .cxx_destruct]
+ -[WRDiagnostic applyDict:error:]
+ -[WRDiagnostic copyWithZone:]
+ -[WRDiagnostic debugDescription]
+ -[WRDiagnostic encodedDict]
+ -[WRDiagnostic gatherTailspin]
+ -[WRDiagnostic hasAnySpindumpReports]
+ -[WRDiagnostic hasTriggerThresholdCount]
+ -[WRDiagnostic hasTriggerThresholdDurationSingle]
+ -[WRDiagnostic hasTriggerThresholdDurationSum]
+ -[WRDiagnostic hasTriggerThresholdDurationUnion]
+ -[WRDiagnostic hash]
+ -[WRDiagnostic initWithDict:backupName:error:]
+ -[WRDiagnostic initWithEncodedDict:error:]
+ -[WRDiagnostic isEqual:]
+ -[WRDiagnostic isValidForSignpost]
+ -[WRDiagnostic isValidForWorkflow]
+ -[WRDiagnostic name]
+ -[WRDiagnostic reportOmittingNetworkBoundIntervals]
+ -[WRDiagnostic reportOtherSignpostWithName]
+ -[WRDiagnostic reportProcessesWithName]
+ -[WRDiagnostic reportSpindumpForDispatchQueueWithLabel]
+ -[WRDiagnostic reportSpindumpForMainThread]
+ -[WRDiagnostic reportSpindumpForThisDispatchQueue]
+ -[WRDiagnostic reportSpindumpForThisThread]
+ -[WRDiagnostic reportSpindumpForThreadWithName]
+ -[WRDiagnostic tailspinIncludeOSLogs]
+ -[WRDiagnostic triggerEventTimeout]
+ -[WRDiagnostic triggerThresholdCount]
+ -[WRDiagnostic triggerThresholdDurationSingle]
+ -[WRDiagnostic triggerThresholdDurationSum]
+ -[WRDiagnostic triggerThresholdDurationUnion]
+ -[WRDiagnostic validate]
+ -[WRIntervalAndThreads encodedDict]
+ -[WRIntervalAndThreads initWithEncodedDict:error:]
+ -[WRIntervalAndThreads insertIntoSortedArray:]
+ -[WROpenIndividuatedSignpostInterval .cxx_destruct]
+ -[WROpenIndividuatedSignpostInterval individuationIdentifier]
+ -[WROpenIndividuatedSignpostInterval initWithSignpost:individuationIdentifier:timestampAndThread:]
+ -[WROpenIndividuatedSignpostInterval signpost]
+ -[WROpenIndividuatedSignpostInterval timestampAndThread]
+ -[WRSignpost diagnostics]
+ -[WRSignpost eventIdentifierFieldName]
+ -[WRSignpost hasDiagnosticThresholdIntervalSeconds]
+ -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:diagnostics:]
+ -[WRSignpost networkBound]
+ -[WRSignpostTracker diagnosticsExceedingThresholdsWithEventStartNs:eventEndNs:]
+ -[WRSignpostTracker encodedDict]
+ -[WRSignpostTracker incompleteIntervalStartsMutable]
+ -[WRSignpostTracker incompleteIntervalStarts]
+ -[WRSignpostTracker initWithEncodedDict:signpost:error:]
+ -[WRSignpostTracker setIncompleteIntervalStartsMutable:]
+ -[WRSignpostTracker statsWithEventEndNs:]
+ -[WRTimestampAndThread .cxx_destruct]
+ -[WRTimestampAndThread date]
+ -[WRTimestampAndThread encodedDict]
+ -[WRTimestampAndThread initWithEncodedDict:error:]
+ -[WRTimestampAndThread initWithThreadID:machContTimeNs:date:]
+ -[WRTimestampAndThread insertIntoSortedArray:]
+ -[WRWorkflow allowListForAllSignposts]
+ -[WRWorkflow allowListForDiagnostics]
+ -[WRWorkflow compare:]
+ -[WRWorkflow encodedDict]
+ -[WRWorkflow hasMaximumEventDuration]
+ -[WRWorkflow initWithEncodedDict:error:]
+ -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]
+ -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:].cold.1
+ -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:].cold.2
+ -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:].cold.3
+ -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:].cold.4
+ -[WRWorkflow maximumEventDuration]
+ -[WRWorkflow workflowDiagnostics]
+ -[WRWorkflow workflowSupportsConcurrentEvents]
+ -[WRWorkflow wrsignpostWithName:]
+ -[WRWorkflowEventTracker applySignpost:toSignpostTracker:].cold.2
+ -[WRWorkflowEventTracker applySignpost:toSignpostTracker:].cold.3
+ -[WRWorkflowEventTracker applySignpost:toSignpostTracker:].cold.4
+ -[WRWorkflowEventTracker concurrentEvents]
+ -[WRWorkflowEventTracker diagnosticsExceedingThresholds]
+ -[WRWorkflowEventTracker doneHandlingSignpostsWithEndTimeMachContNs:]
+ -[WRWorkflowEventTracker encodedDict]
+ -[WRWorkflowEventTracker encodedDict].cold.1
+ -[WRWorkflowEventTracker encodedDict].cold.2
+ -[WRWorkflowEventTracker encodedStringWithError:]
+ -[WRWorkflowEventTracker endSignpost]
+ -[WRWorkflowEventTracker error]
+ -[WRWorkflowEventTracker eventEnd]
+ -[WRWorkflowEventTracker eventIdentifierForSignpostObject:eventFieldName:]
+ -[WRWorkflowEventTracker eventIdentifier]
+ -[WRWorkflowEventTracker eventStart]
+ -[WRWorkflowEventTracker fillInNonDiagnosticSignpost:]
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded]
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.1
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.10
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.11
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.12
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.13
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.14
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.15
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.16
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.2
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.3
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.4
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.5
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.6
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.7
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.8
+ -[WRWorkflowEventTracker gatherDiagnosticsIfNeeded].cold.9
+ -[WRWorkflowEventTracker generateTelemetry]
+ -[WRWorkflowEventTracker generateTelemetry].cold.1
+ -[WRWorkflowEventTracker generateTelemetry].cold.2
+ -[WRWorkflowEventTracker handleError:atEndTime:]
+ -[WRWorkflowEventTracker handleSignpost:].cold.4
+ -[WRWorkflowEventTracker handleSignpost:].cold.5
+ -[WRWorkflowEventTracker handleSignpost:].cold.6
+ -[WRWorkflowEventTracker handleSignpost:].cold.7
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:]
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.1
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.2
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.3
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.4
+ -[WRWorkflowEventTracker haveAnyEndSignpostsWithIndividuationFieldName:]
+ -[WRWorkflowEventTracker initForLiveStreamingWithWorkflow:timeoutQueue:eventCompletionCallback:]
+ -[WRWorkflowEventTracker initForReadbackWithWorkflow:eventCompletionCallback:]
+ -[WRWorkflowEventTracker initWithEncodedData:error:]
+ -[WRWorkflowEventTracker initWithEncodedDict:error:]
+ -[WRWorkflowEventTracker initWithEncodedString:error:]
+ -[WRWorkflowEventTracker initWithSpindump:error:]
+ -[WRWorkflowEventTracker initWithTailspin:error:]
+ -[WRWorkflowEventTracker initWithWorkflow:]
+ -[WRWorkflowEventTracker newConcurrentEventWithIdentifier:]
+ -[WRWorkflowEventTracker numHandledSignposts]
+ -[WRWorkflowEventTracker numOutsideSignposts]
+ -[WRWorkflowEventTracker numUnhandledSignposts]
+ -[WRWorkflowEventTracker openIndividuatedIntervalsWithFieldNameMatchingAnEndSignpostFromBeforeEventStart]
+ -[WRWorkflowEventTracker reportCoreAnalyticsEventForSignpost:allCount:allDurationUnionSec:allDurationSumSec:allDurationLongestSec:allDurationUntrackedSec:allDurationNonNetworkBoundSec:allTimeUntilFirstSignpost:allTimeAfterLastSignpost:incompleteCount:completeDurationUnionSec:completeDurationSumSec:completeDurationLongestSec:completeTimeUntilFirstSignpost:environment:]
+ -[WRWorkflowEventTracker reportCoreAnalyticsEventForSignpost:allCount:allDurationUnionSec:allDurationSumSec:allDurationLongestSec:allDurationUntrackedSec:allDurationNonNetworkBoundSec:allTimeUntilFirstSignpost:allTimeAfterLastSignpost:incompleteCount:completeDurationUnionSec:completeDurationSumSec:completeDurationLongestSec:completeTimeUntilFirstSignpost:environment:].cold.1
+ -[WRWorkflowEventTracker reportCoreAnalyticsEventForSignpost:allCount:allDurationUnionSec:allDurationSumSec:allDurationLongestSec:allDurationUntrackedSec:allDurationNonNetworkBoundSec:allTimeUntilFirstSignpost:allTimeAfterLastSignpost:incompleteCount:completeDurationUnionSec:completeDurationSumSec:completeDurationLongestSec:completeTimeUntilFirstSignpost:environment:].cold.2
+ -[WRWorkflowEventTracker reportErrorsAndResetAtTime:date:]
+ -[WRWorkflowEventTracker reportErrorsAndResetAtTime:date:].cold.1
+ -[WRWorkflowEventTracker reportErrorsAndResetAtTime:date:].cold.2
+ -[WRWorkflowEventTracker resetWithoutReportingErrors]
+ -[WRWorkflowEventTracker sawIndividuationFieldName:withIndividuationIdentifier:]
+ -[WRWorkflowEventTracker setConcurrentEvents:]
+ -[WRWorkflowEventTracker setEndSignpost:]
+ -[WRWorkflowEventTracker setError:]
+ -[WRWorkflowEventTracker setEventEnd:]
+ -[WRWorkflowEventTracker setEventIdentifier:]
+ -[WRWorkflowEventTracker setEventStart:]
+ -[WRWorkflowEventTracker setOpenIndividuatedIntervalsWithFieldNameMatchingAnEndSignpostFromBeforeEventStart:]
+ -[WRWorkflowEventTracker setTimeoutQueue:]
+ -[WRWorkflowEventTracker setTimeoutSource:]
+ -[WRWorkflowEventTracker stats]
+ -[WRWorkflowEventTracker timeoutQueue]
+ -[WRWorkflowEventTracker timeoutSource]
+ -[WRWorkflowEventTracker valueForFieldName:inSignpostEvent:]
+ -[WRWorkflowEventTracker valueForFieldName:inSignpostObject:]
+ -[WRWorkflowEventTracker valueForFieldName:inSignpostObject:].cold.1
+ -[WRWorkflowEventTracker valueForFieldName:inSignpostObject:].cold.2
+ -[WRWorkflowProvider handleSettingsChanged:]
+ -[WRWorkflowProvider handleSettingsChanged:].cold.1
+ -[WRWorkflowProvider registerNotification].cold.2
+ -[WRWorkflowProvider taskingNotifyToken]
+ -[WRWorkflowProvider wrSettingsChangedNotifyToken]
+ -[WRWorkflowProviderAllWorkflows handleSettingsChanged:]
+ -[WRWorkflowProviderAllWorkflows handleSettingsChanged:].cold.1
+ -[WRWorkflowProviderSingleWorkflow handleSettingsChanged:]
+ -[WRWorkflowProviderSingleWorkflow handleSettingsChanged:].cold.1
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table12
+ GCC_except_table123
+ GCC_except_table13
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table8
+ GCC_except_table9
+ GCC_except_table93
+ _AllDiagnosticKeys
+ _AllDiagnosticKeys.allDiagnosticKeys
+ _AllDiagnosticKeys.onceToken
+ _AllSignpostKeys
+ _AllSignpostKeys.allSignpostKeys
+ _AllSignpostKeys.onceToken
+ _AllWorkflowKeys
+ _AllWorkflowKeys.allWorkflowKeys
+ _AllWorkflowKeys.onceToken
+ _AnalyticsSendEvent
+ _DictGetDict
+ _DictGetType
+ _NSCocoaErrorDomain
+ _NSDebugDescriptionErrorKey
+ _NSFilePosixPermissions
+ _NSFileTypeRegular
+ _NSPOSIXErrorDomain
+ _NSStringFromClass
+ _NSURLCreationDateKey
+ _NSURLIsRegularFileKey
+ _NSURLNameKey
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_SignpostSupportObjectExtractor
+ _OBJC_CLASS_$_WRDiagnostic
+ _OBJC_CLASS_$_WROpenIndividuatedSignpostInterval
+ _OBJC_IVAR_$_WRDiagnostic._gatherTailspin
+ _OBJC_IVAR_$_WRDiagnostic._name
+ _OBJC_IVAR_$_WRDiagnostic._reportOmittingNetworkBoundIntervals
+ _OBJC_IVAR_$_WRDiagnostic._reportOtherSignpostWithName
+ _OBJC_IVAR_$_WRDiagnostic._reportProcessesWithName
+ _OBJC_IVAR_$_WRDiagnostic._reportSpindumpForDispatchQueueWithLabel
+ _OBJC_IVAR_$_WRDiagnostic._reportSpindumpForMainThread
+ _OBJC_IVAR_$_WRDiagnostic._reportSpindumpForThisDispatchQueue
+ _OBJC_IVAR_$_WRDiagnostic._reportSpindumpForThisThread
+ _OBJC_IVAR_$_WRDiagnostic._reportSpindumpForThreadWithName
+ _OBJC_IVAR_$_WRDiagnostic._tailspinIncludeOSLogs
+ _OBJC_IVAR_$_WRDiagnostic._triggerEventTimeout
+ _OBJC_IVAR_$_WRDiagnostic._triggerThresholdCount
+ _OBJC_IVAR_$_WRDiagnostic._triggerThresholdDurationSingle
+ _OBJC_IVAR_$_WRDiagnostic._triggerThresholdDurationSum
+ _OBJC_IVAR_$_WRDiagnostic._triggerThresholdDurationUnion
+ _OBJC_IVAR_$_WROpenIndividuatedSignpostInterval._individuationIdentifier
+ _OBJC_IVAR_$_WROpenIndividuatedSignpostInterval._signpost
+ _OBJC_IVAR_$_WROpenIndividuatedSignpostInterval._timestampAndThread
+ _OBJC_IVAR_$_WRSignpost._diagnostics
+ _OBJC_IVAR_$_WRSignpost._eventIdentifierFieldName
+ _OBJC_IVAR_$_WRSignpost._hasDiagnosticThresholdInterval
+ _OBJC_IVAR_$_WRSignpost._networkBound
+ _OBJC_IVAR_$_WRSignpostTracker._incompleteIntervalStartsMutable
+ _OBJC_IVAR_$_WRTimestampAndThread._date
+ _OBJC_IVAR_$_WRWorkflow._allowListForAllSignposts
+ _OBJC_IVAR_$_WRWorkflow._allowListForDiagnostics
+ _OBJC_IVAR_$_WRWorkflow._maximumEventDuration
+ _OBJC_IVAR_$_WRWorkflow._workflowDiagnostics
+ _OBJC_IVAR_$_WRWorkflow._workflowSupportsConcurrentEvents
+ _OBJC_IVAR_$_WRWorkflowEventTracker._concurrentEvents
+ _OBJC_IVAR_$_WRWorkflowEventTracker._endSignpost
+ _OBJC_IVAR_$_WRWorkflowEventTracker._error
+ _OBJC_IVAR_$_WRWorkflowEventTracker._eventEnd
+ _OBJC_IVAR_$_WRWorkflowEventTracker._eventIdentifier
+ _OBJC_IVAR_$_WRWorkflowEventTracker._eventStart
+ _OBJC_IVAR_$_WRWorkflowEventTracker._numHandledSignposts
+ _OBJC_IVAR_$_WRWorkflowEventTracker._numOutsideSignposts
+ _OBJC_IVAR_$_WRWorkflowEventTracker._numUnhandledSignposts
+ _OBJC_IVAR_$_WRWorkflowEventTracker._openIndividuatedIntervalsWithFieldNameMatchingAnEndSignpostFromBeforeEventStart
+ _OBJC_IVAR_$_WRWorkflowEventTracker._timeoutQueue
+ _OBJC_IVAR_$_WRWorkflowEventTracker._timeoutSource
+ _OBJC_IVAR_$_WRWorkflowProvider._taskingNotifyToken
+ _OBJC_IVAR_$_WRWorkflowProvider._wrSettingsChangedNotifyToken
+ _OBJC_METACLASS_$_WRDiagnostic
+ _OBJC_METACLASS_$_WROpenIndividuatedSignpostInterval
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _SPReportWorkflowResponsivenessDelay
+ _TSPDumpOptions_CollectOsLogs
+ _TSPDumpOptions_CollectOsSignposts
+ _TSPDumpOptions_MinTimestamp
+ _TSPDumpOptions_NoSymbolicate
+ _TSPDumpOptions_ReasonString
+ _TSPDumpOptions_ScrubOutput
+ _WRCheckForBadDiagnosticDict
+ _WRCheckForBadSignpostDict
+ _WRCheckForBadWorkflowDict
+ _WRCreateOSTransaction
+ _WRDiagnosticGatherTailspinKey
+ _WRDiagnosticNameKey
+ _WRDiagnosticOptionReportOmitNetworkBoundIntervalsKey
+ _WRDiagnosticOptionReportOtherSignpostWithNameKey
+ _WRDiagnosticOptionReportProcessesWithNameKey
+ _WRDiagnosticOptionTailspinIncludesOSLogsKey
+ _WRDiagnosticReportSpindumpForDispatchQueueWithLabelKey
+ _WRDiagnosticReportSpindumpForMainThreadKey
+ _WRDiagnosticReportSpindumpForThisDispatchQueueKey
+ _WRDiagnosticReportSpindumpForThisThreadKey
+ _WRDiagnosticReportSpindumpForThreadWithNameKey
+ _WRDiagnosticTriggerEventTimeoutKey
+ _WRDiagnosticTriggerThresholdCountKey
+ _WRDiagnosticTriggerThresholdDurationSingleKey
+ _WRDiagnosticTriggerThresholdDurationSumKey
+ _WRDiagnosticTriggerThresholdDurationUnionKey
+ _WRErrorDomain
+ _WRIsAppleInternal
+ _WRIsAppleInternal.appleInternal
+ _WRIsAppleInternal.onceToken
+ _WRIsDisabledWorkflow
+ _WRIsDisabledWorkflow.cold.1
+ _WRMachTimeFromNanosecondsUsingLiveTimebase
+ _WRMachTimebaseForLiveMachine.once
+ _WRMachTimebaseForLiveMachine.timebase
+ _WRMakeError
+ _WRMakeErrorWithUnderlyingError
+ _WROverrideDiagnosticForSignpost
+ _WROverrideDiagnosticForWorkflow
+ _WROverrideDiagnosticsEnablement
+ _WROverrideDiagnosticsEnablementForWorkflow
+ _WROverrideForSignpost
+ _WROverrideForWorkflow
+ _WROverrideNewSignpostsForWorkflow
+ _WROverrideNewWorkflows
+ _WROverrideTelemetryEnablement
+ _WROverrideTelemetryEnablementForWorkflow
+ _WRRangesSortAndCoalesce
+ _WRSanitizeForCA
+ _WRSanitizeForCA.onceToken
+ _WRSanitizeForCA.removedCharacters
+ _WRSignpostDiagnosticsKey
+ _WRSignpostEventIdentifierFieldNameKey
+ _WRSignpostNetworkBoundKey
+ _WRStringForDate.dateFormatter
+ _WRStringForDate.onceToken
+ _WRTaskingNumberForKey
+ _WRTaskingStringForKey
+ _WRTaskingValueForKeyOfType
+ _WRValidateBool
+ _WRValidateDouble
+ _WRValidateSignpostDictLeafEntry
+ _WRValidateString
+ _WRWorkflowDiagnosticsKey
+ _WRWorkflowMaximumDurationKey
+ __OBJC_$_CLASS_METHODS_WRWorkflowEventTracker
+ __OBJC_$_INSTANCE_METHODS_WRDiagnostic
+ __OBJC_$_INSTANCE_METHODS_WROpenIndividuatedSignpostInterval
+ __OBJC_$_INSTANCE_VARIABLES_WRDiagnostic
+ __OBJC_$_INSTANCE_VARIABLES_WROpenIndividuatedSignpostInterval
+ __OBJC_$_PROP_LIST_WRDiagnostic
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WRDictEncoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WRDictEncoding
+ __OBJC_CLASS_PROTOCOLS_$_WRDiagnostic
+ __OBJC_CLASS_PROTOCOLS_$_WRWorkflow
+ __OBJC_CLASS_RO_$_WRDiagnostic
+ __OBJC_CLASS_RO_$_WROpenIndividuatedSignpostInterval
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_WRDictEncoding
+ __OBJC_METACLASS_RO_$_WRDiagnostic
+ __OBJC_METACLASS_RO_$_WROpenIndividuatedSignpostInterval
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_WRDictEncoding
+ __WROverrideDiagnostics
+ __WROverrideDict
+ ___115+[WRDiagnostic diagnosticsForWorkflowName:signpostName:diagnosticDicts:diagnosticsEnabled:checkForOverrides:error:]_block_invoke
+ ___26+[WRWorkflow allWorkflows]_block_invoke.cold.1
+ ___26+[WRWorkflow allWorkflows]_block_invoke.cold.2
+ ___26+[WRWorkflow allWorkflows]_block_invoke.cold.3
+ ___26+[WRWorkflow allWorkflows]_block_invoke.cold.4
+ ___31+[WRWorkflow workflowWithName:]_block_invoke
+ ___31+[WRWorkflow workflowWithName:]_block_invoke.cold.1
+ ___31+[WRWorkflow workflowWithName:]_block_invoke.cold.2
+ ___31+[WRWorkflow workflowWithName:]_block_invoke.cold.3
+ ___31+[WRWorkflow workflowWithName:]_block_invoke.cold.4
+ ___370-[WRWorkflowEventTracker reportCoreAnalyticsEventForSignpost:allCount:allDurationUnionSec:allDurationSumSec:allDurationLongestSec:allDurationUntrackedSec:allDurationNonNetworkBoundSec:allTimeUntilFirstSignpost:allTimeAfterLastSignpost:incompleteCount:completeDurationUnionSec:completeDurationSumSec:completeDurationLongestSec:completeTimeUntilFirstSignpost:environment:]_block_invoke
+ ___42-[WRWorkflowProvider registerNotification]_block_invoke.180
+ ___42-[WRWorkflowProvider registerNotification]_block_invoke.180.cold.1
+ ___42-[WRWorkflowProvider registerNotification]_block_invoke.cold.1
+ ___43-[WRWorkflowEventTracker generateTelemetry]_block_invoke
+ ___43-[WRWorkflowEventTracker generateTelemetry]_block_invoke.cold.1
+ ___43-[WRWorkflowEventTracker generateTelemetry]_block_invoke.cold.2
+ ___46-[WRIntervalAndThreads insertIntoSortedArray:]_block_invoke
+ ___46-[WRTimestampAndThread insertIntoSortedArray:]_block_invoke
+ ___49-[WRWorkflowEventTracker initWithTailspin:error:]_block_invoke
+ ___49-[WRWorkflowEventTracker initWithTailspin:error:]_block_invoke_2
+ ___51-[WRWorkflowEventTracker gatherDiagnosticsIfNeeded]_block_invoke
+ ___51-[WRWorkflowEventTracker gatherDiagnosticsIfNeeded]_block_invoke.cold.1
+ ___51-[WRWorkflowEventTracker gatherDiagnosticsIfNeeded]_block_invoke.cold.2
+ ___51-[WRWorkflowEventTracker gatherDiagnosticsIfNeeded]_block_invoke.cold.3
+ ___51-[WRWorkflowEventTracker gatherDiagnosticsIfNeeded]_block_invoke.cold.4
+ ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke
+ ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.189
+ ___52-[WRWorkflowEventTracker initWithEncodedDict:error:]_block_invoke
+ ___56-[WRSignpostTracker initWithEncodedDict:signpost:error:]_block_invoke
+ ___56-[WRWorkflowProviderAllWorkflows handleSettingsChanged:]_block_invoke
+ ___57+[WRWorkflowEventTracker workflowResponsivenessDirectory]_block_invoke
+ ___58-[WRWorkflowProviderSingleWorkflow handleSettingsChanged:]_block_invoke
+ ___61+[WRWorkflowEventTracker makeWorkflowResponsivenessDirectory]_block_invoke
+ ___61+[WRWorkflowEventTracker makeWorkflowResponsivenessDirectory]_block_invoke.cold.1
+ ___61+[WRWorkflowEventTracker makeWorkflowResponsivenessDirectory]_block_invoke.cold.2
+ ___61+[WRWorkflowEventTracker makeWorkflowResponsivenessDirectory]_block_invoke.cold.3
+ ___67-[WRWorkflowEventTracker initWithWorkflow:eventCompletionCallback:]_block_invoke
+ ___75+[WRWorkflowEventTracker cleanupWorkflowResponsivenessDiagnosticsDirectory]_block_invoke
+ ___75+[WRWorkflowEventTracker cleanupWorkflowResponsivenessDiagnosticsDirectory]_block_invoke.cold.1
+ ___88-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]_block_invoke
+ ___88-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]_block_invoke.76
+ ___88-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]_block_invoke_2
+ ___AllDiagnosticKeys_block_invoke
+ ___AllSignpostKeys_block_invoke
+ ___AllWorkflowKeys_block_invoke
+ ___WRCheckForBadDiagnosticDict_block_invoke
+ ___WRCheckForBadSignpostDict_block_invoke
+ ___WRCheckForBadSignpostDict_block_invoke.cold.1
+ ___WRCheckForBadWorkflowDict_block_invoke
+ ___WRCheckForBadWorkflowDict_block_invoke.cold.1
+ ___WRIsAppleInternal_block_invoke
+ ___WRMachTimebaseForLiveMachine_block_invoke
+ ___WRRangesSortAndCoalesce_block_invoke
+ ___WRSanitizeForCA_block_invoke
+ ___WRStringForDate_block_invoke
+ ___block_descriptor_114_e8_32s40s48s56s64s72s80r88r96r104r_e48_"NSError"24?0"NSDictionary"8"NSDictionary"16lr80l8s32l8r88l8s40l8r96l8s48l8s56l8r104l8s64l8s72l8
+ ___block_descriptor_32_e15_i24?0r^v8r^v16l
+ ___block_descriptor_32_e27_B24?0"NSURL"8"NSError"16l
+ ___block_descriptor_32_e39_q24?0"WRDiagnostic"8"WRDiagnostic"16l
+ ___block_descriptor_32_e55_q24?0"WRIntervalAndThreads"8"WRIntervalAndThreads"16l
+ ___block_descriptor_32_e55_q24?0"WRTimestampAndThread"8"WRTimestampAndThread"16l
+ ___block_descriptor_40_e8_32bs_e32_v16?0"WRWorkflowEventTracker"8ls32l8
+ ___block_descriptor_40_e8_32r_e15_v32?0816^B24lr32l8
+ ___block_descriptor_40_e8_32r_e23_B16?0^{ktrace_chunk=}8lr32l8
+ ___block_descriptor_40_e8_32s_e24_B16?0"SignpostObject"8ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_50_e8_32s40r_e27_"WRWorkflow"16?0"NSURL"8ls32l8r40l8
+ ___block_descriptor_50_e8_32s40s_e15_v16?0"NSURL"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e34_v32?0"NSString"8"NSArray"16^B24lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s_e27_v16?0"WRSignpostTracker"8ls32l8
+ ___block_descriptor_60_e8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e25_v32?0"NSString"816^B24lr56l8s32l8s40l8s48l8
+ ___block_literal_global.11
+ ___block_literal_global.195
+ ___block_literal_global.201
+ ___block_literal_global.207
+ ___block_literal_global.344
+ ___block_literal_global.493
+ ___block_literal_global.499
+ ___block_literal_global.502
+ ___block_literal_global.62
+ ___block_literal_global.91
+ ___block_literal_global.93
+ ___kCFBooleanTrue
+ ___udivti3
+ __dispatch_source_type_timer
+ __unnamed_array_storage
+ __unnamed_array_storage.8
+ _close
+ _dispatch_activate
+ _dispatch_get_global_queue
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _fclose
+ _fdopen
+ _ffsctl
+ _fgets
+ _fread
+ _free
+ _fstat
+ _ftell
+ _geteuid
+ _ktrace_chunk_map_data
+ _ktrace_chunk_size
+ _ktrace_chunk_tag
+ _ktrace_chunk_unmap_data
+ _ktrace_chunk_version_major
+ _ktrace_config_create
+ _ktrace_config_destroy
+ _ktrace_config_get_reason
+ _ktrace_file_close
+ _ktrace_file_iterate
+ _ktrace_file_open
+ _mach_get_times
+ _mach_timebase_info
+ _makeWorkflowResponsivenessDirectory.onceToken
+ _malloc_type_malloc
+ _memmove
+ _mergesort_b
+ _objc_autorelease
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$UTF8String
+ _objc_msgSend$addCharactersInString:
+ _objc_msgSend$allKeys
+ _objc_msgSend$allSignpostTrackers
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$allowListForAllSignposts
+ _objc_msgSend$allowListForDiagnostics
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$beginDate
+ _objc_msgSend$cleanupWorkflowResponsivenessDiagnosticsDirectory
+ _objc_msgSend$code
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$date
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$description
+ _objc_msgSend$diagnostics
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$domain
+ _objc_msgSend$emits
+ _objc_msgSend$encodedDict
+ _objc_msgSend$encodedStringWithError:
+ _objc_msgSend$end
+ _objc_msgSend$endDate
+ _objc_msgSend$endSignpost
+ _objc_msgSend$error
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$eventEnd
+ _objc_msgSend$eventIdentifier
+ _objc_msgSend$eventIdentifierFieldName
+ _objc_msgSend$eventStart
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileSize
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$fileType
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$gatherTailspin
+ _objc_msgSend$handleSettingsChanged:
+ _objc_msgSend$hasMaximumEventDuration
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hasTriggerThresholdCount
+ _objc_msgSend$hasTriggerThresholdDurationSingle
+ _objc_msgSend$hasTriggerThresholdDurationSum
+ _objc_msgSend$hasTriggerThresholdDurationUnion
+ _objc_msgSend$incompleteIntervalStarts
+ _objc_msgSend$indexOfObject:inSortedRange:options:usingComparator:
+ _objc_msgSend$init
+ _objc_msgSend$initForLiveStreamingWithWorkflow:timeoutQueue:eventCompletionCallback:
+ _objc_msgSend$initForReadbackWithWorkflow:eventCompletionCallback:
+ _objc_msgSend$initWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithEncodedDict:error:
+ _objc_msgSend$initWithEncodedString:error:
+ _objc_msgSend$initWithFormat:arguments:
+ _objc_msgSend$initWithObjectsAndKeys:
+ _objc_msgSend$initWithPattern:options:error:
+ _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:diagnostics:
+ _objc_msgSend$initWithTimeIntervalSince1970:
+ _objc_msgSend$initWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$integerValue
+ _objc_msgSend$intervals
+ _objc_msgSend$invert
+ _objc_msgSend$invertedSet
+ _objc_msgSend$longLongValue
+ _objc_msgSend$maximumEventDuration
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$networkBound
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$overridePlistDirectory
+ _objc_msgSend$overridesBeginTime
+ _objc_msgSend$overridesEndTime
+ _objc_msgSend$passesSubsystem:category:
+ _objc_msgSend$path
+ _objc_msgSend$processTraceFileWithPath:startDate:endDate:errorOut:
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$removeObjectIdenticalTo:
+ _objc_msgSend$reportOmittingNetworkBoundIntervals
+ _objc_msgSend$reportOtherSignpostWithName
+ _objc_msgSend$reportProcessesWithName
+ _objc_msgSend$reportSpindumpForDispatchQueueWithLabel
+ _objc_msgSend$reportSpindumpForMainThread
+ _objc_msgSend$reportSpindumpForThisDispatchQueue
+ _objc_msgSend$reportSpindumpForThisThread
+ _objc_msgSend$reportSpindumpForThreadWithName
+ _objc_msgSend$resourceValuesForKeys:error:
+ _objc_msgSend$setBeginEventProcessingBlock:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setEmitEventProcessingBlock:
+ _objc_msgSend$setIntervalCompletionProcessingBlock:
+ _objc_msgSend$setSubsystemCategoryFilter:
+ _objc_msgSend$start
+ _objc_msgSend$startSignpost
+ _objc_msgSend$stats
+ _objc_msgSend$statsWithEventEndNs:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$tailspinIncludeOSLogs
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$timeRecordedNanoseconds
+ _objc_msgSend$triggerEventTimeout
+ _objc_msgSend$triggerThresholdCount
+ _objc_msgSend$triggerThresholdDurationSingle
+ _objc_msgSend$triggerThresholdDurationSum
+ _objc_msgSend$triggerThresholdDurationUnion
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$userInfo
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _objc_msgSend$workflowDiagnostics
+ _objc_msgSend$workflowSupportsConcurrentEvents
+ _objc_retainAutorelease
+ _open
+ _os_transaction_create
+ _reallocf
+ _strncmp
+ _tailspin_currently_running
+ _tailspin_dump_output_with_options
+ _vsnprintf
+ _workflowResponsivenessDirectory.onceToken
+ _workflowResponsivenessDirectory.url
- +[WRWorkflow _taskingValueForKey:type:]
- +[WRWorkflow _taskingValueForKey:type:].cold.1
- +[WRWorkflow overrideDiagnosticThresholdCountForWorkflow:subsystem:category:signpostName:]
- +[WRWorkflow overrideDiagnosticThresholdIntervalSecondsForWorkflow:subsystem:category:signpostName:]
- +[WRWorkflow overrideDiagnosticsEnablementForWorkflow:]
- +[WRWorkflow overrideOverallDiagnosticThresholdIntervalSecondsForWorkflow:]
- +[WRWorkflow overrideOverallDiagnosticThresholdIntervalSecondsForWorkflow:].cold.1
- +[WRWorkflow overrideTelemetryEnablementForWorkflow:]
- +[WRWorkflow taskingNumberForKey:]
- +[WRWorkflow taskingStringForKey:]
- +[WRWorkflow workflowNameForPlist:]
- -[WRSignpost initWithSubsystem:category:name:individuationFieldName:environmentFieldNames:diagnosticThresholdCount:diagnosticThresholdIntervalSeconds:]
- -[WRSignpostTracker setCount:]
- -[WRSignpostTracker setTimeUntilFirstSignpostNanoseconds:]
- -[WRSignpostTracker setTotalDurationNanoseconds:]
- -[WRTimestampAndThread initWithThreadID:machContTimeNs:]
- -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:]
- -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:].cold.1
- -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:].cold.2
- -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:].cold.3
- -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:].cold.4
- -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:].cold.5
- -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:].cold.6
- -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:].cold.7
- -[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:].cold.8
- -[WRWorkflowEventTracker haveAnyEndSignpostsWithIndividuation:individuationIdentifier:trackThem:]
- -[WRWorkflowEventTracker haveAnyEndSignpostsWithIndividuation:individuationIdentifier:trackThem:].cold.1
- -[WRWorkflowEventTracker individuationIdentifierForSignpostObject:individuationFieldName:].cold.1
- -[WRWorkflowEventTracker openIndividuatedIntervalsWithMatchingEndSignpostOutsideEvent]
- -[WRWorkflowEventTracker overallIntervalStart]
- -[WRWorkflowEventTracker setOpenIndividuatedIntervalsWithMatchingEndSignpostOutsideEvent:]
- -[WRWorkflowEventTracker setOverallIntervalStart:]
- -[WRWorkflowProvider handleTaskingChanged:]
- -[WRWorkflowProvider handleTaskingChanged:].cold.1
- -[WRWorkflowProvider notifyToken]
- -[WRWorkflowProvider startSignpost]
- -[WRWorkflowProviderAllWorkflows handleTaskingChanged:]
- -[WRWorkflowProviderAllWorkflows handleTaskingChanged:].cold.1
- -[WRWorkflowProviderSingleWorkflow handleTaskingChanged:]
- -[WRWorkflowProviderSingleWorkflow handleTaskingChanged:].cold.1
- GCC_except_table32
- GCC_except_table49
- _OBJC_IVAR_$_WRSignpost._diagnosticThresholdCount
- _OBJC_IVAR_$_WRSignpost._diagnosticThresholdIntervalSeconds
- _OBJC_IVAR_$_WRSignpostTracker._count
- _OBJC_IVAR_$_WRSignpostTracker._timeUntilFirstSignpostNanoseconds
- _OBJC_IVAR_$_WRSignpostTracker._totalDurationNanoseconds
- _OBJC_IVAR_$_WRWorkflow._allowList
- _OBJC_IVAR_$_WRWorkflow._overallDiagnosticThresholdIntervalSeconds
- _OBJC_IVAR_$_WRWorkflowEventTracker._openIndividuatedIntervalsWithMatchingEndSignpostOutsideEvent
- _OBJC_IVAR_$_WRWorkflowEventTracker._overallIntervalStart
- _OBJC_IVAR_$_WRWorkflowProvider._notifyToken
- _OBJC_IVAR_$_WRWorkflowProvider._startSignpost
- __DictGet
- __OBJC_$_PROP_LIST_WRWorkflowProvider
- ___41-[WRWorkflowEventTracker handleSignpost:]_block_invoke
- ___55-[WRWorkflowProviderAllWorkflows handleTaskingChanged:]_block_invoke
- ___57-[WRWorkflowProviderSingleWorkflow handleTaskingChanged:]_block_invoke
- ___64-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:]_block_invoke
- ___64-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:]_block_invoke_2
- ___assert_rtn
- ___block_descriptor_32_e35_q24?0"WRWorkflow"8"WRWorkflow"16l
- ___block_literal_global.44
- _objc_msgSend$allObjects
- _objc_msgSend$diagnosticThresholdCount
- _objc_msgSend$diagnosticThresholdIntervalSeconds
- _objc_msgSend$durationNanoseconds
- _objc_msgSend$handleTaskingChanged:
- _objc_msgSend$hasDiagnosticThresholdCount
- _objc_msgSend$hasDiagnosticThresholdInterval
- _objc_msgSend$initWithPlist:telemetryEnabled:diagnosticsEnabled:
- _objc_msgSend$initWithSignpost:individuationIdentifier:
- _objc_msgSend$initWithStart:end:
- _objc_msgSend$initWithSubsystem:category:name:individuationFieldName:environmentFieldNames:diagnosticThresholdCount:diagnosticThresholdIntervalSeconds:
- _objc_msgSend$initWithThreadID:machContTimeNs:
- _objc_msgSend$reset
- _objc_msgSend$totalDurationNanoseconds
CStrings:
+ ""
+ "\a7"
+ "\x11"
+ "\x16"
+ "\x17"
+ " "
+ "!4"
+ "$"
+ "%@"
+ "%@ contains invalid characters (\"%@\": \"%@\")"
+ "%@ is above max value (%f > %f)"
+ "%@ is negative (%f)"
+ "%@ is negative (%lld)"
+ "%@ is not a bool (%d)"
+ "%@-%@.%@"
+ "%@:%@:%@ (event:%@ indiv:%@ env:%@ thresholds:%lu)"
+ "%u"
+ "%{public}@: %{public}@: %{public}@->%@: Both begin and end times are overridden - assuming they occured on threads 0x%#llx and 0x%#llx"
+ "%{public}@: %{public}@: %{public}@->%@: Handling synthetic event as SignpostEvent, not SignpostInterval"
+ "%{public}@: %{public}@: %{public}@->%@: Interval start after event end (%.3f later)"
+ "%{public}@: %{public}@: %{public}@->%@: No field value"
+ "%{public}@: %{public}@: %{public}@->%@: Unable to get event identifier for start signpost, throwing out all current events in case they were incomplete events"
+ "%{public}@: %{public}@: %{public}@->%@: Unable to get event identifier, ignoring signpost"
+ "%{public}@: %{public}@: %{public}@->%@: fill non-diagnostic signposts: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@: %{public}@: %{public}@->%@: fill non-diagnostic signposts: event middle %+.3fs @%llu"
+ "%{public}@: %{public}@: %{public}@->%@: metadata is data type"
+ "%{public}@: %{public}@: %{public}@->%@: outside any workflow event (%llu)"
+ "%{public}@: %{public}@: Both begin and end times are overridden - assuming they occured on threads 0x%#llx and 0x%#llx"
+ "%{public}@: %{public}@: Cannot log telemetry for %{public}@ -> %@, conflicts with existing entry"
+ "%{public}@: %{public}@: Handling synthetic event as SignpostEvent, not SignpostInterval"
+ "%{public}@: %{public}@: Interval start after event end (%.3f later)"
+ "%{public}@: %{public}@: Invalid signpost override: %@"
+ "%{public}@: %{public}@: Logging %@ to CA: %@"
+ "%{public}@: %{public}@: No indivudation field name for identifier %@"
+ "%{public}@: %{public}@: Unable to get event identifier for start signpost, throwing out all current events in case they were incomplete events"
+ "%{public}@: %{public}@: Unable to get event identifier, ignoring signpost"
+ "%{public}@: %{public}@: diagnostic %{public}@: applied override: %{public}@ -> %{public}@"
+ "%{public}@: %{public}@: diagnostic %{public}@: disabled via override"
+ "%{public}@: %{public}@: diagnostic %{public}@: invalid new dict: %{public}@\n%{public}@"
+ "%{public}@: %{public}@: diagnostic %{public}@: invalid new settings: %{public}@"
+ "%{public}@: %{public}@: diagnostic %{public}@: invalid override dict: %{public}@\n%{public}@"
+ "%{public}@: %{public}@: diagnostic %{public}@: invalid override settings: %{public}@"
+ "%{public}@: %{public}@: event start @ %@ (%llu)"
+ "%{public}@: %{public}@: event start @%llu (%+.3fs in previous event)"
+ "%{public}@: %{public}@: fill non-diagnostic signposts: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@: %{public}@: fill non-diagnostic signposts: event middle %+.3fs @%llu"
+ "%{public}@: %{public}@: no signposts for telemetry"
+ "%{public}@: %{public}@: outside any workflow event (%llu)"
+ "%{public}@: Adding workflow from %{public}@"
+ "%{public}@: Also failed to remove tailspin file: %{public}@"
+ "%{public}@: Bad error domain %@"
+ "%{public}@: Bad override for diagnostics enablement: %{public}@"
+ "%{public}@: Bad override for telemetry enablement: %{public}@"
+ "%{public}@: Bad override workflow: %{public}@"
+ "%{public}@: Failed to create encoded string: %{public}@"
+ "%{public}@: Failed to generate tailspin, could not open file %{public}@: %{errno}d"
+ "%{public}@: Failed to save tailspin to file to %{public}@"
+ "%{public}@: Found workflow from %@"
+ "%{public}@: Generating diagnostics"
+ "%{public}@: Have error with bad domain %@"
+ "%{public}@: Have exceeded diagnostic thresholds, but none use tailspin"
+ "%{public}@: Ignoring duplicate workflow from %{public}@"
+ "%{public}@: Incomplete event when done handling signposts, ignoring"
+ "%{public}@: Invalid new signpost with no name: %@"
+ "%{public}@: Invalid new signposts: %@"
+ "%{public}@: Invalid signpost override: %@"
+ "%{public}@: Logging %@ to CA: %@"
+ "%{public}@: New workflow disabled"
+ "%{public}@: New workflow is duplicate of existing workflow (whose settings are already overridden)"
+ "%{public}@: No diagnostic thresholds were exceeded"
+ "%{public}@: No diagnostics enabled for workflow"
+ "%{public}@: Tailspin is not available on this platform"
+ "%{public}@: Trying to report workflow without an end time"
+ "%{public}@: Unable to create new workflow: %{public}@"
+ "%{public}@: Unable to create workflow: %{public}@"
+ "%{public}@: Unable to get fileSystemRepresentation for %{public}@"
+ "%{public}@: Unable to read in %{public}@: %@"
+ "%{public}@: Unable to read in %{public}@: %{public}@"
+ "%{public}@: Workflow disabled"
+ "%{public}@: concurrent workflow done"
+ "%{public}@: diagnostic %{public}@: applied override: %{public}@ -> %{public}@"
+ "%{public}@: diagnostic %{public}@: disabled via override"
+ "%{public}@: diagnostic %{public}@: invalid new dict: %{public}@\n%{public}@"
+ "%{public}@: diagnostic %{public}@: invalid new settings: %{public}@"
+ "%{public}@: diagnostic %{public}@: invalid override dict: %{public}@\n%{public}@"
+ "%{public}@: diagnostic %{public}@: invalid override settings: %{public}@"
+ "%{public}@: gatherDiagnostics called outside eventCompletionCallback"
+ "%{public}@: generating CA telemetry for %lu trackers"
+ "%{public}@: incomplete interval %llu after event end %llu"
+ "%{public}@: network-bound duration %llu > workflow event duration %llu"
+ "%{public}@: reset in middle of event, reporting error"
+ "%{public}@: saved tailspin file %{public}@ for slow workflow, notifying spindump"
+ "%{public}@: signpost interval %llu-%llu outside event time range %llu-%llu"
+ "%{public}@: union of all signposts duration %llu > workflow event duration %llu"
+ "%{public}@: workflow name doesn't match plist filename %{public}@"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: Both begin and end times are overridden - assuming they occured on threads 0x%#llx and 0x%#llx"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: End signpost group candidate"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: End signpost with individuation, set as candidate for group"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: End signpost with individuation, still needs %@"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: Handling synthetic event as SignpostEvent, not SignpostInterval"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: No field value"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: No missing end signposts, but didn't find an end signpost tracker"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: Saw new individuation identifier needed for end signpost %@"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: candidateEndSignpostTracker is bad class %s"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: contained environment %{public}@ not a number/string"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: contained environment %{public}@->%{public}@"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: event end %+.3fs @%llu"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: event middle %+.3fs @%llu"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: fill non-diagnostic signposts: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: fill non-diagnostic signposts: event middle %+.3fs @%llu"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: found missing individuation identifier"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: metadata is data type"
+ "%{public}@<%{public}@>: %{public}@: %{public}@->%@: missing environment %{public}@"
+ "%{public}@<%{public}@>: %{public}@: Allocating new concurrent event"
+ "%{public}@<%{public}@>: %{public}@: Both begin and end times are overridden - assuming they occured on threads 0x%#llx and 0x%#llx"
+ "%{public}@<%{public}@>: %{public}@: Cannot log telemetry for %{public}@ -> %@, conflicts with existing entry"
+ "%{public}@<%{public}@>: %{public}@: End signpost group candidate"
+ "%{public}@<%{public}@>: %{public}@: End signpost with individuation, set as candidate for group"
+ "%{public}@<%{public}@>: %{public}@: End signpost with individuation, still needs %@"
+ "%{public}@<%{public}@>: %{public}@: Handling synthetic event as SignpostEvent, not SignpostInterval"
+ "%{public}@<%{public}@>: %{public}@: Logging %@ to CA: %@"
+ "%{public}@<%{public}@>: %{public}@: No concurrent event with event identifier"
+ "%{public}@<%{public}@>: %{public}@: No indivudation field name for identifier %@"
+ "%{public}@<%{public}@>: %{public}@: No missing end signposts, but didn't find an end signpost tracker"
+ "%{public}@<%{public}@>: %{public}@: Saw new individuation identifier needed for end signpost %@"
+ "%{public}@<%{public}@>: %{public}@: candidateEndSignpostTracker is bad class %s"
+ "%{public}@<%{public}@>: %{public}@: contained environment %{public}@ not a number/string"
+ "%{public}@<%{public}@>: %{public}@: contained environment %{public}@->%{public}@"
+ "%{public}@<%{public}@>: %{public}@: event end %+.3fs @%llu"
+ "%{public}@<%{public}@>: %{public}@: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@<%{public}@>: %{public}@: event middle %+.3fs @%llu"
+ "%{public}@<%{public}@>: %{public}@: event start @ %@ (%llu)"
+ "%{public}@<%{public}@>: %{public}@: event start @%llu (%+.3fs in previous event)"
+ "%{public}@<%{public}@>: %{public}@: fill non-diagnostic signposts: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@<%{public}@>: %{public}@: fill non-diagnostic signposts: event middle %+.3fs @%llu"
+ "%{public}@<%{public}@>: %{public}@: missing environment %{public}@"
+ "%{public}@<%{public}@>: %{public}@: no signposts for telemetry"
+ "%{public}@<%{public}@>: Also failed to remove tailspin file: %{public}@"
+ "%{public}@<%{public}@>: Bad error domain %@"
+ "%{public}@<%{public}@>: Failed to create encoded string: %{public}@"
+ "%{public}@<%{public}@>: Failed to generate tailspin, could not open file %{public}@: %{errno}d"
+ "%{public}@<%{public}@>: Failed to save tailspin to file to %{public}@"
+ "%{public}@<%{public}@>: Generating diagnostics"
+ "%{public}@<%{public}@>: Have error with bad domain %@"
+ "%{public}@<%{public}@>: Have exceeded diagnostic thresholds, but none use tailspin"
+ "%{public}@<%{public}@>: Incomplete event when done handling signposts, ignoring"
+ "%{public}@<%{public}@>: Logging %@ to CA: %@"
+ "%{public}@<%{public}@>: No diagnostic thresholds were exceeded"
+ "%{public}@<%{public}@>: No diagnostics enabled for workflow"
+ "%{public}@<%{public}@>: Tailspin is not available on this platform"
+ "%{public}@<%{public}@>: Trying to report workflow without an end time"
+ "%{public}@<%{public}@>: Unable to get fileSystemRepresentation for %{public}@"
+ "%{public}@<%{public}@>: Unknown signpost object type %{public}s"
+ "%{public}@<%{public}@>: candidateEndSignpostTracker is bad class %s"
+ "%{public}@<%{public}@>: concurrent workflow done"
+ "%{public}@<%{public}@>: gatherDiagnostics called outside eventCompletionCallback"
+ "%{public}@<%{public}@>: generating CA telemetry for %lu trackers"
+ "%{public}@<%{public}@>: incomplete interval %llu after event end %llu"
+ "%{public}@<%{public}@>: network-bound duration %llu > workflow event duration %llu"
+ "%{public}@<%{public}@>: reset in middle of event, reporting error"
+ "%{public}@<%{public}@>: saved tailspin file %{public}@ for slow workflow, notifying spindump"
+ "%{public}@<%{public}@>: signpost interval %llu-%llu outside event time range %llu-%llu"
+ "%{public}@<%{public}@>: union of all signposts duration %llu > workflow event duration %llu"
+ ","
+ "-%@-%@"
+ "-error"
+ "-generic"
+ "/private/var/db/WorkflowResponsiveness/"
+ "/private/var/db/WorkflowResponsiveness/OverridePlists"
+ "<signpost>"
+ "<workflow>"
+ "@\"NSDate\""
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSError\""
+ "@\"NSError\"24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"WRWorkflow\"16@?0@\"NSURL\"8"
+ "@24@0:8^@16"
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8@\"NSDictionary\"16^@24"
+ "@32@0:8@16^@24"
+ "@36@0:8@16B24^@28"
+ "@76@0:8@16@24@32@40@48@56B64@68"
+ "B16@?0@\"SignpostObject\"8"
+ "B16@?0^{ktrace_chunk=}8"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "Bad bool for %@: %d"
+ "Bad num for %@: %f"
+ "Bad override for new workflows: %{public}@"
+ "Cannot report spindump for this dispatch queue, but in a specified process %@"
+ "Cannot report spindump for this thread, but in a specified process %@"
+ "Could not open tailspin file %@"
+ "Custom Output:"
+ "Duplicate signpost dictionary for signpost %@"
+ "Encoded string does not contain a workflow event"
+ "Error getting diagnotic enablement override: %{public}@"
+ "Error iterating over tailspin file %@"
+ "Failed to create encoded string, unable to create UTF8 string from JSON data (%@)\n"
+ "Failed to create encoded string, unable to serialize into JSON (%@)\n"
+ "Failed to mark %{public}@ purgeable: %{errno}d"
+ "Filename \"%@\" doesn't match workflow name \"%@\""
+ "Gathering tailspin for workflow %s"
+ "I"
+ "I16@0:8"
+ "Invalid dispatch queue label regex \"%@\": %@"
+ "Invalid thread name regex \"%@\": %@"
+ "Invalid type in environment (%s -> %s)"
+ "Invalid type in signpostTrackerDicts (%s -> %s)"
+ "Invalid type in signpostTrackerDicts (%s)"
+ "JSONObjectWithData:options:error:"
+ "Key %@: unexpected value type %s"
+ "Key %@: unexpected value type %s in array"
+ "Marked %{public}@ purgeable"
+ "Multiple diagnostics with name %@"
+ "Multiple signposts with name %@"
+ "Mutiple diagnostic dictionaries in array, but no name: %@"
+ "NSCopying"
+ "No category for signpost %@"
+ "No end signpost in plist"
+ "No name for signpost"
+ "No override dictionary for workflow %@ new signpost %@"
+ "No reason string in tailspin file %@"
+ "No signposts for new workflow %@"
+ "No signposts in plist"
+ "No start signpost in plist"
+ "No subsystem for signpost %@"
+ "No such workflow, or workflow disabled"
+ "No workflow in tracker dict %@"
+ "Received com.apple.da.tasking_changed"
+ "Received com.apple.workflow_responsiveness.settings_changed"
+ "Removed %{public}@ successfully, but received error: %{public}@"
+ "Signpost %@ diagnostic %@ reports other signpost %@, but no such signpost exists"
+ "Signpost name is reserved: %@"
+ "Spindump custom output is empty"
+ "Spindump has no custom output"
+ "Start signposts cannot be individuated (%@) for signpost %@"
+ "String is not an encoded dictionary"
+ "T@\"NSArray\",R,V_diagnostics"
+ "T@\"NSArray\",R,V_workflowDiagnostics"
+ "T@\"NSDate\",R,V_date"
+ "T@\"NSError\",R"
+ "T@\"NSString\",R"
+ "T@\"NSString\",R,V_eventIdentifierFieldName"
+ "T@\"NSString\",R,V_reportOtherSignpostWithName"
+ "T@\"NSString\",R,V_reportProcessesWithName"
+ "T@\"NSString\",R,V_reportSpindumpForDispatchQueueWithLabel"
+ "T@\"NSString\",R,V_reportSpindumpForThreadWithName"
+ "T@\"SignpostSupportSubsystemCategoryAllowlist\",R"
+ "T@\"SignpostSupportSubsystemCategoryAllowlist\",R,V_allowListForAllSignposts"
+ "T@\"SignpostSupportSubsystemCategoryAllowlist\",R,V_allowListForDiagnostics"
+ "T@\"WRSignpost\",R"
+ "T@\"WRTimestampAndThread\",R"
+ "TB,R,V_gatherTailspin"
+ "TB,R,V_hasDiagnosticThresholdInterval"
+ "TB,R,V_networkBound"
+ "TB,R,V_reportOmittingNetworkBoundIntervals"
+ "TB,R,V_reportSpindumpForMainThread"
+ "TB,R,V_reportSpindumpForThisDispatchQueue"
+ "TB,R,V_reportSpindumpForThisThread"
+ "TB,R,V_tailspinIncludeOSLogs"
+ "TB,R,V_triggerEventTimeout"
+ "TB,R,V_workflowSupportsConcurrentEvents"
+ "TI,R,V_triggerThresholdCount"
+ "TQ,R,V_numHandledSignposts"
+ "TQ,R,V_numOutsideSignposts"
+ "TQ,R,V_numUnhandledSignposts"
+ "Tailspin %@ is not a Workflow Responsiveness tailspin"
+ "Td,R"
+ "Td,R,V_maximumEventDuration"
+ "Td,R,V_triggerThresholdDurationSingle"
+ "Td,R,V_triggerThresholdDurationSum"
+ "Td,R,V_triggerThresholdDurationUnion"
+ "URLByAppendingPathComponent:"
+ "URLByStandardizingPath"
+ "UTF8String"
+ "Unable to create data with encoded string"
+ "Unable to create folder at %@: %@"
+ "Unable to determine filename for %{public}@"
+ "Unable to fdopen %@"
+ "Unable to fread custom output from %@"
+ "Unable to fstat %@"
+ "Unable to get path for URL %@"
+ "Unable to get uft8 string from %@"
+ "Unable to init"
+ "Unable to init WRSignpostTracker"
+ "Unable to init WRWorkflowEventTracker"
+ "Unable to malloc %lu buffer"
+ "Unable to open %@"
+ "Unable to register for settings changed notifications: %d"
+ "Unable to register for tasking updated notifications: %d"
+ "Unable to remove %{public}@: %{public}@"
+ "Unexpected type %s for tasking value for key %@"
+ "Unknown diagnostic key \"%@\""
+ "Unknown diagnostic key %@"
+ "Unknown signpost key \"%@\""
+ "Unknown signpost leaf key %@"
+ "Unknown workflow key \"%@\""
+ "Unknown workflow leaf key %@"
+ "WR cleanup: %@ is not a regular file"
+ "WR cleanup: %@ is not a tailspin file"
+ "WR cleanup: %{public}@ created at %{public}@, removing"
+ "WR cleanup: %{public}@ created at %{public}@, skipping"
+ "WR cleanup: Error cleaning up workflow responsiveness directory file %{public}@: %{public}@"
+ "WR cleanup: No workflow responsiveness directory, no cleanup required"
+ "WR cleanup: Unable to create enumerator for %{public}@ to clean up workflow responsiveness directory"
+ "WR cleanup: Unable to get info about %@: filename:%@ isRegularFile:%@ creationDate:%@"
+ "WR cleanup: Unable to get path from %{public}@"
+ "WR mkdir: Unable to get path from %{public}@"
+ "WR.%@."
+ "WR.%@.%@"
+ "WR.%@.%@."
+ "WR.%@.%@.diagnostics.%@."
+ "WR.%@.diagnostics.%@."
+ "WR.workflows"
+ "WRDiagnostic"
+ "WRDictEncoding"
+ "WRIntervalAndThreads: No end in dict"
+ "WRIntervalAndThreads: No start in dict"
+ "WROpenIndividuatedSignpostInterval"
+ "WRTimestampAndThread: No machContTimeNs in dict"
+ "WRTimestampAndThread: No threadID in dict"
+ "WRWorkflowEventTracker: No signpost trackers in dict"
+ "Workflow %@ end signpost %@ doesn't exist"
+ "Workflow %@ has wrong name %@"
+ "Workflow %@ new signpost %@ has wrong name %@"
+ "Workflow %@ signpost %@ doesn't exist"
+ "Workflow %@ start signpost %@ doesn't exist"
+ "Workflow diagnostic %@ has event timeout threshold, but workflow has no maximum duration"
+ "Workflow diagnostic %@ omits network-bound work, but no network-bound signposts"
+ "Workflow diagnostic %@ reports signpost %@, but no such signpost exists"
+ "Workflow disabled"
+ "Workflow disabled by override"
+ "Workflow event incomplete"
+ "Workflow event timed out"
+ "Workflow name is reserved: %@"
+ "Workflow responsiveness delay detected in %@"
+ "Workflow supports concurrent events, but start signpost %@ has no event identifier field name"
+ "WorkflowResponsivenessError"
+ "Wrong type for signpost diagnostic dict: %s"
+ "Wrong type for signpost environmental field name: %s"
+ "Wrong type for workflow diagnostic dict: %s"
+ "Wrong type for workflow signpost dict: %s"
+ "Wrong value type for diagnostic key \"%@\": %s, expected %@"
+ "Wrong value type for signpost key \"%@\": %s, expected %@"
+ "Wrong value type for workflow key \"%@\": %s, expected %@"
+ "^"
+ "_"
+ "_allowListForAllSignposts"
+ "_allowListForDiagnostics"
+ "_concurrentEvents"
+ "_date"
+ "_diagnostics"
+ "_endSignpost"
+ "_error"
+ "_eventEnd"
+ "_eventIdentifier"
+ "_eventIdentifierFieldName"
+ "_eventStart"
+ "_gatherTailspin"
+ "_hasDiagnosticThresholdInterval"
+ "_incompleteIntervalStartsMutable"
+ "_maximumEventDuration"
+ "_networkBound"
+ "_numHandledSignposts"
+ "_numOutsideSignposts"
+ "_numUnhandledSignposts"
+ "_openIndividuatedIntervalsWithFieldNameMatchingAnEndSignpostFromBeforeEventStart"
+ "_reportOmittingNetworkBoundIntervals"
+ "_reportOtherSignpostWithName"
+ "_reportProcessesWithName"
+ "_reportSpindumpForDispatchQueueWithLabel"
+ "_reportSpindumpForMainThread"
+ "_reportSpindumpForThisDispatchQueue"
+ "_reportSpindumpForThisThread"
+ "_reportSpindumpForThreadWithName"
+ "_tailspinIncludeOSLogs"
+ "_taskingNotifyToken"
+ "_timeoutQueue"
+ "_timeoutSource"
+ "_timestampAndThread"
+ "_triggerEventTimeout"
+ "_triggerThresholdCount"
+ "_triggerThresholdDurationSingle"
+ "_triggerThresholdDurationSum"
+ "_triggerThresholdDurationUnion"
+ "_workflowDiagnostics"
+ "_workflowSupportsConcurrentEvents"
+ "_wrSettingsChangedNotifyToken"
+ "addCharactersInString:"
+ "allKeys"
+ "allocWithZone:"
+ "allowListForAllSignposts"
+ "allowListForDiagnostics"
+ "alphanumericCharacterSet"
+ "attributesOfItemAtPath:error:"
+ "beginDate"
+ "cleanupWorkflowResponsivenessDiagnosticsDirectory"
+ "code"
+ "com.apple.workflow-responsiveness"
+ "com.apple.workflow_responsiveness.settings_changed"
+ "completeDelaySec"
+ "completeDurationLongestSec"
+ "completeDurationSec"
+ "completeDurationUnionSec"
+ "componentsJoinedByString:"
+ "componentsSeparatedByCharactersInSet:"
+ "componentsSeparatedByString:"
+ "copyWithZone:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dataUsingEncoding:"
+ "dataWithJSONObject:options:error:"
+ "date"
+ "dateByAddingTimeInterval:"
+ "delayAfterSec"
+ "delaySec"
+ "description"
+ "diagnostic count threshold is invalid for the workflow"
+ "diagnostic event timeout threshold is invalid for signposts"
+ "diagnostic interval sum threshold is invalid for the workflow"
+ "diagnostic interval union threshold is invalid for the workflow"
+ "diagnostics"
+ "dictionaryWithObjects:forKeys:count:"
+ "dictionaryWithObjectsAndKeys:"
+ "domain"
+ "doneHandlingSignpostsWithEndTimeMachContNs:"
+ "durationLongestSec"
+ "durationNonNetworkBoundSec"
+ "durationSec"
+ "durationUnionSec"
+ "durationUntrackedSec"
+ "encodedDict"
+ "encodedStringWithError:"
+ "endDate"
+ "endSignpost"
+ "env_%@"
+ "error"
+ "errorWithDomain:code:userInfo:"
+ "eventEnd"
+ "eventIdentifier"
+ "eventIdentifierFieldName"
+ "eventStart"
+ "event_identifier_field_name"
+ "fileExistsAtPath:"
+ "fileSize"
+ "fileSystemRepresentation"
+ "fileType"
+ "fileURLWithPath:"
+ "fileURLWithPath:isDirectory:"
+ "formUnionWithCharacterSet:"
+ "gatherDiagnosticsIfNeeded"
+ "gatherTailspin"
+ "gather_tailspin"
+ "generateTelemetry"
+ "generic"
+ "group%d"
+ "handleSettingsChanged must be overridden by subclass"
+ "handleSettingsChanged:"
+ "hasAnySpindumpReports"
+ "hasMaximumEventDuration"
+ "hasSuffix:"
+ "hasTriggerThresholdCount"
+ "hasTriggerThresholdDurationSingle"
+ "hasTriggerThresholdDurationSum"
+ "hasTriggerThresholdDurationUnion"
+ "i24@?0r^v8r^v16"
+ "iat_end"
+ "iat_start"
+ "incompleteIntervalStarts"
+ "incompleteOccurrencesCount"
+ "indexOfObject:inSortedRange:options:usingComparator:"
+ "initForLiveStreamingWithWorkflow:timeoutQueue:eventCompletionCallback:"
+ "initForReadbackWithWorkflow:eventCompletionCallback:"
+ "initWithBytesNoCopy:length:freeWhenDone:"
+ "initWithContentsOfURL:error:"
+ "initWithData:encoding:"
+ "initWithDomain:code:userInfo:"
+ "initWithEncodedDict:error:"
+ "initWithEncodedString:error:"
+ "initWithFormat:arguments:"
+ "initWithObjectsAndKeys:"
+ "initWithPattern:options:error:"
+ "initWithSpindump:error:"
+ "initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:diagnostics:"
+ "initWithTailspin:error:"
+ "initWithTimeIntervalSince1970:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "insertObject:atIndex:"
+ "integerValue"
+ "invert"
+ "invertedSet"
+ "longLongValue"
+ "makeOverridePlistDirectoryWithError:"
+ "maximumEventDuration"
+ "maximum_duration"
+ "must run as root to create directory /private/var/db/WorkflowResponsiveness/ (running as %d)"
+ "mutableCopy"
+ "name:%@\ntriggerThresholdDurationSum:%f\ntriggerThresholdDurationUnion:%f\ntriggerThresholdDurationSingle:%f\ntriggerThresholdCount:%u\ntriggerEventTimeout:%u\ngatherTailspin:%u\ntailspinIncludeOSLogs:%u\nreportSpindumpForThisThread:%u\nreportSpindumpForThreadWithName:%@\nreportSpindumpForMainThread:%u\nreportSpindumpForThisDispatchQueue:%u\nreportSpindumpForDispatchQueueWithLabel:%@\nreportOtherSignpostWithName:%@\nreportProcessesWithName:%@\nreportOmittingNetworkBoundIntervals:%u\n"
+ "networkBound"
+ "network_bound"
+ "no diagnostics enabled"
+ "no threshold for diagnostic"
+ "numHandledSignposts"
+ "numOutsideSignposts"
+ "numUnhandledSignposts"
+ "numberWithDouble:"
+ "numberWithInt:"
+ "numberWithInteger:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedInteger:"
+ "numberWithUnsignedLongLong:"
+ "occurrencesCount"
+ "omitting network bound intervals is invalid for signposts"
+ "option_report_omit_network_bound_intervals"
+ "option_report_other_processes"
+ "option_report_other_signpost"
+ "option_tailspin_includes_oslogs"
+ "overall"
+ "overridePlistDirectory"
+ "overridesBeginTime"
+ "overridesEndTime"
+ "passesSubsystem:category:"
+ "path"
+ "processTraceFileWithPath:startDate:endDate:errorOut:"
+ "propertyListWithData:options:format:error:"
+ "q24@?0@\"WRDiagnostic\"8@\"WRDiagnostic\"16"
+ "q24@?0@\"WRIntervalAndThreads\"8@\"WRIntervalAndThreads\"16"
+ "q24@?0@\"WRTimestampAndThread\"8@\"WRTimestampAndThread\"16"
+ "r"
+ "rangeOfCharacterFromSet:"
+ "removeItemAtURL:error:"
+ "removeObjectIdenticalTo:"
+ "reportOmittingNetworkBoundIntervals"
+ "reportOtherSignpostWithName"
+ "reportProcessesWithName"
+ "reportSpindumpForDispatchQueueWithLabel"
+ "reportSpindumpForMainThread"
+ "reportSpindumpForThisDispatchQueue"
+ "reportSpindumpForThisThread"
+ "reportSpindumpForThreadWithName"
+ "report_spindump_dispatchqueue_label"
+ "report_spindump_main_thread"
+ "report_spindump_this_dispatchqueue"
+ "report_spindump_this_thread"
+ "report_spindump_thread_name"
+ "reporting multiple spindumps from a single diagnostic"
+ "reporting spindump, but not gathering tailspin"
+ "resourceValuesForKeys:error:"
+ "setBeginEventProcessingBlock:"
+ "setDateFormat:"
+ "setEmitEventProcessingBlock:"
+ "setIntervalCompletionProcessingBlock:"
+ "setSubsystemCategoryFilter:"
+ "st_emits"
+ "st_environment"
+ "st_incomplete_interval_starts"
+ "st_individuation_identifier"
+ "st_intervals"
+ "st_name"
+ "stats"
+ "statsWithEventEndNs:"
+ "stringByAppendingFormat:"
+ "stringByAppendingString:"
+ "stringFromDate:"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "substringWithRange:"
+ "tailspin"
+ "tailspinIncludeOSLogs"
+ "tat_date"
+ "tat_machContTimeNs"
+ "tat_threadId"
+ "timeIntervalSinceNow"
+ "timeIntervalSinceReferenceDate"
+ "timeRecordedNanoseconds"
+ "triggerEventTimeout"
+ "triggerThresholdCount"
+ "triggerThresholdDurationSingle"
+ "triggerThresholdDurationSum"
+ "triggerThresholdDurationUnion"
+ "trigger_event_timeout"
+ "trigger_threshold_count"
+ "trigger_threshold_duration_single"
+ "trigger_threshold_duration_sum"
+ "trigger_threshold_duration_union"
+ "unhandled signpost array key %@"
+ "unhandled signpost array key %{public}@"
+ "unhandled workflow array key %@"
+ "unhandled workflow array key %{public}@"
+ "unsignedIntValue"
+ "unsignedLongLongValue"
+ "userInfo"
+ "v12@?0B8"
+ "v16@?0@\"NSURL\"8"
+ "v16@?0@\"WRSignpostTracker\"8"
+ "v16@?0@\"WRWorkflowEventTracker\"8"
+ "v24@0:8Q16"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v32@?0@8@16^B24"
+ "whitespaceAndNewlineCharacterSet"
+ "workflowDiagnostics"
+ "workflowName"
+ "workflowSupportsConcurrentEvents"
+ "workflowWithPlist:checkForOverrides:error:"
+ "wrlogging"
+ "wt_error_code"
+ "wt_error_description"
+ "wt_event_end"
+ "wt_event_identifier"
+ "wt_event_start"
+ "wt_signpost_end"
+ "wt_signpost_start"
+ "wt_signpost_trackers"
+ "wt_workflow"
+ "yyyy-MM-dd-HHmmss.SSS"
+ "{?=QQQ}16@0:8"
+ "{?={?=QQQQQQ}{?=QQQQQQ}}24@0:8Q16"
- "\x04\x11"
- "\a"
- "\x12"
- "\x12#"
- "\x15"
- "%@:%@:%@ (indiv:%@ env:%@ thresholds:%.3f/%u)"
- "%{public}@: %{public}@: %{public}@->%@: No individuation field"
- "%{public}@: %{public}@: %{public}@->%@: Unable to find individuation identifier for interval begin outside event, won't know to wait for corresponding end signpost"
- "%{public}@: %{public}@: %{public}@->%@: found non-number/string individuation identifier"
- "%{public}@: %{public}@: Duplicate signpost in plist"
- "%{public}@: %{public}@: No category in plist"
- "%{public}@: %{public}@: No subsystem in plist"
- "%{public}@: %{public}@: Non-positive diagnostic threshold count %d in plist"
- "%{public}@: %{public}@: Non-positive diagnostic threshold count %d in tasking settings"
- "%{public}@: %{public}@: Non-positive diagnostic threshold interval %f in plist"
- "%{public}@: %{public}@: Non-positive diagnostic threshold interval %f in tasking settings"
- "%{public}@: %{public}@: Start signposts cannot be individuated (%@)"
- "%{public}@: %{public}@: Unable to find individuation identifier for interval begin outside event, won't know to wait for corresponding end signpost"
- "%{public}@: %{public}@: end value not <true/> in plist"
- "%{public}@: %{public}@: event start @%llu"
- "%{public}@: %{public}@: event start @%llu (%+.3fs in previous event), resetting"
- "%{public}@: %{public}@: overall_interval value not <true/> in plist"
- "%{public}@: %{public}@: start value not <true/> in plist"
- "%{public}@: No end signpost in plist"
- "%{public}@: No name for signpost in plist"
- "%{public}@: No signposts in plist"
- "%{public}@: No start signpost in plist"
- "%{public}@: Non-positive diagnostic threshold interval %f in plist"
- "%{public}@: Non-positive overall diagnostic threshold interval %f in tasking settings"
- "-[WRWorkflowEventTracker haveAnyEndSignpostsWithIndividuation:individuationIdentifier:trackThem:]"
- "@32@0:8@16@24"
- "@32@0:8@16B24B28"
- "@32@0:8Q16Q24"
- "@68@0:8@16@24@32@40@48i56d60"
- "T@\"SignpostSupportSubsystemCategoryAllowlist\",R,V_allowList"
- "T@\"WRSignpost\",R,V_startSignpost"
- "Td,R,V_diagnosticThresholdIntervalSeconds"
- "Td,R,V_overallDiagnosticThresholdIntervalSeconds"
- "Ti,R,V_diagnosticThresholdCount"
- "Tracker for %@, count:%d"
- "Tracker for %@, count:%d total:%.3fs"
- "Unable to read in %{public}@: %{public}@"
- "Unable to register for tasking update notifications: %d"
- "Unexpected type %{public}s for tasking value for key %{public}@"
- "WR.%@.%@.%@.%@.diagnosticThresholdCount"
- "WR.%@.%@.%@.%@.diagnosticThresholdIntervalSeconds"
- "WR.%@.overallDiagnosticThresholdIntervalSeconds"
- "WRWorkflowEventTracker.m"
- "Workflow %{public}@ has incorrect name %{public}@"
- "_allowList"
- "_count"
- "_diagnosticThresholdCount"
- "_diagnosticThresholdIntervalSeconds"
- "_notifyToken"
- "_openIndividuatedIntervalsWithMatchingEndSignpostOutsideEvent"
- "_overallDiagnosticThresholdIntervalSeconds"
- "_overallIntervalStart"
- "_timeUntilFirstSignpostNanoseconds"
- "_totalDurationNanoseconds"
- "allObjects"
- "durationNanoseconds"
- "handleTaskingChanged must be overridden by subclass"
- "handleTaskingChanged:"
- "initWithPlist:telemetryEnabled:diagnosticsEnabled:"
- "initWithSignpost:individuationIdentifier:"
- "initWithStart:end:"
- "initWithSubsystem:category:name:individuationFieldName:environmentFieldNames:diagnosticThresholdCount:diagnosticThresholdIntervalSeconds:"
- "initWithThreadID:machContTimeNs:"
- "q"
- "q24@?0@\"WRWorkflow\"8@\"WRWorkflow\"16"
- "v24@0:8@16"
- "wrsignpost.individuationFieldName && (individuationIdentifier || !trackThem)"

```
