## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1224.3.1.0.0
-  __TEXT.__text: 0x73290
+1224.4.11.0.0
+  __TEXT.__text: 0x79c28
   __TEXT.__auth_stubs: 0x3830
-  __TEXT.__objc_methlist: 0x62ac
-  __TEXT.__cstring: 0x70f4
-  __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0x845a
-  __TEXT.__gcc_except_tab: 0x1c7c
+  __TEXT.__objc_methlist: 0x67b4
+  __TEXT.__cstring: 0x7405
+  __TEXT.__const: 0x180
+  __TEXT.__oslogstring: 0x8d5f
+  __TEXT.__gcc_except_tab: 0x1cbc
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1b68
-  __TEXT.__objc_classname: 0x14b1
-  __TEXT.__objc_methname: 0xed47
-  __TEXT.__objc_methtype: 0x6972
-  __TEXT.__objc_stubs: 0x9d60
-  __DATA_CONST.__got: 0x9f0
-  __DATA_CONST.__const: 0x2080
-  __DATA_CONST.__objc_classlist: 0x400
+  __TEXT.__unwind_info: 0x1d98
+  __TEXT.__objc_classname: 0x1504
+  __TEXT.__objc_methname: 0xfd43
+  __TEXT.__objc_methtype: 0x6ea6
+  __TEXT.__objc_stubs: 0xa700
+  __DATA_CONST.__got: 0xa00
+  __DATA_CONST.__const: 0x2200
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31b0
+  __DATA_CONST.__objc_selrefs: 0x3458
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2b0
+  __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x350
   __AUTH_CONST.__auth_got: 0x1c28
-  __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x7ac0
-  __AUTH_CONST.__objc_const: 0xc478
+  __AUTH_CONST.__const: 0x8a0
+  __AUTH_CONST.__cfstring: 0x7d40
+  __AUTH_CONST.__objc_const: 0xcbd0
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1450
+  __AUTH.__objc_data: 0x1540
   __AUTH.__data: 0xa50
-  __DATA.__objc_ivar: 0x7c8
+  __DATA.__objc_ivar: 0x838
   __DATA.__data: 0x1728
   __DATA.__bss: 0x198
   __DATA.__common: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 23D13490-7D09-3ED9-AB47-32786372767B
-  Functions: 2181
-  Symbols:   9060
-  CStrings:  5617
+  UUID: 29D1F0F8-5FD5-39B8-B91B-C05EE102AB6D
+  Functions: 2319
+  Symbols:   9523
+  CStrings:  5842
 
Symbols:
+ +[CADDatabaseConnectionPoolManager defaultManager]
+ +[CADDatabaseConnectionPoolManager defaultManager].cold.1
+ +[CADIndexState fullReindexState]
+ +[CADIndexState incrementalState]
+ +[CADIndexState reindexingCalendarsStateWithDeleteBeforeIndexing:]
+ +[CADIndexState reindexingEventsStateWithDatabase:lastProcessedRowID:]
+ +[CADSpotlightIndexer _spotlightDomainIDWithBundleID:personaID:storeID:calendarID:eventID:forIndexedEntityType:]
+ +[CADSpotlightIndexer _spotlightDomainIDWithBundleID:personaID:storeID:calendarID:eventID:forIndexedEntityType:].cold.1
+ +[CADSpotlightIndexer _typeLabelsForReindexingEvents:calendars:]
+ +[CADSpotlightIndexer expectedClientState]
+ +[CADSpotlightIndexer spotlightUniqueIDForCalendar:]
+ +[CADSpotlightIndexer spotlightUniqueIDForEvent:occurrenceDate:]
+ +[CADSpotlightUpsertContext _sendSpotlightUpdates:deletes:toIndex:]
+ -[CADCoreSpotlightIndex fetchLastClientStateWithCompletionHandler:]
+ -[CADCoreSpotlightIndex reportDonationProgressWithAllKnownItems:itemsNeedingDonation:completionHandler:]
+ -[CADCoreSpotlightIndexProvider donateCalendars]
+ -[CADDatabaseInitializationOptions(Internal) databaseInitializationConfig]
+ -[CADDatabaseInitializationOptions(Internal) initWithDatabaseConfiguration:]
+ -[CADDatabaseInitializationOptions(Internal) purifyOptions]
+ -[CADDatabaseInitializationOptions(Internal) validOptionsForConnection:]
+ -[CADFullLoggingSpotlightIndex fetchLastClientStateWithCompletionHandler:]
+ -[CADFullLoggingSpotlightIndex reportDonationProgressWithAllKnownItems:itemsNeedingDonation:completionHandler:]
+ -[CADFullLoggingSpotlightIndexProvider donateCalendars]
+ -[CADIndexState description]
+ -[CADIndexState hash]
+ -[CADIndexState initWithData:]
+ -[CADIndexState initWithState:databaseID:lastProcessedRowID:deleteBeforeIndexing:]
+ -[CADIndexState isEqual:]
+ -[CADIndexState isReindexing]
+ -[CADIndexState redactedDescription]
+ -[CADIndexState reindexingCalendarsDeleteBeforeIndexing]
+ -[CADIndexState reindexingEventsDatabaseID]
+ -[CADIndexState reindexingEventsLastProcessedRowID]
+ -[CADIndexState serializedData]
+ -[CADIndexState state]
+ -[CADMockSpotlightIndex fetchLastClientStateWithCompletionHandler:]
+ -[CADMockSpotlightIndex reportDonationProgressWithAllKnownItems:itemsNeedingDonation:completionHandler:]
+ -[CADMockSpotlightIndexProvider _incrementAndCheckIfShouldFailCall]
+ -[CADMockSpotlightIndexProvider batchAPIMisuseCallback]
+ -[CADMockSpotlightIndexProvider clientState]
+ -[CADMockSpotlightIndexProvider donateCalendars]
+ -[CADMockSpotlightIndexProvider itemsInIndexPassingTest:]
+ -[CADMockSpotlightIndexProvider setBatchAPIMisuseCallback:]
+ -[CADMockSpotlightIndexProvider setClientState:]
+ -[CADMockSpotlightIndexProvider setDonateCalendars:]
+ -[CADSpotlightDefaults .cxx_destruct]
+ -[CADSpotlightDefaults dataPreferenceValueForKey:]
+ -[CADSpotlightDefaults datePreferenceValueForKey:]
+ -[CADSpotlightDefaults initWithDefaults:]
+ -[CADSpotlightDefaults init]
+ -[CADSpotlightDefaults intPreferenceValueForKey:]
+ -[CADSpotlightDefaults lastABCReport]
+ -[CADSpotlightDefaults lastReindexStartDate]
+ -[CADSpotlightDefaults lastSpotlightIndexCalendarsVersion]
+ -[CADSpotlightDefaults lastSpotlightIndexEventsVersion]
+ -[CADSpotlightDefaults reindexState]
+ -[CADSpotlightDefaults reindexesStartedWithoutProgress]
+ -[CADSpotlightDefaults reindexingInProgress]
+ -[CADSpotlightDefaults setLastABCReport:]
+ -[CADSpotlightDefaults setLastABCReportAtDate:]
+ -[CADSpotlightDefaults setLastReindexStartDate:]
+ -[CADSpotlightDefaults setLastSpotlightIndexCalendarsVersion:]
+ -[CADSpotlightDefaults setLastSpotlightIndexEventsVersion:]
+ -[CADSpotlightDefaults setReindexState:]
+ -[CADSpotlightDefaults setReindexesStartedWithoutProgress:]
+ -[CADSpotlightIndexer _addCommonCalendarAttributesToSet:forCalendar:]
+ -[CADSpotlightIndexer _advanceReindexingWithState:]
+ -[CADSpotlightIndexer _advanceReindexingWithState:].cold.1
+ -[CADSpotlightIndexer _checkForAndReportPastSpotlightMigrationErrorsAndReindexIfNeeded]
+ -[CADSpotlightIndexer _checkForAndReportPastSpotlightMigrationErrorsAndReindexIfNeeded].cold.1
+ -[CADSpotlightIndexer _commonReindexPreambleWithState:]
+ -[CADSpotlightIndexer _commonReindexPreambleWithState:].cold.1
+ -[CADSpotlightIndexer _continueReindexWithState:]
+ -[CADSpotlightIndexer _continueReindexWithState:].cold.1
+ -[CADSpotlightIndexer _continueReindexWithState:].cold.2
+ -[CADSpotlightIndexer _continueReindexWithState:].cold.3
+ -[CADSpotlightIndexer _continueReindexWithState:].cold.4
+ -[CADSpotlightIndexer _continueReindexWithState:].cold.5
+ -[CADSpotlightIndexer _continueReindexWithState:].cold.6
+ -[CADSpotlightIndexer _countTotalSpotlightDonationItems]
+ -[CADSpotlightIndexer _deleteEverythingFromSpotlightForFullReindex]
+ -[CADSpotlightIndexer _deleteEverythingFromSpotlightForFullReindex].cold.1
+ -[CADSpotlightIndexer _deleteFromIndex:index:]
+ -[CADSpotlightIndexer _enumerateDatabasesWithBlockingCalls:]
+ -[CADSpotlightIndexer _enumerateDatabasesWithoutBlockingCalls:]
+ -[CADSpotlightIndexer _fullCalendarsReindexWithDeleteFirst:]
+ -[CADSpotlightIndexer _fullCalendarsReindexWithDeleteFirst:].cold.1
+ -[CADSpotlightIndexer _fullReindexOfEvents:calendars:withReason:]
+ -[CADSpotlightIndexer _fullReindexOfEvents:calendars:withReason:].cold.1
+ -[CADSpotlightIndexer _fullReindexOfEvents:calendars:withReason:].cold.2
+ -[CADSpotlightIndexer _fullReindexOfEvents:calendars:withReason:].cold.3
+ -[CADSpotlightIndexer _incrementalReindexEventsWithState:]
+ -[CADSpotlightIndexer _loadCurrentReindexState]
+ -[CADSpotlightIndexer _nextDatabaseIDAfterDatabaseID:]
+ -[CADSpotlightIndexer _personaID:]
+ -[CADSpotlightIndexer _personaID:].cold.1
+ -[CADSpotlightIndexer _pushBatchedUpdatesForEventsWithUUIDs:calendarsWithUUIDs:database:personaID:deleteBeforeInserting:]
+ -[CADSpotlightIndexer _pushUpdatesForEventsWithUUIDs:calendarsWithUUIDs:database:personaID:deleteBeforeInserting:]
+ -[CADSpotlightIndexer _pushUpdatesForEventsWithUUIDs:calendarsWithUUIDs:inBatchesOf:database:personaID:deleteBeforeInserting:]
+ -[CADSpotlightIndexer _pushUpdatesForEventsWithUUIDs:calendarsWithUUIDs:inBatchesOf:database:personaID:deleteBeforeInserting:].cold.1
+ -[CADSpotlightIndexer _reportDonationCountWithAllKnownItems:itemsNeedingDonation:]
+ -[CADSpotlightIndexer _reportDonationProgressForChange]
+ -[CADSpotlightIndexer _resumeQueue]
+ -[CADSpotlightIndexer _saveIndexState:]
+ -[CADSpotlightIndexer _spotlightItemAttributesForCalendar:]
+ -[CADSpotlightIndexer _spotlightItemAttributesForEvent:]
+ -[CADSpotlightIndexer _startPendingReindexIfAllowed]
+ -[CADSpotlightIndexer _updateRetryReindexDate]
+ -[CADSpotlightIndexer _upsertCalendar:withDomainID:context:]
+ -[CADSpotlightIndexer _upsertCalendar:withDomainID:context:].cold.1
+ -[CADSpotlightIndexer _upsertCalendar:withDomainID:context:].cold.2
+ -[CADSpotlightIndexer _upsertEvent:withDomainID:context:]
+ -[CADSpotlightIndexer _upsertEvent:withDomainID:context:].cold.1
+ -[CADSpotlightIndexer _upsertEvent:withDomainID:context:].cold.2
+ -[CADSpotlightIndexer _upsertToIndex:inDatabase:personaID:deleteBeforeInserting:index:]
+ -[CADSpotlightIndexer addToDomainIdsToDelete:forChangeDict:entityType:database:personaID:donateCalendars:]
+ -[CADSpotlightIndexer addToDomainIdsToDelete:forChangeDict:entityType:database:personaID:donateCalendars:].cold.1
+ -[CADSpotlightIndexer addToDomainIdsToDelete:forChangeDict:entityType:database:personaID:donateCalendars:].cold.2
+ -[CADSpotlightIndexer addToEntitiesToIndex:forChangeDict:entityType:modifiedObjectID:database:donateCalendars:]
+ -[CADSpotlightIndexer addToEntitiesToIndex:forChangeDict:entityType:modifiedObjectID:database:donateCalendars:].cold.1
+ -[CADSpotlightIndexer dealloc]
+ -[CADSpotlightIndexer now]
+ -[CADSpotlightIndexer protectedDataAvailable]
+ -[CADSpotlightIndexer setNow:]
+ -[CADSpotlightMockDefaults setObjectCallback]
+ -[CADSpotlightMockDefaults setSetObjectCallback:]
+ -[CADSpotlightUpsertContext .cxx_destruct]
+ -[CADSpotlightUpsertContext addIdToRemove:]
+ -[CADSpotlightUpsertContext addItemToIndex:]
+ -[CADSpotlightUpsertContext database]
+ -[CADSpotlightUpsertContext deleteBeforeInserting]
+ -[CADSpotlightUpsertContext donateCalendars]
+ -[CADSpotlightUpsertContext flushBatch]
+ -[CADSpotlightUpsertContext index]
+ -[CADSpotlightUpsertContext initWithDatabase:indexProvider:personaID:deleteBeforeInserting:recordCount:batchSize:index:]
+ -[CADSpotlightUpsertContext isBatchFull]
+ -[CADSpotlightUpsertContext nlCalendarID]
+ -[CADSpotlightUpsertContext now]
+ -[CADSpotlightUpsertContext oneYearFromNow]
+ -[CADSpotlightUpsertContext personaID]
+ -[CADSpotlightUpsertContext sixMonthsFromNow]
+ GCC_except_table101
+ GCC_except_table38
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table62
+ _CalDatabaseCopyCalendarWithUUID
+ _CalDatabaseCopyEventUUIDsBatched
+ _CalDatabaseGetChangeCountForClientExcludingDeletes
+ _CalDatabaseGetCountOfCalendarsInStore
+ _CalEventCopyUUID
+ _CalPassthroughSpotlightAttributes
+ _OBJC_CLASS_$_CADIndexState
+ _OBJC_CLASS_$_CADSpotlightDefaults
+ _OBJC_CLASS_$_CADSpotlightUpsertContext
+ _OBJC_CLASS_$_CSDonationProgress
+ _OBJC_IVAR_$_CADIndexState._reindexingCalendarsDeleteBeforeIndexing
+ _OBJC_IVAR_$_CADIndexState._reindexingEventsDatabaseID
+ _OBJC_IVAR_$_CADIndexState._reindexingEventsLastProcessedRowID
+ _OBJC_IVAR_$_CADIndexState._state
+ _OBJC_IVAR_$_CADMockSpotlightIndex._needsReindex
+ _OBJC_IVAR_$_CADMockSpotlightIndexProvider._batchAPIMisuseCallback
+ _OBJC_IVAR_$_CADMockSpotlightIndexProvider._clientState
+ _OBJC_IVAR_$_CADMockSpotlightIndexProvider._donateCalendars
+ _OBJC_IVAR_$_CADSpotlightDefaults._lastABCReport
+ _OBJC_IVAR_$_CADSpotlightDefaults._spotlightDefaults
+ _OBJC_IVAR_$_CADSpotlightIndexer._dbConnectionProvider
+ _OBJC_IVAR_$_CADSpotlightIndexer._donationLock
+ _OBJC_IVAR_$_CADSpotlightIndexer._now
+ _OBJC_IVAR_$_CADSpotlightIndexer._personaIDCache
+ _OBJC_IVAR_$_CADSpotlightIndexer._poolConfig
+ _OBJC_IVAR_$_CADSpotlightIndexer._resumed
+ _OBJC_IVAR_$_CADSpotlightIndexer._retryReindexDate
+ _OBJC_IVAR_$_CADSpotlightMockDefaults._setObjectCallback
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._batchSize
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._database
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._deleteBeforeInserting
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._donateCalendars
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._idsToRemove
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._index
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._itemsToIndex
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._nlCalendarID
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._now
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._oneYearFromNow
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._personaID
+ _OBJC_IVAR_$_CADSpotlightUpsertContext._sixMonthsFromNow
+ _OBJC_METACLASS_$_CADIndexState
+ _OBJC_METACLASS_$_CADSpotlightDefaults
+ _OBJC_METACLASS_$_CADSpotlightUpsertContext
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_CADDatabaseConnectionPoolManager
+ __OBJC_$_CLASS_METHODS_CADIndexState
+ __OBJC_$_CLASS_METHODS_CADSpotlightUpsertContext
+ __OBJC_$_INSTANCE_METHODS_CADDatabaseInitializationOptions(Internal)
+ __OBJC_$_INSTANCE_METHODS_CADIndexState
+ __OBJC_$_INSTANCE_METHODS_CADSpotlightDefaults
+ __OBJC_$_INSTANCE_METHODS_CADSpotlightUpsertContext
+ __OBJC_$_INSTANCE_VARIABLES_CADIndexState
+ __OBJC_$_INSTANCE_VARIABLES_CADSpotlightDefaults
+ __OBJC_$_INSTANCE_VARIABLES_CADSpotlightUpsertContext
+ __OBJC_$_PROP_LIST_CADIndexState
+ __OBJC_$_PROP_LIST_CADSpotlightDefaults
+ __OBJC_$_PROP_LIST_CADSpotlightIndexProvider
+ __OBJC_$_PROP_LIST_CADSpotlightIndexer
+ __OBJC_$_PROP_LIST_CADSpotlightUpsertContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CADSpotlightDefaultsStorage
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CADSpotlightDefaultsStorage
+ __OBJC_$_PROTOCOL_REFS_CADSpotlightDefaultsStorage
+ __OBJC_CLASS_RO_$_CADIndexState
+ __OBJC_CLASS_RO_$_CADSpotlightDefaults
+ __OBJC_CLASS_RO_$_CADSpotlightUpsertContext
+ __OBJC_LABEL_PROTOCOL_$_CADSpotlightDefaultsStorage
+ __OBJC_METACLASS_RO_$_CADIndexState
+ __OBJC_METACLASS_RO_$_CADSpotlightDefaults
+ __OBJC_METACLASS_RO_$_CADSpotlightUpsertContext
+ __OBJC_PROTOCOL_$_CADSpotlightDefaultsStorage
+ ___104-[CADCoreSpotlightIndex reportDonationProgressWithAllKnownItems:itemsNeedingDonation:completionHandler:]_block_invoke
+ ___104-[CADCoreSpotlightIndex reportDonationProgressWithAllKnownItems:itemsNeedingDonation:completionHandler:]_block_invoke.cold.1
+ ___111-[CADFullLoggingSpotlightIndex reportDonationProgressWithAllKnownItems:itemsNeedingDonation:completionHandler:]_block_invoke
+ ___119-[CADSpotlightIndexer initWithDatabaseConfiguration:spotlightIndexProvider:spotlightDefaults:spotlightEntityAnnotator:]_block_invoke_2
+ ___34-[CADSpotlightIndexer _personaID:]_block_invoke
+ ___46-[CADSpotlightIndexer _deleteFromIndex:index:]_block_invoke
+ ___46-[CADSpotlightIndexer _deleteFromIndex:index:]_block_invoke.165
+ ___46-[CADSpotlightIndexer _deleteFromIndex:index:]_block_invoke.165.cold.1
+ ___46-[CADSpotlightIndexer _deleteFromIndex:index:]_block_invoke.cold.1
+ ___49-[CADSpotlightIndexer _continueReindexWithState:]_block_invoke
+ ___49-[CADSpotlightIndexer _continueReindexWithState:]_block_invoke.cold.1
+ ___50+[CADDatabaseConnectionPoolManager defaultManager]_block_invoke
+ ___54-[CADSpotlightIndexer _nextDatabaseIDAfterDatabaseID:]_block_invoke
+ ___55-[CADSpotlightIndexer _reportDonationProgressForChange]_block_invoke
+ ___56-[CADSpotlightIndexer _countTotalSpotlightDonationItems]_block_invoke
+ ___56-[CADSpotlightIndexer _spotlightItemAttributesForEvent:]_block_invoke
+ ___56-[CADSpotlightIndexer _spotlightItemAttributesForEvent:]_block_invoke.cold.1
+ ___58-[CADSpotlightIndexer _incrementalReindexEventsWithState:]_block_invoke
+ ___58-[CADSpotlightIndexer _incrementalReindexEventsWithState:]_block_invoke_2
+ ___58-[CADSpotlightIndexer _incrementalReindexEventsWithState:]_block_invoke_2.cold.1
+ ___58-[CADSpotlightIndexer _incrementalReindexEventsWithState:]_block_invoke_2.cold.2
+ ___60-[CADSpotlightIndexer _fullCalendarsReindexWithDeleteFirst:]_block_invoke
+ ___60-[CADSpotlightIndexer _fullCalendarsReindexWithDeleteFirst:]_block_invoke.123
+ ___60-[CADSpotlightIndexer _fullCalendarsReindexWithDeleteFirst:]_block_invoke_2
+ ___60-[CADSpotlightIndexer _fullCalendarsReindexWithDeleteFirst:]_block_invoke_2.124
+ ___60-[CADSpotlightIndexer _fullCalendarsReindexWithDeleteFirst:]_block_invoke_3
+ ___60-[CADSpotlightIndexer _fullCalendarsReindexWithDeleteFirst:]_block_invoke_3.cold.1
+ ___60-[CADSpotlightIndexer _fullCalendarsReindexWithDeleteFirst:]_block_invoke_3.cold.2
+ ___67+[CADSpotlightUpsertContext _sendSpotlightUpdates:deletes:toIndex:]_block_invoke
+ ___67+[CADSpotlightUpsertContext _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.413
+ ___67+[CADSpotlightUpsertContext _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.413.cold.1
+ ___67+[CADSpotlightUpsertContext _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.417
+ ___67+[CADSpotlightUpsertContext _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.417.cold.1
+ ___67+[CADSpotlightUpsertContext _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.cold.1
+ ___74-[CADFullLoggingSpotlightIndex fetchLastClientStateWithCompletionHandler:]_block_invoke
+ ___82-[CADSpotlightIndexer _reportDonationCountWithAllKnownItems:itemsNeedingDonation:]_block_invoke
+ ___82-[CADSpotlightIndexer _reportDonationCountWithAllKnownItems:itemsNeedingDonation:]_block_invoke.cold.1
+ ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke.65
+ ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke.65.cold.1
+ ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.247
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r96l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_112_e8_32s40s48s56s64r72r80r88r96r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8r64l8s56l8r72l8r80l8r88l8r96l8
+ ___block_descriptor_116_e8_32s40s48s56s64s72s80s88r96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8s64l8r88l8r96l8s72l8s80l8
+ ___block_descriptor_32_e341_B24?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16l
+ ___block_descriptor_32_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20l
+ ___block_descriptor_33_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24l
+ ___block_descriptor_36_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12l
+ ___block_descriptor_40_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20l
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8
+ ___block_descriptor_40_e8_32bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8
+ ___block_descriptor_40_e8_32bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20ls32l8
+ ___block_descriptor_40_e8_32bs_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8
+ ___block_descriptor_40_e8_32r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8
+ ___block_descriptor_40_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr32l8
+ ___block_descriptor_40_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr32l8
+ ___block_descriptor_40_e8_32s_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls32l8
+ ___block_descriptor_40_e8_32s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8
+ ___block_descriptor_40_e8_32s_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8
+ ___block_descriptor_41_e8_32r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8
+ ___block_descriptor_44_e8_32bs_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls32l8
+ ___block_descriptor_44_e8_32r_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8lr32l8
+ ___block_descriptor_44_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr32l8
+ ___block_descriptor_44_e8_32r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20lr32l8
+ ___block_descriptor_48_e8_32r40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr32l8
+ ___block_descriptor_48_e8_32s40bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"816^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8
+ ___block_descriptor_49_e8_32s40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8
+ ___block_descriptor_52_e8_32bs40r_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls32l8r40l8
+ ___block_descriptor_52_e8_32r40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8r40l8
+ ___block_descriptor_52_e8_32s40bs_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls40l8s32l8
+ ___block_descriptor_52_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr40l8s32l8
+ ___block_descriptor_56_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_56_e8_32s40bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20ls40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32r40r48r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr32l8r40l8r48l8
+ ___block_descriptor_57_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
+ ___block_descriptor_57_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40r48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40r48r56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e8_B12?0B8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e8_B12?0B8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e349_v24?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8"NSArray"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8
+ ___block_descriptor_65_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s56l8s48l8
+ ___block_descriptor_68_e8_32s40r48r_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls32l8r40l8r48l8
+ ___block_descriptor_68_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8
+ ___block_descriptor_68_e8_32s40s48s56s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8r64l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr48l8r56l8s32l8s40l8r64l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8r64l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r56l8r64l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_76_e8_32s40r48r_e8_B12?0B8lr40l8s32l8r48l8
+ ___block_descriptor_80_e8_32s40r48r56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8r48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48r56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8r64l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r64l8s40l8s48l8r72l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8r64l8s56l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8s56l8s64l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e8_B12?0B8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56s64r72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72r80r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr72l8s32l8s40l8s48l8r80l8s56l8s64l8
+ ___block_literal_global.33
+ ___block_literal_global.62
+ _defaultManager.defaultManager
+ _defaultManager.onceToken
+ _kCADSpotlightIndexerLongReindexRetryInterval
+ _kCADSpotlightIndexerReindexBatchSize
+ _kCADSpotlightIndexerShortReindexRetryInterval
+ _kCalDBCurrentSpotlightIndexCalendarsVersion
+ _kCalDBCurrentSpotlightIndexEventsVersion
+ _kCalDBLastSpotlightIndexCalendarsVersion
+ _kCalDBLastSpotlightIndexEventsVersion
+ _kCalDBReindexAttemptsStartedWithoutProgress
+ _kCalDBReindexState
+ _kCalIndexedCalendarUniqueIDPrefix
+ _objc_msgSend$_addCommonCalendarAttributesToSet:forCalendar:
+ _objc_msgSend$_advanceReindexingWithState:
+ _objc_msgSend$_checkForAndReportPastSpotlightMigrationErrorsAndReindexIfNeeded
+ _objc_msgSend$_commonReindexPreambleWithState:
+ _objc_msgSend$_continueReindexWithState:
+ _objc_msgSend$_countTotalSpotlightDonationItems
+ _objc_msgSend$_deleteEverythingFromSpotlightForFullReindex
+ _objc_msgSend$_deleteFromIndex:index:
+ _objc_msgSend$_enumerateDatabasesWithBlockingCalls:
+ _objc_msgSend$_enumerateDatabasesWithoutBlockingCalls:
+ _objc_msgSend$_fullCalendarsReindexWithDeleteFirst:
+ _objc_msgSend$_fullReindexOfEvents:calendars:withReason:
+ _objc_msgSend$_incrementalReindexEventsWithState:
+ _objc_msgSend$_loadCurrentReindexState
+ _objc_msgSend$_nextDatabaseIDAfterDatabaseID:
+ _objc_msgSend$_pushBatchedUpdatesForEventsWithUUIDs:calendarsWithUUIDs:database:personaID:deleteBeforeInserting:
+ _objc_msgSend$_pushUpdatesForEventsWithUUIDs:calendarsWithUUIDs:database:personaID:deleteBeforeInserting:
+ _objc_msgSend$_pushUpdatesForEventsWithUUIDs:calendarsWithUUIDs:inBatchesOf:database:personaID:deleteBeforeInserting:
+ _objc_msgSend$_reportDonationCountWithAllKnownItems:itemsNeedingDonation:
+ _objc_msgSend$_reportDonationProgressForChange
+ _objc_msgSend$_resumeQueue
+ _objc_msgSend$_saveIndexState:
+ _objc_msgSend$_spotlightDomainIDWithBundleID:personaID:storeID:calendarID:eventID:forIndexedEntityType:
+ _objc_msgSend$_spotlightItemAttributesForCalendar:
+ _objc_msgSend$_spotlightItemAttributesForEvent:
+ _objc_msgSend$_startPendingReindexIfAllowed
+ _objc_msgSend$_typeLabelsForReindexingEvents:calendars:
+ _objc_msgSend$_updateRetryReindexDate
+ _objc_msgSend$_upsertCalendar:withDomainID:context:
+ _objc_msgSend$_upsertEvent:withDomainID:context:
+ _objc_msgSend$_upsertToIndex:inDatabase:personaID:deleteBeforeInserting:index:
+ _objc_msgSend$addIdToRemove:
+ _objc_msgSend$addItemToIndex:
+ _objc_msgSend$addToDomainIdsToDelete:forChangeDict:entityType:database:personaID:donateCalendars:
+ _objc_msgSend$addToEntitiesToIndex:forChangeDict:entityType:modifiedObjectID:database:donateCalendars:
+ _objc_msgSend$associateCalendarEntityWithIdentifier:withSearchableItem:
+ _objc_msgSend$attributeForKey:
+ _objc_msgSend$batchAPIMisuseCallback
+ _objc_msgSend$clientState
+ _objc_msgSend$dataContainerProvider
+ _objc_msgSend$dataPreferenceValueForKey:
+ _objc_msgSend$databaseInitializationConfig
+ _objc_msgSend$datePreferenceValueForKey:
+ _objc_msgSend$deleteBeforeInserting
+ _objc_msgSend$donateCalendars
+ _objc_msgSend$expectedClientState
+ _objc_msgSend$fetchLastClientStateWithCompletionHandler:
+ _objc_msgSend$flushBatch
+ _objc_msgSend$fullReindexState
+ _objc_msgSend$incrementalState
+ _objc_msgSend$index
+ _objc_msgSend$initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:
+ _objc_msgSend$initWithDatabase:indexProvider:personaID:deleteBeforeInserting:recordCount:batchSize:index:
+ _objc_msgSend$initWithDatabaseConfiguration:
+ _objc_msgSend$initWithDefaults:
+ _objc_msgSend$initWithState:databaseID:lastProcessedRowID:deleteBeforeIndexing:
+ _objc_msgSend$intPreferenceValueForKey:
+ _objc_msgSend$isBatchFull
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$isReindexing
+ _objc_msgSend$itemsInIndex
+ _objc_msgSend$lastABCReport
+ _objc_msgSend$lastReindexStartDate
+ _objc_msgSend$lastSpotlightIndexCalendarsVersion
+ _objc_msgSend$lastSpotlightIndexEventsVersion
+ _objc_msgSend$nlCalendarID
+ _objc_msgSend$oneYearFromNow
+ _objc_msgSend$protectedDataAvailable
+ _objc_msgSend$reindexState
+ _objc_msgSend$reindexesStartedWithoutProgress
+ _objc_msgSend$reindexingCalendarsDeleteBeforeIndexing
+ _objc_msgSend$reindexingCalendarsStateWithDeleteBeforeIndexing:
+ _objc_msgSend$reindexingEventsDatabaseID
+ _objc_msgSend$reindexingEventsLastProcessedRowID
+ _objc_msgSend$reindexingEventsStateWithDatabase:lastProcessedRowID:
+ _objc_msgSend$reindexingInProgress
+ _objc_msgSend$reportDonationProgress:completionHandler:
+ _objc_msgSend$reportDonationProgressWithAllKnownItems:itemsNeedingDonation:completionHandler:
+ _objc_msgSend$serializedData
+ _objc_msgSend$setAttribute:forKey:
+ _objc_msgSend$setClientState:
+ _objc_msgSend$setContainerIdentifier:
+ _objc_msgSend$setLastABCReport:
+ _objc_msgSend$setLastReindexStartDate:
+ _objc_msgSend$setLastSpotlightIndexCalendarsVersion:
+ _objc_msgSend$setLastSpotlightIndexEventsVersion:
+ _objc_msgSend$setObjectCallback
+ _objc_msgSend$setReindexState:
+ _objc_msgSend$setReindexesStartedWithoutProgress:
+ _objc_msgSend$sixMonthsFromNow
+ _objc_msgSend$spotlightUniqueIDForCalendar:
+ _objc_msgSend$spotlightUniqueIDForEvent:occurrenceDate:
+ _objc_msgSend$state
- +[CADSpotlightIndexer _personaID:]
- +[CADSpotlightIndexer _personaID:].cold.1
- +[CADSpotlightIndexer _spotlightDomainIDForItem:bundleID:personaID:].cold.1
- +[ClientConnection poolManager].cold.1
- -[CADDatabaseInitializationOptions(ClientConnection) purifyOptions]
- -[CADDatabaseInitializationOptions(ClientConnection) validOptionsForConnection:]
- -[CADMockSpotlightIndexProvider failureMode]
- -[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]
- -[CADSpotlightIndexer _enumerateDatabases:]
- -[CADSpotlightIndexer _expectedClientState]
- -[CADSpotlightIndexer _fullReindexWithReason:].cold.1
- -[CADSpotlightIndexer _fullReindexWithReason:].cold.2
- -[CADSpotlightIndexer _mostRecentFailureWithinADayOfNow:]
- -[CADSpotlightIndexer _mostRecentFailure]
- -[CADSpotlightIndexer _pushBatchedUpdatesForCalendarItemsWithUUIDs:database:personaID:deleteBeforeInserting:]
- -[CADSpotlightIndexer _pushUpdatesForCalendarItemsWithUUIDs:database:personaID:deleteBeforeInserting:]
- -[CADSpotlightIndexer _pushUpdatesForCalendarItemsWithUUIDs:database:personaID:deleteBeforeInserting:].cold.1
- -[CADSpotlightIndexer _pushUpdatesForCalendarItemsWithUUIDs:inBatchesOf:database:personaID:deleteBeforeInserting:]
- -[CADSpotlightIndexer _pushUpdatesForCalendarItemsWithUUIDs:inBatchesOf:database:personaID:deleteBeforeInserting:].cold.1
- -[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]
- -[CADSpotlightIndexer _spotlightItemAttributes:]
- -[CADSpotlightIndexer _upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:]
- -[CADSpotlightIndexer _upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:].cold.1
- -[CADSpotlightIndexer _upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:].cold.2
- -[CADSpotlightIndexer checkForAndReportPastSpotlightMigrationErrorsAndReindexIfNeeded]
- -[CADSpotlightIndexer checkForAndReportPastSpotlightMigrationErrorsAndReindexIfNeeded].cold.1
- GCC_except_table34
- GCC_except_table72
- _CalDatabaseCopyCalendarItemUUIDs
- _CalDatabaseEnumerateDatabasesWithConfiguration
- _OBJC_IVAR_$_CADMockSpotlightIndex.needsReindex
- _OBJC_IVAR_$_CADSpotlightIndexer._databaseConfiguration
- __OBJC_$_INSTANCE_METHODS_CADDatabaseInitializationOptions(ClientConnection)
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CADSpotlightDefaults
- __OBJC_$_PROTOCOL_METHOD_TYPES_CADSpotlightDefaults
- __OBJC_$_PROTOCOL_REFS_CADSpotlightDefaults
- __OBJC_LABEL_PROTOCOL_$_CADSpotlightDefaults
- __OBJC_PROTOCOL_$_CADSpotlightDefaults
- ___31+[ClientConnection poolManager]_block_invoke
- ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke
- ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke_2
- ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke_2.cold.1
- ___46-[CADSpotlightIndexer _fullReindexWithReason:]_block_invoke_2.cold.2
- ___52-[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]_block_invoke
- ___52-[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]_block_invoke.134
- ___52-[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]_block_invoke.134.cold.1
- ___52-[CADSpotlightIndexer _deleteFromIndex:eventsIndex:]_block_invoke.cold.1
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.157
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.157.cold.1
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.161
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.161.cold.1
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.cold.1
- ___86-[CADSpotlightIndexer checkForAndReportPastSpotlightMigrationErrorsAndReindexIfNeeded]_block_invoke
- ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke.59
- ___88-[CADSpotlightIndexer _deleteAllSearchableItemsAndSetClientStateForBundleID:eventIndex:]_block_invoke.59.cold.1
- ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.211
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r96l8s64l8s72l8s80l8s88l8
- ___block_descriptor_112_e8_32s40s48s56s64r72r80r88r96r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8r64l8s56l8r72l8r80l8r88l8r96l8
- ___block_descriptor_116_e8_32s40s48s56s64s72s80s88r96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8s64l8r88l8r96l8s72l8s80l8
- ___block_descriptor_32_e341_B24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16l
- ___block_descriptor_32_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20l
- ___block_descriptor_33_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24l
- ___block_descriptor_36_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12l
- ___block_descriptor_40_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20l
- ___block_descriptor_40_e8_32bs_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8
- ___block_descriptor_40_e8_32bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8
- ___block_descriptor_40_e8_32bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20ls32l8
- ___block_descriptor_40_e8_32bs_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8
- ___block_descriptor_40_e8_32r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8
- ___block_descriptor_40_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr32l8
- ___block_descriptor_40_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr32l8
- ___block_descriptor_40_e8_32s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8
- ___block_descriptor_40_e8_32s_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24ls32l8
- ___block_descriptor_40_e8_32s_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8
- ___block_descriptor_41_e8_32r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8
- ___block_descriptor_44_e8_32bs_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls32l8
- ___block_descriptor_44_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr32l8
- ___block_descriptor_44_e8_32r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20lr32l8
- ___block_descriptor_48_e8_32r40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr32l8r40l8
- ___block_descriptor_48_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr32l8
- ___block_descriptor_48_e8_32s40bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls40l8s32l8
- ___block_descriptor_48_e8_32s40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8
- ___block_descriptor_49_e8_32s40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8
- ___block_descriptor_52_e8_32bs40r_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls32l8r40l8
- ___block_descriptor_52_e8_32r40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8r40l8
- ___block_descriptor_52_e8_32s40bs_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls40l8s32l8
- ___block_descriptor_52_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr40l8s32l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20ls40l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32r40r48r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr32l8r40l8r48l8
- ___block_descriptor_57_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40r48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr40l8s32l8r48l8
- ___block_descriptor_64_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40r48r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20lr40l8r48l8s32l8
- ___block_descriptor_64_e8_32s40r_e8_B12?0B8ls32l8r40l8
- ___block_descriptor_64_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r48l8s40l8r56l8
- ___block_descriptor_64_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40s48r56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r48l8s40l8r56l8
- ___block_descriptor_64_e8_32s40s48r56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40s48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r56l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e349_v24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8"NSArray"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8
- ___block_descriptor_65_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8
- ___block_descriptor_65_e8_32s40s48s56bs_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s56l8s48l8
- ___block_descriptor_68_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8
- ___block_descriptor_68_e8_32s40s48s56s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
- ___block_descriptor_72_e8_32s40s48bs56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8r64l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr48l8r56l8s32l8s40l8r64l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8r64l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8r64l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s_e8_B12?0B8ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40r48r56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8r48l8r56l8r64l8
- ___block_descriptor_80_e8_32s40s48r56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r48l8s40l8r56l8r64l8
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24ls32l8s40l8s56l8r64l8s48l8r72l8
- ___block_descriptor_80_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8r64l8s48l8
- ___block_descriptor_80_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r64l8s40l8s48l8r72l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8r64l8s56l8r72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8s56l8s64l8r72l8
- ___block_descriptor_81_e8_32s40s48s56s64r72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_descriptor_89_e8_32s40s48s56s64s72r80r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr72l8s32l8s40l8s48l8r80l8s56l8s64l8
- ___block_literal_global.48
- ___block_literal_global.64
- _kCalDBCurrentSpotlightIndexVersion
- _kCalDBLastSpotlightError
- _kCalDBLastSpotlightIndexVersion
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_deleteFromIndex:eventsIndex:
- _objc_msgSend$_enumerateDatabases:
- _objc_msgSend$_expectedClientState
- _objc_msgSend$_mostRecentFailure
- _objc_msgSend$_mostRecentFailureWithinADayOfNow:
- _objc_msgSend$_pushBatchedUpdatesForCalendarItemsWithUUIDs:database:personaID:deleteBeforeInserting:
- _objc_msgSend$_pushUpdatesForCalendarItemsWithUUIDs:database:personaID:deleteBeforeInserting:
- _objc_msgSend$_pushUpdatesForCalendarItemsWithUUIDs:inBatchesOf:database:personaID:deleteBeforeInserting:
- _objc_msgSend$_spotlightItemAttributes:
- _objc_msgSend$_upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:
- _objc_msgSend$checkForAndReportPastSpotlightMigrationErrorsAndReindexIfNeeded
- _objc_msgSend$failureCallback
- _objc_msgSend$failureMode
- _objc_msgSend$laterDate:
- _objc_msgSend$numCalls
- _objc_msgSend$timestamps
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x6
- _poolManager.defaultManager
- _poolManager.onceToken
CStrings:
+ " options = %lx"
+ "%@.%@%@"
+ "%@.%@%@.%@"
+ "%@.%@%@.%@.%@"
+ "%@.%@%@.%@.%@.%@"
+ "%@: {databaseInitOptions = %lu, enablePropertyModificationLogging = %@, unitTesting = %@, management = %i, managementBundleID = %@, changeTrackingID = %@, databaseDirectory = %@, containerProvider = %@, allowDelegateSources: %@, allowIntegrations: %@, allowedSourceIdentifiers: %@, privacyClientIdentity: %@, mockPermissions: %@, remoteClientIdentity: %@}"
+ "****** [Spotlight indexing] reindex needed for %{public}@, last events version was %{public}i, last calendars version was %{public}i"
+ "-_advanceReindexingWithState: called with incremental indexing state"
+ "<CADIndexState: %@>"
+ "@\"<CADSpotlightDefaultsStorage>\""
+ "@\"CADSpotlightDefaults\""
+ "@\"NSArray\"24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "@\"NSString\"32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "@20@0:8B16"
+ "@24@0:8B16B20"
+ "@24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "@28@0:8i16q20"
+ "@32@0:8Q16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "@32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "@32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
+ "@36@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24@?28"
+ "@36@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24^B28"
+ "@40@0:8Q16i24q28B36"
+ "@40@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16^v24@32"
+ "@48@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32^B40"
+ "@48@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32^i40"
+ "@56@0:8@16@24@32^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}40^i48"
+ "@60@0:8@16@24@32@40@48i56"
+ "@64@0:8^v16Q24@32@40^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}48^B56"
+ "@68@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24@32B40Q44Q52@60"
+ "@76@0:8@16@24@32^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}40Q48i56^@60^i68"
+ "AB"
+ "Attempting to build domain ID for unsupported indexed entity type %d"
+ "Aux database with ID %i has an empty persona ID"
+ "B20@0:8B16"
+ "B24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "B24@?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8^v16"
+ "B32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "B40@0:8Q16^v24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "B44@0:8@\"CADPooledDatabaseConfiguration\"16Q24i32@?<v@?^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}>36"
+ "B44@0:8^{__CFArray=}16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32B40"
+ "B52@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32@40B48"
+ "B52@0:8^{__CFArray=}16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32B40@44"
+ "B60@0:8@16@24Q32^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}40@48B56"
+ "Beginning delete of %lu items, before indexing %lu items"
+ "Beginning indexing of %lu items"
+ "Beginning wait for delete, then indexing of items"
+ "CADIndexState"
+ "CADSpotlightDefaultsStorage"
+ "CADSpotlightUpsertContext"
+ "Calendar with id %d <%{public}@> has no store. Silently ignoring."
+ "CalendarsInSpotlight"
+ "Can't determine persona ID for database ID %i"
+ "Client state mismatch during reindexing. Restarting reindexing from the beginning"
+ "Could not find a calendar with UUID [%@].  Will not push this item to Spotlight."
+ "Couldn't load previous indexing state; starting over with a full reindex"
+ "Deleted all spotlight items for full re-index, beginning events index"
+ "Deleted indexed calendars during full re-index, beginning index"
+ "Deleting all spotlight items for full re-index using bundle ID %{public}@"
+ "Deleting calendars for database during full re-index"
+ "Error deleting indexed calendars, error = %@"
+ "Error deleting indexed calendars, error = %@. Retrying..."
+ "Error fetching client state: %@"
+ "Error indexing a batch of %lu events in this database as part of a full-reindex, out of retries"
+ "Error indexing a batch of %lu events in this database as part of a full-reindex, retrying..."
+ "Error reporting donation count error = %@"
+ "Finished indexing a batch of %lu events in database %i as part of a full-reindex"
+ "Finished pushing delete of %lu items into batch"
+ "Found %lu entity updates and %lu domains to delete"
+ "Ignoring calendar with id %d because it has no UUID"
+ "Ignoring hidden calendar with id %d <%{public}@>"
+ "Ignoring integration calendar with id %d <%{public}@>"
+ "Ignoring reindex call that did not request anything be reindexed: -[CADSpotlightIndexer _fullReindexOfEvents:NO calendars:NO reason:%lu]"
+ "Incremental"
+ "Indexing %lu calendars in this database as part of full-reindex"
+ "Indexing %lu calendars in this database as part of reindex"
+ "Indexing calendar with id %d <%{public}@>"
+ "Internal"
+ "Key %@ set in passthroughSpotlightAttributes for event %@ but this key is set already by calendar, ignoring."
+ "Loaded index state %@"
+ "Loaded index state %{public}@"
+ "Missing required fields to handle deleted calendar: storeID = %{public}@, calendarID = %{public}@"
+ "Missing required fields to handle deleted event: storeID = %{public}@, calendarID = %{public}@, eventID = %{public}@"
+ "NeedFullReindex"
+ "Possible changes detected. Checking whether updates are needed for the spotlight index."
+ "Q24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "Reindex failed due to no progress: %@.  Will try again after %@"
+ "Reindex failed. Will try again after %@"
+ "ReindexAttemptsWithoutProgress"
+ "ReindexState"
+ "ReindexingCalendars(deleteFirst:%@)"
+ "ReindexingEvents(db:%u, rowID:%lld)"
+ "Retrieved state of length %lu: %@"
+ "Starting reindex attempt with state: %@"
+ "Successfully finished reindex started with state: %@"
+ "T@\"<CADSpotlightIndex>\",R,N,V_index"
+ "T@\"NSData\",&,N"
+ "T@\"NSData\",&,N,V_clientState"
+ "T@\"NSDate\",&,N"
+ "T@\"NSDate\",&,N,V_lastABCReport"
+ "T@\"NSDate\",R,N,V_now"
+ "T@\"NSDate\",R,N,V_oneYearFromNow"
+ "T@\"NSDate\",R,N,V_sixMonthsFromNow"
+ "T@\"NSString\",R,N,V_personaID"
+ "T@?,C,N,V_batchAPIMisuseCallback"
+ "T@?,C,N,V_setObjectCallback"
+ "TB,N,V_donateCalendars"
+ "TB,R,N,V_deleteBeforeInserting"
+ "TB,R,N,V_donateCalendars"
+ "TB,R,N,V_needsReindex"
+ "TB,R,N,V_reindexingCalendarsDeleteBeforeIndexing"
+ "TQ,N,V_databaseInitOptions"
+ "TQ,R,N,V_state"
+ "T^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB},N,V_database"
+ "T^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB},R,N,V_database"
+ "Ti,R,N,V_nlCalendarID"
+ "Ti,R,N,V_reindexingEventsDatabaseID"
+ "Tq,R,N,V_reindexingEventsLastProcessedRowID"
+ "Triggered spotlight re-index of  %@ for all databases with reason: %@"
+ "Triggered spotlight re-index of %{public}@ for all databases with reason: %@"
+ "Unable to fetch client state: %@"
+ "Unexpected entity type being upserted. type = %d, uid = %d"
+ "Unknown(%lu)"
+ "Updates to spotlight index complete"
+ "^v64@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32^v40@48Q56"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@0:8"
+ "_addCommonCalendarAttributesToSet:forCalendar:"
+ "_advanceReindexingWithState:"
+ "_batchAPIMisuseCallback"
+ "_batchSize"
+ "_checkForAndReportPastSpotlightMigrationErrorsAndReindexIfNeeded"
+ "_clientState"
+ "_commonReindexPreambleWithState:"
+ "_continueReindexWithState:"
+ "_countTotalSpotlightDonationItems"
+ "_dbConnectionProvider"
+ "_deleteBeforeInserting"
+ "_deleteEverythingFromSpotlightForFullReindex"
+ "_deleteFromIndex:index:"
+ "_donateCalendars"
+ "_donationLock"
+ "_enumerateDatabasesWithBlockingCalls:"
+ "_enumerateDatabasesWithoutBlockingCalls:"
+ "_fullCalendarsReindexWithDeleteFirst:"
+ "_fullReindexOfEvents:calendars:withReason:"
+ "_idsToRemove"
+ "_incrementalReindexEventsWithState:"
+ "_itemsToIndex"
+ "_lastABCReport"
+ "_loadCurrentReindexState"
+ "_needsReindex"
+ "_nextDatabaseIDAfterDatabaseID:"
+ "_nlCalendarID"
+ "_oneYearFromNow"
+ "_personaID"
+ "_personaIDCache"
+ "_poolConfig"
+ "_pushBatchedUpdatesForEventsWithUUIDs:calendarsWithUUIDs:database:personaID:deleteBeforeInserting:"
+ "_pushUpdatesForEventsWithUUIDs:calendarsWithUUIDs:database:personaID:deleteBeforeInserting:"
+ "_pushUpdatesForEventsWithUUIDs:calendarsWithUUIDs:inBatchesOf:database:personaID:deleteBeforeInserting:"
+ "_reindexingCalendarsDeleteBeforeIndexing"
+ "_reindexingEventsDatabaseID"
+ "_reindexingEventsLastProcessedRowID"
+ "_reportDonationCountWithAllKnownItems:itemsNeedingDonation:"
+ "_reportDonationProgressForChange"
+ "_resumeQueue"
+ "_resumed"
+ "_retryReindexDate"
+ "_saveIndexState:"
+ "_setObjectCallback"
+ "_sixMonthsFromNow"
+ "_spotlightDomainIDWithBundleID:personaID:storeID:calendarID:eventID:forIndexedEntityType:"
+ "_spotlightItemAttributesForCalendar:"
+ "_spotlightItemAttributesForEvent:"
+ "_startPendingReindexIfAllowed"
+ "_typeLabelsForReindexingEvents:calendars:"
+ "_updateRetryReindexDate"
+ "_upsertCalendar:withDomainID:context:"
+ "_upsertEvent:withDomainID:context:"
+ "_upsertToIndex:inDatabase:personaID:deleteBeforeInserting:index:"
+ "addIdToRemove:"
+ "addItemToIndex:"
+ "addToDomainIdsToDelete:forChangeDict:entityType:database:personaID:donateCalendars:"
+ "addToEntitiesToIndex:forChangeDict:entityType:modifiedObjectID:database:donateCalendars:"
+ "associateCalendarEntityWithIdentifier:withSearchableItem:"
+ "attributeForKey:"
+ "batchAPIMisuseCallback"
+ "calaccessd"
+ "calendar."
+ "clientState"
+ "d32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "d40@0:8^v16^v24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "d40@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24^@32"
+ "d40@0:8^v16d24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "dataContainerProvider"
+ "dataPreferenceValueForKey:"
+ "databaseInitializationConfig"
+ "datePreferenceValueForKey:"
+ "deleteBeforeInserting"
+ "donateCalendars"
+ "error deleting indexed calendars: %@"
+ "error deleting indexed calendars: %@. Retrying..."
+ "error indexing a batch of %lu events in this database as part of a full-reindex, out of retries"
+ "error indexing a batch of %lu events in this database as part of a full-reindex, retrying..."
+ "events and calendars"
+ "expectedClientState"
+ "fetchLastClientStateWithCompletionHandler called"
+ "fetchLastClientStateWithCompletionHandler finished with state %@"
+ "fetchLastClientStateWithCompletionHandler:"
+ "finished reportDonationProgress"
+ "finished reportDonationProgress: %@"
+ "flushBatch"
+ "fullReindexState"
+ "i24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "i32@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "i32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "i40@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "i40@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32"
+ "i44@0:8^v16@24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32i40"
+ "i56@0:8@16@24@32@40^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}48"
+ "incrementalState"
+ "index"
+ "initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:"
+ "initWithDatabase:indexProvider:personaID:deleteBeforeInserting:recordCount:batchSize:index:"
+ "initWithDatabaseConfiguration:"
+ "initWithDefaults:"
+ "initWithState:databaseID:lastProcessedRowID:deleteBeforeIndexing:"
+ "intPreferenceValueForKey:"
+ "isBatchFull"
+ "isEqualToData:"
+ "isReindexing"
+ "itemsInIndexPassingTest:"
+ "kCalDBLastSpotLightIndexCalendarsVersion"
+ "lastABCReport"
+ "lastReindexStartDate"
+ "lastSpotlightIndexCalendarsVersion"
+ "lastSpotlightIndexEventsVersion"
+ "nlCalendarID"
+ "none"
+ "oneYearFromNow"
+ "protectedDataAvailable"
+ "reindexState"
+ "reindexesStartedWithoutProgress"
+ "reindexingCalendarsDeleteBeforeIndexing"
+ "reindexingCalendarsStateWithDeleteBeforeIndexing:"
+ "reindexingEventsDatabaseID"
+ "reindexingEventsLastProcessedRowID"
+ "reindexingEventsStateWithDatabase:lastProcessedRowID:"
+ "reindexingInProgress"
+ "reportDonationProgress:completionHandler:"
+ "reportDonationProgressWithAllKnownItems called with all known item count: %lu and items needing donation count %lu"
+ "reportDonationProgressWithAllKnownItems finished with all known item count: %lu and items needing donation count %lu"
+ "reportDonationProgressWithAllKnownItems:itemsNeedingDonation:completionHandler:"
+ "resuming reindex now because it was allowed at %@"
+ "serializedData"
+ "setAttribute:forKey:"
+ "setBatchAPIMisuseCallback:"
+ "setClientState:"
+ "setContainerIdentifier:"
+ "setDonateCalendars:"
+ "setLastABCReport:"
+ "setLastABCReportAtDate:"
+ "setLastReindexStartDate:"
+ "setLastSpotlightIndexCalendarsVersion:"
+ "setLastSpotlightIndexEventsVersion:"
+ "setNow:"
+ "setObjectCallback"
+ "setReindexState:"
+ "setReindexesStartedWithoutProgress:"
+ "setSetObjectCallback:"
+ "sixMonthsFromNow"
+ "spotlightUniqueIDForCalendar:"
+ "spotlightUniqueIDForEvent:occurrenceDate:"
+ "state"
+ "v16@?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8"
+ "v20@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}12"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
+ "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v24@?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8@\"NSArray\"16"
+ "v28@?0i8@\"NSArray\"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}20"
+ "v28@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}12^B20"
+ "v28@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}12^v20"
+ "v32@0:8B16B20Q24"
+ "v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
+ "v32@0:8q16q24"
+ "v32@?0@\"NSString\"8@16^B24"
+ "v32@?0^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8^v16^B24"
+ "v40@0:8@\"CADPooledDatabaseConfiguration\"16Q24@?<v@?i^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}^B>32"
+ "v40@0:8@\"NSMutableSet\"16^v24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "v40@0:8@16Q24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "v40@0:8@16^v24^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "v40@0:8Q16Q24@?32"
+ "v40@0:8Q16Q24@?<v@?@\"NSError\">32"
+ "v56@0:8@16@24i32^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}36@44B52"
+ "v56@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32^@40^@48"
+ "v56@0:8^{__CFSet=}16@24i32@36^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}44B52"
+ "v76@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24i28i32@36@44@52@60^B68"
- " options = %x"
- "%@.%@.%@"
- "%@.%@.%@.%@"
- "%@.%@.%@.%@.%@"
- "%@: {databaseInitOptions = %i, enablePropertyModificationLogging = %@, unitTesting = %@, management = %i, managementBundleID = %@, changeTrackingID = %@, databaseDirectory = %@, containerProvider = %@, allowDelegateSources: %@, allowIntegrations: %@, allowedSourceIdentifiers: %@, privacyClientIdentity: %@, mockPermissions: %@, remoteClientIdentity: %@}"
- "****** [Spotlight indexing] 1 day since last failure, reindex needed"
- "****** [Spotlight indexing] reindex aborted, less than one day since last failure"
- "****** [Spotlight indexing] reindex needed, last version was %@"
- "@\"<CADSpotlightDefaults>\""
- "@\"NSArray\"24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
- "@\"NSString\"32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
- "@24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
- "@32@0:8Q16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
- "@32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
- "@32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
- "@36@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24@?28"
- "@36@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24^B28"
- "@40@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16^v24@32"
- "@48@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32^B40"
- "@48@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32^i40"
- "@56@0:8@16@24@32^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}40^i48"
- "@64@0:8^v16Q24@32@40^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}48^B56"
- "@76@0:8@16@24@32^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}40Q48i56^@60^i68"
- "B24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
- "B24@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8^v16"
- "B32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
- "B40@0:8Q16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
- "B44@0:8@\"CADPooledDatabaseConfiguration\"16Q24i32@?<v@?^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}>36"
- "B44@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32B40"
- "B44@0:8^{__CFArray=}16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32B40"
- "B52@0:8@16Q24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32@40B48"
- "B52@0:8^{__CFArray=}16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32B40@44"
- "Beginning delete of %lu events, before indexing %lu events"
- "Beginning indexing of %lu events"
- "Beginning spotlight re-index for all databases: %@"
- "Beginning wait for delete, then indexing of events"
- "CalDBSpotLightError"
- "Deleted events for database during full re-index, beginning index"
- "Error determining non-empty personaID for non-nil auxDatabase"
- "Error indexing %lu events in this database as part of a full-reindex, out of retries"
- "Error indexing %lu events in this database as part of a full-reindex, retrying..."
- "Finished indexing %lu events in this database as part of a full-reindex"
- "Finished pushing delete of %lu events into batch"
- "Finished spotlight re-index for all databases"
- "Indexing %lu events in this database as part of full-reindex"
- "Indexing %lu events in this database as part of reindex"
- "Q24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
- "TQ,N,V_failureMode"
- "T^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB},N,V_database"
- "Ti,N,V_databaseInitOptions"
- "Unable to get valid domain ID when there's not a valid storeID. CalendarID: %@"
- "^v64@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32^v40@48Q56"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@0:8"
- "_databaseConfiguration"
- "_deleteFromIndex:eventsIndex:"
- "_enumerateDatabases:"
- "_expectedClientState"
- "_mostRecentFailure"
- "_mostRecentFailureWithinADayOfNow:"
- "_pushBatchedUpdatesForCalendarItemsWithUUIDs:database:personaID:deleteBeforeInserting:"
- "_pushUpdatesForCalendarItemsWithUUIDs:database:personaID:deleteBeforeInserting:"
- "_pushUpdatesForCalendarItemsWithUUIDs:inBatchesOf:database:personaID:deleteBeforeInserting:"
- "_spotlightItemAttributes:"
- "_upsertToIndex:inDatabase:personaID:deleteBeforeInserting:eventsIndex:"
- "checkForAndReportPastSpotlightMigrationErrorsAndReindexIfNeeded"
- "com_apple_mobilecal_recipientParticipationStatuses"
- "d32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
- "d40@0:8^v16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
- "d40@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24^@32"
- "d40@0:8^v16d24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
- "error indexing %lu events in this database as part of a full-reindex, out of retries"
- "error indexing %lu events in this database as part of a full-reindex, retrying..."
- "error while attemping full reindex, writing error pref"
- "failureMode"
- "finished _fullReindexWithReason: %@"
- "i24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
- "i32@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
- "i32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
- "i40@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
- "i40@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32"
- "i44@0:8^v16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32i40"
- "i56@0:8@16@24@32@40^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}48"
- "laterDate:"
- "reindex aborted, less than one day since last failure"
- "started _fullReindexWithReason: %@"
- "v16@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8"
- "v20@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}12"
- "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
- "v24@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8@\"NSArray\"16"
- "v28@?0i8@\"NSArray\"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}20"
- "v28@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}12^B20"
- "v28@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}12^v20"
- "v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
- "v32@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8^v16^B24"
- "v40@0:8@\"CADPooledDatabaseConfiguration\"16Q24@?<v@?i^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}^B>32"
- "v40@0:8@\"NSMutableSet\"16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
- "v40@0:8@16Q24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
- "v40@0:8@16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
- "v56@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32^@40^@48"
- "v76@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24i28i32@36@44@52@60^B68"

```
