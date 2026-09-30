## ProactiveSupport

> `/System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport`

```diff

-406.0.0.0.0
-  __TEXT.__text: 0x66c00
-  __TEXT.__auth_stubs: 0x1dd0
-  __TEXT.__objc_methlist: 0x39b0
+408.0.0.0.0
+  __TEXT.__text: 0x67754
+  __TEXT.__auth_stubs: 0x1df0
+  __TEXT.__objc_methlist: 0x3ce4
+  __TEXT.__const: 0xc4b
+  __TEXT.__objc_databytes: 0x1
   __TEXT.__swift5_typeref: 0x225
   __TEXT.__swift5_capture: 0x9c
-  __TEXT.__const: 0xbcb
-  __TEXT.__cstring: 0x5eef
+  __TEXT.__cstring: 0x60cc
   __TEXT.__constg_swiftt: 0x618
   __TEXT.__swift5_reflstr: 0x58
   __TEXT.__swift5_fieldmd: 0x194
   __TEXT.__swift5_proto: 0xac
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__gcc_except_tab: 0x1a8c
-  __TEXT.__oslogstring: 0x40b9
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0x10
+  __TEXT.__gcc_except_tab: 0x1aec
+  __TEXT.__oslogstring: 0x4130
   __TEXT.__ustring: 0x13c
-  __TEXT.__objc_databytes: 0x1
-  __TEXT.__unwind_info: 0x1968
-  __TEXT.__eh_frame: 0x578
-  __TEXT.__objc_classname: 0x95a
-  __TEXT.__objc_methname: 0x88d0
-  __TEXT.__objc_methtype: 0x1be6
-  __TEXT.__objc_stubs: 0x5dc0
-  __DATA_CONST.__got: 0x600
+  __TEXT.__unwind_info: 0x1980
+  __TEXT.__eh_frame: 0x480
+  __TEXT.__objc_classname: 0x98a
+  __TEXT.__objc_methname: 0x8b71
+  __TEXT.__objc_methtype: 0x1c62
+  __TEXT.__objc_stubs: 0x5fc0
+  __DATA_CONST.__got: 0x610
   __DATA_CONST.__const: 0x560
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2148
+  __DATA_CONST.__objc_selrefs: 0x2258
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x218
+  __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0xf00
-  __AUTH_CONST.__const: 0x23f0
-  __AUTH_CONST.__cfstring: 0x4340
-  __AUTH_CONST.__objc_const: 0x6dc8
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0xf10
+  __AUTH_CONST.__const: 0x2420
+  __AUTH_CONST.__cfstring: 0x4840
+  __AUTH_CONST.__objc_const: 0x6cb0
+  __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x500
+  __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0xf0
   __AUTH.__objc_dataobj: 0x18
-  __DATA.__objc_ivar: 0x3ec
+  __DATA.__objc_ivar: 0x414
   __DATA.__data: 0xa18
   __DATA.__bss: 0x1718
   __DATA_DIRTY.__objc_data: 0x1b30

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AppleSystemInfo.framework/Versions/A/AppleSystemInfo
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
   - /System/Library/PrivateFrameworks/InternationalTextSearch.framework/Versions/A/InternationalTextSearch
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1DFD3E5B-22EA-3359-81E2-405A121A6D0E
-  Functions: 1966
-  Symbols:   4479
-  CStrings:  3339
+  UUID: AF7A20C7-7B0E-3BEA-B2D6-6C84568D6957
+  Functions: 1977
+  Symbols:   4549
+  CStrings:  3460
 
Symbols:
+ -[_PASSQLTelemetryApi .cxx_destruct]
+ -[_PASSQLTelemetryApi applyCallbackWithCompletion:]
+ -[_PASSQLTelemetryApi initWithTelemetryContext:]
+ -[_PASSQLTelemetryApi removeCallback]
+ -[_PASSQLTelemetryApi sendTelemetry]
+ -[_PASSQLTelemetryApi sqlEventLogForTelemetry]
+ -[_PASSQLTelemetryContext .cxx_destruct]
+ -[_PASSQLTelemetryContext applyCallbackWithCompletion:]
+ -[_PASSQLTelemetryContext authorizerStatusBlock]
+ -[_PASSQLTelemetryContext createEventLogForQueryOpCode:argumentOneValue:argumentTwoValue:]
+ -[_PASSQLTelemetryContext currentProcessName]
+ -[_PASSQLTelemetryContext currentTargetName]
+ -[_PASSQLTelemetryContext initWithConnection:sqlQuery:filterPii:]
+ -[_PASSQLTelemetryContext initWithConnectionAndSettings:sqlQuery:filterPii:targetProcess:]
+ -[_PASSQLTelemetryContext isSqlConst]
+ -[_PASSQLTelemetryContext isSqlValidLength]
+ -[_PASSQLTelemetryContext isTargetProcess]
+ -[_PASSQLTelemetryContext removeCallback]
+ -[_PASSQLTelemetryContext resetLog]
+ -[_PASSQLTelemetryContext sendTelemetry:]
+ -[_PASSQLTelemetryContext setAuthorizerStatusBlock:]
+ -[_PASSQLTelemetryContext sqlEventLogForTelemetry]
+ GCC_except_table1402
+ GCC_except_table1403
+ GCC_except_table1406
+ GCC_except_table1411
+ GCC_except_table1414
+ GCC_except_table1418
+ GCC_except_table1450
+ GCC_except_table1456
+ GCC_except_table1464
+ GCC_except_table1571
+ GCC_except_table1572
+ GCC_except_table1598
+ GCC_except_table1600
+ GCC_except_table1619
+ GCC_except_table1622
+ GCC_except_table1626
+ GCC_except_table1634
+ GCC_except_table1645
+ GCC_except_table1653
+ GCC_except_table1665
+ GCC_except_table1683
+ GCC_except_table1684
+ OBJC_IVAR_$__PASSQLTelemetryApi._telemetryContext
+ OBJC_IVAR_$__PASSQLTelemetryContext._authorizerStatusBlock
+ OBJC_IVAR_$__PASSQLTelemetryContext._dbConnection
+ OBJC_IVAR_$__PASSQLTelemetryContext._eventToStringMap
+ OBJC_IVAR_$__PASSQLTelemetryContext._filterPii
+ OBJC_IVAR_$__PASSQLTelemetryContext._shouldSendTelemetry
+ OBJC_IVAR_$__PASSQLTelemetryContext._sql
+ OBJC_IVAR_$__PASSQLTelemetryContext._sqlEventsLog
+ OBJC_IVAR_$__PASSQLTelemetryContext._targetProcess
+ OBJC_IVAR_$__PASSqliteDatabase._sqlTelemetryApi
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$__PASSQLTelemetryApi
+ _OBJC_CLASS_$__PASSQLTelemetryContext
+ _OBJC_METACLASS_$__PASSQLTelemetryApi
+ _OBJC_METACLASS_$__PASSQLTelemetryContext
+ __213+[_PASXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:whitelistedClientInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:logHandle:]_block_invoke.11
+ __33-[_PASSqliteDatabase userVersion]_block_invoke.260
+ __35-[_PASHistogramData countWhereA:b:]_block_invoke.14
+ __36-[_PASSqliteDatabase hasTableNamed:]_block_invoke.273
+ __39-[_PASDatabaseMigrator _clearDatabase:]_block_invoke.58
+ __39-[_PASDatabaseMigrator _clearDatabase:]_block_invoke.67
+ __39-[_PASDatabaseMigrator _clearDatabase:]_block_invoke.72
+ __39-[_PASDatabaseMigrator _clearDatabase:]_block_invoke.76
+ __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.123
+ __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.126
+ __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.130
+ __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.134
+ __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.139
+ __41-[_PASSqliteDatabase valueForPragmaName:]_block_invoke.116
+ __42-[_PASSqliteDatabase languageForFTSTable:]_block_invoke.306
+ __48-[_PASDatabaseJournal executeQueriesOnDatabase:]_block_invoke.63
+ __50-[_PASXPCClientHelper _locked_establishConnection]_block_invoke.7
+ __58-[_PASSqliteDatabase vacuumWithShouldContinueBlock:error:]_block_invoke.137
+ __58-[_PASSqliteDatabase vacuumWithShouldContinueBlock:error:]_block_invoke.141
+ __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke.130
+ __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_2.108
+ __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_2.133
+ __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_3.114
+ __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_4.118
+ __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_5.122
+ __80+[_PASFileUtils iterSortedEntriesInDirectory:selectDirent:onSortedDirent:error:]_block_invoke.11
+ __80+[_PASFileUtils iterSortedEntriesInDirectory:selectDirent:onSortedDirent:error:]_block_invoke.41
+ __80+[_PASFileUtils iterSortedEntriesInDirectory:selectDirent:onSortedDirent:error:]_block_invoke.46
+ __83+[_PASLPWriterV1 _scanPlist:recursionDepth:sizeUpperBound:allDictionaryKeys:error:]_block_invoke.72
+ __83+[_PASLPWriterV1 _scanPlist:recursionDepth:sizeUpperBound:allDictionaryKeys:error:]_block_invoke.80
+ __83+[_PASLPWriterV1 _scanPlist:recursionDepth:sizeUpperBound:allDictionaryKeys:error:]_block_invoke_2.76
+ __88-[_PASLPReaderV1 _validateObjectGraphWithFilename:rootValue:recursionDepth:stats:error:]_block_invoke.92
+ __95+[_PASSqliteDatabase initializeDatabase:withContentProtection:newDatabaseCreated:errorHandler:]_block_invoke.61
+ __Block_byref_object_copy_.2087
+ __Block_byref_object_copy_.2346
+ __Block_byref_object_copy_.2480
+ __Block_byref_object_copy_.2696
+ __Block_byref_object_copy_.3013
+ __Block_byref_object_copy_.3264
+ __Block_byref_object_copy_.3439
+ __Block_byref_object_copy_.4115
+ __Block_byref_object_copy_.795
+ __Block_byref_object_dispose_.2088
+ __Block_byref_object_dispose_.2347
+ __Block_byref_object_dispose_.2481
+ __Block_byref_object_dispose_.2697
+ __Block_byref_object_dispose_.3014
+ __Block_byref_object_dispose_.3265
+ __Block_byref_object_dispose_.3440
+ __Block_byref_object_dispose_.4116
+ __Block_byref_object_dispose_.796
+ __OBJC_$_INSTANCE_METHODS__PASSQLTelemetryApi
+ __OBJC_$_INSTANCE_METHODS__PASSQLTelemetryContext
+ __OBJC_$_INSTANCE_VARIABLES__PASSQLTelemetryApi
+ __OBJC_$_INSTANCE_VARIABLES__PASSQLTelemetryContext
+ __OBJC_$_PROP_LIST__PASSQLTelemetryContext
+ __OBJC_CLASS_RO_$__PASSQLTelemetryApi
+ __OBJC_CLASS_RO_$__PASSQLTelemetryContext
+ __OBJC_METACLASS_RO_$__PASSQLTelemetryApi
+ __OBJC_METACLASS_RO_$__PASSQLTelemetryContext
+ __PASSQLCallback
+ __ZNKSt3__16vectorIDv8_fN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIDv8_iN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrIN9proactive3pas18SynchronizedObjectIN12_GLOBAL__N_113HDGuardedDataENS2_6detail14RecursiveMutexEEENS_14default_deleteIS8_EEE5resetB8ne190102EPS8_
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB8ne190102IPKhS6_EENS_11__wrap_iterIPhEENS7_IS6_EET_T0_l
+ ___41-[_PASSQLTelemetryContext sendTelemetry:]_block_invoke
+ ___45-[_PASSqliteDatabase runQuery:onRow:onError:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0l
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.102
+ __block_literal_global.116
+ __block_literal_global.121
+ __block_literal_global.1213
+ __block_literal_global.132
+ __block_literal_global.156
+ __block_literal_global.1586
+ __block_literal_global.1784
+ __block_literal_global.1932
+ __block_literal_global.2095
+ __block_literal_global.2332
+ __block_literal_global.2485
+ __block_literal_global.2528
+ __block_literal_global.262
+ __block_literal_global.2928
+ __block_literal_global.3069
+ __block_literal_global.308
+ __block_literal_global.3604
+ __block_literal_global.390
+ __block_literal_global.4023
+ __block_literal_global.4121
+ __block_literal_global.4196
+ __block_literal_global.46.4024
+ __block_literal_global.49.3064
+ __block_literal_global.49.4025
+ __block_literal_global.54
+ __block_literal_global.63
+ __block_literal_global.75
+ __block_literal_global.8.2080
+ __block_literal_global.83
+ __block_literal_global.93
+ __block_literal_global.93.3969
+ __block_literal_global.95
+ __block_literal_global.97
+ _kSqlEventFired_block_invoke
+ _objc_msgSend$applyCallbackWithCompletion:
+ _objc_msgSend$authorizerStatusBlock
+ _objc_msgSend$createEventLogForQueryOpCode:argumentOneValue:argumentTwoValue:
+ _objc_msgSend$initWithConnection:sqlQuery:filterPii:
+ _objc_msgSend$initWithConnectionAndSettings:sqlQuery:filterPii:targetProcess:
+ _objc_msgSend$initWithTelemetryContext:
+ _objc_msgSend$isSqlConst
+ _objc_msgSend$isTargetProcess
+ _objc_msgSend$operatingSystemVersionString
+ _objc_msgSend$removeCallback
+ _objc_msgSend$resetLog
+ _objc_msgSend$sendTelemetry
+ _objc_msgSend$sendTelemetry:
+ _objc_msgSend$setAuthorizerStatusBlock:
+ _objc_msgSend$sqlEventLogForTelemetry
+ _objc_msgSend$stringWithCString:encoding:
+ _sqlite3_set_authorizer
+ cfAllocateAlwaysFailing.111
+ cfAllocateAlwaysFailing.1718
+ cfDeallocateReleaseInfo.110
+ corruptionError.1994
+ corruptionError.98
+ runWithGlobalPLPLock.lock.3362
- GCC_except_table1378
- GCC_except_table1381
- GCC_except_table1386
- GCC_except_table1389
- GCC_except_table1393
- GCC_except_table1425
- GCC_except_table1431
- GCC_except_table1439
- GCC_except_table1546
- GCC_except_table1547
- GCC_except_table1573
- GCC_except_table1575
- GCC_except_table1583
- GCC_except_table1594
- GCC_except_table1597
- GCC_except_table1601
- GCC_except_table1603
- GCC_except_table1609
- GCC_except_table1620
- GCC_except_table1640
- GCC_except_table1659
- __213+[_PASXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:whitelistedClientInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:logHandle:]_block_invoke.5
- __33-[_PASSqliteDatabase userVersion]_block_invoke.252
- __35-[_PASHistogramData countWhereA:b:]_block_invoke.8
- __36-[_PASSqliteDatabase hasTableNamed:]_block_invoke.265
- __39-[_PASDatabaseMigrator _clearDatabase:]_block_invoke.52
- __39-[_PASDatabaseMigrator _clearDatabase:]_block_invoke.61
- __39-[_PASDatabaseMigrator _clearDatabase:]_block_invoke.66
- __39-[_PASDatabaseMigrator _clearDatabase:]_block_invoke.70
- __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.108
- __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.111
- __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.124
- __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.128
- __41-[_PASLPReaderV1 _objectForValue:errMsg:]_block_invoke.133
- __41-[_PASSqliteDatabase valueForPragmaName:]_block_invoke.110
- __42-[_PASSqliteDatabase languageForFTSTable:]_block_invoke.298
- __48-[_PASDatabaseJournal executeQueriesOnDatabase:]_block_invoke.57
- __50-[_PASXPCClientHelper _locked_establishConnection]_block_invoke.3
- __58-[_PASSqliteDatabase vacuumWithShouldContinueBlock:error:]_block_invoke.131
- __58-[_PASSqliteDatabase vacuumWithShouldContinueBlock:error:]_block_invoke.135
- __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke.124
- __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_2.102
- __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_2.127
- __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_3.108
- __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_4.112
- __71+[_PASLPWriterV1 _valueWordForObjectGraph:allocContext:recursionDepth:]_block_invoke_5.116
- __80+[_PASFileUtils iterSortedEntriesInDirectory:selectDirent:onSortedDirent:error:]_block_invoke.35
- __80+[_PASFileUtils iterSortedEntriesInDirectory:selectDirent:onSortedDirent:error:]_block_invoke.40
- __80+[_PASFileUtils iterSortedEntriesInDirectory:selectDirent:onSortedDirent:error:]_block_invoke.5
- __83+[_PASLPWriterV1 _scanPlist:recursionDepth:sizeUpperBound:allDictionaryKeys:error:]_block_invoke.66
- __83+[_PASLPWriterV1 _scanPlist:recursionDepth:sizeUpperBound:allDictionaryKeys:error:]_block_invoke.74
- __83+[_PASLPWriterV1 _scanPlist:recursionDepth:sizeUpperBound:allDictionaryKeys:error:]_block_invoke_2.70
- __88-[_PASLPReaderV1 _validateObjectGraphWithFilename:rootValue:recursionDepth:stats:error:]_block_invoke.86
- __95+[_PASSqliteDatabase initializeDatabase:withContentProtection:newDatabaseCreated:errorHandler:]_block_invoke.55
- __Block_byref_object_copy_.2108
- __Block_byref_object_copy_.2366
- __Block_byref_object_copy_.2500
- __Block_byref_object_copy_.2715
- __Block_byref_object_copy_.3037
- __Block_byref_object_copy_.3290
- __Block_byref_object_copy_.3461
- __Block_byref_object_copy_.4122
- __Block_byref_object_copy_.822
- __Block_byref_object_dispose_.2109
- __Block_byref_object_dispose_.2367
- __Block_byref_object_dispose_.2501
- __Block_byref_object_dispose_.2716
- __Block_byref_object_dispose_.3038
- __Block_byref_object_dispose_.3291
- __Block_byref_object_dispose_.3462
- __Block_byref_object_dispose_.4123
- __Block_byref_object_dispose_.823
- __ZNKSt3__16vectorIDv8_fN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIDv8_iN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110unique_ptrIN9proactive3pas18SynchronizedObjectIN12_GLOBAL__N_113HDGuardedDataENS2_6detail14RecursiveMutexEEENS_14default_deleteIS8_EEE5resetB8ne180100EPS8_
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB8ne180100IPKhS6_EENS_11__wrap_iterIPhEENS7_IS6_EET_T0_l
- __block_invoke
- __block_literal_global.115
- __block_literal_global.1251
- __block_literal_global.126
- __block_literal_global.150
- __block_literal_global.1612
- __block_literal_global.1805
- __block_literal_global.1954
- __block_literal_global.2116
- __block_literal_global.2352
- __block_literal_global.2505
- __block_literal_global.254
- __block_literal_global.2547
- __block_literal_global.2950
- __block_literal_global.300
- __block_literal_global.3091
- __block_literal_global.3605
- __block_literal_global.4
- __block_literal_global.40
- __block_literal_global.4040
- __block_literal_global.4129
- __block_literal_global.414.4120
- __block_literal_global.4202
- __block_literal_global.43
- __block_literal_global.45.4041
- __block_literal_global.48
- __block_literal_global.49.3086
- __block_literal_global.69
- __block_literal_global.77
- __block_literal_global.87
- __block_literal_global.87.3988
- __block_literal_global.89
- __block_literal_global.91
- __block_literal_global.96
- __block_literal_global.98
- cfAllocateAlwaysFailing.120
- cfAllocateAlwaysFailing.1745
- cfDeallocateReleaseInfo.119
- corruptionError.104
- corruptionError.2018
- runWithGlobalPLPLock.lock.3385
CStrings:
+ "%@ %@ %@ "
+ "%lu"
+ "@\"NSDictionary\"8@?0"
+ "@\"_PASSQLTelemetryApi\""
+ "@\"_PASSQLTelemetryContext\""
+ "@36@0:8^{sqlite3=}16@24B32"
+ "@44@0:8^{sqlite3=}16@24B32@36"
+ "ALTER TABLE"
+ "ANALYZE"
+ "ATTACH"
+ "CREATE INDEX"
+ "CREATE TABLE"
+ "CREATE TEMP INDEX"
+ "CREATE TEMP TABLE"
+ "CREATE TEMP TRIGGER"
+ "CREATE TEMP VIEW"
+ "CREATE TRIGGER"
+ "CREATE VIEW"
+ "CREATE VTABLE"
+ "DELETE"
+ "DETACH"
+ "DROP INDEX"
+ "DROP TABLE"
+ "DROP TEMP INDEX"
+ "DROP TEMP TRIGGER"
+ "DROP TEMP VIEW"
+ "DROP TRIGGER"
+ "DROP VIEW"
+ "DROP VTABLE"
+ "EventName"
+ "FUNCTION"
+ "INSERT"
+ "OsVersion"
+ "PAS : Current process is %@ Target process is %@"
+ "PAS: Inside _PAS callback"
+ "PAS: Resetting log"
+ "PRAGMA"
+ "Process"
+ "READ"
+ "RECURSIVE"
+ "REINDEX"
+ "SAVEPOINT"
+ "SELECT"
+ "SqlEventLog"
+ "SqlLength"
+ "T@?,C,N,V_authorizerStatusBlock"
+ "TRANSACTION"
+ "UPDATE"
+ "_PAS Telemetry : Sending"
+ "_PASSQLTelemetryApi"
+ "_PASSQLTelemetryContext"
+ "_authorizerStatusBlock"
+ "_dbConnection"
+ "_eventToStringMap"
+ "_filterPii"
+ "_shouldSendTelemetry"
+ "_sql"
+ "_sqlEventsLog"
+ "_sqlTelemetryApi"
+ "_targetProcess"
+ "_telemetryContext"
+ "applyCallbackWithCompletion:"
+ "authorizerStatusBlock"
+ "com.apple.sear.diagnostics"
+ "createEventLogForQueryOpCode:argumentOneValue:argumentTwoValue:"
+ "currentProcessName"
+ "currentTargetName"
+ "initWithConnection:sqlQuery:filterPii:"
+ "initWithConnectionAndSettings:sqlQuery:filterPii:targetProcess:"
+ "initWithTelemetryContext:"
+ "isSqlConst"
+ "isSqlValidLength"
+ "isTargetProcess"
+ "operatingSystemVersionString"
+ "removeCallback"
+ "resetLog"
+ "sendTelemetry"
+ "sendTelemetry:"
+ "setAuthorizerStatusBlock:"
+ "sqlEventLogForTelemetry"
+ "stringWithCString:encoding:"
+ "v36@0:8i16@20@28"
- ".."

```
