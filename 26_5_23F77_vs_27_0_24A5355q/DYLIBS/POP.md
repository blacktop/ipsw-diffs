## POP

> `/System/Library/PrivateFrameworks/Message.framework/MailServices/POP.framework/POP`

```diff

-3864.600.51.2.1
-  __TEXT.__text: 0x924c
-  __TEXT.__auth_stubs: 0x440
+3891.100.17.2.4
+  __TEXT.__text: 0x8bd0
   __TEXT.__objc_methlist: 0x76c
-  __TEXT.__gcc_except_tab: 0x14b8
-  __TEXT.__cstring: 0x3eb
+  __TEXT.__gcc_except_tab: 0x13e4
+  __TEXT.__cstring: 0x3fa
   __TEXT.__ustring: 0x2fc
   __TEXT.__const: 0xa8
   __TEXT.__oslogstring: 0x27f
-  __TEXT.__unwind_info: 0x4c0
-  __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0x1fde
-  __TEXT.__objc_methtype: 0x3fc
-  __TEXT.__objc_stubs: 0x2220
-  __DATA_CONST.__got: 0x1c0
+  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa88
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x1c0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x5c0
   __AUTH_CONST.__objc_const: 0x920
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x88
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/MessageSupport.framework/MessageSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DEFD2556-B60D-33C9-BE0B-45CD4E14669A
+  UUID: B279A2C8-8F7C-3573-BBF2-749AAD297D0E
   Functions: 157
-  Symbols:   906
-  CStrings:  570
+  Symbols:   912
+  CStrings:  119
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$primaryMailbox
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x8
- _objc_msgSend$primaryMailboxUid
- _objc_retain_x28
Functions:
~ +[MFAPOPAuthScheme initialize] : 124 -> 120
~ -[MFAPOPAuthScheme connectionClassForAccountClass:] : 136 -> 120
~ -[MFAPOPAuthScheme name] : 64 -> 16
~ -[MFAPOPConnection authenticateUsingAccount:] : 892 -> 832
~ -[MFLibraryPOPStore initWithMailbox:readOnly:] : 76 -> 80
~ -[MFLibraryPOPStore dataForMimePart:inRange:isComplete:downloadIfNecessary:didDownload:] : 616 -> 588
~ -[MFLibraryPOPStore dataForMimePart:inRange:isComplete:withConsumer:downloadIfNecessary:didDownload:] : 196 -> 192
~ -[MFLibraryPOPStore bodyDataForMessage:isComplete:isPartial:downloadIfNecessary:] : 344 -> 324
~ -[MFLibraryPOPStore fullBodyDataForMessage:andHeaderDataIfReadilyAvailable:isComplete:downloadIfNecessary:usePartDatas:didDownload:] : 132 -> 128
~ -[MFLibraryPOPStore _fetchHeaderDataForMessage:downloadIfNecessary:] : 636 -> 604
~ -[MFLibraryPOPStore _fetchBodyDataForMessage:andHeaderDataIfReadilyAvailable:downloadIfNecessary:partial:] : 1128 -> 1084
~ -[MFLibraryPOPStore purgeMessages:] : 140 -> 136
~ -[MFLibraryPOPStore fetchNumMessages:preservingUID:options:] : 408 -> 384
~ -[MFLibraryPOPStore messageForRemoteID:] : 252 -> 236
~ -[MFLibraryPOPStore messagesWereDeleted:] : 452 -> 436
~ -[MFLibraryPOPStore _handleFlagsChangedForMessages:flags:oldFlagsByMessage:] : 552 -> 560
~ -[MFLibraryPOPStore setServerMessageCount:] : 16 -> 20
~ -[MFLibraryPOPStore serverMessageCount] : 16 -> 20
~ -[MFLibraryPOPStore setServerUnreadOnlyOnServerCount:] : 148 -> 140
~ +[MFPOP3Fetcher _fetchWithAccount:intoQueue:newMessages:oldMessages:preservingUID:withStore:] : 4704 -> 4476
~ +[MFPOP3Fetcher fetchWithAccount:newMessages:oldMessages:preservingUID:withStore:] : 268 -> 276
~ -[MFPOPMessage messageData] : 148 -> 144
~ -[MFPOPMessage setMessageData:isComplete:] : 144 -> 136
~ -[MFPOPMessage messageDataHolder] : 176 -> 164
~ -[MFPOPMessage setMessageSize:] : 16 -> 20
~ -[MFPOPMessage messageData:messageSize:isComplete:downloadIfNecessary:] : 156 -> 168
~ -[MFPOPMessage messageDataHolder:messageSize:isComplete:downloadIfNecessary:] : 176 -> 184
~ -[MFPOPMessage remoteMailboxURL] : 64 -> 20
~ -[MFPOPMessage headers] : 300 -> 288
~ -[MFPOPMessage setAccountURL:] : 120 -> 116
~ -[MFPOPMessage messageNumber] : 16 -> 20
~ -[MFPOPMessage setMessageNumber:] : 16 -> 20
~ -[MFPOPMessage messageID] : 16 -> 20
~ +[MFPOP3Connection log] : 176 -> 160
~ ___23+[MFPOP3Connection log]_block_invoke : 136 -> 132
~ -[MFPOP3Connection init] : 96 -> 100
~ -[MFPOP3Connection capabilities] : 1004 -> 888
~ -[MFPOP3Connection authenticationMechanisms] : 568 -> 552
~ -[MFPOP3Connection _doBasicConnectionWithAccount:] : 576 -> 512
~ -[MFPOP3Connection connectUsingAccount:] : 584 -> 548
~ -[MFPOP3Connection authenticateUsingAccount:] : 2296 -> 2056
~ -[MFPOP3Connection authenticateUsingAccount:authenticator:] : 788 -> 772
~ -[MFPOP3Connection supportsAPOP] : 24 -> 28
~ -[MFPOP3Connection disableAPOP] : 20 -> 24
~ -[MFPOP3Connection doStat] : 308 -> 312
~ -[MFPOP3Connection list:] : 164 -> 160
~ -[MFPOP3Connection _getListResults] : 520 -> 516
~ -[MFPOP3Connection _getUidlResults] : 716 -> 732
~ -[MFPOP3Connection getMessageNumbers:messageIdsByNumber:numbersByMessageId:] : 280 -> 284
~ -[MFPOP3Connection serverMessageCount] : 116 -> 124
~ -[MFPOP3Connection idForMessageNumber:] : 420 -> 416
~ -[MFPOP3Connection _retrieveMessage:ofSize:consumer:] : 224 -> 220
~ -[MFPOP3Connection retr:consumer:intoQueue:idsByNumber:allowIncomplete:queueStatus:] : 1116 -> 1032
~ -[MFPOP3Connection retr:data:] : 148 -> 144
~ -[MFPOP3Connection dele:] : 168 -> 164
~ -[MFPOP3Connection sizeOfMessageNumber:] : 180 -> 176
~ -[MFPOP3Connection numberOfMessagesAvailable] : 16 -> 20
~ -[MFPOP3Connection fetchMessages:intoQueue:serverIDsByNumber:] : 784 -> 700
~ -[MFPOP3Connection deleteMessagesOnServer:] : 268 -> 256
~ -[MFPOP3Connection startTLSForAccount:] : 764 -> 712
~ -[MFPOP3Connection getTop:ofMessageNumber:intoMutableData:] : 384 -> 376
~ -[MFPOP3Connection _readMultilineResponseWithMaxSize:consumer:] : 500 -> 492
~ -[MFPOP3Connection _sendCommand:withArguments:] : 552 -> 556
~ -[MFPOP3Connection _getStatusFromReply] : 1232 -> 1236
~ -[MFPOP3Connection _apopWithUsername:password:] : 592 -> 628
~ -[POPAccount initWithLibrary:persistentAccount:] : 296 -> 316
~ -[POPAccount fetchNumNewMessages:oldMessages:preservingUID:withStore:] : 532 -> 476
~ -[POPAccount releaseAllForcedConnections] : 128 -> 124
~ +[POPAccount accountTypeIdentifier] : 64 -> 16
~ +[POPAccount csAccountTypeString] : 64 -> 16
~ -[POPAccount certUIService] : 64 -> 16
~ -[POPAccount statisticsKind] : 64 -> 16
~ -[POPAccount storeClassForMailbox:] : 144 -> 124
~ -[POPAccount connectionClass] : 112 -> 88
~ -[POPAccount shouldAttemptAPOP] : 16 -> 20
~ -[POPAccount setShouldAttemptAPOP:] : 16 -> 20
~ -[POPAccount setDelayedMessageDeletionInterval:] : 144 -> 140
~ -[POPAccount messageDeletionPolicy] : 292 -> 288
~ -[POPAccount delayedMessageDeletionInterval] : 144 -> 140
~ -[POPAccount _URLScheme] : 64 -> 16
~ -[POPAccount setOldestKnownMessageUID:] : 120 -> 116
~ -[POPAccount setNewestKnownMessageUID:] : 120 -> 116
~ -[POPAccount oldestKnownMessageUID] : 64 -> 20
~ -[POPAccount newestKnownMessageUID] : 64 -> 20
~ -[POPAccount setNumberOfKnownUIDs:] : 16 -> 20
~ -[POPAccount numberOfKnownUIDs] : 16 -> 20
~ -[POPAccount _deleteHook] : 292 -> 280
~ -[POPAccount connectionsInUse] : 60 -> 64
~ -[POPAccount _getCachedConnection] : 176 -> 188
~ -[POPAccount authenticatedConnection] : 264 -> 268
~ -[POPAccount checkInConnection:currentUIDs:] : 484 -> 492
~ -[POPAccount mailboxUidOfType:createIfNeeded:] : 140 -> 136
~ -[POPAccount scheduleDisconnect] : 108 -> 112
~ -[POPAccount closeConnection:andSaveUIDs:] : 468 -> 464
~ -[POPAccount closeCachedConnectionForcedOnly:] : 436 -> 448
CStrings:
- "#16@0:8"
- "#24@0:8#16"
- "#24@0:8@16"
- ".cxx_destruct"
- "@\"MFActivityMonitor\""
- "@\"MFLock\""
- "@\"MFMailMessageLibrary\""
- "@\"MFMailboxUid\""
- "@\"MFPOP3Connection\""
- "@\"MFSqliteMessageIDStore\""
- "@\"NSArray\""
- "@\"NSConditionLock\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSMutableData\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8q16B24"
- "@32@0:8@16@24"
- "@44@0:8@16^@24B32^B36"
- "@44@0:8@16^B24^B32B40"
- "@56@0:8@16^@24^B32B40B44^B48"
- "@60@0:8@16{_NSRange=QQ}24^B40B48^B52"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8#16@24"
- "B32@0:8@16@24"
- "B44@0:8^@16^Q24^B32B40"
- "B68@0:8@16{_NSRange=QQ}24^B40@48B56^B60"
- "I16@0:8"
- "MFAPOPAuthScheme"
- "MFAPOPConnection"
- "MFLibraryPOPStore"
- "MFPOP3Connection"
- "MFPOP3Fetcher"
- "MFPOPDownloadQueue"
- "MFPOPMessage"
- "POPAccount"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8Q16"
- "T@\"NSData\",&,N"
- "T@\"NSString\",C,N,V_messageID"
- "Tq,N,V_messageNumber"
- "UIDsToDeleteInMailbox:"
- "URLString"
- "UTF8String"
- "^v16@0:8"
- "_URLScheme"
- "_accountURL"
- "_apopTimeStamp"
- "_apopWithUsername:password:"
- "_cachedBodyDataContainerForMessage:valueIfNotPresent:"
- "_connection"
- "_connectionActivityLock"
- "_connectionTimeout"
- "_connectionsInUse"
- "_createNewConnection"
- "_currentUIDs"
- "_deleteHook"
- "_doBasicConnectionWithAccount:"
- "_fetchBodyDataForMessage:andHeaderDataIfReadilyAvailable:downloadIfNecessary:partial:"
- "_fetchHeaderDataForMessage:downloadIfNecessary:"
- "_fetchMonitor"
- "_fetchWithAccount:intoQueue:newMessages:oldMessages:preservingUID:withStore:"
- "_fetcherNeedsReset"
- "_getCachedConnection"
- "_getListResults"
- "_getStatusFromReply"
- "_getUidlResults"
- "_handleFlagsChangedForMessages:flags:oldFlagsByMessage:"
- "_hasDoneBackgroundSynchronization"
- "_hidingPassword"
- "_library"
- "_listResults"
- "_mailbox"
- "_messageData"
- "_messageDataIsComplete"
- "_messageID"
- "_messageIdsByNumber"
- "_messageNumber"
- "_newestMessageUID"
- "_numberOfKnownUIDs"
- "_numberOfMessagesAvailable"
- "_numbersByMessageId"
- "_oldestMessageUID"
- "_pass:"
- "_queueAccountInfoDidChange"
- "_readMultilineResponseWithMaxSize:consumer:"
- "_retrieveMessage:ofSize:consumer:"
- "_sendBuffer"
- "_sendCommand:withArguments:"
- "_serverMessageCount"
- "_sharedConnectionCondition"
- "_shouldAttemptAPOP"
- "_size"
- "_state"
- "_uidStore"
- "_user:"
- "account"
- "accountLogString"
- "accountPropertyForKey:"
- "accountTypeIdentifier"
- "accountTypeString"
- "addInvocation:"
- "addItem:"
- "addMessages:withMailbox:newMessagesByOldMessage:remoteIDs:setFlags:addPOPUIDs:dataSectionsByMessage:generationWindow:"
- "addObject:"
- "allKeys"
- "allUIDsInMailbox:"
- "allValues"
- "anyObject"
- "appendBytes:length:"
- "appendData:"
- "authenticateUsingAccount:"
- "authenticateUsingAccount:authenticator:"
- "authenticatedConnection"
- "authenticationMechanisms"
- "authenticationState"
- "authenticatorClass"
- "autofetchAccount:mailboxUid:"
- "b1"
- "b4"
- "bodyDataForMessage:isComplete:isPartial:downloadIfNecessary:"
- "bodyFetchRequiresNetworkActivity"
- "bytes"
- "canAuthenticateAccountClass:connection:"
- "canCreateNewMailboxes"
- "canGoOffline"
- "canMailboxBeRenamed:"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "capabilities"
- "certUIService"
- "checkInConnection:currentUIDs:"
- "clientCertificates"
- "closeCachedConnection"
- "closeCachedConnectionForcedOnly:"
- "closeConnection:andSaveUIDs:"
- "code"
- "compactMessages:permanently:notifyPersistence:"
- "compare:"
- "connectUsingAccount:"
- "connectionClass"
- "connectionClassForAccountClass:"
- "connectionsInUse"
- "containsObject:"
- "contentType"
- "conversationFlags"
- "copy"
- "copyMessageHeaderForMessageNumber:"
- "copyReplyLineData"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "credentialAccessibility"
- "csAccountTypeString"
- "currentMonitor"
- "data"
- "dataConsumerForMessage:part:incomplete:"
- "dataForMimePart:inRange:isComplete:downloadIfNecessary:didDownload:"
- "dataForMimePart:inRange:isComplete:withConsumer:downloadIfNecessary:didDownload:"
- "dataHolderWithData:"
- "dataUsingEncoding:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dateReceived"
- "dateReceivedAsTimeIntervalSince1970"
- "dateWithTimeIntervalSinceNow:"
- "defaultPortNumber"
- "defaultSecurePortNumber"
- "delayedMessageDeletionInterval"
- "dele:"
- "deleteAllUIDs"
- "deleteMessagesOnServer:"
- "deletePOPUID:inMailbox:"
- "deleteUIDsNotInArray:"
- "description"
- "didReflectNewMessages:"
- "disableAPOP"
- "disconnect"
- "doStat"
- "domain"
- "done"
- "ef_publicDescription"
- "enableSSL"
- "encodedHeaders"
- "error"
- "errorWithDomain:code:localizedDescription:"
- "errorWithDomain:code:localizedDescription:title:userInfo:"
- "f"
- "fetchMessages:"
- "fetchMessages:intoQueue:serverIDsByNumber:"
- "fetchNumMessages:preservingUID:options:"
- "fetchNumNewMessages:oldMessages:preservingUID:withStore:"
- "fetchWithAccount:newMessages:oldMessages:preservingUID:withStore:"
- "firstHeaderForKey:"
- "flagsForUID:"
- "flush"
- "fullBodyDataForMessage:andHeaderDataIfReadilyAvailable:isComplete:downloadIfNecessary:usePartDatas:didDownload:"
- "getMessageNumbers:andMessageIdsByNumber:"
- "getMessageNumbers:messageIdsByNumber:numbersByMessageId:"
- "getTop:ofMessageNumber:intoMutableData:"
- "getTopOfMessageNumber:intoMutableData:"
- "gotNewMessagesState"
- "handleItems:"
- "hasEncryption"
- "headerData"
- "headers"
- "headersIfAvailable"
- "hiddenPOPUIDsInMailbox:"
- "hookRegistry"
- "hostname"
- "humanReadableName"
- "idForMessageNumber:"
- "inaccessiblePasswordErrorWithTitle:"
- "indexOfObject:"
- "init"
- "initWithBytes:length:"
- "initWithBytes:length:encoding:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCapacity:"
- "initWithHeaderData:encoding:"
- "initWithLibrary:URLString:"
- "initWithLibrary:persistentAccount:"
- "initWithMailbox:readOnly:"
- "initWithMaximumSize:latency:"
- "initWithName:andDelegate:"
- "initWithName:condition:andDelegate:"
- "initialize"
- "intValue"
- "integerForKey:"
- "isCellularConnection"
- "isEqual:"
- "isEqualToString:"
- "isFatPipe"
- "isFetching"
- "isMainThread"
- "isValid"
- "justSentPlainTextPassword"
- "knownMessageIDsFromSet:"
- "legacyKeychainProtocol"
- "length"
- "library"
- "list:"
- "lock"
- "lockWhenCondition:"
- "log"
- "lowercaseString"
- "mailbox"
- "mailboxPathExtension"
- "mailboxUidOfType:createIfNeeded:"
- "mainThreadScheduler"
- "message"
- "messageChangeManager"
- "messageData"
- "messageData:messageSize:isComplete:downloadIfNecessary:"
- "messageDataHolder"
- "messageDataHolder:messageSize:isComplete:downloadIfNecessary:"
- "messageDataIsComplete:downloadIfNecessary:"
- "messageDeletionPolicy"
- "messageFlags"
- "messageForRemoteID:"
- "messageID"
- "messageIDsAddedBeforeDate:"
- "messageNumber"
- "messageSize"
- "messageWithRemoteID:inRemoteMailbox:"
- "messagesAvailable"
- "messagesWereDeleted:"
- "mf_appendCString:"
- "mf_convertNetworkLineEndingsToUnix"
- "mf_decodeBase64"
- "mf_encodeBase64WithoutLineBreaks"
- "mf_invocationWithSelector:target:object1:object2:"
- "mf_isUserCancelledError"
- "mf_lock"
- "mf_rangeOfCString:options:"
- "mf_rangeOfCString:options:range:"
- "mf_rangeOfRFC822HeaderData"
- "mf_subdataWithRange:"
- "mf_unlock"
- "mimeBody"
- "minusSet:"
- "missingPasswordErrorWithTitle:"
- "mutableCopy"
- "mutableCopyWithZone:"
- "name"
- "newestKnownMessageUID"
- "nonDeletedCountForMailbox:"
- "numberOfKnownUIDs"
- "numberOfMessageIDs"
- "numberOfMessagesAvailable"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "oldestKnownMessageUID"
- "openSynchronouslyUpdatingMetadata:"
- "originalMailboxURL"
- "password"
- "performBlock:"
- "performSelector:withObject:afterDelay:"
- "persistence"
- "persistenceDidAddMessages:generationWindow:"
- "persistenceDidFinishUpdates"
- "persistenceWillBeginUpdates"
- "portNumber"
- "preferredAuthScheme"
- "preferredEncoding"
- "primaryMailboxUid"
- "processRemoteContentFromHeaderData:bodyData:forMessage:"
- "purgeMessages:"
- "purgeMessagesBeyondLimit:"
- "q"
- "q16@0:8"
- "q20@0:8i16"
- "q24@0:8@16"
- "q24@0:8Q16"
- "q32@0:8@16@24"
- "q32@0:8Q16@24"
- "q32@0:8Q16^@24"
- "q32@0:8^@16^@24"
- "q32@0:8r*16@24"
- "q36@0:8i16Q20@28"
- "q40@0:8@16@24@32"
- "q40@0:8Q16@24Q32"
- "q40@0:8Q16Q24@32"
- "q40@0:8^@16^@24^@32"
- "q48@0:8Q16Q24@32@40"
- "q56@0:8@16Q24Q32@40@48"
- "q60@0:8Q16@24@32@40B48^B52"
- "q64@0:8@16@24Q32Q40@48@56"
- "quit"
- "range"
- "readLineIntoData:"
- "recordTransportType:"
- "registerSchemeClass:"
- "releaseAllConnections"
- "releaseAllForcedConnections"
- "remoteID"
- "remoteMailboxURL"
- "removeObjectForKey:"
- "replaceObjectsInRange:withObjectsFromArray:range:"
- "requiresAuthentication"
- "requiresPassword"
- "reset"
- "responseForServerData:"
- "retr:consumer:intoQueue:idsByNumber:allowIncomplete:queueStatus:"
- "retr:data:"
- "retr:dataConsumer:"
- "saslName"
- "saslProfileName"
- "savePersistentAccount"
- "saveState"
- "scheduleDisconnect"
- "schemeWithName:"
- "secureServiceName"
- "securityProtocol"
- "serverMessageCount"
- "serverUnreadOnlyOnServerCount"
- "serviceName"
- "setAccountProperty:forKey:"
- "setAccountURL:"
- "setAuthenticationState:"
- "setClientCertificates:"
- "setCurrentCount:"
- "setDelayedMessageDeletionInterval:"
- "setDisplayName:maxCount:"
- "setError:"
- "setGotNewMessagesState:"
- "setHeader:forKey:"
- "setIsFetching:"
- "setLength:"
- "setMailbox:"
- "setMessageData:"
- "setMessageData:isComplete:"
- "setMessageDeletionPolicy:"
- "setMessageFlags:"
- "setMessageID:"
- "setMessageNumber:"
- "setMessageSize:"
- "setMessageStore:"
- "setNewestKnownMessageUID:"
- "setNumberOfKnownUIDs:"
- "setObject:forKeyedSubscript:"
- "setOldestKnownMessageUID:"
- "setPercentDone:"
- "setPreferredAuthScheme:"
- "setServerMessageCount:"
- "setServerUnreadOnlyOnServerCount:"
- "setServerUnreadOnlyOnServerCount:forMailbox:"
- "setSet:"
- "setShouldAttemptAPOP:"
- "setUserInfoObject:forKey:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithObjects:"
- "setWithSet:"
- "sharedInstance"
- "sharedInvocationQueue"
- "shouldAttemptAPOP"
- "shouldCancel"
- "shouldRestoreMessagesAfterFailedDelete"
- "sizeForItem:"
- "sizeOfMessageNumber:"
- "sortUsingComparator:"
- "standardUserDefaults"
- "startDate"
- "startTLSForAccount:"
- "statisticsKind"
- "store"
- "storeClass"
- "storeClassForMailbox:"
- "stringWithFormat:"
- "subarrayWithRange:"
- "subject"
- "supportsAPOP"
- "supportsAccountType:"
- "supportsPurge"
- "supportsSyncingReadState"
- "timeIntervalSince1970"
- "timeIntervalSinceReferenceDate"
- "topLevelPart"
- "transportType"
- "type"
- "unionSet:"
- "unlock"
- "unlockWithCondition:"
- "unsignedLongValue"
- "uppercaseString"
- "username"
- "usesSSL"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v32@0:8@16@24"
- "v40@0:8@16@24@32"
- "writeData:dontLogBytesInRange:"

```
