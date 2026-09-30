## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1194.6.2.0.0
-  __TEXT.__text: 0x6bbb0
-  __TEXT.__auth_stubs: 0x3700
-  __TEXT.__objc_methlist: 0x5d2c
-  __TEXT.__cstring: 0x6dad
+1216.0.0.0.0
+  __TEXT.__text: 0x712e0
+  __TEXT.__auth_stubs: 0x37e0
+  __TEXT.__objc_methlist: 0x615c
+  __TEXT.__cstring: 0x6f3d
   __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0x7fa2
-  __TEXT.__gcc_except_tab: 0x19f0
+  __TEXT.__oslogstring: 0x81af
+  __TEXT.__gcc_except_tab: 0x1ba4
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1980
-  __TEXT.__objc_classname: 0x143c
-  __TEXT.__objc_methname: 0xe09a
-  __TEXT.__objc_methtype: 0x640a
-  __TEXT.__objc_stubs: 0x92c0
-  __DATA_CONST.__got: 0x998
-  __DATA_CONST.__const: 0x1e50
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __TEXT.__unwind_info: 0x1a88
+  __TEXT.__objc_classname: 0x1499
+  __TEXT.__objc_methname: 0xea03
+  __TEXT.__objc_methtype: 0x6620
+  __TEXT.__objc_stubs: 0x9b00
+  __DATA_CONST.__got: 0x9e8
+  __DATA_CONST.__const: 0x1fe0
+  __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x1c0
+  __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ef0
+  __DATA_CONST.__objc_selrefs: 0x3108
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x1b90
-  __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0x76a0
-  __AUTH_CONST.__objc_const: 0xb8f0
-  __AUTH_CONST.__objc_intobj: 0x420
+  __AUTH_CONST.__auth_got: 0x1c00
+  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__cfstring: 0x7980
+  __AUTH_CONST.__objc_const: 0xc0b8
+  __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xeb0
+  __AUTH.__objc_data: 0x1400
   __AUTH.__data: 0xa50
-  __DATA.__objc_ivar: 0x730
-  __DATA.__data: 0x16c8
+  __DATA.__objc_ivar: 0x784
+  __DATA.__data: 0x1728
   __DATA.__bss: 0x198
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1770
+  __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0x150
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 52903E7B-E1E5-3879-8508-0E87169D0A9B
-  Functions: 2050
-  Symbols:   8568
-  CStrings:  5360
+  UUID: CC37E7F8-4582-34E7-B336-A0B7AA4132BA
+  Functions: 2146
+  Symbols:   8927
+  CStrings:  5539
 
Symbols:
+ +[CADClientBlockOperation blockOperationWithToken:block:]
+ +[CADFetchCalendarItemsWithPredicateOperation isJunkEvent:]
+ +[CADFetchCalendarItemsWithPredicateOperation performSynchronouslyWithPredicate:entityType:connection:fetchIdentifier:cancellationToken:]
+ +[CADFetchCalendarItemsWithPredicateOperation queryDatabase:withID:predicate:connection:serializer:cancellationToken:]
+ +[CADRemovedEventWrapper supportsSecureCoding]
+ -[CADBlockList .cxx_destruct]
+ -[CADBlockList initWithBlockList:]
+ -[CADBlockList isBlockListEmpty]
+ -[CADBlockList isEventBlocked:]
+ -[CADCalSearchOperation token]
+ -[CADClientBlockOperation initWithToken:]
+ -[CADClientBlockOperation token]
+ -[CADDatabaseConnectionPool _poolForPath:auxDatabaseID:]
+ -[CADDatabaseConnectionPool hasDatabaseAtPath:withDatabaseID:]
+ -[CADDatabaseSingleConnectionProvider hasDatabaseAtPath:withDatabaseID:]
+ -[CADEventOccurrenceSet addOccurrenceWithDB:rowID:date:]
+ -[CADEventOccurrenceSet clear]
+ -[CADEventOccurrenceSet datesForDatabase:rowID:]
+ -[CADEventOccurrenceSet dealloc]
+ -[CADEventOccurrenceSet enumerateDatabases:]
+ -[CADEventOccurrenceSet enumerateOccurrenceRowIDsInDatabase:block:]
+ -[CADEventOccurrenceSet infoForDB:]
+ -[CADEventOccurrenceSet setOccurrenceDatesWithDB:rowID:dates:outRemovedDates:outAddedAnyDates:]
+ -[CADEventPredicate concisePublicDescription]
+ -[CADEventPredicate copyWithStartDate:endDate:]
+ -[CADEventPredicate generateDatesForEvent:]
+ -[CADEventPredicate hash]
+ -[CADEventPredicate incrementalPredicatesToExpandResultsFromPredicate:filteringRequiredToRemoveEventsNoLongerMatched:]
+ -[CADEventPredicate matchingDatesForEvent:modifiedProperties:dates:inRange:database:outReset:]
+ -[CADEventPredicate supportsEfficientMonitoring]
+ -[CADFetchCalendarItemsWithPredicateOperation .cxx_destruct]
+ -[CADFetchCalendarItemsWithPredicateOperation cancel]
+ -[CADFetchCalendarItemsWithPredicateOperation initWithPredicate:entityType:connection:fetchIdentifier:completionHandler:]
+ -[CADFetchCalendarItemsWithPredicateOperation main]
+ -[CADFetchCalendarItemsWithPredicateOperation predicate]
+ -[CADFetchCalendarItemsWithPredicateOperation setPredicate:]
+ -[CADFetchCalendarItemsWithPredicateOperation setStartCallback:]
+ -[CADFetchCalendarItemsWithPredicateOperation startCallback]
+ -[CADFetchCalendarItemsWithPredicateOperation token]
+ -[CADNaturalLanguageSuggestedEventsSearchPredicate matchesIgnoringDate:database:]
+ -[CADNaturalLanguageSuggestedEventsSearchPredicate matchingDate:]
+ -[CADNaturalLanguageSuggestedEventsSearchPredicate matchingDatesForEvent:modifiedProperties:dates:inRange:database:outReset:]
+ -[CADNaturalLanguageSuggestedEventsSearchPredicate resetRequiredForRemovalOfMatchingOccurrence]
+ -[CADNaturalLanguageSuggestedEventsSearchPredicate supportsEfficientMonitoring]
+ -[CADNotificationGatheringContext isEventBlocked:]
+ -[CADNotificationGatheringContext isSharedCalendarOwnerBlocked:]
+ -[CADPredicate concisePublicDescription]
+ -[CADPredicate incrementalPredicatesToExpandResultsFromPredicate:filteringRequiredToRemoveEventsNoLongerMatched:]
+ -[CADPredicate matchingDatesForEvent:modifiedProperties:dates:inRange:database:outReset:]
+ -[CADPredicate resetRequiredForRemovalOfMatchingOccurrence]
+ -[CADPredicate supportsEfficientMonitoring]
+ -[CADPredicateMonitorAgent .cxx_destruct]
+ -[CADPredicateMonitorAgent filterWithPredicate:]
+ -[CADPredicateMonitorAgent handleChangeReport:]
+ -[CADPredicateMonitorAgent initWithPredicate:filter:options:token:connection:]
+ -[CADPredicateMonitorAgent processChangeReport:forDatabaseID:]
+ -[CADPredicateMonitorAgent reportResultsReset:newAndUpdated:removed:databaseIDForRemovals:reportPredicateGeneration:generation:]
+ -[CADPredicateMonitorAgent reportResultsReset:newAndUpdated:removed:reportPredicateGeneration:generation:]
+ -[CADPredicateMonitorAgent reset]
+ -[CADPredicateMonitorAgent start]
+ -[CADPredicateMonitorAgent stop]
+ -[CADPredicateMonitorAgent token]
+ -[CADPredicateMonitorAgent updatePredicate:propertyFilter:options:generation:]
+ -[CADRemovedEventWrapper .cxx_destruct]
+ -[CADRemovedEventWrapper encodeWithCoder:]
+ -[CADRemovedEventWrapper initWithCoder:]
+ -[CADRemovedEventWrapper initWithRowID:removedDates:]
+ -[CADRemovedEventWrapper removedDates]
+ -[CADRemovedEventWrapper rowID]
+ -[CADServer handleDistributeChangeReport:]
+ -[CADServer handlePostChangeNote:connection:processName:]
+ -[CADXPCImplementation(CADCalendarItemOperationGroup) CADDatabaseMonitorResultsForPredicate:propertyFilter:options:identifier:reply:]
+ -[CADXPCImplementation(CADCalendarItemOperationGroup) CADDatabaseMonitorUpdatePredicate:propertyFilter:options:identifier:generation:reply:]
+ -[CADXPCImplementation(CADCalendarItemOperationGroup) CADDatabaseStopMonitoringPredicate:]
+ -[CADXPCImplementation(CADEventOperationGroup) CADOccurrenceCacheGetOccurrenceCountOrSumDurationWithStartDate:endDate:calendarIDs:sumDuration:reply:]
+ -[CADXPCImplementation(CADSourceOperationGroup) CADCountOriginalCalendarItemsBySource:reply:]
+ -[ClientConnection addAgent:]
+ -[ClientConnection agentWithToken:]
+ -[ClientConnection blockListOverride]
+ -[ClientConnection blockList]
+ -[ClientConnection cancelOperationsWithToken:]
+ -[ClientConnection hasDatabaseAtPath:withDatabaseID:]
+ -[ClientConnection removeAgentWithToken:]
+ -[ClientConnection setBlockListOverride:]
+ -[EKPredicate calendarRowIDSetForDatabaseID:]
+ GCC_except_table34
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table72
+ _CADEventPredicateDescriptionDateFormatter
+ _CADEventPredicateDescriptionDateFormatter.cold.1
+ _CADEventPredicateDescriptionDateFormatter.formatter
+ _CADEventPredicateDescriptionDateFormatter.onceToken
+ _CADPackedArrayCount
+ _CADPackedArrayFree
+ _CADPackedArrayInsert
+ _CADPackedArrayRead
+ _CADPackedArrayRemove
+ _CADPackedArrayRemoveAll
+ _CFDictionaryCreateMutable
+ _CFDictionaryGetCount
+ _CFDictionaryGetKeysAndValues
+ _CFDictionaryGetValue
+ _CFDictionaryRemoveValue
+ _CFDictionarySetValue
+ _CFNotificationCenterGetLocalCenter
+ _CFTimeZoneCreateWithTimeIntervalFromGMT
+ _CalCalendarCopySharedOwnerAddress
+ _CalDatabaseGetCountOfOriginalCalendarItemsInStore
+ _CalEventCopyOccurrenceDatesInDateRange
+ _CalEventOccurrenceCacheCountByCalendar
+ _CalEventOccurrenceCreate
+ _CalStoreSupportsDefaultAlarms
+ _CalTimeInterval_OneDayInSeconds
+ _EKCalendarItemProperty_hasAttachment
+ _OBJC_CLASS_$_CADBlockList
+ _OBJC_CLASS_$_CADClientBlockOperation
+ _OBJC_CLASS_$_CADEventOccurrenceSet
+ _OBJC_CLASS_$_CADFetchCalendarItemsWithPredicateOperation
+ _OBJC_CLASS_$_CADPredicateMonitorAgent
+ _OBJC_CLASS_$_CADRemovedEventWrapper
+ _OBJC_CLASS_$_CalBlockListWrapper
+ _OBJC_CLASS_$_CalDatabaseChangeReport
+ _OBJC_CLASS_$_NSBlockOperation
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_IVAR_$_CADBlockList._blockList
+ _OBJC_IVAR_$_CADClientBlockOperation._token
+ _OBJC_IVAR_$_CADEventOccurrenceSet._dbCapacity
+ _OBJC_IVAR_$_CADEventOccurrenceSet._dbCount
+ _OBJC_IVAR_$_CADEventOccurrenceSet._dbs
+ _OBJC_IVAR_$_CADFetchCalendarItemsWithPredicateOperation._completion
+ _OBJC_IVAR_$_CADFetchCalendarItemsWithPredicateOperation._connection
+ _OBJC_IVAR_$_CADFetchCalendarItemsWithPredicateOperation._entityType
+ _OBJC_IVAR_$_CADFetchCalendarItemsWithPredicateOperation._predicate
+ _OBJC_IVAR_$_CADFetchCalendarItemsWithPredicateOperation._startCallback
+ _OBJC_IVAR_$_CADFetchCalendarItemsWithPredicateOperation._token
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._conn
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._filter
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._lock
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._occurrences
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._options
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._predicate
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._predicateGeneration
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._resetGeneration
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._shutdown
+ _OBJC_IVAR_$_CADPredicateMonitorAgent._token
+ _OBJC_IVAR_$_CADRemovedEventWrapper._removedDates
+ _OBJC_IVAR_$_CADRemovedEventWrapper._rowID
+ _OBJC_IVAR_$_ClientConnection._agentLock
+ _OBJC_IVAR_$_ClientConnection._agents
+ _OBJC_IVAR_$_ClientConnection._blockListOverride
+ _OBJC_IVAR_$_EKPredicate._databaseToCalendarRowIDSets
+ _OBJC_METACLASS_$_CADBlockList
+ _OBJC_METACLASS_$_CADClientBlockOperation
+ _OBJC_METACLASS_$_CADEventOccurrenceSet
+ _OBJC_METACLASS_$_CADFetchCalendarItemsWithPredicateOperation
+ _OBJC_METACLASS_$_CADPredicateMonitorAgent
+ _OBJC_METACLASS_$_CADRemovedEventWrapper
+ _OBJC_METACLASS_$_NSBlockOperation
+ __OBJC_$_CLASS_METHODS_CADClientBlockOperation
+ __OBJC_$_CLASS_METHODS_CADFetchCalendarItemsWithPredicateOperation
+ __OBJC_$_CLASS_METHODS_CADRemovedEventWrapper
+ __OBJC_$_CLASS_PROP_LIST_CADRemovedEventWrapper
+ __OBJC_$_INSTANCE_METHODS_CADBlockList
+ __OBJC_$_INSTANCE_METHODS_CADClientBlockOperation
+ __OBJC_$_INSTANCE_METHODS_CADEventOccurrenceSet
+ __OBJC_$_INSTANCE_METHODS_CADFetchCalendarItemsWithPredicateOperation
+ __OBJC_$_INSTANCE_METHODS_CADPredicateMonitorAgent
+ __OBJC_$_INSTANCE_METHODS_CADRemovedEventWrapper
+ __OBJC_$_INSTANCE_VARIABLES_CADBlockList
+ __OBJC_$_INSTANCE_VARIABLES_CADClientBlockOperation
+ __OBJC_$_INSTANCE_VARIABLES_CADEventOccurrenceSet
+ __OBJC_$_INSTANCE_VARIABLES_CADFetchCalendarItemsWithPredicateOperation
+ __OBJC_$_INSTANCE_VARIABLES_CADPredicateMonitorAgent
+ __OBJC_$_INSTANCE_VARIABLES_CADRemovedEventWrapper
+ __OBJC_$_PROP_LIST_CADClientAgent
+ __OBJC_$_PROP_LIST_CADClientBlockOperation
+ __OBJC_$_PROP_LIST_CADClientOperation
+ __OBJC_$_PROP_LIST_CADFetchCalendarItemsWithPredicateOperation
+ __OBJC_$_PROP_LIST_CADPredicateMonitorAgent
+ __OBJC_$_PROP_LIST_CADRemovedEventWrapper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CADClientAgent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CADClientOperation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CADClientAgent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CADClientOperation
+ __OBJC_$_PROTOCOL_REFS_CADClientAgent
+ __OBJC_$_PROTOCOL_REFS_CADClientOperation
+ __OBJC_CLASS_PROTOCOLS_$_CADClientBlockOperation
+ __OBJC_CLASS_PROTOCOLS_$_CADFetchCalendarItemsWithPredicateOperation
+ __OBJC_CLASS_PROTOCOLS_$_CADPredicateMonitorAgent
+ __OBJC_CLASS_PROTOCOLS_$_CADRemovedEventWrapper
+ __OBJC_CLASS_RO_$_CADBlockList
+ __OBJC_CLASS_RO_$_CADClientBlockOperation
+ __OBJC_CLASS_RO_$_CADEventOccurrenceSet
+ __OBJC_CLASS_RO_$_CADFetchCalendarItemsWithPredicateOperation
+ __OBJC_CLASS_RO_$_CADPredicateMonitorAgent
+ __OBJC_CLASS_RO_$_CADRemovedEventWrapper
+ __OBJC_LABEL_PROTOCOL_$_CADClientAgent
+ __OBJC_LABEL_PROTOCOL_$_CADClientOperation
+ __OBJC_METACLASS_RO_$_CADBlockList
+ __OBJC_METACLASS_RO_$_CADClientBlockOperation
+ __OBJC_METACLASS_RO_$_CADEventOccurrenceSet
+ __OBJC_METACLASS_RO_$_CADFetchCalendarItemsWithPredicateOperation
+ __OBJC_METACLASS_RO_$_CADPredicateMonitorAgent
+ __OBJC_METACLASS_RO_$_CADRemovedEventWrapper
+ __OBJC_PROTOCOL_$_CADClientAgent
+ __OBJC_PROTOCOL_$_CADClientOperation
+ ___106-[CADPredicateMonitorAgent reportResultsReset:newAndUpdated:removed:reportPredicateGeneration:generation:]_block_invoke
+ ___106-[CADPredicateMonitorAgent reportResultsReset:newAndUpdated:removed:reportPredicateGeneration:generation:]_block_invoke.37
+ ___137+[CADFetchCalendarItemsWithPredicateOperation performSynchronouslyWithPredicate:entityType:connection:fetchIdentifier:cancellationToken:]_block_invoke
+ ___137+[CADFetchCalendarItemsWithPredicateOperation performSynchronouslyWithPredicate:entityType:connection:fetchIdentifier:cancellationToken:]_block_invoke_2
+ ___137+[CADFetchCalendarItemsWithPredicateOperation performSynchronouslyWithPredicate:entityType:connection:fetchIdentifier:cancellationToken:]_block_invoke_3
+ ___149-[CADXPCImplementation(CADEventOperationGroup) CADOccurrenceCacheGetOccurrenceCountOrSumDurationWithStartDate:endDate:calendarIDs:sumDuration:reply:]_block_invoke
+ ___33-[CADPredicateMonitorAgent reset]_block_invoke
+ ___33-[CADPredicateMonitorAgent reset]_block_invoke_2
+ ___33-[CADServer _setUpSignalHandlers]_block_invoke.61
+ ___33-[CADServer _setUpSignalHandlers]_block_invoke.62
+ ___33-[CADServer _setUpSignalHandlers]_block_invoke.63
+ ___38-[CADServer _registerForNotifications]_block_invoke.83
+ ___47-[CADPredicateMonitorAgent handleChangeReport:]_block_invoke
+ ___48-[CADPredicateMonitorAgent filterWithPredicate:]_block_invoke
+ ___48-[CADPredicateMonitorAgent filterWithPredicate:]_block_invoke_2
+ ___48-[CADPredicateMonitorAgent filterWithPredicate:]_block_invoke_3
+ ___62-[CADPredicateMonitorAgent processChangeReport:forDatabaseID:]_block_invoke
+ ___62-[CADPredicateMonitorAgent processChangeReport:forDatabaseID:]_block_invoke_2
+ ___63+[CADConferenceUtils _performConferenceURLRenewalWithDatabase:]_block_invoke.34
+ ___78-[CADPredicateMonitorAgent updatePredicate:propertyFilter:options:generation:]_block_invoke
+ ___78-[CADPredicateMonitorAgent updatePredicate:propertyFilter:options:generation:]_block_invoke_2
+ ___78-[CADPredicateMonitorAgent updatePredicate:propertyFilter:options:generation:]_block_invoke_3
+ ___93-[CADXPCImplementation(CADSourceOperationGroup) CADCountOriginalCalendarItemsBySource:reply:]_block_invoke
+ ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.193
+ ___CADEventPredicateDescriptionDateFormatter_block_invoke
+ ___CalDatabaseChangeReportAvailableNotification
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r96l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_112_e8_32s40s48s56s64r72r80r88r96r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8r64l8s56l8r72l8r80l8r88l8r96l8
+ ___block_descriptor_116_e8_32s40s48s56s64s72s80s88r96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8s64l8r88l8r96l8s72l8s80l8
+ ___block_descriptor_124_e8_32s40s48s56s64s72s80s88r96r_e26_B32?0i8B12Q16"NSArray"24ls32l8s40l8r88l8s48l8s56l8s64l8s72l8r96l8s80l8
+ ___block_descriptor_32_e341_B24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16l
+ ___block_descriptor_32_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20l
+ ___block_descriptor_33_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24l
+ ___block_descriptor_36_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12l
+ ___block_descriptor_40_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20l
+ ___block_descriptor_40_e8_32bs_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8
+ ___block_descriptor_40_e8_32bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8
+ ___block_descriptor_40_e8_32bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20ls32l8
+ ___block_descriptor_40_e8_32bs_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8
+ ___block_descriptor_40_e8_32r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8
+ ___block_descriptor_40_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr32l8
+ ___block_descriptor_40_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr32l8
+ ___block_descriptor_40_e8_32s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8
+ ___block_descriptor_40_e8_32s_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8
+ ___block_descriptor_41_e8_32r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8
+ ___block_descriptor_44_e8_32bs_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls32l8
+ ___block_descriptor_44_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr32l8
+ ___block_descriptor_44_e8_32r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20lr32l8
+ ___block_descriptor_44_e8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr32l8
+ ___block_descriptor_48_e8_32s40bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8
+ ___block_descriptor_49_e8_32s40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8
+ ___block_descriptor_52_e8_32bs40r_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls32l8r40l8
+ ___block_descriptor_52_e8_32r40r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr32l8r40l8
+ ___block_descriptor_52_e8_32s40bs_e337_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8ls40l8s32l8
+ ___block_descriptor_52_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr40l8s32l8
+ ___block_descriptor_52_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_56_e8_32s40bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20ls40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32r40r48r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^v20lr32l8r40l8r48l8
+ ___block_descriptor_57_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e349_v24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8"NSArray"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8
+ ___block_descriptor_65_e8_32s40s48r56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s56l8s48l8
+ ___block_descriptor_68_e8_32s40r_e17_v16?0"NSArray"8ls32l8r40l8
+ ___block_descriptor_68_e8_32s40s48s56s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40r48r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r40l8r48l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8r64l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr48l8r56l8s32l8s40l8r64l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8r64l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e8_v12?0i8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40r48r56r64r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr40l8s32l8r48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48r56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48r56w_e5_v8?0ls32l8w56l8r48l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e345_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^v16^B24ls32l8s40l8s56l8r64l8s48l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r56l8s40l8r64l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r64l8s40l8s48l8r72l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8r64l8s56l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8s56l8s64l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s_e8_v12?0i8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56s64r72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72r80r_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20lr72l8s32l8s40l8s48l8r80l8s56l8s64l8
+ ___block_literal_global.107
+ ___block_literal_global.119
+ ___block_literal_global.129
+ ___block_literal_global.131
+ ___block_literal_global.273
+ ___block_literal_global.368
+ ___block_literal_global.40
+ ___block_literal_global.64
+ ___block_literal_global.66
+ ___block_literal_global.88
+ _malloc_type_realloc
+ _objc_msgSend$CADClientReceivePredicateResults:forToken:
+ _objc_msgSend$CADDatabaseCancelFetchRequestWithIdentifier:
+ _objc_msgSend$CalDateByComponentwiseAddingComponents:inCalendar:
+ _objc_msgSend$CalGregorianCalendarForTimeZone:
+ _objc_msgSend$CalIsBeforeOrSameAsDate:
+ _objc_msgSend$_poolForPath:auxDatabaseID:
+ _objc_msgSend$addAgent:
+ _objc_msgSend$addExecutionBlock:
+ _objc_msgSend$addOccurrenceWithDB:rowID:date:
+ _objc_msgSend$agentWithToken:
+ _objc_msgSend$blockList
+ _objc_msgSend$blockListOverride
+ _objc_msgSend$blockOperationWithToken:block:
+ _objc_msgSend$calendarRowIDSetForDatabaseID:
+ _objc_msgSend$cancelOperationsWithToken:
+ _objc_msgSend$copyWithStartDate:endDate:
+ _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$datesForDatabase:rowID:
+ _objc_msgSend$enumerateDatabases:
+ _objc_msgSend$enumerateImpactedEvents:
+ _objc_msgSend$enumerateOccurrenceRowIDsInDatabase:block:
+ _objc_msgSend$excludeSkippedReminders
+ _objc_msgSend$filterWithPredicate:
+ _objc_msgSend$generateDatesForEvent:
+ _objc_msgSend$handleDistributeChangeReport:
+ _objc_msgSend$handlePostChangeNote:connection:processName:
+ _objc_msgSend$hasDatabaseAtPath:withDatabaseID:
+ _objc_msgSend$hasMailto
+ _objc_msgSend$hasTel
+ _objc_msgSend$incrementalPredicatesToExpandResultsFromPredicate:filteringRequiredToRemoveEventsNoLongerMatched:
+ _objc_msgSend$infoForDB:
+ _objc_msgSend$initWithBlockList:
+ _objc_msgSend$initWithPredicate:filter:options:token:connection:
+ _objc_msgSend$initWithRowID:removedDates:
+ _objc_msgSend$initWithToken:
+ _objc_msgSend$isBlockListEmpty
+ _objc_msgSend$isBlockedWithEmail:
+ _objc_msgSend$isBlockedWithPhoneNumber:
+ _objc_msgSend$isEmpty
+ _objc_msgSend$isEventBlocked:
+ _objc_msgSend$isSharedCalendarOwnerBlocked:
+ _objc_msgSend$matchesIgnoringDate:database:
+ _objc_msgSend$matchingDate:
+ _objc_msgSend$matchingDatesForEvent:modifiedProperties:dates:inRange:database:outReset:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$processChangeReport:forDatabaseID:
+ _objc_msgSend$range
+ _objc_msgSend$removeAgentWithToken:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$reportResultsReset:newAndUpdated:removed:databaseIDForRemovals:reportPredicateGeneration:generation:
+ _objc_msgSend$reportResultsReset:newAndUpdated:removed:reportPredicateGeneration:generation:
+ _objc_msgSend$resetRequiredForRemovalOfMatchingOccurrence
+ _objc_msgSend$setDay:
+ _objc_msgSend$setExcludeAllDayEvents:
+ _objc_msgSend$setExcludeDeclined:
+ _objc_msgSend$setExcludeDeclinedUnlessProposed:
+ _objc_msgSend$setExcludeNoAttendeeEvents:
+ _objc_msgSend$setExcludeNoLocationEvents:
+ _objc_msgSend$setExcludeProposed:
+ _objc_msgSend$setExcludeTimedEvents:
+ _objc_msgSend$setFilteredOutTitles:
+ _objc_msgSend$setOccurrenceDatesWithDB:rowID:dates:outRemovedDates:outAddedAnyDates:
+ _objc_msgSend$setPredicate:
+ _objc_msgSend$setSecond:
+ _objc_msgSend$setStartCallback:
+ _objc_msgSend$sharedBlockList
+ _objc_msgSend$stop
+ _objc_msgSend$stringRemovingTel
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
+ _objc_msgSend$updatePredicate:propertyFilter:options:generation:
+ _object_getClassName
+ _xpc_dictionary_get_data
- +[_CADFetchCalendarItemsWithPredicateOperation isJunkEvent:]
- +[_CADFetchCalendarItemsWithPredicateOperation performSynchronouslyWithPredicate:entityType:connection:fetchIdentifier:cancellationToken:]
- +[_CADFetchCalendarItemsWithPredicateOperation queryDatabase:withID:predicate:connection:serializer:cancellationToken:]
- -[CADDatabaseSingleConnectionProvider _databaseRestoreGenerationChanged:]
- -[CADDatabaseSingleConnectionProvider database:restoreGenerationChangedExternally:]
- -[CADDatabaseSingleConnectionProvider databaseRestoreGenerationChanged:]
- -[CADEventPredicate predicateFormat].cold.1
- -[ClientConnection operations]
- -[_CADFetchCalendarItemsWithPredicateOperation .cxx_destruct]
- -[_CADFetchCalendarItemsWithPredicateOperation cancel]
- -[_CADFetchCalendarItemsWithPredicateOperation fetchIdentifier]
- -[_CADFetchCalendarItemsWithPredicateOperation initWithPredicate:entityType:connection:fetchIdentifier:completionHandler:]
- -[_CADFetchCalendarItemsWithPredicateOperation main]
- GCC_except_table35
- GCC_except_table55
- GCC_except_table64
- GCC_except_table67
- _CalDatabaseClearRestoreGenerationChangedDelegate
- _CalDatabaseSetRestoreGenerationChangedDelegate
- _OBJC_CLASS_$__CADFetchCalendarItemsWithPredicateOperation
- _OBJC_IVAR_$_CADDatabaseSingleConnectionProvider._databaseRestoreGeneration
- _OBJC_IVAR_$__CADFetchCalendarItemsWithPredicateOperation._completion
- _OBJC_IVAR_$__CADFetchCalendarItemsWithPredicateOperation._connection
- _OBJC_IVAR_$__CADFetchCalendarItemsWithPredicateOperation._entityType
- _OBJC_IVAR_$__CADFetchCalendarItemsWithPredicateOperation._fetchIdentifier
- _OBJC_IVAR_$__CADFetchCalendarItemsWithPredicateOperation._predicate
- _OBJC_METACLASS_$__CADFetchCalendarItemsWithPredicateOperation
- __OBJC_$_CLASS_METHODS__CADFetchCalendarItemsWithPredicateOperation
- __OBJC_$_INSTANCE_METHODS__CADFetchCalendarItemsWithPredicateOperation
- __OBJC_$_INSTANCE_VARIABLES__CADFetchCalendarItemsWithPredicateOperation
- __OBJC_$_PROP_LIST__CADFetchCalendarItemsWithPredicateOperation
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CalCalendarDatabaseRestoreGenerationChangedDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CalCalendarDatabaseRestoreGenerationChangedDelegate
- __OBJC_$_PROTOCOL_REFS_CalCalendarDatabaseRestoreGenerationChangedDelegate
- __OBJC_CLASS_PROTOCOLS_$__CADFetchCalendarItemsWithPredicateOperation
- __OBJC_CLASS_RO_$__CADFetchCalendarItemsWithPredicateOperation
- __OBJC_LABEL_PROTOCOL_$_CalCalendarDatabaseRestoreGenerationChangedDelegate
- __OBJC_METACLASS_RO_$__CADFetchCalendarItemsWithPredicateOperation
- __OBJC_PROTOCOL_$_CalCalendarDatabaseRestoreGenerationChangedDelegate
- ___138+[_CADFetchCalendarItemsWithPredicateOperation performSynchronouslyWithPredicate:entityType:connection:fetchIdentifier:cancellationToken:]_block_invoke
- ___138+[_CADFetchCalendarItemsWithPredicateOperation performSynchronouslyWithPredicate:entityType:connection:fetchIdentifier:cancellationToken:]_block_invoke_2
- ___138+[_CADFetchCalendarItemsWithPredicateOperation performSynchronouslyWithPredicate:entityType:connection:fetchIdentifier:cancellationToken:]_block_invoke_3
- ___33-[CADServer _setUpSignalHandlers]_block_invoke.44
- ___33-[CADServer _setUpSignalHandlers]_block_invoke.45
- ___33-[CADServer _setUpSignalHandlers]_block_invoke.46
- ___36-[CADEventPredicate predicateFormat]_block_invoke
- ___38-[CADServer _registerForNotifications]_block_invoke.66
- ___39-[CADXPCProxyHelper forwardInvocation:]_block_invoke.cold.4
- ___63+[CADConferenceUtils _performConferenceURLRenewalWithDatabase:]_block_invoke.16
- ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.190
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r96l8s64l8s72l8s80l8s88l8
- ___block_descriptor_112_e8_32s40s48s56s64r72r80r88r96r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8r64l8s56l8r72l8r80l8r88l8r96l8
- ___block_descriptor_116_e8_32s40s48s56s64s72s80s88r96r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8s64l8r88l8r96l8s72l8s80l8
- ___block_descriptor_32_e343_B24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8^v16l
- ___block_descriptor_32_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20l
- ___block_descriptor_33_e347_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8^v16^B24l
- ___block_descriptor_36_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12l
- ___block_descriptor_40_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20l
- ___block_descriptor_40_e8_32bs_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8
- ___block_descriptor_40_e8_32bs_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8
- ___block_descriptor_40_e8_32bs_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^v20ls32l8
- ___block_descriptor_40_e8_32bs_e354_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}20ls32l8
- ___block_descriptor_40_e8_32r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr32l8
- ___block_descriptor_40_e8_32r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20lr32l8
- ___block_descriptor_40_e8_32r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^v20lr32l8
- ___block_descriptor_40_e8_32s_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8
- ___block_descriptor_40_e8_32s_e347_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8^v16^B24ls32l8
- ___block_descriptor_40_e8_32s_e354_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}20ls32l8
- ___block_descriptor_41_e8_32r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr32l8
- ___block_descriptor_44_e8_32bs_e339_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8ls32l8
- ___block_descriptor_44_e8_32r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^v20lr32l8
- ___block_descriptor_44_e8_32r_e354_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}20lr32l8
- ___block_descriptor_48_e8_32r40r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20lr32l8r40l8
- ___block_descriptor_48_e8_32r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20lr32l8
- ___block_descriptor_48_e8_32s40bs_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls40l8s32l8
- ___block_descriptor_48_e8_32s40r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e347_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8^v16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e354_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}20lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e354_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}20ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8s40l8
- ___block_descriptor_49_e8_32s40r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r40l8
- ___block_descriptor_52_e8_32bs40r_e339_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8ls32l8r40l8
- ___block_descriptor_52_e8_32r40r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr32l8r40l8
- ___block_descriptor_52_e8_32s40bs_e339_v16?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8ls40l8s32l8
- ___block_descriptor_52_e8_32s40r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^v20lr40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^v20ls40l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^v20ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e354_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}20ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e347_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8^v16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e354_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}20ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32r40r48r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^v20lr32l8r40l8r48l8
- ___block_descriptor_57_e8_32s40r48r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40r48r56r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40r48r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr40l8s32l8r48l8
- ___block_descriptor_64_e8_32s40r48r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40r48r_e354_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}20lr40l8r48l8s32l8
- ___block_descriptor_64_e8_32s40s48r56r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r48l8s40l8r56l8
- ___block_descriptor_64_e8_32s40s48r56r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40s48r56r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8r48l8s40l8r56l8
- ___block_descriptor_64_e8_32s40s48r56r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40s48r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8s40l8r56l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e351_v24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8"NSArray"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48r56r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8
- ___block_descriptor_65_e8_32s40s48s56bs_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40r48r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r40l8r48l8
- ___block_descriptor_72_e8_32s40s48bs56r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr48l8r56l8s32l8s40l8r64l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8r48l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20lr48l8r56l8s32l8s40l8r64l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8s40l8r48l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r56l8s40l8r64l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r56l8s40l8s48l8r64l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56s_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40r48r56r64r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20lr40l8s32l8r48l8r56l8r64l8
- ___block_descriptor_80_e8_32s40s48r56r64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r48l8s40l8r56l8r64l8
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e347_v32?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8^v16^B24ls32l8s40l8s56l8r64l8s48l8r72l8
- ___block_descriptor_80_e8_32s40s48s56r64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r56l8s40l8r64l8s48l8
- ___block_descriptor_80_e8_32s40s48s56r64r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8r64l8s40l8s48l8r72l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8r64l8s56l8r72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8s56l8s64l8r72l8
- ___block_descriptor_81_e8_32s40s48s56s64r72r_e342_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_descriptor_89_e8_32s40s48s56s64s72r80r_e346_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}12^B20lr72l8s32l8s40l8s48l8r80l8s56l8s64l8
- ___block_literal_global.113
- ___block_literal_global.115
- ___block_literal_global.356
- ___block_literal_global.49
- ___block_literal_global.51
- ___block_literal_global.62
- ___block_literal_global.65
- ___block_literal_global.71
- ___block_literal_global.82
- ___block_literal_global.85
- ___block_literal_global.90
- _objc_msgSend$_databaseRestoreGenerationChanged:
- _objc_msgSend$fetchIdentifier
- _objc_msgSend$operations
- _objc_msgSend$replyID
- _os_unfair_lock_assert_not_owner
- _predicateFormat.formatter
- _predicateFormat.onceToken
CStrings:
+ "\t"
+ "; cals:%@"
+ "; end:%@"
+ "; exclusions:["
+ "; filteredOutTitles:[%lu]"
+ "; limit:%ld"
+ "; randomize:YES"
+ "; start:%@"
+ "@\"<CalBlockList>\""
+ "@\"CADEventOccurrenceSet\""
+ "@\"NSArray\"24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "@\"NSString\"32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "@20@0:8I16"
+ "@24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "@24@0:8i16i20"
+ "@28@0:8I16@?20"
+ "@28@0:8i16@20"
+ "@32@0:8@16^B24"
+ "@32@0:8Q16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "@32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "@32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
+ "@36@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24@?28"
+ "@40@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16^v24@32"
+ "@48@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32^B40"
+ "@48@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32^i40"
+ "@48@0:8@16i24@28I36@40"
+ "@48@0:8@16i24@28I36@?40"
+ "@52@0:8@16Q24Q32i40@44"
+ "@56@0:8@16@24@32^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}40^i48"
+ "@64@0:8^v16Q24@32@40^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}48^B56"
+ "@76@0:8@16@24@32^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}40Q48i56^@60^i68"
+ "Asked to update predicate monitor %i, but it doesn't exist"
+ "Asked to update predicate monitor %i, but it is actually a %s"
+ "B20@0:8I16"
+ "B24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "B24@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8^v16"
+ "B32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "B32@0:8i16i20@24"
+ "B32@?0i8B12Q16@\"NSArray\"24"
+ "B40@0:8Q16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "B44@0:8@\"CADPooledDatabaseConfiguration\"16Q24i32@?<v@?^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}>36"
+ "B44@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32B40"
+ "B44@0:8^{__CFArray=}16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32B40"
+ "B48@0:8i16i20@24@32^B40"
+ "B52@0:8@16Q24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32@40B48"
+ "CADBlockList"
+ "CADClientAgent"
+ "CADClientBlockOperation"
+ "CADClientOperation"
+ "CADClientReceivePredicateResults:forToken:"
+ "CADCountOriginalCalendarItemsBySource:reply:"
+ "CADDatabaseMonitorResultsForPredicate:propertyFilter:options:identifier:reply:"
+ "CADDatabaseMonitorUpdatePredicate:propertyFilter:options:identifier:generation:reply:"
+ "CADDatabaseStopMonitoringPredicate:"
+ "CADEventOccurrenceSet"
+ "CADFetchCalendarItemsWithPredicateOperation"
+ "CADOccurrenceCacheGetOccurrenceCountOrSumDurationWithStartDate:endDate:calendarIDs:sumDuration:reply:"
+ "CADPredicateMonitorAgent"
+ "CADRemovedEventWrapper"
+ "CalDateByComponentwiseAddingComponents:inCalendar:"
+ "CalGregorianCalendarForTimeZone:"
+ "CalIsBeforeOrSameAsDate:"
+ "Could not fetch calendars from calendar IDs: %@"
+ "Couldn't find event with id %i"
+ "Error sending predicate results: %@"
+ "Failed to deserialize report: %@"
+ "Index %lu beyond bounds %lu"
+ "Index (%lu) beyond bounds (%i)"
+ "Invalid database path"
+ "No change report found to distribute"
+ "No database path with change report"
+ "Q24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "Skipping notificable event %d because organizer is blocked"
+ "Skipping shared calendar invitation for calendar %d because the owner is blocked"
+ "T@\"<CalBlockList>\",&,N,V_blockListOverride"
+ "T@\"CADPredicate\",&,N,V_predicate"
+ "T@\"NSArray\",R,N,V_removedDates"
+ "T@?,C,N,V_startCallback"
+ "TI,R,N"
+ "T^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB},N,V_database"
+ "Ti,R,N"
+ "Ti,R,N,V_rowID"
+ "Told to reset while filtering old results: %i %i; predicate=%@"
+ "^v64@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32^v40@48Q56"
+ "^{?=i^{__CFDictionary}}"
+ "^{?=i^{__CFDictionary}}20@0:8i16"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@0:8"
+ "_agentLock"
+ "_agents"
+ "_blockList"
+ "_blockListOverride"
+ "_databaseToCalendarRowIDSets"
+ "_dbCapacity"
+ "_dbCount"
+ "_dbs"
+ "_filter"
+ "_occurrences"
+ "_poolForPath:auxDatabaseID:"
+ "_predicateGeneration"
+ "_removedDates"
+ "_resetGeneration"
+ "_shutdown"
+ "_startCallback"
+ "addAgent:"
+ "addExecutionBlock:"
+ "addOccurrenceWithDB:rowID:date:"
+ "agentWithToken:"
+ "allday,"
+ "blockList"
+ "blockListOverride"
+ "blockOperationWithToken:block:"
+ "calendarRowIDSetForDatabaseID:"
+ "cancelOperationsWithToken:"
+ "com_apple_mobilecal_current_user_participation_status"
+ "concisePublicDescription"
+ "copyWithStartDate:endDate:"
+ "d32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "d40@0:8^v16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "d40@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24^@32"
+ "d40@0:8^v16d24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "datesForDatabase:rowID:"
+ "declined,"
+ "declinedUnlessProposed,"
+ "distribute_change_report"
+ "enumerateDatabases:"
+ "enumerateImpactedEvents:"
+ "enumerateOccurrenceRowIDsInDatabase:block:"
+ "filterWithPredicate:"
+ "generateDatesForEvent:"
+ "generation"
+ "handleChangeReport:"
+ "handleDistributeChangeReport:"
+ "handlePostChangeNote:connection:processName:"
+ "hasDatabaseAtPath:withDatabaseID:"
+ "hasMailto"
+ "hasTel"
+ "i24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "i32@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "i32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "i40@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "i40@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32"
+ "i44@0:8^v16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32i40"
+ "i56@0:8@16@24@32@40^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}48"
+ "incrementalPredicatesToExpandResultsFromPredicate:filteringRequiredToRemoveEventsNoLongerMatched:"
+ "infoForDB:"
+ "initWithBlockList:"
+ "initWithPredicate:filter:options:token:connection:"
+ "initWithRowID:removedDates:"
+ "initWithToken:"
+ "isBlockListEmpty"
+ "isBlockedWithEmail:"
+ "isBlockedWithPhoneNumber:"
+ "isEmpty"
+ "isEventBlocked:"
+ "isSharedCalendarOwnerBlocked:"
+ "matchesIgnoringDate:database:"
+ "matchingDate:"
+ "matchingDatesForEvent:modifiedProperties:dates:inRange:database:outReset:"
+ "new"
+ "noAttendee,"
+ "noLocation,"
+ "numberWithLongLong:"
+ "processChangeReport:forDatabaseID:"
+ "proposed,"
+ "range"
+ "removalsByDB"
+ "removeAgentWithToken:"
+ "removeObserver:"
+ "removed"
+ "removedDates"
+ "reportResultsReset:newAndUpdated:removed:databaseIDForRemovals:reportPredicateGeneration:generation:"
+ "reportResultsReset:newAndUpdated:removed:reportPredicateGeneration:generation:"
+ "resetRequiredForRemovalOfMatchingOccurrence"
+ "setBlockListOverride:"
+ "setDay:"
+ "setOccurrenceDatesWithDB:rowID:dates:outRemovedDates:outAddedAnyDates:"
+ "setPredicate:"
+ "setSecond:"
+ "setStartCallback:"
+ "sharedBlockList"
+ "startCallback"
+ "stop"
+ "stringRemovingTel"
+ "supportsEfficientMonitoring"
+ "timed,"
+ "unarchivedObjectOfClass:fromData:error:"
+ "updatePredicate:propertyFilter:options:generation:"
+ "v12@?0i8"
+ "v16@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8"
+ "v20@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}12"
+ "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "v24@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8@\"NSArray\"16"
+ "v28@0:8@\"NSDictionary\"16I24"
+ "v28@0:8@16I24"
+ "v28@?0i8@\"NSArray\"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}20"
+ "v28@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}12^B20"
+ "v28@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}12^v20"
+ "v32@0:8@\"CADObjectID\"16@?<v@?iQ>24"
+ "v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
+ "v32@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8^v16^B24"
+ "v40@0:8@\"CADPooledDatabaseConfiguration\"16Q24@?<v@?i^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}^B>32"
+ "v40@0:8@\"NSMutableSet\"16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "v40@0:8@16Q24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "v40@0:8@16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
+ "v44@0:8@16Q24Q32i40"
+ "v44@0:8B16@20@28B36i40"
+ "v44@0:8i16q20Q28@?36"
+ "v48@0:8B16@20@28i36B40i44"
+ "v52@0:8@\"NSDate\"16@\"NSDate\"24@\"NSArray\"32B40@?<v@?ii>44"
+ "v52@0:8@\"NSPredicate\"16Q24Q32i40@?<v@?i>44"
+ "v52@0:8@16@24@32B40@?44"
+ "v52@0:8@16Q24Q32i40@?44"
+ "v56@0:8@\"NSPredicate\"16Q24Q32i40i44@?<v@?i>48"
+ "v56@0:8@16Q24Q32i40i44@?48"
+ "v56@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32^@40^@48"
+ "v60@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16i24@28@36@44@52"
- "@\"NSArray\"24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16"
- "@\"NSString\"32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24"
- "@24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16"
- "@24@0:8^{CalDatabase=}16"
- "@32@0:8Q16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24"
- "@32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24"
- "@32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16@24"
- "@36@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16i24@?28"
- "@40@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16^v24@32"
- "@48@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32^B40"
- "@48@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32^i40"
- "@48@0:8@16i24@28i36@40"
- "@48@0:8@16i24@28i36@?40"
- "@56@0:8@16@24@32^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}40^i48"
- "@76@0:8@16@24@32^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}40Q48i56^@60^i68"
- "B24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16"
- "B24@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}8^v16"
- "B32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24"
- "B40@0:8Q16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32"
- "B44@0:8@\"CADPooledDatabaseConfiguration\"16Q24i32@?<v@?^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}>36"
- "B44@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24@32B40"
- "B44@0:8^{__CFArray=}16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24@32B40"
- "B52@0:8@16Q24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32@40B48"
- "CalCalendarDatabaseRestoreGenerationChangedDelegate"
- "Database restore generation changed to %d"
- "Q24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16"
- "T^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB},N,V_database"
- "Ti,R,N,V_fetchIdentifier"
- "^v64@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32^v40@48Q56"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16@0:8"
- "_CADFetchCalendarItemsWithPredicateOperation"
- "_databaseRestoreGenerationChanged:"
- "_fetchIdentifier"
- "d32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24"
- "d40@0:8^v16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32"
- "d40@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24^@32"
- "d40@0:8^v16d24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32"
- "database:restoreGenerationChangedExternally:"
- "databaseRestoreGenerationChanged:"
- "fetchIdentifier"
- "i24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16"
- "i32@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24"
- "i32@0:8^v16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24"
- "i40@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32"
- "i40@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24@32"
- "i44@0:8^v16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32i40"
- "i56@0:8@16@24@32@40^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}48"
- "operations"
- "v16@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}8"
- "v20@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}12"
- "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16"
- "v24@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}8@\"NSArray\"16"
- "v28@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16i24"
- "v28@?0i8@\"NSArray\"12^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}20"
- "v28@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}12^B20"
- "v28@?0i8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}12^v20"
- "v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16@24"
- "v32@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}8^v16^B24"
- "v40@0:8@\"CADPooledDatabaseConfiguration\"16Q24@?<v@?i^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}^B>32"
- "v40@0:8@\"NSMutableSet\"16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32"
- "v40@0:8@16Q24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32"
- "v40@0:8@16^v24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32"
- "v56@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24@32^@40^@48"
- "v60@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16i24@28@36@44@52"

```
