## SignpostCollection

> `/System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection`

```diff

-174.8.0.0.0
-  __TEXT.__text: 0x6d64
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x394
+197.0.0.0.0
+  __TEXT.__text: 0x6fa8
+  __TEXT.__objc_methlist: 0x3fc
   __TEXT.__const: 0x128
   __TEXT.__gcc_except_tab: 0x320
-  __TEXT.__cstring: 0xa06
-  __TEXT.__oslogstring: 0x2d6
-  __TEXT.__unwind_info: 0x228
-  __TEXT.__objc_classname: 0xbe
-  __TEXT.__objc_methname: 0x1c13
-  __TEXT.__objc_methtype: 0x22e
-  __TEXT.__objc_stubs: 0x1e20
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x340
+  __TEXT.__cstring: 0xa8d
+  __TEXT.__oslogstring: 0x328
+  __TEXT.__unwind_info: 0x220
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x398
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_selrefs: 0x958
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x700
-  __AUTH_CONST.__objc_const: 0x548
-  __AUTH.__objc_data: 0xa0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x760
+  __AUTH_CONST.__objc_const: 0x588
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x8
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x58
+  __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 679DD738-44B1-360E-A5D3-F5231DD176BD
-  Functions: 134
-  Symbols:   718
-  CStrings:  478
+  UUID: AF344C1D-CF82-3864-A651-9941BE417851
+  Functions: 145
+  Symbols:   792
+  CStrings:  158
 
Symbols:
+ +[SSPSMAggregation(FileReading) aggregationRetainingSlices:fromFilePath:startDate:endDate:errorOut:]
+ +[SignpostSupportObjectExtractor(AllFileReading) getDataSourceDateRange:earliestDateOut:latestDateOut:errorOut:]
+ -[SSPSMAggregation(FileReading) aggregateFromFilePath:startDate:endDate:errorOut:]
+ -[SignpostSupportObjectExtractor(AllFileReading) processFileWithPath:startDate:endDate:errorOut:]
+ -[SignpostSupportObjectExtractor(OSLogEventStreamProcessing) _setupLoggingSystemPredicates:]
+ -[SignpostSupportObjectExtractor(OSLogEventStreamProcessing) _shouldBuildEventWithProxy:shouldReport:]
+ -[SignpostSupportObjectExtractor(TraceReading) _finishProcessing]
+ -[SignpostSupportObjectExtractor(TraceReading) _finishProcessing].cold.1
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$_SSPSMAggregation
+ _OBJC_CLASS_$_SSPeriodicSystemMetricsReader
+ _SignpostSupportStringForDate
+ _SignpostSupportStringForDate.cold.1
+ _SignpostSupportStringForDate.formatter
+ _SignpostSupportStringForDate.onceToken
+ __OBJC_$_CATEGORY_CLASS_METHODS_SSPSMAggregation_$_FileReading
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_SSPSMAggregation_$_FileReading
+ __OBJC_$_CATEGORY_SSPSMAggregation_$_FileReading
+ ___112-[SignpostSupportObjectExtractor(OSLogEventStreamProcessing) _processLogEventStream:startDate:endDate:errorOut:]_block_invoke.3
+ ___82-[SSPSMAggregation(FileReading) aggregateFromFilePath:startDate:endDate:errorOut:]_block_invoke
+ ___82-[SSPSMAggregation(FileReading) aggregateFromFilePath:startDate:endDate:errorOut:]_block_invoke_2
+ ___SignpostSupportStringForDate_block_invoke
+ ___block_descriptor_40_e8_32s_e36_B16?0"SSHighCadenceSystemMetrics"8ls32l8
+ ___block_descriptor_40_e8_32s_e38_B16?0"SSMediumCadenceSystemMetrics"8ls32l8
+ ___block_literal_global.24
+ __signpost_debug_log
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_calculateLoggingSupportStreamPredicateFromFilters
+ _objc_msgSend$_finishProcessing
+ _objc_msgSend$_hasReportedStateBlocks
+ _objc_msgSend$_hasSignpostDependentProcessingBlock
+ _objc_msgSend$_setupLoggingSystemPredicates:
+ _objc_msgSend$_shouldBuildEventWithProxy:shouldReport:
+ _objc_msgSend$activityIdentifier
+ _objc_msgSend$addMetrics:
+ _objc_msgSend$aggregateFromFilePath:startDate:endDate:errorOut:
+ _objc_msgSend$animationIntervalCompletionProcessingBlock
+ _objc_msgSend$caresAboutSubsystem:category:pid:processName:
+ _objc_msgSend$date
+ _objc_msgSend$dedicatedExtractor
+ _objc_msgSend$deviceRebootedOrReadingSessionFinished:lastKnownDate:
+ _objc_msgSend$errorWithCode:description:subErrors:
+ _objc_msgSend$evaluateWithObject:
+ _objc_msgSend$filterPredicate
+ _objc_msgSend$fullFilterPredicate
+ _objc_msgSend$getDataSourceDateRange:earliestDateOut:latestDateOut:errorOut:
+ _objc_msgSend$hasOutstandingAnimations
+ _objc_msgSend$initRetainingSlices:
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$processFileWithPath:startDate:endDate:errorOut:
+ _objc_msgSend$reportedStateProcessor
+ _objc_msgSend$setBootUUID:
+ _objc_msgSend$setFormatOptions:
+ _objc_msgSend$setHighCadenceSystemMetricsBlock:
+ _objc_msgSend$setLastKnownDate:
+ _objc_msgSend$setLastKnownMCT:
+ _objc_msgSend$setMediumCadenceSystemMetricsBlock:
+ _objc_msgSend$setMessageSegments:
+ _objc_msgSend$setOsActivityId:
+ _objc_msgSend$setSizeBytes:
+ _objc_msgSend$setTranslatedClientDerivedFilterPredicate:
+ _objc_msgSend$size
+ _objc_msgSend$skipAnimationStateTrackingOptimization
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$translatedClientDerivedFilterPredicate
+ _objc_msgSend$underlyingErrors
+ _objc_msgSend$unprocessedClientDerivedFilterPredicate
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- GCC_except_table1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- ___112-[SignpostSupportObjectExtractor(OSLogEventStreamProcessing) _processLogEventStream:startDate:endDate:errorOut:]_block_invoke.2
- _objc_msgSend$_hasSignpostProcessingBlock
- _objc_msgSend$_loggingSupportStreamPredicateFromFiltersWithForLiveStreaming:
- _objc_msgSend$_shouldBuildEventWithPid:uniquePid:processName:subsystem:category:shouldReport:
- _objc_msgSend$finishProcessingSerializedData
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "B16@?0@\"SSHighCadenceSystemMetrics\"8"
+ "B16@?0@\"SSMediumCadenceSystemMetrics\"8"
+ "Called 'processingComplete' on an already finished SignpostSupportObjectExtractor"
+ "Error determining date range"
+ "Error processing"
+ "visionOS"
- ".cxx_destruct"
- "@\"NSMutableArray\""
- "@\"SignpostSerializationFilterConfiguration\""
- "@\"SignpostSupportExactProcessNameFilter\""
- "@\"SignpostSupportObjectExtractor\""
- "@\"SignpostSupportPIDFilter\""
- "@\"SignpostSupportSubsystemCategoryFilter\""
- "@\"SignpostSupportUniquePIDFilter\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8@16^@24"
- "@32@0:8@16d24"
- "@36@0:8@16d24B32"
- "@72@0:8@16d24B32Q36B44Q48@56@?64"
- "@?"
- "@?16@0:8"
- "AllFileReading"
- "B"
- "B16@0:8"
- "B32@0:8@16^@24"
- "B32@0:8Q16^@24"
- "B44@0:8Q16B24@28^@36"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16^@24^@32^@40"
- "Collection"
- "LogArchiveReading"
- "LoggingSupport"
- "Notifications"
- "OSLogEventStreamProcessing"
- "Q"
- "Q16@0:8"
- "SignpostSerializationFilterConfiguration"
- "SignpostSupportObjectSerializer"
- "T@\"NSMutableArray\",&,N,V_outstandingLogMessage"
- "T@\"NSMutableArray\",&,N,V_outstandingSignpostObjects"
- "T@\"SignpostSerializationFilterConfiguration\",&,N,V_filterConfiguration"
- "T@\"SignpostSupportExactProcessNameFilter\",&,N,V_processNameFilter"
- "T@\"SignpostSupportObjectExtractor\",&,N,V_extractor"
- "T@\"SignpostSupportPIDFilter\",&,N,V_pidFilter"
- "T@\"SignpostSupportSubsystemCategoryFilter\",&,N,V_subsystemCategoryFilter"
- "T@\"SignpostSupportUniquePIDFilter\",&,N,V_uniquePidFilter"
- "T@?,C,N"
- "T@?,C,N,V_serializedLogMessageBlock"
- "T@?,C,N,V_serializedSignpostEventBlock"
- "TB,N,V_redactPrivacySensitiveData"
- "TQ,N,V_maxBatchSize"
- "TQ,N,V_maxBytesSize"
- "TraceReading"
- "UTF8String"
- "_addListeningTimeTranslator:"
- "_checkDateRange:endDate:"
- "_checkForFormatStringFlags:shouldCompose:"
- "_checkProcessingConfiguration"
- "_dataArrayForSignpostSupportObjectArray:errorOut:"
- "_eventSourceForPath:errorOut:"
- "_extractor"
- "_filterConfiguration"
- "_fixupToSupportFramerateCalculation"
- "_globalNotificationDispatchQueue"
- "_grabMachTimesSnapshot"
- "_handleSignpostDescriptionPlaceholder:"
- "_handleSignpostTelemetryPlaceholder:"
- "_hasProcessingBlocks"
- "_hasSignpostProcessingBlock"
- "_isTrackingIntervals"
- "_key"
- "_liveStream"
- "_loggingSupportStreamPredicateFromFiltersWithForLiveStreaming:"
- "_maxBatchSize"
- "_maxBytesSize"
- "_nameStringFromSegment:"
- "_notificationTimeout"
- "_outstandingLogMessage"
- "_outstandingSignpostObjects"
- "_parseMetadataSegments:"
- "_pidFilter"
- "_populateMetrics"
- "_processLogEventStream:startDate:endDate:errorOut:"
- "_processNameFilter"
- "_processOSLogEventProxy:"
- "_processPowerNotificationOfType:withNotificationID:"
- "_processSignpostEvent:shouldReport:"
- "_processSignpostSupportLogMessage:"
- "_processStreamedOSLogEventProxy:shouldCalculateFramerate:"
- "_processTraceFileWithPath:startDate:endDate:errorOut:"
- "_processTraceUsingKtraceLoggingDataSource:startDate:endDate:errorOut:"
- "_processingCompleted:"
- "_redactPrivacySensitiveData"
- "_removeListeningTimeTranslator:"
- "_sanityCheckParameters"
- "_serializedLogMessageBlock"
- "_serializedSignpostEventBlock"
- "_shouldBuildEventWithPid:uniquePid:processName:subsystem:category:shouldReport:"
- "_shouldStopProcessing"
- "_snapshotMachTimesForAllListeners"
- "_subsystemCategoryFilter"
- "_timeTranslationLog"
- "_uniquePidFilter"
- "activate"
- "activateStreamFromDate:"
- "addObject:"
- "addObjectsFromArray:"
- "addTimestampPairWithMachAbsoluteTime:machContinuousTime:"
- "argument"
- "argumentAtIndex:"
- "argumentObject"
- "array"
- "arrayWithObjects:count:"
- "attributes"
- "availability"
- "backtrace"
- "bootUUID"
- "cachedTimebaseRatio"
- "category"
- "checkResourceIsReachableAndReturnError:"
- "compare:"
- "completionSemaphore"
- "composedMessage"
- "containsString:"
- "continuousNanosecondsSinceBoot"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "creatorProcessUniqueIdentifier"
- "currentBootUUID"
- "dataRepresentation"
- "dataRepresentationDuringMonitoring"
- "dateRangeOfLogArchiveWithPath:startDateOut:endDateOut:errorOut:"
- "decomposedMessage"
- "defaultManager"
- "deviceRebootProcessingBlock"
- "distantPast"
- "dropAccumulatedState"
- "errorWithCode:description:"
- "eventType"
- "extractor"
- "fileExistsAtPath:"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "filterConfiguration"
- "finishProcessingSerializedData"
- "firstDate"
- "flags"
- "frames"
- "getDataSourceDateRange:earliestDateOut:latestDateOut:errorsOut:"
- "imageOffset"
- "imageUUID"
- "init"
- "initWithArgumentObject:scalarType:typeNamespace:type:tokens:stringPrefix:privacy:"
- "initWithArray:copyItems:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithDataSourceDelegate:"
- "initWithKtraceFile:"
- "initWithLiveSource:"
- "initWithMaxEntries:"
- "initWithOSLogEventProxy:timebaseRatio:"
- "initWithOSLogEventProxy:timebaseRatio:shouldCompose:"
- "initWithOSLogEventProxy:timebaseRatio:shouldCompose:serialNumber:shouldCollectFrameInfo:timeoutInSec:timeoutHandlingQueue:timeoutHandlingBlock:"
- "initWithSource:"
- "initWithSource:skipNonSignpostFiles:"
- "initWithSubsystem:category:timebaseRatio:unixDate:unixTimeZone:"
- "initWithSubsystem:category:timebaseRatio:unixDate:unixTimeZone:stackFrames:"
- "initWithUUID:offset:"
- "intervalBuilder"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isMonitoringSleepWake"
- "isSyntheticIntervalEvent"
- "lastDate"
- "lastPathComponent"
- "length"
- "literalPrefixAtIndex:"
- "liveLocalStore"
- "localStore"
- "logMessageProcessingBlock"
- "logType"
- "machContinuousTimestamp"
- "matchingEventForEvent:removeIfFound:"
- "maxBatchSize"
- "maxBytesSize"
- "metadata"
- "metadataSegments"
- "newestDate"
- "notificationProcessingQueue"
- "numberWithUnsignedInteger:"
- "objectRepresentation"
- "oldestDate"
- "outstandingLogMessage"
- "outstandingSignpostObjects"
- "pathExtension"
- "pidFilter"
- "placeholderArrayWithOSLogEventProxy:"
- "placeholderAtIndex:"
- "placeholderCount"
- "predicateWithFormat:"
- "prepareWithCompletionHandler:"
- "privacy"
- "process"
- "processFileWithPath:startDate:endDate:errorsOut:"
- "processIdentifier"
- "processImagePath"
- "processImageUUID"
- "processLogArchiveWithPath:startDate:endDate:errorOut:"
- "processNameFilter"
- "processNotificationsWithIntervalTimeoutInSeconds:errorOut:"
- "processNotificationsWithIntervalTimeoutInSeconds:shouldCalculateAnimationFramerate:targetQueue:errorOut:"
- "processSerializedObjectsFromData:errorOut:"
- "processTraceFileWithPath:errorOut:"
- "processTraceFileWithPath:startDate:endDate:errorOut:"
- "processedEventCount"
- "reason"
- "redactPrivacySensitiveData"
- "removeAllObjects"
- "removeObject:"
- "scalarType"
- "senderImagePath"
- "senderImageUUID"
- "serialNumber"
- "serializeLogArchiveWithPath:startDate:endDate:errorOut:"
- "serializeNotificationsWithIntervalTimeoutInSeconds:errorOut:"
- "serializedLogMessageBlock"
- "serializedSignpostEventBlock"
- "set"
- "setAttributes:"
- "setBeginEventProcessingBlock:"
- "setCachedTimebaseRatio:"
- "setCurrentBootUUID:"
- "setDisableGeneratorProcessing:"
- "setEmitEventProcessingBlock:"
- "setEndEventProcessingBlock:"
- "setEventHandler:"
- "setEventType:"
- "setExtractor:"
- "setFilterConfiguration:"
- "setFilterPredicate:"
- "setFlags:"
- "setHasNonScalarDynamicData:"
- "setInvalidationHandler:"
- "setIsAnimationStart:"
- "setIsMonitoringSleepWake:"
- "setLogMessageProcessingBlock:"
- "setMaxBatchSize:"
- "setMaxBytesSize:"
- "setMaxEntries:"
- "setMessage:"
- "setMessageType:"
- "setMetadata:"
- "setMetadataSegments:"
- "setName:"
- "setNotificationProcessingQueue:"
- "setNumber1Name:"
- "setNumber1Value:"
- "setNumber2Name:"
- "setNumber2Value:"
- "setObject:forKeyedSubscript:"
- "setOutstandingLogMessage:"
- "setOutstandingSignpostObjects:"
- "setOverridingBeginMachContinuousTime:"
- "setOverridingEmitMachContinuousTime:"
- "setOverridingEndMachContinuousTime:"
- "setPidFilter:"
- "setProcessID:"
- "setProcessImagePath:"
- "setProcessImageUUID:"
- "setProcessName:"
- "setProcessNameFilter:"
- "setProcessUniqueID:"
- "setProcessedEventCount:"
- "setProcessingCompletionBlock:"
- "setQueue:"
- "setRedactPrivacySensitiveData:"
- "setScope:"
- "setSenderImagePath:"
- "setSenderImageUUID:"
- "setSerialNumber:"
- "setSerializedLogMessageBlock:"
- "setSerializedSignpostEventBlock:"
- "setSignpostId:"
- "setString1Name:"
- "setString1Value:"
- "setString2Name:"
- "setString2Value:"
- "setSubsystemCategoryFilter:"
- "setTelemetryEnabled:"
- "setThreadID:"
- "setTimeoutSource:"
- "setUniquePidFilter:"
- "setUpgradeConfirmationHandler:"
- "set_liveStream:"
- "set_machContinuousTimestamp:"
- "set_notificationTimeout:"
- "set_shouldStopProcessing:"
- "set_stopProcessingBlock:"
- "shouldComposeMetadataString"
- "signpostIdentifier"
- "signpostName"
- "signpostScope"
- "signpostType"
- "startMonitoringSleepWake"
- "state"
- "stopMonitoringSleepWake"
- "stopProcessing"
- "storeWithArchiveURL:"
- "stringPrefix"
- "stringValue"
- "stringWithFormat:"
- "subarrayWithRange:"
- "subsystem"
- "subsystemCategoryFilter"
- "threadIdentifier"
- "timeIntervalSince1970"
- "timedOutBeginEventProcessingBlock"
- "timeoutSource"
- "tokens"
- "type"
- "typeNamespace"
- "uniquePidFilter"
- "unixDate"
- "unixTimeZone"
- "unsignedLongLongValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v28@0:8@16B24"
- "v28@0:8I16q20"

```
