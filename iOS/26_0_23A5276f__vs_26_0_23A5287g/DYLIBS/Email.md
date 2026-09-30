## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3856.100.4.0.0
-  __TEXT.__text: 0xdb080
+3858.100.10.2.1
+  __TEXT.__text: 0xde850
   __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0xd37c
-  __TEXT.__gcc_except_tab: 0x1d150
-  __TEXT.__const: 0x11c8
-  __TEXT.__cstring: 0xb9ac
-  __TEXT.__oslogstring: 0x63a3
+  __TEXT.__objc_methlist: 0xd3f4
+  __TEXT.__gcc_except_tab: 0x1dac4
+  __TEXT.__const: 0x11b8
+  __TEXT.__cstring: 0xbbdc
+  __TEXT.__oslogstring: 0x6943
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x154
   __TEXT.__constg_swiftt: 0x3e8

   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7fe8
+  __TEXT.__unwind_info: 0x8218
   __TEXT.__eh_frame: 0x1f8
-  __TEXT.__objc_classname: 0x1bda
-  __TEXT.__objc_methname: 0x1c542
-  __TEXT.__objc_methtype: 0x4c85
-  __TEXT.__objc_stubs: 0x12740
-  __DATA_CONST.__got: 0xc98
-  __DATA_CONST.__const: 0x4718
-  __DATA_CONST.__objc_classlist: 0x5a8
+  __TEXT.__objc_classname: 0x1bf4
+  __TEXT.__objc_methname: 0x1c8b8
+  __TEXT.__objc_methtype: 0x4c93
+  __TEXT.__objc_stubs: 0x12cc0
+  __DATA_CONST.__got: 0xcc0
+  __DATA_CONST.__const: 0x48a0
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6100
+  __DATA_CONST.__objc_selrefs: 0x6268
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__auth_got: 0xa88
-  __AUTH_CONST.__const: 0x19c8
-  __AUTH_CONST.__cfstring: 0x98e0
-  __AUTH_CONST.__objc_const: 0x17620
+  __AUTH_CONST.__const: 0x1a08
+  __AUTH_CONST.__cfstring: 0x9d20
+  __AUTH_CONST.__objc_const: 0x17650
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x6e0
+  __AUTH.__objc_data: 0x730
   __AUTH.__data: 0x200
-  __DATA.__objc_ivar: 0xcd0
+  __DATA.__objc_ivar: 0xcc8
   __DATA.__data: 0x2a08
-  __DATA.__bss: 0x1db0
+  __DATA.__bss: 0x1dc0
   __DATA_DIRTY.__objc_data: 0x3368
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x640
+  __DATA_DIRTY.__bss: 0x650
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter
   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec
   - /System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing
   - /System/Library/PrivateFrameworks/EmailCore.framework/EmailCore
   - /System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F0BA582C-FBF3-3659-A880-FE1391085010
-  Functions: 5017
-  Symbols:   18596
-  CStrings:  8598
+  UUID: 8DC03722-C680-37E6-9C89-A0B6BCABE048
+  Functions: 5042
+  Symbols:   18732
+  CStrings:  8732
 
Symbols:
+ +[EMMessageListItemPredicates isPredicateForMessagesInConversations:conversationIDs:]
+ +[EMParsecInstantAnswers dictionaryFromTimezone:]
+ +[EMParsecInstantAnswers flightInformationWithAirlineCode:flightNumber:flightDate:]
+ +[EMParsecInstantAnswers formattedDate:withTimezone:]
+ +[EMParsecInstantAnswers log]
+ +[EMParsecInstantAnswers sfAirportToDictionnary:]
+ +[EMParsecInstantAnswers sfFlightStatusToString:]
+ +[EMParsecInstantAnswers sfFlightsToDictionary:]
+ +[EMParsecInstantAnswers updatedFlightURLForInstantAnswer:]
+ +[EMParsecInstantAnswers utcFormatter]
+ +[EMParsecInstantAnswers utcFormatter].cold.1
+ -[EMCategorizationSyncManager primaryIcloudMailboxFuture]
+ -[EMCoreAnalyticsCollector blocks]
+ -[EMCoreAnalyticsCollector registerForLogEventsWithBlock:]
+ -[EMInstantAnswerFlight setCheckInUrl:]
+ -[EMMessageList enumerateObserversWithLastBlock:]
+ -[EMRemoteContentURLSession dataTaskWithRequest:isSynthetic:allowProxying:failOpen:background:completionHandler:]
+ -[EMRemoteContentURLSession syntheticDataTaskWithRequest:failOpen:background:completionHandler:]
+ GCC_except_table167
+ GCC_except_table168
+ _OBJC_CLASS_$_EMParsecInstantAnswers
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$_PARRequest
+ _OBJC_CLASS_$_PARSession
+ _OBJC_CLASS_$_PARSessionConfiguration
+ _OBJC_IVAR_$_EMCoreAnalyticsCollector._blocks
+ _OBJC_IVAR_$_EMCoreAnalyticsCollector._didRegister
+ _OBJC_METACLASS_$_EMParsecInstantAnswers
+ __OBJC_$_CLASS_METHODS_EMParsecInstantAnswers
+ __OBJC_CLASS_RO_$_EMParsecInstantAnswers
+ __OBJC_METACLASS_RO_$_EMParsecInstantAnswers
+ ___113-[EMRemoteContentURLSession dataTaskWithRequest:isSynthetic:allowProxying:failOpen:background:completionHandler:]_block_invoke
+ ___113-[EMRemoteContentURLSession dataTaskWithRequest:isSynthetic:allowProxying:failOpen:background:completionHandler:]_block_invoke.140
+ ___146-[EMCategorizationSyncManager categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]_block_invoke.25
+ ___146-[EMCategorizationSyncManager categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]_block_invoke.27
+ ___146-[EMCategorizationSyncManager categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]_block_invoke.27.cold.1
+ ___29+[EMParsecInstantAnswers log]_block_invoke
+ ___38+[EMParsecInstantAnswers utcFormatter]_block_invoke
+ ___38-[EMQueryingCollection stopObserving:]_block_invoke_2
+ ___39-[EMQueryingCollection beginObserving:]_block_invoke.23
+ ___39-[EMQueryingCollection beginObserving:]_block_invoke_2
+ ___39-[EMQueryingCollection beginObserving:]_block_invoke_2.24
+ ___44-[EMCoreAnalyticsCollector logOneTimeEvent:]_block_invoke.27
+ ___44-[EMQueryingCollection _cancelQueryIfNeeded]_block_invoke_2
+ ___49-[EMMessageList enumerateObserversWithLastBlock:]_block_invoke
+ ___49-[EMMessageList enumerateObserversWithLastBlock:]_block_invoke_2
+ ___49-[EMQueryingCollection queryDidFinishInitialLoad]_block_invoke.31
+ ___49-[EMQueryingCollection queryDidFinishInitialLoad]_block_invoke.34
+ ___49-[EMQueryingCollection queryDidFinishInitialLoad]_block_invoke_2.35
+ ___52-[EMQueryingCollection enumerateObserversWithBlock:]_block_invoke
+ ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.171
+ ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.171.cold.1
+ ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.173
+ ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke_2.170
+ ___57-[EMCategorizationSyncManager primaryIcloudMailboxFuture]_block_invoke
+ ___57-[EMCategorizationSyncManager primaryIcloudMailboxFuture]_block_invoke_2
+ ___58-[EMCoreAnalyticsCollector registerForLogEventsWithBlock:]_block_invoke
+ ___58-[EMCoreAnalyticsCollector registerForLogEventsWithBlock:]_block_invoke_2
+ ___58-[EMCoreAnalyticsCollector registerForLogEventsWithBlock:]_block_invoke_3
+ ___58-[EMCoreAnalyticsCollector registerForLogEventsWithBlock:]_block_invoke_4
+ ___58-[EMMessageList _attemptToFinishRetryingPromisesByItemID:]_block_invoke.175
+ ___63-[EMQueryingCollection queryMatchedChangedObjectIDs:extraInfo:]_block_invoke.28
+ ___75-[EMInMemoryThreadCollection _nts_messagesWereChanged:forKeyPaths:deleted:]_block_invoke_2
+ ___82-[EMCategorizationSyncManager categoryRulesController:didReceiveNewOldTimestamps:]_block_invoke_2
+ ___83+[EMParsecInstantAnswers flightInformationWithAirlineCode:flightNumber:flightDate:]_block_invoke
+ ___93-[EMInMemoryThreadCollection _nts_objectIDDidChangeForMessage:oldObjectID:oldConversationID:]_block_invoke.80
+ ___block_descriptor_40_ea8_32bs_e21_v16?0"NSHashTable"8ls32l8
+ ___block_descriptor_40_ea8_32r_e29_v16?0"NSMutableDictionary"8lr32l8
+ ___block_descriptor_40_ea8_32s_e38_B16?0"<EMCollectionChangeObserver>"8ls32l8
+ ___block_descriptor_48_ea8_32r_e21_v16?0"NSHashTable"8lu40l8r32l8
+ ___block_descriptor_48_ea8_32s40bs_e21_v16?0"NSHashTable"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40bs_e29_v16?0"NSMutableDictionary"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e21_v16?0"NSHashTable"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40w_e19_v16?0"EMMailbox"8lw40l8s32l8
+ ___block_descriptor_56_ea8_32s40r48r_e45_v32?0"PARTask"8"PARResponse"16"NSError"24lr40l8r48l8s32l8
+ ___block_descriptor_56_ea8_32s40s48r_e21_v16?0"NSHashTable"8ls32l8s40l8r48l8
+ ___block_descriptor_64_ea8_32s40s48r_e28_"EMSortableThreadProxy"8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e19_v16?0"EMMailbox"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_ea8_32s40s48s56s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_89_ea8_32s40s48s56s64s72s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.213
+ ___block_literal_global.34
+ _objc_msgSend$arrivalActualTime
+ _objc_msgSend$arrivalAirport
+ _objc_msgSend$arrivalGate
+ _objc_msgSend$arrivalPublishedTime
+ _objc_msgSend$arrivalTerminal
+ _objc_msgSend$blocks
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$carrierCode
+ _objc_msgSend$carrierWebsite
+ _objc_msgSend$collectionPrefersBatchingUpdates:
+ _objc_msgSend$dataTaskWithRequest:isSynthetic:allowProxying:failOpen:background:completionHandler:
+ _objc_msgSend$departureActualTime
+ _objc_msgSend$departureAirport
+ _objc_msgSend$departureGate
+ _objc_msgSend$departurePublishedTime
+ _objc_msgSend$departureTerminal
+ _objc_msgSend$dictionaryFromTimezone:
+ _objc_msgSend$divertedAirport
+ _objc_msgSend$ef_partition:
+ _objc_msgSend$flightCarrierCode
+ _objc_msgSend$flightInformationWithAirlineCode:flightNumber:flightDate:
+ _objc_msgSend$flightNumber
+ _objc_msgSend$flightRequestForQuery:date:appBundleId:
+ _objc_msgSend$flightResults
+ _objc_msgSend$formatOptions
+ _objc_msgSend$formattedDate:withTimezone:
+ _objc_msgSend$initWithCalendarIdentifier:
+ _objc_msgSend$initWithId:userAgent:
+ _objc_msgSend$isCancelled
+ _objc_msgSend$legs
+ _objc_msgSend$primaryIcloudMailboxFuture
+ _objc_msgSend$registerForLogEventsWithBlock:
+ _objc_msgSend$secondsFromGMT
+ _objc_msgSend$setDontPreloadImages:
+ _objc_msgSend$setFormatOptions:
+ _objc_msgSend$setNetworkServiceType:
+ _objc_msgSend$setParsecEnabled:
+ _objc_msgSend$setRepresentation
+ _objc_msgSend$sfAirportToDictionnary:
+ _objc_msgSend$sfFlightStatusToString:
+ _objc_msgSend$sfFlightsToDictionary:
+ _objc_msgSend$taskWithRequest:completion:
+ _objc_msgSend$timeZoneForSecondsFromGMT:
+ _objc_msgSend$timeZoneWithAbbreviation:
+ _objc_msgSend$timezone
+ _objc_msgSend$title
+ _objc_msgSend$updatedFlightURLForInstantAnswer:
+ _objc_msgSend$utcFormatter
+ _utcFormatter.onceToken
+ _utcFormatter.utcFormatter
- -[EMCategorizationSyncManager primaryIcloudMailbox]
- -[EMCoreAnalyticsCollector periodicDataProviders]
- -[EMCoreAnalyticsCollector registered]
- -[EMCoreAnalyticsCollector registrationScheduler]
- -[EMCoreAnalyticsCollector setRegistered:]
- -[EMQueryingCollection enumerateObserversWithLastBlock:]
- -[EMRemoteContentURLSession dataTaskWithRequest:isSynthetic:allowProxying:failOpen:completionHandler:]
- -[EMRemoteContentURLSession dataTaskWithRequest:isSynthetic:completionHandler:]
- _OBJC_IVAR_$_EMCoreAnalyticsCollector._periodicDataProviders
- _OBJC_IVAR_$_EMCoreAnalyticsCollector._registered
- _OBJC_IVAR_$_EMCoreAnalyticsCollector._registrationScheduler
- _OBJC_IVAR_$_EMQueryingCollection._changeObserversLock
- ___102-[EMRemoteContentURLSession dataTaskWithRequest:isSynthetic:allowProxying:failOpen:completionHandler:]_block_invoke
- ___102-[EMRemoteContentURLSession dataTaskWithRequest:isSynthetic:allowProxying:failOpen:completionHandler:]_block_invoke.140
- ___146-[EMCategorizationSyncManager categoryCloudStorage:didChangeLastSeenDate:lastSeenDisplayDate:forCategoryType:inMailboxWithExternalURL:originator:]_block_invoke.24
- ___39-[EMQueryingCollection beginObserving:]_block_invoke.21
- ___44-[EMCoreAnalyticsCollector logOneTimeEvent:]_block_invoke.28
- ___46-[EMCoreAnalyticsCollector _logPeriodicEvents]_block_invoke.33
- ___49-[EMQueryingCollection queryDidFinishInitialLoad]_block_invoke.27
- ___49-[EMQueryingCollection queryDidFinishInitialLoad]_block_invoke.30
- ___49-[EMQueryingCollection queryDidFinishInitialLoad]_block_invoke_2.31
- ___51-[EMCategorizationSyncManager primaryIcloudMailbox]_block_invoke
- ___51-[EMCategorizationSyncManager primaryIcloudMailbox]_block_invoke.31
- ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.165
- ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.167
- ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.167.cold.1
- ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke_2.166
- ___58-[EMMessageList _attemptToFinishRetryingPromisesByItemID:]_block_invoke.171
- ___63-[EMQueryingCollection queryMatchedChangedObjectIDs:extraInfo:]_block_invoke.24
- ___73-[EMCoreAnalyticsCollector registerForLogEventsWithPeriodicDataProvider:]_block_invoke_3
- ___73-[EMCoreAnalyticsCollector registerForLogEventsWithPeriodicDataProvider:]_block_invoke_4
- ___93-[EMInMemoryThreadCollection _nts_objectIDDidChangeForMessage:oldObjectID:oldConversationID:]_block_invoke.75
- ___block_descriptor_40_ea8_32r_e24_v16?0"NSMutableArray"8lr32l8
- ___block_descriptor_40_ea8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
- ___block_descriptor_40_ea8_32w_e24_v16?0"NSMutableArray"8lw32l8
- ___block_descriptor_56_ea8_32s40s48r_e24_v16?0"NSMutableArray"8ls32l8s40l8r48l8
- ___block_descriptor_64_ea8_32s40s48s56s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_81_ea8_32s40s48s56s64s72s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.211
- ___block_literal_global.28
- ___block_literal_global.32
- ___block_literal_global.83
- _objc_msgSend$dataTaskWithRequest:isSynthetic:allowProxying:failOpen:completionHandler:
- _objc_msgSend$periodicDataProviders
- _objc_msgSend$primaryIcloudMailbox
- _objc_msgSend$registrationScheduler
CStrings:
+ "%p: Missing threadProxy in %{public}@. Created new threadProxy:%p for itemID:%{public}@"
+ "<%p> Adding %lu items to threadItemID: %{public}@ after %{public}@, isLastObserver: %{BOOL}d"
+ "<%p> Adding %lu items to threadItemID: %{public}@ before %{public}@, isLastObserver: %{BOOL}d"
+ "<%p> [section %lu] Adding %lu items after %{public}@, isLastObserver: %{BOOL}d"
+ "<%p> [section %lu] Adding %lu items before %{public}@, isLastObserver: %{BOOL}d"
+ "@\"EMSortableThreadProxy\"8@?0"
+ "@20@0:8i16"
+ "@48@0:8@16B24B28B32B36@?40"
+ "@`"
+ "B16@?0@\"<EMCollectionChangeObserver>\"8"
+ "Can't create formattedDate, date is nil"
+ "EMParsecInstantAnswer.m"
+ "EMParsecInstantAnswers"
+ "Failed to get primary iCloud mailbox: %@"
+ "Logging periodic events for %ld providers"
+ "No primary iCloud account was found."
+ "T@\"EFLocked\",&,N,V_changeObservers"
+ "T@\"EFLocked\",R,N,V_blocks"
+ "T@\"NSURL\",&,N,V_checkInUrl"
+ "UTC"
+ "Unable to save New/Old timestamps. Categories: %@"
+ "[instant answers][flights api] Can't get flightInformation, airlineCode is nil"
+ "[instant answers][flights api] Can't get flightInformation, flightDate is nil"
+ "[instant answers][flights api] Can't get flightInformation, flightNumber is nil"
+ "[instant answers][flights api] Can't get flightInformation, query is malformed"
+ "[instant answers][flights api] Received nil flightDepartureTimeZone, using UTC timeZone to initialize Calendar"
+ "[instant answers][flights api] bundleIdentifier is undefined."
+ "[instant answers][flights api] coreparsec request timed out (timeout = %d ms)"
+ "[instant answers][flights api] coreparsec results count = %lu"
+ "[instant answers][flights api] empty coreparsec response for flight"
+ "[instant answers][flights api] error when calling coreparsec : %@"
+ "[instant answers][flights api] flightDepartureActualDate or flightArrivalActualDate is nil, skipping live info. update"
+ "[instant answers][flights api] found %lu events from flights api response"
+ "[instant answers][flights api] found %lu flight legs with same departure airport and date"
+ "[instant answers][flights api] found flight leg with no departure airport"
+ "[instant answers][flights api] found flight leg with no departure airport code"
+ "[instant answers][flights api] no matching leg was found from flights api response"
+ "_blocks"
+ "_didRegister"
+ "_nts_messagesWereAdded:extraInfo:"
+ "_nts_messagesWereChanged:forKeyPaths:deleted:"
+ "arrivalActualTime"
+ "arrivalAirport"
+ "arrivalGate"
+ "arrivalPublishedTime"
+ "arrivalTerminal"
+ "blocks"
+ "bundleIdentifier"
+ "canceled"
+ "carrierCode"
+ "carrierWebsite"
+ "collectionPrefersBatchingUpdates:"
+ "com.apple.mail"
+ "com.apple.undefined"
+ "dataTaskWithRequest:isSynthetic:allowProxying:failOpen:background:completionHandler:"
+ "delayed"
+ "departureActualTime"
+ "departureAirport"
+ "departureGate"
+ "departurePublishedTime"
+ "departureTerminal"
+ "dictionaryFromTimezone:"
+ "diverted"
+ "divertedAirport"
+ "ef_partition:"
+ "flightCarrierCode"
+ "flightInformationWithAirlineCode:flightNumber:flightDate:"
+ "flightNumber"
+ "flightRequestForQuery:date:appBundleId:"
+ "flightResults"
+ "formatOptions"
+ "formattedDate:withTimezone:"
+ "initWithCalendarIdentifier:"
+ "initWithId:userAgent:"
+ "isPredicateForMessagesInConversations:conversationIDs:"
+ "landed"
+ "legs"
+ "mail/1"
+ "primaryIcloudMailboxFuture"
+ "registerForLogEventsWithBlock:"
+ "scheduled"
+ "secondsFromGMT"
+ "setCheckInUrl:"
+ "setDontPreloadImages:"
+ "setFormatOptions:"
+ "setNetworkServiceType:"
+ "setParsecEnabled:"
+ "setRepresentation"
+ "sfAirportToDictionnary:"
+ "sfFlightStatusToString:"
+ "sfFlightsToDictionary:"
+ "syntheticDataTaskWithRequest:failOpen:background:completionHandler:"
+ "taskWithRequest:completion:"
+ "timeZoneForSecondsFromGMT:"
+ "timeZoneWithAbbreviation:"
+ "timezone"
+ "title"
+ "unknown"
+ "updatedFlightURLForInstantAnswer:"
+ "utcFormatter"
+ "v16@?0@\"EMMailbox\"8"
+ "v32@?0@\"PARTask\"8@\"PARResponse\"16@\"NSError\"24"
- "%p: Missing threadProxy. Created new threadProxy:%p for itemID:%{public}@"
- "<%p> [section %lu] Adding %{public}@ after %{public}@"
- "<%p> [section %lu] Adding %{public}@ before %{public}@"
- "@44@0:8@16B24B28B32@?36"
- "EMMailboxCategoryCloudStorage didChangeLastSeenDate: %@, lastSeenDisplayDate: %@, categoryType: %@, url: %@"
- "Logging periodic events for providers: %ld"
- "T@\"<EFScheduler>\",R,N,V_registrationScheduler"
- "T@\"EFLocked\",R,N,V_periodicDataProviders"
- "T@\"NSHashTable\",&,N,V_changeObservers"
- "T@\"NSURL\",R,N,V_checkInUrl"
- "TB,N,V_registered"
- "Unable to save New/Old timestamps. Categories: %@, icloudMailbox: %@"
- "_changeObserversLock"
- "_periodicDataProviders"
- "_registered"
- "_registrationScheduler"
- "com.apple.email.EMCoreAnalyticsCollector.registrationScheduler"
- "dataTaskWithRequest:isSynthetic:allowProxying:failOpen:completionHandler:"
- "dataTaskWithRequest:isSynthetic:completionHandler:"
- "periodicDataProviders"
- "primaryIcloudMailbox"
- "registered"
- "registrationScheduler"
- "setRegistered:"

```
