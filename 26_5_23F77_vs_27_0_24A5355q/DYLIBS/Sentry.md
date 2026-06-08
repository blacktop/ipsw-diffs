## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

```diff

-3.0.0.0.0
-  __TEXT.__text: 0x10c8c
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xd50
-  __TEXT.__const: 0xe4
-  __TEXT.__cstring: 0x1431
-  __TEXT.__oslogstring: 0x1c09
-  __TEXT.__gcc_except_tab: 0x444
+9.0.0.0.0
+  __TEXT.__text: 0x10460
+  __TEXT.__objc_methlist: 0xd60
+  __TEXT.__const: 0x104
+  __TEXT.__cstring: 0x14c9
+  __TEXT.__oslogstring: 0x1f8c
+  __TEXT.__gcc_except_tab: 0x344
   __TEXT.__unwind_info: 0x490
-  __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methname: 0x2e56
-  __TEXT.__objc_methtype: 0x3dd
-  __TEXT.__objc_stubs: 0x1ec0
-  __DATA_CONST.__got: 0x270
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_selrefs: 0xa58
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x338
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x11c0
-  __AUTH_CONST.__objc_const: 0x19b0
+  __DATA_CONST.__got: 0x278
+  __AUTH_CONST.__const: 0x360
+  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__objc_const: 0x19d0
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x148
+  __DATA.__objc_ivar: 0x14c
   __DATA.__data: 0xe8
   __DATA.__bss: 0x80
   __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0xc0
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 9D401CC3-58C0-3D1F-A50A-8C1CDC2F25AA
-  Functions: 448
-  Symbols:   1666
-  CStrings:  988
+  UUID: 8CCDACAC-CD44-37CF-9DEE-F611F895C2CF
+  Functions: 462
+  Symbols:   1716
+  CStrings:  453
 
Symbols:
+ +[STYDeviceInfo _determineProductType]
+ +[STYDeviceInfo _determineProductType].cold.1
+ +[STYDeviceInfo _determineProductType].cold.2
+ +[STYDeviceInfo _determineProductType].cold.3
+ +[STYDeviceInfo productType]
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.15
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.16
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleInterval:].cold.17
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleIntervalBegin:]
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleIntervalBegin:].cold.1
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleIntervalBegin:].cold.2
+ -[STYSpecialAppLaunchSignpostMonitorHelper handleIntervalBegin:].cold.3
+ -[STYSpecialAppLaunchSignpostMonitorHelper init].cold.1
+ -[STYSpecialAppLaunchSignpostMonitorHelper init].cold.2
+ -[STYUserScenario initWithLifecycleScenarioCategoryAndProductType:productType:titleText:]
+ -[STYUserScenarioCache productType]
+ -[STYUserScenarioCache setProductType:]
+ GCC_except_table123
+ GCC_except_table140
+ GCC_except_table142
+ _MGGetStringAnswer
+ _MobileGestalt_copy_productTypeDescForPowerPerf_obj
+ _MobileGestalt_get_current_device
+ _OBJC_IVAR_$_STYSpecialAppLaunchSignpostMonitorHelper._perfHUDClient
+ _OBJC_IVAR_$_STYUserScenarioCache._productType
+ _PerfHUDClientFunction
+ _PerfHUDContentFunction
+ _PerfHUDServicesLibrary.sLib
+ _PerfHUDServicesLibrary.sOnce
+ ___28+[STYDeviceInfo productType]_block_invoke
+ ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.171
+ ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.172
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.485
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.488
+ ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.489
+ ___50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.383
+ ___PerfHUDServicesLibrary_block_invoke
+ ___block_literal_global.156
+ ___block_literal_global.159
+ ___block_literal_global.162
+ ___block_literal_global.165
+ ___block_literal_global.480
+ ___block_literal_global.555
+ ___block_literal_global.560
+ ___block_literal_global.6
+ __os_log_default
+ _classPerfHUDClient
+ _classPerfHUDContent
+ _dlopen
+ _getPerfHUDClientClass
+ _getPerfHUDContentClass
+ _initPerfHUDClient
+ _initPerfHUDClient.cold.1
+ _initPerfHUDContent
+ _initPerfHUDContent.cold.1
+ _objc_claimAutoreleasedReturnValue
+ _objc_getClass
+ _objc_msgSend$_determineProductType
+ _objc_msgSend$contentForLine:
+ _objc_msgSend$contentWithTitle:label:timeValue:color:
+ _objc_msgSend$createStreamLineWithClientLineID:content:config:error:
+ _objc_msgSend$endLine:withContent:error:
+ _objc_msgSend$initWithClientID:
+ _objc_msgSend$productType
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setTimeValue:
+ _objc_msgSend$signpostId
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _productType.onceToken
+ _productType.productType
- +[STYDeviceInfo _determineHardwareModel]
- +[STYDeviceInfo hardwareModel]
- -[STYUserScenario initWithLifecycleScenarioCategoryAndModelName:modelName:titleText:]
- -[STYUserScenarioCache hwModel]
- -[STYUserScenarioCache setHwModel:]
- GCC_except_table122
- GCC_except_table139
- GCC_except_table141
- GCC_except_table200
- GCC_except_table205
- GCC_except_table207
- GCC_except_table220
- _OBJC_IVAR_$_STYUserScenarioCache._hwModel
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- ___30+[STYDeviceInfo hardwareModel]_block_invoke
- ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke.172
- ___39-[STYSignpostsMonitor checkMonitoring:]_block_invoke_2.173
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.478
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.481
- ___46-[STYWorkflowResponsivenessMonitorHelper init]_block_invoke.482
- ___50-[STYGeneralSignpostMonitorHelper handleInterval:]_block_invoke.384
- ___block_literal_global.157
- ___block_literal_global.160
- ___block_literal_global.163
- ___block_literal_global.166
- ___block_literal_global.4
- ___block_literal_global.473
- ___block_literal_global.548
- _free
- _hardwareModel.model
- _hardwareModel.onceToken
- _malloc_type_malloc
- _objc_msgSend$_determineHardwareModel
- _objc_msgSend$hardwareModel
- _objc_msgSend$stringWithUTF8String:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "/AppleInternal/Library/Frameworks/PerfHUDServices.framework/PerfHUDServices"
+ "AppLaunch"
+ "Created PerfHUD stream line %llu for app launch"
+ "Created PerfHUDClient obj:%{private}@ with clientID:%{private}@"
+ "Ended PerfHUD stream line %llu for app launch: %@ (duration: %.2fms)"
+ "Ending PerfHUD stream line for ApplicationFirstFramePresentation signpostName=%@ process=%@ subsystem=%@ category=%@ signpostID=%llu duration=%.2fms"
+ "Failed to create PerfHUD stream line for app launch: %@"
+ "Failed to end PerfHUD stream line %llu: %@"
+ "Failed to get current device from MobileGestalt: %{darwin.errno}d"
+ "Failed to get productType from MobileGestalt: %{darwin.errno}d"
+ "Got an empty productType string from MobileGestalt"
+ "Launch"
+ "No PerfHUD content found for line %llu - line may have timed out or was never created (process=%@, signpostID=%llu)"
+ "PerfHUDClient"
+ "PerfHUDContent"
+ "PerfHUDServices framework not available at runtime, app launch HUD disabled"
+ "ProductType"
+ "Received app launch begin for signpostName=%@ process=%@ subsystem=%@ category=%@ signpostID=%llu timestamp=%llu isSynthetic=%d"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSString\""
- "@\"NSUserDefaults\""
- "@\"STYAbcHelper\""
- "@\"STYGeneralSignpostMonitorHelper\""
- "@\"STYSignpostStreamingStatistics\""
- "@\"STYSpecialAppLaunchSignpostMonitorHelper\""
- "@\"STYUserScenario\""
- "@\"STYWorkflowResponsivenessMonitorHelper\""
- "@\"SignpostInterval\""
- "@\"SignpostSupportObjectExtractor\""
- "@\"SignpostSupportSubsystemCategoryAllowlist\""
- "@\"WRWorkflowEventTracker\""
- "@\"WRWorkflowProvider\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16^@24"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@68@0:8@16@24q32@40@48@56i64"
- "@?"
- "@?16@0:8"
- "App launch threshold enforced"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8@16"
- "B28@0:8i16i20i24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "I"
- "I16@0:8"
- "Q"
- "Q16@0:8"
- "STYAbcHelper"
- "STYDeviceInfo"
- "STYDiagCollectorLogger"
- "STYDiagnosticsCollector"
- "STYGeneralSignpostMonitorHelper"
- "STYPerformanceChecker"
- "STYScenarioReportLogger"
- "STYSignpostStreamingStatistics"
- "STYSignpostsMonitor"
- "STYSignpostsMonitorHelper"
- "STYSpecialAppLaunchSignpostMonitorHelper"
- "STYUserScenario"
- "STYUserScenarioCache"
- "STYWorkflowEventTracker"
- "STYWorkflowResponsivenessMonitorHelper"
- "T@\"NSArray\",&,V_workflowEventTrackers"
- "T@\"NSDate\",&,V_timeOfLastExtractorFailure"
- "T@\"NSDictionary\",&,V_animationConfigForWhitelistedCategories"
- "T@\"NSDictionary\",&,V_animationConfigForWhitelistedNames"
- "T@\"NSDictionary\",&,V_animationConfigForWhitelistedSubsystems"
- "T@\"NSDictionary\",&,V_bundleIdForAppName"
- "T@\"NSDictionary\",&,V_perfCheckerErrors"
- "T@\"NSDictionary\",&,V_responsivenessConfigForWhitelistedCategories"
- "T@\"NSDictionary\",&,V_responsivenessConfigForWhitelistedNames"
- "T@\"NSDictionary\",&,V_responsivenessConfigForWhitelistedSubsystems"
- "T@\"NSError\",&,V_badConfigError"
- "T@\"NSError\",&,V_bundledIdLookupFailedrror"
- "T@\"NSMutableDictionary\",&,V_lifecycleScenarios"
- "T@\"NSMutableDictionary\",&,V_scenarioObjects"
- "T@\"NSMutableDictionary\",&,V_symptomsSignature"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_monitorQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_processingQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_serialUtilityQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_settingsChangedCallbackQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_sharedConcurrentQueueAtBackground"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_sharedConcurrentQueueAtUtility"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_sharedSerialQueueAtUtility"
- "T@\"NSObject<OS_dispatch_source>\",&,V_perDayTimer"
- "T@\"NSObject<OS_dispatch_source>\",&,V_perPeriodTimer"
- "T@\"NSObject<OS_os_log>\",&,V_logHandle"
- "T@\"NSObject<OS_os_log>\",&,V_logger"
- "T@\"NSObject<OS_os_transaction>\",&,V_osTransaction"
- "T@\"NSString\",&,V_hwModel"
- "T@\"NSString\",&,V_metadata"
- "T@\"NSString\",R"
- "T@\"NSString\",R,V_appBundleId"
- "T@\"NSString\",R,V_appName"
- "T@\"NSString\",R,V_issueCategory"
- "T@\"NSString\",R,V_scenarioGroup"
- "T@\"NSString\",R,V_scenarioID"
- "T@\"NSString\",R,V_titleText"
- "T@\"STYAbcHelper\",&,V_abcHelper"
- "T@\"STYGeneralSignpostMonitorHelper\",&,V_generalSignpostHelper"
- "T@\"STYSignpostStreamingStatistics\",&,V_streamingStatistics"
- "T@\"STYSpecialAppLaunchSignpostMonitorHelper\",&,V_specialAppLaunchSignpostHelper"
- "T@\"STYUserScenario\",R,V_scenario"
- "T@\"STYWorkflowResponsivenessMonitorHelper\",&,V_workflowResponsivenessHelper"
- "T@\"SignpostInterval\",&,V_interval"
- "T@\"SignpostSupportObjectExtractor\",&,V_signpostExtractor"
- "T@\"SignpostSupportSubsystemCategoryAllowlist\",R"
- "T@\"WRWorkflowEventTracker\",&,V_wrTracker"
- "T@\"WRWorkflowProvider\",&,V_workflowProvider"
- "T@?,C,V_settingsChangedCallback"
- "TB,R"
- "TB,V_avoidGeneratingTailspinsForAppLaunches"
- "TB,V_enforceAppLaunchThreshold"
- "TB,V_forceAppLaunchDiagnostics"
- "TB,V_isEnabled"
- "TB,V_seedUserMode"
- "TB,V_shouldBeEnabled"
- "TB,V_underMemoryPressure"
- "TB,V_underThermalPressure"
- "TI,V_eventCount"
- "TI,V_successiveExtractorFailureCount"
- "TQ,R"
- "TQ,R,V_scenarioEndTime"
- "TQ,R,V_scenarioStartTime"
- "Tf,R,V_observedFps"
- "Tf,R,V_observedLatencyInMs"
- "Tf,R,V_targetFps"
- "Tf,V_targetLatencyInMs"
- "Ti"
- "Ti,R,V_appProcessID"
- "Ti,V_perDayEventCount"
- "Ti,V_perDayLogLimit"
- "Ti,V_perPeriodEventCount"
- "Ti,V_perPeriodLogLimit"
- "Tq,R,V_kpi"
- "UTF8String"
- "_abcHelper"
- "_allowList"
- "_animationConfigForWhitelistedCategories"
- "_animationConfigForWhitelistedNames"
- "_animationConfigForWhitelistedSubsystems"
- "_appBundleId"
- "_appName"
- "_appProcessID"
- "_avoidGeneratingTailspinsForAppLaunches"
- "_badConfigError"
- "_bundleIdForAppName"
- "_bundledIdLookupFailedrror"
- "_defaults"
- "_determineBootVolumeType"
- "_determineHardwareModel"
- "_enforceAppLaunchThreshold"
- "_eventCount"
- "_forceAppLaunchDiagnostics"
- "_generalSignpostHelper"
- "_hwModel"
- "_interval"
- "_isEnabled"
- "_issueCategory"
- "_kpi"
- "_lifecycleScenarios"
- "_logHandle"
- "_logger"
- "_machAbsTimeStart"
- "_metadata"
- "_monitorQueue"
- "_observedFps"
- "_observedLatencyInMs"
- "_osTransaction"
- "_perDayEventCount"
- "_perDayLogLimit"
- "_perDayTimer"
- "_perPeriodEventCount"
- "_perPeriodLogLimit"
- "_perPeriodTimer"
- "_perfCheckerErrors"
- "_periodLengthSec"
- "_periodicTimer"
- "_processingQueue"
- "_queue"
- "_responsivenessConfigForWhitelistedCategories"
- "_responsivenessConfigForWhitelistedNames"
- "_responsivenessConfigForWhitelistedSubsystems"
- "_scenario"
- "_scenarioEndTime"
- "_scenarioGroup"
- "_scenarioID"
- "_scenarioObjects"
- "_scenarioStartTime"
- "_seedUserMode"
- "_serialUtilityQueue"
- "_settingsChangedCallback"
- "_settingsChangedCallbackQueue"
- "_sharedConcurrentQueueAtBackground"
- "_sharedConcurrentQueueAtUtility"
- "_sharedSerialQueueAtUtility"
- "_shouldBeEnabled"
- "_signpostExtractor"
- "_sigtermSource"
- "_specialAppLaunchSignpostHelper"
- "_streamingStatistics"
- "_subsystemDict"
- "_successiveExtractorFailureCount"
- "_symptomsSignature"
- "_targetFps"
- "_targetLatencyInMs"
- "_timeOfLastExtractorFailure"
- "_titleText"
- "_totalCount"
- "_underMemoryPressure"
- "_underThermalPressure"
- "_workflowEventTrackers"
- "_workflowProvider"
- "_workflowResponsivenessHelper"
- "_wrTracker"
- "abcHelper"
- "addAllowlist:"
- "addObject:"
- "addObserverForName:object:queue:usingBlock:"
- "addSignpost:"
- "addSubsystem:category:"
- "allKeys"
- "allowList"
- "allowListForDiagnostics"
- "animationConfigForWhitelistedCategories"
- "animationConfigForWhitelistedNames"
- "animationConfigForWhitelistedSubsystems"
- "appBundleId"
- "appName"
- "appNameFromBundleId:"
- "appProcessID"
- "arrayWithObjects:count:"
- "attributes"
- "avoidGeneratingTailspinsForAppLaunches"
- "badConfigError"
- "beginEvent"
- "boolForKey:"
- "boolValue"
- "bootVolumeType"
- "bundleForClass:"
- "bundleIdForAppName"
- "bundleIdForProcessName:"
- "bundleWithPath:"
- "bundledIdLookupFailedrror"
- "category"
- "checkFramerateOfAnimationScenario:completionHandler:"
- "checkLatencyOfResponsivenessScenario:completionHandler:"
- "checkMonitoring:"
- "checkPerformanceOfScenarioReport:completionHandler:"
- "cleanupWorkflowResponsivenessDiagnosticsDirectory"
- "code"
- "collectTailspinForScenarioReport:tailspinFileDescriptor:completionHandler:"
- "containsObject:"
- "convertDictionaryToString:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataWithJSONObject:options:error:"
- "date"
- "dealloc"
- "defaultCenter"
- "description"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "didEndMonitoring"
- "disable"
- "durationMachContinuousTime"
- "durationMs"
- "durationSeconds"
- "emitTelemetry"
- "endEvent"
- "endMachContinuousTime"
- "errorWithDomain:code:userInfo:"
- "eventCount"
- "f"
- "f16@0:8"
- "f24@0:8@16"
- "floatValue"
- "forEachEnabledHelper:"
- "forEachHelper:"
- "forceAppLaunchDiagnostics"
- "frameRate"
- "framerateGoalsForSignpostInterval:"
- "gatherDiagnosticsIfNeeded"
- "generalSignpostHelper"
- "handleEmit:"
- "handleInterval:"
- "handleIntervalBegin:"
- "handleSignpost:"
- "hardwareModel"
- "hasPrefix:"
- "hash"
- "hw.model"
- "hwModel"
- "i"
- "i16@0:8"
- "i24@0:8@16"
- "infoDictionary"
- "init"
- "initForLiveStreamingWithWorkflow:timeoutQueue:eventCompletionCallback:"
- "initWithCapacity:"
- "initWithConfiguration:scenarioGroup:kpi:processBundleID:titleText:processName:processID:"
- "initWithData:encoding:"
- "initWithFormat:"
- "initWithLifecycleScenarioCategoryAndModelName:modelName:titleText:"
- "initWithPlatform:"
- "initWithScenario:"
- "initWithSignpostEvent:scenario:error:"
- "initWithSignpostInterval:scenario:error:"
- "initWithSuiteName:"
- "intValue"
- "internalResourceBundle"
- "interval"
- "invalidate"
- "isAnimationScenarioWhitelisted:error:"
- "isAppleInternal"
- "isEnabled"
- "isEqual:"
- "isEqualToString:"
- "isMemoryConstrained"
- "isResponsivenessScenarioWhitelisted:error:"
- "isSyntheticIntervalEvent"
- "issueCategoryForSignpostInterval:"
- "kpi"
- "kpiIsLatency:"
- "lastPathComponent"
- "latencyGoalsForSignpostInterval:"
- "length"
- "lifecycleScenarios"
- "loadWhitelist:platform:bundles:"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "logHandle"
- "logger"
- "mainBundle"
- "metadata"
- "monitorAppLaunchSignposts"
- "monitorQueue"
- "monitorSignposts:"
- "monitorWorkflowsWithDailyLogLimit:perPeriodLogLimit:periodLengthSec:"
- "name"
- "needsEnablementChange"
- "notifyWhenSettingsChanged:block:"
- "now"
- "number1Name"
- "number1Value"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observedFps"
- "observedLatencyInMs"
- "osBuild"
- "osTransaction"
- "passesSubsystem:category:"
- "pathForResource:ofType:"
- "perDayEventCount"
- "perDayLogLimit"
- "perDayTimer"
- "perPeriodEventCount"
- "perPeriodLogLimit"
- "perPeriodTimer"
- "perfCheckerErrors"
- "perfProblemDetected:tailspinFilenamePrefix:"
- "perfProblemDetectedOnMac:"
- "periodLengthSec"
- "postNotificationName:object:userInfo:"
- "processAppLaunch:tailspinFilenamePrefix:duration:andPID:reason:"
- "processBundleIdForSignpostInterval:"
- "processID"
- "processIdForSignpostEvent:"
- "processName"
- "processNotificationsWithIntervalTimeoutInSeconds:shouldCalculateAnimationFramerate:targetQueue:errorOut:"
- "processWhitelisted:error:"
- "processingQueue"
- "providerForAllWorkflowsWithQueue:callback:"
- "q16@0:8"
- "q24@0:8@16"
- "removeObjectForKey:"
- "reportError:report:completionHandler:"
- "reportFromSignpostEvent:error:"
- "reportFromSignpostInterval:error:"
- "reportLatencyToReceiveSignposts:"
- "reset"
- "resetCounts"
- "resetPerDayCounts"
- "resetPerPeriodCounts"
- "resetState"
- "responsivenessConfigForWhitelistedCategories"
- "responsivenessConfigForWhitelistedNames"
- "responsivenessConfigForWhitelistedSubsystems"
- "scanUpToString:intoString:"
- "scannerWithString:"
- "scenario"
- "scenarioEndTime"
- "scenarioForFrontboardLaunchWatchdog:"
- "scenarioFromSignpostEvent:error:"
- "scenarioFromSignpostInterval:error:"
- "scenarioGroup"
- "scenarioGroupForSignpostInterval:"
- "scenarioIdForSignpostEmittedEvent:"
- "scenarioIdForSignpostInterval:"
- "scenarioObjects"
- "scenarioStartTime"
- "scenarioWhitelisted:error:"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "scope"
- "seedUserMode"
- "serialUtilityQueue"
- "setAbcHelper:"
- "setAnimationConfigForWhitelistedCategories:"
- "setAnimationConfigForWhitelistedNames:"
- "setAnimationConfigForWhitelistedSubsystems:"
- "setAvoidGeneratingTailspinsForAppLaunches:"
- "setBadConfigError:"
- "setBeginEventProcessingBlock:"
- "setBundleIdForAppName:"
- "setBundledIdLookupFailedrror:"
- "setDateFormat:"
- "setEmitEventProcessingBlock:"
- "setEnforceAppLaunchThreshold:"
- "setEventCount:"
- "setForceAppLaunchDiagnostics:"
- "setGeneralSignpostHelper:"
- "setHwModel:"
- "setInterval:"
- "setIntervalCompletionProcessingBlock:"
- "setIsEnabled:"
- "setLifecycleScenarios:"
- "setLogHandle:"
- "setLogger:"
- "setMetadata:"
- "setMonitorQueue:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOsTransaction:"
- "setPerDayEventCount:"
- "setPerDayLogLimit:"
- "setPerDayTimer:"
- "setPerPeriodEventCount:"
- "setPerPeriodLogLimit:"
- "setPerPeriodTimer:"
- "setPerfCheckerErrors:"
- "setPeriodLengthSec:"
- "setProcessingCompletionBlock:"
- "setProcessingQueue:"
- "setResponsivenessConfigForWhitelistedCategories:"
- "setResponsivenessConfigForWhitelistedNames:"
- "setResponsivenessConfigForWhitelistedSubsystems:"
- "setScenarioObjects:"
- "setSeedUserMode:"
- "setSerialUtilityQueue:"
- "setSettingsChangedCallback:"
- "setSettingsChangedCallbackQueue:"
- "setSharedConcurrentQueueAtBackground:"
- "setSharedConcurrentQueueAtUtility:"
- "setSharedSerialQueueAtUtility:"
- "setShouldBeEnabled:"
- "setSignpostExtractor:"
- "setSpecialAppLaunchSignpostHelper:"
- "setStreamingStatistics:"
- "setSubsystemCategoryFilter:"
- "setSuccessiveExtractorFailureCount:"
- "setSymptomsSignature:"
- "setTargetLatencyInMs:"
- "setTimeOfLastExtractorFailure:"
- "setUnderMemoryPressure:"
- "setUnderThermalPressure:"
- "setWorkflowEventTrackers:"
- "setWorkflowProvider:"
- "setWorkflowResponsivenessHelper:"
- "setWrTracker:"
- "settingsChangedCallback"
- "settingsChangedCallbackQueue"
- "setupBundleIdWhitelists:bundles:"
- "setupRetryAfterFailure"
- "setupWhitelistedAnimationScenarios:bundles:"
- "setupWhitelistedResponsivenessScenarios:bundles:"
- "setupWhitelistedScenarios:bundles:"
- "shareSeedDiagnosticsWithABC:tailspinFilenamePrefix:"
- "sharedCache"
- "sharedConcurrentQueueAtBackground"
- "sharedConcurrentQueueAtUtility"
- "sharedDiagnosticsCollector"
- "sharedHelper"
- "sharedLogger"
- "sharedMonitor"
- "sharedPerfChecker"
- "sharedSerialQueueAtUtility"
- "shouldBeEnabled"
- "signpostExtractor"
- "snapshotWithSignature:duration:events:payload:actions:reply:"
- "specialAppLaunchSignpostHelper"
- "startMachContinuousTime"
- "stopMonitoringAppLaunchSignposts"
- "stopMonitoringSignposts"
- "stopMonitoringWorkflows"
- "stopProcessing"
- "streamingStatistics"
- "string1Value"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringValue"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringToIndex:"
- "subsystem"
- "subsystemForSignposts"
- "successiveExtractorFailureCount"
- "symptomsSignature"
- "symptomsSignatureForReport"
- "takeTransaction"
- "targetFps"
- "targetLatencyInMs"
- "timeIntervalSinceDate:"
- "timeOfLastExtractorFailure"
- "timeRecordedMachContinuousTime"
- "titleText"
- "triage:"
- "underMemoryPressure"
- "underThermalPressure"
- "unsignedLongLongValue"
- "updateAllowList"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8@16i24@?28"
- "v40@0:8q16@24@?32"
- "v56@0:8@16@24@32@40@48"
- "valueForKey:"
- "wantsAnimationFrameRate"
- "willStartMonitoring"
- "workflow"
- "workflowEventCompleted:completedWRTracker:"
- "workflowEventTrackers"
- "workflowIsUnderLimits:"
- "workflowProvider"
- "workflowResponsivenessHelper"
- "wrTracker"

```
