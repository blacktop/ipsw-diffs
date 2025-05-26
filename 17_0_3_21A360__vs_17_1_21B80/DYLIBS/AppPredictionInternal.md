## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-541.0.5.0.0
-  __TEXT.__text: 0x474434
-  __TEXT.__auth_stubs: 0x3110
-  __TEXT.__objc_methlist: 0x39290
-  __TEXT.__const: 0x2644
-  __TEXT.__cstring: 0x57332
-  __TEXT.__oslogstring: 0x38e4b
-  __TEXT.__gcc_except_tab: 0xcf08
+541.5.2.0.1
+  __TEXT.__text: 0x4727e0
+  __TEXT.__auth_stubs: 0x30f0
+  __TEXT.__objc_methlist: 0x39088
+  __TEXT.__const: 0x2654
+  __TEXT.__cstring: 0x572f2
+  __TEXT.__oslogstring: 0x38e2b
+  __TEXT.__gcc_except_tab: 0xcf30
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0xd4f

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xea60
+  __TEXT.__unwind_info: 0xe998
   __TEXT.__eh_frame: 0x1aa8
-  __TEXT.__objc_classname: 0x8ef5
-  __TEXT.__objc_methname: 0xaf383
-  __TEXT.__objc_methtype: 0x19a60
-  __TEXT.__objc_stubs: 0x4e7e0
+  __TEXT.__objc_classname: 0x8eb6
+  __TEXT.__objc_methname: 0xaf07f
+  __TEXT.__objc_methtype: 0x19a53
+  __TEXT.__objc_stubs: 0x4e180
   __DATA_CONST.__got: 0xaa8
-  __DATA_CONST.__const: 0xbab0
-  __DATA_CONST.__objc_classlist: 0x1fc8
+  __DATA_CONST.__const: 0xbaa8
+  __DATA_CONST.__objc_classlist: 0x1fb0
   __DATA_CONST.__objc_catlist: 0x170
-  __DATA_CONST.__objc_protolist: 0x4e0
+  __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x73408
-  __DATA_CONST.__objc_selrefs: 0x1c7a0
+  __DATA_CONST.__objc_const: 0x72bc0
+  __DATA_CONST.__objc_selrefs: 0x1c6a0
   __DATA_CONST.__objc_arraydata: 0x13c8
-  __AUTH_CONST.__objc_const: 0x16f48
-  __AUTH_CONST.__cfstring: 0x3b140
+  __AUTH_CONST.__objc_const: 0x16de0
+  __AUTH_CONST.__cfstring: 0x3b060
   __AUTH_CONST.__const: 0x7878
-  __AUTH_CONST.__objc_intobj: 0x35a0
+  __AUTH_CONST.__objc_intobj: 0x35b8
   __AUTH_CONST.__objc_arrayobj: 0x1188
   __AUTH_CONST.__auth_ptr: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0x18a0
-  __AUTH.__objc_data: 0x6128
+  __AUTH_CONST.__auth_got: 0x1890
+  __AUTH.__objc_data: 0x6178
   __AUTH.__data: 0x1c80
   __DATA.__objc_protorefs: 0xb0
-  __DATA.__objc_classrefs: 0x2cd8
-  __DATA.__objc_superrefs: 0x15f0
-  __DATA.__objc_ivar: 0x4e5c
+  __DATA.__objc_classrefs: 0x2cb8
+  __DATA.__objc_superrefs: 0x15e0
+  __DATA.__objc_ivar: 0x4e38
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x3d30
+  __DATA.__data: 0x3cd0
   __DATA.__bss: 0x1b10
   __DATA.__common: 0x70
-  __DATA_DIRTY.__objc_data: 0xdea0
+  __DATA_DIRTY.__objc_data: 0xdd60
   __DATA_DIRTY.__data: 0x710
-  __DATA_DIRTY.__bss: 0xb08
+  __DATA_DIRTY.__bss: 0xaf8
   __DATA_DIRTY.__common: 0x60
   - /AppleInternal/Library/Frameworks/ProactiveTimeIntelligence.framework/ProactiveTimeIntelligence
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26281
-  Symbols:   78565
-  CStrings:  35960
+  Functions: 26233
+  Symbols:   78366
+  CStrings:  35908
 
Symbols:
+ +[ATXComplicationSuggestionHeuristics _numBluetoothConnectionsOverLastWeek]
+ -[ATXAnchorModelPredictionScheduler _cache]
+ -[ATXAnchorModelPredictionScheduler _readPredictionsFromCache]
+ -[ATXComplicationSuggestionHeuristics flushCache]
+ -[ATXComplicationSuggestionHeuristicsCache numBluetoothConnectionsOverLastWeek]
+ -[ATXComplicationSuggestionHeuristicsCache numCalendarEventsOverLastAndNextWeek]
+ -[ATXComplicationSuggestionHeuristicsCache numRemindersOverLastWeek]
+ -[ATXComplicationSuggestionHeuristicsCache setNumBluetoothConnectionsOverLastWeek:]
+ -[ATXComplicationSuggestionHeuristicsCache setNumCalendarEventsOverLastAndNextWeek:]
+ -[ATXComplicationSuggestionHeuristicsCache setNumRemindersOverLastWeek:]
+ -[ATXNotificationsSuggestion initWithSuggestionType:notificationsHistogram:applaunchHistogram:dataStore:aggdlogger:]
+ -[_ATXDataStore migration_purgeExpensiveCachesFromUserDefaults]
+ GCC_except_table561
+ GCC_except_table566
+ GCC_except_table587
+ _OBJC_CLASS_$_ATXComplicationSuggestionHeuristicsCache
+ _OBJC_CLASS_$__PASLazyPurgeableResult
+ _OBJC_IVAR_$_ATXComplicationSuggestionHeuristics._cache
+ _OBJC_IVAR_$_ATXComplicationSuggestionHeuristicsCache._numBluetoothConnectionsOverLastWeek
+ _OBJC_IVAR_$_ATXComplicationSuggestionHeuristicsCache._numCalendarEventsOverLastAndNextWeek
+ _OBJC_IVAR_$_ATXComplicationSuggestionHeuristicsCache._numRemindersOverLastWeek
+ _OBJC_METACLASS_$_ATXComplicationSuggestionHeuristicsCache
+ __OBJC_$_INSTANCE_METHODS_ATXComplicationSuggestionHeuristicsCache
+ __OBJC_$_INSTANCE_VARIABLES_ATXComplicationSuggestionHeuristicsCache
+ __OBJC_$_PROP_LIST_ATXComplicationSuggestionHeuristicsCache
+ __OBJC_CLASS_RO_$_ATXComplicationSuggestionHeuristicsCache
+ __OBJC_METACLASS_RO_$_ATXComplicationSuggestionHeuristicsCache
+ ___49-[ATXComplicationSuggestionHeuristics flushCache]_block_invoke
+ ___53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.137
+ ___53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.137.cold.1
+ ___53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.138
+ ___53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.138.cold.1
+ ___66+[ATXComplicationSuggestionHeuristics _countedHomeAccessoryEvents]_block_invoke.137
+ ___66+[ATXComplicationSuggestionHeuristics _countedHomeAccessoryEvents]_block_invoke.137.cold.1
+ ___75+[ATXComplicationSuggestionHeuristics _numBluetoothConnectionsOverLastWeek]_block_invoke
+ ___75+[ATXComplicationSuggestionHeuristics _numBluetoothConnectionsOverLastWeek]_block_invoke.127
+ ___75+[ATXComplicationSuggestionHeuristics _numBluetoothConnectionsOverLastWeek]_block_invoke.cold.1
+ ___75-[ATXBiomePrivacyPruner pruneWithStreamIdentifier:activity:config:endTime:]_block_invoke.78
+ ___block_descriptor_32_e47_"ATXComplicationSuggestionHeuristicsCache"8?0l
+ ___block_descriptor_32_e76_"BPSPublisher"16?0"ATXProactiveSuggestionShadowLoggingContextEventTuple"8l
+ ___block_literal_global.1083
+ ___block_literal_global.1088
+ ___block_literal_global.136
+ ___block_literal_global.249
+ ___block_literal_global.493
+ ___block_literal_global.497
+ ___block_literal_global.500
+ ___block_literal_global.505
+ ___block_literal_global.509
+ ___block_literal_global.513
+ ___block_literal_global.517
+ ___block_literal_global.521
+ ___block_literal_global.525
+ ___block_literal_global.537
+ ___block_literal_global.542
+ ___block_literal_global.546
+ ___block_literal_global.557
+ ___block_literal_global.560
+ ___block_literal_global.565
+ ___block_literal_global.570
+ ___block_literal_global.573
+ ___block_literal_global.581
+ ___block_literal_global.612
+ ___block_literal_global.618
+ ___block_literal_global.622
+ ___block_literal_global.626
+ ___block_literal_global.634
+ ___block_literal_global.639
+ ___block_literal_global.649
+ ___block_literal_global.653
+ ___block_literal_global.657
+ ___block_literal_global.661
+ ___block_literal_global.665
+ ___block_literal_global.671
+ ___block_literal_global.677
+ ___block_literal_global.680
+ ___block_literal_global.695
+ ___block_literal_global.700
+ ___block_literal_global.703
+ ___block_literal_global.706
+ ___block_literal_global.712
+ ___block_literal_global.720
+ ___block_literal_global.724
+ ___block_literal_global.729
+ ___block_literal_global.738
+ ___registerForFaceSuggestionsCTSJob_block_invoke.640
+ ___registerForFaceSuggestionsCTSJob_block_invoke.640.cold.1
+ ___registerForFaceSuggestionsCTSJob_block_invoke.644
+ ___registerForFaceSuggestionsCTSJob_block_invoke.644.cold.1
+ ___registerForFaceSuggestionsCTSJob_block_invoke.644.cold.2
+ ___registerForNotificationAndSuggestionDatastorePruning_block_invoke.698
+ __unnamed_array_storage.590
+ __unnamed_array_storage.608
+ __unnamed_array_storage.810
+ _objc_msgSend$Bluetooth
+ _objc_msgSend$Wireless
+ _objc_msgSend$_readPredictionsFromCache
+ _objc_msgSend$flushCache
+ _objc_msgSend$initWithBlock:idleTimeout:
+ _objc_msgSend$initWithSuggestionType:notificationsHistogram:applaunchHistogram:dataStore:aggdlogger:
+ _objc_msgSend$numBluetoothConnectionsOverLastWeek
+ _objc_msgSend$numCalendarEventsOverLastAndNextWeek
+ _objc_msgSend$numRemindersOverLastWeek
+ _objc_msgSend$result
+ _objc_msgSend$setNumBluetoothConnectionsOverLastWeek:
+ _objc_msgSend$setNumCalendarEventsOverLastAndNextWeek:
+ _objc_msgSend$setNumRemindersOverLastWeek:
+ _objc_msgSend$setStoreLocationOption:
- +[ATXNotificationsLogger sharedInstance]
- +[ATXPeriodicLogger getEnrollmentRate]
- +[ATXPeriodicLogger readDateFromDefaultsForKey:]
- +[ATXPeriodicLogger readEnrollmentFromDefaults]
- +[ATXPeriodicLogger readLastEnrolledFromDefaults]
- +[ATXPeriodicLogger readLastSentFromDefaults]
- +[_ATXObjectLogger logJSONObjectforNotificationLogDictionary:]
- +[_ATXObjectLogger logJSONObjectforSessionLogDictionary:BugID:Prefix:]
- +[_ATXObjectLogger logJSONObjectforSessionLogDictionary:BugID:Prefix:].cold.1
- -[ATXAnchorModelPredictionScheduler deserializePredictionsDataOrInitializeDictionary:]
- -[ATXAnchorModelPredictionScheduler deserializePredictionsDataOrInitializeDictionary:].cold.1
- -[ATXAnchorModelPredictionScheduler deserializePredictionsDataOrInitializeDictionary:].cold.2
- -[ATXAnchorModelPredictionScheduler readPredictionsFromUserDefaults]
- -[ATXAnchorModelPredictionScheduler serializePredictions:]
- -[ATXAnchorModelPredictionScheduler serializePredictions:].cold.1
- -[ATXAnchorModelPredictionScheduler writePredictionsToUserDefaults:]
- -[ATXAppIconStateLogger getMetrics]
- -[ATXAppIconStateLogger setEnabled:]
- -[ATXAppLaunchLogger getMetrics]
- -[ATXAppLaunchLogger setEnabled:]
- -[ATXComplicationSuggestionHeuristics _numBluetoothConnectionsOverLastWeek]
- -[ATXNotificationsLogger .cxx_destruct]
- -[ATXNotificationsLogger init]
- -[ATXNotificationsLogger samplingRateForLogType:]
- -[ATXNotificationsLogger samplingRateFromParsecBag]
- -[ATXNotificationsLogger submitWithProtobuf:logtype:]
- -[ATXNotificationsSettingsLogger logNotificationSettingsWithActivity:]
- -[ATXNotificationsSuggestion initWithSuggestionType:notificationsHistogram:applaunchHistogram:dataStore:notificationsLogger:aggdlogger:]
- -[ATXNotificationsSuggestion logRTTOutcomeWithBundleId:topic:rttOutcome:]
- -[ATXPeriodicLogger .cxx_destruct]
- -[ATXPeriodicLogger clearUserId]
- -[ATXPeriodicLogger compileAndSendMetrics:]
- -[ATXPeriodicLogger compileLog]
- -[ATXPeriodicLogger convertDictionaryToDataUnits:]
- -[ATXPeriodicLogger determineEnrollment]
- -[ATXPeriodicLogger generateUserId]
- -[ATXPeriodicLogger getEnrollment]
- -[ATXPeriodicLogger getLastEnrolled]
- -[ATXPeriodicLogger getLastSent]
- -[ATXPeriodicLogger getUserId]
- -[ATXPeriodicLogger hasEnrollmentExpired:]
- -[ATXPeriodicLogger initWithSources:uploadInterval:enrollmentPeriod:enrollmentRate:]
- -[ATXPeriodicLogger init]
- -[ATXPeriodicLogger isItTimeYet:]
- -[ATXPeriodicLogger overrideEnrollmentRate:]
- -[ATXPeriodicLogger sendMetricsAtThisTime:]
- -[ATXPeriodicLogger sendMetricsIfNeededAtThisTime:]
- -[ATXPeriodicLogger sendMetricsIfNeeded]
- -[ATXPeriodicLogger setDate:forKey:]
- -[ATXPeriodicLogger setEnabledOnSourcesTo:]
- -[ATXPeriodicLogger setEnrollment:]
- -[ATXPeriodicLogger setLastEnrolledToTime:]
- -[ATXPeriodicLogger setLastSentToTime:]
- -[ATXPeriodicLogger submit:]
- GCC_except_table560
- GCC_except_table565
- GCC_except_table586
- _ATXNRTOutcomeToSettingResponse
- _OBJC_CLASS_$_ATXAppIconStateLogger
- _OBJC_CLASS_$_ATXNotificationsLogger
- _OBJC_CLASS_$_ATXPeriodicLogger
- _OBJC_CLASS_$_PARSession
- _OBJC_CLASS_$_SFCustomFeedback
- _OBJC_CLASS_$__ATXObjectLogger
- _OBJC_IVAR_$_ATXComplicationSuggestionHeuristics._bluetoothDataProvider
- _OBJC_IVAR_$_ATXComplicationSuggestionHeuristics._duetHelper
- _OBJC_IVAR_$_ATXNotificationRecorder._logger
- _OBJC_IVAR_$_ATXNotificationsLogger._queue
- _OBJC_IVAR_$_ATXNotificationsLogger._standardSamplingRate
- _OBJC_IVAR_$_ATXNotificationsSuggestion._logger
- _OBJC_IVAR_$_ATXPeriodicLogger._enrolled
- _OBJC_IVAR_$_ATXPeriodicLogger._enrollmentPeriod
- _OBJC_IVAR_$_ATXPeriodicLogger._enrollmentRate
- _OBJC_IVAR_$_ATXPeriodicLogger._lastEnrolled
- _OBJC_IVAR_$_ATXPeriodicLogger._lastSent
- _OBJC_IVAR_$_ATXPeriodicLogger._sources
- _OBJC_IVAR_$_ATXPeriodicLogger._uploadInterval
- _OBJC_METACLASS_$_ATXAppIconStateLogger
- _OBJC_METACLASS_$_ATXNotificationsLogger
- _OBJC_METACLASS_$_ATXPeriodicLogger
- _OBJC_METACLASS_$__ATXObjectLogger
- _OSAWriteLogForSubmission
- __OBJC_$_CLASS_METHODS_ATXNotificationsLogger
- __OBJC_$_CLASS_METHODS_ATXPeriodicLogger
- __OBJC_$_CLASS_METHODS__ATXObjectLogger
- __OBJC_$_INSTANCE_METHODS_ATXAppIconStateLogger
- __OBJC_$_INSTANCE_METHODS_ATXNotificationsLogger
- __OBJC_$_INSTANCE_METHODS_ATXPeriodicLogger
- __OBJC_$_INSTANCE_VARIABLES_ATXNotificationsLogger
- __OBJC_$_INSTANCE_VARIABLES_ATXPeriodicLogger
- __OBJC_$_PROP_LIST_ATXAppIconStateLogger
- __OBJC_$_PROP_LIST_ATXAppLaunchLogger
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ATXPeriodicLoggerSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_ATXPeriodicLoggerSource
- __OBJC_$_PROTOCOL_REFS_ATXPeriodicLoggerSource
- __OBJC_CLASS_PROTOCOLS_$_ATXAppIconStateLogger
- __OBJC_CLASS_PROTOCOLS_$_ATXAppLaunchLogger
- __OBJC_CLASS_RO_$_ATXAppIconStateLogger
- __OBJC_CLASS_RO_$_ATXNotificationsLogger
- __OBJC_CLASS_RO_$_ATXPeriodicLogger
- __OBJC_CLASS_RO_$__ATXObjectLogger
- __OBJC_LABEL_PROTOCOL_$_ATXPeriodicLoggerSource
- __OBJC_METACLASS_RO_$_ATXAppIconStateLogger
- __OBJC_METACLASS_RO_$_ATXNotificationsLogger
- __OBJC_METACLASS_RO_$_ATXPeriodicLogger
- __OBJC_METACLASS_RO_$__ATXObjectLogger
- __OBJC_PROTOCOL_$_ATXPeriodicLoggerSource
- ___32-[ATXAppLaunchLogger getMetrics]_block_invoke
- ___32-[ATXAppLaunchLogger getMetrics]_block_invoke_2
- ___33-[ATXAppLaunchLogger setEnabled:]_block_invoke
- ___40+[ATXNotificationsLogger sharedInstance]_block_invoke
- ___53-[ATXNotificationsLogger submitWithProtobuf:logtype:]_block_invoke
- ___53-[ATXNotificationsLogger submitWithProtobuf:logtype:]_block_invoke.cold.1
- ___53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.107
- ___53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.107.cold.1
- ___53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.108
- ___53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.108.cold.1
- ___66+[ATXComplicationSuggestionHeuristics _countedHomeAccessoryEvents]_block_invoke.113
- ___66+[ATXComplicationSuggestionHeuristics _countedHomeAccessoryEvents]_block_invoke.113.cold.1
- ___70+[_ATXObjectLogger logJSONObjectforSessionLogDictionary:BugID:Prefix:]_block_invoke
- ___block_descriptor_32_e78_"<BPSPublisher>"16?0"ATXProactiveSuggestionShadowLoggingContextEventTuple"8l
- ___block_descriptor_40_e8_32s_e22_v16?0"NSFileHandle"8ls32l8
- ___block_literal_global.1077
- ___block_literal_global.1082
- ___block_literal_global.219
- ___block_literal_global.495
- ___block_literal_global.499
- ___block_literal_global.503
- ___block_literal_global.506
- ___block_literal_global.511
- ___block_literal_global.515
- ___block_literal_global.519
- ___block_literal_global.523
- ___block_literal_global.527
- ___block_literal_global.538
- ___block_literal_global.544
- ___block_literal_global.549
- ___block_literal_global.553
- ___block_literal_global.564
- ___block_literal_global.567
- ___block_literal_global.572
- ___block_literal_global.577
- ___block_literal_global.580
- ___block_literal_global.588
- ___block_literal_global.619
- ___block_literal_global.625
- ___block_literal_global.629
- ___block_literal_global.633
- ___block_literal_global.637
- ___block_literal_global.641
- ___block_literal_global.646
- ___block_literal_global.656
- ___block_literal_global.660
- ___block_literal_global.664
- ___block_literal_global.668
- ___block_literal_global.672
- ___block_literal_global.678
- ___block_literal_global.694
- ___block_literal_global.698
- ___block_literal_global.702
- ___block_literal_global.707
- ___block_literal_global.710
- ___block_literal_global.713
- ___block_literal_global.719
- ___block_literal_global.723
- ___block_literal_global.727
- ___block_literal_global.731
- ___block_literal_global.736
- ___block_literal_global.745
- ___registerForFaceSuggestionsCTSJob_block_invoke.647
- ___registerForFaceSuggestionsCTSJob_block_invoke.647.cold.1
- ___registerForFaceSuggestionsCTSJob_block_invoke.651
- ___registerForFaceSuggestionsCTSJob_block_invoke.651.cold.1
- ___registerForFaceSuggestionsCTSJob_block_invoke.651.cold.2
- ___registerForNotificationAndSuggestionDatastorePruning_block_invoke.705
- ___registerForNotificationSettingsUploadCTSJob_block_invoke
- __unnamed_array_storage.21
- __unnamed_array_storage.597
- __unnamed_array_storage.615
- _objc_msgSend$aggregate
- _objc_msgSend$bag
- _objc_msgSend$clearUserId
- _objc_msgSend$compileAndSendMetrics:
- _objc_msgSend$compileLog
- _objc_msgSend$convertDictionaryToDataUnits:
- _objc_msgSend$defaultPeriodicLoggerEnrollmentPeriodSeconds
- _objc_msgSend$defaultPeriodicLoggerEnrollmentRate
- _objc_msgSend$defaultPeriodicLoggerUploadIntervalSeconds
- _objc_msgSend$deserializePredictionsDataOrInitializeDictionary:
- _objc_msgSend$determineEnrollment
- _objc_msgSend$duetExpertCustomFeedbackSamplingPercentage
- _objc_msgSend$generateUserId
- _objc_msgSend$getEnrollment
- _objc_msgSend$getEnrollmentRate
- _objc_msgSend$getLastEnrolled
- _objc_msgSend$getLastSent
- _objc_msgSend$getMetrics
- _objc_msgSend$getSamplingRate
- _objc_msgSend$getUserId
- _objc_msgSend$hasEnrollmentExpired:
- _objc_msgSend$initWithSources:uploadInterval:enrollmentPeriod:enrollmentRate:
- _objc_msgSend$initWithSuggestionType:notificationsHistogram:applaunchHistogram:dataStore:notificationsLogger:aggdlogger:
- _objc_msgSend$initWithType:data:
- _objc_msgSend$isDNUEnabled
- _objc_msgSend$isItTimeYet:
- _objc_msgSend$logJSONObjectforNotificationLogDictionary:
- _objc_msgSend$logJSONObjectforSessionLogDictionary:BugID:Prefix:
- _objc_msgSend$logNotificationSettingsWithActivity:
- _objc_msgSend$logRTTOutcomeWithBundleId:topic:rttOutcome:
- _objc_msgSend$message:topic:response:
- _objc_msgSend$notificationsAppSamplingRate
- _objc_msgSend$notificationsCustomerSamplingRate
- _objc_msgSend$notificationsInternalSamplingRate
- _objc_msgSend$notificationsSeedSamplingRate
- _objc_msgSend$numberOfApps
- _objc_msgSend$numberOfFolders
- _objc_msgSend$numberOfPages
- _objc_msgSend$readDateFromDefaultsForKey:
- _objc_msgSend$readEnrollmentFromDefaults
- _objc_msgSend$readLastEnrolledFromDefaults
- _objc_msgSend$readLastSentFromDefaults
- _objc_msgSend$readPredictionsFromUserDefaults
- _objc_msgSend$rttOutcomeLogger
- _objc_msgSend$samplingRateForLogType:
- _objc_msgSend$samplingRateFromParsecBag
- _objc_msgSend$sendCustomFeedback:
- _objc_msgSend$sendMetricsAtThisTime:
- _objc_msgSend$sendMetricsIfNeeded
- _objc_msgSend$sendMetricsIfNeededAtThisTime:
- _objc_msgSend$serializePredictions:
- _objc_msgSend$setDataUnits:
- _objc_msgSend$setDate:forKey:
- _objc_msgSend$setEnabledOnSourcesTo:
- _objc_msgSend$setEnrollment:
- _objc_msgSend$setLastEnrolledToTime:
- _objc_msgSend$setLastSentToTime:
- _objc_msgSend$setPeriodEnd:
- _objc_msgSend$setPeriodStart:
- _objc_msgSend$setValue:
- _objc_msgSend$sharedSession
- _objc_msgSend$submit:
- _objc_msgSend$submitWithProtobuf:logtype:
- _objc_msgSend$wrapLog:
- _objc_msgSend$writePredictionsToUserDefaults:
CStrings:
+ "@\"<ATXClientModelCacheManagerProtocol>\""
+ "@\"ATXComplicationSuggestionHeuristicsCache\"8@?0"
+ "@\"BPSPublisher\"16@?0@\"ATXProactiveSuggestionShadowLoggingContextEventTuple\"8"
+ "@\"NSString\"24@0:8@\"NSString\"16"
+ "@\"_PASLazyPurgeableResult\""
+ "@56@0:8q16@24@32@40@48"
+ "ATXComplicationSuggestionHeuristicsCache"
+ "Bluetooth"
+ "Could not query Bluetooth connected events for complication heuristics: %@"
+ "Deleting all trained relevance models for migration"
+ "Donation Processing - Tried to add duplicate entry to alog table for BundleId: %@ of Action Type: %{sensitive}@ with UUID: %@"
+ "Pruning tombstones for stream identifier: %@ based on endTime: %f"
+ "Purging expensive caches from user defaults"
+ "Received location, %{sensitive}f, %{sensitive}f"
+ "Removed %d tombstone events for stream identifier: %@"
+ "TQ,N,V_numBluetoothConnectionsOverLastWeek"
+ "TQ,N,V_numCalendarEventsOverLastAndNextWeek"
+ "TQ,N,V_numRemindersOverLastWeek"
+ "Wireless"
+ "_readPredictionsFromCache"
+ "anchorModelSchedulerCurrentPredictions"
+ "cached anchor model predictions"
+ "cachedFamilyCircle"
+ "flushCache"
+ "initWithBlock:idleTimeout:"
+ "initWithSuggestionType:notificationsHistogram:applaunchHistogram:dataStore:aggdlogger:"
+ "migration_purgeExpensiveCachesFromUserDefaults"
+ "numBluetoothConnectionsOverLastWeek"
+ "numCalendarEventsOverLastAndNextWeek"
+ "numRemindersOverLastWeek"
+ "setNumBluetoothConnectionsOverLastWeek:"
+ "setNumCalendarEventsOverLastAndNextWeek:"
+ "setNumRemindersOverLastWeek:"
+ "setStoreLocationOption:"
- "229"
- "@\"<BPSPublisher>\"16@?0@\"ATXProactiveSuggestionShadowLoggingContextEventTuple\"8"
- "@\"ATXBluetoothDuetDataProvider\""
- "@\"ATXClientModelCacheManager\""
- "@\"ATXNotificationsLogger\""
- "@48@0:8@16d24d32d40"
- "@64@0:8q16@24@32@40@48@56"
- "ATXAppIconStateLogger"
- "ATXId"
- "ATXNotificationsLogger"
- "ATXPeriodicLogger"
- "ATXPeriodicLoggerSource"
- "DELETE FROM launches"
- "Deleting all trained relevance models for migration."
- "Donation Processing - Tried to add duplicate entry to alog table for BundleId:%@ of Action Type:%@ with UUID: %@"
- "NumApps"
- "NumFolders"
- "NumPages"
- "Received location, %@"
- "Running notifications settings logging..."
- "SELECT launchType, count(*) FROM launches GROUP BY launchType"
- "Scheduler: Unable to deserialize predictions data because it was nil"
- "Scheduler: Unable to get predictions from defaults: %@"
- "Scheduler: Unable to serialize prediction data. Error: %@"
- "_ATXObjectLogger"
- "_bluetoothDataProvider"
- "_enrolled"
- "_enrollmentPeriod"
- "_enrollmentRate"
- "_lastEnrolled"
- "_lastSent"
- "_logger"
- "_standardSamplingRate"
- "_uploadInterval"
- "bag"
- "clearUserId"
- "com.apple.duetexpertd.notificationsettinglogging"
- "compileAndSendMetrics:"
- "compileLog"
- "convertDictionaryToDataUnits:"
- "deserializePredictionsDataOrInitializeDictionary:"
- "determineEnrollment"
- "duetExpertCustomFeedbackSamplingPercentage"
- "generateUserId"
- "getEnrollment"
- "getEnrollmentRate"
- "getLastEnrolled"
- "getLastSent"
- "getMetrics"
- "getUserId"
- "hasEnrollmentExpired:"
- "initWithSources:uploadInterval:enrollmentPeriod:enrollmentRate:"
- "initWithSuggestionType:notificationsHistogram:applaunchHistogram:dataStore:notificationsLogger:aggdlogger:"
- "initWithType:data:"
- "isDNUEnabled"
- "isItTimeYet:"
- "lastSent"
- "logJSONObjectforNotificationLogDictionary:"
- "logJSONObjectforSessionLogDictionary:BugID:Prefix:"
- "logNotificationSettingsWithActivity:"
- "logRTTOutcomeWithBundleId:topic:rttOutcome:"
- "overrideEnrollmentRate:"
- "periodicLogEnrolled"
- "proactive_notification"
- "readDateFromDefaultsForKey:"
- "readEnrollmentFromDefaults"
- "readLastEnrolledFromDefaults"
- "readLastSentFromDefaults"
- "readPredictionsFromUserDefaults"
- "samplingRateForLogType:"
- "samplingRateFromParsecBag"
- "sendCustomFeedback:"
- "sendMetricsAtThisTime:"
- "sendMetricsIfNeeded"
- "sendMetricsIfNeededAtThisTime:"
- "serializePredictions:"
- "setDate:forKey:"
- "setEnabledOnSourcesTo:"
- "setEnrollment:"
- "setLastEnrolledToTime:"
- "setLastSentToTime:"
- "sharedSession"
- "submit:"
- "submitWithProtobuf:logtype:"
- "v16@?0@\"NSFileHandle\"8"
- "wrapping up atxnotification protobuf message with type: %d, bytes: %d"
- "writePredictionsToUserDefaults:"

```
