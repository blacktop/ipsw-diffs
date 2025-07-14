## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-1787.80.12.0.0
-  __TEXT.__text: 0xce788
+1851.102.4.0.0
+  __TEXT.__text: 0xd4344
   __TEXT.__auth_stubs: 0x1960
-  __TEXT.__objc_methlist: 0x7a6c
-  __TEXT.__const: 0x14a0
-  __TEXT.__cstring: 0x33274
-  __TEXT.__gcc_except_tab: 0x2140
-  __TEXT.__oslogstring: 0x5912
-  __TEXT.__unwind_info: 0x29c8
+  __TEXT.__objc_methlist: 0x7db0
+  __TEXT.__const: 0x14b8
+  __TEXT.__cstring: 0x33d21
+  __TEXT.__gcc_except_tab: 0x21b0
+  __TEXT.__oslogstring: 0x6108
+  __TEXT.__unwind_info: 0x2acc
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x7da
-  __TEXT.__objc_methname: 0x117a6
-  __TEXT.__objc_methtype: 0x170e
-  __TEXT.__objc_stubs: 0xe380
+  __TEXT.__objc_classname: 0x827
+  __TEXT.__objc_methname: 0x11f0a
+  __TEXT.__objc_methtype: 0x173a
+  __TEXT.__objc_stubs: 0xeb00
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x2348
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__const: 0x23c8
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x62c8
-  __DATA_CONST.__objc_selrefs: 0x4940
-  __DATA_CONST.__objc_arraydata: 0x30ac8
-  __AUTH_CONST.__const: 0x1aa0
-  __AUTH_CONST.__cfstring: 0x4e220
-  __AUTH_CONST.__objc_const: 0x2930
-  __AUTH_CONST.__objc_intobj: 0x4308
+  __DATA_CONST.__objc_const: 0x6528
+  __DATA_CONST.__objc_selrefs: 0x4b48
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x3f0
+  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_arraydata: 0x31330
+  __AUTH_CONST.__const: 0x1c00
+  __AUTH_CONST.__cfstring: 0x4fa80
+  __AUTH_CONST.__objc_const: 0x29c0
+  __AUTH_CONST.__objc_intobj: 0x4320
   __AUTH_CONST.__objc_doubleobj: 0xcb0
-  __AUTH_CONST.__objc_arrayobj: 0xf00
-  __AUTH_CONST.__objc_dictobj: 0xc6e8
+  __AUTH_CONST.__objc_arrayobj: 0xf18
+  __AUTH_CONST.__objc_dictobj: 0xc8f0
   __AUTH_CONST.__auth_got: 0xcc8
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x3e0
-  __DATA.__objc_superrefs: 0x290
-  __DATA.__objc_ivar: 0x5e8
-  __DATA.__data: 0x3d8
-  __DATA.__bss: 0x1bf9
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x604
+  __DATA.__data: 0x438
+  __DATA.__bss: 0x1bd9
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0xaa8
+  __DATA_DIRTY.__bss: 0xa88
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6A30FE14-8E85-36D9-8C81-2983FCA8405D
-  Functions: 4439
-  Symbols:   14424
-  CStrings:  24500
+  UUID: 5E8F95AE-3067-3A78-BAC7-6B0A454EFA2A
+  Functions: 4563
+  Symbols:   14776
+  CStrings:  25020
 
Symbols:
+ +[PLEntry dataFormatForMetric:auxiliaryMetrics:]
+ +[PLEntryDefinition DMAKeysForEntryDefinition:]
+ +[PLEntryDefinition arrayKeyConfigsForEntryKey:]
+ +[PLEntryDefinition hasDMAKeysForEntryDefinition:]
+ +[PLEntryDefinition hasDMAKeysForEntryKey:]
+ +[PLEntryNotificationOperatorComposition luxEntryNotificationWithOperator:withBlock:]
+ +[PLOperator createEntriesForMetrics:withData:withDate:].cold.1
+ +[PLUtilities bundleIDFromProcessName:]
+ +[PLUtilities markFilesAsPurgeable:withUrgency:]
+ +[PLUtilities markFilesInDirectoryAsPurgeable:ofType:withUrgency:]
+ +[PLUtilities markFilesInDirectoryAsPurgeable:ofType:withUrgency:].cold.1
+ +[PLUtilities markFilesInDirectoryAsPurgeable:ofType:withUrgency:].cold.2
+ +[PLUtilities sanitizeCAPayload:]
+ +[PPSEntryKey addAuxiliaryType:withEntryKey:]
+ +[PPSEntryKey allArrayKeysForEntryKey:]
+ +[PPSEntryKey allBaseKeysForEntryKey:]
+ +[PPSEntryKey allDynamicKeysForEntryKey:]
+ +[PPSEntryKey anyMetricsForEntryKey:]
+ +[PPSEntryKey arrayMetricsForEntryKey:]
+ +[PPSEntryKey baseMetricsForEntryKey:]
+ +[PPSEntryKey dynamicMetricsForEntryKey:]
+ +[PPSEntryKey dynamicTableNameForEntryKey:]
+ +[PPSEntryKey filterEntryLoggingForEntryKey:]
+ +[PPSEntryKey hasArrayKeys:]
+ +[PPSEntryKey hasDynamicKeys:]
+ +[PPSEntryKey resetMetricsForEntryKey:]
+ +[PPSSQLStorage trimConditionsForXCSQLWithTrimDate:]
+ -[PLArchiveManager XCSQLDBDuration]
+ -[PLArchiveManager deprecateTablesXCSQL]
+ -[PLArchiveManager setXCSQLDBDuration:]
+ -[PLArchiveManager trimXcodeOrganizerLog]
+ -[PLEntry DMAKeys]
+ -[PLEntry hasDMAKeys]
+ -[PLEntry isPPSEnabled]
+ -[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_mJ]
+ -[PLOperator logDMAEntry:]
+ -[PLOperator logDMAEntry:].cold.1
+ -[PLOperator logDMAEntry:].cold.2
+ -[PLSQLiteConnection sortedSqlFormatedColumnNamesForTableInsert:]
+ -[PLSQLiteConnection writeDynamicEntriesToPPS:]
+ -[PLSQLiteConnection writeDynamicEntriesToPPS:].cold.1
+ -[PLSQLiteConnection writeDynamicEntriesToPPS:].cold.2
+ -[PLSQLiteConnection writeDynamicEntriesToPPS:].cold.3
+ -[PLSQLiteConnection writeDynamicEntriesToPPS:].cold.4
+ -[PLSQLiteConnection writeDynamicEntriesToPPS:].cold.5
+ -[PLSubmissionConfig copyWithZone:]
+ -[PLSubmissionConfig setSubmittedFilesMask:]
+ -[PLSubmissionConfig splitBySubmissionType]
+ -[PLSubmissionConfig submissionCategory]
+ -[PLSubmissionConfig submissionMaskToString]
+ -[PLSubmissionConfig submitXC]
+ -[PLSubmissionFileXC copyAndPrepareLog]
+ -[PLSubmissionFileXC copyAndPrepareLog].cold.1
+ -[PLSubmissionFileXC copyAndPrepareLog].cold.2
+ -[PLSubmissionFileXC copyAndPrepareLog].cold.3
+ -[PLSubmissionFileXC copyAndPrepareLog].cold.4
+ -[PLSubmissionFileXC copyAndPrepareLog].cold.5
+ -[PLSubmissionFileXC copyAndPrepareLog].cold.6
+ -[PLSubmissionFileXC copyAndPrepareLog].cold.7
+ -[PLSubmissionFileXC copyAndPrepareLog].cold.8
+ -[PLSubmissionFileXC fileExtension]
+ -[PLSubmissionFileXC fileType]
+ -[PLSubmissionFileXC getXCSQLFile]
+ -[PLSubmissionFileXC getXCSQLFile].cold.1
+ -[PLSubmissionFileXC initWithConfig:]
+ -[PLSubmissionFileXC obfuscateTimestampsForTable:connection:withOffset:]
+ -[PLSubmissionFileXC obfuscateTimestampsForTable:connection:withOffset:].cold.1
+ -[PLSubmissionFileXC obfuscateTimestampsForTable:connection:withOffset:].cold.2
+ -[PLSubmissionFileXC randomizedBaseOffset]
+ -[PLSubmissionFileXC randomizedBaseOffset].cold.1
+ -[PLSubmissionFileXC submit]
+ -[PLTimeReferenceKernel initializeOffsetWithEntries:].cold.1
+ -[PLTimeReferenceKernel quarantineWithExitReason:]
+ -[PPSCollectionOperator monitorMetricsForSubsystem:category:payload:]
+ -[PPSCollectionOperator monitor]
+ -[PPSCollectionOperator monitoredCategory]
+ -[PPSCollectionOperator monitoredSubsystem]
+ -[PPSCollectionOperator setMonitor:]
+ -[PPSCollectionOperator setMonitoredCategory:]
+ -[PPSCollectionOperator setMonitoredSubsystem:]
+ -[PPSCollectionOperator setStartMonitor:]
+ -[PPSCollectionOperator setStopMonitor:]
+ -[PPSCollectionOperator startMonitor]
+ -[PPSCollectionOperator stopMonitor]
+ -[PPSFeatureFlagReaderHelper .cxx_destruct]
+ -[PPSFeatureFlagReaderHelper closeXPCConnection]
+ -[PPSFeatureFlagReaderHelper closeXPCConnection].cold.1
+ -[PPSFeatureFlagReaderHelper connectionToServer]
+ -[PPSFeatureFlagReaderHelper createXPCConnection]
+ -[PPSFeatureFlagReaderHelper createXPCConnection].cold.1
+ -[PPSFeatureFlagReaderHelper createXPCConnection].cold.2
+ -[PPSFeatureFlagReaderHelper getFeatureFlags]
+ -[PPSFeatureFlagReaderHelper getFeatureFlags].cold.1
+ -[PPSFeatureFlagReaderHelper getFeatureFlags].cold.2
+ -[PPSFeatureFlagReaderHelper setConnectionToServer:]
+ -[PPSSQLStorage XCSQLConnection]
+ -[PPSSQLStorage setupArrayTableForEntryKey:withName:withConnection:]
+ -[PPSSQLStorage setupDynamicTableForEntryKey:withName:withConnection:]
+ -[PPSSQLStorage setupDynamicTableForEntryKey:withName:withConnection:].cold.1
+ -[PPSSQLStorage setupDynamicTableForEntryKey:withName:withConnection:].cold.2
+ -[PPSSQLStorage updateTable:transferDataForKeys:].cold.1
+ GCC_except_table101
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table135
+ GCC_except_table72
+ GCC_except_table96
+ _ArrayReserved_block_invoke.classDebugEnabled
+ _ArrayReserved_block_invoke.defaultOnce
+ _ArrayReserved_block_invoke_2.classDebugEnabled
+ _ArrayReserved_block_invoke_2.classDebugEnabled.86
+ _ArrayReserved_block_invoke_2.defaultOnce
+ _ArrayReserved_block_invoke_2.defaultOnce.85
+ _ArrayReserved_block_invoke_3.classDebugEnabled
+ _ArrayReserved_block_invoke_3.classDebugEnabled.133
+ _ArrayReserved_block_invoke_3.classDebugEnabled.140
+ _ArrayReserved_block_invoke_3.classDebugEnabled.146
+ _ArrayReserved_block_invoke_3.defaultOnce
+ _ArrayReserved_block_invoke_3.defaultOnce.132
+ _ArrayReserved_block_invoke_3.defaultOnce.139
+ _ArrayReserved_block_invoke_3.defaultOnce.145
+ _ArrayReserved_block_invoke_4.classDebugEnabled
+ _ArrayReserved_block_invoke_4.classDebugEnabled.107
+ _ArrayReserved_block_invoke_4.classDebugEnabled.182
+ _ArrayReserved_block_invoke_4.classDebugEnabled.188
+ _ArrayReserved_block_invoke_4.classDebugEnabled.194
+ _ArrayReserved_block_invoke_4.classDebugEnabled.230
+ _ArrayReserved_block_invoke_4.classDebugEnabled.234
+ _ArrayReserved_block_invoke_4.defaultOnce
+ _ArrayReserved_block_invoke_4.defaultOnce.106
+ _ArrayReserved_block_invoke_4.defaultOnce.181
+ _ArrayReserved_block_invoke_4.defaultOnce.187
+ _ArrayReserved_block_invoke_4.defaultOnce.193
+ _ArrayReserved_block_invoke_4.defaultOnce.229
+ _ArrayReserved_block_invoke_4.defaultOnce.233
+ _ArrayReserved_block_invoke_5.classDebugEnabled
+ _ArrayReserved_block_invoke_5.classDebugEnabled.202
+ _ArrayReserved_block_invoke_5.classDebugEnabled.208
+ _ArrayReserved_block_invoke_5.classDebugEnabled.214
+ _ArrayReserved_block_invoke_5.classDebugEnabled.220
+ _ArrayReserved_block_invoke_5.defaultOnce
+ _ArrayReserved_block_invoke_5.defaultOnce.201
+ _ArrayReserved_block_invoke_5.defaultOnce.207
+ _ArrayReserved_block_invoke_5.defaultOnce.213
+ _ArrayReserved_block_invoke_5.defaultOnce.219
+ _ArrayReserved_block_invoke_6.classDebugEnabled
+ _ArrayReserved_block_invoke_6.classDebugEnabled.260
+ _ArrayReserved_block_invoke_6.classDebugEnabled.267
+ _ArrayReserved_block_invoke_6.defaultOnce
+ _ArrayReserved_block_invoke_6.defaultOnce.259
+ _ArrayReserved_block_invoke_6.defaultOnce.266
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_PLSubmissionFileXC
+ _OBJC_CLASS_$_PPSFeatureFlagReaderHelper
+ _OBJC_IVAR_$_PLArchiveManager._XCSQLDBDuration
+ _OBJC_IVAR_$_PPSCollectionOperator._monitor
+ _OBJC_IVAR_$_PPSCollectionOperator._monitoredCategory
+ _OBJC_IVAR_$_PPSCollectionOperator._monitoredSubsystem
+ _OBJC_IVAR_$_PPSCollectionOperator._startMonitor
+ _OBJC_IVAR_$_PPSCollectionOperator._stopMonitor
+ _OBJC_IVAR_$_PPSFeatureFlagReaderHelper._connectionToServer
+ _OBJC_METACLASS_$_PLSubmissionFileXC
+ _OBJC_METACLASS_$_PPSFeatureFlagReaderHelper
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _PLLogArchiving
+ _PLLogArchiving.__logObj
+ _PLLogArchiving.onceToken
+ _PLLogTimeManager
+ _PLLogTimeManager._logHandle
+ _PLLogTimeManager.onceToken
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.69
+ _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.68
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_2.classDebugEnabled.49
+ _PLSubmissionAnalyticsStateSuccess_block_invoke_2.defaultOnce.48
+ _PPSDataStreamLog
+ _PPSDataStreamLog.__logObj
+ _PPSDataStreamLog.onceToken
+ __OBJC_$_INSTANCE_METHODS_PLSubmissionFileXC
+ __OBJC_$_INSTANCE_METHODS_PPSFeatureFlagReaderHelper
+ __OBJC_$_INSTANCE_VARIABLES_PPSFeatureFlagReaderHelper
+ __OBJC_$_PROP_LIST_PPSFeatureFlagReaderHelper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PPSFeatureFlagReaderProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PPSFeatureFlagReaderProtocol
+ __OBJC_CLASS_PROTOCOLS_$_PLSubmissionConfig
+ __OBJC_CLASS_RO_$_PLSubmissionFileXC
+ __OBJC_CLASS_RO_$_PPSFeatureFlagReaderHelper
+ __OBJC_LABEL_PROTOCOL_$_PPSFeatureFlagReaderProtocol
+ __OBJC_METACLASS_RO_$_PLSubmissionFileXC
+ __OBJC_METACLASS_RO_$_PPSFeatureFlagReaderHelper
+ __OBJC_PROTOCOL_$_PPSFeatureFlagReaderProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_PPSFeatureFlagReaderProtocol
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006ILi0EEEPKc
+ __ZNSt3__116__pad_and_outputB8ue170006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ue170006Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ue170006Ev
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__124__put_character_sequenceB8ue170006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ ___104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.828
+ ___18-[PLOperator init]_block_invoke.39
+ ___18-[PLXPCRelay init]_block_invoke.20
+ ___21-[PLCoreStorage init]_block_invoke.64
+ ___21-[PLCoreStorage init]_block_invoke.92
+ ___21-[PLTimeManager init]_block_invoke.25
+ ___21-[PLTimeManager init]_block_invoke.25.cold.1
+ ___23-[PLKQueue setEnabled:]_block_invoke.16
+ ___23-[PLKQueue setEnabled:]_block_invoke.24
+ ___23-[PLKQueue setEnabled:]_block_invoke.31
+ ___24-[PLXPCRelay startRelay]_block_invoke.30
+ ___24-[PLXPCRelay startRelay]_block_invoke.30.cold.1
+ ___24-[PLXPCRelay startRelay]_block_invoke.30.cold.2
+ ___24-[PLXPCRelay startRelay]_block_invoke.36
+ ___24-[PLXPCRelay startRelay]_block_invoke.41
+ ___24-[PLXPCRelay startRelay]_block_invoke.41.cold.1
+ ___24-[PLXPCRelay startRelay]_block_invoke_2.42
+ ___25-[PLActivity runActivity]_block_invoke.17
+ ___25-[PLActivity runActivity]_block_invoke.18
+ ___25-[PLOperator flushBuffer]_block_invoke.63
+ ___26-[PLOperator logDMAEntry:]_block_invoke
+ ___26-[PLOperator logDMAEntry:]_block_invoke.229
+ ___26-[PLOperator logDMAEntry:]_block_invoke_2
+ ___26-[PLOperator logDMAEntry:]_block_invoke_3
+ ___26-[PLOperator logDMAEntry:]_block_invoke_3.cold.1
+ ___26-[PLOperator postEntries:]_block_invoke.101
+ ___26-[PLOperator postEntries:]_block_invoke.101.cold.1
+ ___26-[PLOperator postEntries:]_block_invoke.101.cold.2
+ ___26-[PLOperator postEntries:]_block_invoke.108
+ ___26-[PLOperator postEntries:]_block_invoke_2.102
+ ___26-[PLTimer setTimerActive:]_block_invoke.23
+ ___26-[PLTimer setTimerActive:]_block_invoke.23.cold.1
+ ___26-[PLTimer setTimerActive:]_block_invoke_2.24
+ ___27-[PLArchiveManager migrate]_block_invoke.406
+ ___27-[PLMonotonicTimer _cancel]_block_invoke.42
+ ___27-[PLMonotonicTimer _cancel]_block_invoke.48
+ ___28-[PLMonotonicTimer schedule]_block_invoke.30
+ ___28-[PLMonotonicTimer schedule]_block_invoke.34
+ ___29+[PLUtilities deviceBootUUID]_block_invoke.117
+ ___29-[PLSubmissionFilePLL submit]_block_invoke.116
+ ___29-[PLXPCRelay relayConnection]_block_invoke.157.cold.1
+ ___29-[PLXPCRelay relayConnection]_block_invoke.157.cold.2
+ ___29-[PLXPCRelay relayConnection]_block_invoke.157.cold.3
+ ___29-[PLXPCRelay relayConnection]_block_invoke.157.cold.4
+ ___29-[PLXPCRelay relayConnection]_block_invoke.160
+ ___29-[PLXPCRelay relayConnection]_block_invoke.167
+ ___29-[PLXPCRelay relayConnection]_block_invoke.173
+ ___29-[PLXPCRelay relayConnection]_block_invoke.179
+ ___29-[PLXPCRelay relayConnection]_block_invoke.185
+ ___30-[PLMonotonicTimer reschedule]_block_invoke.89
+ ___30-[PLMonotonicTimer reschedule]_block_invoke.95
+ ___33-[PLSemaphore waitWithBlockSync:]_block_invoke.45
+ ___34-[PLSQLiteConnection updateEntry:]_block_invoke.668
+ ___34-[PLSQLiteConnection updateEntry:]_block_invoke.674
+ ___34-[PLSQLiteConnection updateEntry:]_block_invoke.680
+ ___34-[PLSemaphore signalDoneByObject:]_block_invoke.26
+ ___34-[PLSemaphore signalDoneByObject:]_block_invoke.32
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.102
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.108
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.114
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.120
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.126
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.132
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.141
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.147
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.57
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.63
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.69
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.75
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.87
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.93
+ ___35+[PPSCoreStorage setupEntryObjects]_block_invoke.30
+ ___35-[PLArchiveManager migrateArchive:]_block_invoke.390
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.400
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.400.cold.1
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.406
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.411
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.411.cold.1
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke_2.412
+ ___35-[PLSQLiteConnection runTrimQuery:]_block_invoke.325
+ ___35-[PLSQLiteConnection runTrimQuery:]_block_invoke.331
+ ___36-[PLTimeReferenceDynamic setOffset:]_block_invoke.50
+ ___37+[PLUtilities exitWithReason:action:]_block_invoke.175
+ ___37+[PLUtilities exitWithReason:action:]_block_invoke_9
+ ___37-[PLCoreStorage blockingFlushQueues:]_block_invoke.681
+ ___37-[PLCoreStorage blockingFlushQueues:]_block_invoke.685
+ ___37-[PLCoreStorage blockingFlushQueues:]_block_invoke.685.cold.1
+ ___37-[PLCoreStorage blockingFlushQueues:]_block_invoke.691
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.734
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.740
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.747
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.753
+ ___37-[PLStorageCache entryIDForNewEntry:]_block_invoke.100
+ ___37-[PLStorageCache entryIDForNewEntry:]_block_invoke.115
+ ___37-[PLSubmissions submitReasonForToday]_block_invoke.80
+ ___37-[PLSubmissions submitReasonForToday]_block_invoke.86
+ ___37-[PLSubmissions submitReasonForToday]_block_invoke.92
+ ___37-[PLSubmissions taskingModeSafeguard]_block_invoke.331
+ ___38+[PPSEntryKey allBaseKeysForEntryKey:]_block_invoke
+ ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.367
+ ___38-[PLStorageCache addToLastEntryCache:]_block_invoke.87
+ ___38-[PLSubmissionFileBDC getBDCPlistFile]_block_invoke.50
+ ___38-[PLSubmissionFileBDC getBDCPlistFile]_block_invoke.50.cold.1
+ ___38-[PLTimeReference getHourBucketOffset]_block_invoke.23
+ ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.29
+ ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.29.cold.1
+ ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.37
+ ___39+[PLAppDeletion constructUpdateQueries]_block_invoke.101
+ ___39+[PLNetworkUtilities handleIPSecEvent:]_block_invoke.150
+ ___39+[PLNetworkUtilities handleIPSecEvent:]_block_invoke.156
+ ___39+[PLUtilities bundleIDFromProcessName:]_block_invoke
+ ___39+[PLUtilities bundleIDFromProcessName:]_block_invoke_2
+ ___39+[PPSEntryKey allArrayKeysForEntryKey:]_block_invoke
+ ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.645
+ ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.647
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.106
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.117
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.121
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.125
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.129
+ ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.133
+ ___41+[PLNetworkUtilities getNetworkWakeInfo:]_block_invoke.123
+ ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.296
+ ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.302
+ ___41+[PPSEntryKey allDynamicKeysForEntryKey:]_block_invoke
+ ___41-[PLCoreStorage initOperatorDependancies]_block_invoke.303
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128.cold.1
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128.cold.2
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128.cold.3
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.128.cold.4
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.134
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.141
+ ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.147
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.310
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.316
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.322
+ ___42-[PLSQLiteConnection removeEmptyOldTables]_block_invoke.379
+ ___42-[PLSQLiteConnection writeDynamicEntries:]_block_invoke.629
+ ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.47
+ ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.47.cold.1
+ ___43+[PLNetworkUtilities handlePowerWakeEvent:]_block_invoke.144
+ ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.56
+ ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.56.cold.1
+ ___44-[PLSQLiteConnection scheduleIntegrityCheck]_block_invoke.77
+ ___44-[PLStorageCache lastEntryCachePruneToDate:]_block_invoke.64
+ ___44-[PLStorageCache lastEntryCachePruneToDate:]_block_invoke.69
+ ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.25
+ ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.30
+ ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.30.cold.1
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.335
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.341
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.351
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.362
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.368
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.377
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.399
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.405
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.411
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.418
+ ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.279
+ ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.293
+ ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.312
+ ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke_2.305
+ ___45-[PPSFeatureFlagReaderHelper getFeatureFlags]_block_invoke
+ ___46+[PLNetworkUtilities getUnattributedWakeInfo:]_block_invoke.132
+ ___46-[PLActivityCriterionEntry didEnableActivity:]_block_invoke.38
+ ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.368
+ ___46-[PLOperator subscribeNotificationsForEntries]_block_invoke.157
+ ___46-[PLStorageCache insertIntoStagingEntryCache:]_block_invoke.158
+ ___46-[PPSSQLStorage handleSchemaMismatchForTable:]_block_invoke.155
+ ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.104
+ ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.96
+ ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.96.cold.1
+ ___47+[PLNetworkUtilities getNormalizedIPV6Address:]_block_invoke.179
+ ___47-[PLCoreStorage blockingFlushCachesWithReason:]_block_invoke.672
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.247.cold.1
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.247.cold.2
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.247.cold.3
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.258
+ ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.268
+ ___48+[PLEntryKey setupEntryObjectsForOperatorClass:]_block_invoke.16
+ ___48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.715
+ ___49-[PLStorageCache clearLastEntryCacheForEntryKey:]_block_invoke.55
+ ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.31
+ ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.38
+ ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.53
+ ___49-[PPSFeatureFlagReaderHelper createXPCConnection]_block_invoke
+ ___49-[PPSFeatureFlagReaderHelper createXPCConnection]_block_invoke.10
+ ___49-[PPSFeatureFlagReaderHelper createXPCConnection]_block_invoke.10.cold.1
+ ___49-[PPSFeatureFlagReaderHelper createXPCConnection]_block_invoke.13
+ ___49-[PPSFeatureFlagReaderHelper createXPCConnection]_block_invoke.13.cold.1
+ ___49-[PPSFeatureFlagReaderHelper createXPCConnection]_block_invoke.cold.1
+ ___50-[PLSQLiteConnection createTableName:withColumns:]_block_invoke.474
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.255
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.255.cold.1
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.255.cold.2
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.255.cold.3
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.261
+ ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.268
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.177
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.183
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.189
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.195
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.199
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.199.cold.1
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.199.cold.2
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.199.cold.3
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.199.cold.4
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.199.cold.5
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.203
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.209
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.215
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.221
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.231
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_2.200
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_2.235
+ ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_3.239
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.188
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.197
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.206
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.212
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.230
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.236
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.242
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.251
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.54
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.60
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.64
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.64.cold.1
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.64.cold.2
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.70
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.77
+ ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.83
+ ___51-[PLSQLiteConnection entriesForKey:withProperties:]_block_invoke.758
+ ___51-[PLSubmissionFile submitLogToiCloud:WithCompress:]_block_invoke.186
+ ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.16
+ ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.16.cold.1
+ ___56+[PLOperator createEntriesForMetrics:withData:withDate:]_block_invoke.cold.3
+ ___57-[PLSubmissionFilePLL generateSubmissionTagForCurrentLog]_block_invoke.51
+ ___57-[PLSubmissionFilePLL generateSubmissionTagForCurrentLog]_block_invoke_2.52
+ ___58-[PLIOHIDOperatorComposition initWithOperator:forService:]_block_invoke.27
+ ___58-[PLIOHIDOperatorComposition initWithOperator:forService:]_block_invoke.36
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.107
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.107.cold.1
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.107.cold.2
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.108
+ ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.109
+ ___59-[PLStorageCache flushStagingAggregateEntryCacheToDatabase]_block_invoke.248
+ ___61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.874
+ ___61-[PLEntryDefinition commonTypeDict_IntegerFormat_withUnit_mJ]_block_invoke
+ ___61-[PLStorageCache updateStagingEntryCacheWithEntry:withBlock:]_block_invoke.164
+ ___61-[PLStorageCache updateStagingEntryCacheWithEntry:withBlock:]_block_invoke.167
+ ___62-[PLCoreStorage(XPCScheduling) registerDailyTasks_XPCActivity]_block_invoke.38
+ ___62-[PLCoreStorage(XPCScheduling) registerDailyTasks_XPCActivity]_block_invoke.40
+ ___63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.776
+ ___64-[PLSubmissions(XPCScheduling) registerUploadSchedulingActivity]_block_invoke.14
+ ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.99
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.37
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.37.cold.1
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.38
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.38.cold.1
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.39
+ ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.39.cold.1
+ ___68-[PLIOKitOperatorComposition initWithOperator:forService:withBlock:]_block_invoke.34
+ ___68-[PLSQLiteConnection trimAllTablesFromDate:toDate:withTableFilters:]_block_invoke.289
+ ___68-[PLSQLiteConnection trimAllTablesFromDate:toDate:withTableFilters:]_block_invoke.309
+ ___73-[PLTimeReferenceDynamic unregisterForTimeChangedCallbackWithIdentifier:]_block_invoke.82
+ ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.136
+ ___74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.537
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82.cold.1
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82.cold.2
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82.cold.3
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.86
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.86.cold.1
+ ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.724
+ ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.730
+ ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.56
+ ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.62
+ ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.68
+ ___82-[PLTimeReferenceDynamic registerForTimeChangedCallbackWithIdentifier:usingBlock:]_block_invoke.76
+ ___87-[PLSubmissionFile logSubmissionResultToCAWithErrorType:withFileType:withOverrideKeys:]_block_invoke.87
+ ___89-[PLOperator postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:]_block_invoke.137
+ ___93-[PLEnhancedTaskingAgent logAggregatedDataFromSignpostWithPayload:withStartDate:withEndDate:]_block_invoke.119
+ ___Block_byref_object_copy_.165
+ ___Block_byref_object_copy_.710
+ ___Block_byref_object_dispose_.166
+ ___Block_byref_object_dispose_.711
+ ___PLLogArchiving_block_invoke
+ ___PLLogTimeManager_block_invoke
+ ___PPSDataStreamLog_block_invoke
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_40_e8_32s_e40_"PLEntry"24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e25_v32?0"NSString"816^B24ls32l8r56l8s40l8s48l8
+ ___block_literal_global.103
+ ___block_literal_global.104
+ ___block_literal_global.105
+ ___block_literal_global.107
+ ___block_literal_global.11
+ ___block_literal_global.12
+ ___block_literal_global.122
+ ___block_literal_global.14
+ ___block_literal_global.141
+ ___block_literal_global.16
+ ___block_literal_global.172
+ ___block_literal_global.177
+ ___block_literal_global.187
+ ___block_literal_global.195
+ ___block_literal_global.199
+ ___block_literal_global.213
+ ___block_literal_global.218
+ ___block_literal_global.221
+ ___block_literal_global.224
+ ___block_literal_global.228
+ ___block_literal_global.231
+ ___block_literal_global.233
+ ___block_literal_global.238
+ ___block_literal_global.243
+ ___block_literal_global.244
+ ___block_literal_global.248
+ ___block_literal_global.258
+ ___block_literal_global.263
+ ___block_literal_global.267
+ ___block_literal_global.271
+ ___block_literal_global.273
+ ___block_literal_global.275
+ ___block_literal_global.285
+ ___block_literal_global.287
+ ___block_literal_global.29
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.297
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.306
+ ___block_literal_global.31
+ ___block_literal_global.314
+ ___block_literal_global.321
+ ___block_literal_global.326
+ ___block_literal_global.328
+ ___block_literal_global.33
+ ___block_literal_global.333
+ ___block_literal_global.338
+ ___block_literal_global.347
+ ___block_literal_global.350
+ ___block_literal_global.365
+ ___block_literal_global.383
+ ___block_literal_global.39
+ ___block_literal_global.401
+ ___block_literal_global.407
+ ___block_literal_global.409
+ ___block_literal_global.414
+ ___block_literal_global.419
+ ___block_literal_global.421
+ ___block_literal_global.423
+ ___block_literal_global.427
+ ___block_literal_global.430
+ ___block_literal_global.433
+ ___block_literal_global.436
+ ___block_literal_global.439
+ ___block_literal_global.444
+ ___block_literal_global.449
+ ___block_literal_global.458
+ ___block_literal_global.466
+ ___block_literal_global.51
+ ___block_literal_global.515
+ ___block_literal_global.53
+ ___block_literal_global.57
+ ___block_literal_global.59
+ ___block_literal_global.603
+ ___block_literal_global.61
+ ___block_literal_global.65
+ ___block_literal_global.662
+ ___block_literal_global.664
+ ___block_literal_global.675
+ ___block_literal_global.680
+ ___block_literal_global.684
+ ___block_literal_global.687
+ ___block_literal_global.690
+ ___block_literal_global.693
+ ___block_literal_global.80
+ ___block_literal_global.808
+ ___block_literal_global.81
+ ___block_literal_global.831
+ ___block_literal_global.85
+ ___block_literal_global.851
+ ___block_literal_global.88
+ ___block_literal_global.9
+ ___block_literal_global.98
+ ___kQueueEvent_block_invoke.104
+ ___logPPSFeatureFlagReaderHelper_block_invoke
+ __cancel.classDebugEnabled.41
+ __cancel.classDebugEnabled.47
+ __cancel.defaultOnce.40
+ __cancel.defaultOnce.46
+ __unnamed_array_storage.102
+ __unnamed_array_storage.103
+ __unnamed_array_storage.111
+ __unnamed_array_storage.12
+ __unnamed_array_storage.130
+ __unnamed_array_storage.142
+ __unnamed_array_storage.160
+ __unnamed_array_storage.162
+ __unnamed_array_storage.163
+ __unnamed_array_storage.164
+ __unnamed_array_storage.167
+ __unnamed_array_storage.168
+ __unnamed_array_storage.171
+ __unnamed_array_storage.172
+ __unnamed_array_storage.175
+ __unnamed_array_storage.176
+ __unnamed_array_storage.180
+ __unnamed_array_storage.181
+ __unnamed_array_storage.184
+ __unnamed_array_storage.192
+ __unnamed_array_storage.193
+ __unnamed_array_storage.200
+ __unnamed_array_storage.214
+ __unnamed_array_storage.217
+ __unnamed_array_storage.218
+ __unnamed_array_storage.219
+ __unnamed_array_storage.220
+ __unnamed_array_storage.232
+ __unnamed_array_storage.233
+ __unnamed_array_storage.236
+ __unnamed_array_storage.237
+ __unnamed_array_storage.245
+ __unnamed_array_storage.246
+ __unnamed_array_storage.268
+ __unnamed_array_storage.269
+ __unnamed_array_storage.272
+ __unnamed_array_storage.273
+ __unnamed_array_storage.284
+ __unnamed_array_storage.29
+ __unnamed_array_storage.290
+ __unnamed_array_storage.291
+ __unnamed_array_storage.301
+ __unnamed_array_storage.309
+ __unnamed_array_storage.310
+ __unnamed_array_storage.311
+ __unnamed_array_storage.322
+ __unnamed_array_storage.323
+ __unnamed_array_storage.326
+ __unnamed_array_storage.327
+ __unnamed_array_storage.334
+ __unnamed_array_storage.335
+ __unnamed_array_storage.336
+ __unnamed_array_storage.339
+ __unnamed_array_storage.34
+ __unnamed_array_storage.345
+ __unnamed_array_storage.350
+ __unnamed_array_storage.356
+ __unnamed_array_storage.360
+ __unnamed_array_storage.364
+ __unnamed_array_storage.365
+ __unnamed_array_storage.372
+ __unnamed_array_storage.373
+ __unnamed_array_storage.374
+ __unnamed_array_storage.422
+ __unnamed_array_storage.423
+ __unnamed_array_storage.43
+ __unnamed_array_storage.431
+ __unnamed_array_storage.432
+ __unnamed_array_storage.47
+ __unnamed_array_storage.474
+ __unnamed_array_storage.54
+ __unnamed_array_storage.548
+ __unnamed_array_storage.549
+ __unnamed_array_storage.55
+ __unnamed_array_storage.569
+ __unnamed_array_storage.573
+ __unnamed_array_storage.574
+ __unnamed_array_storage.580
+ __unnamed_array_storage.581
+ __unnamed_array_storage.587
+ __unnamed_array_storage.591
+ __unnamed_array_storage.595
+ __unnamed_array_storage.599
+ __unnamed_array_storage.600
+ __unnamed_array_storage.615
+ __unnamed_array_storage.619
+ __unnamed_array_storage.620
+ __unnamed_array_storage.63
+ __unnamed_array_storage.819
+ __unnamed_array_storage.820
+ __unnamed_array_storage.853
+ __unnamed_array_storage.857
+ __unnamed_array_storage.861
+ __unnamed_array_storage.88
+ __unnamed_array_storage.882
+ __unnamed_array_storage.883
+ __unnamed_array_storage.91
+ __unnamed_array_storage.92
+ __unnamed_array_storage.98
+ __unnamed_array_storage.99
+ _blockingFlushCachesWithReason:.classDebugEnabled.671
+ _blockingFlushCachesWithReason:.defaultOnce.670
+ _blockingFlushQueues:.classDebugEnabled.680
+ _blockingFlushQueues:.classDebugEnabled.690
+ _blockingFlushQueues:.defaultOnce.679
+ _blockingFlushQueues:.defaultOnce.689
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.55
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.61
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.67
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.54
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.60
+ _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.66
+ _bundleIDFromProcessName:.onceToken
+ _bundleIDFromProcessName:.processNameToBundleID
+ _checkTaskingCompletionStatus.classDebugEnabled.286
+ _checkTaskingCompletionStatus.classDebugEnabled.304
+ _checkTaskingCompletionStatus.defaultOnce.285
+ _checkTaskingCompletionStatus.defaultOnce.303
+ _clearLastEntryCacheForEntryKey:.classDebugEnabled.54
+ _clearLastEntryCacheForEntryKey:.defaultOnce.53
+ _clearTaskingDefaults.classDebugEnabled.309
+ _clearTaskingDefaults.classDebugEnabled.315
+ _clearTaskingDefaults.classDebugEnabled.321
+ _clearTaskingDefaults.defaultOnce.308
+ _clearTaskingDefaults.defaultOnce.314
+ _clearTaskingDefaults.defaultOnce.320
+ _commonTypeDict_IntegerFormat_withUnit_mJ._typedict_integer
+ _commonTypeDict_IntegerFormat_withUnit_mJ.onceToken
+ _createTableName:withColumns:.classDebugEnabled.473
+ _createTableName:withColumns:.defaultOnce.472
+ _currentTime.classDebugEnabled.36
+ _currentTime.defaultOnce.35
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.187
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.196
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.205
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.211
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.229
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.235
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.241
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.250
+ _decodeIPPacket:encryptedPath:.defaultOnce.186
+ _decodeIPPacket:encryptedPath:.defaultOnce.195
+ _decodeIPPacket:encryptedPath:.defaultOnce.204
+ _decodeIPPacket:encryptedPath:.defaultOnce.210
+ _decodeIPPacket:encryptedPath:.defaultOnce.228
+ _decodeIPPacket:encryptedPath:.defaultOnce.234
+ _decodeIPPacket:encryptedPath:.defaultOnce.240
+ _decodeIPPacket:encryptedPath:.defaultOnce.249
+ _decorateFileAtPath:.classDebugEnabled.105
+ _decorateFileAtPath:.classDebugEnabled.116
+ _decorateFileAtPath:.classDebugEnabled.120
+ _decorateFileAtPath:.classDebugEnabled.124
+ _decorateFileAtPath:.classDebugEnabled.128
+ _decorateFileAtPath:.classDebugEnabled.132
+ _decorateFileAtPath:.defaultOnce.104
+ _decorateFileAtPath:.defaultOnce.115
+ _decorateFileAtPath:.defaultOnce.119
+ _decorateFileAtPath:.defaultOnce.123
+ _decorateFileAtPath:.defaultOnce.127
+ _decorateFileAtPath:.defaultOnce.131
+ _deviceBootUUID.classDebugEnabled.116
+ _deviceBootUUID.defaultOnce.115
+ _didEnableActivity:.classDebugEnabled.24
+ _didEnableActivity:.classDebugEnabled.37
+ _didEnableActivity:.defaultOnce.23
+ _didEnableActivity:.defaultOnce.36
+ _entriesForKey:withProperties:.classDebugEnabled.757
+ _entriesForKey:withProperties:.defaultOnce.756
+ _entryIDForNewEntry:.classDebugEnabled.114
+ _entryIDForNewEntry:.classDebugEnabled.99
+ _entryIDForNewEntry:.defaultOnce.113
+ _entryIDForNewEntry:.defaultOnce.98
+ _flushCachesWithReason:.classDebugEnabled.644
+ _flushCachesWithReason:.defaultOnce.646
+ _flushStagingAggregateEntryCacheToDatabase.classDebugEnabled.247
+ _flushStagingAggregateEntryCacheToDatabase.defaultOnce.246
+ _flushStagingEntryCacheToDatabase.classDebugEnabled.238
+ _flushStagingEntryCacheToDatabase.defaultOnce.176
+ _flushStagingEntryCacheToDatabase.defaultOnce.237
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.135
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.134
+ _getHourBucketOffset.classDebugEnabled.22
+ _getHourBucketOffset.defaultOnce.21
+ _getNetworkWakeInfo:.classDebugEnabled.122
+ _getNetworkWakeInfo:.defaultOnce.121
+ _getNormalizedIPV6Address:.classDebugEnabled.178
+ _getNormalizedIPV6Address:.defaultOnce.177
+ _getUnattributedWakeInfo:.classDebugEnabled.131
+ _getUnattributedWakeInfo:.defaultOnce.130
+ _handleIPSecEvent:.classDebugEnabled.149
+ _handleIPSecEvent:.classDebugEnabled.155
+ _handleIPSecEvent:.defaultOnce.148
+ _handleIPSecEvent:.defaultOnce.154
+ _handlePeer:forEvent:.classDebugEnabled.101
+ _handlePeer:forEvent:.classDebugEnabled.107
+ _handlePeer:forEvent:.classDebugEnabled.113
+ _handlePeer:forEvent:.classDebugEnabled.119
+ _handlePeer:forEvent:.classDebugEnabled.125
+ _handlePeer:forEvent:.classDebugEnabled.131
+ _handlePeer:forEvent:.classDebugEnabled.140
+ _handlePeer:forEvent:.classDebugEnabled.146
+ _handlePeer:forEvent:.classDebugEnabled.56
+ _handlePeer:forEvent:.classDebugEnabled.62
+ _handlePeer:forEvent:.classDebugEnabled.68
+ _handlePeer:forEvent:.classDebugEnabled.74
+ _handlePeer:forEvent:.classDebugEnabled.86
+ _handlePeer:forEvent:.classDebugEnabled.92
+ _handlePeer:forEvent:.defaultOnce.100
+ _handlePeer:forEvent:.defaultOnce.106
+ _handlePeer:forEvent:.defaultOnce.112
+ _handlePeer:forEvent:.defaultOnce.118
+ _handlePeer:forEvent:.defaultOnce.124
+ _handlePeer:forEvent:.defaultOnce.130
+ _handlePeer:forEvent:.defaultOnce.139
+ _handlePeer:forEvent:.defaultOnce.145
+ _handlePeer:forEvent:.defaultOnce.55
+ _handlePeer:forEvent:.defaultOnce.61
+ _handlePeer:forEvent:.defaultOnce.67
+ _handlePeer:forEvent:.defaultOnce.73
+ _handlePeer:forEvent:.defaultOnce.85
+ _handlePeer:forEvent:.defaultOnce.91
+ _handlePowerWakeEvent:.classDebugEnabled.143
+ _handlePowerWakeEvent:.defaultOnce.142
+ _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.536
+ _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.535
+ _init.classDebugEnabled.38
+ _init.defaultOnce.37
+ _initWithOperator:forService:.classDebugEnabled.35
+ _initWithOperator:forService:.defaultOnce.34
+ _initWithOperator:forService:withBlock:.classDebugEnabled.33
+ _initWithOperator:forService:withBlock:.defaultOnce.32
+ _insertIntoStagingEntryCache:.defaultOnce.157
+ _isESPPacket:offset:.classDebugEnabled.295
+ _isESPPacket:offset:.classDebugEnabled.301
+ _isESPPacket:offset:.defaultOnce.294
+ _isESPPacket:offset:.defaultOnce.300
+ _kPLEDDMACompliantKeys
+ _kPLTaskingEndNotification_block_invoke_5.classDebugEnabled.739
+ _kPLTaskingEndNotification_block_invoke_5.classDebugEnabled.746
+ _kPLTaskingEndNotification_block_invoke_5.classDebugEnabled.752
+ _kPLTaskingEndNotification_block_invoke_5.defaultOnce.738
+ _kPLTaskingEndNotification_block_invoke_5.defaultOnce.745
+ _kPLTaskingEndNotification_block_invoke_5.defaultOnce.751
+ _lastEntryCachePruneToDate:.classDebugEnabled.63
+ _lastEntryCachePruneToDate:.defaultOnce.62
+ _lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.873
+ _lastEntryForKey:withComparisons:isSingleton:.defaultOnce.872
+ _logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.923
+ _logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.924
+ _logPPSFeatureFlagReaderHelper
+ _logPPSFeatureFlagReaderHelper._logHandle
+ _logPPSFeatureFlagReaderHelper.onceToken
+ _migrateArchive:.classDebugEnabled.389
+ _migrateArchive:.defaultOnce.388
+ _objc_msgSend$DMAKeys
+ _objc_msgSend$DMAKeysForEntryDefinition:
+ _objc_msgSend$XCSQLConnection
+ _objc_msgSend$absoluteString
+ _objc_msgSend$addAuxiliaryType:withEntryKey:
+ _objc_msgSend$allArrayKeysForEntryKey:
+ _objc_msgSend$allBaseKeysForEntryKey:
+ _objc_msgSend$allDynamicKeysForEntryKey:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$anyMetricsForEntryKey:
+ _objc_msgSend$arrayKeyConfigsForEntryKey:
+ _objc_msgSend$arrayMetricsForEntryKey:
+ _objc_msgSend$auxiliaryType
+ _objc_msgSend$baseMetricsForEntryKey:
+ _objc_msgSend$bundleIDFromProcessName:
+ _objc_msgSend$conditionCheckForXcodeUserActions
+ _objc_msgSend$dataFormatForMetric:auxiliaryMetrics:
+ _objc_msgSend$defaultTaskingTypeParameters
+ _objc_msgSend$deprecateTablesXCSQL
+ _objc_msgSend$dictionaryWithValuesForKeys:
+ _objc_msgSend$dynamicMetricsForEntryKey:
+ _objc_msgSend$dynamicTableNameForEntryKey:
+ _objc_msgSend$filterEntryLoggingForEntryKey:
+ _objc_msgSend$getFeatureFlags:
+ _objc_msgSend$getXCSQLFile
+ _objc_msgSend$hasArrayKeys:
+ _objc_msgSend$hasDMAKeys
+ _objc_msgSend$hasDMAKeysForEntryDefinition:
+ _objc_msgSend$hasDynamicKeys:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$isPPSEnabled
+ _objc_msgSend$logDMAEntry:
+ _objc_msgSend$monitor
+ _objc_msgSend$monitorMetricsForSubsystem:category:payload:
+ _objc_msgSend$monitoredCategory
+ _objc_msgSend$monitoredSubsystem
+ _objc_msgSend$obfuscateTimestampsForTable:connection:withOffset:
+ _objc_msgSend$ondemand
+ _objc_msgSend$perModelTaskingTypeParameters
+ _objc_msgSend$quarantineWithExitReason:
+ _objc_msgSend$randomizedBaseOffset
+ _objc_msgSend$sanitizeCAPayload:
+ _objc_msgSend$setBlobFailureReason:
+ _objc_msgSend$setMonitor:
+ _objc_msgSend$setMonitoredCategory:
+ _objc_msgSend$setMonitoredSubsystem:
+ _objc_msgSend$setSubmittedFilesMask:
+ _objc_msgSend$setValuesForKeysWithDictionary:
+ _objc_msgSend$setupArrayTableForEntryKey:withName:withConnection:
+ _objc_msgSend$setupDynamicTableForEntryKey:withName:withConnection:
+ _objc_msgSend$sortedSqlFormatedColumnNamesForTableInsert:
+ _objc_msgSend$splitBySubmissionType
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$submissionCategory
+ _objc_msgSend$submissionMaskToString
+ _objc_msgSend$submitXC
+ _objc_msgSend$taskingBuild
+ _objc_msgSend$taskingDeviceModels
+ _objc_msgSend$taskingPercentage
+ _objc_msgSend$taskingPopulation
+ _objc_msgSend$trimXcodeOrganizerLog
+ _objc_msgSend$writeDynamicEntriesToPPS:
+ _postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:.classDebugEnabled.136
+ _postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:.defaultOnce.135
+ _registerDailyTasks.classDebugEnabled.405
+ _registerDailyTasks.defaultOnce.404
+ _registerEPLNotificationWithQueue:.classDebugEnabled.103
+ _registerEPLNotificationWithQueue:.defaultOnce.102
+ _registerForTimeChangedCallbackWithIdentifier:usingBlock:.classDebugEnabled.75
+ _registerForTimeChangedCallbackWithIdentifier:usingBlock:.defaultOnce.74
+ _relayConnection.classDebugEnabled.178
+ _relayConnection.classDebugEnabled.184
+ _relayConnection.defaultOnce.177
+ _relayConnection.defaultOnce.183
+ _relayConnectionSync_block_invoke.classDebugEnabled.35
+ _relayConnectionSync_block_invoke.defaultOnce.34
+ _relayConnectionSync_block_invoke_3.classDebugEnabled.159
+ _relayConnectionSync_block_invoke_3.classDebugEnabled.166
+ _relayConnectionSync_block_invoke_3.classDebugEnabled.172
+ _relayConnectionSync_block_invoke_3.defaultOnce.158
+ _relayConnectionSync_block_invoke_3.defaultOnce.165
+ _relayConnectionSync_block_invoke_3.defaultOnce.171
+ _removeEmptyOldTables.classDebugEnabled.378
+ _removeEmptyOldTables.defaultOnce.377
+ _reschedule.classDebugEnabled.88
+ _reschedule.classDebugEnabled.94
+ _reschedule.defaultOnce.87
+ _reschedule.defaultOnce.93
+ _runTrimQuery:.classDebugEnabled.324
+ _runTrimQuery:.classDebugEnabled.330
+ _runTrimQuery:.defaultOnce.323
+ _runTrimQuery:.defaultOnce.329
+ _schedule.classDebugEnabled.29
+ _schedule.classDebugEnabled.36
+ _schedule.defaultOnce.28
+ _schedule.defaultOnce.35
+ _setEnabled:.classDebugEnabled.15
+ _setEnabled:.classDebugEnabled.23
+ _setEnabled:.classDebugEnabled.30
+ _setEnabled:.defaultOnce.14
+ _setEnabled:.defaultOnce.22
+ _setEnabled:.defaultOnce.29
+ _shouldStartTaskingToday.classDebugEnabled.334
+ _shouldStartTaskingToday.classDebugEnabled.340
+ _shouldStartTaskingToday.classDebugEnabled.361
+ _shouldStartTaskingToday.classDebugEnabled.367
+ _shouldStartTaskingToday.classDebugEnabled.376
+ _shouldStartTaskingToday.classDebugEnabled.398
+ _shouldStartTaskingToday.classDebugEnabled.404
+ _shouldStartTaskingToday.classDebugEnabled.410
+ _shouldStartTaskingToday.defaultOnce.333
+ _shouldStartTaskingToday.defaultOnce.339
+ _shouldStartTaskingToday.defaultOnce.360
+ _shouldStartTaskingToday.defaultOnce.366
+ _shouldStartTaskingToday.defaultOnce.375
+ _shouldStartTaskingToday.defaultOnce.397
+ _shouldStartTaskingToday.defaultOnce.403
+ _shouldStartTaskingToday.defaultOnce.409
+ _signalDoneByObject:.classDebugEnabled.25
+ _signalDoneByObject:.classDebugEnabled.31
+ _signalDoneByObject:.defaultOnce.24
+ _signalDoneByObject:.defaultOnce.30
+ _submitLogToiCloud:WithCompress:.classDebugEnabled.185
+ _submitLogToiCloud:WithCompress:.defaultOnce.184
+ _submitReasonForToday.classDebugEnabled.79
+ _submitReasonForToday.classDebugEnabled.85
+ _submitReasonForToday.classDebugEnabled.91
+ _submitReasonForToday.defaultOnce.78
+ _submitReasonForToday.defaultOnce.84
+ _submitReasonForToday.defaultOnce.90
+ _subscribeNotificationsForEntries.classDebugEnabled.156
+ _subscribeNotificationsForEntries.defaultOnce.155
+ _taskingModeSafeguard.classDebugEnabled.342
+ _taskingModeSafeguard.defaultOnce.341
+ _timerFiredForMonotonicFireDate:.classDebugEnabled.53
+ _timerFiredForMonotonicFireDate:.classDebugEnabled.59
+ _timerFiredForMonotonicFireDate:.classDebugEnabled.76
+ _timerFiredForMonotonicFireDate:.classDebugEnabled.82
+ _timerFiredForMonotonicFireDate:.defaultOnce.52
+ _timerFiredForMonotonicFireDate:.defaultOnce.58
+ _timerFiredForMonotonicFireDate:.defaultOnce.75
+ _timerFiredForMonotonicFireDate:.defaultOnce.81
+ _trimAllTablesFromDate:toDate:withTableFilters:.classDebugEnabled.288
+ _trimAllTablesFromDate:toDate:withTableFilters:.classDebugEnabled.308
+ _trimAllTablesFromDate:toDate:withTableFilters:.defaultOnce.287
+ _trimAllTablesFromDate:toDate:withTableFilters:.defaultOnce.307
+ _unregisterForTimeChangedCallbackWithIdentifier:.classDebugEnabled.81
+ _unregisterForTimeChangedCallbackWithIdentifier:.defaultOnce.80
+ _updateEntry:.classDebugEnabled.667
+ _updateEntry:.classDebugEnabled.673
+ _updateEntry:.classDebugEnabled.679
+ _updateEntry:.defaultOnce.666
+ _updateEntry:.defaultOnce.672
+ _updateEntry:.defaultOnce.678
+ _updateStagingEntryCacheWithEntry:withBlock:.classDebugEnabled.163
+ _updateStagingEntryCacheWithEntry:withBlock:.defaultOnce.162
+ _waitWithBlockSync:.classDebugEnabled.44
+ _waitWithBlockSync:.defaultOnce.43
+ _writeDynamicEntries:.classDebugEnabled.628
+ _writeDynamicEntries:.defaultOnce.627
+ _writeEntry:.classDebugEnabled.571
+ _writeEntry:.defaultOnce.570
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.723
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.729
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.722
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.728
- +[PLEntryNotificationOperatorComposition significantBatteryChangeNotificationWithOperator:withBlock:].cold.1
- +[PLEntryNotificationOperatorComposition significantBatteryChangeNotificationWithOperator:withMaxIntervalInSecs:withBlock:].cold.1
- +[PPSEntryKey allKeysForEntryKey:]
- +[PPSEntryKey versionHashForEntryKey:]
- -[PLTimeReferenceKernel currentTime].cold.3
- -[PPSSQLStorage handleSchemaMismatchForTable:].cold.1
- -[PPSSQLStorage handleSchemaMismatchForTable:].cold.2
- GCC_except_table100
- GCC_except_table103
- GCC_except_table108
- GCC_except_table71
- GCC_except_table93
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.369
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.376
- _PLSubmissionAnalyticsStateSuccess_block_invoke.classDebugEnabled.66
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.368
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.375
- _PLSubmissionAnalyticsStateSuccess_block_invoke.defaultOnce.65
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.classDebugEnabled.413
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.classDebugEnabled.420
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.classDebugEnabled.46
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.classDebugEnabled.77
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.defaultOnce.412
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.defaultOnce.419
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.defaultOnce.45
- _PLSubmissionAnalyticsStateSuccess_block_invoke_2.defaultOnce.76
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.124
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.131
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.classDebugEnabled.137
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.123
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.130
- _PLSubmissionAnalyticsStateSuccess_block_invoke_3.defaultOnce.136
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.classDebugEnabled
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.classDebugEnabled.173
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.classDebugEnabled.179
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.classDebugEnabled.185
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.classDebugEnabled.221
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.classDebugEnabled.225
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.classDebugEnabled.98
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.defaultOnce
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.defaultOnce.172
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.defaultOnce.178
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.defaultOnce.184
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.defaultOnce.220
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.defaultOnce.224
- _PLSubmissionAnalyticsStateSuccess_block_invoke_4.defaultOnce.97
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.193
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.199
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.205
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.classDebugEnabled.211
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.192
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.198
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.204
- _PLSubmissionAnalyticsStateSuccess_block_invoke_5.defaultOnce.210
- _PLSubmissionAnalyticsStateSuccess_block_invoke_6.classDebugEnabled
- _PLSubmissionAnalyticsStateSuccess_block_invoke_6.classDebugEnabled.251
- _PLSubmissionAnalyticsStateSuccess_block_invoke_6.classDebugEnabled.258
- _PLSubmissionAnalyticsStateSuccess_block_invoke_6.defaultOnce
- _PLSubmissionAnalyticsStateSuccess_block_invoke_6.defaultOnce.250
- _PLSubmissionAnalyticsStateSuccess_block_invoke_6.defaultOnce.257
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__116__pad_and_outputB7v160006IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__shared_weak_count16__release_sharedB7v160006Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B7v160006Ev
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__124__put_character_sequenceB7v160006IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- ___104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.825
- ___18-[PLOperator init]_block_invoke.30
- ___18-[PLXPCRelay init]_block_invoke.17
- ___21-[PLCoreStorage init]_block_invoke.61
- ___21-[PLCoreStorage init]_block_invoke.89
- ___21-[PLTimeManager init]_block_invoke.20
- ___21-[PLTimeManager init]_block_invoke.20.cold.1
- ___23-[PLKQueue setEnabled:]_block_invoke.13
- ___23-[PLKQueue setEnabled:]_block_invoke.21
- ___23-[PLKQueue setEnabled:]_block_invoke.28
- ___24-[PLXPCRelay startRelay]_block_invoke.27
- ___24-[PLXPCRelay startRelay]_block_invoke.27.cold.1
- ___24-[PLXPCRelay startRelay]_block_invoke.27.cold.2
- ___24-[PLXPCRelay startRelay]_block_invoke.33
- ___24-[PLXPCRelay startRelay]_block_invoke.38
- ___24-[PLXPCRelay startRelay]_block_invoke.38.cold.1
- ___24-[PLXPCRelay startRelay]_block_invoke_2.39
- ___25-[PLActivity runActivity]_block_invoke.14
- ___25-[PLActivity runActivity]_block_invoke.15
- ___25-[PLOperator flushBuffer]_block_invoke.54
- ___26-[PLOperator postEntries:]_block_invoke.92
- ___26-[PLOperator postEntries:]_block_invoke.92.cold.1
- ___26-[PLOperator postEntries:]_block_invoke.92.cold.2
- ___26-[PLOperator postEntries:]_block_invoke.99
- ___26-[PLOperator postEntries:]_block_invoke_2.93
- ___26-[PLTimer setTimerActive:]_block_invoke.20
- ___26-[PLTimer setTimerActive:]_block_invoke.20.cold.1
- ___26-[PLTimer setTimerActive:]_block_invoke_2.21
- ___27-[PLArchiveManager migrate]_block_invoke.414
- ___27-[PLArchiveManager migrate]_block_invoke.421
- ___27-[PLArchiveManager migrate]_block_invoke_2
- ___27-[PLArchiveManager recover]_block_invoke.370
- ___27-[PLArchiveManager recover]_block_invoke.377
- ___27-[PLArchiveManager recover]_block_invoke_2
- ___27-[PLMonotonicTimer _cancel]_block_invoke.39
- ___27-[PLMonotonicTimer _cancel]_block_invoke.45
- ___28-[PLMonotonicTimer schedule]_block_invoke.27
- ___28-[PLMonotonicTimer schedule]_block_invoke.31
- ___29+[PLUtilities deviceBootUUID]_block_invoke.105
- ___29-[PLSubmissionFilePLL submit]_block_invoke.110
- ___29-[PLXPCRelay relayConnection]_block_invoke.154
- ___29-[PLXPCRelay relayConnection]_block_invoke.154.cold.1
- ___29-[PLXPCRelay relayConnection]_block_invoke.154.cold.2
- ___29-[PLXPCRelay relayConnection]_block_invoke.154.cold.3
- ___29-[PLXPCRelay relayConnection]_block_invoke.154.cold.4
- ___29-[PLXPCRelay relayConnection]_block_invoke.164
- ___29-[PLXPCRelay relayConnection]_block_invoke.170
- ___29-[PLXPCRelay relayConnection]_block_invoke.176
- ___29-[PLXPCRelay relayConnection]_block_invoke.182
- ___30-[PLMonotonicTimer reschedule]_block_invoke.86
- ___30-[PLMonotonicTimer reschedule]_block_invoke.92
- ___33-[PLSemaphore waitWithBlockSync:]_block_invoke.42
- ___34+[PPSEntryKey allKeysForEntryKey:]_block_invoke
- ___34-[PLSQLiteConnection updateEntry:]_block_invoke.649
- ___34-[PLSQLiteConnection updateEntry:]_block_invoke.655
- ___34-[PLSQLiteConnection updateEntry:]_block_invoke.661
- ___34-[PLSemaphore signalDoneByObject:]_block_invoke.23
- ___34-[PLSemaphore signalDoneByObject:]_block_invoke.29
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.105
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.111
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.117
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.123
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.129
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.138
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.144
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.54
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.60
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.66
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.72
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.84
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.90
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.99
- ___35+[PPSCoreStorage setupEntryObjects]_block_invoke.19
- ___35-[PLArchiveManager migrateArchive:]_block_invoke.393
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.397
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.397.cold.1
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.403
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.408
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.408.cold.1
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke_2.409
- ___35-[PLSQLiteConnection runTrimQuery:]_block_invoke.314
- ___35-[PLSQLiteConnection runTrimQuery:]_block_invoke.320
- ___36-[PLTimeReferenceDynamic setOffset:]_block_invoke.47
- ___36-[PLTimeReferenceKernel currentTime]_block_invoke.10
- ___36-[PLTimeReferenceKernel currentTime]_block_invoke.19
- ___37+[PLUtilities exitWithReason:action:]_block_invoke.160
- ___37-[PLCoreStorage blockingFlushQueues:]_block_invoke.678
- ___37-[PLCoreStorage blockingFlushQueues:]_block_invoke.682
- ___37-[PLCoreStorage blockingFlushQueues:]_block_invoke.682.cold.1
- ___37-[PLCoreStorage blockingFlushQueues:]_block_invoke.688
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.731
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.737
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.744
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.750
- ___37-[PLStorageCache entryIDForNewEntry:]_block_invoke.106
- ___37-[PLStorageCache entryIDForNewEntry:]_block_invoke.91
- ___37-[PLSubmissions submitReasonForToday]_block_invoke.77
- ___37-[PLSubmissions submitReasonForToday]_block_invoke.83
- ___37-[PLSubmissions submitReasonForToday]_block_invoke.89
- ___37-[PLSubmissions taskingModeSafeguard]_block_invoke.330
- ___38+[PPSEntryKey versionHashForEntryKey:]_block_invoke
- ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.354
- ___38-[PLStorageCache addToLastEntryCache:]_block_invoke.78
- ___38-[PLSubmissionFileBDC getBDCPlistFile]_block_invoke.47
- ___38-[PLSubmissionFileBDC getBDCPlistFile]_block_invoke.47.cold.1
- ___38-[PLTimeReference getHourBucketOffset]_block_invoke.20
- ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.26
- ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.26.cold.1
- ___38-[PLTimeReferenceBaseband currentTime]_block_invoke.34
- ___39+[PLAppDeletion constructUpdateQueries]_block_invoke_3
- ___39+[PLNetworkUtilities handleIPSecEvent:]_block_invoke.147
- ___39+[PLNetworkUtilities handleIPSecEvent:]_block_invoke.153
- ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.642
- ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.644
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.103
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.114
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.118
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.122
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.126
- ___39-[PLSubmissionFile decorateFileAtPath:]_block_invoke.99
- ___41+[PLNetworkUtilities getNetworkWakeInfo:]_block_invoke.120
- ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.293
- ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.299
- ___41-[PLCoreStorage initOperatorDependancies]_block_invoke.300
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.119
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.119.cold.1
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.119.cold.2
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.119.cold.3
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.119.cold.4
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.125
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.132
- ___41-[PLStorageCache addToStagingEntryCache:]_block_invoke.138
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.272
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.278
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.284
- ___42-[PLSQLiteConnection removeEmptyOldTables]_block_invoke.368
- ___42-[PLSQLiteConnection writeDynamicEntries:]_block_invoke.607
- ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.41
- ___42-[RbdcConverterHelper createXPCConnection]_block_invoke.41.cold.1
- ___43+[PLNetworkUtilities handlePowerWakeEvent:]_block_invoke.138
- ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.50
- ___43-[SignpostReaderHelper createXPCConnection]_block_invoke.50.cold.1
- ___44-[PLSQLiteConnection scheduleIntegrityCheck]_block_invoke.74
- ___44-[PLStorageCache lastEntryCachePruneToDate:]_block_invoke.55
- ___44-[PLStorageCache lastEntryCachePruneToDate:]_block_invoke.60
- ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.22
- ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.27
- ___45-[PLActivityCriterionTime didEnableActivity:]_block_invoke.27.cold.1
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.297
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.303
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.313
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.324
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.330
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.339
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.361
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.367
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.373
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.380
- ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.278
- ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.292
- ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke.311
- ___45-[PLSubmissions checkTaskingCompletionStatus]_block_invoke_2.304
- ___46+[PLArchiveManager systemTimeChangedByOffset:]_block_invoke
- ___46+[PLArchiveManager systemTimeChangedByOffset:]_block_invoke.430
- ___46+[PLNetworkUtilities getUnattributedWakeInfo:]_block_invoke.129
- ___46-[PLActivityCriterionEntry didEnableActivity:]_block_invoke.35
- ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.355
- ___46-[PLOperator subscribeNotificationsForEntries]_block_invoke.148
- ___46-[PLStorageCache insertIntoStagingEntryCache:]_block_invoke.149
- ___46-[PPSSQLStorage handleSchemaMismatchForTable:]_block_invoke.136
- ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.101
- ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.93
- ___47+[PLDefaults registerEPLNotificationWithQueue:]_block_invoke.93.cold.1
- ___47+[PLNetworkUtilities getNormalizedIPV6Address:]_block_invoke.176
- ___47-[PLCoreStorage blockingFlushCachesWithReason:]_block_invoke.669
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.236
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.236.cold.1
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.236.cold.2
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.236.cold.3
- ___47-[PLSQLiteConnection mergeDataFromOtherDBFile:]_block_invoke.257
- ___48+[PLEntryKey setupEntryObjectsForOperatorClass:]_block_invoke.13
- ___48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.712
- ___49-[PLStorageCache clearLastEntryCacheForEntryKey:]_block_invoke.46
- ___49-[PPSCollectionOperator initOperatorDependancies]_block_invoke.28
- ___50-[PLSQLiteConnection createTableName:withColumns:]_block_invoke.463
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.246
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.246.cold.1
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.246.cold.2
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.246.cold.3
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.252
- ___50-[PLStorageCache addToStagingAggregateEntryCache:]_block_invoke.259
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.168
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.174
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.180
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.186
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.190
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.190.cold.1
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.190.cold.2
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.190.cold.3
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.190.cold.4
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.190.cold.5
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.194
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.200
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.206
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.212
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke.222
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_2.191
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_2.226
- ___50-[PLStorageCache flushStagingEntryCacheToDatabase]_block_invoke_3.230
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.185
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.194
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.203
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.209
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.227
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.233
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.239
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.248
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.51
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.57
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.61
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.61.cold.1
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.61.cold.2
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.67
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.74
- ___51-[PLMonotonicTimer timerFiredForMonotonicFireDate:]_block_invoke.80
- ___51-[PLSQLiteConnection entriesForKey:withProperties:]_block_invoke.739
- ___51-[PLSubmissionFile submitLogToiCloud:WithCompress:]_block_invoke.168
- ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.13
- ___51-[RbdcConverterHelper processRbdc:withServiceType:]_block_invoke.13.cold.1
- ___57-[PLSubmissionFilePLL generateSubmissionTagForCurrentLog]_block_invoke.48
- ___57-[PLSubmissionFilePLL generateSubmissionTagForCurrentLog]_block_invoke_2.49
- ___58-[PLIOHIDOperatorComposition initWithOperator:forService:]_block_invoke.24
- ___58-[PLIOHIDOperatorComposition initWithOperator:forService:]_block_invoke.33
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.104
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.104.cold.1
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.104.cold.2
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.105
- ___58-[PLSubmissions(XPCScheduling) submitRecord:withActivity:]_block_invoke.106
- ___59-[PLStorageCache flushStagingAggregateEntryCacheToDatabase]_block_invoke.239
- ___61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.871
- ___61-[PLStorageCache updateStagingEntryCacheWithEntry:withBlock:]_block_invoke.155
- ___61-[PLStorageCache updateStagingEntryCacheWithEntry:withBlock:]_block_invoke.158
- ___62-[PLCoreStorage(XPCScheduling) registerDailyTasks_XPCActivity]_block_invoke.35
- ___62-[PLCoreStorage(XPCScheduling) registerDailyTasks_XPCActivity]_block_invoke.37
- ___63-[PLArchiveManager registerForArchivingNotificationUsingBlock:]_block_invoke.441
- ___63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.773
- ___64-[PLSubmissions(XPCScheduling) registerUploadSchedulingActivity]_block_invoke.11
- ___66-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:]_block_invoke.96
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.32
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.32.cold.1
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.33
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.33.cold.1
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.34
- ___66-[SignpostReaderHelper processSignpostWithConfig:withServiceType:]_block_invoke.34.cold.1
- ___68-[PLIOKitOperatorComposition initWithOperator:forService:withBlock:]_block_invoke.31
- ___68-[PLSQLiteConnection trimAllTablesFromDate:toDate:withTableFilters:]_block_invoke.278
- ___68-[PLSQLiteConnection trimAllTablesFromDate:toDate:withTableFilters:]_block_invoke.298
- ___73-[PLTimeReferenceDynamic unregisterForTimeChangedCallbackWithIdentifier:]_block_invoke.79
- ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.124
- ___74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.534
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.70
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.70.cold.1
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.70.cold.2
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.70.cold.3
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.74
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.74.cold.1
- ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.721
- ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.727
- ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.51
- ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.57
- ___77-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:]_block_invoke.63
- ___82-[PLTimeReferenceDynamic registerForTimeChangedCallbackWithIdentifier:usingBlock:]_block_invoke.73
- ___87-[PLSubmissionFile logSubmissionResultToCAWithErrorType:withFileType:withOverrideKeys:]_block_invoke.80
- ___89-[PLOperator postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:]_block_invoke.128
- ___93-[PLEnhancedTaskingAgent logAggregatedDataFromSignpostWithPayload:withStartDate:withEndDate:]_block_invoke.116
- ___Block_byref_object_copy_.156
- ___Block_byref_object_copy_.707
- ___Block_byref_object_dispose_.157
- ___Block_byref_object_dispose_.708
- ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"816^B24ls32l8s40l8s48l8
- ___block_literal_global.110
- ___block_literal_global.129
- ___block_literal_global.162
- ___block_literal_global.169
- ___block_literal_global.18
- ___block_literal_global.180
- ___block_literal_global.19
- ___block_literal_global.196
- ___block_literal_global.198
- ___block_literal_global.205
- ___block_literal_global.208
- ___block_literal_global.21
- ___block_literal_global.211
- ___block_literal_global.215
- ___block_literal_global.216
- ___block_literal_global.22
- ___block_literal_global.220
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.23
- ___block_literal_global.230
- ___block_literal_global.234
- ___block_literal_global.235
- ___block_literal_global.24
- ___block_literal_global.240
- ___block_literal_global.245
- ___block_literal_global.252
- ___block_literal_global.255
- ___block_literal_global.259
- ___block_literal_global.265
- ___block_literal_global.269
- ___block_literal_global.27
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.282
- ___block_literal_global.286
- ___block_literal_global.288
- ___block_literal_global.294
- ___block_literal_global.302
- ___block_literal_global.311
- ___block_literal_global.313
- ___block_literal_global.318
- ___block_literal_global.323
- ___block_literal_global.332
- ___block_literal_global.335
- ___block_literal_global.344
- ___block_literal_global.349
- ___block_literal_global.352
- ___block_literal_global.355
- ___block_literal_global.361
- ___block_literal_global.363
- ___block_literal_global.368
- ___block_literal_global.373
- ___block_literal_global.375
- ___block_literal_global.381
- ___block_literal_global.382
- ___block_literal_global.384
- ___block_literal_global.387
- ___block_literal_global.390
- ___block_literal_global.391
- ___block_literal_global.393
- ___block_literal_global.398
- ___block_literal_global.403
- ___block_literal_global.412
- ___block_literal_global.48
- ___block_literal_global.554
- ___block_literal_global.613
- ___block_literal_global.615
- ___block_literal_global.626
- ___block_literal_global.631
- ___block_literal_global.635
- ___block_literal_global.638
- ___block_literal_global.64
- ___block_literal_global.641
- ___block_literal_global.644
- ___block_literal_global.7
- ___block_literal_global.76
- ___block_literal_global.77
- ___block_literal_global.78
- ___block_literal_global.8
- ___block_literal_global.805
- ___block_literal_global.828
- ___block_literal_global.848
- ___block_literal_global.86
- ___block_literal_global.91
- ___block_literal_global.92
- ___block_literal_global.95
- ___kQueueEvent_block_invoke.101
- __cancel.classDebugEnabled.38
- __cancel.classDebugEnabled.44
- __cancel.defaultOnce.37
- __cancel.defaultOnce.43
- __unnamed_array_storage.105
- __unnamed_array_storage.112
- __unnamed_array_storage.133
- __unnamed_array_storage.140
- __unnamed_array_storage.141
- __unnamed_array_storage.147
- __unnamed_array_storage.148
- __unnamed_array_storage.151
- __unnamed_array_storage.153
- __unnamed_array_storage.154
- __unnamed_array_storage.169
- __unnamed_array_storage.177
- __unnamed_array_storage.186
- __unnamed_array_storage.189
- __unnamed_array_storage.190
- __unnamed_array_storage.191
- __unnamed_array_storage.196
- __unnamed_array_storage.199
- __unnamed_array_storage.202
- __unnamed_array_storage.203
- __unnamed_array_storage.212
- __unnamed_array_storage.222
- __unnamed_array_storage.229
- __unnamed_array_storage.230
- __unnamed_array_storage.234
- __unnamed_array_storage.235
- __unnamed_array_storage.239
- __unnamed_array_storage.240
- __unnamed_array_storage.242
- __unnamed_array_storage.243
- __unnamed_array_storage.25
- __unnamed_array_storage.257
- __unnamed_array_storage.258
- __unnamed_array_storage.26
- __unnamed_array_storage.264
- __unnamed_array_storage.283
- __unnamed_array_storage.293
- __unnamed_array_storage.297
- __unnamed_array_storage.298
- __unnamed_array_storage.299
- __unnamed_array_storage.307
- __unnamed_array_storage.318
- __unnamed_array_storage.328
- __unnamed_array_storage.331
- __unnamed_array_storage.332
- __unnamed_array_storage.333
- __unnamed_array_storage.337
- __unnamed_array_storage.340
- __unnamed_array_storage.342
- __unnamed_array_storage.351
- __unnamed_array_storage.352
- __unnamed_array_storage.353
- __unnamed_array_storage.358
- __unnamed_array_storage.362
- __unnamed_array_storage.368
- __unnamed_array_storage.369
- __unnamed_array_storage.384
- __unnamed_array_storage.385
- __unnamed_array_storage.393
- __unnamed_array_storage.394
- __unnamed_array_storage.40
- __unnamed_array_storage.44
- __unnamed_array_storage.471
- __unnamed_array_storage.49
- __unnamed_array_storage.51
- __unnamed_array_storage.545
- __unnamed_array_storage.546
- __unnamed_array_storage.566
- __unnamed_array_storage.567
- __unnamed_array_storage.571
- __unnamed_array_storage.577
- __unnamed_array_storage.578
- __unnamed_array_storage.584
- __unnamed_array_storage.585
- __unnamed_array_storage.589
- __unnamed_array_storage.593
- __unnamed_array_storage.597
- __unnamed_array_storage.60
- __unnamed_array_storage.612
- __unnamed_array_storage.613
- __unnamed_array_storage.617
- __unnamed_array_storage.79
- __unnamed_array_storage.816
- __unnamed_array_storage.817
- __unnamed_array_storage.82
- __unnamed_array_storage.83
- __unnamed_array_storage.850
- __unnamed_array_storage.851
- __unnamed_array_storage.855
- __unnamed_array_storage.879
- __unnamed_array_storage.880
- __unnamed_array_storage.89
- __unnamed_array_storage.9
- __unnamed_array_storage.90
- __unnamed_array_storage.93
- __unnamed_array_storage.94
- _blockingFlushCachesWithReason:.classDebugEnabled.668
- _blockingFlushCachesWithReason:.defaultOnce.667
- _blockingFlushQueues:.classDebugEnabled.677
- _blockingFlushQueues:.classDebugEnabled.687
- _blockingFlushQueues:.defaultOnce.676
- _blockingFlushQueues:.defaultOnce.686
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.50
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.56
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.classDebugEnabled.62
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.49
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.55
- _bucketTimeStampForDate:withTimeReference:withBucketInterval:.defaultOnce.61
- _checkTaskingCompletionStatus.classDebugEnabled.285
- _checkTaskingCompletionStatus.classDebugEnabled.303
- _checkTaskingCompletionStatus.defaultOnce.284
- _checkTaskingCompletionStatus.defaultOnce.302
- _clearLastEntryCacheForEntryKey:.classDebugEnabled.45
- _clearLastEntryCacheForEntryKey:.defaultOnce.44
- _clearTaskingDefaults.classDebugEnabled.271
- _clearTaskingDefaults.classDebugEnabled.277
- _clearTaskingDefaults.classDebugEnabled.283
- _clearTaskingDefaults.defaultOnce.270
- _clearTaskingDefaults.defaultOnce.276
- _clearTaskingDefaults.defaultOnce.282
- _createTableName:withColumns:.classDebugEnabled.462
- _createTableName:withColumns:.defaultOnce.461
- _currentTime.classDebugEnabled.18
- _currentTime.classDebugEnabled.33
- _currentTime.defaultOnce.17
- _currentTime.defaultOnce.32
- _decodeIPPacket:encryptedPath:.classDebugEnabled.184
- _decodeIPPacket:encryptedPath:.classDebugEnabled.193
- _decodeIPPacket:encryptedPath:.classDebugEnabled.202
- _decodeIPPacket:encryptedPath:.classDebugEnabled.208
- _decodeIPPacket:encryptedPath:.classDebugEnabled.226
- _decodeIPPacket:encryptedPath:.classDebugEnabled.232
- _decodeIPPacket:encryptedPath:.classDebugEnabled.238
- _decodeIPPacket:encryptedPath:.classDebugEnabled.247
- _decodeIPPacket:encryptedPath:.defaultOnce.183
- _decodeIPPacket:encryptedPath:.defaultOnce.192
- _decodeIPPacket:encryptedPath:.defaultOnce.201
- _decodeIPPacket:encryptedPath:.defaultOnce.207
- _decodeIPPacket:encryptedPath:.defaultOnce.225
- _decodeIPPacket:encryptedPath:.defaultOnce.231
- _decodeIPPacket:encryptedPath:.defaultOnce.237
- _decodeIPPacket:encryptedPath:.defaultOnce.246
- _decorateFileAtPath:.classDebugEnabled.102
- _decorateFileAtPath:.classDebugEnabled.113
- _decorateFileAtPath:.classDebugEnabled.117
- _decorateFileAtPath:.classDebugEnabled.121
- _decorateFileAtPath:.classDebugEnabled.125
- _decorateFileAtPath:.classDebugEnabled.98
- _decorateFileAtPath:.defaultOnce.101
- _decorateFileAtPath:.defaultOnce.112
- _decorateFileAtPath:.defaultOnce.116
- _decorateFileAtPath:.defaultOnce.120
- _decorateFileAtPath:.defaultOnce.124
- _decorateFileAtPath:.defaultOnce.97
- _deviceBootUUID.classDebugEnabled.104
- _deviceBootUUID.defaultOnce.103
- _didEnableActivity:.classDebugEnabled.21
- _didEnableActivity:.classDebugEnabled.34
- _didEnableActivity:.defaultOnce.20
- _didEnableActivity:.defaultOnce.33
- _entriesForKey:withProperties:.classDebugEnabled.738
- _entriesForKey:withProperties:.defaultOnce.737
- _entryIDForNewEntry:.classDebugEnabled.105
- _entryIDForNewEntry:.classDebugEnabled.90
- _entryIDForNewEntry:.defaultOnce.104
- _entryIDForNewEntry:.defaultOnce.89
- _flushCachesWithReason:.classDebugEnabled.641
- _flushCachesWithReason:.defaultOnce.640
- _flushStagingAggregateEntryCacheToDatabase.classDebugEnabled.238
- _flushStagingAggregateEntryCacheToDatabase.defaultOnce.237
- _flushStagingEntryCacheToDatabase.classDebugEnabled.229
- _flushStagingEntryCacheToDatabase.defaultOnce.167
- _flushStagingEntryCacheToDatabase.defaultOnce.228
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.123
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.122
- _getHourBucketOffset.classDebugEnabled.19
- _getHourBucketOffset.defaultOnce.18
- _getNetworkWakeInfo:.classDebugEnabled.119
- _getNetworkWakeInfo:.defaultOnce.118
- _getNormalizedIPV6Address:.classDebugEnabled.175
- _getNormalizedIPV6Address:.defaultOnce.174
- _getUnattributedWakeInfo:.classDebugEnabled.128
- _getUnattributedWakeInfo:.defaultOnce.127
- _handleIPSecEvent:.classDebugEnabled.146
- _handleIPSecEvent:.classDebugEnabled.152
- _handleIPSecEvent:.defaultOnce.145
- _handleIPSecEvent:.defaultOnce.151
- _handlePeer:forEvent:.classDebugEnabled.104
- _handlePeer:forEvent:.classDebugEnabled.110
- _handlePeer:forEvent:.classDebugEnabled.116
- _handlePeer:forEvent:.classDebugEnabled.122
- _handlePeer:forEvent:.classDebugEnabled.128
- _handlePeer:forEvent:.classDebugEnabled.137
- _handlePeer:forEvent:.classDebugEnabled.143
- _handlePeer:forEvent:.classDebugEnabled.53
- _handlePeer:forEvent:.classDebugEnabled.59
- _handlePeer:forEvent:.classDebugEnabled.65
- _handlePeer:forEvent:.classDebugEnabled.71
- _handlePeer:forEvent:.classDebugEnabled.83
- _handlePeer:forEvent:.classDebugEnabled.89
- _handlePeer:forEvent:.classDebugEnabled.98
- _handlePeer:forEvent:.defaultOnce.103
- _handlePeer:forEvent:.defaultOnce.109
- _handlePeer:forEvent:.defaultOnce.115
- _handlePeer:forEvent:.defaultOnce.121
- _handlePeer:forEvent:.defaultOnce.127
- _handlePeer:forEvent:.defaultOnce.136
- _handlePeer:forEvent:.defaultOnce.142
- _handlePeer:forEvent:.defaultOnce.52
- _handlePeer:forEvent:.defaultOnce.58
- _handlePeer:forEvent:.defaultOnce.64
- _handlePeer:forEvent:.defaultOnce.70
- _handlePeer:forEvent:.defaultOnce.82
- _handlePeer:forEvent:.defaultOnce.88
- _handlePeer:forEvent:.defaultOnce.97
- _handlePowerWakeEvent:.classDebugEnabled.137
- _handlePowerWakeEvent:.defaultOnce.136
- _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.533
- _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.532
- _init.classDebugEnabled.29
- _init.defaultOnce.28
- _initWithOperator:forService:.classDebugEnabled.32
- _initWithOperator:forService:.defaultOnce.31
- _initWithOperator:forService:withBlock:.classDebugEnabled.30
- _initWithOperator:forService:withBlock:.defaultOnce.29
- _insertIntoStagingEntryCache:.defaultOnce.148
- _isESPPacket:offset:.classDebugEnabled.292
- _isESPPacket:offset:.classDebugEnabled.298
- _isESPPacket:offset:.defaultOnce.291
- _isESPPacket:offset:.defaultOnce.297
- _kPLTaskingEndNotification_block_invoke_5.classDebugEnabled.736
- _kPLTaskingEndNotification_block_invoke_5.classDebugEnabled.743
- _kPLTaskingEndNotification_block_invoke_5.classDebugEnabled.749
- _kPLTaskingEndNotification_block_invoke_5.defaultOnce.735
- _kPLTaskingEndNotification_block_invoke_5.defaultOnce.742
- _kPLTaskingEndNotification_block_invoke_5.defaultOnce.748
- _lastEntryCachePruneToDate:.classDebugEnabled.54
- _lastEntryCachePruneToDate:.defaultOnce.53
- _lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.870
- _lastEntryForKey:withComparisons:isSingleton:.defaultOnce.869
- _logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.920
- _logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.921
- _migrateArchive:.classDebugEnabled.392
- _migrateArchive:.defaultOnce.391
- _objc_msgSend$allKeysForEntryKey:
- _objc_msgSend$md5Hash:
- _postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:.classDebugEnabled.127
- _postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:.defaultOnce.126
- _registerDailyTasks.classDebugEnabled.402
- _registerDailyTasks.defaultOnce.401
- _registerEPLNotificationWithQueue:.classDebugEnabled.100
- _registerEPLNotificationWithQueue:.defaultOnce.99
- _registerForArchivingNotificationUsingBlock:.classDebugEnabled
- _registerForArchivingNotificationUsingBlock:.defaultOnce
- _registerForTimeChangedCallbackWithIdentifier:usingBlock:.classDebugEnabled.72
- _registerForTimeChangedCallbackWithIdentifier:usingBlock:.defaultOnce.71
- _relayConnection.classDebugEnabled.175
- _relayConnection.classDebugEnabled.181
- _relayConnection.defaultOnce.174
- _relayConnection.defaultOnce.180
- _relayConnectionSync_block_invoke.classDebugEnabled.32
- _relayConnectionSync_block_invoke.defaultOnce.31
- _relayConnectionSync_block_invoke_3.classDebugEnabled.156
- _relayConnectionSync_block_invoke_3.classDebugEnabled.163
- _relayConnectionSync_block_invoke_3.classDebugEnabled.169
- _relayConnectionSync_block_invoke_3.defaultOnce.155
- _relayConnectionSync_block_invoke_3.defaultOnce.162
- _relayConnectionSync_block_invoke_3.defaultOnce.168
- _removeEmptyOldTables.classDebugEnabled.367
- _removeEmptyOldTables.defaultOnce.366
- _reschedule.classDebugEnabled.85
- _reschedule.classDebugEnabled.91
- _reschedule.defaultOnce.84
- _reschedule.defaultOnce.90
- _runTrimQuery:.classDebugEnabled.313
- _runTrimQuery:.classDebugEnabled.319
- _runTrimQuery:.defaultOnce.312
- _runTrimQuery:.defaultOnce.318
- _schedule.classDebugEnabled.26
- _schedule.classDebugEnabled.33
- _schedule.defaultOnce.25
- _schedule.defaultOnce.32
- _setEnabled:.classDebugEnabled.12
- _setEnabled:.classDebugEnabled.20
- _setEnabled:.classDebugEnabled.27
- _setEnabled:.defaultOnce.11
- _setEnabled:.defaultOnce.19
- _setEnabled:.defaultOnce.26
- _shouldStartTaskingToday.classDebugEnabled.296
- _shouldStartTaskingToday.classDebugEnabled.302
- _shouldStartTaskingToday.classDebugEnabled.323
- _shouldStartTaskingToday.classDebugEnabled.329
- _shouldStartTaskingToday.classDebugEnabled.338
- _shouldStartTaskingToday.classDebugEnabled.360
- _shouldStartTaskingToday.classDebugEnabled.366
- _shouldStartTaskingToday.classDebugEnabled.372
- _shouldStartTaskingToday.defaultOnce.295
- _shouldStartTaskingToday.defaultOnce.301
- _shouldStartTaskingToday.defaultOnce.322
- _shouldStartTaskingToday.defaultOnce.328
- _shouldStartTaskingToday.defaultOnce.337
- _shouldStartTaskingToday.defaultOnce.359
- _shouldStartTaskingToday.defaultOnce.365
- _shouldStartTaskingToday.defaultOnce.371
- _signalDoneByObject:.classDebugEnabled.22
- _signalDoneByObject:.classDebugEnabled.28
- _signalDoneByObject:.defaultOnce.21
- _signalDoneByObject:.defaultOnce.27
- _submitLogToiCloud:WithCompress:.classDebugEnabled.167
- _submitLogToiCloud:WithCompress:.defaultOnce.166
- _submitReasonForToday.classDebugEnabled.76
- _submitReasonForToday.classDebugEnabled.82
- _submitReasonForToday.classDebugEnabled.88
- _submitReasonForToday.defaultOnce.75
- _submitReasonForToday.defaultOnce.81
- _submitReasonForToday.defaultOnce.87
- _subscribeNotificationsForEntries.classDebugEnabled.147
- _subscribeNotificationsForEntries.defaultOnce.146
- _systemTimeChangedByOffset:.classDebugEnabled
- _systemTimeChangedByOffset:.classDebugEnabled.429
- _systemTimeChangedByOffset:.defaultOnce
- _systemTimeChangedByOffset:.defaultOnce.428
- _taskingModeSafeguard.classDebugEnabled.341
- _taskingModeSafeguard.defaultOnce.340
- _timerFiredForMonotonicFireDate:.classDebugEnabled.50
- _timerFiredForMonotonicFireDate:.classDebugEnabled.56
- _timerFiredForMonotonicFireDate:.classDebugEnabled.73
- _timerFiredForMonotonicFireDate:.classDebugEnabled.79
- _timerFiredForMonotonicFireDate:.defaultOnce.49
- _timerFiredForMonotonicFireDate:.defaultOnce.55
- _timerFiredForMonotonicFireDate:.defaultOnce.72
- _timerFiredForMonotonicFireDate:.defaultOnce.78
- _trimAllTablesFromDate:toDate:withTableFilters:.classDebugEnabled.277
- _trimAllTablesFromDate:toDate:withTableFilters:.classDebugEnabled.297
- _trimAllTablesFromDate:toDate:withTableFilters:.defaultOnce.276
- _trimAllTablesFromDate:toDate:withTableFilters:.defaultOnce.296
- _unregisterForTimeChangedCallbackWithIdentifier:.classDebugEnabled.78
- _unregisterForTimeChangedCallbackWithIdentifier:.defaultOnce.77
- _updateEntry:.classDebugEnabled.648
- _updateEntry:.classDebugEnabled.654
- _updateEntry:.classDebugEnabled.660
- _updateEntry:.defaultOnce.647
- _updateEntry:.defaultOnce.653
- _updateEntry:.defaultOnce.659
- _updateStagingEntryCacheWithEntry:withBlock:.classDebugEnabled.154
- _updateStagingEntryCacheWithEntry:withBlock:.defaultOnce.153
- _waitWithBlockSync:.classDebugEnabled.41
- _waitWithBlockSync:.defaultOnce.40
- _writeDynamicEntries:.classDebugEnabled.606
- _writeDynamicEntries:.defaultOnce.605
- _writeEntry:.classDebugEnabled.560
- _writeEntry:.defaultOnce.559
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.720
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.726
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.719
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.725
CStrings:
+ "\x16"
+ " VALUES "
+ "%@KernelTimePowerlog_%f%@"
+ "(?, %@"
+ "(timeInterval = %f AND timestamp < %f) OR (timeInterval = %f AND Energy < %f AND timestamp < %f) OR (timeInterval = %f AND timestamp < %f)"
+ "-"
+ "-[PLSQLiteConnection writeDynamicEntriesToPPS:]"
+ ".XCSQL"
+ ".xc.anon"
+ "@\"PLEntry\"24@?0@\"NSString\"8@\"NSString\"16"
+ "AP_F1"
+ "AP_F2"
+ "AP_F3"
+ "AP_F4"
+ "AP_F5"
+ "AP_F6"
+ "AP_VMAX"
+ "AP_VMIN"
+ "AP_VNOM"
+ "AP_VOVD"
+ "Adding to %@ entries array %@"
+ "AlbumAnimationDuration"
+ "AlbumMotionDownload"
+ "AppDeletion : updateQueries for AppDistributorID is %@"
+ "AppDistributorID"
+ "Audio"
+ "AutomatedDeviceGroupRawValue"
+ "B40@0:8@16@24Q32"
+ "BOOST_F1"
+ "BOOST_F2"
+ "BOOST_F3"
+ "BOOST_F4"
+ "BOOST_F5"
+ "BOOST_F6"
+ "BOOST_VMAX"
+ "BOOST_VMIN"
+ "BOOST_VNOM"
+ "BOOST_VOVD"
+ "BWR_F1"
+ "BWR_F2"
+ "BWR_F3"
+ "BWR_F4"
+ "BWR_F5"
+ "BWR_F6"
+ "BWR_VMAX"
+ "BWR_VMIN"
+ "BWR_VNOM"
+ "BWR_VOVD"
+ "CLPC_F1"
+ "CLPC_F2"
+ "CLPC_F3"
+ "CLPC_F4"
+ "CLPC_F5"
+ "CLPC_F6"
+ "CLPC_VMAX"
+ "CLPC_VMIN"
+ "CLPC_VNOM"
+ "CLPC_VOVD"
+ "CPUCoreConfig"
+ "Computed randomized offset '%f' with randomization interval ['%f', '%f']"
+ "DCS_F6_ACT"
+ "DMA data '%@' has dynamic keys"
+ "DMACompliantKeys"
+ "DMAKeys"
+ "DMAKeysForEntryDefinition:"
+ "DataStream"
+ "DataUUID"
+ "Domain"
+ "DynamicArray=%@ and count %lu"
+ "DynamicEntry %@"
+ "Failed to connect to copied XCSQL for timestamp obfuscation"
+ "Failed to copy xcsql file to %@"
+ "Failed to create a XC log tarball"
+ "Failed to mark files in directory %@ purgeable -- error when retrieving contents of directory: '%@'"
+ "Failed to mark files in directory %@ purgeable -- path is not directory"
+ "Failed to move XC log tarball"
+ "Failed to translate process name '%@' to bundle ID for DMA!"
+ "FeatureName"
+ "Finished preparing XC"
+ "GFX_F1"
+ "GFX_F2"
+ "GFX_F3"
+ "GFX_F4"
+ "GFX_F5"
+ "GFX_F6"
+ "GFX_VMAX"
+ "GFX_VMIN"
+ "GFX_VNOM"
+ "GFX_VOVD"
+ "INSERT INTO \"%@\" ('FK_ID',"
+ "INSERT INTO \"%@_Array_%@\" (\"FK_ID\", \"%@\") VALUES "
+ "InstallType"
+ "LastUpgradeSystemTimestamp"
+ "MISC_F1"
+ "MISC_F2"
+ "MISC_F3"
+ "MISC_F4"
+ "MISC_F5"
+ "MISC_F6"
+ "MISC_VMAX"
+ "MISC_VMIN"
+ "MISC_VNOM"
+ "MISC_VOVD"
+ "Metadata"
+ "Metric name: %@ is not String class %@"
+ "MonitorCategory"
+ "MonitorSubsystem"
+ "PDEP_channelValueDiff"
+ "PDEP_cycleCount"
+ "PDEP_variant"
+ "PDLP_channelValueDiff"
+ "PDLP_cycleCount"
+ "PDLP_variant"
+ "PDPowermW"
+ "PLBatteryAgent_EventForward_AdapterDetails"
+ "PLConfigAgent_EventForward_FeatureFlags"
+ "PLIOReportAgent_EventBackward_PMPPMCDCSFloor"
+ "PLIOReportAgent_EventBackward_PMPPMCSOCFloor"
+ "PLSubmissionCleanup"
+ "PLSubmissionFileXC"
+ "PMP_F1"
+ "PMP_F2"
+ "PMP_F3"
+ "PMP_F4"
+ "PMP_F5"
+ "PMP_F6"
+ "PMP_VMAX"
+ "PMP_VMIN"
+ "PMP_VNOM"
+ "PMP_VOVD"
+ "POWER_DOMAIN_CHANNEL_ID_52"
+ "POWER_DOMAIN_CHANNEL_ID_53"
+ "POWER_DOMAIN_CHANNEL_ID_57"
+ "POWER_DOMAIN_CHANNEL_ID_59"
+ "POWER_DOMAIN_CHANNEL_ID_60"
+ "POWER_DOMAIN_CHANNEL_ID_61"
+ "POWER_DOMAIN_CHANNEL_ID_62"
+ "PP3b_channelValue"
+ "PP3b_channelValueDiff"
+ "PP3b_cycleCount"
+ "PP3b_variant"
+ "PP4b_channelValue"
+ "PP4b_channelValueDiff"
+ "PP4b_cycleCount"
+ "PP4b_variant"
+ "PP5b_channelValue"
+ "PP5b_channelValueDiff"
+ "PP5b_cycleCount"
+ "PP5b_variant"
+ "PP6b_channelValue"
+ "PP6b_channelValueDiff"
+ "PP6b_cycleCount"
+ "PP6b_variant"
+ "PP7b_channelValue"
+ "PP7b_channelValueDiff"
+ "PP7b_cycleCount"
+ "PP7b_variant"
+ "PP8b_channelValue"
+ "PP8b_channelValueDiff"
+ "PP8b_cycleCount"
+ "PP8b_variant"
+ "PP9b_channelValue"
+ "PP9b_channelValueDiff"
+ "PP9b_cycleCount"
+ "PP9b_variant"
+ "PPSFeatureFlagReaderHelper"
+ "PPSFeatureFlagReaderHelper Connection was interrupted."
+ "PPSFeatureFlagReaderHelper Invalid connection handler is happening."
+ "PPSFeatureFlagReaderHelper Spinning up xpc svc"
+ "PPSFeatureFlagReaderHelper establishing a connection"
+ "PPSFeatureFlagReaderHelper getFeatureFlags Connection Closed"
+ "PPSFeatureFlagReaderHelper getFeatureFlags called"
+ "PPSFeatureFlagReaderHelper getFeatureFlags result: %@"
+ "PPSFeatureFlagReaderProtocol"
+ "PPTStorageOperator_TimeOffset_30_1"
+ "PPab_channelValue"
+ "PPab_channelValueDiff"
+ "PPab_cycleCount"
+ "PPab_variant"
+ "PPdb_channelValue"
+ "PPdb_channelValueDiff"
+ "PPdb_cycleCount"
+ "PPdb_variant"
+ "PZC1"
+ "PerfPowerServicesDataStream"
+ "Performing timestamp obfuscation for %@ with base timestamp '%f'"
+ "Platform"
+ "PortControllerBootFlags"
+ "PowerState"
+ "PrintingTime"
+ "Processing DMA data: '%@'"
+ "RMBS_F1"
+ "RMBS_F2"
+ "RMBS_F3"
+ "RMBS_F4"
+ "RMBS_F5"
+ "RMBS_F6"
+ "RMBS_VMAX"
+ "RMBS_VMIN"
+ "RMBS_VNOM"
+ "RMBS_VOVD"
+ "ReadingTime"
+ "Removing XC log tarball: %@, %@"
+ "Requested Xcode DB file: %@"
+ "SELECT name FROM pragma_table_info('%@')"
+ "Sing"
+ "Skipping %@ for marking as purgeable -- file is of type '%@' & doesn't not match given extension filter."
+ "Skipping conditional tasking..."
+ "Starting conditional tasking..."
+ "Starting monitoring for subsystem: %@ category: %@"
+ "Starting submission for %@, mask = %llu"
+ "Stopping monitoring"
+ "Submitting '%@:%@' record for %@ via DiagnosticPipeline"
+ "T@\"NSString\",&,V_monitoredCategory"
+ "T@\"NSString\",&,V_monitoredSubsystem"
+ "T@\"NSString\",?,R,C"
+ "T@\"PLCFNotificationOperatorComposition\",&,V_startMonitor"
+ "T@\"PLCFNotificationOperatorComposition\",&,V_stopMonitor"
+ "TB,V_monitor"
+ "Target"
+ "Td,V_XCSQLDBDuration"
+ "Time for getting PPSFeatureFlagReaderHelper getFeatureFlags reading to run: %f, %@, %@"
+ "UPDATE %@ SET timestamp = timestamp - %f;"
+ "UPDATE '%@' SET %@ ='%@' WHERE %@ = '%@' AND AppDeletedDate != 0;"
+ "USBSleepPoolPowermW"
+ "USBWakePoolPowermW"
+ "UpdateTable alter query %@"
+ "UpdateTable insert query %@"
+ "UserAction"
+ "VP3b_channelValue"
+ "VP3b_channelValueDiff"
+ "VP3b_cycleCount"
+ "VP3b_variant"
+ "VP4b_channelValue"
+ "VP4b_channelValueDiff"
+ "VP4b_cycleCount"
+ "VP4b_variant"
+ "VP5b_channelValue"
+ "VP5b_channelValueDiff"
+ "VP5b_cycleCount"
+ "VP5b_variant"
+ "VP6b_channelValue"
+ "VP6b_channelValueDiff"
+ "VP6b_cycleCount"
+ "VP6b_variant"
+ "VP7b_channelValue"
+ "VP7b_channelValueDiff"
+ "VP7b_cycleCount"
+ "VP7b_variant"
+ "VP8b_channelValue"
+ "VP8b_channelValueDiff"
+ "VP8b_cycleCount"
+ "VP8b_variant"
+ "VP9b_channelValue"
+ "VP9b_channelValueDiff"
+ "VP9b_cycleCount"
+ "VP9b_variant"
+ "VPab_channelValue"
+ "VPab_channelValueDiff"
+ "VPab_cycleCount"
+ "VPab_variant"
+ "VPdb_channelValue"
+ "VPdb_channelValueDiff"
+ "VPdb_cycleCount"
+ "VPdb_variant"
+ "XC"
+ "XCSQLConnection"
+ "XCSQLDBDuration"
+ "XcodeMetrics"
+ "XcodeMetrics_TimeOffset_365_4"
+ "XcodeMetrics_UserAction_365_4"
+ "XcodeOrganizer"
+ "XcodeVersion"
+ "_Array"
+ "_XCSQLDBDuration"
+ "__PPSArray__"
+ "__PPSDynamic__"
+ "__PPSKVPairs__"
+ "_monitor"
+ "_monitoredCategory"
+ "_monitoredSubsystem"
+ "_startMonitor"
+ "_stopMonitor"
+ "absoluteString"
+ "addAuxiliaryType:withEntryKey:"
+ "allArrayKeysForEntryKey:"
+ "allBaseKeysForEntryKey:"
+ "allocWithZone:"
+ "anyMetricsForEntryKey:"
+ "app_distributorid"
+ "archiving"
+ "arrayKeyConfigsForEntryKey:"
+ "arrayMetricsForEntryKey:"
+ "auxiliaryType"
+ "baseMetricsForEntryKey:"
+ "bundleIDFromProcessName:"
+ "ce-archive"
+ "com.apple.PPSFeatureFlagReader"
+ "com.apple.perfpowerservices.dma.%@"
+ "com.apple.power.error.kernelTimeDB"
+ "com.apple.powerlog.dataStreamStartMonitor"
+ "com.apple.powerlog.dataStreamStopMonitor"
+ "commonTypeDict_IntegerFormat_withUnit_mJ"
+ "conditionCheckForXcodeUserActions"
+ "dataFormatForMetric:auxiliaryMetrics:"
+ "deprecateTablesXCSQL"
+ "dictionaryWithValuesForKeys:"
+ "dynamicMetricsForEntryKey:"
+ "dynamicTableNameForEntryKey:"
+ "ftBR"
+ "getFeatureFlags"
+ "getFeatureFlags:"
+ "getXCSQLFile"
+ "hasArrayKeys:"
+ "hasDMAKeys"
+ "hasDMAKeysForEntryDefinition:"
+ "hasDMAKeysForEntryKey:"
+ "hasDynamicKeys:"
+ "initWithSuiteName:"
+ "isPPSEnabled"
+ "isWireless"
+ "kPLExitReasonDescKernelTime"
+ "kernelTimeDB"
+ "logDMAEntry:"
+ "luxEntryNotificationWithOperator:withBlock:"
+ "markFilesAsPurgeable:withUrgency:"
+ "markFilesInDirectoryAsPurgeable:ofType:withUrgency:"
+ "mlPB"
+ "monitor"
+ "monitorMetricsForSubsystem:category:payload:"
+ "monitoredCategory"
+ "monitoredSubsystem"
+ "monotonicTimeWentBackwards=%d"
+ "numCoreTypes"
+ "numEcpuCores"
+ "numPcpuCores"
+ "obfuscateTimestampsForTable:connection:withOffset:"
+ "os_log_debug Connection error happened %@"
+ "quarantineWithExitReason:"
+ "randomizedBaseOffset"
+ "resetMetricsForEntryKey:"
+ "sanitizeCAPayload:"
+ "setMonitor:"
+ "setMonitoredCategory:"
+ "setMonitoredSubsystem:"
+ "setStartMonitor:"
+ "setStopMonitor:"
+ "setSubmittedFilesMask:"
+ "setValuesForKeysWithDictionary:"
+ "setXCSQLDBDuration:"
+ "setupArrayTableForEntryKey:withName:withConnection:"
+ "setupDynamicTableForEntryKey:withName:withConnection:"
+ "sortedSqlFormatedColumnNamesForTableInsert:"
+ "splitBySubmissionType"
+ "startMonitor"
+ "stopMonitor"
+ "stringForKey:"
+ "submissionCategory"
+ "submissionMaskToString"
+ "submitXC"
+ "tasking config bools: %@, %@, %@, %@, %@, %@, %@"
+ "time_printing"
+ "time_processing"
+ "time_reading"
+ "trimConditionsForXCSQLWithTrimDate:"
+ "trimXcodeOrganizerLog"
+ "v16@?0@\"NSArray\"8"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "writeDynamicEntriesToPPS:"
+ "xc-archive"
+ "xcode_%@.XCSQL"
+ "xcode_db"
+ "\x92"
- "%@%0.2f"
- "+[PLArchiveManager systemTimeChangedByOffset:]"
- "-[PLArchiveManager migrate]_block_invoke"
- "-[PLArchiveManager recover]_block_invoke"
- "-[PLArchiveManager recover]_block_invoke_2"
- "-[PLArchiveManager registerForArchivingNotificationUsingBlock:]"
- "-[PLTimeReferenceKernel currentTime]"
- "/Library/Caches/com.apple.xbs/Sources/PerfPowerServices/Storage/PLTimeReferenceClasses/PLTimeReferenceKernel.m"
- "AllocatedSize"
- "CPU_DutyCycle"
- "CPU_Energy"
- "DirtySize"
- "ECPUDTL00"
- "ECPUDTL01"
- "ECPUDTL02"
- "ECPUDTL03"
- "ECPUDTL04"
- "ECPUDTL05"
- "ECPUDTL10"
- "ECPUDTL11"
- "ECPUDTL12"
- "ECPUDTL13"
- "ECPUDTL14"
- "ECPUDTL15"
- "ECPUDTL20"
- "ECPUDTL21"
- "ECPUDTL22"
- "ECPUDTL23"
- "ECPUDTL24"
- "ECPUDTL25"
- "ECPUDTL30"
- "ECPUDTL31"
- "ECPUDTL32"
- "ECPUDTL33"
- "ECPUDTL34"
- "ECPUDTL35"
- "ECPUDTL36"
- "Event_Duration"
- "Event_Type"
- "INSERT INTO \"%@_Array_%@\" (\"FK_ID\", \"value\") VALUES "
- "PurgeableSize"
- "ResidentSize"
- "SBC trigger occurred"
- "Skipping submission for conditional tasking..."
- "SoC Base Energy"
- "Starting OTA submission for tasking Config %@..."
- "Starting submission for conditional tasking..."
- "Submitting record %@ via DiagnosticPipeline"
- "WiredSize"
- "tasking config bools: %@, %@, %@, %@, %@, %@"
- "versionHashForEntryKey:"
- "\x82"

```
