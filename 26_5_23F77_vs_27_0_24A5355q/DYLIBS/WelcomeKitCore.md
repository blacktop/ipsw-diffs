## WelcomeKitCore

> `/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore`

```diff

-1224.122.6.0.0
-  __TEXT.__text: 0x38734
-  __TEXT.__auth_stubs: 0xd30
+1410.0.0.0.0
+  __TEXT.__text: 0x3682c
   __TEXT.__objc_methlist: 0x336c
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0xb34e
-  __TEXT.__gcc_except_tab: 0xf64
-  __TEXT.__unwind_info: 0xe10
-  __TEXT.__objc_classname: 0x56d
-  __TEXT.__objc_methname: 0x881f
-  __TEXT.__objc_methtype: 0x17fa
-  __TEXT.__objc_stubs: 0x7960
-  __DATA_CONST.__got: 0x428
+  __TEXT.__cstring: 0xb384
+  __TEXT.__gcc_except_tab: 0xfcc
+  __TEXT.__unwind_info: 0xd08
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1230
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_selrefs: 0x21a0
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x6a8
+  __DATA_CONST.__got: 0x428
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x6de0
   __AUTH_CONST.__objc_const: 0x5120
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x11d0
   __DATA.__objc_ivar: 0x348
   __DATA.__data: 0x370

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 475A0CA6-6807-3B0B-AB26-7630C6377F2A
+  UUID: 15FC1AF8-0C4B-3F96-AE5E-2037D3D17113
   Functions: 1182
-  Symbols:   4620
-  CStrings:  3616
+  Symbols:   4624
+  CStrings:  1913
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.359
+ ___block_literal_global.406
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
- ___block_literal_global.352
- ___block_literal_global.360
- ___block_literal_global.407
Functions:
~ +[WLAuthenticationCredentials generateAuthenticationCredentialsContainingSelfSignedCertificate] : 248 -> 244
~ +[WLAuthenticationUtilities hashWithString:] : 268 -> 264
~ +[WLAuthenticationUtilities generateSelfSignedCertificateWithOrganization:commonName:completion:] : 668 -> 664
~ +[WLAuthenticationUtilities pemFormattedCertificateData:] : 172 -> 164
~ +[WLAuthenticationUtilities _appendBase64Data:toString:] : 108 -> 104
~ +[WLAuthenticationUtilities dataFromPEMFormattedData:] : 444 -> 440
~ +[WLCredentialStore sharedInstance] : 84 -> 68
~ -[WLCredentialStore setCredentials:forAuthentication:] : 148 -> 152
~ -[WLCredentialStore credentialsForAuthentication:] : 208 -> 204
~ -[WLSRPServer initWithUsername:password:] : 432 -> 428
~ -[WLSRPServer didReceiveClientPublicKey_A:proofOfMatch_M:] : 588 -> 564
~ -[WLSRPServer isHmacData:validForData:] : 216 -> 204
~ -[WLAutomation writeCodeForTestAutomationIfNeeded:] : 544 -> 516
~ -[WLAutomation deleteTestAutomationCachesIfNeeded] : 336 -> 316
~ +[WLDeviceDiscoveryController sharedInstance] : 84 -> 68
~ -[WLDeviceDiscoveryController init] : 184 -> 176
~ -[WLDeviceDiscoveryController sourceDevice] : 120 -> 116
~ -[WLDeviceDiscoveryController startWiFiAndDeviceDiscoveryWithPreGeneratedCode:completion:] : 224 -> 236
~ ___90-[WLDeviceDiscoveryController startWiFiAndDeviceDiscoveryWithPreGeneratedCode:completion:]_block_invoke_2 : 216 -> 224
~ ___84-[WLDeviceDiscoveryController _queue_startDiscoveryWithPreGeneratedCode:completion:]_block_invoke : 224 -> 220
~ -[WLDeviceDiscoveryController enableSoftAPWithSSID:password:channels:secret:srp:completion:] : 520 -> 560
~ -[WLDeviceDiscoveryController _enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:currentChannel:] : 484 -> 524
~ -[WLDeviceDiscoveryController softAPDidStart:ssid:psk:secret:srp:channel:error:completion:] : 1028 -> 1036
~ -[WLDeviceDiscoveryController listenerDidStart:srp:] : 508 -> 500
~ -[WLDeviceDiscoveryController stopDeviceDiscoveryWithCompletion:] : 200 -> 204
~ -[WLDeviceDiscoveryController stopWiFiAndDeviceDiscoveryWithCompletion:] : 200 -> 204
~ ___72-[WLDeviceDiscoveryController stopWiFiAndDeviceDiscoveryWithCompletion:]_block_invoke_2 : 196 -> 188
~ -[WLDeviceDiscoveryController _queue_stopWiFiAndDeviceDiscoveryWithCompletion:] : 336 -> 328
~ -[WLDeviceDiscoveryController importLocalContent] : 220 -> 212
~ -[WLDeviceDiscoveryController attemptDirectConnectionToAddress:] : 384 -> 364
~ -[WLDeviceDiscoveryController setNextIncomingConnectionHandler:] : 128 -> 132
~ -[WLDeviceDiscoveryController _ssidWithSecret:] : 156 -> 144
~ -[WLDeviceDiscoveryController listenForConnectionOnSocket:withConnectionHandler:] : 220 -> 224
~ -[WLDeviceDiscoveryController acceptIncomingConnectionWithListenerSocket:nonBlocking:] : 764 -> 756
~ -[WLDeviceDiscoveryController _allowConnectionsFromAnyAddress] : 156 -> 152
~ -[WLDeviceDiscoveryController deviceDiscoverySocketHandler:didDiscoverCandidate:] : 220 -> 224
~ -[WLDeviceDiscoveryController deviceDiscoverySocketHandler:didFinishHandshakeWithSourceDevice:] : 196 -> 200
~ -[WLDeviceDiscoveryController deviceDiscoverySocketHandler:didFailToHandshakeWithSourceDevice:error:] : 388 -> 392
~ ___101-[WLDeviceDiscoveryController deviceDiscoverySocketHandler:didFailToHandshakeWithSourceDevice:error:]_block_invoke : 156 -> 152
~ -[WLDeviceDiscoveryController setQueue:] : 64 -> 12
~ -[WLDeviceDiscoverySocketHandler initWithSocket:srpPassword:delegate:] : 216 -> 228
~ -[WLDeviceDiscoverySocketHandler resume] : 148 -> 144
~ -[WLDeviceDiscoverySocketHandler close] : 16 -> 20
~ -[WLDeviceDiscoverySocketHandler invalidateWithError:] : 144 -> 152
~ -[WLDeviceDiscoverySocketHandler _performSRPAuthenticationAndHandshake] : 4900 -> 4628
~ ___71-[WLDeviceDiscoverySocketHandler _performSRPAuthenticationAndHandshake]_block_invoke : 200 -> 192
~ ___71-[WLDeviceDiscoverySocketHandler _performSRPAuthenticationAndHandshake]_block_invoke_2 : 200 -> 192
~ ___71-[WLDeviceDiscoverySocketHandler _performSRPAuthenticationAndHandshake]_block_invoke_3 : 200 -> 192
~ -[WLDeviceDiscoverySocketHandler _commandStringWithData:] : 256 -> 248
~ -[WLDeviceDiscoverySocketHandler _okResponseData] : 104 -> 96
~ -[WLDeviceDiscoverySocketHandler _handshakeCommandData] : 104 -> 96
~ -[WLDeviceDiscoverySocketHandler _didReceiveHandshakeData:] : 372 -> 376
~ -[WLDeviceDiscoverySocketHandler _handshakeResponseData] : 780 -> 776
~ -[WLDeviceDiscoverySocketHandler sendData:completion:] : 196 -> 208
~ ___54-[WLDeviceDiscoverySocketHandler sendData:completion:]_block_invoke : 216 -> 220
~ ___54-[WLDeviceDiscoverySocketHandler sendData:completion:]_block_invoke_2 : 116 -> 124
~ -[WLDeviceDiscoverySocketHandler sockfd] : 16 -> 20
~ -[WLSourceDeviceHandshakeParser parseData:modifyingSourceDevice:completion:] : 404 -> 412
~ -[WLSourceDeviceHandshakeParser _parseDeviceInfoNode:modifyingSourceDevice:] : 2092 -> 1992
~ -[WLSourceDeviceHandshakeParser _parseConnectionFailureReasons:] : 208 -> 192
~ -[WLAccessibilityMigrator estimateItemSizeForSummary:account:] : 84 -> 76
~ -[WLAccessibilityMigrator importRecordData:summary:account:completion:] : 748 -> 740
~ -[WLApp initWithBundleIdentifier:appStoreIdentifier:isFree:] : 152 -> 156
~ -[WLApp setAppStoreIdentifier:] : 64 -> 12
~ -[NSError(WelcomeKit) wk_representsTransientConnectivityIssueForAttempt:] : 240 -> 232
~ -[WLAppMigrator initWithDevice:sqlController:] : 136 -> 140
~ -[WLAppMigrator estimateItemSizeForSummary:account:] : 84 -> 76
~ -[WLAppMigrator importDataFromProvider:forSummaries:summaryStart:summaryCompletion:] : 1232 -> 1216
~ ___84-[WLAppMigrator importDataFromProvider:forSummaries:summaryStart:summaryCompletion:]_block_invoke : 112 -> 104
~ -[WLAppMigrator _lookupStoreItemsMatchingExternalIDs:attempt:completion:] : 268 -> 280
~ ___73-[WLAppMigrator _lookupStoreItemsMatchingExternalIDs:attempt:completion:]_block_invoke : 524 -> 516
~ -[WLAppMigrator _insertMatchingApps:] : 696 -> 652
~ +[WLAppMigrator installMigratableApps:completion:] : 204 -> 212
~ ___50+[WLAppMigrator installMigratableApps:completion:]_block_invoke : 156 -> 148
~ ___50+[WLAppMigrator installMigratableApps:completion:]_block_invoke_2 : 188 -> 180
~ +[WLAppMigrator _sendStoreDownloadRequestForFreeMigratableApps:completion:] : 1300 -> 1276
~ ___75+[WLAppMigrator _sendStoreDownloadRequestForFreeMigratableApps:completion:]_block_invoke : 348 -> 320
~ ___75+[WLAppMigrator _sendStoreDownloadRequestForFreeMigratableApps:completion:]_block_invoke_2 : 148 -> 140
~ +[WLAppMigrator _ssItemForiTunesStoreIdentifier:] : 376 -> 388
~ -[WLAppMigrator setDevice:] : 64 -> 12
~ -[WLAppMigrator setSqlController:] : 64 -> 12
~ -[WLAppSearchRequest initWithAndroidIdentifiers:] : 144 -> 140
~ -[WLAppSearchRequest search:] : 528 -> 508
~ ___29-[WLAppSearchRequest search:]_block_invoke : 948 -> 912
~ -[WLBookmarksMigrator estimateItemSizeForSummary:account:] : 84 -> 76
~ -[WLBookmarksMigrator importWillBegin] : 444 -> 432
~ +[WLBookmarksMigrator _createBookmarkFolderWithTitle:UUID:] : 212 -> 216
~ +[WLBookmarksMigrator _createRootBookmarkFolder] : 228 -> 208
~ +[WLBookmarksMigrator _bookmarkFolderAtTitlePath:withinBookmarkFolder:] : 648 -> 624
~ +[WLBookmarksMigrator _bookmarkFolderAtTitlePath:withinRootFolder:] : 200 -> 184
~ -[WLBookmarksMigrator importDataFromProvider:forSummaries:summaryStart:summaryCompletion:] : 1888 -> 1864
~ -[WLCalendarMigrator estimateItemSizeForSummary:account:] : 84 -> 76
~ -[WLCalendarMigrator importRecordData:summary:account:completion:] : 236 -> 240
~ -[WLCalendarMigrator _importDataRecord:summary:] : 204 -> 200
~ -[WLContactsMigrator estimateItemSizeForSummary:account:] : 84 -> 76
~ -[WLContactsMigrator importRecordData:summary:account:completion:] : 1008 -> 1012
~ -[WLContactsMigrator _vcardDataWithoutCustomFieldsFromVcardData:] : 1004 -> 960
~ -[WLContactsMigrator setContactStore:] : 64 -> 12
~ -[WLDisplayMigrator estimateItemSizeForSummary:account:] : 84 -> 76
~ -[WLDisplayMigrator importRecordData:summary:account:completion:] : 656 -> 648
~ -[WLMailAccountMigrator init] : 720 -> 696
~ -[WLMailAccountMigrator estimateItemSizeForSummary:account:] : 84 -> 76
~ -[WLMailAccountMigrator importRecordData:summary:account:completion:] : 1272 -> 1252
~ -[WLMailAccountMigrator importWillBegin] : 264 -> 256
~ -[WLMailAccountMigrator setAccountStore:] : 64 -> 12
~ +[WLMessage _populateMimeHeaders:recipients:fromRange:ofString:addCountryCodeToParties:sqlController:] : 728 -> 704
~ +[WLMessage _dateFormatterForMimeDateStrings] : 84 -> 68
~ ___45+[WLMessage _dateFormatterForMimeDateStrings]_block_invoke : 188 -> 184
~ +[WLMessage dateFromMimeHeaders:] : 216 -> 204
~ -[WLMessage parseMIMEData:sqlController:] : 2180 -> 2084
~ +[WLMessage _fileNameForPart:smilContext:] : 624 -> 600
~ ___41+[WLMessage _shouldIgnoreMessageThreadID]_block_invoke : 144 -> 140
~ -[WLMessage progressiveMimeParser:finishedMimePart:] : 992 -> 948
~ -[WLMessage summary] : 56 -> 8
~ -[WLMessage setSummary:] : 64 -> 12
~ -[WLMessage setSender:] : 64 -> 12
~ -[WLMessage setRecipients:] : 64 -> 12
~ -[WLMessageAttachment _initWithData:fileName:mimeType:uti:] : 208 -> 224
~ -[WLMessageParty _initWithAddress:addCountryCode:sqlController:] : 1860 -> 1760
~ +[WLMessageParty _guessIccForNumber:] : 440 -> 428
~ ___37+[WLMessageParty _guessIccForNumber:]_block_invoke : 244 -> 232
~ +[WLMessageParty _normalize:] : 308 -> 292
~ ___29+[WLMessageParty _normalize:]_block_invoke : 228 -> 220
~ -[NSData(WLMessage) wl_subdataWithRangeExcludingTrailingCrnl:] : 268 -> 256
~ -[WLMessageSMILContext parser:didStartElement:namespaceURI:qualifiedName:attributes:] : 320 -> 316
~ -[WLMessageSMILContext parser:didEndElement:namespaceURI:qualifiedName:] : 224 -> 220
~ -[WLMessageSMILContext parser:foundCharacters:] : 140 -> 136
~ -[WLMessageSMILPart initWithElementName:attributes:] : 144 -> 152
~ -[WLMessageSMILPart fileName] : 108 -> 100
~ -[WLMessagesMigrator estimateItemSizeForSummary:account:] : 84 -> 76
~ -[WLMessagesMigrator performPreImportPhaseForSummary:data:] : 1020 -> 964
~ -[WLMessagesMigrator importWillBegin] : 356 -> 340
~ -[WLMessagesMigrator importDidEnd] : 180 -> 172
~ -[WLMessagesMigrator _databaseFilename] : 92 -> 84
~ -[WLMessagesMigrator _openDatabase] : 136 -> 132
~ -[WLMessagesMigrator _performSimpleQuery:] : 264 -> 260
~ -[WLMessagesMigrator _ourAddressWithMessage:] : 216 -> 192
~ -[WLMessagesMigrator _otherPartyAddressWithNonGroupMessage:] : 200 -> 176
~ -[WLMessagesMigrator _insertMessage:] : 2528 -> 2392
~ +[WLMessagesMigrator _attachmentPersistentPathForGuid:fileName:mimeType:uti:] : 708 -> 656
~ -[WLMessagesMigrator _insertRowWithAttachment:filePath:forMessage:] : 856 -> 836
~ -[WLMessagesMigrator _handleIDsForMessage:] : 1108 -> 1116
~ -[WLMessagesMigrator _uniqueHandleStringsWithMessage:] : 728 -> 692
~ -[WLMessagesMigrator _senderHandleIDFromReceivedGroupMessageHandleIDs:] : 68 -> 64
~ -[WLMessagesMigrator _handleIDFromNonGroupMessageHandleIDs:] : 68 -> 64
~ -[WLMessagesMigrator _chatIDForHandleIDs:groupRoomName:groupID:message:] : 2044 -> 2056
~ -[WLMessagesMigrator _chatGUIDWithNonGroupMessage:] : 112 -> 104
~ -[WLMessagesMigrator _chatAccountIDWithMessage:] : 56 -> 8
~ -[WLMessagesMigrator _chatAccountLoginWithMessage:] : 112 -> 104
~ -[WLMessagesMigrator _insertMessageRowWithMessage:handleIDs:groupRoomName:] : 1324 -> 1296
~ -[WLMessagesMigrator _messageAttributedBodyDataWithMessage:] : 612 -> 588
~ -[WLMessagesMigrator _messageAccountWithMessage:] : 112 -> 104
~ -[WLMessagesMigrator _messageAccountGUIDWithMessage:] : 56 -> 8
~ -[WLMessagesMigrator _messageDateWithMessage:] : 76 -> 72
~ -[WLMessagesMigrator _messageDateReadWithMessage:] : 76 -> 72
~ -[WLMessagesMigrator _messageDateDeliveredWithMessage:] : 76 -> 72
~ -[WLMessagesMigrator _attachmentDateWithMessage:] : 64 -> 60
~ -[WLMessagesMigrator _updateClient] : 336 -> 332
~ -[WLMessagesMigrator isValidTableName:] : 184 -> 172
~ -[WLMessagesMigrator deleteFromTable:] : 336 -> 332
~ -[WLMessagesMigrator setSqlController:] : 64 -> 12
~ -[WLFileProvider fetchRootPath] : 492 -> 472
~ -[WLFilesMigrator init] : 172 -> 168
~ -[WLFilesMigrator importRecordData:summary:account:completion:] : 1808 -> 1720
~ -[WLPhotoLibrary init] : 408 -> 388
~ -[WLPhotoLibrary addAsset:filename:size:collection:completion:] : 796 -> 808
~ ___63-[WLPhotoLibrary addAsset:filename:size:collection:completion:]_block_invoke_2 : 152 -> 156
~ -[WLPhotoLibrary addAsset:collection:] : 512 -> 488
~ -[WLPhotoLibrary photoLibraryDidComplete:filename:success:error:] : 312 -> 300
~ -[WLPhotoLibrary copy:filename:error:] : 548 -> 520
~ -[WLPhotoLibrary assetCollectionChangeRequest:] : 260 -> 240
~ -[WLPhotosMigrator importRecordData:summary:account:completion:] : 372 -> 360
~ -[WLVideosMigrator importRecordData:summary:account:completion:] : 372 -> 360
~ -[WLSourceDeviceAccount initWithInfo:] : 100 -> 96
~ +[WLSourceDeviceAccount accountInfoArrayContainsNonSyncableAccount:] : 328 -> 324
~ +[WLSourceDeviceAccount accountInfoRepresentsSyncableAccount:] : 80 -> 76
~ -[WLSourceDeviceMigrationMetadata setCommunicationDate:] : 64 -> 12
~ -[WLSourceDeviceMigrationMetadata setDeviceOSVersion:] : 64 -> 12
~ -[WLSourceDeviceMigrationMetadata setDeviceType:] : 64 -> 12
~ -[WLSourceDeviceMigrationMetadata setDeviceModel:] : 64 -> 12
~ +[WLSourceDeviceRecordSummary summaryWithInfo:account:] : 112 -> 116
~ +[WLSourceDeviceRecordSummary _numberFormatter] : 84 -> 68
~ -[WLSourceDeviceRecordSummary initWithInfo:account:] : 692 -> 648
~ -[WLSourceDeviceRecordSummary setAccount:] : 64 -> 12
~ -[WLItemSizeConfirmationCompletionAdapter initWithUnconfirmedItemSize:segmentSize:originalSegmentCompletion:originalCompletion:] : 412 -> 420
~ ___128-[WLItemSizeConfirmationCompletionAdapter initWithUnconfirmedItemSize:segmentSize:originalSegmentCompletion:originalCompletion:]_block_invoke_2 : 200 -> 196
~ +[WLLocalDataSource _localSourceDataPath] : 84 -> 68
~ ___41+[WLLocalDataSource _localSourceDataPath]_block_invoke : 100 -> 92
~ +[WLLocalDataSource localDataExists] : 132 -> 124
~ -[WLLocalDataSource accountsDataForMigrator:completion:] : 804 -> 760
~ -[WLLocalDataSource summariesDataForAccount:migrator:completion:] : 1020 -> 972
~ -[WLLocalDataSource fileForSummary:migrator:fileAccessor:completion:] : 280 -> 264
~ -[WLLocalDataSource dataForSummary:migrator:completion:] : 320 -> 304
~ ___73-[WLLocalDataSource dataSegmentForSummary:byteRange:migrator:completion:]_block_invoke : 164 -> 160
~ -[WLLocalDataSource itemSizeForSummary:migrator:completion:] : 104 -> 100
~ +[WLLocalDataSource deleteLocalData] : 168 -> 164
~ +[WLLocalDataSource _relativePathForAccount:migrator:] : 316 -> 288
~ +[WLLocalDataSource _relativePathForSummary:migrator:] : 424 -> 384
~ +[WLLocalDataSource stashFileForSummary:migrator:] : 492 -> 464
~ +[WLLocalDataSource stashData:forSummary:migrator:] : 464 -> 444
~ -[WLMigrationContext setSourceDevice:] : 64 -> 12
~ -[WLMigrationContext setDelegate:] : 64 -> 12
~ -[WLMigrationContext setDataSource:] : 64 -> 12
~ -[WLMigrationContext setDataCoordinator:] : 64 -> 12
~ -[WLMigrationContext setSqlController:] : 64 -> 12
~ -[WLMigrationContext setMigrators:] : 64 -> 12
~ -[WLMigrationContext setLastProgressSentDate:] : 64 -> 12
~ -[WLMigrationContext setThroughputSegmentStartDate:] : 64 -> 12
~ -[WLMigrationContext setThroughputSamples:] : 64 -> 12
~ -[WLMigrationContext setTimeEstimateAccuracyTracker:] : 64 -> 12
~ -[WLMigrationContext setUrlSessionController:] : 64 -> 12
~ -[WLMigrationContext setAggregateStatistics:] : 64 -> 12
~ -[WLMigrationContext setMetadata:] : 64 -> 12
~ -[WLMigrationContext setImportErrors:] : 64 -> 12
~ -[WLMigrationContext setPayload:] : 64 -> 12
~ -[WLMigrationDataCoordinator init] : 144 -> 136
~ -[WLMigrationDataCoordinator fetchAccountsAndSummariesFromSource:forMigrator:statistics:accountsRequestDurationBlock:summariesRequestDurationBlock:completion:] : 404 -> 444
~ ___159-[WLMigrationDataCoordinator fetchAccountsAndSummariesFromSource:forMigrator:statistics:accountsRequestDurationBlock:summariesRequestDurationBlock:completion:]_block_invoke : 796 -> 800
~ ___89-[WLMigrationDataCoordinator _fetchAccountsFromSource:forMigrator:statistics:completion:]_block_invoke : 540 -> 536
~ -[WLMigrationDataCoordinator _fetchSummariesFromSource:forMigrator:account:statistics:completion:] : 404 -> 424
~ ___98-[WLMigrationDataCoordinator _fetchSummariesFromSource:forMigrator:account:statistics:completion:]_block_invoke : 632 -> 616
~ -[WLMigrationDataCoordinator downloadFileFromSource:forMigrator:summary:account:segmentCompletion:completion:] : 1036 -> 1076
~ ___110-[WLMigrationDataCoordinator downloadFileFromSource:forMigrator:summary:account:segmentCompletion:completion:]_block_invoke : 304 -> 292
~ ___110-[WLMigrationDataCoordinator downloadFileFromSource:forMigrator:summary:account:segmentCompletion:completion:]_block_invoke_2 : 332 -> 324
~ ___110-[WLMigrationDataCoordinator downloadFileFromSource:forMigrator:summary:account:segmentCompletion:completion:]_block_invoke_3 : 180 -> 176
~ ___49+[WLMigrationDataCoordinator downloadSegmentSize]_block_invoke : 184 -> 180
~ -[WLMigrationDataCoordinator _downloadSegmentsFromSource:forMigrator:startingAtByteLocation:ofSummary:account:itemSize:toFileHandle:segmentCompletion:completion:] : 660 -> 688
~ ___162-[WLMigrationDataCoordinator _downloadSegmentsFromSource:forMigrator:startingAtByteLocation:ofSummary:account:itemSize:toFileHandle:segmentCompletion:completion:]_block_invoke : 252 -> 256
~ -[WLMigrationDataCoordinator _downloadFileInMultipleSegmentsFromSource:forMigrator:summary:account:itemSize:segmentCompletion:completion:] : 948 -> 912
~ ___138-[WLMigrationDataCoordinator _downloadFileInMultipleSegmentsFromSource:forMigrator:summary:account:itemSize:segmentCompletion:completion:]_block_invoke : 148 -> 144
~ -[WLMigrationDataCoordinator downloadDataFromSource:forMigrator:summary:account:completion:] : 436 -> 452
~ ___92-[WLMigrationDataCoordinator downloadDataFromSource:forMigrator:summary:account:completion:]_block_invoke : 256 -> 252
~ -[WLMigrationDataCoordinator importDataForMigrator:fromProvider:forSummaries:summaryStart:summaryCompletion:] : 984 -> 1012
~ ___81-[WLMigrationDataCoordinator updateSource:withProgress:remainingTime:completion:]_block_invoke : 140 -> 132
~ -[WLMigrationDataCoordinator _recordSummaryForMigrator:withInfo:account:] : 656 -> 616
~ -[WLMigrator _deleteDownloadsPath:] : 156 -> 164
~ -[WLMigrator _prepareMetadata:usingRetryPolicies:allowContinuationFromAnotherDevice:] : 592 -> 572
~ -[WLMigrator startMigrationWithSourceDevice:usingRetryPolicies:delegate:completion:] : 180 -> 184
~ -[WLMigrator prepare:delegate:error:] : 1508 -> 1396
~ -[WLMigrator startMigration:usingRetryPolicies:completion:] : 2116 -> 1920
~ -[WLMigrator migrators:] : 1260 -> 1156
~ -[WLMigrator fetchSummary:] : 804 -> 724
~ -[WLMigrator selectDataTypes:] : 588 -> 540
~ -[WLMigrator downloadData:] : 1396 -> 1344
~ ___27-[WLMigrator downloadData:]_block_invoke.115 : 72 -> 16
~ -[WLMigrator importData:] : 1188 -> 1116
~ ___25-[WLMigrator importData:]_block_invoke : 72 -> 16
~ -[WLMigrator runPostMigrationTasks:] : 104 -> 96
~ -[WLMigrator finishMigration:] : 1032 -> 972
~ -[WLMigrator _finishMigrationWithError:context:disconnected:completion:] : 1012 -> 944
~ -[WLMigrator _fetchAccountsAndSummariesWithContext:] : 1220 -> 1184
~ ___52-[WLMigrator _fetchAccountsAndSummariesWithContext:]_block_invoke : 312 -> 280
~ ___52-[WLMigrator _fetchAccountsAndSummariesWithContext:]_block_invoke_2 : 312 -> 280
~ ___52-[WLMigrator _fetchAccountsAndSummariesWithContext:]_block_invoke_3 : 632 -> 628
~ -[WLMigrator _selectDataTypesWithContext:] : 2232 -> 2152
~ ___42-[WLMigrator _selectDataTypesWithContext:]_block_invoke : 380 -> 344
~ ___42-[WLMigrator _selectDataTypesWithContext:]_block_invoke_2 : 200 -> 196
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke : 2744 -> 2724
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_2 : 220 -> 204
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_3 : 248 -> 232
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_4 : 152 -> 148
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_5 : 172 -> 168
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_6 : 152 -> 148
~ ___61-[WLMigrator _selectFromDataTypeToSizeMap:device:completion:]_block_invoke_8 : 152 -> 148
~ +[WLMigrator _dataTypesAndSizesXMLDataFromMap:] : 692 -> 640
~ +[WLMigrator _parseDataTypesXMLData:completion:] : 784 -> 768
~ -[WLMigrator _downloadDataWithContext:failureDetailsBlock:] : 4112 -> 3916
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke : 260 -> 248
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_3 : 160 -> 152
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_4 : 108 -> 104
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_5 : 348 -> 344
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_7 : 380 -> 352
~ ___59-[WLMigrator _downloadDataWithContext:failureDetailsBlock:]_block_invoke_8 : 552 -> 536
~ -[WLMigrator _didFinishDownloadingSegmentOfSize:expectedSize:migratorEstimatesItemSizes:endDate:context:] : 1456 -> 1392
~ -[WLMigrator _reportTimeEstimatesWithContext:] : 140 -> 132
~ ___46-[WLMigrator _reportTimeEstimatesWithContext:]_block_invoke : 144 -> 140
~ -[WLMigrator _importDataWithContext:failureDetailsBlock:] : 1948 -> 1876
~ ___57-[WLMigrator _importDataWithContext:failureDetailsBlock:]_block_invoke : 116 -> 108
~ ___57-[WLMigrator _importDataWithContext:failureDetailsBlock:]_block_invoke_2 : 100 -> 96
~ ___57-[WLMigrator _importDataWithContext:failureDetailsBlock:]_block_invoke_3 : 600 -> 568
~ -[WLMigrator _progressIncrementForImportedSummary:summaries:accounts:migrators:] : 152 -> 156
~ -[WLMigrator _logStatisticsAndSendStatisticsTelemetryWithContext:] : 1544 -> 1420
~ +[WLMigrator _systemVersion] : 88 -> 84
~ -[WLMigrator close:] : 224 -> 228
~ -[WLMigrator cleanup] : 148 -> 140
~ -[WLMigrator finalizeMigratableAppsWithCompletion:] : 368 -> 360
~ ___51-[WLMigrator finalizeMigratableAppsWithCompletion:]_block_invoke : 368 -> 360
~ +[WLMigrator _presentPromptForMigrableApps:] : 500 -> 480
~ -[WLMigrator _cleanUpAfterFinalizeMigratableAppsWithSQLController:completion:] : 116 -> 112
~ -[WLMigrator _setProgressTo:context:] : 228 -> 212
~ -[WLMigrator _incrementProgressBy:context:] : 256 -> 240
~ -[WLMigrator _updateSourceWithProgress:remainingTime:context:completion:] : 564 -> 544
~ ___73-[WLMigrator _updateSourceWithProgress:remainingTime:context:completion:]_block_invoke_2 : 196 -> 192
~ +[WLMigrator _bytesFreeOnDevice] : 180 -> 176
~ -[WLMigrator setDataSource:] : 64 -> 12
~ -[WLRemoteDeviceDataSource accountsDataForMigrator:completion:] : 280 -> 276
~ ___63-[WLRemoteDeviceDataSource accountsDataForMigrator:completion:]_block_invoke : 460 -> 468
~ -[WLRemoteDeviceDataSource _urlForAccountsWithMigrator:] : 220 -> 204
~ -[WLRemoteDeviceDataSource summariesDataForAccount:migrator:completion:] : 328 -> 324
~ ___72-[WLRemoteDeviceDataSource summariesDataForAccount:migrator:completion:]_block_invoke : 464 -> 472
~ -[WLRemoteDeviceDataSource _urlForRecordSummariesForMigrator:withAccountIdentifier:] : 412 -> 376
~ -[WLRemoteDeviceDataSource itemSizeForSummary:migrator:completion:] : 384 -> 372
~ -[WLRemoteDeviceDataSource fileForSummary:migrator:fileAccessor:completion:] : 404 -> 396
~ ___76-[WLRemoteDeviceDataSource fileForSummary:migrator:fileAccessor:completion:]_block_invoke : 168 -> 164
~ -[WLRemoteDeviceDataSource _urlForRecordForMigrator:withSummaryIdentifier:accountIdentifier:segmentByteRange:] : 716 -> 668
~ -[WLRemoteDeviceDataSource _performDownloadRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:] : 488 -> 500
~ ___131-[WLRemoteDeviceDataSource _performDownloadRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:]_block_invoke : 292 -> 284
~ -[WLRemoteDeviceDataSource _downloadTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:] : 368 -> 392
~ ___132-[WLRemoteDeviceDataSource _downloadTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:]_block_invoke : 1376 -> 1352
~ ___132-[WLRemoteDeviceDataSource _downloadTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:]_block_invoke_5 : 280 -> 272
~ -[WLRemoteDeviceDataSource dataSegmentForSummary:byteRange:migrator:completion:] : 388 -> 376
~ ___80-[WLRemoteDeviceDataSource dataSegmentForSummary:byteRange:migrator:completion:]_block_invoke : 256 -> 244
~ -[WLRemoteDeviceDataSource dataForSummary:migrator:completion:] : 380 -> 368
~ ___63-[WLRemoteDeviceDataSource dataForSummary:migrator:completion:]_block_invoke : 256 -> 244
~ -[WLRemoteDeviceDataSource updateUIWithProgress:remainingTime:logString:completion:] : 464 -> 448
~ -[WLRemoteDeviceDataSource _urlScheme] : 84 -> 68
~ +[WLRemoteDeviceDataSource _requestSerialQueue] : 84 -> 68
~ ___47+[WLRemoteDeviceDataSource _requestSerialQueue]_block_invoke : 108 -> 104
~ -[WLRemoteDeviceDataSource _performRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:] : 408 -> 420
~ ___174-[WLRemoteDeviceDataSource _performRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:]_block_invoke : 348 -> 336
~ -[WLRemoteDeviceDataSource _runTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:] : 508 -> 516
~ ___178-[WLRemoteDeviceDataSource _runTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:]_block_invoke : 744 -> 728
~ ___178-[WLRemoteDeviceDataSource _runTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:]_block_invoke_2 : 704 -> 688
~ -[WLRemoteDeviceDataSource _taskDurationSinceStartDate:] : 96 -> 92
~ -[WLRemoteDeviceDataSource _shouldRetryLaterWithResponse:error:] : 156 -> 160
~ -[WLRemoteDeviceDataSource _shouldRetryWithData:response:error:] : 212 -> 208
~ -[WLRemoteDeviceDataSource _newNumberOfRetriesAllowed:startDate:] : 212 -> 204
~ -[WLRemoteDeviceDataSource setSession:] : 64 -> 12
~ -[WLThroughputSample setStartDate:] : 64 -> 12
~ -[WLThroughputSample setEndDate:] : 64 -> 12
~ -[WLTimeEstimateSample setStartDate:] : 64 -> 12
~ -[WLTimeEstimateSample setAssociatedObject:] : 64 -> 12
~ -[WLTimeEstimateAccuracyTracker _thresholdAtIndex:] : 220 -> 200
~ -[WLTimeEstimateAccuracyTracker didCalculateTimeEstimate:atDate:associatedObject:] : 328 -> 320
~ -[WLTimeEstimateAccuracyTracker estimatesDidResolveAtDate:block:] : 420 -> 416
~ -[WLTimeEstimateAccuracyTracker setThresholds:] : 64 -> 12
~ -[WLTimeEstimateAccuracyTracker setSamples:] : 64 -> 12
~ -[WLURLSessionController initWithAuthentication:] : 280 -> 272
~ -[WLURLSessionController URLSession:didReceiveChallenge:completionHandler:] : 1052 -> 988
~ -[NSDictionary(Integer) wl_integerForKey:] : 128 -> 124
~ -[NSDictionary(String) wl_stringForKey:] : 104 -> 88
~ -[WLXMLSerialization XMLObjectWithString:] : 104 -> 96
~ -[WLXMLSerialization XMLObjectWithData:] : 168 -> 164
~ -[WLXMLSerialization parseXMLContent:] : 492 -> 476
~ -[NSData(Hex) wl_blobIsComplete] : 156 -> 152
~ +[NSData(Hex) wl_lengthPrefixedBlobSequenceFromDataArray:] : 368 -> 360
~ -[NSData(Hex) wl_lengthPrefixedBlob] : 204 -> 192
~ -[NSData(Hex) wl_arrayOfDataFromLengthPrefixedBlobSequenceWithExpectedCount:] : 476 -> 456
~ -[NSData(Hex) wl_dataFromLengthPrefixedBlob] : 88 -> 80
~ -[NSData(Hex) wl_hexEncodedData] : 88 -> 80
~ +[NSData(Hex) wl_dataFromHexEncodedData:] : 100 -> 92
~ ___34-[NSData(Hex) wl_hexEncodedString]_block_invoke : 72 -> 80
~ +[NSData(Hex) wl_dataFromHexEncodedString:] : 448 -> 432
~ -[WLServerConnection close] : 348 -> 352
~ -[WLServerConnection _accept:] : 560 -> 556
~ -[WLSocketCommandMessage command] : 16 -> 20
~ -[WLSocketHandler observeSocket:forSourceEventType:handler:] : 220 -> 224
~ ___58+[WLSocketHandler lookupAndConnectToHost:port:completion:]_block_invoke : 664 -> 648
~ -[WLSocketHandler beginReadingIntoCacheFromSocket:] : 236 -> 232
~ -[WLSocketHandler _readIntoCacheFromSocket:] : 376 -> 368
~ -[WLSocketHandler endReadingIntoCache] : 140 -> 136
~ -[WLSocketHandler waitForDataFromReadCacheReturningError:] : 424 -> 412
~ -[WLSocketHandler waitForBlobDataFromReadCacheReturningError:] : 480 -> 472
~ -[WLSocketHandler waitForCommand:fromReadCacheReturningError:] : 588 -> 564
~ -[WLSocketHandler waitForMessageFromReadCacheReturningError:] : 392 -> 372
~ +[WLSocketHandler _commandStringWithData:] : 256 -> 248
~ -[WLSocketHandler _writeBytes:offset:length:toSocket:completion:] : 524 -> 516
~ -[WLSocketHandler sendCommand:toSocket:completion:] : 280 -> 276
~ -[WLSocketHandler sendData:toSocket:completion:] : 224 -> 228
~ ___48-[WLSocketHandler sendData:toSocket:completion:]_block_invoke : 112 -> 120
~ -[WLSocketHandler cancel] : 296 -> 288
~ +[WLSocketMessage messageWithData:error:] : 2072 -> 1960
~ -[WLSocketVersionMessage version] : 16 -> 20
~ -[WLSocketVersionMessage setVersion:] : 16 -> 20
~ -[WLSQLController init] : 180 -> 172
~ -[WLSQLController databasePath] : 56 -> 8
~ -[WLSQLController insertAccount:migrator:device:] : 276 -> 284
~ ___49-[WLSQLController insertAccount:migrator:device:]_block_invoke : 484 -> 468
~ -[WLSQLController accountsForMigrator:device:] : 340 -> 348
~ ___46-[WLSQLController accountsForMigrator:device:]_block_invoke : 640 -> 620
~ -[WLSQLController deleteAccountsAndSummariesForMigrator:device:] : 240 -> 252
~ ___64-[WLSQLController deleteAccountsAndSummariesForMigrator:device:]_block_invoke : 800 -> 776
~ -[WLSQLController insertRecordSummary:account:] : 240 -> 252
~ ___47-[WLSQLController insertRecordSummary:account:]_block_invoke : 1004 -> 968
~ ___104-[WLSQLController _totalSummarySegmentCountForAccounts:migrationStateComparisonOperator:migrationState:]_block_invoke : 760 -> 756
~ -[WLSQLController totalSummaryItemSizeForAccounts:addOverhead:completion:] : 284 -> 292
~ ___74-[WLSQLController totalSummaryItemSizeForAccounts:addOverhead:completion:]_block_invoke : 816 -> 808
~ -[WLSQLController setData:forSummary:] : 188 -> 196
~ -[WLSQLController dataForSummary:] : 276 -> 272
~ ___34-[WLSQLController dataForSummary:]_block_invoke : 424 -> 420
~ -[WLSQLController setDidDownloadForSummary:forSourceDevice:] : 160 -> 152
~ -[WLSQLController setWillImportForSummary:] : 160 -> 152
~ -[WLSQLController removeDataAndSetDidImportForSummary:] : 160 -> 152
~ -[WLSQLController setMigrationError:forSummary:] : 312 -> 308
~ -[WLSQLController migrationErrors] : 208 -> 188
~ ___34-[WLSQLController migrationErrors]_block_invoke : 640 -> 624
~ -[WLSQLController updateModifiedDateForSummary:] : 160 -> 152
~ ___48-[WLSQLController updateModifiedDateForSummary:]_block_invoke : 312 -> 308
~ -[WLSQLController summariesForAccount:] : 196 -> 188
~ -[WLSQLController summariesForAccounts:sortedByModifiedDate:] : 656 -> 664
~ ___61-[WLSQLController summariesForAccounts:sortedByModifiedDate:]_block_invoke : 1624 -> 1580
~ -[WLSQLController migrationMetadataForSourceDevice:strictMatch:] : 600 -> 556
~ ___64-[WLSQLController migrationMetadataForSourceDevice:strictMatch:]_block_invoke : 544 -> 532
~ -[WLSQLController insertMetadata:forSourceDevice:] : 188 -> 200
~ ___50-[WLSQLController insertMetadata:forSourceDevice:]_block_invoke : 468 -> 456
~ -[WLSQLController setMetadata:forSourceDevice:] : 188 -> 196
~ ___47-[WLSQLController setMetadata:forSourceDevice:]_block_invoke : 464 -> 452
~ -[WLSQLController insertMigratableApp:forDevice:] : 300 -> 304
~ ___49-[WLSQLController insertMigratableApp:forDevice:]_block_invoke : 388 -> 380
~ ___44-[WLSQLController _migratableAppsForDevice:]_block_invoke : 808 -> 788
~ -[WLSQLController insertMessagePhoneNumberWithIcc:ccAcNumber:] : 188 -> 196
~ -[WLSQLController messagePhoneNumberIccForCcAcNumber:] : 276 -> 272
~ ___54-[WLSQLController messagePhoneNumberIccForCcAcNumber:]_block_invoke : 408 -> 404
~ -[WLSQLController groupMessageInfoMatchingSourceThreadID:] : 276 -> 272
~ ___58-[WLSQLController groupMessageInfoMatchingSourceThreadID:]_block_invoke : 504 -> 492
~ -[WLSQLController groupMessageInfoMatchingSortedHandleIDs:handleIDsAreComplete:didMatchExactly:] : 424 -> 428
~ ___96-[WLSQLController groupMessageInfoMatchingSortedHandleIDs:handleIDsAreComplete:didMatchExactly:]_block_invoke : 572 -> 556
~ ___96-[WLSQLController groupMessageInfoMatchingSortedHandleIDs:handleIDsAreComplete:didMatchExactly:]_block_invoke_2 : 716 -> 692
~ -[WLSQLController _foundHandleIDs:representSameGroupMessageAsHandleIDs:handleIDsAreComplete:] : 128 -> 124
~ -[WLSQLController insertGroupMessageInfoWithSourceThreadID:roomName:groupID:] : 220 -> 228
~ -[WLSQLController insertGroupMessageInfoWithSortedHandleIDs:handleIDsAreComplete:roomName:groupID:] : 228 -> 244
~ ___99-[WLSQLController insertGroupMessageInfoWithSortedHandleIDs:handleIDsAreComplete:roomName:groupID:]_block_invoke : 444 -> 440
~ -[WLSQLController statisticsForContentType:] : 232 -> 220
~ ___44-[WLSQLController statisticsForContentType:]_block_invoke : 632 -> 624
~ -[WLSQLController updateStatistics:] : 160 -> 152
~ ___36-[WLSQLController updateStatistics:]_block_invoke : 584 -> 572
~ -[WLSQLController _insertStatistics_onDatabaseQueue:] : 584 -> 572
~ -[WLSQLController _openDatabase] : 272 -> 260
~ -[WLSQLController _ensureCorrectSchema] : 548 -> 544
~ ___33-[WLSQLController _schemaVersion]_block_invoke : 136 -> 132
~ -[WLSQLController _performQuery:rowHandler:] : 240 -> 248
~ ___44-[WLSQLController _performQuery:rowHandler:]_block_invoke : 568 -> 552
~ -[WLSQLController _sqlite3_column_NSDateForStatement:column:] : 80 -> 76
~ +[WLGroupMessageInfo groupMessageInfoWithSourceThreadID:sortedHandleIDs:handleIDsAreComplete:roomName:groupID:] : 200 -> 224
~ -[WLStatistics description] : 432 -> 396
~ -[WLStatistics fetchLogString] : 356 -> 328
~ -[WLStatistics setImportStartDate:] : 64 -> 12
~ -[WLStatistics setImportEndDate:] : 64 -> 12
~ -[NSString(WLSQLController) wl_sqlIDComponentsSeparatedByString:] : 368 -> 364
~ -[WLNETRBClient _didStartDHCPWithSuccess:] : 648 -> 640
~ +[WLWiFiController sharedInstance] : 84 -> 68
~ -[WLWiFiController _initWithWiFiManager:netrbClient:] : 172 -> 180
~ -[WLWiFiController _newRequestID] : 72 -> 68
~ -[WLWiFiController enableSoftAPWithSSID:password:channel:completion:] : 508 -> 520
~ ___69-[WLWiFiController enableSoftAPWithSSID:password:channel:completion:]_block_invoke : 268 -> 264
~ ___70-[WLWiFiController _enableSoftAPWithSSID:password:channel:completion:]_block_invoke : 268 -> 272
~ -[WLWiFiController disableSoftAPWithCompletion:] : 208 -> 212
~ ___48-[WLWiFiController disableSoftAPWithCompletion:]_block_invoke : 212 -> 204
~ ___49-[WLWiFiController _disableSoftAPWithCompletion:]_block_invoke_2 : 148 -> 140
~ -[WLWiFiController _ensureStartedNetworkReflectsPreferences] : 288 -> 276
~ -[WLWiFiController _startedNetwork] : 236 -> 240
~ ___35-[WLWiFiController _startedNetwork]_block_invoke : 124 -> 112
~ -[WLWiFiController _startWiFiWithSSID:password:channel:completion:] : 344 -> 348
~ ___67-[WLWiFiController _startWiFiWithSSID:password:channel:completion:]_block_invoke : 352 -> 332
~ -[WLWiFiController _networkRecordFromSSID:password:channel:] : 476 -> 460
~ ___44-[WLWiFiController _stopWiFiWithCompletion:]_block_invoke : 208 -> 204
~ -[WLWiFiDeviceClient hostedNetworkMatchingSSID:] : 356 -> 348
~ -[WLWiFiDeviceClient startNetworkWithHostRole:request:completion:] : 356 -> 352
~ __startSessionToCompletionMap : 84 -> 68
~ -[WLWiFiDeviceClient _startNetworkWithRole:request:session:] : 116 -> 120
~ __WLWiFiDeviceClient_startNetworkCallback : 212 -> 204
~ -[WLWiFiDeviceClient stopNetwork:completion:] : 340 -> 336
~ __stopSessionToCompletionMap : 84 -> 68
~ -[WLWiFiDeviceClient _stopNetwork:session:] : 128 -> 132
~ __WLWiFiDeviceClient_stopNetworkCallbackRaw : 152 -> 148
~ __WLWiFiDeviceClient_stopNetworkCallback : 212 -> 196
~ -[WLWiFiDeviceClient _completionMapsAreEmpty] : 188 -> 172
~ -[WLWiFiManager scanNetwork:] : 604 -> 608
~ __WiFiDeviceClientScanAsyncCallback : 400 -> 384
~ -[WLWiFiManager currentNetwork:channels:completion:] : 420 -> 436
~ -[WLWiFiManager _preferredChannel:network:channels:completion:] : 1988 -> 1968
~ -[NSError(WelcomeKit) wl_encodableError] : 228 -> 212
~ +[NSError(WelcomeKit) wl_encodableErrorSupportedClasses] : 84 -> 68
~ ___56+[NSError(WelcomeKit) wl_encodableErrorSupportedClasses]_block_invoke : 280 -> 276
~ +[NSError(WelcomeKit) _wl_encodableObjectFromObject:] : 312 -> 292
~ ___61+[NSError(WelcomeKit) _wl_encodableDictionaryFromDictionary:]_block_invoke : 168 -> 164
~ +[NSError(WelcomeKit) _wl_objectIsKindOfNonCollectionPlistClass:] : 296 -> 300
~ ___65+[NSError(WelcomeKit) _wl_objectIsKindOfNonCollectionPlistClass:]_block_invoke : 196 -> 192
CStrings:
- "#16@0:8"
- "*36@0:8i16Q20^q28"
- ".cxx_destruct"
- "@\"<NSObject>\""
- "@\"<WLDataMigrationDelegate>\""
- "@\"<WLDeviceDiscoverySocketHandlerDelegate>\""
- "@\"<WLMigrationDataSource>\""
- "@\"<WLServerConnectionDelegate>\""
- "@\"ACAccountStore\""
- "@\"CNContactStore\""
- "@\"EKEventStore\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSData\"40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\"16@0:8"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSOperationQueue\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURLSession\""
- "@\"WLAuthenticationCredentials\""
- "@\"WLAutomation\""
- "@\"WLDeviceAuthentication\""
- "@\"WLFeaturePayload\""
- "@\"WLMessageParty\""
- "@\"WLMessageSMILContext\""
- "@\"WLMigrationDataCoordinator\""
- "@\"WLNETRBClient\""
- "@\"WLPayload\""
- "@\"WLPhotoLibrary\""
- "@\"WLSQLController\""
- "@\"WLSocketHandler\""
- "@\"WLSourceDevice\""
- "@\"WLSourceDeviceAccount\""
- "@\"WLSourceDeviceMigrationMetadata\""
- "@\"WLSourceDeviceRecordSummary\""
- "@\"WLStatistics\""
- "@\"WLTimeEstimateAccuracyTracker\""
- "@\"WLURLSessionController\""
- "@\"WLWiFiManager\""
- "@\"WLWiFiNetwork\""
- "@\"WebBookmarkCollection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{__WiFiDeviceClient=}16"
- "@24@0:8^{__WiFiNetwork=}16"
- "@24@0:8^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16"
- "@28@0:8@16B24"
- "@28@0:8^{sqlite3_stmt=}16i24"
- "@28@0:8i16@?20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@32@0:8{_NSRange=QQ}16"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24@28"
- "@36@0:8@16B24^B28"
- "@36@0:8@16S24@28"
- "@36@0:8i16@20@28"
- "@36@0:8i16^{dispatch_source_type_s=}20@?28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32^{_NSRange=QQ}40"
- "@48@0:8Q16Q24@?32@?40"
- "@52@0:8@16@24B32@36@44"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8q16q24"
- "B32@0:8r*16q24"
- "B36@0:8@16@24B32"
- "B36@0:8B16d20d28"
- "B36@0:8q16q24B32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24@?32"
- "B40@0:8@16@24^@32"
- "B40@0:8@16Q24^@32"
- "B40@0:8q16q24q32"
- "B44@0:8@16@24B32^@36"
- "Hex"
- "Integer"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "NSURLSessionDelegate"
- "NSXMLParserDelegate"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8Q16"
- "Q32@0:8@16@24"
- "Q32@0:8Q16@24"
- "Q32@0:8Q16Q24"
- "Q40@0:8@16@24@32"
- "Q40@0:8@16@24q32"
- "S"
- "S16@0:8"
- "String"
- "T#,R"
- "T@\"<NSObject>\",&,N,V_associatedObject"
- "T@\"<WLDataMigrationDelegate>\",&,N,V_delegate"
- "T@\"<WLDeviceDiscoverySocketHandlerDelegate>\",W,N,V_delegate"
- "T@\"<WLMigrationDataSource>\",&,N,V_dataSource"
- "T@\"<WLServerConnectionDelegate>\",W,N,V_delegate"
- "T@\"ACAccountStore\",&,N,V_accountStore"
- "T@\"CNContactStore\",&,N,V_contactStore"
- "T@\"NSArray\",&,N,V_importErrors"
- "T@\"NSArray\",&,N,V_recipients"
- "T@\"NSArray\",&,N,V_samples"
- "T@\"NSArray\",&,N,V_thresholds"
- "T@\"NSArray\",R,N,V_attachments"
- "T@\"NSArray\",R,N,V_parts"
- "T@\"NSArray\",R,N,V_sortedHandleIDs"
- "T@\"NSData\",R,N,V_data"
- "T@\"NSData\",R,N,V_hashOfProofOfMatch_HAMK"
- "T@\"NSData\",R,N,V_mimeData"
- "T@\"NSData\",R,N,V_salt_s"
- "T@\"NSData\",R,N,V_serverPublicKey_B"
- "T@\"NSData\",R,N,V_sharedKey_K"
- "T@\"NSDate\",&,N,V_communicationDate"
- "T@\"NSDate\",&,N,V_endDate"
- "T@\"NSDate\",&,N,V_importEndDate"
- "T@\"NSDate\",&,N,V_importStartDate"
- "T@\"NSDate\",&,N,V_lastProgressSentDate"
- "T@\"NSDate\",&,N,V_startDate"
- "T@\"NSDate\",&,N,V_throughputSegmentStartDate"
- "T@\"NSDate\",C,N,V_modifiedDate"
- "T@\"NSDate\",R,N,V_date"
- "T@\"NSDictionary\",C,N,V_metadata"
- "T@\"NSDictionary\",R,N,V_attributes"
- "T@\"NSMutableArray\",&,N,V_migrators"
- "T@\"NSMutableArray\",&,N,V_throughputSamples"
- "T@\"NSNumber\",&,N,V_appStoreIdentifier"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",&,N,V_deviceModel"
- "T@\"NSString\",&,N,V_deviceOSVersion"
- "T@\"NSString\",&,N,V_deviceType"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_bucket"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_clientVersion"
- "T@\"NSString\",C,N,V_command"
- "T@\"NSString\",C,N,V_dataFilePath"
- "T@\"NSString\",C,N,V_databasePath"
- "T@\"NSString\",C,N,V_downloadsPath"
- "T@\"NSString\",C,N,V_host"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_identifiers"
- "T@\"NSString\",C,N,V_relativePath"
- "T@\"NSString\",C,N,V_rootPath"
- "T@\"NSString\",C,N,V_ssid"
- "T@\"NSString\",N,V_guid"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_address"
- "T@\"NSString\",R,N,V_ccAcNumber"
- "T@\"NSString\",R,N,V_characters"
- "T@\"NSString\",R,N,V_contentType"
- "T@\"NSString\",R,N,V_dateString"
- "T@\"NSString\",R,N,V_elementName"
- "T@\"NSString\",R,N,V_fileName"
- "T@\"NSString\",R,N,V_groupID"
- "T@\"NSString\",R,N,V_icc"
- "T@\"NSString\",R,N,V_messageText"
- "T@\"NSString\",R,N,V_mimeType"
- "T@\"NSString\",R,N,V_np"
- "T@\"NSString\",R,N,V_roomName"
- "T@\"NSString\",R,N,V_sourceThreadID"
- "T@\"NSString\",R,N,V_subject"
- "T@\"NSString\",R,N,V_threadID"
- "T@\"NSString\",R,N,V_uti"
- "T@\"NSURLSession\",&,N,V_session"
- "T@\"NSURLSession\",R,N,V_urlSession"
- "T@\"WLFeaturePayload\",W,N,V_featurePayload"
- "T@\"WLMessageParty\",&,N,V_sender"
- "T@\"WLMigrationDataCoordinator\",&,N,V_dataCoordinator"
- "T@\"WLPayload\",&,N,V_payload"
- "T@\"WLSQLController\",&,N,V_sqlController"
- "T@\"WLSocketHandler\",W,N,V_activeSocketHandler"
- "T@\"WLSourceDevice\",&,N,V_device"
- "T@\"WLSourceDevice\",&,N,V_sourceDevice"
- "T@\"WLSourceDevice\",R,N"
- "T@\"WLSourceDeviceAccount\",&,N,V_account"
- "T@\"WLSourceDeviceMigrationMetadata\",&,N,V_metadata"
- "T@\"WLStatistics\",&,N,V_aggregateStatistics"
- "T@\"WLTimeEstimateAccuracyTracker\",&,N,V_timeEstimateAccuracyTracker"
- "T@\"WLURLSessionController\",&,N,V_urlSessionController"
- "T@?,R,N,V_completion"
- "T@?,R,N,V_segmentCompletion"
- "TB,N,V_didDownload"
- "TB,N,V_isFree"
- "TB,N,V_isGroupMessage"
- "TB,N,V_selectedForMigration"
- "TB,N,V_stashDataLocally"
- "TB,N,V_storeDataAsFile"
- "TB,R,N"
- "TB,R,N,V_handleIDsAreComplete"
- "TB,R,N,V_isPhoneNumber"
- "TQ,N,V_attemptCount"
- "TQ,N,V_bytes"
- "TQ,N,V_completedDownloadSegmentCount"
- "TQ,N,V_contentType"
- "TQ,N,V_crashCount"
- "TQ,N,V_downloadByteCount"
- "TQ,N,V_downloadDuration"
- "TQ,N,V_downloadSegmentCount"
- "TQ,N,V_errorCount"
- "TQ,N,V_estimate"
- "TQ,N,V_expectedBytes"
- "TQ,N,V_expectedDownloadBytesRemainingForItemsWithConcreteSizes"
- "TQ,N,V_expectedDownloadSegmentsRemaining"
- "TQ,N,V_expectedDownloadSegmentsRemainingForItemsWithEstimatedSizes"
- "TQ,N,V_importEndBytesFree"
- "TQ,N,V_importFailedRecordCount"
- "TQ,N,V_importRecordCount"
- "TQ,N,V_importStartBytesFree"
- "TQ,N,V_itemSize"
- "TQ,N,V_messageDirection"
- "TQ,N,V_sqlID"
- "TQ,N,V_state"
- "TQ,N,V_threshold"
- "TQ,N,V_throughputBytesInCurrentPeriod"
- "TQ,N,V_throughputSegmentsInCurrentPeriod"
- "TQ,N,V_type"
- "TQ,N,V_version"
- "TQ,R"
- "TQ,R,N,V_messageType"
- "TS,N,V_port"
- "T^q,N,V_rowID"
- "T^v,N,V_powerAssertion"
- "T^{__SecCertificate=},N,V_localCertificate"
- "T^{__SecCertificate=},N,V_remoteCertificate"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_privateKey"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_publicKey"
- "T^{__WiFiDeviceClient=},N,V_ref"
- "T^{__WiFiManagerClient=},N,V_ref"
- "T^{__WiFiNetwork=},N,V_ref"
- "Td,N,V_duration"
- "Td,N,V_lastProgressSentToAndroidDevice"
- "Td,N,V_progress"
- "Ti,R,N,V_sockfd"
- "Tq,N,V_channel"
- "URL"
- "URLByAppendingPathComponent:"
- "URLByDeletingLastPathComponent"
- "URLPathAllowedCharacterSet"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "WLAccessibility"
- "WLAccessibilityMigrator"
- "WLAnalyticsDataSource"
- "WLApp"
- "WLAppMigrator"
- "WLAppSearchRequest"
- "WLAuthenticationCredentials"
- "WLAuthenticationUtilities"
- "WLAutomation"
- "WLBookmarksMigrator"
- "WLCalendarMigrator"
- "WLConnection"
- "WLContactsMigrator"
- "WLCredentialStore"
- "WLDataMigratorProtocol"
- "WLDataclassMigrating"
- "WLDevice"
- "WLDeviceDiscoveryController"
- "WLDeviceDiscoverySocketHandler"
- "WLDeviceDiscoverySocketHandlerDelegate"
- "WLDisplayMigrator"
- "WLFileProvider"
- "WLFilesMigrator"
- "WLGroupMessageInfo"
- "WLItemSizeConfirmationCompletionAdapter"
- "WLLocalDataSource"
- "WLMailAccountMigrator"
- "WLMessage"
- "WLMessageAttachment"
- "WLMessageParty"
- "WLMessageSMILContext"
- "WLMessageSMILPart"
- "WLMessagesMigrator"
- "WLMigrationContext"
- "WLMigrationDataCoordinator"
- "WLMigrationDataSource"
- "WLMigrator"
- "WLNETRBClient"
- "WLPhotoLibrary"
- "WLPhotosMigrator"
- "WLRemoteDeviceDataSource"
- "WLSQLController"
- "WLSRPServer"
- "WLServerConnection"
- "WLSocketCommandMessage"
- "WLSocketHandler"
- "WLSocketMessage"
- "WLSocketVersionMessage"
- "WLSourceDeviceAccount"
- "WLSourceDeviceHandshakeParser"
- "WLSourceDeviceMigrationMetadata"
- "WLSourceDeviceRecordSummary"
- "WLStatistics"
- "WLThroughputSample"
- "WLTimeEstimateAccuracyTracker"
- "WLTimeEstimateSample"
- "WLURLSessionController"
- "WLVideosMigrator"
- "WLWiFiController"
- "WLWiFiDeviceClient"
- "WLWiFiManager"
- "WLWiFiNetwork"
- "WLXMLSerialization"
- "WelcomeKit"
- "XMLObjectWithData:"
- "XMLObjectWithString:"
- "^q"
- "^q16@0:8"
- "^v"
- "^v16@0:8"
- "^{NETRBClient=}"
- "^{NETRBClient=}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__SecCertificate=}"
- "^{__SecCertificate=}16@0:8"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8"
- "^{__WiFiDeviceClient=}"
- "^{__WiFiDeviceClient=}16@0:8"
- "^{__WiFiManagerClient=}"
- "^{__WiFiManagerClient=}16@0:8"
- "^{__WiFiNetwork=}"
- "^{__WiFiNetwork=}16@0:8"
- "^{sqlite3=}"
- "^{srp_st=ii^{cstr_st}^v^v^{cstr_st}^v^v^v^v^v^v^{cstr_st}^{srp_meth_st}^v^v^v^?^{srp_server_lu_st}}"
- "_accept:"
- "_account"
- "_accountGuid"
- "_accountStore"
- "_accountTypes"
- "_activeSocketHandler"
- "_address"
- "_aggregateStatistics"
- "_allowConnectionsFromAnyAddress"
- "_allowSegmentedDownloads"
- "_allowedAddress"
- "_appStoreIdentifier"
- "_appendBase64Data:toString:"
- "_associatedObject"
- "_attachmentDateWithMessage:"
- "_attachmentPersistentPathForGuid:fileName:mimeType:uti:"
- "_attachments"
- "_attemptCount"
- "_attributes"
- "_auth"
- "_authentication"
- "_automation"
- "_beginTransaction"
- "_bookmarkFolderAtTitlePath:withinBookmarkFolder:"
- "_bookmarkFolderAtTitlePath:withinRootFolder:"
- "_bucket"
- "_bundleIdentifier"
- "_bytes"
- "_bytesFreeOnDevice"
- "_ccAcNumber"
- "_channel"
- "_characters"
- "_chatAccountIDWithMessage:"
- "_chatAccountLoginWithMessage:"
- "_chatDisplayNameWithMessage:"
- "_chatGUIDWithGroupRoomName:"
- "_chatGUIDWithNonGroupMessage:"
- "_chatGroupIDWithNonGroupMessage:"
- "_chatIDForHandleIDs:groupRoomName:groupID:message:"
- "_chatIdentifierWithNonGroupMessage:"
- "_chatLastAddressedHandleWithMessage:"
- "_chatPropertiesDataWithMessage:"
- "_chatServiceWithMessage:"
- "_chatStateWithMessage:"
- "_chatStyleWithMessage:"
- "_cleanUpAfterFinalizeMigratableAppsWithSQLController:completion:"
- "_clientVersion"
- "_closeDatabase"
- "_collection"
- "_command"
- "_commandStringWithData:"
- "_commitTransaction"
- "_communicationDate"
- "_completedDownloadSegmentCount"
- "_completion"
- "_completionMapsAreEmpty"
- "_completionsAreNil"
- "_connections"
- "_contactStore"
- "_contentType"
- "_countOfPairingAttemptsWithCurrentSecret"
- "_crashCount"
- "_createBookmarkFolderWithTitle:UUID:"
- "_createRootBookmarkFolder"
- "_credentials"
- "_data"
- "_dataCache"
- "_dataCacheReadSource"
- "_dataCacheSema"
- "_dataCoordinator"
- "_dataFilePath"
- "_dataSource"
- "_dataTypesAndSizesXMLDataFromMap:"
- "_database"
- "_databaseFilename"
- "_databasePath"
- "_databaseQueue"
- "_date"
- "_dateFormatterForMimeDateStrings"
- "_dateString"
- "_delegate"
- "_delegateOperationQueue"
- "_deleteAccounts"
- "_deleteDownloadsPath:"
- "_deleteSummaries"
- "_device"
- "_deviceModel"
- "_deviceOSVersion"
- "_deviceType"
- "_dhcpStartCompletionBlock"
- "_dhcpStopCompletionBlock"
- "_didConsultPreferencesForStartedNetwork"
- "_didDownload"
- "_didFinishDownloadingSegmentOfSize:expectedSize:migratorEstimatesItemSizes:endDate:context:"
- "_didReceiveHandshakeData:"
- "_didStartDHCPWithSuccess:"
- "_didStopDHCPWithSuccess:"
- "_disableSoftAPWithCompletion:"
- "_doneSent"
- "_downloadByteCount"
- "_downloadDataWithContext:failureDetailsBlock:"
- "_downloadDuration"
- "_downloadFileInMultipleSegmentsFromSource:forMigrator:summary:account:itemSize:segmentCompletion:completion:"
- "_downloadSegmentCount"
- "_downloadSegmentsFromSource:forMigrator:startingAtByteLocation:ofSummary:account:itemSize:toFileHandle:segmentCompletion:completion:"
- "_downloadTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:"
- "_downloadsPath"
- "_duration"
- "_elementName"
- "_enableSoftAPWithSSID:password:channel:completion:"
- "_enableSoftAPWithSSID:password:channels:secret:srp:completion:enabled:error:channel:currentChannel:"
- "_endDate"
- "_ensureCorrectSchema"
- "_ensureStartedNetworkReflectsPreferences"
- "_errorCount"
- "_estimate"
- "_eventStore"
- "_existingAccounts"
- "_expectedBytes"
- "_expectedDownloadBytesRemainingForItemsWithConcreteSizes"
- "_expectedDownloadSegmentsRemaining"
- "_expectedDownloadSegmentsRemainingForItemsWithEstimatedSizes"
- "_featurePayload"
- "_fetchAccountsAndSummariesWithContext:"
- "_fetchAccountsFromSource:forMigrator:statistics:completion:"
- "_fetchSummariesFromSource:forMigrator:account:statistics:completion:"
- "_fileName"
- "_fileNameForPart:smilContext:"
- "_finishMigrationWithError:context:disconnected:completion:"
- "_foundHandleIDs:representSameGroupMessageAsHandleIDs:handleIDsAreComplete:"
- "_generatePairingSecret"
- "_groupID"
- "_guessIccForNumber:"
- "_guid"
- "_handleIDFromNonGroupMessageHandleIDs:"
- "_handleIDsAreComplete"
- "_handleIDsForMessage:"
- "_handshakeCommandData"
- "_handshakeResponseData"
- "_hasTestAutomationCaches"
- "_hashOfProofOfMatch_HAMK"
- "_host"
- "_hostedNetworks"
- "_icc"
- "_identifier"
- "_identifiers"
- "_importDataRecord:summary:"
- "_importDataWithContext:failureDetailsBlock:"
- "_importEndBytesFree"
- "_importEndDate"
- "_importErrorCount"
- "_importErrors"
- "_importFailedRecordCount"
- "_importRecordCount"
- "_importStartBytesFree"
- "_importStartDate"
- "_inBody"
- "_inPar"
- "_incomingConnSource"
- "_incrementProgressBy:context:"
- "_indexOfThresholdGreaterThanOrEqualToEstimate:"
- "_initWithAddress:addCountryCode:sqlController:"
- "_initWithData:fileName:mimeType:uti:"
- "_initWithWiFiManager:netrbClient:"
- "_initWithoutWiFiDeviceClientRef"
- "_insertChatHandleJoinRowWithChatID:handleID:duplicateMightExist:"
- "_insertChatMessageJoinRowWithChatID:messageID:date:"
- "_insertMatchingApps:"
- "_insertMessage:"
- "_insertMessageAttachmentJoinRowWithMessageID:attachmentID:"
- "_insertMessageRowWithMessage:handleIDs:groupRoomName:"
- "_insertRowWithAttachment:filePath:forMessage:"
- "_insertStatistics_onDatabaseQueue:"
- "_isFree"
- "_isGroupMessage"
- "_isPhoneNumber"
- "_isTerminated:length:"
- "_itemSize"
- "_lastProgressSentDate"
- "_lastProgressSentToAndroidDevice"
- "_lastRequestID"
- "_listen:"
- "_listenerSocket"
- "_localCertificate"
- "_localSourceDataPath"
- "_logStatisticsAndSendStatisticsTelemetryWithContext:"
- "_lookupStoreItemsMatchingExternalIDs:attempt:completion:"
- "_maximumRetryableTaskDurationForLongServerOperations"
- "_messageAccountGUIDWithMessage:"
- "_messageAccountWithMessage:"
- "_messageAttributedBodyDataWithMessage:"
- "_messageDateDeliveredWithMessage:"
- "_messageDateReadWithMessage:"
- "_messageDateWithMessage:"
- "_messageDirection"
- "_messageErrorWithMessage:"
- "_messageGroupTitleWithMessage:"
- "_messageIsFromMeWithMessage:"
- "_messageServiceCenterWithMessage:"
- "_messageServiceWithMessage:"
- "_messageSubjectWithMessage:"
- "_messageText"
- "_messageType"
- "_messageVersionWithMessage:"
- "_metadata"
- "_migratableAppsForDevice:"
- "_migrators"
- "_mimeData"
- "_mimeParts"
- "_mimeType"
- "_modifiedDate"
- "_netrbClient"
- "_netrbClientRef"
- "_networkRecordFromSSID:password:channel:"
- "_newNumberOfRetriesAllowed:startDate:"
- "_newRequestID"
- "_nextIncomingConnectionHandler"
- "_normalize:"
- "_np"
- "_numberFormatter"
- "_okResponseData"
- "_onDatabaseQueue_updateMigrationState:forSummary:removeData:"
- "_openDatabase"
- "_otherPartyAddressWithNonGroupMessage:"
- "_ourAddressWithMessage:"
- "_parseConnectionFailureReasons:"
- "_parseDataTypesXMLData:completion:"
- "_parseDeviceInfoNode:modifyingSourceDevice:"
- "_parts"
- "_payload"
- "_performDownloadRequest:expectedContentLength:numberOfRetriesAllowed:startDate:fileAccessor:completion:"
- "_performQuery:rowHandler:"
- "_performRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:"
- "_performSRPAuthenticationAndHandshake"
- "_performSimpleQuery:"
- "_photoLibrary"
- "_populateMimeHeaders:recipients:fromRange:ofString:addCountryCodeToParties:sqlController:"
- "_port"
- "_postSourceDevicesDidChangeNotification"
- "_powerAssertion"
- "_preferredChannel:network:channels:completion:"
- "_prepareMetadata:usingRetryPolicies:allowContinuationFromAnotherDevice:"
- "_presentPromptForMigrableApps:"
- "_privateKey"
- "_progress"
- "_progressIncrementForImportedSummary:summaries:accounts:migrators:"
- "_publicKey"
- "_queue"
- "_queue_startDiscoveryWithPreGeneratedCode:completion:"
- "_queue_stopDeviceDiscoveryWithCompletion:"
- "_queue_stopWiFiAndDeviceDiscoveryWithCompletion:"
- "_read:"
- "_readIntoCacheFromSocket:"
- "_readQueue"
- "_readSource"
- "_recipients"
- "_recordSummaryForMigrator:withInfo:account:"
- "_ref"
- "_relativePath"
- "_relativePathForAccount:migrator:"
- "_relativePathForSummary:migrator:"
- "_remoteCertificate"
- "_reportTimeEstimatesWithContext:"
- "_requestQueue"
- "_requestSerialQueue"
- "_retryLaterDelayInSeconds"
- "_rollbackTransaction"
- "_roomName"
- "_rootPath"
- "_rowID"
- "_runTaskWithRequest:expectedContentLength:numberOfRetriesAllowed:preventRetriesAfterTaskExceedsDuration:taskDurationLimit:startDate:completionHandler:"
- "_salt_s"
- "_samples"
- "_schemaVersion"
- "_segmentCompletion"
- "_selectDataTypesWithContext:"
- "_selectFromDataTypeToSizeMap:device:completion:"
- "_selectedForMigration"
- "_sendStoreDownloadRequestForFreeMigratableApps:completion:"
- "_sender"
- "_senderHandleIDFromReceivedGroupMessageHandleIDs:"
- "_serverPublicKey_B"
- "_serviceStringWithMessage:"
- "_session"
- "_setProgressTo:context:"
- "_sharedKey_K"
- "_shouldContinueMigrationFromAnotherDevice"
- "_shouldForceDiscoveryError"
- "_shouldForceDownloadError"
- "_shouldHandleHTTPErrorWithResponse:expectedContentLength:error:"
- "_shouldIgnoreMessageThreadID"
- "_shouldRetryLaterWithResponse:error:"
- "_shouldRetryWithData:response:error:"
- "_shouldRetryWithPreventRetriesAfterTaskExceedsDuration:taskDurationLimit:taskDuration:"
- "_shouldTerminateMigrationBeforeImport"
- "_shouldTerminateMigrationOnError"
- "_smilContext"
- "_socketHandlers"
- "_sockfd"
- "_sortedHandleIDs"
- "_sortedHandleIDs:"
- "_sourceDevice"
- "_sourceDevices"
- "_sourceThreadID"
- "_sqlController"
- "_sqlID"
- "_sqlite3_bind_NSDate:forStatement:position:"
- "_sqlite3_column_NSDateForStatement:column:"
- "_srpPassword"
- "_ssItemForiTunesStoreIdentifier:"
- "_ssid"
- "_ssidWithSecret:"
- "_startDHCPWithInterface:"
- "_startDate"
- "_startNetworkWithRole:request:session:"
- "_startWiFiWithSSID:password:channel:completion:"
- "_startedNetwork"
- "_starting"
- "_stashDataLocally"
- "_state"
- "_statisticsWithContentType:"
- "_stopDHCP"
- "_stopNetwork:session:"
- "_stopWiFiWithCompletion:"
- "_storeDataAsFile"
- "_subject"
- "_summary"
- "_systemVersion"
- "_taskDurationSinceStartDate:"
- "_threadID"
- "_threshold"
- "_thresholdAtIndex:"
- "_thresholdBelowLastSample"
- "_thresholds"
- "_throughputBytesInCurrentPeriod"
- "_throughputSamples"
- "_throughputSegmentStartDate"
- "_throughputSegmentsInCurrentPeriod"
- "_timeEstimateAccuracyTracker"
- "_totalSummarySegmentCountForAccounts:migrationStateComparisonOperator:migrationState:"
- "_type"
- "_uncanonicalizedIDWithMessage:"
- "_uniqueHandleStringsWithMessage:"
- "_updateClient"
- "_updateSourceWithProgress:remainingTime:context:completion:"
- "_urlForAccountsWithMigrator:"
- "_urlForRecordForMigrator:withSummaryIdentifier:accountIdentifier:segmentByteRange:"
- "_urlForRecordSummariesForMigrator:withAccountIdentifier:"
- "_urlRequestTimeout"
- "_urlScheme"
- "_urlSession"
- "_urlSessionController"
- "_uti"
- "_vcardDataWithoutCustomFieldsFromVcardData:"
- "_version"
- "_wifiManager"
- "_willRetryPerformRequest"
- "_wl_encodableArrayFromArray:"
- "_wl_encodableDictionaryFromDictionary:"
- "_wl_encodableObjectFromObject:"
- "_wl_encodableSetFromSet:"
- "_wl_objectIsKindOfNonCollectionPlistClass:"
- "_writeBytes:offset:length:toSocket:completion:"
- "_writeQueue"
- "absoluteString"
- "acceptIncomingConnectionWithListenerSocket:nonBlocking:"
- "accessibilityFontScale"
- "accessibilitySettings"
- "account"
- "accountBased"
- "accountInfoArrayContainsNonSyncableAccount:"
- "accountInfoRepresentsSyncableAccount:"
- "accountStore"
- "accountTypeWithAccountTypeIdentifier:"
- "accountWithInfo:"
- "accountsDataForMigrator:completion:"
- "accountsForMigrator:device:"
- "accountsWithAccountType:"
- "activeSocketHandler"
- "addAsset:collection:"
- "addAsset:filename:size:collection:completion:"
- "addAssets:"
- "addContact:toContainerWithIdentifier:"
- "addFinishBlock:"
- "addObject:"
- "addObjectsFromArray:"
- "addOperation:"
- "addRecipients:toMimeHeaders:"
- "addToFetchByteCount:"
- "addWorkingTime:"
- "address"
- "aggregateContentType"
- "aggregateStatistics"
- "allKeys"
- "alphanumericCharacterSet"
- "apiLevel"
- "appStoreIdentifier"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "archivedDataWithRootObject:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayByAddingObject:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assetCollectionChangeRequest:"
- "associatedObject"
- "attachments"
- "attemptCount"
- "attemptDirectConnectionToAddress:"
- "authenticationMethod"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "beginReadingIntoCacheFromSocket:"
- "blockOperationWithBlock:"
- "boolForKey:"
- "boolValue"
- "bytes"
- "calendars"
- "canAddAccessibility"
- "canAddDisplay"
- "canAddFiles"
- "cancel"
- "cancelAllOperations"
- "ccAcNumber"
- "changeRequestForAssetCollection:"
- "channel"
- "characterAtIndex:"
- "characters"
- "class"
- "cleanup"
- "clientVersion"
- "close"
- "close:"
- "closeDatabase"
- "closeFile"
- "communicationDate"
- "compare:"
- "completedDownloadSegmentCount"
- "completion"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "confirmItemSizeWithSourceBeforeDownloading"
- "conformsToProtocol:"
- "connectToHost:address:port:"
- "connection:didReceiveText:"
- "connectionDidEnd"
- "contactStore"
- "contactsWithData:error:"
- "containerURLForSecurityApplicationGroupIdentifier:"
- "containsObject:"
- "contentTransferEncoding"
- "contentType"
- "contentTypeDidComplete:downloadByteCount:importRecordCount:importFailedRecordCount:downloadDuration:importDuration:android:model:version:"
- "copy"
- "copy:filename:error:"
- "copyItemAtURL:toURL:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "crashCount"
- "createBagForSubProfile"
- "createDeviceClient"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createFileAtPath:contents:attributes:"
- "createListenerSocketOnPort:"
- "creationRequestForAssetCollectionWithTitle:"
- "creationRequestForAssetFromImageAtFileURL:"
- "creationRequestForAssetFromVideoAtFileURL:"
- "credentialForTrust:"
- "credentialWithIdentity:certificates:persistence:"
- "credentialsForAuthentication:"
- "currentAuthentication"
- "currentLocale"
- "currentNetwork:channels:completion:"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "d48@0:8@16@24@32@40"
- "d52@0:8Q16Q24B32@36@44"
- "data"
- "dataCoordinator"
- "dataFilePath"
- "dataForSummary:"
- "dataForSummary:migrator:completion:"
- "dataFromPEMFormattedData:"
- "dataMigrator:didFailWithError:"
- "dataMigrator:didUpdateMigrationState:"
- "dataMigrator:didUpdateProgressPercentage:"
- "dataMigrator:didUpdateRemainingDownloadTime:"
- "dataMigratorDidBecomeRestartable:"
- "dataMigratorDidFinish:withImportErrors:context:"
- "dataSegmentForSummary:byteRange:migrator:completion:"
- "dataSource"
- "dataTaskWithRequest:completionHandler:"
- "dataType"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithCapacity:"
- "dataWithContentsOfURL:options:error:"
- "dataWithJSONObject:options:error:"
- "databasePath"
- "date"
- "dateByAddingTimeInterval:"
- "dateFromMimeHeaders:"
- "dateFromString:"
- "dateString"
- "dateWithTimeIntervalSince1970:"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "defaultCalendarForNewEvents"
- "defaultHFSFileManager"
- "defaultManager"
- "defaultSessionConfiguration"
- "defaultStore"
- "delegate"
- "deleteAccountsAndSummariesForAllDevices"
- "deleteAccountsAndSummariesForMigrator:device:"
- "deleteData"
- "deleteFromTable:"
- "deleteGroupMessageInfoForAllDevices"
- "deleteLocalData"
- "deleteMessagePhoneNumbersForAllDevices"
- "deleteMessages"
- "deleteMetadataForAllDevices"
- "deleteMigratableAppsForAllDevices"
- "deleteStatisticsForAllDevices"
- "deleteSuggestedAppBundleIDsForAllDevices"
- "deleteSummaryDataForAllDevices"
- "deleteTestAutomationCachesIfNeeded"
- "description"
- "device"
- "deviceDidFailWithAuthenticationError"
- "deviceDiscoverySocketHandler:didDiscoverCandidate:"
- "deviceDiscoverySocketHandler:didFailToHandshakeWithSourceDevice:error:"
- "deviceDiscoverySocketHandler:didFinishHandshakeWithSourceDevice:"
- "deviceModel"
- "deviceName"
- "deviceOSVersion"
- "deviceType"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "didCalculateTimeEstimate:atDate:associatedObject:"
- "didDownload"
- "didLookupAppsWithMatchedApps:mismatchedApps:"
- "didReceiveClientPublicKey_A:proofOfMatch_M:"
- "didResolveTimeEstimate:forDownloadTask:threshold:actualTime:"
- "disable"
- "disableSoftAPWithCompletion:"
- "disassociate"
- "displaySettings"
- "disposition"
- "domain"
- "downloadByteCount"
- "downloadBytesPerSecond"
- "downloadData:"
- "downloadDataFromSource:forMigrator:summary:account:completion:"
- "downloadDuration"
- "downloadFileFromSource:forMigrator:summary:account:segmentCompletion:completion:"
- "downloadSegmentCount"
- "downloadSegmentSize"
- "downloadTaskWithRequest:completionHandler:"
- "downloadsPath"
- "duration"
- "elapsedTime"
- "elementName"
- "enable"
- "enableAccessibilityDisplayInversion"
- "enableDisplayDarkMode"
- "enableDisplayZoom"
- "enableSoftAPWithSSID:password:channel:completion:"
- "enableSoftAPWithSSID:password:channels:secret:srp:completion:"
- "endDate"
- "endReadingIntoCache"
- "enumerateByteRangesUsingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "error"
- "errorCount"
- "errorWithDomain:code:userInfo:"
- "estimate"
- "estimateItemSizeForSummary:account:"
- "estimatesDidResolveAtDate:block:"
- "executeSaveRequest:error:"
- "expectedBytes"
- "expectedDownloadBytesRemainingForItemsWithConcreteSizes"
- "expectedDownloadSegmentsRemaining"
- "expectedDownloadSegmentsRemainingForItemsWithEstimatedSizes"
- "failureResponse"
- "featurePayload"
- "fetchAccountsAndSummariesFromSource:forMigrator:statistics:accountsRequestDurationBlock:summariesRequestDurationBlock:completion:"
- "fetchAssetCollectionsWithType:subtype:options:"
- "fetchContentType"
- "fetchLogString"
- "fetchRootPath"
- "fetchSummary:"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileForSummary:migrator:fileAccessor:completion:"
- "fileHandleForWritingAtPath:"
- "fileName"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "finalizeMigratableAppsWithCompletion:"
- "finishMigration:"
- "firstObject"
- "floatValue"
- "generateAuthenticationCredentialsContainingSelfSignedCertificate"
- "generateSelfSignedCertificateWithOrganization:commonName:completion:"
- "generatedRoomNameForGroupChat"
- "getResourceValue:forKey:error:"
- "groupID"
- "groupMessageInfoMatchingSortedHandleIDs:handleIDsAreComplete:didMatchExactly:"
- "groupMessageInfoMatchingSourceThreadID:"
- "groupMessageInfoWithSourceThreadID:sortedHandleIDs:handleIDsAreComplete:roomName:groupID:"
- "guid"
- "handleIDsAreComplete"
- "hardwareBrand"
- "hardwareDesign"
- "hardwareMaker"
- "hardwareModel"
- "hardwareProduct"
- "hasPrefix:"
- "hasSoftAPCapability"
- "hasSuffix:"
- "hash"
- "hashOfProofOfMatch_HAMK"
- "hashWithString:"
- "hmacDataForData:"
- "host"
- "hostedNetworkMatchingSSID:"
- "httpPort"
- "i16@0:8"
- "i20@0:8i16"
- "i24@0:8Q16"
- "i24@0:8i16B20"
- "i32@0:8@16@24"
- "i36@0:8@16^{hostent=*^*ii^*}24S32"
- "i36@0:8@16^{sqlite3_stmt=}24i32"
- "i36@0:8i16@20@28"
- "icc"
- "identifier"
- "identifiers"
- "image"
- "importBytesUsed"
- "importData:"
- "importDataForMigrator:fromProvider:forSummaries:summaryStart:summaryCompletion:"
- "importDataFromProvider:forSummaries:summaryStart:summaryCompletion:"
- "importDidEnd"
- "importDidFailSilentlyForContentType:"
- "importDuration"
- "importEndBytesFree"
- "importEndDate"
- "importErrorCount"
- "importErrors"
- "importFailedRecordCount"
- "importICSData:intoCalendar:options:"
- "importLocalContent"
- "importRecordCount"
- "importRecordData:summary:account:completion:"
- "importStartBytesFree"
- "importStartDate"
- "importWillBegin"
- "incrementFetchFailedRequestCount"
- "incrementFetchRequestCount"
- "init"
- "initWithAccountType:"
- "initWithAndroidIdentifiers:"
- "initWithAuthentication:"
- "initWithBase64EncodedData:options:"
- "initWithBase64EncodedString:options:"
- "initWithBodyData:topLevelHeaders:headersToPreserve:"
- "initWithBundleIdentifier:appStoreIdentifier:isFree:"
- "initWithBytes:length:"
- "initWithBytes:length:encoding:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCString:encoding:"
- "initWithCapacity:"
- "initWithCommandString:"
- "initWithContentType:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDelegate:"
- "initWithDevice:sqlController:"
- "initWithDictionary:"
- "initWithElementName:attributes:"
- "initWithHost:port:session:"
- "initWithInfo:"
- "initWithInfo:account:"
- "initWithItem:"
- "initWithLocaleIdentifier:"
- "initWithObjects:"
- "initWithPurchases:"
- "initWithSQLController:"
- "initWithSocket:srpPassword:delegate:"
- "initWithString:"
- "initWithType:"
- "initWithType:clientIdentifier:clientVersion:bag:"
- "initWithUTF8String:"
- "initWithUnconfirmedItemSize:segmentSize:originalSegmentCompletion:originalCompletion:"
- "initWithUsername:password:"
- "initWithVersion:"
- "initWithWiFiDeviceClientRef:"
- "initWithWiFiNetworkRef:"
- "insertAccount:migrator:device:"
- "insertGroupMessageInfoWithSortedHandleIDs:handleIDsAreComplete:roomName:groupID:"
- "insertGroupMessageInfoWithSourceThreadID:roomName:groupID:"
- "insertMessagePhoneNumberWithIcc:ccAcNumber:"
- "insertMetadata:forSourceDevice:"
- "insertMigratableApp:forDevice:"
- "insertRecordSummary:account:"
- "installMigratableApps:completion:"
- "intValue"
- "integerValue"
- "invalidate"
- "invalidateAndCancel"
- "invalidateWithError:"
- "invertColorsEnabled"
- "ipAddress"
- "isEqual:"
- "isEqualToData:"
- "isEqualToString:"
- "isGroupMessage"
- "isHmacData:validForData:"
- "isIPAddressInRange:"
- "isInternal"
- "isKindOfClass:"
- "isLocal"
- "isMemberOfClass:"
- "isPhoneNumber"
- "isProxy"
- "isSelectingDataTypeInHandshake"
- "isSubsetOfSet:"
- "isTetheringSupported"
- "isValid"
- "isValidTableName:"
- "itemSizeForSummary:migrator:completion:"
- "keysSortedByValueUsingComparator:"
- "lastObject"
- "lastPathComponent"
- "lastProgressSentDate"
- "lastProgressSentToAndroidDevice"
- "length"
- "listen:"
- "listenForConnectionOnSocket:withConnectionHandler:"
- "listenerDidStart:srp:"
- "localCertificate"
- "localDataExists"
- "lockSync"
- "longLongValue"
- "lookupAndConnectToHost:port:completion:"
- "lowercaseString"
- "makeDirectoriesInPath:mode:"
- "mergeWithBookmarksDictionary:clearHidden:error:"
- "messageDirection"
- "messagePhoneNumberIccForCcAcNumber:"
- "messageText"
- "messageType"
- "messageWithData:error:"
- "metadata"
- "migratableAppsForAllDevices"
- "migrationErrors"
- "migrationMetadataForSourceDevice:strictMatch:"
- "migratorDidFinish:"
- "migrators"
- "migrators:"
- "mimeData"
- "mimeHeadersFromMimeData:sqlController:"
- "mimeType"
- "modifiedDate"
- "moveItemAtPath:toPath:error:"
- "mutableCopy"
- "nextObject"
- "now"
- "np"
- "numberFromString:"
- "numberWithBool:"
- "numberWithChar:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithShort:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeSocket:forSourceEventType:handler:"
- "osAPIVersion"
- "osVersion"
- "parse"
- "parseData:modifyingSourceDevice:completion:"
- "parseMIMEData:sqlController:"
- "parseXMLContent:"
- "parser:didEndElement:namespaceURI:qualifiedName:"
- "parser:didEndMappingPrefix:"
- "parser:didStartElement:namespaceURI:qualifiedName:attributes:"
- "parser:didStartMappingPrefix:toURI:"
- "parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:"
- "parser:foundCDATA:"
- "parser:foundCharacters:"
- "parser:foundComment:"
- "parser:foundElementDeclarationWithName:model:"
- "parser:foundExternalEntityDeclarationWithName:publicID:systemID:"
- "parser:foundIgnorableWhitespace:"
- "parser:foundInternalEntityDeclarationWithName:value:"
- "parser:foundNotationDeclarationWithName:publicID:systemID:"
- "parser:foundProcessingInstructionWithTarget:data:"
- "parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:"
- "parser:parseErrorOccurred:"
- "parser:resolveExternalEntityName:systemID:"
- "parser:validationErrorOccurred:"
- "parserDidEndDocument:"
- "parserDidStartDocument:"
- "parts"
- "path"
- "pathComponents"
- "pathExtension"
- "pathExtensionForMIMEType:"
- "pathExtensionForUTIType:"
- "payload"
- "pemFormattedCertificateData:"
- "perform"
- "performChanges:completionHandler:"
- "performDNSLookupForHost:completion:"
- "performPreImportPhaseForSummary:data:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentIdentifier"
- "persistentValueForDate:"
- "photoLibraryDidComplete:filename:success:error:"
- "photoLibraryDidFailWithExtension:"
- "placeholderForCreatedAsset"
- "potentiallyLargeRecordData"
- "powerAssertion"
- "predicateWithFormat:"
- "preferredChannel:"
- "preferredContentSizeCategoryName"
- "preparatoryDataDidComplete:contentType:duration:android:model:version:"
- "prepare:delegate:error:"
- "previousFailureCount"
- "privateKey"
- "progress"
- "progressiveMimeParser:beganDataForMimePart:"
- "progressiveMimeParser:beganMimePart:"
- "progressiveMimeParser:failedWithError:"
- "progressiveMimeParser:finishedMimePart:"
- "protectionSpace"
- "publicKey"
- "q16@0:8"
- "q24@0:8@16"
- "q32@0:8@16@?24"
- "q40@0:8@16@24@32"
- "q48@0:8@16@24@32@40"
- "queue"
- "range"
- "rangeOfString:"
- "rangeOfString:options:range:"
- "readBytesFromSocket:maximumSize:bytesRead:"
- "recipients"
- "recipientsFromMimeHeaders:"
- "ref"
- "release"
- "remoteCertificate"
- "removeAllObjects"
- "removeDataAndSetDidImportForSummary:"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeLastObject"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsInRange:"
- "replaceCharactersInRange:withString:"
- "requestWithURL:"
- "requestWithURL:cachePolicy:timeoutInterval:"
- "reset"
- "respondsToSelector:"
- "responseDataItems"
- "resume"
- "retain"
- "retainCount"
- "roomName"
- "rootPath"
- "rowID"
- "runPostMigrationTasks:"
- "safariBookmarkCollection"
- "salt_s"
- "samples"
- "saveVerifiedAccount:error:"
- "scanNetwork:"
- "search:"
- "segmentCompletion"
- "segmentCountForItemSize:segmentSize:"
- "selectDataTypes:"
- "selectedForMigration"
- "self"
- "sendCommand:toSocket:completion:"
- "sendData:completion:"
- "sendData:toSocket:completion:"
- "sender"
- "senderFromMimeHeaders:"
- "serverPublicKey_B"
- "serverTrust"
- "session"
- "sessionUUID"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setAccount:"
- "setAccountDescription:"
- "setAccountStore:"
- "setActiveSocketHandler:"
- "setAggregateStatistics:"
- "setAndroidAPILevel:"
- "setAndroidBrand:"
- "setAndroidLocale:"
- "setAndroidModel:"
- "setAndroidOSVersion:"
- "setAndroidVersion:"
- "setAndroidVersionCode:"
- "setApi:"
- "setApiLevel:"
- "setAppStoreIdentifier:"
- "setAssociatedObject:"
- "setAttemptCount:"
- "setBool:forKey:"
- "setBrand:"
- "setBucket:"
- "setBundleIdentifier:"
- "setBytes:"
- "setCanAddAccessibility:"
- "setCanAddDisplay:"
- "setCanAddFiles:"
- "setChannel:"
- "setClientVersion:"
- "setCommand:"
- "setCommunicationDate:"
- "setCompletedDownloadSegmentCount:"
- "setContactStore:"
- "setContentType:"
- "setCount:"
- "setCrashCount:"
- "setCredentials:forAuthentication:"
- "setData:forSummary:"
- "setDataCoordinator:"
- "setDataFilePath:"
- "setDataSource:"
- "setDatabasePath:"
- "setDateFormat:"
- "setDelegate:"
- "setDevice:"
- "setDeviceModel:"
- "setDeviceOSVersion:"
- "setDeviceType:"
- "setDidDownload:"
- "setDidDownloadForSummary:forSourceDevice:"
- "setDownloadByteCount:"
- "setDownloadDuration:"
- "setDownloadSegmentCount:"
- "setDownloadsPath:"
- "setDuration:"
- "setElapsedTime:"
- "setEnabled:"
- "setEnabled:forDataclass:"
- "setEndDate:"
- "setErrorCount:"
- "setEstimate:"
- "setEstimatedDataSize:"
- "setExpectedBytes:"
- "setExpectedDownloadBytesRemainingForItemsWithConcreteSizes:"
- "setExpectedDownloadSegmentsRemaining:"
- "setExpectedDownloadSegmentsRemainingForItemsWithEstimatedSizes:"
- "setFeaturePayload:"
- "setFetchDuration:"
- "setFetchEndBytesFree:"
- "setFetchStartBytesFree:"
- "setFilters:"
- "setGuid:"
- "setHTTPMaximumConnectionsPerHost:"
- "setHTTPMethod:"
- "setHardwareBrand:"
- "setHardwareDesign:"
- "setHardwareMaker:"
- "setHardwareModel:"
- "setHardwareProduct:"
- "setHost:"
- "setHttpPort:"
- "setIdentifier:"
- "setIdentifiers:"
- "setImportEndBytesFree:"
- "setImportEndDate:"
- "setImportErrorCount:"
- "setImportErrors:"
- "setImportFailedRecordCount:"
- "setImportRecordCount:"
- "setImportStartBytesFree:"
- "setImportStartDate:"
- "setIpAddress:"
- "setIsEnabled:"
- "setIsFree:"
- "setIsGroupMessage:"
- "setIsLocal:"
- "setIsSelectingDataTypeInHandshake:"
- "setItemSize:"
- "setLastProgressSentDate:"
- "setLastProgressSentToAndroidDevice:"
- "setLocalCertificate:"
- "setLocale:"
- "setMaxConcurrentOperationCount:"
- "setMessageDirection:"
- "setMetadata:"
- "setMetadata:forSourceDevice:"
- "setMigrationError:forSummary:"
- "setMigrators:"
- "setModeValue:"
- "setModel:"
- "setModifiedDate:"
- "setName:"
- "setNextIncomingConnectionHandler:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOsAPIVersion:"
- "setOsVersion:"
- "setPayload:"
- "setPersistentIdentifier:"
- "setPort:"
- "setPowerAssertion:"
- "setPredicate:"
- "setPrivateKey:"
- "setProgress:"
- "setProvisioned:forDataclass:"
- "setPublicKey:"
- "setQueue:"
- "setRecipients:"
- "setRef:"
- "setRelativePath:"
- "setRemoteCertificate:"
- "setRootPath:"
- "setRowID:"
- "setSamples:"
- "setSelectedForMigration:"
- "setSender:"
- "setSession:"
- "setSize:"
- "setSocketPort:"
- "setSourceDevice:"
- "setSqlController:"
- "setSqlID:"
- "setSsid:"
- "setStartDate:"
- "setStashDataLocally:"
- "setState:"
- "setStoreDataAsFile:"
- "setSummary:"
- "setSupportsFileLength:"
- "setSuspended:"
- "setTLSMaximumSupportedProtocolVersion:"
- "setTLSMinimumSupportedProtocolVersion:"
- "setThreshold:"
- "setThresholds:"
- "setThroughputBytesInCurrentPeriod:"
- "setThroughputSamples:"
- "setThroughputSegmentStartDate:"
- "setThroughputSegmentsInCurrentPeriod:"
- "setTimeEstimateAccuracyTracker:"
- "setTimeZone:"
- "setTimeoutInterval:"
- "setType:"
- "setUnderlyingQueue:"
- "setUrlSessionController:"
- "setUseMigrationKit:"
- "setUsername:"
- "setValue:forKey:"
- "setValue:forParameter:"
- "setVersion:"
- "setVersionCode:"
- "setWillImportForSummary:"
- "setWithArray:"
- "setWithObjects:"
- "settingsWithData:"
- "sharedInstance"
- "sharedKey_K"
- "sharedPhotoLibrary"
- "size"
- "socketPort"
- "sockfd"
- "softAPDidStart:ssid:psk:secret:srp:channel:error:completion:"
- "sortDescriptorWithKey:ascending:"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingDescriptors:"
- "sortedHandleIDs"
- "sourceDevice"
- "sourceThreadID"
- "sqlController"
- "sqlID"
- "ssid"
- "standardUserDefaults"
- "start"
- "startDHCPWithCompletion:"
- "startDate"
- "startMigration:usingRetryPolicies:completion:"
- "startMigrationWithSourceDevice:usingRetryPolicies:delegate:completion:"
- "startNetworkWithHostRole:request:completion:"
- "startWiFiAndDeviceDiscoveryWithPreGeneratedCode:completion:"
- "startWithItemLookupBlock:"
- "startWithPurchaseResponseBlock:completionBlock:"
- "stashData:forSummary:migrator:"
- "stashDataLocally"
- "stashFileForSummary:migrator:"
- "state"
- "statisticsForContentType:"
- "statusCode"
- "stopDHCPWithCompletion:"
- "stopDeviceDiscoveryWithCompletion:"
- "stopNetwork:completion:"
- "stopWiFiAndDeviceDiscoveryWithCompletion:"
- "storeDataAsFile"
- "storeRecordDataInDatabase"
- "string"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringByReplacingCharactersInRange:withString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByReplacingOccurrencesOfString:withString:options:range:"
- "stringByResolvingAndStandardizingPath"
- "stringByTrimmingCharactersInSet:"
- "stringForKey:"
- "stringValue"
- "stringWithCapacity:"
- "stringWithCharacters:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "subdataWithRange:"
- "subject"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "subtype"
- "summariesDataForAccount:migrator:completion:"
- "summariesForAccount:"
- "summariesForAccounts:sortedByModifiedDate:"
- "summary"
- "summaryWithInfo:account:"
- "superclass"
- "supportedDataclasses"
- "supportsLocalImport"
- "suspend"
- "synchronizeFile"
- "threadID"
- "threshold"
- "thresholds"
- "throughputBytesInCurrentPeriod"
- "throughputSamples"
- "throughputSegmentStartDate"
- "throughputSegmentsInCurrentPeriod"
- "timeEstimateAccuracyTracker"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "timeIntervalSinceReferenceDate"
- "timeZoneForSecondsFromGMT:"
- "totalSummaryDownloadSegmentCountForAccounts:"
- "totalSummaryDownloadedSegmentCountForAccounts:"
- "totalSummaryItemSizeForAccounts:addOverhead:completion:"
- "typeWithMIMEType:"
- "unarchivedObjectOfClasses:fromData:error:"
- "unlockSync"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updateModifiedDateForSummary:"
- "updateSource:withProgress:remainingTime:completion:"
- "updateStatistics:"
- "updateUIWithProgress:remainingTime:logString:completion:"
- "uppercaseString"
- "urlSession"
- "urlSessionController"
- "useMigrationKit"
- "userDidChooseToInstallMigratableApps:"
- "userInfo"
- "username"
- "uti"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8S16"
- "v20@0:8i16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@\"NSXMLParser\"16"
- "v24@0:8@\"WLFeaturePayload\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^q16"
- "v24@0:8^v16"
- "v24@0:8^{__SecCertificate=}16"
- "v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16"
- "v24@0:8^{__WiFiDeviceClient=}16"
- "v24@0:8^{__WiFiManagerClient=}16"
- "v24@0:8^{__WiFiNetwork=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8i16@20"
- "v32@0:8@\"<WLDataclassMigrating>\"16@?<v@?@\"NSDictionary\"Q@\"NSError\"d>24"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"NSXMLParser\"16@\"NSData\"24"
- "v32@0:8@\"NSXMLParser\"16@\"NSError\"24"
- "v32@0:8@\"NSXMLParser\"16@\"NSString\"24"
- "v32@0:8@\"WLDeviceDiscoverySocketHandler\"16@\"WLSourceDevice\"24"
- "v32@0:8@\"WLSourceDeviceRecordSummary\"16@\"NSData\"24"
- "v32@0:8@\"WLSourceDeviceRecordSummary\"16@\"WLSourceDeviceAccount\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16B24B28"
- "v32@0:8^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16@24"
- "v32@0:8d16@24"
- "v32@0:8i16@20B28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16S24@?28"
- "v36@0:8@16i24@?28"
- "v36@0:8i16@20@?28"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"WLDeviceDiscoverySocketHandler\"16@\"WLSourceDevice\"24@\"NSError\"32"
- "v40@0:8@\"WLSourceDeviceAccount\"16@\"<WLDataclassMigrating>\"24@?<v@?@\"NSDictionary\"Q@\"NSError\"d>32"
- "v40@0:8@\"WLSourceDeviceRecordSummary\"16@\"<WLDataclassMigrating>\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"WLSourceDeviceRecordSummary\"16@\"<WLDataclassMigrating>\"24@?<v@?Q@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8Q16@24@32"
- "v40@0:8^{__WiFiDeviceClient=}16@24@?32"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16B24@28@36"
- "v44@0:8@16B24@28@?36"
- "v44@0:8r^v16Q24i32@?36"
- "v48@0:8@\"NSData\"16@\"WLSourceDeviceRecordSummary\"24@\"WLSourceDeviceAccount\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
- "v48@0:8@\"WLSourceDeviceRecordSummary\"16@\"<WLDataclassMigrating>\"24@?<@\"NSError\"@?@\"NSURL\">32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@?32@?40"
- "v48@0:8@16d24d32@?40"
- "v48@0:8@?16@24@?32@?40"
- "v48@0:8@?<@\"NSData\"@?@\"WLSourceDeviceRecordSummary\">16@\"NSArray\"24@?<v@?@\"WLSourceDeviceRecordSummary\">32@?<v@?@\"WLSourceDeviceRecordSummary\"@\"NSError\">40"
- "v48@0:8^{__WiFiDeviceClient=}16^{__WiFiNetwork=}24@32@?40"
- "v48@0:8d16d24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8d16d24@32@?40"
- "v52@0:8r^v16Q24Q32i40@?44"
- "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48"
- "v56@0:8@\"NSXMLParser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@\"WLSourceDeviceRecordSummary\"16{_NSRange=QQ}24@\"<WLDataclassMigrating>\"40@?<v@?@\"NSData\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24Q32@40@?48"
- "v56@0:8@16@?24@32@?40@?48"
- "v56@0:8@16{_NSRange=QQ}24@40@?48"
- "v64@0:8@16@24@32@40@48@?56"
- "v64@0:8@16@24@32@40@?48@?56"
- "v64@0:8@16@24@32@?40@?48@?56"
- "v64@0:8@16Q24Q32@40@?48@?56"
- "v68@0:8@16Q24Q32B40d44@52@?60"
- "v72@0:8@16@24@32@40Q48@?56@?64"
- "v76@0:8B16@20@28@36@44@52@60@?68"
- "v88@0:8@16@24Q32@40@48Q56@64@?72@?80"
- "v92@0:8@16@24@32@40@48@?56B64@68@76q84"
- "valueForHTTPHeaderField:"
- "valueWithRange:"
- "versionCode"
- "video"
- "videos"
- "waitForBlobDataFromReadCacheReturningError:"
- "waitForCommand:fromReadCacheReturningError:"
- "waitForDataFromReadCacheReturningError:"
- "waitForMessageFromReadCacheReturningError:"
- "waitUntilAllOperationsAreFinished"
- "wantsSegmentedDownloads"
- "whitespaceAndNewlineCharacterSet"
- "wifiDidFail"
- "wk_representsTransientConnectivityIssueForAttempt:"
- "wl_arrayOfDataFromLengthPrefixedBlobSequenceWithExpectedCount:"
- "wl_blobIsComplete"
- "wl_dataFromHexEncodedData:"
- "wl_dataFromHexEncodedString:"
- "wl_dataFromLengthPrefixedBlob"
- "wl_encodableError"
- "wl_encodableErrorSupportedClasses"
- "wl_hexEncodedData"
- "wl_hexEncodedString"
- "wl_hmacSHA256DataForData:key:"
- "wl_integerForKey:"
- "wl_lengthPrefixedBlob"
- "wl_lengthPrefixedBlobSequenceFromDataArray:"
- "wl_sqlIDComponentsSeparatedByString:"
- "wl_stringForKey:"
- "wl_subdataWithRangeExcludingTrailingCrnl:"
- "wl_uniqueIdentifier"
- "wl_utf8String"
- "writeBytes:length:toSocket:completion:"
- "writeCodeForTestAutomationIfNeeded:"
- "writeData:"
- "writeToFile:atomically:"
- "writeToURL:options:error:"
- "zone"
- "{_NSRange=QQ}68@0:8@16@24{_NSRange=QQ}32@48B56@60"

```
