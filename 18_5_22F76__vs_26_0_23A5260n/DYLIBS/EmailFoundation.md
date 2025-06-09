## EmailFoundation

> `/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation`

```diff

-3826.600.51.2.1
-  __TEXT.__text: 0x64a98
-  __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_methlist: 0x6534
-  __TEXT.__gcc_except_tab: 0xc094
+3853.100.6.2.6
+  __TEXT.__text: 0x660ec
+  __TEXT.__auth_stubs: 0x14d0
+  __TEXT.__objc_methlist: 0x6684
+  __TEXT.__gcc_except_tab: 0xc2d4
   __TEXT.__const: 0x1fa
-  __TEXT.__cstring: 0x46e7
-  __TEXT.__oslogstring: 0x114f
+  __TEXT.__cstring: 0x4897
+  __TEXT.__oslogstring: 0xfdf
   __TEXT.__ustring: 0x138
   __TEXT.__swift5_typeref: 0xda
   __TEXT.__swift5_capture: 0xd0

   __TEXT.__swift5_fieldmd: 0x7c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x4998
+  __TEXT.__unwind_info: 0x4a40
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0xe58
-  __TEXT.__objc_methname: 0xc0b4
-  __TEXT.__objc_methtype: 0x1c5f
-  __TEXT.__objc_stubs: 0x8880
-  __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x2108
-  __DATA_CONST.__objc_classlist: 0x438
+  __TEXT.__objc_classname: 0xe72
+  __TEXT.__objc_methname: 0xc2ac
+  __TEXT.__objc_methtype: 0x1c0d
+  __TEXT.__objc_stubs: 0x8ac0
+  __DATA_CONST.__got: 0x778
+  __DATA_CONST.__const: 0x2130
+  __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3438
+  __DATA_CONST.__objc_selrefs: 0x34b8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x390
-  __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xa30
-  __AUTH_CONST.__const: 0x10a8
-  __AUTH_CONST.__cfstring: 0x55e0
-  __AUTH_CONST.__objc_const: 0xc180
+  __DATA_CONST.__objc_superrefs: 0x398
+  __DATA_CONST.__objc_arraydata: 0x48
+  __AUTH_CONST.__auth_got: 0xa80
+  __AUTH_CONST.__const: 0x1148
+  __AUTH_CONST.__cfstring: 0x5640
+  __AUTH_CONST.__objc_const: 0xc328
   __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x510
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x524
   __DATA.__data: 0xf28
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1b8
-  __DATA_DIRTY.__objc_data: 0x23a0
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x208
+  __DATA_DIRTY.__objc_data: 0x22b0
   __DATA_DIRTY.__data: 0x1
-  __DATA_DIRTY.__bss: 0x328
+  __DATA_DIRTY.__bss: 0x31c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress
   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: EB077466-EE74-375D-B88C-D2B979F9A179
-  Functions: 2620
-  Symbols:   9970
-  CStrings:  4309
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 7B49CF74-1321-39B4-93BD-BDB933FCACCF
+  Functions: 2654
+  Symbols:   10119
+  CStrings:  4343
 
Symbols:
+ +[EFFileLogger enabled]
+ +[EFManualCancelationToken _descriptionString]
+ +[EFManualCancelationToken tokenWithCancelationBlock:]
+ +[EFManualCancelationToken tokenWithLabel:cancelationBlock:]
+ +[EFQueryLogger _logQueue]
+ +[EFQueryLogger _logQueue].cold.1
+ +[NSDate(EmailFoundationAdditions) ef_dateSecondsAgo:]
+ +[NSDate(EmailFoundationAdditions) ef_nextWeekday:]
+ +[NSDate(EmailFoundationAdditions) ef_weekDayForDate:]
+ +[NSPredicate(EmailFoundationAdditions) _ef_compoundPredicateWithSubpredicatesForSearch:isAnd:]
+ +[NSPredicate(EmailFoundationAdditions) ef_andCompoundPredicateWithSubpredicatesForSearchQuery:]
+ -[EFCancelationToken dealloc]
+ -[EFDevice isRealityDevice]
+ -[EFDevice isRealityDevice].cold.1
+ -[EFFileLogger .cxx_destruct]
+ -[EFFileLogger _ensureCustomLogFileInDirectory:]
+ -[EFFileLogger _ensureCustomLogFileInDirectory:].cold.1
+ -[EFFileLogger filename]
+ -[EFFileLogger initWithFilename:directory:]
+ -[EFFileLogger logSnippet:]
+ -[EFFileLogger setFilename:]
+ -[EFFileLogger slurpAndRemoveLookasideFile:prefixString:suffixString:]
+ -[EFInt64Set _appendRange:toString:withSeparator:]
+ -[EFInt64Set _lastRange]
+ -[EFManualCancelationToken addCancelable:]
+ -[EFManualCancelationToken addCancelationBlock:]
+ -[EFManualCancelationToken cancel]
+ -[EFManualCancelationToken isCanceled]
+ -[EFManualCancelationToken removeAllCancelationBlocks]
+ -[EFMutableOrderedDictionary removeObjectsAtIndexes:]
+ -[EFMutableOrderedDictionary removeObjectsForKeys:]
+ -[EFOrderedDictionary objectsAtIndexes:]
+ -[EFOrderedDictionary objectsForKeys:notFoundMarker:]
+ -[EFQueryLogger .cxx_destruct]
+ -[EFQueryLogger _moveLogFileContentsAtPath:]
+ -[EFQueryLogger _moveLogFileContentsWithoutDateAtPath:]
+ -[EFQueryLogger _openLookasideFile]
+ -[EFQueryLogger _sortAndWriteQueries:forCount:totalCount:queryCountMap:]
+ -[EFQueryLogger countQueryString:executionTime:]
+ -[EFQueryLogger flushLogsWithoutDate]
+ -[EFQueryLogger flushLogs]
+ -[EFQueryLogger initWithBaseFilename:directory:]
+ -[EFQueryLogger logPlainTextData:]
+ -[EFQueryLogger logQueryString:]
+ -[EFQueryLogger logUniqueQueryString:]
+ -[EFQueryStatistics count]
+ -[EFQueryStatistics setCount:]
+ -[EFQueryStatistics setTotalExecutionTime:]
+ -[EFQueryStatistics totalExecutionTime]
+ OBJC_IVAR_$_EFQueryLogger._didFlushLogs
+ OBJC_IVAR_$_EFQueryLogger._lookasideFileHandle
+ OBJC_IVAR_$_EFQueryLogger._lookasideFilePath
+ _CFCalendarCreateWithIdentifier
+ _CFCalendarDecomposeAbsoluteTime
+ _CFStringCreateCopy
+ _DACPLoggingAddCustomLogFile
+ _DACPLoggingAppendDataToLogFile
+ _DACPLoggingSlurpFileIntoLogFile
+ _DAMigrateLogsIfNeeded
+ _NSLog
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_DATrafficLogFilename
+ _OBJC_CLASS_$_EFFileLogger
+ _OBJC_CLASS_$_EFManualCancelationToken
+ _OBJC_CLASS_$_EFQueryLogger
+ _OBJC_CLASS_$_EFQueryStatistics
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_IVAR_$_EFFileLogger._filename
+ _OBJC_IVAR_$_EFQueryLogger._baseFileName
+ _OBJC_IVAR_$_EFQueryLogger._logDirectory
+ _OBJC_IVAR_$_EFQueryStatistics._count
+ _OBJC_IVAR_$_EFQueryStatistics._totalExecutionTime
+ _OBJC_METACLASS_$_EFFileLogger
+ _OBJC_METACLASS_$_EFManualCancelationToken
+ _OBJC_METACLASS_$_EFQueryLogger
+ _OBJC_METACLASS_$_EFQueryStatistics
+ __OBJC_$_CLASS_METHODS_EFFileLogger
+ __OBJC_$_CLASS_METHODS_EFManualCancelationToken
+ __OBJC_$_CLASS_METHODS_EFQueryLogger
+ __OBJC_$_INSTANCE_METHODS_EFFileLogger
+ __OBJC_$_INSTANCE_METHODS_EFManualCancelationToken
+ __OBJC_$_INSTANCE_METHODS_EFQueryLogger
+ __OBJC_$_INSTANCE_METHODS_EFQueryStatistics
+ __OBJC_$_INSTANCE_VARIABLES_EFFileLogger
+ __OBJC_$_INSTANCE_VARIABLES_EFQueryLogger
+ __OBJC_$_INSTANCE_VARIABLES_EFQueryStatistics
+ __OBJC_$_PROP_LIST_EFFileLogger
+ __OBJC_$_PROP_LIST_EFManualCancelationToken
+ __OBJC_$_PROP_LIST_EFQueryStatistics
+ __OBJC_CLASS_PROTOCOLS_$_EFManualCancelationToken
+ __OBJC_CLASS_RO_$_EFFileLogger
+ __OBJC_CLASS_RO_$_EFManualCancelationToken
+ __OBJC_CLASS_RO_$_EFQueryLogger
+ __OBJC_CLASS_RO_$_EFQueryStatistics
+ __OBJC_METACLASS_RO_$_EFFileLogger
+ __OBJC_METACLASS_RO_$_EFManualCancelationToken
+ __OBJC_METACLASS_RO_$_EFQueryLogger
+ __OBJC_METACLASS_RO_$_EFQueryStatistics
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__115insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEaSB8ne200100ERKx
+ __ZNSt3__118__set_intersectionB8ne200100INS_17_ClassicAlgPolicyENS_6__lessIvvEENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES9_S9_S9_NS_15insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEEEENS_25__set_intersection_resultIT1_T3_T5_EESJ_T2_SK_T4_SL_OT0_NS_20forward_iterator_tagESR_
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__122__lower_bound_onesidedB8ne200100INS_17_ClassicAlgPolicyENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES7_xKNS_10__identityENS_6__lessIvvEEEET0_SC_T1_RKT2_RT4_RT3_
+ __ZNSt3__123__lower_bound_bisectingB8ne200100INS_17_ClassicAlgPolicyENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEExKNS_10__identityENS_6__lessIvvEEEET0_SC_RKT1_NS_15iterator_traitsISC_E15difference_typeERT3_RT2_
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__138__set_intersection_add_output_if_equalB8ne200100INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES6_NS_15insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEEEEvbRT_RT0_RT1_Rb
+ __ZNSt3__13setIxNS_4lessIxEENS_9allocatorIxEEE6insertB8ne200100INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEEvT_SD_
+ __ZNSt3__13setIxNS_4lessIxEENS_9allocatorIxEEEC2B8ne200100ERKS5_
+ __ZNSt3__16__treeIxNS_4lessIxEENS_9allocatorIxEEE18_DetachedTreeCacheD2B8ne200100Ev
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE12__advance_toB8ne200100INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEENS_15iterator_traitsIT_E15difference_typeERSB_SD_RKSB_NS_26bidirectional_iterator_tagE
+ __ZNSt3__19__advanceB8ne200100INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEEvRT_NS_15iterator_traitsIS7_E15difference_typeENS_26bidirectional_iterator_tagE
+ __ZnwmSt19__type_descriptor_t
+ ___26+[EFQueryLogger _logQueue]_block_invoke
+ ___26-[EFQueryLogger flushLogs]_block_invoke
+ ___27-[EFDevice isRealityDevice]_block_invoke
+ ___27-[EFFileLogger logSnippet:]_block_invoke
+ ___34-[EFQueryLogger logPlainTextData:]_block_invoke
+ ___37-[EFQueryLogger flushLogsWithoutDate]_block_invoke
+ ___38-[EFQueryLogger logUniqueQueryString:]_block_invoke
+ ___42-[EFManualCancelationToken addCancelable:]_block_invoke
+ ___48-[EFFileLogger _ensureCustomLogFileInDirectory:]_block_invoke
+ ___48-[EFFileLogger _ensureCustomLogFileInDirectory:]_block_invoke_2
+ ___48-[EFFileLogger _ensureCustomLogFileInDirectory:]_block_invoke_3
+ ___48-[EFQueryLogger countQueryString:executionTime:]_block_invoke
+ ___48-[EFQueryLogger countQueryString:executionTime:]_block_invoke_2
+ ___70-[EFFileLogger slurpAndRemoveLookasideFile:prefixString:suffixString:]_block_invoke
+ ___95+[NSPredicate(EmailFoundationAdditions) _ef_compoundPredicateWithSubpredicatesForSearch:isAnd:]_block_invoke
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_32_e98_^{__CFString=}76?0i8^{__CFDate=}12^{__CFString=}20^{__CFString=}28r*36r*44Q52^v60^{__CFString=}68l
+ ___block_descriptor_40_ea8_32r_e28_v32?0"NSPredicate"8Q16^B24lr32l8
+ ___block_descriptor_48_ea8_32s40bs_e34_v16?0"EFManualCancelationToken"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_ea8_32s40bs48w_e34_v16?0"EFManualCancelationToken"8lw48l8s32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48s_e34_v16?0"EFManualCancelationToken"8ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s_e48_"EFManualCancelationToken"16?0"<EFObserver>"8ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.150
+ ___block_literal_global.41
+ ___block_literal_global.48
+ __block_invoke.uniqueQuerySet
+ __block_invoke_2.logCount
+ __block_invoke_2.queryCountMap
+ __ensureCustomLogFileInDirectory:.knownCustomNames
+ __ensureCustomLogFileInDirectory:.logSetupQueue
+ __ensureCustomLogFileInDirectory:.once
+ __logQueue.logQueue
+ __logQueue.onceToken
+ __openLookasideFile.sResponseNumber
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_EmailFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_EmailFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_EmailFoundation
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_EmailFoundation
+ _isRealityDevice.isRealityDevice
+ _isRealityDevice.onceToken
+ _kCFBooleanFalse
+ _kCFGregorianCalendar
+ _kDACPLoggingCustomCreateLogFormatBlock
+ _kDACPLoggingCustomLogDirectoryKey
+ _kDACPLoggingCustomLogNameKey
+ _kDACPLoggingCustomMaxConsoleLevelKey
+ _kDACPLoggingCustomMaxLogFileLevelKey
+ _kDACPLoggingEnableNewlinesKey
+ _modf
+ _objc_msgSend$_appendRange:toString:withSeparator:
+ _objc_msgSend$_ef_compoundPredicateWithSubpredicatesForSearch:isAnd:
+ _objc_msgSend$_ensureCustomLogFileInDirectory:
+ _objc_msgSend$_lastRange
+ _objc_msgSend$_logQueue
+ _objc_msgSend$_moveLogFileContentsAtPath:
+ _objc_msgSend$_moveLogFileContentsWithoutDateAtPath:
+ _objc_msgSend$_openLookasideFile
+ _objc_msgSend$_sortAndWriteQueries:forCount:totalCount:queryCountMap:
+ _objc_msgSend$countQueryString:executionTime:
+ _objc_msgSend$enabled
+ _objc_msgSend$fileDescriptor
+ _objc_msgSend$filename
+ _objc_msgSend$filenameWithBasename:
+ _objc_msgSend$flushLogs
+ _objc_msgSend$flushLogsWithoutDate
+ _objc_msgSend$initWithFileDescriptor:closeOnDealloc:
+ _objc_msgSend$initWithFilename:directory:
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$logPlainTextData:
+ _objc_msgSend$logQueryString:
+ _objc_msgSend$logQueryString:executionTime:firstRowExecutionTime:numberOfRows:
+ _objc_msgSend$logSnippet:
+ _objc_msgSend$logUniqueQueryString:
+ _objc_msgSend$redactedQueryStringForQueryString:
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$scanCharactersFromSet:intoString:
+ _objc_msgSend$scanString:intoString:
+ _objc_msgSend$scanUpToString:intoString:
+ _objc_msgSend$setCount:
+ _objc_msgSend$setFilename:
+ _objc_msgSend$setTotalExecutionTime:
+ _objc_msgSend$slurpAndRemoveLookasideFile:prefixString:suffixString:
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$totalExecutionTime
+ _objc_msgSend$weekday
+ _write
- +[EFCancelationToken _descriptionString]
- +[EFCancelationToken tokenWithCancelationBlock:]
- +[EFCancelationToken tokenWithLabel:cancelationBlock:]
- +[EFFileProtectionHandler log]
- +[EFPrivacy redactedQueryStringForSearchableQueryString:]
- -[EFAutoCancelationToken dealloc]
- -[EFCancelationToken addCancelable:]
- -[EFCancelationToken addCancelationBlock:]
- -[EFCancelationToken cancel]
- -[EFCancelationToken isCanceled]
- -[EFCancelationToken removeAllCancelationBlocks]
- -[EFFileProtectionHandler .cxx_destruct]
- -[EFFileProtectionHandler _moveQueuedFiles]
- -[EFFileProtectionHandler enqueueMovingFile:toProtectionClass:]
- -[EFFileProtectionHandler enqueueMovingFileProtections:]
- -[EFFileProtectionHandler enqueueMovingFiles:toProtectionClass:]
- -[EFFileProtectionHandler init]
- -[EFFileProtectionHandler moveFile:toProtectionClass:]
- -[EFFileProtectionHandler moveFile:toProtectionClass:].cold.1
- -[EFFileProtectionHandler registerMoveFileBackgroundTask]
- -[EFFileProtectionHandler registerMoveFileBackgroundTask].cold.1
- -[EFFileProtectionHandler unregisterMoveFileBackgroundTask]
- -[EFFileProtectionHandler unregisterMoveFileBackgroundTask].cold.1
- -[EFSQLPreparedStatement executeUsingBlock:error:].cold.5
- _AnalyticsSendEventLazy
- _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
- _OBJC_CLASS_$_BGSystemTaskScheduler
- _OBJC_CLASS_$_EFAutoCancelationToken
- _OBJC_CLASS_$_EFFileProtectionHandler
- _OBJC_IVAR_$_EFFileProtectionHandler._backgroundTaskQueue
- _OBJC_IVAR_$_EFFileProtectionHandler._lock
- _OBJC_IVAR_$_EFFileProtectionHandler._moveFileQueue
- _OBJC_METACLASS_$_EFAutoCancelationToken
- _OBJC_METACLASS_$_EFFileProtectionHandler
- __OBJC_$_CLASS_METHODS_EFCancelationToken
- __OBJC_$_CLASS_METHODS_EFFileProtectionHandler
- __OBJC_$_CLASS_PROP_LIST_EFFileProtectionHandler
- __OBJC_$_INSTANCE_METHODS_EFAutoCancelationToken
- __OBJC_$_INSTANCE_METHODS_EFFileProtectionHandler
- __OBJC_$_INSTANCE_VARIABLES_EFFileProtectionHandler
- __OBJC_$_PROP_LIST_EFCancelationToken
- __OBJC_$_PROP_LIST_EFFileProtectionHandler
- __OBJC_CLASS_PROTOCOLS_$_EFCancelationToken
- __OBJC_CLASS_PROTOCOLS_$_EFFileProtectionHandler
- __OBJC_CLASS_RO_$_EFAutoCancelationToken
- __OBJC_CLASS_RO_$_EFFileProtectionHandler
- __OBJC_METACLASS_RO_$_EFAutoCancelationToken
- __OBJC_METACLASS_RO_$_EFFileProtectionHandler
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__115insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEaSB8ne190102ERKx
- __ZNSt3__118__set_intersectionB8ne190102INS_17_ClassicAlgPolicyENS_6__lessIvvEENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES9_S9_S9_NS_15insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEEEENS_25__set_intersection_resultIT1_T3_T5_EESJ_T2_SK_T4_SL_OT0_NS_20forward_iterator_tagESR_
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__122__lower_bound_onesidedB8ne190102INS_17_ClassicAlgPolicyENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES7_xKNS_10__identityENS_6__lessIvvEEEET0_SC_T1_RKT2_RT4_RT3_
- __ZNSt3__123__lower_bound_bisectingB8ne190102INS_17_ClassicAlgPolicyENS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEExKNS_10__identityENS_6__lessIvvEEEET0_SC_RKT1_NS_15iterator_traitsISC_E15difference_typeERT3_RT2_
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__138__set_intersection_add_output_if_equalB8ne190102INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEES6_NS_15insert_iteratorINS_3setIxNS_4lessIxEENS_9allocatorIxEEEEEEEEvbRT_RT0_RT1_Rb
- __ZNSt3__13setIxNS_4lessIxEENS_9allocatorIxEEE6insertB8ne190102INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEEvT_SD_
- __ZNSt3__13setIxNS_4lessIxEENS_9allocatorIxEEEC2B8ne190102ERKS5_
- __ZNSt3__16__treeIxNS_4lessIxEENS_9allocatorIxEEE18_DetachedTreeCacheD2B8ne190102Ev
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE12__advance_toB8ne190102INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEENS_15iterator_traitsIT_E15difference_typeERSB_SD_RKSB_NS_26bidirectional_iterator_tagE
- __ZNSt3__19__advanceB8ne190102INS_21__tree_const_iteratorIxPNS_11__tree_nodeIxPvEElEEEEvRT_NS_15iterator_traitsIS7_E15difference_typeENS_26bidirectional_iterator_tagE
- __Znwm
- ___30+[EFFileProtectionHandler log]_block_invoke
- ___36-[EFCancelationToken addCancelable:]_block_invoke
- ___43-[EFFileProtectionHandler _moveQueuedFiles]_block_invoke
- ___43-[EFFileProtectionHandler _moveQueuedFiles]_block_invoke_2
- ___57+[EFPrivacy redactedQueryStringForSearchableQueryString:]_block_invoke
- ___57-[EFFileProtectionHandler registerMoveFileBackgroundTask]_block_invoke
- ___57-[EFFileProtectionHandler registerMoveFileBackgroundTask]_block_invoke.cold.1
- ___block_descriptor_40_ea8_32w_e31_v16?0"BGRepeatingSystemTask"8lw32l8
- ___block_descriptor_48_ea8_32s40bs_e28_v16?0"EFCancelationToken"8ls32l8s40l8
- ___block_descriptor_48_ea8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
- ___block_descriptor_48_ea8_32s40s_e37_v32?0"NSTextCheckingResult"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_ea8_32s40bs48w_e28_v16?0"EFCancelationToken"8lw48l8s32l8s40l8
- ___block_descriptor_56_ea8_32s40s48s_e28_v16?0"EFCancelationToken"8ls32l8s40l8s48l8
- ___block_descriptor_56_ea8_32s40s_e42_"EFCancelationToken"16?0"<EFObserver>"8ls32l8s40l8
- ___block_literal_global.146
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_EmailFoundation
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_EmailFoundation
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_EmailFoundation
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_EmailFoundation
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_EmailFoundation
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_EmailFoundation
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_EmailFoundation
- _objc_msgSend$_moveQueuedFiles
- _objc_msgSend$deregisterTaskWithIdentifier:
- _objc_msgSend$dictionaryWithDictionary:
- _objc_msgSend$dictionaryWithObject:forKey:
- _objc_msgSend$emailAddressValue
- _objc_msgSend$fullyOrPartiallyRedactedStringForString:
- _objc_msgSend$initWithIdentifier:
- _objc_msgSend$moveFile:toProtectionClass:
- _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
- _objc_msgSend$setInterval:
- _objc_msgSend$setMinDurationBetweenInstances:
- _objc_msgSend$setRequiresExternalPower:
- _objc_msgSend$setRequiresNetworkConnectivity:
- _objc_msgSend$setRequiresProtectionClass:
- _objc_msgSend$setResourceValue:forKey:error:
- _objc_msgSend$sharedScheduler
- _objc_msgSend$submitTaskRequest:error:
- _objc_msgSend$taskRequestForIdentifier:
CStrings:
+ "\nCount: %lu, Percentage of total: %.2f%%, Average Execution Time: %0.06f seconds\n%@"
+ "\nTotal query count: %lu, Unique query count: %lu"
+ "%d-%d"
+ "%lld:%lld"
+ "%p QUERY PLAN for clause(%llu): %@"
+ "(uint64_t)loc + len <= INT64_MAX"
+ ","
+ ",...(%llu more)..."
+ "<<%04d-%02d-%02d %02d:%02d:%02d.%03d>>"
+ "@\"<EFCancelable>\"24@0:8@?<v@?@\"EFManualCancelationToken\">16"
+ "@\"EFManualCancelationToken\""
+ "@\"EFManualCancelationToken\"16@?0@\"<EFObserver>\"8"
+ "@\"NSFileHandle\""
+ "EFFileLogger"
+ "EFInt64Range EFMakeInt64Range(int64_t, uint64_t)"
+ "EFInt64Set.h"
+ "EFManualCancelationToken"
+ "EFQueryLogger"
+ "EFQueryLogger.m"
+ "EFQueryStatistics"
+ "INT64_MAX - (int64_t)len >= loc"
+ "RealityDevice"
+ "Starting a new session for logging unique queries"
+ "T@\"NSString\",&,N,V_filename"
+ "TQ,N,V_count"
+ "Td,N,V_totalExecutionTime"
+ "UNION"
+ "Warning: couldn't open the log file %s: returned errno %ld, \"%s\""
+ "^{__CFString=}76@?0i8^{__CFDate=}12^{__CFString=}20^{__CFString=}28r*36r*44Q52^v60^{__CFString=}68"
+ "_appendRange:toString:withSeparator:"
+ "_baseFileName"
+ "_didFlushLogs"
+ "_ef_compoundPredicateWithSubpredicatesForSearch:isAnd:"
+ "_ensureCustomLogFileInDirectory:"
+ "_filename"
+ "_lastRange"
+ "_logDirectory"
+ "_logQueue"
+ "_lookasideFileHandle"
+ "_lookasideFilePath"
+ "_lookasideFilePath is not nil in _openTempLogFile"
+ "_moveLogFileContentsAtPath:"
+ "_moveLogFileContentsWithoutDateAtPath:"
+ "_openLookasideFile"
+ "_sortAndWriteQueries:forCount:totalCount:queryCountMap:"
+ "_totalExecutionTime"
+ "com.apple.email.EFQueryLoggerQueue"
+ "com.apple.email.queryLogging"
+ "countQueryString:executionTime:"
+ "ef_andCompoundPredicateWithSubpredicatesForSearchQuery:"
+ "ef_dateSecondsAgo:"
+ "ef_nextWeekday:"
+ "ef_weekDayForDate:"
+ "enabled"
+ "fileDescriptor"
+ "filenameWithBasename:"
+ "flushLogs"
+ "flushLogsWithoutDate"
+ "initWithBaseFilename:directory:"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "initWithFilename:directory:"
+ "isRealityDevice"
+ "keysSortedByValueUsingComparator:"
+ "len <= INT64_MAX"
+ "logPlainTextData:"
+ "logQueryString:"
+ "logQueryString:executionTime:firstRowExecutionTime:numberOfRows:"
+ "logSnippet:"
+ "logUniqueQueryString:"
+ "removeObjectsInArray:"
+ "scanCharactersFromSet:intoString:"
+ "scanString:intoString:"
+ "scanUpToString:intoString:"
+ "setCount:"
+ "setTotalExecutionTime:"
+ "slurpAndRemoveLookasideFile:prefixString:suffixString:"
+ "sortUsingSelector:"
+ "totalExecutionTime"
+ "v16@?0@\"EFManualCancelationToken\"8"
+ "v32@0:8@16d24"
+ "v44@0:8{_EFInt64Range=qQ}16@32B40"
+ "v48@0:8@16Q24Q32@40"
+ "weekday"
+ "yMdHms"
+ "{_EFInt64Range=qQ}16@0:8"
+ "{set<long long, std::less<long long>, std::allocator<long long>>=\"__tree_\"{__tree<long long, std::less<long long>, std::allocator<long long>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "%@ = '%@'"
- "%@|"
- "%lld,"
- ") = '([^']+)'\\)"
- "<%@: %p> ["
- "@\"<EFCancelable>\"24@0:8@?<v@?@\"EFCancelationToken\">16"
- "@\"EFCancelationToken\""
- "@\"EFCancelationToken\"16@?0@\"<EFObserver>\"8"
- "EFAutoCancelationToken"
- "EFFileProtectionHandler"
- "Fail to create FileProtectionHandler background task. Error %@"
- "Failure"
- "FileProtectionHandler background task already exists."
- "Moving file %@ to protection type %@ failed with error %{public}@"
- "Not handling background task because FileProtectionHandler is nil."
- "Starting background task for moving file protection"
- "Status"
- "Stopping background task for moving file protection"
- "Success"
- "Successfully moved file %@ to protection type %@"
- "Target File Protection"
- "\\(("
- "_backgroundTaskQueue"
- "_moveFileQueue"
- "_moveQueuedFiles"
- "com.apple.email.moveFileProtection"
- "com.apple.email.moveFileProtectionBackgroundTaskQueue"
- "com.apple.mail.moveFileProtectionEvent"
- "deregisterTaskWithIdentifier:"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "emailAddressValue"
- "enqueueMovingFile:toProtectionClass:"
- "enqueueMovingFileProtections:"
- "enqueueMovingFiles:toProtectionClass:"
- "initWithIdentifier:"
- "kMDItemAuthorEmailAddresses"
- "kMDItemAuthors"
- "moveFile:toProtectionClass:"
- "redactedQueryStringForSearchableQueryString:"
- "registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "registerMoveFileBackgroundTask"
- "setInterval:"
- "setMinDurationBetweenInstances:"
- "setRequiresExternalPower:"
- "setRequiresNetworkConnectivity:"
- "setRequiresProtectionClass:"
- "setResourceValue:forKey:error:"
- "sharedScheduler"
- "submitTaskRequest:error:"
- "taskRequestForIdentifier:"
- "unregisterMoveFileBackgroundTask"
- "v16@?0@\"BGRepeatingSystemTask\"8"
- "v16@?0@\"EFCancelationToken\"8"
- "{set<long long, std::less<long long>, std::allocator<long long>>=\"__tree_\"{__tree<long long, std::less<long long>, std::allocator<long long>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<long long, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::less<long long>>=\"__value_\"Q}}}"

```
