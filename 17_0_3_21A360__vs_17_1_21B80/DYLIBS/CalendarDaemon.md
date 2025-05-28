## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1163.0.0.1.0
-  __TEXT.__text: 0x6101c
-  __TEXT.__auth_stubs: 0x3400
-  __TEXT.__objc_methlist: 0x4270
-  __TEXT.__cstring: 0x606a
+1163.1.1.3.0
+  __TEXT.__text: 0x627fc
+  __TEXT.__auth_stubs: 0x3440
+  __TEXT.__objc_methlist: 0x4348
+  __TEXT.__cstring: 0x666c
   __TEXT.__const: 0x78
-  __TEXT.__oslogstring: 0x76e4
-  __TEXT.__gcc_except_tab: 0x15b0
+  __TEXT.__oslogstring: 0x76e8
+  __TEXT.__gcc_except_tab: 0x15bc
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x167c
-  __TEXT.__objc_classname: 0x112e
-  __TEXT.__objc_methname: 0xc933
-  __TEXT.__objc_methtype: 0x5a1d
-  __TEXT.__objc_stubs: 0x83e0
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__const: 0x1ae8
-  __DATA_CONST.__objc_classlist: 0x320
+  __TEXT.__unwind_info: 0x16ac
+  __TEXT.__objc_classname: 0x118c
+  __TEXT.__objc_methname: 0xc9d9
+  __TEXT.__objc_methtype: 0x5a40
+  __TEXT.__objc_stubs: 0x84a0
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x1b28
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x107c0
-  __DATA_CONST.__objc_selrefs: 0x2988
+  __DATA_CONST.__objc_const: 0x11128
+  __DATA_CONST.__objc_selrefs: 0x29b8
   __DATA_CONST.__objc_arraydata: 0x340
-  __AUTH_CONST.__objc_const: 0x2998
-  __AUTH_CONST.__cfstring: 0x6ba0
-  __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__objc_const: 0x2a70
+  __AUTH_CONST.__cfstring: 0x7100
+  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x1a10
-  __AUTH.__objc_data: 0xbe0
+  __AUTH_CONST.__auth_got: 0x1a30
+  __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0xa38
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x548
+  __DATA.__objc_classrefs: 0x570
   __DATA.__objc_superrefs: 0x210
-  __DATA.__objc_ivar: 0x604
+  __DATA.__objc_ivar: 0x60c
   __DATA.__data: 0x1430
-  __DATA.__bss: 0x108
+  __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x1360
   __DATA_DIRTY.__bss: 0x148
   __DATA_DIRTY.__common: 0x28

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1751
-  Symbols:   7752
-  CStrings:  4021
+  Functions: 1777
+  Symbols:   7873
+  CStrings:  4077
 
Symbols:
+ +[CADSpotlightLogger _logWithFormat:args:prependErrorMarker:]
+ +[CADSpotlightLogger log:]
+ +[CADSpotlightLogger logError:]
+ +[CalDAVTrafficLogScrubber log]
+ +[CalDAVTrafficLogScrubber redactLog:toOutputFile:context:]
+ +[CalDAVTrafficLogScrubber setSortICSDocuments:]
+ +[CalDAVTrafficLogScrubber sortICSDocuments]
+ -[CADDiagnosticsCalDAVSpotlightLogCollector .cxx_destruct]
+ -[CADDiagnosticsCalDAVSpotlightLogCollector collect:]
+ -[CADDiagnosticsCalDAVSpotlightLogCollector determineExpectedOutputFiles:]
+ -[CADDiagnosticsCalDAVSpotlightLogCollector findAllLogFiles:]
+ -[CADDiagnosticsCalDAVSpotlightLogCollector parseFilenameDates:context:]
+ -[CADDiagnosticsCalDAVSpotlightLogCollector sortAndTrimLogFiles:context:]
+ -[CADDiagnosticsCalDAVTrafficLogCollector .cxx_destruct]
+ -[CADDiagnosticsCalDAVTrafficLogCollector collect:]
+ -[CADDiagnosticsCalDAVTrafficLogCollector determineExpectedOutputFiles:]
+ -[CADDiagnosticsCalDAVTrafficLogCollector findAllLogFiles:]
+ -[CADDiagnosticsCalDAVTrafficLogCollector parseFilenameDates:context:]
+ -[CADDiagnosticsCalDAVTrafficLogCollector sortAndTrimLogFiles:context:]
+ -[CADSpotlightIndexer _fullReindexIfAllowedWithTransaction:reason:]
+ -[CADSpotlightIndexer _fullReindexWithReason:]
+ -[CADStateDumpModule _storeTypeStringFromType:]
+ -[CADStateDumpModule activate]
+ -[CADStateDumpModule deactivate]
+ -[CADStateDumpModule didRegisterForAlarms]
+ -[CADStateDumpModule protectedDataDidBecomeAvailable]
+ -[CADStateDumpModule receivedAlarmNamed:]
+ -[CADStateDumpModule receivedNotificationNamed:]
+ -[CADStateDumpModule registerForStateCapture]
+ -[CalDAVTrafficLogScrubber .cxx_destruct]
+ -[CalDAVTrafficLogScrubber cleanUp]
+ -[CalDAVTrafficLogScrubber compressFileAt:to:]
+ -[CalDAVTrafficLogScrubber compressFileAt:to:].cold.1
+ -[CalDAVTrafficLogScrubber compressFileAt:to:].cold.2
+ -[CalDAVTrafficLogScrubber compressFileAt:to:].cold.3
+ -[CalDAVTrafficLogScrubber context]
+ -[CalDAVTrafficLogScrubber decompressedInputFile]
+ -[CalDAVTrafficLogScrubber decompressedInputFile].cold.1
+ -[CalDAVTrafficLogScrubber decompressedInputFile].cold.2
+ -[CalDAVTrafficLogScrubber decompressedInputFile].cold.3
+ -[CalDAVTrafficLogScrubber init]
+ -[CalDAVTrafficLogScrubber inputURL]
+ -[CalDAVTrafficLogScrubber outputURL]
+ -[CalDAVTrafficLogScrubber scrub]
+ -[CalDAVTrafficLogScrubber scrub].cold.1
+ -[CalDAVTrafficLogScrubber scrub].cold.2
+ -[CalDAVTrafficLogScrubber setContext:]
+ -[CalDAVTrafficLogScrubber setInputURL:]
+ -[CalDAVTrafficLogScrubber setOutputURL:]
+ -[CalDAVTrafficLogScrubber temporaryUncompressedFile]
+ -[ClientConnection addressURLIsAccountOwner:]
+ _CalDatabaseCopyStoreForBirthdayCalendar
+ _CalStoreCopyDefaultAlarmOffset
+ _DACPLoggingAddCustomLogFile
+ _DACPLoggingAppendDataToLogFile
+ _OBJC_CLASS_$_CADDiagnosticsCalDAVSpotlightLogCollector
+ _OBJC_CLASS_$_CADDiagnosticsCalDAVTrafficLogCollector
+ _OBJC_CLASS_$_CADSpotlightLogger
+ _OBJC_CLASS_$_CADStateDumpModule
+ _OBJC_CLASS_$_CDBDefaultAccountInfo
+ _OBJC_CLASS_$_CalDAVTrafficLogScrubber
+ _OBJC_CLASS_$_DABehaviorOptions
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_IVAR_$_CADDiagnosticsCalDAVSpotlightLogCollector._orderedInputURLs
+ _OBJC_IVAR_$_CADDiagnosticsCalDAVSpotlightLogCollector._orderedOutputURLs
+ _OBJC_IVAR_$_CADDiagnosticsCalDAVTrafficLogCollector._orderedInputURLs
+ _OBJC_IVAR_$_CADDiagnosticsCalDAVTrafficLogCollector._orderedOutputURLs
+ _OBJC_IVAR_$_CalDAVTrafficLogScrubber._context
+ _OBJC_IVAR_$_CalDAVTrafficLogScrubber._inputURL
+ _OBJC_IVAR_$_CalDAVTrafficLogScrubber._outputURL
+ _OBJC_IVAR_$_CalDAVTrafficLogScrubber._urlsToCleanUp
+ _OBJC_METACLASS_$_CADDiagnosticsCalDAVSpotlightLogCollector
+ _OBJC_METACLASS_$_CADDiagnosticsCalDAVTrafficLogCollector
+ _OBJC_METACLASS_$_CADSpotlightLogger
+ _OBJC_METACLASS_$_CADStateDumpModule
+ _OBJC_METACLASS_$_CalDAVTrafficLogScrubber
+ __OBJC_$_CLASS_METHODS_CADSpotlightLogger
+ __OBJC_$_CLASS_METHODS_CalDAVTrafficLogScrubber
+ __OBJC_$_CLASS_PROP_LIST_CalDAVTrafficLogScrubber
+ __OBJC_$_INSTANCE_METHODS_CADDiagnosticsCalDAVSpotlightLogCollector
+ __OBJC_$_INSTANCE_METHODS_CADDiagnosticsCalDAVTrafficLogCollector
+ __OBJC_$_INSTANCE_METHODS_CADStateDumpModule
+ __OBJC_$_INSTANCE_METHODS_CalDAVTrafficLogScrubber
+ __OBJC_$_INSTANCE_VARIABLES_CADDiagnosticsCalDAVSpotlightLogCollector
+ __OBJC_$_INSTANCE_VARIABLES_CADDiagnosticsCalDAVTrafficLogCollector
+ __OBJC_$_INSTANCE_VARIABLES_CalDAVTrafficLogScrubber
+ __OBJC_$_PROP_LIST_CADDiagnosticsCalDAVSpotlightLogCollector
+ __OBJC_$_PROP_LIST_CADDiagnosticsCalDAVTrafficLogCollector
+ __OBJC_$_PROP_LIST_CADStateDumpModule
+ __OBJC_$_PROP_LIST_CalDAVTrafficLogScrubber
+ __OBJC_CLASS_PROTOCOLS_$_CADDiagnosticsCalDAVSpotlightLogCollector
+ __OBJC_CLASS_PROTOCOLS_$_CADDiagnosticsCalDAVTrafficLogCollector
+ __OBJC_CLASS_PROTOCOLS_$_CADStateDumpModule
+ __OBJC_CLASS_RO_$_CADDiagnosticsCalDAVSpotlightLogCollector
+ __OBJC_CLASS_RO_$_CADDiagnosticsCalDAVTrafficLogCollector
+ __OBJC_CLASS_RO_$_CADSpotlightLogger
+ __OBJC_CLASS_RO_$_CADStateDumpModule
+ __OBJC_CLASS_RO_$_CalDAVTrafficLogScrubber
+ __OBJC_METACLASS_RO_$_CADDiagnosticsCalDAVSpotlightLogCollector
+ __OBJC_METACLASS_RO_$_CADDiagnosticsCalDAVTrafficLogCollector
+ __OBJC_METACLASS_RO_$_CADSpotlightLogger
+ __OBJC_METACLASS_RO_$_CADStateDumpModule
+ __OBJC_METACLASS_RO_$_CalDAVTrafficLogScrubber
+ ___103-[CADXPCImplementation(CADDatabaseOperationGroup) CADDatabaseMigrateSubscribedCalendar:toSource:reply:]_block_invoke.39
+ ___142-[CADXPCImplementation(CADDatabaseOperationGroup) CADDatabaseCommitDeletes:updatesAndInserts:options:andFetchChangesSinceTimestamp:withReply:]_block_invoke.36
+ ___30-[CADStateDumpModule activate]_block_invoke
+ ___31+[CalDAVTrafficLogScrubber log]_block_invoke
+ ___45-[CADStateDumpModule registerForStateCapture]_block_invoke
+ ___45-[CADStateDumpModule registerForStateCapture]_block_invoke_2
+ ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke
+ ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke.56
+ ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke.cold.1
+ ___61+[CADSpotlightLogger _logWithFormat:args:prependErrorMarker:]_block_invoke
+ ___61+[CADSpotlightLogger _logWithFormat:args:prependErrorMarker:]_block_invoke.19
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.121
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.121.cold.1
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.125
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.125.cold.1
+ ___64-[CADCoreSpotlightIndex indexSearchableItems:completionHandler:]_block_invoke
+ ___64-[CADCoreSpotlightIndex indexSearchableItems:completionHandler:]_block_invoke_2
+ ___67-[CADSpotlightIndexer _fullReindexIfAllowedWithTransaction:reason:]_block_invoke
+ ___71-[CADDiagnosticsCalDAVTrafficLogCollector sortAndTrimLogFiles:context:]_block_invoke
+ ___73-[CADDiagnosticsCalDAVSpotlightLogCollector sortAndTrimLogFiles:context:]_block_invoke
+ ___79-[CADCoreSpotlightIndex deleteAllSearchableItemsForBundleID:completionHandler:]_block_invoke
+ ___86-[CADCoreSpotlightIndex deleteSearchableItemsWithDomainIdentifiers:completionHandler:]_block_invoke
+ ___block_descriptor_32_e26_16?0"CSSearchableItem"8l
+ ___block_descriptor_32_e5_8?0l
+ ___block_literal_global.108
+ __logWithFormat:args:prependErrorMarker:.dateFormatter
+ __logWithFormat:args:prependErrorMarker:.onceToken
+ _activate.onceToken
+ _kCalCalendarImportIgnoreMethod
+ _kDACPLoggingCustomLogFileLevelDefaultsKeyKey
+ _kDACPLoggingCustomLogNameKey
+ _kDACPLoggingCustomMaxConsoleLevelKey
+ _kDACPLoggingCustomMaxLogFileLevelKey
+ _objc_msgSend$DAManagedDefaultForKey:
+ _objc_msgSend$_fullReindexIfAllowedWithTransaction:reason:
+ _objc_msgSend$_fullReindexWithReason:
+ _objc_msgSend$_logWithFormat:args:prependErrorMarker:
+ _objc_msgSend$addressIsAccountOwner:
+ _objc_msgSend$initWithStore:
+ _objc_msgSend$isAppleInternalInstall
+ _objc_msgSend$setFormatOptions:
- +[CalDAVLogScrubber log]
- +[CalDAVLogScrubber redactLog:toOutputFile:context:]
- +[CalDAVLogScrubber setSortICSDocuments:]
- +[CalDAVLogScrubber sortICSDocuments]
- -[CADDiagnosticsCalDAVLogCollector .cxx_destruct]
- -[CADDiagnosticsCalDAVLogCollector collect:]
- -[CADDiagnosticsCalDAVLogCollector determineExpectedOutputFiles:]
- -[CADDiagnosticsCalDAVLogCollector findAllLogFiles:]
- -[CADDiagnosticsCalDAVLogCollector parseFilenameDates:context:]
- -[CADDiagnosticsCalDAVLogCollector sortAndTrimLogFiles:context:]
- -[CADServer _storeTypeStringFromType:]
- -[CADServer registerForStateCapture]
- -[CADSpotlightIndexer _fullReindexIfAllowedWithTransaction:]
- -[CADSpotlightIndexer _fullReindex]
- -[CalDAVLogScrubber .cxx_destruct]
- -[CalDAVLogScrubber cleanUp]
- -[CalDAVLogScrubber compressFileAt:to:]
- -[CalDAVLogScrubber compressFileAt:to:].cold.1
- -[CalDAVLogScrubber compressFileAt:to:].cold.2
- -[CalDAVLogScrubber compressFileAt:to:].cold.3
- -[CalDAVLogScrubber context]
- -[CalDAVLogScrubber decompressedInputFile]
- -[CalDAVLogScrubber decompressedInputFile].cold.1
- -[CalDAVLogScrubber decompressedInputFile].cold.2
- -[CalDAVLogScrubber decompressedInputFile].cold.3
- -[CalDAVLogScrubber init]
- -[CalDAVLogScrubber inputURL]
- -[CalDAVLogScrubber outputURL]
- -[CalDAVLogScrubber scrub]
- -[CalDAVLogScrubber scrub].cold.1
- -[CalDAVLogScrubber scrub].cold.2
- -[CalDAVLogScrubber setContext:]
- -[CalDAVLogScrubber setInputURL:]
- -[CalDAVLogScrubber setOutputURL:]
- -[CalDAVLogScrubber temporaryUncompressedFile]
- _OBJC_CLASS_$_CADDiagnosticsCalDAVLogCollector
- _OBJC_CLASS_$_CalDAVLogScrubber
- _OBJC_IVAR_$_CADDiagnosticsCalDAVLogCollector._orderedInputURLs
- _OBJC_IVAR_$_CADDiagnosticsCalDAVLogCollector._orderedOutputURLs
- _OBJC_IVAR_$_CalDAVLogScrubber._context
- _OBJC_IVAR_$_CalDAVLogScrubber._inputURL
- _OBJC_IVAR_$_CalDAVLogScrubber._outputURL
- _OBJC_IVAR_$_CalDAVLogScrubber._urlsToCleanUp
- _OBJC_METACLASS_$_CADDiagnosticsCalDAVLogCollector
- _OBJC_METACLASS_$_CalDAVLogScrubber
- __OBJC_$_CLASS_METHODS_CalDAVLogScrubber
- __OBJC_$_CLASS_PROP_LIST_CalDAVLogScrubber
- __OBJC_$_INSTANCE_METHODS_CADDiagnosticsCalDAVLogCollector
- __OBJC_$_INSTANCE_METHODS_CalDAVLogScrubber
- __OBJC_$_INSTANCE_VARIABLES_CADDiagnosticsCalDAVLogCollector
- __OBJC_$_INSTANCE_VARIABLES_CalDAVLogScrubber
- __OBJC_$_PROP_LIST_CADDiagnosticsCalDAVLogCollector
- __OBJC_$_PROP_LIST_CalDAVLogScrubber
- __OBJC_CLASS_PROTOCOLS_$_CADDiagnosticsCalDAVLogCollector
- __OBJC_CLASS_RO_$_CADDiagnosticsCalDAVLogCollector
- __OBJC_CLASS_RO_$_CalDAVLogScrubber
- __OBJC_METACLASS_RO_$_CADDiagnosticsCalDAVLogCollector
- __OBJC_METACLASS_RO_$_CalDAVLogScrubber
- ___103-[CADXPCImplementation(CADDatabaseOperationGroup) CADDatabaseMigrateSubscribedCalendar:toSource:reply:]_block_invoke.38
- ___142-[CADXPCImplementation(CADDatabaseOperationGroup) CADDatabaseCommitDeletes:updatesAndInserts:options:andFetchChangesSinceTimestamp:withReply:]_block_invoke.34
- ___24+[CalDAVLogScrubber log]_block_invoke
- ___35-[CADSpotlightIndexer _fullReindex]_block_invoke
- ___35-[CADSpotlightIndexer _fullReindex]_block_invoke.42
- ___35-[CADSpotlightIndexer _fullReindex]_block_invoke.cold.1
- ___36-[CADServer registerForStateCapture]_block_invoke
- ___60-[CADSpotlightIndexer _fullReindexIfAllowedWithTransaction:]_block_invoke
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.90
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.90.cold.1
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.91
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.91.cold.1
- ___64-[CADDiagnosticsCalDAVLogCollector sortAndTrimLogFiles:context:]_block_invoke
- ___block_literal_global.151
- _objc_msgSend$_fullReindex
- _objc_msgSend$_fullReindexIfAllowedWithTransaction:
CStrings:
+ "%@ %@\n"
+ "%@ SPOTLIGHT_ERROR %@\n"
+ "%@, %@"
+ "@16@?0@\"CSSearchableItem\"8"
+ "Asking %@ to determine what logs it will produce"
+ "B24@0:8@\"NSURL\"16"
+ "Beginning spotlight re-index for all databases: %@"
+ "CADDiagnosticsCalDAVSpotlightLogCollector"
+ "CADDiagnosticsCalDAVTrafficLogCollector"
+ "CADSpotlightLogger"
+ "CADStateDumpModule"
+ "CalDAVTrafficLogScrubber"
+ "CalDAVTrafficLogScrubber.m"
+ "DALogLevel"
+ "DAManagedDefaultForKey:"
+ "Failed to push spotlight deletes for domain ids: %@"
+ "Failed to push spotlight deletes for ids before indexing: %@"
+ "Found %lu spotlight logs"
+ "Including %lu spotlight logs"
+ "No"
+ "None"
+ "Skipping record because we got a nil domain id"
+ "SpotlightLog"
+ "Too many spotlight logs; only including the most recent %i"
+ "Unable to find spotlight logs: %@"
+ "Yes"
+ "[UserStateLog] Default Alerts Per Device (iOS, macOS Local Source)"
+ "_fullReindexIfAllowedWithTransaction:reason:"
+ "_fullReindexWithReason:"
+ "_logWithFormat:args:prependErrorMarker:"
+ "addressURLIsAccountOwner:"
+ "com.apple.mobilecal.CalDAVTrafficLogScrubber.attributeDedupingQueue"
+ "com.apple.mobilecal.CalDAVTrafficLogScrubber.elementDedupingQueue"
+ "defaultAllDayAlarm"
+ "defaultBirthdayAlarm"
+ "defaultTimedAlarm"
+ "error deleting searchable items for calendar: %@"
+ "error fetching changes: %d"
+ "error while attemping full reindex, writing error pref"
+ "finished _fullReindexWithReason: %@"
+ "finished deleteAllSearchableItemsForBundleID"
+ "finished deleteAllSearchableItemsForBundleID: %@"
+ "finished deleteSearchableItemsWithDomainIdentifiers"
+ "finished deleteSearchableItemsWithDomainIdentifiers: %@"
+ "finished indexSearchableItems"
+ "finished indexSearchableItems: %@"
+ "ignoreAlerts"
+ "initWithStore:"
+ "isAppleInternalInstall"
+ "setFormatOptions:"
+ "started _fullReindexWithReason: %@"
+ "started deleteAllSearchableItemsForBundleID: %@"
+ "started deleteSearchableItemsWithDomainIdentifiers: %@"
+ "started indexSearchableItems: %@"
+ "timeToLeave"
+ "ttlLocationDisabled"
+ "v36@0:8@16*24B32"
- "Asking %@ to detemine what logs it will produce"
- "Beginning spotlight re-index for all databases"
- "CADDiagnosticsCalDAVLogCollector"
- "CalDAVLogScrubber"
- "CalDAVLogScrubber.m"
- "_fullReindex"
- "_fullReindexIfAllowedWithTransaction:"
- "com.apple.mobilecal.CalDAVLogScrubber.attributeDedupingQueue"
- "com.apple.mobilecal.CalDAVLogScrubber.elementDedupingQueue"

```
