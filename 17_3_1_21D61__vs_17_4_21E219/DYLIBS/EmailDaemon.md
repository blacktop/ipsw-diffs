## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3774.400.21.0.0
-  __TEXT.__text: 0x1aa5b4
+3774.500.171.2.2
+  __TEXT.__text: 0x1ab7a0
   __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x100a4
-  __TEXT.__gcc_except_tab: 0x342d0
+  __TEXT.__objc_methlist: 0x1012c
+  __TEXT.__gcc_except_tab: 0x345c4
   __TEXT.__const: 0x2d2
-  __TEXT.__cstring: 0x1981b
+  __TEXT.__cstring: 0x199ab
   __TEXT.__oslogstring: 0x11bfa
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x2c
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0xc5c0
+  __TEXT.__unwind_info: 0xc638
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x2723
-  __TEXT.__objc_methname: 0x2eb54
-  __TEXT.__objc_methtype: 0x6bbb
-  __TEXT.__objc_stubs: 0x1ee60
+  __TEXT.__objc_classname: 0x2726
+  __TEXT.__objc_methname: 0x2ee66
+  __TEXT.__objc_methtype: 0x6bc1
+  __TEXT.__objc_stubs: 0x1efc0
   __DATA_CONST.__got: 0x680
-  __DATA_CONST.__const: 0x79f0
+  __DATA_CONST.__const: 0x7a48
   __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c218
-  __DATA_CONST.__objc_selrefs: 0x9a18
+  __DATA_CONST.__objc_const: 0x1c2c8
+  __DATA_CONST.__objc_selrefs: 0x9a80
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_classrefs: 0xdf0
+  __DATA_CONST.__objc_superrefs: 0x590
   __DATA_CONST.__objc_arraydata: 0x750
   __AUTH_CONST.__objc_const: 0x280
-  __AUTH_CONST.__cfstring: 0xe560
+  __AUTH_CONST.__cfstring: 0xe6c0
   __AUTH_CONST.__objc_intobj: 0x7f8
-  __AUTH_CONST.__const: 0x9d8
+  __AUTH_CONST.__const: 0xa38
   __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0xdf0
-  __DATA.__objc_superrefs: 0x590
-  __DATA.__objc_ivar: 0x1414
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x1420
   __DATA.__data: 0x25c0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xe8
-  __DATA_DIRTY.__const: 0x15c0
+  __DATA.__bss: 0xc0
+  __DATA_DIRTY.__const: 0x1580
   __DATA_DIRTY.__objc_const: 0x5a30
-  __DATA_DIRTY.__objc_data: 0x4ab0
+  __DATA_DIRTY.__objc_data: 0x4b00
   __DATA_DIRTY.__data: 0x58
-  __DATA_DIRTY.__bss: 0x8d8
+  __DATA_DIRTY.__bss: 0x900
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7668
-  Symbols:   28885
-  CStrings:  11820
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 7682
+  Symbols:   28944
+  CStrings:  11851
 
Symbols:
+ +[EDRemindMeNotificationController localizedRemindMeNotificationPlaceholder]
+ +[EDRemindMeNotificationController localizedRemindMeNotificationTitleNoSender]
+ -[EDInMemoryThread _newestDisplayDate]
+ -[EDMailboxPersistence _sendCoreAnalyticsForLargestMailbox:messageCountInSecondLargestMailbox:]
+ -[EDMailboxPersistence _sendCoreAnalyticsForMailboxesPerAccount:accountTypePerAccount:]
+ -[EDMailboxPersistence _sendCoreAnalyticsForMessagesPerAccount:accountTypePerAccount:]
+ -[EDMailboxPersistence _sendCoreAnalyticsForMessagesPerInbox:accountTypePerAccount:accountPerInbox:]
+ -[EDMailboxPersistence _sendEventToCoreAnalytics:withEventDictionary:]
+ -[EDMailboxPersistence analyticsCollector]
+ -[EDMailboxPersistenceStatistics accountPerInbox]
+ -[EDMailboxPersistenceStatistics accountTypePerAccount]
+ -[EDMailboxPersistenceStatistics initWithMessagesInLargestMailbox:messagesInSecondLargestMailbox:messagesPerMailbox:mailboxesPerAccount:messagesPerAccount:accountTypePerAccount:messagesPerInbox:accountPerInbox:]
+ -[EDMailboxProvider beginDeferringInvalidation]
+ -[EDMailboxProvider endDeferringInvalidation]
+ -[EDMessageRepository _persistedMessagesForObjectIDs:includeDuplicates:]
+ -[EDThreadPersistence _updateForThreadsWithThreadScopeDatabaseID:conversation:]
+ GCC_except_table257
+ _OBJC_IVAR_$_EDMailboxPersistence._analyticsCollector
+ _OBJC_IVAR_$_EDMailboxPersistenceStatistics._accountPerInbox
+ _OBJC_IVAR_$_EDMailboxPersistenceStatistics._accountTypePerAccount
+ __OBJC_$_PROP_LIST_EDMessageRepositoryQueryHandler.126
+ __OBJC_$_PROP_LIST_EDSortableMessage.78
+ __OBJC_$_PROP_LIST_EDThreadQueryHandler.261
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.360
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.360.cold.1
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.362
+ ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.304
+ ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.245
+ ___45-[EDMailboxProvider endDeferringInvalidation]_block_invoke
+ ___55-[EDMailDynamicDataAsset _queryForAssetWithCompletion:]_block_invoke.311
+ ___55-[EDMailDynamicDataAsset _queryForAssetWithCompletion:]_block_invoke.311.cold.1
+ ___67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.223
+ ___72-[EDMessageRepository _persistedMessagesForObjectIDs:includeDuplicates:]_block_invoke
+ ___80-[EDRemindMeNotificationController _fetchMessagesToNotifyWithStartDate:endDate:]_block_invoke
+ ___block_descriptor_32_e55_q24?0"<EDPersistedMessage>"8"<EDPersistedMessage>"16l
+ ___block_descriptor_40_ea8_32w_e51_v36?0"<EFCancelable>"8"NSArray"16B24"NSError"28lw32l8
+ ___block_descriptor_48_ea8_32s_e32_"EMObjectID"16?0"EMObjectID"8ls32l8
+ ___block_literal_global.115
+ ___block_literal_global.173
+ ___block_literal_global.178
+ ___block_literal_global.214
+ ___block_literal_global.249
+ ___block_literal_global.309
+ ___block_literal_global.32
+ ___block_literal_global.322
+ ___block_literal_global.331
+ ___block_literal_global.333
+ ___block_literal_global.339
+ ___block_literal_global.342
+ ___block_literal_global.344
+ ___block_literal_global.346
+ ___block_literal_global.362
+ ___block_literal_global.388
+ ___block_literal_global.634
+ ___block_literal_global.796
+ ___block_literal_global.798
+ ___block_literal_global.853
+ ___block_literal_global.855
+ ___block_literal_global.892
+ ___block_literal_global.99
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_EmailDaemon
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_EmailDaemon
+ _objc_msgSend$_newestDisplayDate
+ _objc_msgSend$_persistedMessagesForObjectIDs:includeDuplicates:
+ _objc_msgSend$_sendCoreAnalyticsForLargestMailbox:messageCountInSecondLargestMailbox:
+ _objc_msgSend$_sendCoreAnalyticsForMailboxesPerAccount:accountTypePerAccount:
+ _objc_msgSend$_sendCoreAnalyticsForMessagesPerAccount:accountTypePerAccount:
+ _objc_msgSend$_sendCoreAnalyticsForMessagesPerInbox:accountTypePerAccount:accountPerInbox:
+ _objc_msgSend$_sendEventToCoreAnalytics:withEventDictionary:
+ _objc_msgSend$_updateForThreadsWithThreadScopeDatabaseID:conversation:
+ _objc_msgSend$accountPerInbox
+ _objc_msgSend$accountTypePerAccount
+ _objc_msgSend$beginDeferringInvalidation
+ _objc_msgSend$ef_uniquifyWithComparator:
+ _objc_msgSend$endDeferringInvalidation
+ _objc_msgSend$initWithCollectionItemID:threadScope:
- -[EDMailboxPersistenceStatistics initWithMessagesInLargestMailbox:messagesInSecondLargestMailbox:messagesPerMailbox:mailboxesPerAccount:messagesPerAccount:messagesPerInbox:]
- -[EDMailboxProvider _beginDeferringInvalidation]
- -[EDMailboxProvider _endDeferringInvalidation]
- -[EDMessageRepository _persistedMessagesForObjectIDs:]
- __OBJC_$_PROP_LIST_EDMessageRepositoryQueryHandler.125
- __OBJC_$_PROP_LIST_EDSortableMessage.77
- __OBJC_$_PROP_LIST_EDThreadQueryHandler.260
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.353
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.353.cold.1
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.355
- ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.303
- ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.244
- ___46-[EDMailboxProvider _endDeferringInvalidation]_block_invoke
- ___55-[EDMailDynamicDataAsset _queryForAssetWithCompletion:]_block_invoke.287
- ___55-[EDMailDynamicDataAsset _queryForAssetWithCompletion:]_block_invoke.287.cold.1
- ___67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.222
- ___block_descriptor_40_ea8_32w_e48_v32?0"<EFCancelable>"8"NSArray"16"NSError"24lw32l8
- ___block_literal_global.114
- ___block_literal_global.213
- ___block_literal_global.248
- ___block_literal_global.285
- ___block_literal_global.321
- ___block_literal_global.328
- ___block_literal_global.332
- ___block_literal_global.338
- ___block_literal_global.341
- ___block_literal_global.343
- ___block_literal_global.345
- ___block_literal_global.633
- ___block_literal_global.789
- ___block_literal_global.791
- ___block_literal_global.852
- ___block_literal_global.854
- ___block_literal_global.891
- _objc_msgSend$_beginDeferringInvalidation
- _objc_msgSend$_endDeferringInvalidation
- _objc_msgSend$_persistedMessagesForObjectIDs:
CStrings:
+ "\x02$"
+ "@\"EMObjectID\"16@?0@\"EMObjectID\"8"
+ "@80@0:8q16q24@32@40@48@56@64@72"
+ "T@\"<EFSQLQueryLogging>\",?,R,N"
+ "T@\"<EFSQLQueryLogging>\",?,R,N,V_queryLogger"
+ "T@\"NSDictionary\",R,&,N,V_accountPerInbox"
+ "T@\"NSDictionary\",R,&,N,V_accountTypePerAccount"
+ "T@\"NSString\",?,R,C"
+ "Unknown objectID class"
+ "_accountPerInbox"
+ "_accountTypePerAccount"
+ "_newestDisplayDate"
+ "_persistedMessagesForObjectIDs:includeDuplicates:"
+ "_sendCoreAnalyticsForLargestMailbox:messageCountInSecondLargestMailbox:"
+ "_sendCoreAnalyticsForMailboxesPerAccount:accountTypePerAccount:"
+ "_sendCoreAnalyticsForMessagesPerAccount:accountTypePerAccount:"
+ "_sendCoreAnalyticsForMessagesPerInbox:accountTypePerAccount:accountPerInbox:"
+ "_sendEventToCoreAnalytics:withEventDictionary:"
+ "_updateForThreadsWithThreadScopeDatabaseID:conversation:"
+ "accountPerInbox"
+ "accountType"
+ "accountTypePerAccount"
+ "beginDeferringInvalidation"
+ "com.apple.mail.MailboxStatistics.mailboxesPerAccount"
+ "com.apple.mail.MailboxStatistics.messagesCountInLargestMailbox"
+ "com.apple.mail.MailboxStatistics.messagesPerAccount"
+ "com.apple.mail.MailboxStatistics.messagesPerInbox"
+ "ef_uniquifyWithComparator:"
+ "endDeferringInvalidation"
+ "initWithCollectionItemID:threadScope:"
+ "initWithMessagesInLargestMailbox:messagesInSecondLargestMailbox:messagesPerMailbox:mailboxesPerAccount:messagesPerAccount:accountTypePerAccount:messagesPerInbox:accountPerInbox:"
+ "localizedRemindMeNotificationPlaceholder"
+ "localizedRemindMeNotificationTitleNoSender"
+ "messageCountInLargestMailbox"
+ "messageCountInSecondLargestMailbox"
+ "v36@?0@\"<EFCancelable>\"8@\"NSArray\"16B24@\"NSError\"28"
- "@64@0:8q16q24@32@40@48@56"
- "T@\"<EFSQLQueryLogging>\",R,N"
- "T@\"<EFSQLQueryLogging>\",R,N,V_queryLogger"
- "_beginDeferringInvalidation"
- "_endDeferringInvalidation"
- "_persistedMessagesForObjectIDs:"
- "initWithMessagesInLargestMailbox:messagesInSecondLargestMailbox:messagesPerMailbox:mailboxesPerAccount:messagesPerAccount:messagesPerInbox:"
- "v32@?0@\"<EFCancelable>\"8@\"NSArray\"16@\"NSError\"24"

```
