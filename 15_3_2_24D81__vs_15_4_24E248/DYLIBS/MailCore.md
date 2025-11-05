## MailCore

> `/System/Library/PrivateFrameworks/MailCore.framework/Versions/A/MailCore`

```diff

-3826.400.131.1.6
-  __TEXT.__text: 0x875fc
+3826.500.181.1.5
+  __TEXT.__text: 0x88bc8
   __TEXT.__auth_stubs: 0x1200
-  __TEXT.__objc_methlist: 0x7444
-  __TEXT.__const: 0x488
-  __TEXT.__cstring: 0x7d8a
-  __TEXT.__gcc_except_tab: 0x161c
-  __TEXT.__oslogstring: 0x1b4d
-  __TEXT.__unwind_info: 0x20f8
+  __TEXT.__objc_methlist: 0x7fec
+  __TEXT.__const: 0x4a0
+  __TEXT.__cstring: 0x7d70
+  __TEXT.__gcc_except_tab: 0x16a0
+  __TEXT.__oslogstring: 0x1b85
+  __TEXT.__unwind_info: 0x21d0
   __TEXT.__objc_classname: 0xdba
-  __TEXT.__objc_methname: 0x140da
+  __TEXT.__objc_methname: 0x140f4
   __TEXT.__objc_methtype: 0x2b5f
   __TEXT.__objc_stubs: 0x10560
   __DATA_CONST.__got: 0x10f0
-  __DATA_CONST.__const: 0x1238
+  __DATA_CONST.__const: 0x11c8
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5198
+  __DATA_CONST.__objc_selrefs: 0x5360
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x190
   __AUTH_CONST.__auth_got: 0x910
   __AUTH_CONST.__const: 0x12c0
-  __AUTH_CONST.__cfstring: 0x9020
-  __AUTH_CONST.__objc_const: 0xde60
+  __AUTH_CONST.__cfstring: 0x9000
+  __AUTH_CONST.__objc_const: 0xc990
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x180

   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x3f8
   __DATA_DIRTY.__objc_data: 0x20d0
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58CCD748-ACEF-3325-842E-FFB6554B1D1C
-  Functions: 2678
-  Symbols:   7694
+  UUID: D8B5DB75-B192-3A22-8733-0046A9BC7FFB
+  Functions: 2814
+  Symbols:   7872
   CStrings:  6721
 
Symbols:
+ +[MCAddressManager previousRecipientsLog].cold.1
+ +[MCArchiveFileWrapper log].cold.1
+ +[MCArchiveFileWrapper workingDirectory].cold.1
+ +[MCAttachment log].cold.1
+ +[MCCIDURLProtocol unregisterDataProvider:].cold.1
+ +[MCContactsManager test_resetSharedInstance].cold.1
+ +[MCDateFormatterFactory newIMAPDateFormatter].cold.1
+ +[MCDateParser _commonDateFormatters].cold.1
+ +[MCDateParser _dateFromString:imapFirst:].cold.1
+ +[MCDateParser _fallbackDateFormaters].cold.1
+ +[MCDateParser _imapDateFormatter].cold.1
+ +[MCInvocationQueue test_cancelAllMonitoredItems].cold.1
+ +[MCInvocationQueue test_uncancelAllMonitoredItems].cold.1
+ +[MCKeychainManager copyEncryptionCertificateForAddress:].cold.1
+ +[MCKeychainManager copySigningIdentityForAddress:error:].cold.1
+ +[MCKeychainManager copyTLSClientIdentities].cold.1
+ +[MCMessageHeaders _localizedHeadersForKeys].cold.1
+ +[MCMessageHeaders basicHeaderKeys].cold.1
+ +[MCMessageHeaders localizedHeaders].cold.1
+ +[MCMimeDataEncoding sharedKeySetForEncodingOptions].cold.1
+ +[MCMonitoredInvocation invocationWithSelector:target:].cold.1
+ +[MCMonitoredInvocation invocationWithSelector:target:object1:object2:].cold.1
+ +[MCMonitoredInvocation invocationWithSelector:target:object1:object2:object3:].cold.1
+ +[MCMonitoredInvocation invocationWithSelector:target:object1:object2:object3:object4:].cold.1
+ +[MCMonitoredInvocation invocationWithSelector:target:object:].cold.1
+ +[MCMutableMessageHeaders log]
+ +[MCNetworkController log].cold.1
+ +[MCNetworkController networkStatus].cold.1
+ +[MCNetworkController networkStatus].cold.2
+ +[MCPowerSourceManager log].cold.1
+ +[MCSharedPreferencesController test_resetSharedInstance].cold.1
+ +[MCSocket log].cold.1
+ +[MCTaskHandler log].cold.1
+ +[MCWorkerThread addInvocationToQueue:].cold.1
+ +[MCWorkerThread runInvocationOnQueueSynchronously:].cold.1
+ +[MCWorkerThread test_cancelAllInvocations].cold.1
+ +[MCWorkerThread test_waitUntilAllOperationsAreFinished].cold.1
+ +[MailCoreFramework isRunningInMail].cold.1
+ +[MailCoreFramework setAccountsUnavailableFromSpotlightImporter:].cold.1
+ -[ABRecord(MailCoreAdditions) compoundName].cold.1
+ -[MCActivityAggregate _updateStatus].cold.1
+ -[MCActivityAggregate updateUnitBasedValues].cold.1
+ -[MCActivityAggregator activityMonitor:didChangeTypeFrom:].cold.1
+ -[MCActivityAggregator activityMonitor:didChangeTypeFrom:].cold.2
+ -[MCActivityUpdater dealloc].cold.1
+ -[MCActivityUpdater invalidate].cold.1
+ -[MCArchiveFileWrapper addFileWrapper:].cold.1
+ -[MCArchiveFileWrapper initWithURL:compressionLevel:error:].cold.2
+ -[MCArchiveFileWrapper keyForFileWrapper:].cold.1
+ -[MCArchiveFileWrapper removeFileWrapper:].cold.1
+ -[MCAttachment approximateSizeForAccessLevel:].cold.1
+ -[MCAttachment dataForAccessLevel:].cold.1
+ -[MCAttachment fileURL].cold.4
+ -[MCAttachment fileWrapperForAccessLevel:error:].cold.1
+ -[MCAttachment getCompressedData:compressedFileURL:archiveType:error:].cold.5
+ -[MCAttachmentWrappingTextAttachment setFileWrapper:].cold.1
+ -[MCCIDURLProtocol startLoading].cold.1
+ -[MCConnection connectDiscoveringBestSettings:].cold.1
+ -[MCConnection connectDiscoveringBestSettings:].cold.2
+ -[MCConnection test_setSocket:].cold.1
+ -[MCContactsManager test_tearDown].cold.1
+ -[MCDisplayNameInfo initWithShortName:fullName:].cold.1
+ -[MCDisplayNameManager _cacheItemForFullAddress:].cold.1
+ -[MCDisplayNameManager _queriedDisplayNameInfoForAddress:].cold.1
+ -[MCDisplayNameManager initWithCacheDelegate:].cold.1
+ -[MCDisplayNameManager test_notificationCenter].cold.1
+ -[MCFileURLAttachmentDataSource _backgroundFileReadingQueue].cold.1
+ -[MCFileWrapper(HFSDataConversion) appleDoubleDataWithFilename:length:].cold.1
+ -[MCFileWrapper(HFSDataConversion) appleSingleDataWithFilename:length:].cold.1
+ -[MCInvocationQueue runInvocationOnQueueSynchronously:].cold.1
+ -[MCMemoryDataSource _flagChangeDictionaryForJunkMailLevel:forMessages:userRecorded:changedMessages:].cold.1
+ -[MCMessage description].cold.1
+ -[MCMessageBody _addWebArchiveDataToArray:].cold.1
+ -[MCMessageBody _mcMessageBodyCommonInit].cold.1
+ -[MCMessageBody addAttachment:forURL:].cold.1
+ -[MCMessageBody attributedStringBlockingRemoteContent:attachmentAccessLevel:].cold.1
+ -[MCMessageGenerator _setMessageIDAndMIMETypeForTopLevelHeaders:].cold.1
+ -[MCMessageHeaders addressListForKey:].cold.1
+ -[MCMessageHeaders firstAddressForKey:].cold.1
+ -[MCMessageHeaders firstHeaderForKey:].cold.1
+ -[MCMessageHeaders firstHeaderForKey:].cold.2
+ -[MCMessageHeaders firstHeaderForKey:].cold.3
+ -[MCMessageHeaders firstMessageIDForKey:].cold.1
+ -[MCMessageHeaders firstURLForKey:].cold.1
+ -[MCMessageHeaders headersForKey:].cold.1
+ -[MCMessageHeaders headersForKey:].cold.2
+ -[MCMessageHeaders headersForKey:].cold.3
+ -[MCMessageHeaders initWithHeaderData:encodingHint:].cold.1
+ -[MCMessageHeaders messageIDListForKey:].cold.1
+ -[MCMessageHeaders urlListForKey:].cold.1
+ -[MCMimeCharset initWithCFEncoding:].cold.1
+ -[MCMimePart _parseSubpartsWithEncodingHint:hasVisualEncoding:depth:].cold.2
+ -[MCMimePart _parseSubpartsWithEncodingHint:hasVisualEncoding:depth:].cold.3
+ -[MCMimePart _parseUUEncodedPartsWithEncodingHint:].cold.1
+ -[MCMimePart childPartWithNumber:].cold.1
+ -[MCMimePart cmsExtractedChildPartWithNumber:].cold.1
+ -[MCMonitoredInvocation invokeWithTarget:].cold.1
+ -[MCMonitoredInvocation setTarget:].cold.1
+ -[MCMutableMessageHeaders _appendHeaderKey:value:toData:].cold.1
+ -[MCMutableMessageHeaders addressListForKey:].cold.1
+ -[MCMutableMessageHeaders encodedHeaders].cold.1
+ -[MCMutableMessageHeaders firstHeaderForKey:].cold.1
+ -[MCMutableMessageHeaders firstHeaderForKey:].cold.2
+ -[MCMutableMessageHeaders messageIDListForKey:].cold.1
+ -[MCMutableMessageHeaders setAddressList:forKey:].cold.1
+ -[MCMutableMessageHeaders setMessageIDList:forKey:].cold.1
+ -[MCProgressEntry addProgress:].cold.1
+ -[MCRemoteURLAttachmentDataSource _remoteDownloadQueue].cold.1
+ -[MCSocket connectToHost:withPort:isBackground:].cold.3
+ -[MCSocket init].cold.1
+ -[MCSocket readBytes:maxLength:error:].cold.3
+ -[MCSocket registerForBytesToArriveWithHandler:].cold.1
+ -[MCSocket unregisterForBytesToArrive].cold.1
+ -[MCSocket writeBytes:maxLength:error:].cold.3
+ -[MCTask dealloc].cold.1
+ -[MCTask end].cold.1
+ -[MCTask operationFinished:].cold.1
+ -[MCTask trackOperation:].cold.1
+ -[MCTaskHandler cleanUp].cold.1
+ -[MCTaskHandler dealloc].cold.1
+ -[MCTaskManager activityDidFinish:].cold.1
+ -[MCTaskManager addActivity:].cold.1
+ -[MCTaskManager addNetworkHandler:].cold.1
+ -[MCTaskManager addPersistenceHandler:].cold.1
+ -[MCTaskManager failedToCreateNetworkHandler].cold.1
+ -[MCTaskManager handlerDidCleanUp:].cold.1
+ -[MCTaskManager removeNetworkHandler:].cold.1
+ -[MCTaskManager removePersistenceHandler:].cold.1
+ -[MCTaskManager tasksNeedAssignment].cold.1
+ -[MCTaskManager test_terminateAndWaitUntilFinished].cold.1
+ -[MCTaskManager utilityQueue].cold.1
+ -[NSData(HFSDataConversion) wrapperForAppleFileDataWithFileEncodingHint:].cold.1
+ -[NSData(HFSDataConversion) wrapperForBinHex40DataWithFileEncodingHint:].cold.1
+ -[NSMutableData(RFC2231Support) appendRFC2231CompliantValue:forKey:withEncodingHint:].cold.1
+ -[NSMutableData(RFC2231Support) appendRFC2231CompliantValue:forKey:withEncodingHint:].cold.2
+ -[NSMutableData(RFC2231Support) appendRFC2231CompliantValue:forKey:withEncodingHint:].cold.3
+ -[NSMutableDictionary(RFC2231Support) fixupRFC2231ValuesWithSender:fromWindows:].cold.1
+ -[NSString(MCFormatFlowedSupport) convertFromFlowedText:].cold.1
+ -[NSString(MailCoreAdditions) stringByReplacingNonBreakingSpacesWithString:].cold.1
+ -[NSString(RFC2047Support) decodeMimeHeaderValueWithCharsetHint:detectOtherEncodings:fromWindows:].cold.1
+ -[NSString(RFC2047Support) decodeMimeHeaderValueWithCharsetHint:detectOtherEncodings:fromWindows:].cold.2
+ -[_MCMemoryMessage setDataSource:].cold.1
+ -[_MCMimeEnrichedReader parenthesesSet].cold.1
+ -[_MCMimeEnrichedReader punctuationSet].cold.1
+ MCAllowInternalDiagnostics.cold.1
+ MCCreateStringFromHeaderData.cold.1
+ MCLogDiagnostics.cold.1
+ MCLogSubsystem.cold.1
+ __27-[MCTaskManager terminate:]_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_MCMutableMessageHeaders
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EFPubliclyDescribable
+ ___30+[MCMutableMessageHeaders log]_block_invoke
+ __mapFlagColorForEmailCore
+ _ef_log_MCProgressGroup.cold.1
+ computeProgress.cold.1
+ createInternetMessageDateFormatter.cold.1
+ enumerateHeaderValueFoldingRanges.cold.1
+ getLogsDirectoryURL.cold.1
CStrings:
+ "Got exception %{public}@ while constructing header data"
+ "ef_shortPublicDescription"
- ", flagged (invalid color)"

```
