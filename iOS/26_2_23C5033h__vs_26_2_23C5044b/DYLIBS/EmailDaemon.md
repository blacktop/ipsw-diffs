## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3864.300.22.2.1
-  __TEXT.__text: 0x2642f4
-  __TEXT.__auth_stubs: 0x2710
-  __TEXT.__objc_methlist: 0x12f1c
-  __TEXT.__const: 0x397c
-  __TEXT.__gcc_except_tab: 0x4e8b0
-  __TEXT.__cstring: 0x2668a
-  __TEXT.__oslogstring: 0x19e54
+3864.300.41.2.1
+  __TEXT.__text: 0x269c48
+  __TEXT.__auth_stubs: 0x2700
+  __TEXT.__objc_methlist: 0x12f84
+  __TEXT.__const: 0x37bc
+  __TEXT.__gcc_except_tab: 0x4e7a0
+  __TEXT.__cstring: 0x2704a
+  __TEXT.__oslogstring: 0x1a264
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x22
-  __TEXT.__constg_swiftt: 0xb84
-  __TEXT.__swift5_typeref: 0xdc7
-  __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0xd04
-  __TEXT.__swift5_fieldmd: 0x1120
+  __TEXT.__constg_swiftt: 0xb4c
+  __TEXT.__swift5_typeref: 0xe21
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_reflstr: 0xcef
+  __TEXT.__swift5_fieldmd: 0x10d0
   __TEXT.__swift5_assocty: 0x138
-  __TEXT.__swift5_proto: 0x26c
-  __TEXT.__swift5_types: 0x144
-  __TEXT.__swift5_capture: 0x3dc
+  __TEXT.__swift5_proto: 0x254
+  __TEXT.__swift5_types: 0x13c
+  __TEXT.__swift5_capture: 0x464
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x10828
-  __TEXT.__eh_frame: 0xfb0
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__unwind_info: 0x10808
+  __TEXT.__eh_frame: 0xe70
   __TEXT.__objc_classname: 0x2bfe
-  __TEXT.__objc_methname: 0x374a1
+  __TEXT.__objc_methname: 0x37532
   __TEXT.__objc_methtype: 0x77ec
-  __TEXT.__objc_stubs: 0x24d40
-  __DATA_CONST.__got: 0x1b90
-  __DATA_CONST.__const: 0x9318
-  __DATA_CONST.__objc_classlist: 0x928
+  __TEXT.__objc_stubs: 0x24d20
+  __DATA_CONST.__got: 0x1ba8
+  __DATA_CONST.__const: 0x9340
+  __DATA_CONST.__objc_classlist: 0x930
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaee8
+  __DATA_CONST.__objc_selrefs: 0xaf10
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x658
-  __AUTH_CONST.__auth_got: 0x1398
-  __AUTH_CONST.__const: 0x5c78
-  __AUTH_CONST.__cfstring: 0x10160
-  __AUTH_CONST.__objc_const: 0x213f0
+  __AUTH_CONST.__auth_got: 0x1390
+  __AUTH_CONST.__const: 0x5d48
+  __AUTH_CONST.__cfstring: 0x101a0
+  __AUTH_CONST.__objc_const: 0x214c0
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0xef0
-  __AUTH.__data: 0x4f8
+  __AUTH.__objc_data: 0xf60
+  __AUTH.__data: 0x528
   __DATA.__objc_ivar: 0x1460
-  __DATA.__data: 0x35e0
+  __DATA.__data: 0x3760
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x4750
-  __DATA.__common: 0x8
+  __DATA.__bss: 0x4450
+  __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x4fc0
-  __DATA_DIRTY.__data: 0xc30
+  __DATA_DIRTY.__data: 0xd10
   __DATA_DIRTY.__bss: 0x1620
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BE4DBC3E-B05E-3188-B6BE-DB95F7ACC05C
-  Functions: 10661
-  Symbols:   34266
-  CStrings:  16230
+  UUID: 6C449E5D-618C-330A-860D-D368687658DB
+  Functions: 10690
+  Symbols:   34374
+  CStrings:  16294
 
Symbols:
+ -[EDGroupedSenderQueryHandler _groupedSenderForEDGroupedSender:].cold.1
+ -[EDGroupedSenderQueryHandler queryHelper:businessIDDidChangeForMessages:fromBusinessID:].cold.1
+ -[EDGroupedSenderQueryHandler queryHelper:didAddMessages:searchInfo:].cold.1
+ -[EDGroupedSenderQueryHandler queryHelper:didDeleteMessages:].cold.1
+ -[EDGroupedSenderQueryHandler queryHelper:didFindMessages:searchInfo:forInitialBatch:].cold.1
+ -[EDGroupedSenderQueryHandler queryHelper:didUpdateMessages:forKeyPaths:].cold.1
+ -[EDGroupedSenderQueryHandler queryHelper:messageFlagsDidChangeForMessages:previousMessages:].cold.1
+ -[EDGroupedSenderQueryHandler queryHelperDidFindAllMessages:localSearchInfoCollector:].cold.1
+ -[EDGroupedSenderQueryHandler queryHelperNeedsRestart:].cold.1
+ -[EDMessageQueryHandler queryHelper:businessIDDidChangeForMessages:fromBusinessID:].cold.1
+ -[EDMessageQueryHandler queryHelper:conversationIDDidChangeForMessages:fromConversationID:].cold.1
+ -[EDMessageQueryHandler queryHelper:conversationNotificationLevelDidChangeForConversation:conversationID:].cold.1
+ -[EDMessageQueryHandler queryHelper:didAddMessages:searchInfo:].cold.1
+ -[EDMessageQueryHandler queryHelper:didDeleteMessages:].cold.1
+ -[EDMessageQueryHandler queryHelper:didFindMessages:searchInfo:forInitialBatch:].cold.1
+ -[EDMessageQueryHandler queryHelper:didUpdateMessages:forKeyPaths:].cold.1
+ -[EDMessageQueryHandler queryHelper:messageFlagsDidChangeForMessages:previousMessages:].cold.1
+ -[EDMessageQueryHandler queryHelper:objectIDDidChangeForMessage:oldObjectID:oldConversationID:].cold.1
+ -[EDMessageQueryHandler queryHelperDidFailInitialLoad:localSearchInfoCollector:].cold.2
+ -[EDMessageQueryHandler queryHelperDidFindAllMessages:localSearchInfoCollector:].cold.1
+ -[EDMessageQueryHandler queryHelperDidFinishRemoteSearch:].cold.1
+ -[EDMessageQueryHandler queryHelperNeedsRestart:].cold.1
+ _OBJC_CLASS_$_EDIMAPTimeToDownloadAnalytics
+ _OBJC_CLASS_$_EMMessageBodyParsingUtils
+ _OBJC_METACLASS_$_EDIMAPTimeToDownloadAnalytics
+ __CLASS_METHODS_EDIMAPTimeToDownloadAnalytics
+ __DATA_EDIMAPTimeToDownloadAnalytics
+ __INSTANCE_METHODS_EDIMAPTimeToDownloadAnalytics
+ __IVARS_EDIMAPTimeToDownloadAnalytics
+ __METACLASS_DATA_EDIMAPTimeToDownloadAnalytics
+ __PROTOCOLS_EDIMAPTimeToDownloadAnalytics
+ __PROTOCOLS_EDIMAPTimeToDownloadAnalytics.2
+ ___105-[EDMessageQueryHelper _calculateAndReportChangesForPersistedMessages:withPendingChangesKey:changeBlock:]_block_invoke.84
+ ___65-[EDGroupedSenderQueryHandler _messagesWereAdded:toInitialBatch:]_block_invoke.cold.1
+ ___65-[EDGroupedSenderQueryHandler _messagesWereAdded:toInitialBatch:]_block_invoke.cold.2
+ ___69-[EDGroupedSenderQueryHandler _persistenceDidFinishMergingBusinesses]_block_invoke.cold.1
+ ___72-[EDMessageQueryHelper _foundMessages:inRemoteSearch:foundInLocalIndex:]_block_invoke.65
+ ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.72
+ ___89-[EDGroupedSenderQueryHandler _messagesWereChanged:previousMessages:forKeyPaths:deleted:]_block_invoke.cold.1
+ ___89-[EDGroupedSenderQueryHandler _messagesWereChanged:previousMessages:forKeyPaths:deleted:]_block_invoke.cold.2
+ ___89-[EDGroupedSenderQueryHandler _messagesWereChanged:previousMessages:forKeyPaths:deleted:]_block_invoke.cold.3
+ ____groupMessagesBySender_block_invoke.cold.1
+ ___block_descriptor_128_ea8_32s40s48s56s64s72s80s88s96bs104bs112r120r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r112l8r120l8s96l8s72l8s80l8s88l8s104l8
+ __swift_FORCE_LOAD_$_swiftMetal_$_IndexingAnalytics
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_IndexingAnalytics
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_IndexingAnalytics
+ __swift_FORCE_LOAD_$_swiftos_$_IndexingAnalytics
+ __swift_FORCE_LOAD_$_swiftsimd_$_IndexingAnalytics
+ _block_copy_helper.33
+ _block_copy_helper.9
+ _block_descriptor.11
+ _block_descriptor.35
+ _block_destroy_helper.10
+ _block_destroy_helper.34
+ _symbolic SS7account_SS15bytesDownloadedSS7endedAtSS12messageCountSS5monthSS7runtimeSS07startedE0t
+ _symbolic SS______t 15EmailFoundation5EventV5ValueO
+ _symbolic Say_____G 15EmailFoundation5EventV
+ _symbolic SdSg
+ _symbolic _____Sg 15EmailFoundation5EventV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 15EmailFoundation5EventV5ValueO
+ _symbolic _____ySS______tG s23_ContiguousArrayStorageC 15EmailFoundation5EventV5ValueO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15EmailFoundation5EventV
+ _symbolic _____y_____SgG s23_ContiguousArrayStorageC 15EmailFoundation5EventV
- -[EDMessageQueryHelper persistenceDidDeleteAllMessagesInMailboxesWithURLs:generationWindow:].cold.1
- _AnalyticsSendEvent
- _OBJC_CLASS_$_ECMessageBodyParsingUtils
- ___105-[EDMessageQueryHelper _calculateAndReportChangesForPersistedMessages:withPendingChangesKey:changeBlock:]_block_invoke.75
- ___72-[EDMessageQueryHelper _foundMessages:inRemoteSearch:foundInLocalIndex:]_block_invoke.56
- ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.63
- ___block_descriptor_112_ea8_32s40s48s56s64s72s80bs88bs96r104r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r96l8r104l8s80l8s72l8s88l8
- ___swift_memcpy17_8
- _associated conformance 17IndexingAnalytics5EventV5ValueOSHAASQ
- _associated conformance 17IndexingAnalytics5EventVSHAASQ
- _get_enum_tag_for_layout_string 17IndexingAnalytics5EventV5ValueO
- _objc_msgSend$weakToWeakObjectsMapTable
- _swift_cvw_enumFn_getEnumTag
- _symbolic SDySS_____G 17IndexingAnalytics5EventV5ValueO
- _symbolic SS______t 17IndexingAnalytics5EventV5ValueO
- _symbolic _____ 17IndexingAnalytics5EventV
- _symbolic _____ 17IndexingAnalytics5EventV5ValueO
- _symbolic _____ySS_____G s18_DictionaryStorageC 17IndexingAnalytics5EventV5ValueO
- _symbolic _____ySS______tG s23_ContiguousArrayStorageC 17IndexingAnalytics5EventV5ValueO
- _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
- _type_layout_string 17IndexingAnalytics5EventV
- _type_layout_string 17IndexingAnalytics5EventV5ValueO
CStrings:
+ "\n             FROM "
+ "\n            WHERE "
+ " - :received AS REAL) / (60*60*24*30)))\n      AND "
+ " = 0 THEN :now ELSE "
+ " = 0) IS NULL\nRETURNING "
+ " = :account\n              AND "
+ " = :account\n      AND ("
+ " = :account\n      AND (SELECT "
+ " = :bytesDownloaded + "
+ " = CASE WHEN :is_complete AND "
+ " > :received\n      AND (SELECT "
+ " AS bytesDownloaded,\n          "
+ " AS messageCount,\n          "
+ " AS month,\n          "
+ " AS runtime,\n          "
+ " ELSE :now END\n    WHERE "
+ " END,\n          "
+ " found in local index"
+ " from remote search"
+ "%p: %lu remaining budget after %lu snippet data for query: %p"
+ "%p: %{public}@: keyPaths:%{public}@ delete:%{BOOL}d"
+ "%p: Adding %lu filtered messages out of %lu%{public}@%{public}@"
+ "%p: Adding %u filtered messages"
+ "%p: Adding (due to change for %{public}@) %lu filtered messages out of %lu"
+ "%p: Adding objectIDs: %{public}@ before: %{public}@"
+ "%p: Avoid creating empty group sender for BusinessID:%{public}@"
+ "%p: Avoid creating group sender with displayMessageItemID equals nil for BusinessID:%lld"
+ "%p: Avoid creating group sender with displayMessageItemID equals nil for BusinessID:%{public}@"
+ "%p: Changing (for %{public}@) %lu filtered messages out of %lu"
+ "%p: Changing businessID for objectIDs: %{public}@"
+ "%p: Changing conversationID for objectIDs: %{public}@"
+ "%p: Changing flags for objectIDs: %{public}@"
+ "%p: Changing key paths: %{public}@ for objectIDs: %{public}@"
+ "%p: Deleting %lu filtered messages out of %lu"
+ "%p: Deleting objectIDs: %{public}@"
+ "%p: Did delete all messages in %lu mailbox(es). Requesting restart."
+ "%p: Empty group sender being created: %{public}@"
+ "%p: Entered grouped sender list %p lock for adding messages"
+ "%p: Entered grouped sender list %p lock for merging businesses"
+ "%p: Entered grouped sender list %p lock for updating business IDs"
+ "%p: Entered grouped sender list %p lock for updating messages"
+ "%p: Entered grouped sender list %p lock for updating unseen counts"
+ "%p: Entering grouped sender list %p lock for adding messages"
+ "%p: Entering grouped sender list %p lock for merging businesses"
+ "%p: Entering grouped sender list %p lock for updating business IDs"
+ "%p: Entering grouped sender list %p lock for updating messages"
+ "%p: Entering grouped sender list %p lock for updating unseen counts"
+ "%p: Exited grouped sender list %p lock for adding messages"
+ "%p: Exited grouped sender list %p lock for merging businesses"
+ "%p: Exited grouped sender list %p lock for updating business IDs"
+ "%p: Exited grouped sender list %p lock for updating messages"
+ "%p: Exited grouped sender list %p lock for updating unseen counts"
+ "%p: Exiting grouped sender list %p lock for adding messages"
+ "%p: Exiting grouped sender list %p lock for merging businesses"
+ "%p: Exiting grouped sender list %p lock for updating business IDs"
+ "%p: Exiting grouped sender list %p lock for updating messages"
+ "%p: Exiting grouped sender list %p lock for updating unseen counts"
+ "%p: Failed live query %p"
+ "%p: Finished Merging Businesses: Found empty messages with old grouped sender:%{public}@"
+ "%p: Finished initial load"
+ "%p: Finished live query %p"
+ "%p: Found %lu objectIDs starting with: %{public}@\nending with:\n%{public}@"
+ "%p: Found %lu objectIDs: %{public}@"
+ "%p: Found a message with business ID 0: %@"
+ "%p: Getting initial results for message query %{public}@"
+ "%p: Got %lu snippet data with %lu remaining budget for query: %p"
+ "%p: Group sender already removed for BusinessID:%{public}@"
+ "%p: Holding %u reconciled persisted messages until initial results"
+ "%p: Ignoring %lu added messages from non-current helper"
+ "%p: Ignoring %lu changed messages from non-current helper"
+ "%p: Ignoring %lu deleted messages from non-current helper"
+ "%p: Ignoring %lu found messages from non-current helper"
+ "%p: Ignoring %lu messages with businessID changes from non-current helper"
+ "%p: Ignoring %lu messages with conversation ID changes from non-current helper"
+ "%p: Ignoring %lu messages with updated hasAttachments"
+ "%p: Ignoring %lu updated messages from non-current helper"
+ "%p: Ignoring 'did fail initial load' from non-current helper"
+ "%p: Ignoring 'did find all' from non-current helper"
+ "%p: Ignoring 'did finish remote search' from non-current helper"
+ "%p: Ignoring 'needs restart' from non-current helper"
+ "%p: Ignoring add for %lu filtered out messages%{public}@%{public}@"
+ "%p: Ignoring business ID %lld being merged because it does not exist in our groups"
+ "%p: Ignoring change (for %{public}@) for %lu filtered out messages (%lu no longer matching)"
+ "%p: Ignoring delete for %lu filtered out messages"
+ "%p: Ignoring message with changed object ID from non-current helper"
+ "%p: Ignoring message with conversation notification level changes from non-current helper"
+ "%p: Moving objectIDs: %{public}@ before: %{public}@"
+ "%p: No previous message for keyPaths:%{public}@ message: %{public}@"
+ "%p: Not deleting objectIDs with still existent duplicates: %{public}@"
+ "%p: Notifying observer of %lu additional groups with section changes (%{public}@):\n%{public}@"
+ "%p: Notifying observer of %lu changed groups (after businessID was changed for messages)"
+ "%p: Notifying observer of %lu changed groups (after groups were merged)"
+ "%p: Notifying observer of %lu changed groups (after last seen dates changed)"
+ "%p: Notifying observer of %lu changed groups (after messages were %{public}@)"
+ "%p: Notifying observer of %lu changed groups (after messages were added)"
+ "%p: Notifying observer of %lu deleted groups (%{public}@):\n%{public}@"
+ "%p: Notifying observer of %lu groups inserted after %{public}@ (%{public}@):\n%{public}@"
+ "%p: Notifying observer of %lu groups moved after %{public}@ (%{public}@):\n%{public}@"
+ "%p: Performing Remote Search (Search Indexer + Server Search)"
+ "%p: Received error %{public}@ while performing initial query: %p"
+ "%p: Reconciled %u filtered messages"
+ "%p: Remove messages from group and it's now empty for sender:%{public}@"
+ "%p: Removed messages from group and it's now empty for sender:%{public}@"
+ "%p: Skip updating the message list update for a Spotlight query result."
+ "%p: Starting with query '%{public}@'"
+ "%p: found %lu initial results for message query %p"
+ "%p: found 0 messages for grouped sender:%{public}@ limit:%ld query:%{public}@"
+ ")\nVALUES (:account, 0, 0, 0, 0, :started_at, NULL),\n       (:account, 1, 0, 0, 0, :started_at, NULL),\n       (:account, 2, 0, 0, 0, :started_at, NULL),\n       (:account, 3, 0, 0, 0, :started_at, NULL),\n       (:account, 4, 0, 0, 0, :started_at, NULL),\n       (:account, 5, 0, 0, 0, :started_at, NULL),\n       (:account, 6, 0, 0, 0, :started_at, NULL),\n       (:account, 7, 0, 0, 0, :started_at, NULL),\n       (:account, 8, 0, 0, 0, :started_at, NULL),\n       (:account, 9, 0, 0, 0, :started_at, NULL),\n       (:account, 10, 0, 0, 0, :started_at, NULL),\n       (:account, 11, 0, 0, 0, :started_at, NULL),\n       (:account, 12, 0, 0, 0, :started_at, NULL),\n       (:account, 13, 0, 0, 0, :started_at, NULL),\n       (:account, 14, 0, 0, 0, :started_at, NULL),\n       (:account, 15, 0, 0, 0, :started_at, NULL),\n       (:account, 16, 0, 0, 0, :started_at, NULL),\n       (:account, 17, 0, 0, 0, :started_at, NULL),\n       (:account, 18, 0, 0, 0, :started_at, NULL),\n       (:account, 19, 0, 0, 0, :started_at, NULL),\n       (:account, 20, 0, 0, 0, :started_at, NULL),\n       (:account, 21, 0, 0, 0, :started_at, NULL),\n       (:account, 22, 0, 0, 0, :started_at, NULL),\n       (:account, 23, 0, 0, 0, :started_at, NULL),\n       (:account, 24, 0, 0, 0, :started_at, NULL)"
+ ":bytesDownloaded"
+ "EDIMAPTimeToDownloadAnalytics"
+ "EmailDaemon/EDIMAPTimeToDownloadAnalytics.swift"
+ "EmailDaemon_Private.EDIMAPTimeToDownloadAnalytics"
+ "INSERT OR IGNORE INTO "
+ "bucketedNumber:leadingDigits:"
+ "bytes_downloaded"
+ "com.apple.mail.IMAP.timeToDownloadByAge"
+ "com.apple.mail.IMAP.timeToDownloadByCount"
+ "com.apple.mail.IMAP.timeToDownloadBySize"
+ "didDownload(size:dateReceived:now:)"
+ "didDownloadMessageOfSize:dateReceived:"
+ "didStartDownloading"
+ "didStop(isComplete:now:)"
+ "didStopDownloadingIsComplete:"
+ "imap_initial_download_statistics"
+ "initWithDatabase:accountIdentifier:"
+ "initWithDouble:"
+ "numberOfMessages"
+ "runtimeStart"
- "%p: %lu remaining budget after %lu snippet data for query: %{public}@"
- "%p: Adding %u filtered messages: %{public}@"
- "%p: Adding objectIDs: %{public}@ before: %{public}@\n%{public}@"
- "%p: Changing businessID for objectIDs: %{public}@\n%{public}@"
- "%p: Changing conversationID for objectIDs: %{public}@\n%{public}@"
- "%p: Changing flags for objectIDs: %{public}@\n%{public}@"
- "%p: Changing key paths: %{public}@ for objectIDs: %{public}@\n%{public}@"
- "%p: Deleting %u filtered messages: %@"
- "%p: Deleting objectIDs: %{public}@\n%{public}@"
- "%p: Did delete all messages in %u mailbox(es). Requesting restart."
- "%p: Failed initial load\n%{public}@"
- "%p: Failed live query %{public}@"
- "%p: Finished initial load\n%{public}@"
- "%p: Finished live query %{public}@"
- "%p: Found %lu objectIDs starting with: %{public}@\nending with:\n%{public}@\n%{public}@"
- "%p: Found %lu objectIDs: %{public}@\n%{public}@"
- "%p: Getting initial results for message query %@"
- "%p: Got %lu snippet data with %lu remaining budget for query: %{public}@"
- "%p: Holding %u reconciled persisted messages until initial results: %@"
- "%p: Moving objectIDs: %{public}@ before: %{public}@\n%{public}@"
- "%p: Not deleting objectIDs with still existent duplicates: %{public}@\n%{public}@"
- "%p: Received error %{public}@ while performing initial query: %@"
- "%p: Reconciled %u filtered messages: %@"
- "%p: found %lu initial results for message query %@"
- "<%@ %p> %{public}@: keyPaths:%{public}@ delete:%{BOOL}d"
- "<%@ %p> Avoid creating empty group sender for BusinessID:%{public}@"
- "<%@ %p> Avoid creating group sender with displayMessageItemID equals nil for BusinessID:%lld"
- "<%@ %p> Avoid creating group sender with displayMessageItemID equals nil for BusinessID:%{public}@"
- "<%@ %p> Empty group sender being created: %{public}@"
- "<%@ %p> Entered grouped sender list %p lock for adding messages"
- "<%@ %p> Entered grouped sender list %p lock for merging businesses"
- "<%@ %p> Entered grouped sender list %p lock for updating business IDs"
- "<%@ %p> Entered grouped sender list %p lock for updating messages"
- "<%@ %p> Entered grouped sender list %p lock for updating unseen counts"
- "<%@ %p> Entering grouped sender list %p lock for adding messages"
- "<%@ %p> Entering grouped sender list %p lock for merging businesses"
- "<%@ %p> Entering grouped sender list %p lock for updating business IDs"
- "<%@ %p> Entering grouped sender list %p lock for updating messages"
- "<%@ %p> Entering grouped sender list %p lock for updating unseen counts"
- "<%@ %p> Exited grouped sender list %p lock for adding messages"
- "<%@ %p> Exited grouped sender list %p lock for merging businesses"
- "<%@ %p> Exited grouped sender list %p lock for updating business IDs"
- "<%@ %p> Exited grouped sender list %p lock for updating messages"
- "<%@ %p> Exited grouped sender list %p lock for updating unseen counts"
- "<%@ %p> Exiting grouped sender list %p lock for adding messages"
- "<%@ %p> Exiting grouped sender list %p lock for merging businesses"
- "<%@ %p> Exiting grouped sender list %p lock for updating business IDs"
- "<%@ %p> Exiting grouped sender list %p lock for updating messages"
- "<%@ %p> Exiting grouped sender list %p lock for updating unseen counts"
- "<%@ %p> Finished Merging Businesses: Found empty messages with old grouped sender:%{public}@"
- "<%@ %p> Found a message with business ID 0: %@"
- "<%@ %p> Group sender already removed for BusinessID:%{public}@"
- "<%@ %p> Ignoring business ID %lld being merged because it does not exist in our groups"
- "<%@ %p> No previous message for keyPaths:%{public}@ message: %{public}@"
- "<%@ %p> Notifying observer of %lu additional groups with section changes (%{public}@):\n%{public}@"
- "<%@ %p> Notifying observer of %lu changed groups (after businessID was changed for messages)"
- "<%@ %p> Notifying observer of %lu changed groups (after groups were merged)"
- "<%@ %p> Notifying observer of %lu changed groups (after last seen dates changed)"
- "<%@ %p> Notifying observer of %lu changed groups (after messages were %{public}@)"
- "<%@ %p> Notifying observer of %lu changed groups (after messages were added)"
- "<%@ %p> Notifying observer of %lu deleted groups (%{public}@):\n%{public}@"
- "<%@ %p> Notifying observer of %lu groups inserted after %{public}@ (%{public}@):\n%{public}@"
- "<%@ %p> Notifying observer of %lu groups moved after %{public}@ (%{public}@):\n%{public}@"
- "<%@ %p> Remove messages from group and it's now empty for sender:%{public}@"
- "<%@ %p> Removed messages from group and it's now empty for sender:%{public}@"
- "<%@ %p> found 0 messages for grouped sender:%{public}@ limit:%ld query:%{public}@"
- "Performing Remote Search (Search Indexer + Server Search)"
- "weakToWeakObjectsMapTable"

```
