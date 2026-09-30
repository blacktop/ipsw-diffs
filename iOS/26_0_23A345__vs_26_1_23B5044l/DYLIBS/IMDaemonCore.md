## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1448.100.1.2.101
-  __TEXT.__text: 0x300034
-  __TEXT.__auth_stubs: 0x5130
-  __TEXT.__objc_methlist: 0x18994
-  __TEXT.__const: 0x5708
-  __TEXT.__cstring: 0x14241
-  __TEXT.__gcc_except_tab: 0x289a8
-  __TEXT.__oslogstring: 0x4abd7
+1450.200.35.2.5
+  __TEXT.__text: 0x303d30
+  __TEXT.__auth_stubs: 0x51a0
+  __TEXT.__objc_methlist: 0x18a84
+  __TEXT.__const: 0x57a8
+  __TEXT.__cstring: 0x143a1
+  __TEXT.__gcc_except_tab: 0x28870
+  __TEXT.__oslogstring: 0x4bba7
   __TEXT.__ustring: 0x32c
   __TEXT.__dlopen_cstrs: 0x246
-  __TEXT.__constg_swiftt: 0x20d4
-  __TEXT.__swift5_typeref: 0x27c0
-  __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x10ff
-  __TEXT.__swift5_fieldmd: 0x138c
+  __TEXT.__constg_swiftt: 0x2118
+  __TEXT.__swift5_typeref: 0x27d6
+  __TEXT.__swift5_builtin: 0x1a4
+  __TEXT.__swift5_reflstr: 0x110f
+  __TEXT.__swift5_fieldmd: 0x13a8
   __TEXT.__swift5_assocty: 0x688
-  __TEXT.__swift5_capture: 0x1140
+  __TEXT.__swift5_capture: 0x11b0
   __TEXT.__swift5_proto: 0x2e4
   __TEXT.__swift5_types: 0x1e0
-  __TEXT.__swift_as_entry: 0x298
-  __TEXT.__swift_as_ret: 0x354
+  __TEXT.__swift_as_entry: 0x29c
+  __TEXT.__swift_as_ret: 0x358
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xcae8
-  __TEXT.__eh_frame: 0x5c9c
-  __TEXT.__objc_classname: 0x3448
-  __TEXT.__objc_methname: 0x4b18c
-  __TEXT.__objc_methtype: 0x9ddb
-  __TEXT.__objc_stubs: 0x2ef40
-  __DATA_CONST.__got: 0x3070
-  __DATA_CONST.__const: 0x61c8
-  __DATA_CONST.__objc_classlist: 0x918
+  __TEXT.__unwind_info: 0xcbb0
+  __TEXT.__eh_frame: 0x5e74
+  __TEXT.__objc_classname: 0x346c
+  __TEXT.__objc_methname: 0x4b534
+  __TEXT.__objc_methtype: 0x9df9
+  __TEXT.__objc_stubs: 0x2f000
+  __DATA_CONST.__got: 0x3068
+  __DATA_CONST.__const: 0x6218
+  __DATA_CONST.__objc_classlist: 0x920
   __DATA_CONST.__objc_catlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x6f8
+  __DATA_CONST.__objc_protolist: 0x708
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf4e8
-  __DATA_CONST.__objc_protorefs: 0x240
+  __DATA_CONST.__objc_selrefs: 0xf580
+  __DATA_CONST.__objc_protorefs: 0x248
   __DATA_CONST.__objc_superrefs: 0x580
   __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__auth_got: 0x28a8
-  __AUTH_CONST.__const: 0x77b8
+  __AUTH_CONST.__auth_got: 0x28e0
+  __AUTH_CONST.__const: 0x7990
   __AUTH_CONST.__cfstring: 0xde40
-  __AUTH_CONST.__objc_const: 0x1eff0
+  __AUTH_CONST.__objc_const: 0x1f0d8
   __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x2e60
-  __AUTH.__data: 0xa78
+  __AUTH.__data: 0xb18
   __DATA.__objc_ivar: 0x10e0
-  __DATA.__data: 0x51e0
-  __DATA.__bss: 0x4d90
+  __DATA.__data: 0x5230
+  __DATA.__bss: 0x4dd0
   __DATA.__common: 0x118
   __DATA_DIRTY.__objc_data: 0x3250
-  __DATA_DIRTY.__data: 0x2120
+  __DATA_DIRTY.__data: 0x2140
   __DATA_DIRTY.__bss: 0x1450
   __DATA_DIRTY.__common: 0x1a8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1CCB55E8-F530-3C69-BB78-67AEED03D775
-  Functions: 12170
-  Symbols:   2886
-  CStrings:  20824
+  UUID: 1074EFCB-D4CC-30D6-813D-664F3D9B99FA
+  Functions: 12257
+  Symbols:   2889
+  CStrings:  20869
 
Symbols:
+ _IMAttachmentsLogHandle
+ _IMDChatLogHandle
+ _IMDMessageStoreLogHandle
+ _IMDatabaseLogHandle
+ _IMOffloadingLogHandle
- _IMMetricsCollectorSensitiveImageReceived
- _IMMetricsCollectorSensitiveImageSent
CStrings:
+ "  => Created new : [IMFileTransfer: %p  state: %ld  sync state: %ld  local path: %@  transferred name: %@  guid: %@  error: %d  total bytes: %d  created: %@ commSafety: %d update reason: %ld]"
+ "  => Updating existing transfer"
+ " => Not sending data, I am a DSDS device and %@ is not enabled for relay"
+ "%@ -> %@"
+ "***Error compressedProtobuf2DataForGroupActionItem called on object %@ %@"
+ "***Error compressedProtobuf2DataForGroupTitleChangeItem called on object %@ %@"
+ "AUTOMATION_HOOK_SNAPNotificationSent"
+ "AUTOMATION_HOOK_SNAPUploadComplete"
+ "Built IMItem from IMDMessageRecordRef: %@[outgoing: %{BOOL}d sender=%@; service=%@; encrypted=%{BOOL}d; handle=%@; destinationCallerID= %@, unformatted=%@; country=%@; roomName='%@'; flags=0x%llx; subject='%@' text='%@' messageID: %lld GUID:'%@' sortID: %lu date:'%f' date-delivered:'%f' date-read:'%f' date-played:'%f' transfer guids: '%@' empty: %{BOOL}d finished: %{BOOL}d sent: %{BOOL}d read: %{BOOL}d delivered: %{BOOL}d scheduleType: %lu, scheduleState: %lu, audio: %{BOOL}d played: %{BOOL}d from-me: %{BOOL}d DD results: %{BOOL}d DD Scanned: %{BOOL}d Downgraded: %{BOOL}d emote: %{BOOL}d expirable: %{BOOL}d expire-state: %d balloon-bundle-id: %@ expressive-send-style-id: %@ time-expressive-send-played: %@ bizIntent: %@ locale: %@ biaReferenceID: %@ error: %d sync-state %lli corrupt: %{BOOL}d shouldSendMeCard: %{BOOL}d isSpam: %{BOOL}d hasUnseenMention: %{BOOL}d threadIdentifier: %@, threadOriginator: %@, replyCountsByPart: %@, isChoros: %{BOOL}d, chorosConversationID: %ld, syndicationRanges: %@, syncedSyndicationRanges: %@, dateEdited: '%f', dateRecovered: '%f', hasGroupActivity: %{BOOL}d, wasDetonated: %{BOOL}d, isSOS: %{BOOL}d, isCritical %{BOOL}d, fallbackHash (len): %llu]"
+ "Calculated hasCancellableScheduledMessage: %{BOOL}d for chat: %@"
+ "Checking if local handle '%@' is in registered URIs: %@"
+ "Determining routing eligibilityisRoutableMessage: %@, canMakeDowngradeRoutingCheck: %@\nmessage: %@\naccount: %@\naccount.service: %@\n"
+ "Error copying chats from grouped handles: %@"
+ "Failed to cancel task request for %s with error: %@"
+ "Found matching alias: %@"
+ "From attachment record, created [IMFileTransfer: %p  state: %ld  sync state: %ld  local path: %@  transferred name: %@  guid: %@  error: %d  total bytes: %d  created: %@ commSafety: %d update reason: %ld]"
+ "Have stored message for guid (%@): %{BOOL}d"
+ "IMDaemonCore_Private.IMDTrustKitDecisioningManager"
+ "IMSpamFilterHelperProtocol"
+ "Invalid account"
+ "Invalid guid"
+ "Junk filtering: TrustKit decisioning skipped because chat has 3+ replies."
+ "Junk filtering: TrustKit decisioning skipped because chat is a business chat."
+ "Junk filtering: TrustKit decisioning skipped because chat is already junk."
+ "Junk filtering: TrustKit decisioning skipped because sender is known/contact."
+ "Local handle '%@' not found in registered URIs"
+ "Low Data Mode because network is ultra constrained"
+ "MarcoLoggingStringForMessageData"
+ "NPSDefaultsChanged"
+ "No chat found for message GUID '%@' or no lastAddressedLocalHandle"
+ "No handle provided to find matching URI"
+ "No message found for message GUID '%@' or no destinationCallerID"
+ "Overriding return val in storeAttachment for Aux transfer %@"
+ "Please tap here to file a radar. This is a serious issue that needs to be identified and addressed."
+ "Processing rich cards media assets of %lu bytes for relay in message: %@, drop rest of the transfer starting from: %@"
+ "Request to store transfer."
+ "Routable message can make downgrade check"
+ "Routable message unable to perform downgrade/routing check. Is the account and service set correctly?"
+ "SNAP sent to %lu recipients"
+ "SNAP upload via legacy API completed"
+ "SNAP upload via modern API completed"
+ "Skipping CTS check"
+ "Stored message for guid (%@): IMMessageItem[outgoing: %{BOOL}d sender=%@; service=%@; encrypted=%{BOOL}d; handle=%@; destinationCallerID= %@, unformatted=%@; country=%@; roomName='%@'; flags=0x%llx; messageID: %lld sortID: %lu date:'%f' date-delivered:'%f' date-read:'%f' date-played:'%f' transfer guids: '%@' empty: %{BOOL}d finished: %{BOOL}d sent: %{BOOL}d read: %{BOOL}d delivered: %{BOOL}d scheduleType: %lu, scheduleState: %lu, audio: %{BOOL}d played: %{BOOL}d from-me: %{BOOL}d DD results: %{BOOL}d DD Scanned: %{BOOL}d Downgraded: %{BOOL}d emote: %{BOOL}d expirable: %{BOOL}d expire-state: %d balloon-bundle-id: %@ expressive-send-style-id: %@ time-expressive-send-played: %@ bizIntent: %@ locale: %@ biaReferenceID: %@ error: %d sync-state %lli corrupt: %{BOOL}d shouldSendMeCard: %{BOOL}d isSpam: %{BOOL}d hasUnseenMention: %{BOOL}d threadIdentifier: %@, threadOriginator: %@, replyCountsByPart: %@, isChoros: %{BOOL}d, chorosConversationID: %ld, syndicationRanges: %@, syncedSyndicationRanges: %@, dateEdited: '%f', dateRecovered: '%f', hasGroupActivity: %{BOOL}d, wasDetonated: %{BOOL}d, isSOS: %{BOOL}d, isCritical %{BOOL}d, fallbackHash (len): %llu]"
+ "T@\"NSMutableSet\",&,N,V_pendingParticipantIDSetsForRemerge"
+ "This is the first incoming message for this group chat. We will kick off a background request in case others in the chat had previously set one before this device was added. toIdentifier: %@, fromIdentifier: %@, chat: %@"
+ "TrustKit"
+ "TrustKit query filtering skipped"
+ "Unable to get callerURI for account: %@"
+ "Updated hasScheduledMessage to: %{BOOL}d"
+ "Updating hasScheduledMessage to: %{BOOL}d for chat: %@"
+ "Updating transfer: [state: %ld -> %ld sync state: %ld -> %ld local path: %@ transferred name: %@ -> %@ guid: %@ -> %@ error: %d -> %d total bytes: %d -> %d created: %@ -> %@ commSafety: %d -> %d update reason: %d -> %d]"
+ "_FZIDType"
+ "_TtC12IMDaemonCore25IMSpamFilterHelperWrapper"
+ "_bestGuessURIFromCanicalizedID"
+ "_findMatchingURI:"
+ "_forwardMessageToPeers:messageType:guid:originalSender:forcedCallerID:hasAttachment:watchOnly:sentToDevices:requiredCapabilities:"
+ "_hasRegisteredLocalPhoneNumberForHandle:"
+ "_pendingParticipantIDSetsForRemerge"
+ "_phoneNumberForRegisteredSimID:"
+ "_remergeChatsWithPendingParticipantIDSets"
+ "_sendingHandleForOutgoingMessageInChat:fromIdentifier:"
+ "account:conference:remoteUser:properties:"
+ "callerURIForMessageGUID:idsAccount:"
+ "chatsWithGroupedHandles:displayName:style:"
+ "com.apple.MobileSMS.SyncedSettings.changed"
+ "compressedProtobuf2DataForGroupActionItem"
+ "compressedProtobuf2DataForGroupTitleChangeItem"
+ "copyChatsWithGroupedHandles:style:displayName:completionHandler:"
+ "existingChatsForGroupedIDs:displayName:style:"
+ "forwardMessageToPeers:messageType:guid:originalSender:forcedCallerID:"
+ "forwardMessageToPeers:messageType:guid:originalSender:forcedCallerID:hasAttachment:watchOnly:"
+ "forwardMessageToPeers:messageType:guid:originalSender:forcedCallerID:watchOnly:"
+ "groupActivity"
+ "handleTrustKitDecisioningForSender:service:trustIndicator:messageBody:myReceiverISOCountryCode:containsOneTimeCode:foundChat:fallbackFilterCategory:fallbackFilterSubCategory:filteringProcessingBlock:processDictCompletionBlock:"
+ "hasDataDetectorResults"
+ "hasMessageHistoryForSpamReport"
+ "hasUnseenMention"
+ "initWithGUIDForSpotlight:flag:context:"
+ "initWithSyncedSettingsManager:spamFilterHelper:"
+ "isCorrupt"
+ "isEmote"
+ "isPlayed"
+ "messageHistoryForSpamReport"
+ "npsDefaultsChanged"
+ "pendingParticipantIDSetsForRemerge"
+ "personCentricIDForChatWithGUID:chatIdentifier:chatStyle:groupID:displayName:lastKnownToBeHybrid:mergeDisplayNames:participantIDs:"
+ "phoneAliasForDominentPhoneAlias:registeredPhoneNumbers:preferredCallerID:CTPhoneNumber:"
+ "populateIMGroupActionItem:withProtobufData:protobuf2Data:"
+ "populateIMGroupTitleChangeItem:withProtobufData:protobuf2Data:"
+ "replyCountsByPart"
+ "setPendingParticipantIDSetsForRemerge:"
+ "setResources:"
+ "shouldSkipTrustKitDecisioningForChat:sender:"
+ "spamFilterHelper"
+ "syncedSyndicationRanges"
+ "updateReason"
+ "v100@0:8@16@24@32@40@48B56@60q68q76@?84@?92"
+ "v56@0:8@16q24@32@40@48"
+ "v64@0:8@16q24@32@40@48B56B60"
+ "v80@0:8@16q24@32@40@48B56B60^@64@72"
+ "wasDataDetected"
- "  => Created new : %@"
- "  => Updating existing : %@"
- "  => Updating existing: %@ with: %@"
- "<>"
- "<> "
- "<IMFindAccountProcessingPipelineComponent> Has replication source %@ but feature flag disabled, dropping message"
- "Built IMItem: %@    from IMDMessageRecordRef: %@"
- "Calculated hasCancellableScheduledMessage: %@ for chat: %@"
- "Chat already already filtered as: %lld"
- "Created: %@ from attachment record: %@"
- "Failed to submit task request for %{public}s with error: %@"
- "Have stored message for guid (%@): %@"
- "Message is SOS, should ignore do not disturb"
- "Offloading"
- "Over ridiing return val in storeAttachment for Aux transfer %@"
- "Request for attachment with attachmentRecord: %@"
- "Request to store transfer: %@"
- "Stored message for guid (%@): %@"
- "T@\"NSString\",&,N,V_originalAlias"
- "TrustKit chat marked as Junk: %@"
- "TrustKit query filtering skipped because chat 3+ replies"
- "TrustKit query skipped because chat 3+ replies"
- "TrustKit query skipped because chat has 3+ replies or message was read."
- "Updated hasScheduledMessage to: %@"
- "Updating %@ from %@"
- "Updating hasCancellableScheduledMessage state for chat: %@"
- "Updating hasScheduledMessage to: %@"
- "_extractSMSSenderAddress:"
- "_forwardMessageToPeers:messageType:guid:originalSender:hasAttachment:watchOnly:sentToDevices:requiredCapabilities:"
- "_originalAlias"
- "canMarkPurgeableIfIsRichLink:"
- "canMarkPurgeableIfIsRichLinkForTransferGUID:"
- "canMarkPurgeableIfIsRichLinkForTransferGUID: %@ file: [%@], hideAttachment: [%@], bundleID: [%@] purgeable: [%@]"
- "characterSetWithCharactersInString:"
- "chat:groupIDUpdated:"
- "chat:originalGroupIDUpdated:"
- "forwardMessageToPeers:messageType:guid:originalSender:"
- "forwardMessageToPeers:messageType:guid:originalSender:hasAttachment:watchOnly:"
- "forwardMessageToPeers:messageType:guid:originalSender:watchOnly:"
- "initWithGUID:flag:spotlightReason:userInfo:"
- "isPriusCompatibilityEnabled"
- "isPriusEnabled"
- "isReplicationEnabled"
- "isSOSAlertingEnabled"
- "isScheduledMessagesCoreEnabled"
- "isScheduledMessagesEnabled"
- "junkFilteringSettingObserver"
- "originalAlias"
- "personCentricIDForChatWithGUID:chatIdentifier:chatStyle:groupID:displayName:lastKnownToBeHybrid:mergeDisplayNames:participantIDs:mergeFilteredThreads:"
- "phoneAliasForDominentPhoneAlias:registeredPhoneNumber:preferedCallerID:CTPhoneNumber:"
- "populateIMGroupActionItem:withProtobufData:"
- "populateIMGroupTitleChangeItem:withProtobufData:"
- "setOriginalAlias:"
- "v48@0:8@16q24@32@40"
- "v52@0:8@16q24@32@40B48"
- "v56@0:8@16q24@32@40B48B52"
- "v72@0:8@16q24@32@40B48B52^@56@64"

```
