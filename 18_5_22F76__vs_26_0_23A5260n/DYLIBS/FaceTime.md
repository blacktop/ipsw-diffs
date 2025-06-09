## FaceTime

> `/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime`

```diff

-1402.600.41.2.8
-  __TEXT.__text: 0x22cd4
+1436.100.6.2.12
+  __TEXT.__text: 0x1f28c
   __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x1964
+  __TEXT.__objc_methlist: 0x1134
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x1770
-  __TEXT.__cstring: 0x37c4
-  __TEXT.__oslogstring: 0x2393
-  __TEXT.__unwind_info: 0x548
-  __TEXT.__objc_classname: 0x396
-  __TEXT.__objc_methname: 0x421b
-  __TEXT.__objc_methtype: 0x1b44
+  __TEXT.__gcc_except_tab: 0x17fc
+  __TEXT.__cstring: 0x1d16
+  __TEXT.__oslogstring: 0x2a03
+  __TEXT.__unwind_info: 0x588
+  __TEXT.__objc_classname: 0x12a
+  __TEXT.__objc_methname: 0x299e
+  __TEXT.__objc_methtype: 0xaa4
   __TEXT.__objc_stubs: 0x2620
   __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x60
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfa8
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x3100
-  __AUTH_CONST.__objc_const: 0x27b8
+  __AUTH_CONST.__cfstring: 0x21c0
+  __AUTH_CONST.__objc_const: 0x2080
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x188
-  __DATA.__data: 0x840
+  __DATA.__data: 0x180
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x30

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
+  - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B86105B8-4EC3-3B6E-9C2D-230C4947E74E
-  Functions: 380
+  UUID: 28DCB51F-0493-3DCA-87DB-3F72AA7A087C
+  Functions: 382
   Symbols:   180
-  CStrings:  1826
+  CStrings:  1329
 
Symbols:
+ _IMGetDaemonListenerProtocol
+ _IMLogHandleForCategory
- __IMLoggingLog
- __IMWarn
CStrings:
- "%s (%@)"
- "-[FaceTimeServiceSession _sendRejectToPeerID:peerToken:sessionToken:callType:reason:clientInfo:]"
- "-[FaceTimeServiceSession handler:incomingMessage:topic:peerID:reason:clientInfo:serviceData:]"
- "-[FaceTimeServiceSession handler:relayCancelled:topic:peerID:relayType:relayTokenAllocReq:relayConnectionID:relayTransactionIDAlloc:relayCandidateID:myRelayIP:myRelayPort:peerRelayIP:peerRelayPort:reason:clientInfo:serviceData:]"
- "-[FaceTimeServiceSession handler:relayInitiated:topic:peerID:peerPushToken:relayType:relayConnectionID:relayTransactionIDAlloc:relayTokenAllocReq:relayCandidateID:myRelayIP:myRelayPort:peerRelayIP:peerRelayPort:clientInfo:serviceData:]"
- "-[FaceTimeServiceSession handler:relayUpdated:topic:peerID:peerPushToken:relayType:relayConnectionID:relayTransactionIDChannelBind:relayTokenChannelBind:relayCandidateID:relayBlob:peerRelayNATIP:peerRelayNATPort:clientInfo:serviceData:]"
- "-[FaceTimeServiceSession handler:sessionAccepted:topic:peerID:peerCN:peerPushToken:peerNATType:peerBlob:peerNatIP:relayType:relayConnectionID:relayTransactionIDAlloc:relayTokenAllocReq:myRelayIP:myRelayPort:peerRelayIP:peerRelayPort:clientInfo:serviceData:]"
- "-[FaceTimeServiceSession handler:sessionCancelled:topic:peerID:reason:clientInfo:serviceData:]"
- "-[FaceTimeServiceSession handler:sessionInitated:topic:myID:peerID:peerDisplayID:peerCN:peerPushToken:peerNATType:peerBlob:peerNatIP:clientInfo:serviceData:]"
- "-[FaceTimeServiceSession handler:sessionRejected:topic:peerID:peerPushToken:reason:clientInfo:serviceData:]"
- "IMDaemonListenerAVProtocol"
- "IMDaemonListenerAccountsProtocol"
- "IMDaemonListenerAnyProtocol"
- "IMDaemonListenerChatCountsProtocol"
- "IMDaemonListenerChatDatabaseProtocol"
- "IMDaemonListenerChatMessageHistoryProtocol"
- "IMDaemonListenerChatProtocol"
- "IMDaemonListenerCloudSyncProtocol"
- "IMDaemonListenerCollaborationProtocol"
- "IMDaemonListenerFileProviderProtocol"
- "IMDaemonListenerFileTransfersProtocol"
- "IMDaemonListenerKeyTransparencyProtocol"
- "IMDaemonListenerNotificationsProtocol"
- "IMDaemonListenerProtocol"
- "IMDaemonListenerRemoteIntentProtocol"
- "IMDaemonListenerServiceProtocol"
- "IMDaemonListenerSetupProtocol"
- "IMDaemonListenerSyncedSettingsProtocol"
- "_automation_markAsReadQuery:finishedWithResult:"
- "account:allowListChanged:"
- "account:avAction:withArguments:toAVChat:isVideo:"
- "account:blockIdleStatusChanged:"
- "account:blockListChanged:"
- "account:blockingModeChanged:"
- "account:buddyPictureChanged:imageData:imageHash:"
- "account:buddyProperties:buddyPictures:"
- "account:buddyPropertiesChanged:"
- "account:chat:style:chatProperties:chatPersonCentricID:member:statusChanged:"
- "account:chat:style:chatProperties:error:"
- "account:chat:style:chatProperties:groupID:chatPersonCentricID:initialEmergencyQuestionnaireReceived:"
- "account:chat:style:chatProperties:groupID:chatPersonCentricID:messageReceived:"
- "account:chat:style:chatProperties:groupID:chatPersonCentricID:messageSent:"
- "account:chat:style:chatProperties:groupID:chatPersonCentricID:messagesReceived:removed:messagesComingFromStorage:"
- "account:chat:style:chatProperties:groupID:chatPersonCentricID:statusChanged:handleInfo:"
- "account:chat:style:chatProperties:invitationReceived:"
- "account:chat:style:chatProperties:updateProperties:"
- "account:chat:style:messageUpdated:"
- "account:chat:style:messageUpdated:suppressNotification:"
- "account:chat:style:messagesUpdated:"
- "account:chat:style:notifySentMessage:sendTime:isReplicating:"
- "account:conference:receivedCounterProposalFrom:properties:"
- "account:conference:receivedUpdateFrom:data:"
- "account:defaults:blockList:allowList:blockingMode:blockIdleStatus:status:capabilities:serviceLoginStatus:loginStatusMessage:"
- "account:defaultsChanged:"
- "account:groupsChanged:error:"
- "account:handleID:updatedLastReceivedOnGridMessageDate:"
- "account:handleSubscriptionRequestFrom:withMessage:"
- "account:loginStatusChanged:message:reason:properties:"
- "account:statusChanged:"
- "accountAdded:defaults:service:"
- "accountRemoved:"
- "activeAccountsChanged:forService:"
- "attachmentQuery:chatID:services:finishedWithResult:"
- "blackholedChatsExist:"
- "capabilitiesUpdatedForHandle:"
- "chat:brandLogoUpdated:transferGuid:"
- "chat:chatPersonCentricID:displayNameUpdated:"
- "chat:chatPersonCentricID:displayNameUpdated:sender:"
- "chat:engramIDUpdated:"
- "chat:isDeletingIncomingMessagesUpdated:"
- "chat:isFilteredUpdated:"
- "chat:isRecoveredUpdated:"
- "chat:lastAddressedHandleUpdated:"
- "chat:lastAddressedHandleUpdated:lastAddressedSIMIDUpdated:"
- "chat:lastAddressedSIMIDUpdated:"
- "chat:lastMessageTimeStampOnLoadUpdated:"
- "chat:nicknamesUpdated:"
- "chat:propertiesUpdated:"
- "chat:uncachedAttachmentCountUpdated:"
- "chat:updated:"
- "chatLoadedWithChatIdentifier:chats:"
- "chatsNeedRemerging:groupedChats:"
- "collaborationNoticesDidChangeForChatGUIDs:"
- "databaseChatSpamUpdated:"
- "databaseUpdated"
- "databaseUpdated:"
- "defaultsChanged:forService:"
- "didAttemptToDisableAllDevicesResult:"
- "didAttemptToDisableiCloudBackups:error:"
- "didAttemptToSetEnabledTo:result:"
- "didFetchCloudKitSyncDebuggingInfo:"
- "didFetchRampState:"
- "didFetchSyncStateStats:"
- "didPerformAdditionalStorageRequiredCheckWithSuccess:additionalStorageRequired:forAccountId:error:"
- "didReceiveCollaborationMessage:inChat:style:account:"
- "didUpdateSettingsKeys:"
- "displayPinCodeForAccount:pinCode:deviceName:deviceType:phoneNumber:"
- "downloadedPurgedAssetBatchForChatIDs:completedTransferGUIDs:"
- "engroupParticipantsUpdatedForChat:"
- "fileTransfer:createdWithProperties:"
- "fileTransfer:explicitDownloadSucceededWithPath:livePhotoBundlePath:"
- "fileTransfer:highQualityDownloadSucceededWithPath:"
- "fileTransfer:updatedWithCurrentBytes:totalBytes:averageTransferRate:"
- "fileTransfer:updatedWithProperties:"
- "fileTransferDownloadFailedWithLocalURL:error:"
- "fileTransferDownloadedSucceededWithLocalURL:"
- "fileTransferExplicitDownloadFailed:suggestedRetryGUID:error:"
- "fileTransferFinishedRemoteIntentDownload:"
- "fileTransferHighQualityDownloadFailed:"
- "fileTransfers:createdWithLocalPaths:"
- "finishedDownloadingPurgedAssetsForChatIDs:"
- "forcedReloadingChatRegistryWithQueryID:"
- "frequentRepliesQuery:chatID:services:finishedWithResult:limit:"
- "groupPhotoUpdatedForChatIdentifier:style:account:userInfo:"
- "historicalMessageGUIDsDeleted:chatGUIDs:queryID:"
- "historyQuery:chatID:services:finishedWithResult:limit:"
- "isDownloadingQuery:chatID:services:finishedWithResult:"
- "itemQuery:finishedWithResult:chatGUIDs:"
- "keyTransparencyOptInStateChanged:"
- "lastFailedMessageDateChanged:"
- "leftChat:"
- "loadedChats:"
- "loadedChats:queryID:"
- "loadedRecoverableMessagesMetadata:queryID:"
- "markAsSpamQuery:chatID:services:finishedWithResult:"
- "markedAsReadForMessageGUID:success:queryID:"
- "messageItemQuery:finishedWithResult:chatGUIDs:"
- "messageQuery:finishedWithResult:chatGUIDs:"
- "movedMessageGUIDsToRecentlyDeleted:forChatWithGUID:queryID:deletionDate:"
- "movedMessagesToRecentlyDeletedForChatsWithGUIDs:queryID:deletionDate:"
- "networkDataAvailabilityChanged:"
- "newSetupInfoAvailable"
- "nicknameRequestResponse:encodedNicknameData:"
- "oneTimeCodesDidChange:"
- "pagedHistoryQuery:chatID:services:numberOfMessagesBefore:numberOfMessagesAfter:finishedWithResult:hasMessagesBefore:hasMessagesAfter:"
- "pendingACRequestComplete"
- "pendingVCRequestComplete"
- "permanentlyDeletedMessagesInChatsWithDeletedChatGUIDs:"
- "permanentlyDeletedMessagesInChatsWithDeletedChatGUIDs:queryID:"
- "permanentlyDeletedRecoverableMessagesForChatsWithGUIDs:deletedChatGUIDs:"
- "persistentProperty:changedTo:from:"
- "pinCodeAlertCompleted:deviceName:deviceType:phoneNumber:responseFromDevice:wasCancelled:"
- "previouslyBlackholedChatLoadedWithChatIdentifier:chats:"
- "previouslyBlackholedChatLoadedWithHandleIDs:chat:"
- "property:changedTo:from:"
- "qosClassWhileServicingRequestsResponse:identifier:"
- "receivedUrgentRequestForMessages:"
- "recoveredMessagesFromRecentlyDeletedForChatsWithGUIDs:"
- "recoveredMessagesWithChatGUIDs:queryID:"
- "refreshStatusForKTPeerURI:"
- "screenTimeEnablementChanged:"
- "service:chat:style:messagesUpdated:"
- "serviceSwitchRequestReceivedForChatWithIdentifier:"
- "setupComplete"
- "setupComplete:info:"
- "showForgotPasswordNotificationForAccount:"
- "showInvalidCertNotificationForAccount:"
- "simSubscriptionsDidChange"
- "stickerPackRemoved:"
- "stickerPackUpdated:"
- "uncachedAttachmentCountQuery:chatID:services:finishedWithResult:"
- "unreadCountChanged:"
- "updateActiveNicknameRecords:"
- "updateCloudKitProgressWithDictionary:"
- "updateCloudKitState"
- "updateCloudKitStateWithDictionary:"
- "updateIgnoredNicknameRecords:"
- "updateNicknameData:"
- "updateNicknameHandlesForSharing:blocked:"
- "updatePendingNicknameUpdates:handledNicknames:archivedNicknames:"
- "updatePersonalNickname:"
- "updateTransitionedNicknameHandles:"
- "updateUnknownSenderRecords:"
- "updatedSummariesForChatsWithGUIDsAndProperties:"
- "v24@0:8@\"IMNickname\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSURL\"16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8@\"NSString\"16B24"
- "v28@0:8@\"NSString\"16I24"
- "v28@0:8@16I24"
- "v28@0:8B16@\"NSDictionary\"20"
- "v28@0:8B16@20"
- "v28@0:8I16@\"NSString\"20"
- "v28@0:8I16@20"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"NSArray\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
- "v32@0:8@\"NSSet\"16@\"NSSet\"24"
- "v32@0:8@\"NSString\"16@\"NSArray\"24"
- "v32@0:8@\"NSString\"16@\"NSData\"24"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@\"NSError\"24"
- "v32@0:8@\"NSString\"16@\"NSNumber\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16Q24"
- "v32@0:8@\"NSString\"16d24"
- "v32@0:8@\"NSString\"16q24"
- "v32@0:8@\"NSURL\"16@\"NSError\"24"
- "v32@0:8@16Q24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v32@0:8q16@\"NSError\"24"
- "v32@0:8q16@24"
- "v36@0:8@\"NSString\"16@\"NSString\"24B32"
- "v36@0:8@\"NSString\"16B24@\"NSString\"28"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@28"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@\"NSString\"32"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@\"NSDate\"32"
- "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16@\"IMItem\"24@\"NSArray\"32"
- "v40@0:8@\"NSString\"16@\"IMMessageItem\"24@\"NSArray\"32"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@\"NSError\"32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDate\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSError\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16@24@32"
- "v44@0:8@\"IMMessageItem\"16@\"NSString\"24C32@\"NSString\"36"
- "v44@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32B40"
- "v44@0:8@\"NSString\"16@\"NSString\"24C32@\"IMItem\"36"
- "v44@0:8@\"NSString\"16@\"NSString\"24C32@\"NSArray\"36"
- "v44@0:8@\"NSString\"16C24@\"NSString\"28@\"NSDictionary\"36"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16@24C32@36"
- "v44@0:8@16C24@28@36"
- "v44@0:8B16Q20@\"NSString\"28@\"NSError\"36"
- "v44@0:8B16Q20@28@36"
- "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSDate\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@\"NSArray\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@\"NSNumber\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSData\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSDictionary\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24C32@\"IMItem\"36B44"
- "v48@0:8@\"NSString\"16I24@\"NSDictionary\"28@\"NSString\"36B44"
- "v48@0:8@\"NSString\"16Q24Q32Q40"
- "v48@0:8@16@24C32@36B44"
- "v48@0:8@16I24@28@36B44"
- "v48@0:8@16Q24Q32Q40"
- "v52@0:8@\"NSString\"16@\"NSString\"24C32@\"NSDictionary\"36@\"IMMessageItem\"44"
- "v52@0:8@\"NSString\"16@\"NSString\"24C32@\"NSDictionary\"36@\"NSDictionary\"44"
- "v52@0:8@\"NSString\"16@\"NSString\"24C32@\"NSDictionary\"36@\"NSError\"44"
- "v52@0:8@\"NSString\"16Q24@\"NSString\"32i40@\"NSDictionary\"44"
- "v52@0:8@16@24C32@36@44"
- "v52@0:8@16Q24@32i40@44"
- "v56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@\"NSArray\"40q48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40B48B52"
- "v56@0:8@\"NSString\"16@\"NSString\"24C32@\"IMMessageItem\"36@\"NSNumber\"44B52"
- "v56@0:8@\"NSString\"16@\"NSString\"24I32@\"NSDictionary\"36I44@\"NSDictionary\"48"
- "v56@0:8@16@24@32@40B48B52"
- "v56@0:8@16@24@32@40q48"
- "v56@0:8@16@24C32@36@44B52"
- "v56@0:8@16@24I32@36I44@48"
- "v64@0:8@\"NSString\"16@\"NSString\"24C32@\"NSDictionary\"36@\"NSString\"44@\"NSDictionary\"52i60"
- "v64@0:8@16@24C32@36@44@52i60"
- "v68@0:8@\"NSString\"16@\"NSString\"24C32@\"NSDictionary\"36@\"NSString\"44@\"NSString\"52@\"IMItem\"60"
- "v68@0:8@\"NSString\"16@\"NSString\"24C32@\"NSDictionary\"36@\"NSString\"44@\"NSString\"52@\"IMMessageItem\"60"
- "v68@0:8@16@24C32@36@44@52@60"
- "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32q40q48@\"NSArray\"56B64B68"
- "v72@0:8@\"NSString\"16@\"NSString\"24C32@\"NSDictionary\"36@\"NSString\"44@\"NSString\"52i60@\"NSArray\"64"
- "v72@0:8@16@24@32q40q48@56B64B68"
- "v72@0:8@16@24C32@36@44@52i60@64"
- "v80@0:8@\"NSString\"16@\"NSString\"24C32@\"NSDictionary\"36@\"NSString\"44@\"NSString\"52@\"NSArray\"60@\"NSArray\"68B76"
- "v80@0:8@16@24C32@36@44@52@60@68B76"
- "v88@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSArray\"32@\"NSArray\"40I48B52@\"NSDictionary\"56Q64Q72@\"NSString\"80"
- "v88@0:8@16@24@32@40I48B52@56Q64Q72@80"
- "vcCapabilitiesChanged:"

```
