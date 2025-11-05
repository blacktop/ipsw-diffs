## IMAP

> `/System/Library/PrivateFrameworks/IMAP.framework/Versions/A/IMAP`

```diff

-3826.400.131.1.6
-  __TEXT.__text: 0x57a54
+3826.500.181.1.5
+  __TEXT.__text: 0x58a94
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0x574c
+  __TEXT.__objc_methlist: 0x682c
   __TEXT.__cstring: 0x4103
-  __TEXT.__const: 0x248
+  __TEXT.__const: 0x250
   __TEXT.__oslogstring: 0x1adc
-  __TEXT.__gcc_except_tab: 0x1dc4
-  __TEXT.__unwind_info: 0x1a78
+  __TEXT.__gcc_except_tab: 0x1dc8
+  __TEXT.__unwind_info: 0x1ad0
   __TEXT.__objc_classname: 0x1123
   __TEXT.__objc_methname: 0xc391
   __TEXT.__objc_methtype: 0x240f

   __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b90
+  __DATA_CONST.__objc_selrefs: 0x2f08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x1410
   __AUTH_CONST.__cfstring: 0x4b20
-  __AUTH_CONST.__objc_const: 0xdd30
+  __AUTH_CONST.__objc_const: 0xbe40
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/MailCore.framework/Versions/A/MailCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58E45F47-9ADF-3037-BCBF-6949A49A740E
-  Functions: 1977
-  Symbols:   5482
+  UUID: B359C80F-2E4D-39C9-8C26-F4B4CFD92E41
+  Functions: 2071
+  Symbols:   5583
   CStrings:  4075
 
Symbols:
+ +[IMAPCommand _IMAPNeedsQuoteCharacterSet].cold.1
+ +[IMAPConnection log].cold.1
+ +[IMAPFetchCommand _fetchDataItemsForMessageSkeletons].cold.1
+ +[IMAPFetchDataItem UIDDataItem].cold.1
+ +[IMAPFetchDataItem appleRemoteLinksDataItem].cold.1
+ +[IMAPFetchDataItem bodyStructureDataItem].cold.1
+ +[IMAPFetchDataItem flagsDataItem].cold.1
+ +[IMAPFetchDataItem gmailLabelsDataItem].cold.1
+ +[IMAPFetchDataItem internalDateDataItem].cold.1
+ +[IMAPFetchDataItem modificationSequenceDataItem].cold.1
+ +[IMAPFetchDataItem sizeDataItem].cold.1
+ +[IMAPFramework logsIMAPErrors].cold.1
+ +[IMAPMessageDownload log].cold.1
+ +[IMAPTaskManager powerLog].cold.1
+ +[IMAPTaskManager sharedKeySetForMessageInfo].cold.1
+ +[IMAPTaskManager syncActivityLog].cold.1
+ -[IMAPAccountSyncTask initWithAccount:taskManager:].cold.1
+ -[IMAPClientData addDataArgument:literalPlus:].cold.1
+ -[IMAPClientData addStringArgument:].cold.1
+ -[IMAPConnection _recordUntaggedResponse:forCommand:exists:receivedExists:fromIDLE:].cold.1
+ -[IMAPConnection _recordUntaggedResponse:forCommand:exists:receivedExists:fromIDLE:].cold.2
+ -[IMAPConnection _responseFromSendingCommand:receivedExists:].cold.1
+ -[IMAPConnection _sendCommand:response:].cold.1
+ -[IMAPConnection _sendCommand:response:].cold.2
+ -[IMAPConnection executeAppend:].cold.1
+ -[IMAPConnection executeAuthenticate:].cold.1
+ -[IMAPConnection executeLogin:].cold.1
+ -[IMAPConnection executeUIDCopyOrMove:].cold.1
+ -[IMAPConnection setAccount:].cold.1
+ -[IMAPDownloadCache downloadForMessage:].cold.1
+ -[IMAPMailboxCommand initWithMailboxName:].cold.1
+ -[IMAPMailboxSyncState messageNumberForUID:orRange:].cold.1
+ -[IMAPMailboxSyncState removeMessageNumber:].cold.1
+ -[IMAPMailboxSyncState setUID:forMessageNumber:].cold.1
+ -[IMAPMailboxSyncState setUID:forMessageNumber:].cold.2
+ -[IMAPMailboxSyncState uidForMessageNumber:].cold.1
+ -[IMAPMailboxSyncTask _checkForWorkWithIMAPMailbox:canTrustExists:canTrustUnseen:allowUpdate:forceUpdate:].cold.1
+ -[IMAPMailboxSyncTask _imapMailboxSyncTaskCommonInitWithDataSource:taskManager:].cold.1
+ -[IMAPMailboxSyncTask fetchFlagsForMessageNumbers:].cold.1
+ -[IMAPMailboxSyncTask initWithDataSource:taskManager:imapMailbox:fromStatus:forceFullSync:].cold.1
+ -[IMAPMailboxSyncTask nextNetworkOperation].cold.1
+ -[IMAPMailboxSyncTask nextPersistenceOperation].cold.1
+ -[IMAPMessage setDataSource:].cold.1
+ -[IMAPMessageActionSyncOperation main].cold.2
+ -[IMAPMessageDownload _addMimeSubdownloadsToPipeline:withCache:].cold.1
+ -[IMAPMessageDownload _addMimeSubdownloadsToPipeline:withCache:].cold.2
+ -[IMAPMessageWithCache messageDataFetchIfNotAvailable:newDocumentID:].cold.1
+ -[IMAPNetworkBlockTask operationFinished:].cold.1
+ -[IMAPNetworkTaskHandler setOperation:].cold.1
+ -[IMAPNetworkTaskOperation setHandler:].cold.1
+ -[IMAPParseContext _parseBasicResponse].cold.1
+ -[IMAPParseContext _parseCapabilityResponse].cold.1
+ -[IMAPParseContext _parseEnabledResponse].cold.1
+ -[IMAPParseContext _parseFetchResponse].cold.1
+ -[IMAPParseContext _parseFlagsResponse].cold.1
+ -[IMAPParseContext _parseListResponse].cold.1
+ -[IMAPParseContext _parseNamespaceResponse].cold.1
+ -[IMAPParseContext _parseOtherResponse].cold.1
+ -[IMAPParseContext _parseQuotaResponse].cold.1
+ -[IMAPParseContext _parseQuotaRootResponse].cold.1
+ -[IMAPParseContext _parseSearchResponse].cold.1
+ -[IMAPParseContext _parseStatusResponse].cold.1
+ -[IMAPParseContext _parseStatusResponse].cold.2
+ -[IMAPParseContext _parseVanishedResponse].cold.1
+ -[IMAPPersistenceBlockTask operationFinished:].cold.1
+ -[IMAPServerInterface _sourceUIDsToDestinationUIDsFromMessageInfo:].cold.1
+ -[IMAPServerInterface _sourceUIDsToDestinationUIDsFromMessageInfo:].cold.2
+ -[IMAPStatusCommand initWithMailboxName:dataItems:].cold.1
+ -[IMAPTaskManager _createNetworkHandler].cold.1
+ -[IMAPTaskManager _createNewConnectionSynchronously:isFirstConnection:].cold.1
+ -[IMAPTaskManager _doCommandBlockForMailbox:block:async:ifSelected:priority:description:].cold.1
+ -[IMAPTaskManager activityDidFinish:].cold.1
+ -[IMAPTaskManager addActivity:].cold.1
+ -[IMAPTaskManager checkForNewLocalActions].cold.1
+ -[IMAPTaskManager connectToServer].cold.1
+ -[IMAPTaskManager newPersistenceHandler].cold.1
+ -[IMAPTaskManager secondaryIdleMailboxName].cold.1
+ -[IMAPTaskManager syncAccountForceFullSync:userInitiated:].cold.1
+ -[IMAPTaskManager syncMailboxWithDataSource:withIMAPMailbox:fromStatus:forceFullSync:userInitiated:].cold.1
+ -[IMAPTaskManager test_tearDown].cold.1
+ -[IMAPTaskManager test_terminateAndWaitUntilFinished].cold.1
+ -[IMAPTaskManager test_waitUntilAllTasksAreFinished].cold.1
+ -[IMAPTaskManager uidsVanished:withMessageNumbers:mailboxName:].cold.1
+ -[IMAPTaskManager uidsVanished:withRanges:mailboxName:].cold.1
+ -[IMAPUIDCommand initWithMailboxName:UIDs:].cold.1
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __23+[IMAPFramework bundle]_block_invoke.cold.1
+ __55-[IMAPTaskManager uidsVanished:withRanges:mailboxName:]_block_invoke_2.cold.1
+ __63-[IMAPTaskManager uidsVanished:withMessageNumbers:mailboxName:]_block_invoke_2.cold.1

```
