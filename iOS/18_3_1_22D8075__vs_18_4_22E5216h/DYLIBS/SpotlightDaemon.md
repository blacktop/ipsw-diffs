## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2328.7.8.5.0
-  __TEXT.__text: 0x960c0
-  __TEXT.__auth_stubs: 0x1c80
-  __TEXT.__objc_methlist: 0x3704
-  __TEXT.__const: 0x320
-  __TEXT.__cstring: 0x740f
-  __TEXT.__gcc_except_tab: 0x3ec4
-  __TEXT.__oslogstring: 0x89e9
-  __TEXT.__unwind_info: 0x1f98
-  __TEXT.__objc_classname: 0x461
-  __TEXT.__objc_methname: 0xc94b
-  __TEXT.__objc_methtype: 0x20c0
-  __TEXT.__objc_stubs: 0xa3c0
-  __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__const: 0x36b8
-  __DATA_CONST.__objc_classlist: 0x148
+2333.7.0.1.0
+  __TEXT.__text: 0x9ed4c
+  __TEXT.__auth_stubs: 0x1d00
+  __TEXT.__objc_methlist: 0x3e9c
+  __TEXT.__const: 0x360
+  __TEXT.__cstring: 0x781e
+  __TEXT.__oslogstring: 0x9bd8
+  __TEXT.__gcc_except_tab: 0x3fcc
+  __TEXT.__unwind_info: 0x2150
+  __TEXT.__objc_classname: 0x48e
+  __TEXT.__objc_methname: 0xd184
+  __TEXT.__objc_methtype: 0x223e
+  __TEXT.__objc_stubs: 0xabc0
+  __DATA_CONST.__got: 0x910
+  __DATA_CONST.__const: 0x3958
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2eb0
+  __DATA_CONST.__objc_selrefs: 0x31d0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0x430
-  __AUTH_CONST.__auth_got: 0xe58
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_arraydata: 0x448
+  __AUTH_CONST.__auth_got: 0xe98
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0xe28
-  __AUTH_CONST.__cfstring: 0x6400
-  __AUTH_CONST.__objc_const: 0x5b38
-  __AUTH_CONST.__objc_arrayobj: 0x318
+  __AUTH_CONST.__const: 0xf28
+  __AUTH_CONST.__cfstring: 0x67c0
+  __AUTH_CONST.__objc_const: 0x54e0
+  __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x3e0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x3fc
   __DATA.__data: 0x7a0
-  __DATA.__bss: 0xe9
+  __DATA.__bss: 0x189
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x220
-  __DATA_DIRTY.__bss: 0x518
+  __DATA_DIRTY.__bss: 0x4f0
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 2470
-  Symbols:   3369
-  CStrings:  4341
+  Functions: 2626
+  Symbols:   3547
+  CStrings:  4551
 
Symbols:
+ _AKSIdentityGetSessionInfo
+ _MDItemInterestingDate
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_SPHistoricalReport
+ _OBJC_CLASS_$_SPHistoricalReportManager
+ _OBJC_METACLASS_$_SPHistoricalReport
+ _OBJC_METACLASS_$_SPHistoricalReportManager
+ _OSThermalNotificationCurrentLevel
+ _SILogBulkDeleteEvent
+ _SINotifyLowspace
+ _SISetThermalStateBad
+ __SIProtectionClass
+ __os_log_fault_impl
+ _flock
+ _fsync
+ _kOSThermalNotificationPressureLevelName
+ _memcpy
+ _read
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
- __ZSt9terminatev
- ___cxa_begin_catch
CStrings:
+ "### _changeFilesToClassC: cant open class C mail index path %@ err:%d(%s)"
+ "### _changeFilesToClassC: cant open class C mail index subpath %@ err:%d(%s)"
+ "### _changeFilesToClassC: changing files in %@ protection class to class C"
+ "### _changeFilesToClassC: error changing protection class of directory %@ err:%d"
+ "### _changeFilesToClassC: error changing protection class of files in %@ err:%d"
+ "### _deleteNonMailBundlesFromClassAIndex: Bundles other than mail to be deleted: %@"
+ "### _deleteNonMailBundlesFromClassAIndex: bundle %@ delete error: %@"
+ "### _deleteNonMailBundlesFromClassAIndex: deletion complete"
+ "### _finishFileTransferToClassCMailIndex: Failed to move class A mail index path:%@ to class C path:%@, error:%@"
+ "### _finishFileTransferToClassCMailIndex: device is locked, trying protection class change on next unlock"
+ "### _fixProtClassForClassCMailIndex: already done"
+ "### _fixProtClassForClassCMailIndex: can't invoke this method before file transfer complete"
+ "### _fixProtClassForClassCMailIndex: class C mail index does not exist, nothing to do"
+ "### _fixProtClassForClassCMailIndex: class C mail index path %@ is not a directory!"
+ "### _fixProtClassForClassCMailIndex: error changing protection class: %@"
+ "### _fixProtClassForClassCMailIndex: unexpected codepath, _moveClassAIndexToClassCMailIndex should have created index directory, sMailClassCFileTransferComplete = %d"
+ "### _mailClassCMarkFileTransferComplete: Creating touch file"
+ "### _mailClassCMarkMigrationComplete: Creating touch file"
+ "### _mailClassCResetIndexAndComplete: Blowing indexes"
+ "### _moveClassAIndexToClassCMailIndex: Class A index does not exist"
+ "### _moveClassAIndexToClassCMailIndex: already done"
+ "### _moveClassAIndexToClassCMailIndex: bundle fetch error: %@"
+ "### _moveClassAIndexToClassCMailIndex: bundle task creation failure"
+ "### _moveClassAIndexToClassCMailIndex: device is locked, trying delete bundles next unlock"
+ "### _useMobileMailIndex: Using default mobile_mail_index_enabled=%d"
+ "### checkMailMigrationToClassCComplete: already done"
+ "### moveBackMailToClassA: Failed to move class C mail index path:%@ to class A path:%@, error:%@"
+ "### moveBackMailToClassA: class C mail index exists, moving it back"
+ "### moveBackMailToClassA: found touch file and FF is disabled!"
+ "### moveMailToClassC: changing protection class on unlock"
+ "### moveMailToClassC: deleting non-mail bundles: %@"
+ "%@_type%d.json"
+ "*warn* ### _moveClassAIndexToClassCMailIndex: Deleting stale class C mail directory"
+ "*warn* Deleted old mail index for mail migration"
+ "*warn* Migration step %@ already completed"
+ "/Library/Spotlight/CoreSpotlight/HistoricalReports"
+ "2333.7.0.1"
+ "@\"NSDate\""
+ "Attempted to open mail index before migration is complete."
+ "Attempted to recreate search connection for existing connection:%@ key:%@"
+ "Attempting to access mail data before migration is complete"
+ "Attempting to access mail in unexpected dataclass: %@"
+ "B64@0:8^{__SI=}16@24@32@40@48@56"
+ "CSSearchClientConnection bundleID:%@, protectionClass:%@, conn:%@"
+ "CX expired"
+ "CX expiring"
+ "Can't open index as part of readying the index, dataclass:%@"
+ "ClassCData"
+ "Client %@ attempted to query mail data in class A"
+ "Cloned the index for mail migration"
+ "Couldn't clean up existing mail index for mail migration: %@"
+ "CrystalEMailCleanClassAComplete.touch"
+ "CrystalEMailCleanClassMailComplete.touch"
+ "CrystalEMailCloneComplete.touch"
+ "CrystalEMailFileTransferComplete.touch"
+ "CrystalEMailMigrationComplete.touch"
+ "Deleted %lu class A items for mail migration"
+ "Deleted %lu mail items for mail migration"
+ "Error creating historical reports directory: %@"
+ "Error deleting mail items for mail migration query: %@"
+ "Error deleting non-mail items for mail migration query: %@"
+ "Error parsing remaining disk space"
+ "Fail to save app usage report. Error: %@"
+ "Failed to clone index from:%@ to:%@ error:%@"
+ "Failed to clone the index for mail migration: %d"
+ "Failed to expire restartAttachmentImport task with error: %@"
+ "Failed to mark migration step as complete: %@"
+ "Index open, result:%d, dataclass:%@, shouldReindexAll:%@, forcePC:%@ createCount:%lu"
+ "M"
+ "Mail"
+ "Mail migration completed successfully"
+ "Migration step failed, result:%d, step:%@"
+ "Migration step succeeded: %@"
+ "MobileMailIndex"
+ "Opened class A index for mail migration"
+ "Opened mail index for mail migration"
+ "Opening class A index for mail migration failed: %d"
+ "Opening mail index for mail migration failed: %d"
+ "Perfoming mail migration step %@"
+ "Performing mail migration step %@"
+ "Previous step failed for mail migration %@"
+ "SPHistoricalReport"
+ "SPHistoricalReportManager"
+ "Skipping open of CX Locked index for dataclass:%@ on locked device, unlocked:%d (%d:%d)"
+ "Slow client state fetch reply by %f seconds"
+ "T@\"NSDate\",&,V_timestamp"
+ "T@\"NSDictionary\",&,V_report"
+ "TB,N,V_onDemandOpen"
+ "TI,V_type"
+ "Thermal state change: %d"
+ "Thermal state initialized: %d"
+ "Throttling indexing reply for %@ by %g s (%g s) (%s) (%lu)"
+ "[%@] Failed to submit the BGST task with error: %@"
+ "[6i]"
+ "[qid=%llu] QoS _mSIQWQS: %d prio: %lld"
+ "[qid=%llu] _mSIQWQS: pRB#: %lu, pR: %@, wQO: %@"
+ "[qid=%llu] _pBWQC: uP: %@, iPB: %@"
+ "[qid=%llu] _pBWQC: uP: YES"
+ "_changeFilesToClassC:"
+ "_deleteNonMailBundlesFromClassAIndex:"
+ "_enumerateIndexersWithProtectionClasses:forBundleIds:inferSpecialIndexes:block:"
+ "_enumerateIndexersWithProtectionClasses:forQueryWithContext:forBundleIds:inferSpecialIndexes:block:"
+ "_enumerateIndexersWithProtectionClasses:inferSpecialIndexes:block:"
+ "_finishFileTransferToClassCMailIndex"
+ "_fixProtClassForClassCMailIndex"
+ "_handleAssetsCommand:"
+ "_kMDItemBundleID != \"%@\""
+ "_kMDItemBundleID!=com.apple.mobilemail && _kMDItemBundleID!=com.apple.searchd"
+ "_kMDItemIndexRankingDateSeconds=0"
+ "_mailClassCMarkFileTransferComplete"
+ "_mailClassCMarkMigrationComplete"
+ "_mailClassCResetIndexAndComplete"
+ "_moveClassAIndexToClassCMailIndex"
+ "_onDemandOpen"
+ "_pommesBundlesWithQueryContext:queryID:"
+ "_report"
+ "_reportsDirectory"
+ "_retentionDays"
+ "_startInternalQueryWithIndex:query:fetchAttributes:forBundleIds:resultsHandler:resultQueue:"
+ "_timestamp"
+ "_type"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "bulk"
+ "checkMailMigrationToClassCComplete"
+ "cleanupOldReports"
+ "cloneIndexFrom:to:"
+ "com.apple.email.SearchIndexer"
+ "com.apple.search.framework"
+ "com.apple.searchd.internal.attachmentImports.%d"
+ "com.apple.searchd.internal.bundle.deletes.%@.%d"
+ "com.apple.searchd.internal.deletes.%@.%d"
+ "com.apple.searchd.restartAttachmentImport"
+ "com.apple.searchd.restartAttachmentImport."
+ "com.apple.spotlightknowledge.historicalReports"
+ "com.appple.spotlight.thermals"
+ "completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:dataLen:completionHandler:"
+ "cxUnlocked"
+ "dataWithLength:"
+ "dateFromString:"
+ "deleteItems Query bundleID:%@ delay by %f"
+ "deleteItems Query bundleID:%@ resume immediately"
+ "deleteTouchfileForMigrationStep:"
+ "deviceCXUnlocked"
+ "dictionaryRepresentation"
+ "en_US_POSIX"
+ "endDate"
+ "fbi"
+ "fetchAllParametersForLanguages:"
+ "fetchBundleIDs:"
+ "fetchBundleIds not supported"
+ "fetchBundleIdsForProtectionClass:completionHandler:"
+ "filenameDateFormatter"
+ "finishDeleteBatchForQueryQueue:bundleID:blockTime:"
+ "getReportsForDateInterval:reportHandler:"
+ "handleAssetsCommand:"
+ "i24@0:8@16"
+ "i32@0:8@16@24"
+ "i32@0:8@16@?24"
+ "i36@0:8B16B20B24@28"
+ "i8@?0"
+ "initWithDictionary:"
+ "initWithIdentifier:"
+ "ipc"
+ "isPriority"
+ "isSpotlightUIClientBundle:"
+ "kIndexOptionManaged"
+ "kMDItemInterestingDate_Ranking=*"
+ "kSPIndexRankingDate"
+ "lengthOfBytesUsingEncoding:"
+ "localeWithLocaleIdentifier:"
+ "mailClassCFileTransferCompleteTouchFile"
+ "mailClassCIndexPath"
+ "mailClassCMigrationCompleteTouchFile"
+ "mergeWithProtectionClasses:power:inferSpecialIndexes:completionHandler:"
+ "mobile_mail_index_enabled"
+ "moveBackMailToClassA"
+ "moveMailToClassC"
+ "moveMailToClassCWithClone"
+ "moveMailToClassCWithoutClone"
+ "mutableBytes"
+ "onDemandOpen"
+ "openIndex %@: SINotifyLowspace error: %d"
+ "openIndex %@: SIOpenIndexAtPathWithCallbacks failed due to low space (ENOSPC), trying read only mode"
+ "openIndex %@: unable to send low disk space notification: %d"
+ "openIndex:shouldReindexAll:readOnly:forcePC:"
+ "performMigrationStepWithTouchfileGuard:step:"
+ "report"
+ "resourcePath"
+ "saveReport:withType:errorHandler:"
+ "setBundleIdentifier:"
+ "setByAddingObjectsFromArray:"
+ "setExpectedDuration:"
+ "setGroupConcurrencyLimit:"
+ "setGroupName:"
+ "setLocale:"
+ "setOnDemandOpen:"
+ "setPriority:"
+ "setReport:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresProtectionClass:"
+ "setRequiresUserInactivity:"
+ "setResourceIntensive:"
+ "setResources:"
+ "setTimestamp:"
+ "setTouchfileExistsForMigrationStep:"
+ "setType:"
+ "submitTaskRequest:error:"
+ "textContentSummary"
+ "timestamp"
+ "touchfileExistsForMigrationStep:"
+ "touchfilePathForMigrationStep:"
+ "updateIndexRankingDates"
+ "updateIndexRankingDates:"
+ "v116@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40@\"NSData\"48@\"NSData\"56@\"NSData\"64@\"NSData\"72@\"NSData\"80@\"NSString\"88@\"NSData\"96B104@?<v@?@\"NSError\"B>108"
+ "v16@?0d8"
+ "v20@?0@\"NSError\"8B16"
+ "v24@0:8@\"NSObject<OS_xpc_object>\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v36@0:8@16I24@?28"
+ "v40@0:8@16@24d32"
+ "v48@?0^{__CFString=}8B16B20q24q32@?<v@?>40"
+ "v88@0:8@16@24B32B36@40B48@52B60d64Q72@?80"
+ "yyyyMMdd-HHmm"
- ".."
- "/Library/Spotlight/Assets"
- "2328.7.8.5"
- "Index open, result:%d, dataclass:%@, shouldReindexAll:%@, createCount:%lu"
- "QoS _mSIQWQS: %d prio: %lld"
- "Throttling indexing reply for %@ by %g s"
- "[5i]"
- "_enumerateIndexersWithProtectionClasses:forBundleIds:inferPriorityIndex:block:"
- "_enumerateIndexersWithProtectionClasses:inferPriorityIndex:block:"
- "_pBWQC: uP: %@, iPB: %@"
- "_pBWQC: uP: YES"
- "_pommesBundlesWithQueryContext:"
- "completeIndexingItemFor:delegate:didBeginThrottle:didEndThrottle:error:live:queue:slow:startTime:completionHandler:"
- "fetchAllParametersForLanguages:resourcePath:"
- "mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:"
- "v40@?0^{__CFString=}8B16B20q24@?<v@?>32"
- "v80@0:8@16@24B32B36@40B48@52B60d64@?72"

```
