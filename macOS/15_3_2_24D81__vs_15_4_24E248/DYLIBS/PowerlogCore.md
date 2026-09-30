## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/PowerlogCore`

```diff

-2308.80.23.0.0
-  __TEXT.__text: 0xcd954
+2423.100.232.0.0
+  __TEXT.__text: 0xd0868
   __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0x78c4
-  __TEXT.__const: 0x510
-  __TEXT.__cstring: 0xff46
-  __TEXT.__gcc_except_tab: 0x2158
-  __TEXT.__oslogstring: 0x5db0
-  __TEXT.__unwind_info: 0x26e0
+  __TEXT.__objc_methlist: 0x7b28
+  __TEXT.__const: 0x568
+  __TEXT.__cstring: 0x10107
+  __TEXT.__gcc_except_tab: 0x2180
+  __TEXT.__oslogstring: 0x6217
+  __TEXT.__unwind_info: 0x2828
   __TEXT.__objc_classname: 0x7f7
-  __TEXT.__objc_methname: 0x113df
-  __TEXT.__objc_methtype: 0x16c6
-  __TEXT.__objc_stubs: 0xdf00
+  __TEXT.__objc_methname: 0x11405
+  __TEXT.__objc_methtype: 0x16c7
+  __TEXT.__objc_stubs: 0xdf60
   __DATA_CONST.__got: 0x5b8
-  __DATA_CONST.__const: 0xe08
+  __DATA_CONST.__const: 0xe38
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4880
+  __DATA_CONST.__objc_selrefs: 0x4900
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x278
-  __DATA_CONST.__objc_arraydata: 0xd00
+  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_arraydata: 0xd20
   __AUTH_CONST.__auth_got: 0xa80
   __AUTH_CONST.__const: 0x3080
-  __AUTH_CONST.__cfstring: 0xf120
-  __AUTH_CONST.__objc_const: 0x8b10
-  __AUTH_CONST.__objc_intobj: 0xb10
+  __AUTH_CONST.__cfstring: 0xf280
+  __AUTH_CONST.__objc_const: 0x86f8
+  __AUTH_CONST.__objc_intobj: 0xb28
   __AUTH_CONST.__objc_doubleobj: 0x160
-  __AUTH_CONST.__objc_arrayobj: 0x300
+  __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0xa28
   __AUTH.__objc_data: 0xb90
   __DATA.__objc_ivar: 0x5d4

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9214F2BD-C9D8-3418-A074-54DF12F27ECA
-  Functions: 3883
-  Symbols:   9505
-  CStrings:  8280
+  UUID: 02356313-099E-349E-B9E0-A87252EB9764
+  Functions: 4038
+  Symbols:   9661
+  CStrings:  8337
 
Symbols:
+ +[NSDate(Monotonic) defaultDateFormatter].cold.1
+ +[PLArchiveJob recoverSelectorForStage:].cold.1
+ +[PLArchiveJob runSelectorForStage:].cold.1
+ +[PLArchiveManager sharedInstance].cold.1
+ +[PLCoreOperator registerOperator:].cold.2
+ +[PLDefaults applicationID].cold.1
+ +[PLDefaults sharedDefaults].cold.1
+ +[PLEntry classForEntryKey:].cold.1
+ +[PLEntry registerEntry:].cold.2
+ +[PLEntryDefinition entryDefinitionsForOperatorClass:].cold.2
+ +[PLEntryDefinition sharedInstance].cold.1
+ +[PLEntryKey setupEntryObjectsForOperatorClass:].cold.1
+ +[PLHelperdLifecycleManager sharedManager].cold.1
+ +[PLModelingUtilities internalBuild].cold.1
+ +[PLModelingUtilities isHeySiriAlwaysOn].cold.1
+ +[PLNetworkUtilities interfaceNameForIndex:].cold.1
+ +[PLOperator className].cold.1
+ +[PLOperator storageQueueName].cold.1
+ +[PLPlatform carrierBuild].cold.1
+ +[PLPlatform hasAOT].cold.1
+ +[PLPlatform hasGenerativeModelSystems].cold.1
+ +[PLPlatform hasOLED].cold.1
+ +[PLPlatform hasProximitySensor]
+ +[PLPlatform hasSleepMedia].cold.1
+ +[PLPlatform internalBuild].cold.1
+ +[PLPlatform is64Bit].cold.1
+ +[PLPlatform isAppleTV].cold.1
+ +[PLPlatform isBasebandDSDS].cold.1
+ +[PLPlatform isBasebandIBIS].cold.1
+ +[PLPlatform isBasebandIce].cold.1
+ +[PLPlatform isBasebandMavLeg].cold.1
+ +[PLPlatform isBasebandMav].cold.1
+ +[PLPlatform isBasebandProto].cold.1
+ +[PLPlatform isVirtualDevice].cold.1
+ +[PLPlatform isWatch].cold.1
+ +[PLPlatform isiOS].cold.1
+ +[PLPlatform isiPad].cold.1
+ +[PLPlatform isiPhone].cold.1
+ +[PLPlatform isiPod].cold.1
+ +[PLSQLiteConnection periodicIntegrityCheckInterval].cold.1
+ +[PLSQLiteConnection tableHasTimestampColumnSem].cold.1
+ +[PLSQLiteConnection tableHasTimestampColumn].cold.1
+ +[PLSemaphore sharedSemaphoreForKey:].cold.1
+ +[PLStateTrackingComposition sharedInstance].cold.1
+ +[PLStorageCache sharedStorageCache].cold.1
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
+ +[PLValueUtilties formatterFromDataType:].cold.1
+ +[PLXPCRelay sharedInstance].cold.1
+ +[PPSEntryKey setupEntryKeyForMetric:].cold.1
+ +[PPSSubmissionUtilities taskingTables].cold.1
+ +[PowerlogCore sharedCore].cold.1
+ -[PLArchiveManager deprecateTablesBGSQL].cold.1
+ -[PLArchiveManager handleFailure:forArchiveEntry:].cold.2
+ -[PLArchiveManager trimBackgroundProcessingLog].cold.1
+ -[PLCoreStorage init].cold.5
+ -[PLCoreStorage storageLocked].cold.1
+ -[PLEntry initWithEntryDate:].cold.1
+ -[PLEntry sem].cold.1
+ -[PLEntryDefinition commonTypeDict_BoolFormat].cold.1
+ -[PLEntryDefinition commonTypeDict_DateFormat].cold.1
+ -[PLEntryDefinition commonTypeDict_DateFormat_isCFAbsoluteTime].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_aggregateFunction_sum].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_W].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_mA].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_mAh].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_mJ].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_mV].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_ms].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_s].cold.1
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_us].cold.1
+ -[PLEntryDefinition commonTypeDict_RawDataFormat].cold.1
+ -[PLEntryDefinition commonTypeDict_RealFormat].cold.1
+ -[PLEntryDefinition commonTypeDict_RealFormat_aggregateFunction_sum].cold.1
+ -[PLEntryDefinition commonTypeDict_RealFormat_withUnit_W].cold.1
+ -[PLEntryDefinition commonTypeDict_RealFormat_withUnit_mJ].cold.1
+ -[PLEntryDefinition commonTypeDict_RealFormat_withUnit_mW].cold.1
+ -[PLEntryDefinition commonTypeDict_RealFormat_withUnit_mWhr].cold.1
+ -[PLEntryDefinition commonTypeDict_RealFormat_withUnit_s].cold.1
+ -[PLEntryDefinition commonTypeDict_StringFormat].cold.1
+ -[PLEntryDefinition commonTypeDict_StringFormat_withAppName].cold.1
+ -[PLEntryDefinition commonTypeDict_StringFormat_withBundleID].cold.1
+ -[PLEntryDefinition commonTypeDict_StringFormat_withProcessName].cold.1
+ -[PLIOHIDOperatorComposition initWithOperator:forService:].cold.3
+ -[PLSQLStatement perform].cold.3
+ -[PLSQLiteConnection initWithFilePath:withCacheSize:].cold.1
+ -[PLSQLiteConnection performQuery:].cold.3
+ -[PLSQLiteConnection runTrimQuery:].cold.4
+ -[PLSQLiteConnection updateEntry:].cold.5
+ -[PLSQLiteConnection writeArrayEntries:].cold.1
+ -[PLSQLiteConnection writeDynamicEntries:].cold.4
+ -[PLSQLiteConnection writeDynamicEntriesToPPS:].cold.6
+ -[PLSQLiteConnection writeEntry:].cold.4
+ -[PLTimeReferenceKernel currentTime].cold.4
+ -[PLTimeReferenceKernel getTimebaseInfo].cold.1
+ -[PLTimeReferenceKernel resolution].cold.1
+ -[PLValueComparison comparisonOperationString].cold.1
+ -[PPSCoreStorage mergePreUnlockDBFiles]
+ -[PPSCoreStorage setupEntryObjects]
+ -[PPSCoreStorage setupMetadataStorage]
+ -[PPSCoreStorage setupStorage]
+ -[PPSCoreStorage startAllStorage]
+ -[PPSCoreStorage storageClassForKey:]
+ -[PPSCoreStorage storageClassForType:]
+ -[PPSSQLStorage init].cold.1
+ -[PPSSQLStorage setupDBConnections].cold.5
+ -[PPSSQLStorage setupStorageForEntryKey:].cold.1
+ -[PPSSQLStorage startStorage].cold.1
+ GCC_except_table115
+ GCC_except_table129
+ GCC_except_table136
+ GCC_except_table146
+ GCC_except_table154
+ GCC_except_table176
+ PLADPushTimeIntervalForDistributionKeySinceStartTime.cold.1
+ PLGetCPUFamily.cold.1
+ PLLogArchiving.cold.1
+ PLLogCommon.cold.1
+ PLLogPower.cold.1
+ PLLogPowerlogHelperdLifecycleManager.cold.1
+ PLLogSQLiteConnection.cold.1
+ PLLogSubmission.cold.1
+ PLLogThreadStats.cold.1
+ PLLogTimeManager.cold.1
+ PLLogZlib.cold.1
+ PPSCoreStorageLog.cold.1
+ PPSDataStreamLog.cold.1
+ PPSLogCommon.cold.1
+ __104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.836
+ __21-[PLCoreStorage init]_block_invoke.64
+ __21-[PLCoreStorage init]_block_invoke.69
+ __21-[PLCoreStorage init]_block_invoke.75
+ __21-[PLCoreStorage init]_block_invoke.99
+ __27-[PLArchiveManager migrate]_block_invoke.334
+ __27-[PLCoreStorage dailyTasks]_block_invoke.440
+ __33-[PLSubmissions taskingModeSetup]_block_invoke.341
+ __33-[PLSubmissions taskingModeSetup]_block_invoke.356
+ __33-[PLSubmissions taskingModeSetup]_block_invoke_2.351
+ __35-[PLArchiveManager migrateArchive:]_block_invoke.318
+ __35-[PLCoreStorage registerDailyTasks]_block_invoke.395
+ __35-[PLCoreStorage registerDailyTasks]_block_invoke.395.cold.1
+ __35-[PLCoreStorage registerDailyTasks]_block_invoke.401
+ __35-[PLCoreStorage registerDailyTasks]_block_invoke.406
+ __35-[PLCoreStorage registerDailyTasks]_block_invoke.406.cold.1
+ __35-[PLCoreStorage registerDailyTasks]_block_invoke_2.407
+ __35-[PLSubmissions performSubmission:]_block_invoke.168
+ __35-[PPSCoreStorage setupEntryObjects]_block_invoke.31
+ __35-[PPSCoreStorage setupEntryObjects]_block_invoke_2.cold.1
+ __36-[PLCoreStorage configureCacheFlush]_block_invoke.233
+ __36-[PLCoreStorage configureCacheFlush]_block_invoke.275
+ __36-[PLCoreStorage configureCacheFlush]_block_invoke_2.276
+ __37-[PLCoreStorage writeAggregateEntry:]_block_invoke.737
+ __37-[PLCoreStorage writeAggregateEntry:]_block_invoke.750
+ __37-[PLCoreStorage writeAggregateEntry:]_block_invoke.756
+ __37-[PLSubmissions submitReasonForToday]_block_invoke.137
+ __37-[PLSubmissions submitReasonForToday]_block_invoke.143
+ __37-[PLSubmissions submitReasonForToday]_block_invoke.149
+ __37-[PLSubmissions taskingModeSafeguard]_block_invoke.321
+ __38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.293
+ __39-[PLCoreStorage flushCachesWithReason:]_block_invoke.641
+ __39-[PLCoreStorage flushCachesWithReason:]_block_invoke.643
+ __39-[PLCoreStorage flushCachesWithReason:]_block_invoke.647
+ __39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke.52
+ __39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke.52.cold.1
+ __39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke.52.cold.2
+ __41-[PLArchiveManager trimXcodeOrganizerLog]_block_invoke.295
+ __41-[PLCoreStorage initOperatorDependancies]_block_invoke.322
+ __42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.384
+ __42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.390
+ __42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.396
+ __44-[PLSQLiteConnection scheduleIntegrityCheck]_block_invoke_2.cold.2
+ __44-[PLSubmissions handleDRConfigUpdate:error:]_block_invoke.118
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.447
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.453
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.463
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.474
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.480
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.489
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.510
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.516
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.522
+ __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.529
+ __45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.266
+ __45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.277
+ __45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.284
+ __45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.302
+ __46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.294
+ __47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.296
+ __48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.718
+ __49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.680
+ __49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.684
+ __49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.684.cold.1
+ __49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.692
+ __55-[PLCoreStorage blockingFlushCachesWithReason:timeout:]_block_invoke.671
+ __61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.882
+ __61-[PLSubmissions submitRecordToDiagnosticPipeline:withConfig:]_block_invoke.202
+ __63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.781
+ __66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.154
+ __66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.158
+ __66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.159
+ __66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.160
+ __74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.535
+ __76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.727
+ __76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.733
+ __77-[PLCoreStorage aggregateEntriesForKey:withBucketLength:inTimeIntervalRange:]_block_invoke.915
+ __Block_byref_object_copy_.713
+ __Block_byref_object_dispose_.714
+ ___29+[PLPlatform isBasebandProto]_block_invoke
+ ___30-[PPSCoreStorage setupStorage]_block_invoke
+ ___33-[PPSCoreStorage startAllStorage]_block_invoke
+ ___35-[PPSCoreStorage setupEntryObjects]_block_invoke
+ ___35-[PPSCoreStorage setupEntryObjects]_block_invoke_2
+ ___38-[PPSCoreStorage setupMetadataStorage]_block_invoke
+ ___39-[PPSCoreStorage mergePreUnlockDBFiles]_block_invoke
+ ___40-[PLArchiveManager deprecateTablesBGSQL]_block_invoke
+ ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke
+ ___block_descriptor_32_e31_q24?0"NSString"8"NSString"16l
+ __block_literal_global.101
+ __block_literal_global.183
+ __block_literal_global.198
+ __block_literal_global.210
+ __block_literal_global.240
+ __block_literal_global.286
+ __block_literal_global.289
+ __block_literal_global.291
+ __block_literal_global.323
+ __block_literal_global.324
+ __block_literal_global.333
+ __block_literal_global.34
+ __block_literal_global.343
+ __block_literal_global.345
+ __block_literal_global.357
+ __block_literal_global.38
+ __block_literal_global.380
+ __block_literal_global.416
+ __block_literal_global.419
+ __block_literal_global.422
+ __block_literal_global.425
+ __block_literal_global.430
+ __block_literal_global.47
+ __block_literal_global.478
+ __block_literal_global.49
+ __block_literal_global.51
+ __block_literal_global.531
+ __block_literal_global.540
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
+ __block_literal_global.77
+ __block_literal_global.79
+ __block_literal_global.816
+ __block_literal_global.828
+ __block_literal_global.839
+ __block_literal_global.859
+ __block_literal_global.87
+ _kPLBB23C
+ _objc_msgSend$BGSQLDBDuration
+ _objc_msgSend$isHealthDataSubmissionAllowed
+ _objc_msgSend$mergePreUnlockDBFiles
+ _objc_msgSend$trimConditionsForBGSQLWithTrimDate:
+ blockingFlushCachesWithReason:timeout:.classDebugEnabled.670
+ blockingFlushCachesWithReason:timeout:.defaultOnce.669
+ blockingFlushQueues:withTimeout:.classDebugEnabled.679
+ blockingFlushQueues:withTimeout:.classDebugEnabled.691
+ blockingFlushQueues:withTimeout:.defaultOnce.678
+ blockingFlushQueues:withTimeout:.defaultOnce.690
+ checkTaskingCompletionStatus.classDebugEnabled.276
+ checkTaskingCompletionStatus.classDebugEnabled.295
+ checkTaskingCompletionStatus.defaultOnce.275
+ checkTaskingCompletionStatus.defaultOnce.294
+ clearTaskingDefaults.classDebugEnabled.383
+ clearTaskingDefaults.classDebugEnabled.389
+ clearTaskingDefaults.classDebugEnabled.395
+ clearTaskingDefaults.defaultOnce.382
+ clearTaskingDefaults.defaultOnce.388
+ clearTaskingDefaults.defaultOnce.394
+ flushCachesWithReason:.defaultOnce.642
+ handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.534
+ handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.533
+ isBasebandProto.onceToken
+ isBasebandProto.result
+ kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.749
+ kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.755
+ kPLTaskingEndNotification_block_invoke_6.defaultOnce.748
+ kPLTaskingEndNotification_block_invoke_6.defaultOnce.754
+ lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.881
+ lastEntryForKey:withComparisons:isSingleton:.defaultOnce.880
+ logHandle.cold.1
+ logHandleRbdcHelper.cold.1
+ logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.929
+ logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.930
+ logPPSFeatureFlagReaderHelper.cold.1
+ migrateArchive:.classDebugEnabled.317
+ migrateArchive:.defaultOnce.316
+ nanoSecondsFromMachTime.cold.1
+ registerDailyTasks.classDebugEnabled.400
+ registerDailyTasks.defaultOnce.399
+ shouldStartTaskingToday.classDebugEnabled.446
+ shouldStartTaskingToday.classDebugEnabled.452
+ shouldStartTaskingToday.classDebugEnabled.473
+ shouldStartTaskingToday.classDebugEnabled.479
+ shouldStartTaskingToday.classDebugEnabled.488
+ shouldStartTaskingToday.classDebugEnabled.509
+ shouldStartTaskingToday.classDebugEnabled.515
+ shouldStartTaskingToday.classDebugEnabled.521
+ shouldStartTaskingToday.defaultOnce.445
+ shouldStartTaskingToday.defaultOnce.451
+ shouldStartTaskingToday.defaultOnce.472
+ shouldStartTaskingToday.defaultOnce.478
+ shouldStartTaskingToday.defaultOnce.487
+ shouldStartTaskingToday.defaultOnce.508
+ shouldStartTaskingToday.defaultOnce.514
+ shouldStartTaskingToday.defaultOnce.520
+ sqlConnectionHandle.cold.1
+ sqlLog.cold.1
+ submitReasonForToday.classDebugEnabled.136
+ submitReasonForToday.classDebugEnabled.142
+ submitReasonForToday.classDebugEnabled.148
+ submitReasonForToday.defaultOnce.135
+ submitReasonForToday.defaultOnce.141
+ submitReasonForToday.defaultOnce.147
+ taskingModeSafeguard.classDebugEnabled.332
+ taskingModeSafeguard.defaultOnce.331
+ writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.726
+ writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.732
+ writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.725
+ writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.731
- +[PLUtilities getJetamPriority:]
- +[PLUtilities getJetamPriority:].cold.1
- +[PPSCoreStorage setupEntryObjects]
- +[PPSCoreStorage setupMetadataStorage]
- +[PPSCoreStorage setupStorage]
- +[PPSCoreStorage startAllStorage]
- +[PPSCoreStorage storageClassForKey:]
- +[PPSCoreStorage storageClassForType:]
- -[PPSCoreStorage mergePreUnlockDBFile]
- GCC_except_table109
- GCC_except_table114
- GCC_except_table128
- GCC_except_table135
- GCC_except_table140
- GCC_except_table145
- GCC_except_table153
- GCC_except_table175
- GCC_except_table99
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- __104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.829
- __21-[PLCoreStorage init]_block_invoke.60
- __21-[PLCoreStorage init]_block_invoke.65
- __21-[PLCoreStorage init]_block_invoke.92
- __27-[PLArchiveManager migrate]_block_invoke.317
- __27-[PLCoreStorage dailyTasks]_block_invoke.433
- __33-[PLSubmissions taskingModeSetup]_block_invoke.327
- __33-[PLSubmissions taskingModeSetup]_block_invoke.342
- __33-[PLSubmissions taskingModeSetup]_block_invoke_2.337
- __35+[PPSCoreStorage setupEntryObjects]_block_invoke.32
- __35+[PPSCoreStorage setupEntryObjects]_block_invoke_2.cold.1
- __35-[PLArchiveManager migrateArchive:]_block_invoke.301
- __35-[PLCoreStorage registerDailyTasks]_block_invoke.388
- __35-[PLCoreStorage registerDailyTasks]_block_invoke.388.cold.1
- __35-[PLCoreStorage registerDailyTasks]_block_invoke.394
- __35-[PLCoreStorage registerDailyTasks]_block_invoke.399
- __35-[PLCoreStorage registerDailyTasks]_block_invoke.399.cold.1
- __35-[PLCoreStorage registerDailyTasks]_block_invoke_2.400
- __35-[PLSubmissions performSubmission:]_block_invoke.154
- __36-[PLCoreStorage configureCacheFlush]_block_invoke.226
- __36-[PLCoreStorage configureCacheFlush]_block_invoke.268
- __36-[PLCoreStorage configureCacheFlush]_block_invoke_2.269
- __37-[PLCoreStorage writeAggregateEntry:]_block_invoke.730
- __37-[PLCoreStorage writeAggregateEntry:]_block_invoke.736
- __37-[PLCoreStorage writeAggregateEntry:]_block_invoke.749
- __37-[PLSubmissions submitReasonForToday]_block_invoke.118
- __37-[PLSubmissions submitReasonForToday]_block_invoke.124
- __37-[PLSubmissions submitReasonForToday]_block_invoke.130
- __37-[PLSubmissions taskingModeSafeguard]_block_invoke.305
- __38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.277
- __39-[PLCoreStorage flushCachesWithReason:]_block_invoke.634
- __39-[PLCoreStorage flushCachesWithReason:]_block_invoke.636
- __39-[PLCoreStorage flushCachesWithReason:]_block_invoke.640
- __41-[PLArchiveManager trimXcodeOrganizerLog]_block_invoke.279
- __41-[PLCoreStorage initOperatorDependancies]_block_invoke.315
- __42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.381
- __42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.387
- __42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.393
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.444
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.450
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.460
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.471
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.477
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.486
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.507
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.513
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.519
- __45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.526
- __45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.250
- __45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.261
- __45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.268
- __45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.286
- __46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.278
- __48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.711
- __49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.673
- __49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.677
- __49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.677.cold.1
- __49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.685
- __55-[PLCoreStorage blockingFlushCachesWithReason:timeout:]_block_invoke.664
- __61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.875
- __61-[PLSubmissions submitRecordToDiagnosticPipeline:withConfig:]_block_invoke.182
- __63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.774
- __66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.135
- __66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.139
- __66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.140
- __66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.141
- __74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.528
- __76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.720
- __76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.726
- __77-[PLCoreStorage aggregateEntriesForKey:withBucketLength:inTimeIntervalRange:]_block_invoke.908
- __Block_byref_object_copy_.706
- __Block_byref_object_dispose_.707
- ___30+[PPSCoreStorage setupStorage]_block_invoke
- ___33+[PPSCoreStorage startAllStorage]_block_invoke
- ___35+[PPSCoreStorage setupEntryObjects]_block_invoke
- ___35+[PPSCoreStorage setupEntryObjects]_block_invoke_2
- ___38+[PPSCoreStorage setupMetadataStorage]_block_invoke
- ___42+[PLUtilities shouldLogPreUnlockTelemetry]_block_invoke
- __block_literal_global.176
- __block_literal_global.191
- __block_literal_global.234
- __block_literal_global.252
- __block_literal_global.270
- __block_literal_global.284
- __block_literal_global.288
- __block_literal_global.307
- __block_literal_global.317
- __block_literal_global.326
- __block_literal_global.329
- __block_literal_global.338
- __block_literal_global.35
- __block_literal_global.350
- __block_literal_global.37
- __block_literal_global.39
- __block_literal_global.414
- __block_literal_global.418
- __block_literal_global.421
- __block_literal_global.424
- __block_literal_global.427
- __block_literal_global.432
- __block_literal_global.482
- __block_literal_global.528
- __block_literal_global.53
- __block_literal_global.537
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
- __block_literal_global.809
- __block_literal_global.826
- __block_literal_global.832
- __block_literal_global.852
- _objc_msgSend$mergePreUnlockDBFile
- blockingFlushCachesWithReason:timeout:.classDebugEnabled.663
- blockingFlushCachesWithReason:timeout:.defaultOnce.662
- blockingFlushQueues:withTimeout:.classDebugEnabled.672
- blockingFlushQueues:withTimeout:.classDebugEnabled.684
- blockingFlushQueues:withTimeout:.defaultOnce.671
- blockingFlushQueues:withTimeout:.defaultOnce.683
- checkTaskingCompletionStatus.classDebugEnabled.260
- checkTaskingCompletionStatus.classDebugEnabled.279
- checkTaskingCompletionStatus.defaultOnce.259
- checkTaskingCompletionStatus.defaultOnce.278
- clearTaskingDefaults.classDebugEnabled.380
- clearTaskingDefaults.classDebugEnabled.386
- clearTaskingDefaults.classDebugEnabled.392
- clearTaskingDefaults.defaultOnce.379
- clearTaskingDefaults.defaultOnce.385
- clearTaskingDefaults.defaultOnce.391
- flushCachesWithReason:.defaultOnce.635
- handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.527
- handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.526
- kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.735
- kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.748
- kPLTaskingEndNotification_block_invoke_6.defaultOnce.734
- kPLTaskingEndNotification_block_invoke_6.defaultOnce.747
- lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.874
- lastEntryForKey:withComparisons:isSingleton:.defaultOnce.873
- logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.922
- logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.923
- migrateArchive:.classDebugEnabled.300
- migrateArchive:.defaultOnce.299
- registerDailyTasks.classDebugEnabled.393
- registerDailyTasks.defaultOnce.392
- shouldLogPreUnlockTelemetry.__shouldLogPreUnlockTelemetry
- shouldLogPreUnlockTelemetry.onceToken
- shouldStartTaskingToday.classDebugEnabled.443
- shouldStartTaskingToday.classDebugEnabled.449
- shouldStartTaskingToday.classDebugEnabled.470
- shouldStartTaskingToday.classDebugEnabled.476
- shouldStartTaskingToday.classDebugEnabled.485
- shouldStartTaskingToday.classDebugEnabled.506
- shouldStartTaskingToday.classDebugEnabled.512
- shouldStartTaskingToday.classDebugEnabled.518
- shouldStartTaskingToday.defaultOnce.442
- shouldStartTaskingToday.defaultOnce.448
- shouldStartTaskingToday.defaultOnce.469
- shouldStartTaskingToday.defaultOnce.475
- shouldStartTaskingToday.defaultOnce.484
- shouldStartTaskingToday.defaultOnce.505
- shouldStartTaskingToday.defaultOnce.511
- shouldStartTaskingToday.defaultOnce.517
- submitReasonForToday.classDebugEnabled.117
- submitReasonForToday.classDebugEnabled.123
- submitReasonForToday.classDebugEnabled.129
- submitReasonForToday.defaultOnce.116
- submitReasonForToday.defaultOnce.122
- submitReasonForToday.defaultOnce.128
- taskingModeSafeguard.classDebugEnabled.316
- taskingModeSafeguard.defaultOnce.315
- writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.719
- writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.725
- writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.718
- writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.724
CStrings:
+ "%@ sysctl value: %u"
+ "'%@' metrics updated"
+ "** Done starting PowerlogCore **"
+ "** Done stopping PowerlogCore **"
+ "** Starting PowerlogCore **"
+ "** Stopping PowerlogCore **"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Agents/PLEnhancedTaskingAgent.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Compositions/PLEntryNotificationOperatorComposition.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Compositions/PLIOHIDOperatorComposition.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Compositions/PLIOKitOperatorComposition.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Compositions/PLTimer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/PowerlogCore/PLCoreOperator.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/PowerlogCore/PLOperator.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/PowerlogCore/PLXPCRelay.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/PowerlogCore/PowerlogCore.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLArchiveJob.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLArchiveManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLCoreStorage.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLDefaults.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLEntry.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLStorageCache.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissions.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionConfig.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFile.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFilePLL.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFileSP.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeReference.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceDynamic.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceSystem.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterion.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterionEntry.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterionTime.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/DataTypes/PLEntryKey.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/DataTypes/PLSQLStatement.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLEntryDefinition.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLKQueue.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLMonotonicTimer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLNetworkUtilities.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLSQLiteConnection.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLSemaphore.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLUtilities.m"
+ "Background Processing dB disabled"
+ "BackgroundProcessing/"
+ "BackgroundProcessing_TaskDependencies_24_5_Array_ConsumedResultIdentifiers"
+ "BatteryMetrics_Battery_1_2"
+ "CurrentBackgroundProcessingDB.BGSQL"
+ "DRConfig cancelled, exiting task mode..."
+ "DisplayMetrics_DisplayState_1_2"
+ "EPSQL"
+ "Error with MEMORYSTATUS_CMD_GET_PRIORITY_LIST. Size %i and sizeof(entry) %lu"
+ "Failed to merge pre-unlock DB '%@'..."
+ "File to upload generated at %@ with %d files included."
+ "Invalid connection to Background Processing DB"
+ "Invalid connection to PreUnlock DB '%@'"
+ "KEYBAG: Lock status notification"
+ "Merged pre-unlock DB '%@'..."
+ "Merging pre-unlock DBs..."
+ "No pre-unlock DBs to merge"
+ "PLArchiveManager::trimBGSQL: disabled"
+ "PLArchiveManager::trimBGSQL: interrupted"
+ "PLArchiveManager::trimBGSQL: start"
+ "PLArchiveManager::trimBGSQL: trimDate=%@"
+ "PLArchiveManager::trimBGSQL: vacuum"
+ "PLStorageLocked"
+ "PPSTmp_BackgroundProcessing_TaskDependencies_24_5_Array_ConsumedResultIdentifiers"
+ "PowerlogStartup"
+ "PowerlogTeardown"
+ "PreUnlockLog_%f.EPSQL"
+ "Starting PowerlogCore"
+ "Starting connection to PreUnlock DB '%@'"
+ "Stopping PowerlogCore"
+ "SubmissionConfigUUID"
+ "Unable to get %@ sysctl value, defaulting to -1: %{errno}d"
+ "bb23C"
+ "com.apple.mobile.keybagd.lock_status"
+ "failed integrity check due to corrupt DB during activity"
+ "failed integrity check due to corrupt DB during init"
+ "getJetsamPriority:"
+ "grabSysctlValue:"
+ "handleFailure: corrupt DB"
+ "hasProximitySensor"
+ "mergePreUnlockDBFiles"
+ "performQuery: corrupt DB"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "runTrimQuery: corrupt DB"
+ "sqlite3_step: corrupt DB"
+ "updateEntry: corrupt DB"
+ "writeArrayEntries: corrupt DB"
+ "writeDynamicEntries: corrupt DB"
+ "writeDynamicEntriesToPPS: corrupt DB"
+ "writeEntry: corrupt DB"
+ "{jetsam_priority_info=iBq}20@0:8i16"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Agents/PLEnhancedTaskingAgent.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Compositions/PLEntryNotificationOperatorComposition.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Compositions/PLIOHIDOperatorComposition.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Compositions/PLIOKitOperatorComposition.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Operators/Compositions/PLTimer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/PowerlogCore/PLCoreOperator.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/PowerlogCore/PLOperator.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/PowerlogCore/PLXPCRelay.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/PowerlogCore/PowerlogCore.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLArchiveJob.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLArchiveManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLCoreStorage.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLDefaults.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLEntry.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLStorageCache.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissions.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionConfig.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFile.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFilePLL.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLSubmissionsClasses/PLSubmissionFileSP.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeReference.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceDynamic.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceSystem.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterion.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterionEntry.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/Activity/PLActivityCriterionTime.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/DataTypes/PLEntryKey.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/DataTypes/PLSQLStatement.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLEntryDefinition.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLKQueue.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLMonotonicTimer.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLNetworkUtilities.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLSQLiteConnection.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLSemaphore.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Utilities/PLUtilities.m"
- "ConfigUUID"
- "Invalid connection to PreUnlock DB"
- "PerfPowerServicesSignpostReader tarball path: %@"
- "PreUnlockLog.EPSQL"
- "SchemaMismatch: table: %@ metrics modified"
- "f"
- "getJetamPriority:"
- "mergePreUnlockDBFile"
- "tarballPath"
- "{jetsam_priority_info=iB}20@0:8i16"

```
