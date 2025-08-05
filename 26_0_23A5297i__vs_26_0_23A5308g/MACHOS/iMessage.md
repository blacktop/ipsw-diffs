## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1445.100.6.2.4
-  __TEXT.__text: 0xb6ed0
-  __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_stubs: 0xbda0
-  __TEXT.__objc_methlist: 0x2934
+1447.100.7.2.3
+  __TEXT.__text: 0xb906c
+  __TEXT.__auth_stubs: 0x1ab0
+  __TEXT.__objc_stubs: 0xc3e0
+  __TEXT.__objc_methlist: 0x2b64
   __TEXT.__const: 0xbb0
-  __TEXT.__gcc_except_tab: 0xb3c4
-  __TEXT.__cstring: 0x33ad
-  __TEXT.__oslogstring: 0x16256
-  __TEXT.__objc_classname: 0x50a
-  __TEXT.__objc_methname: 0x11bfa
-  __TEXT.__objc_methtype: 0x290b
+  __TEXT.__gcc_except_tab: 0xb4d0
+  __TEXT.__cstring: 0x339d
+  __TEXT.__oslogstring: 0x163e6
+  __TEXT.__objc_classname: 0x548
+  __TEXT.__objc_methname: 0x12401
+  __TEXT.__objc_methtype: 0x2955
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x640
   __TEXT.__constg_swiftt: 0x36c

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2298
-  __TEXT.__eh_frame: 0x680
-  __DATA_CONST.__auth_got: 0xd60
-  __DATA_CONST.__got: 0xfd0
+  __TEXT.__unwind_info: 0x2300
+  __TEXT.__eh_frame: 0x740
+  __DATA_CONST.__auth_got: 0xd68
+  __DATA_CONST.__got: 0xfd8
   __DATA_CONST.__auth_ptr: 0x170
-  __DATA_CONST.__const: 0x3790
+  __DATA_CONST.__const: 0x37c0
   __DATA_CONST.__cfstring: 0x36c0
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x390
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x2e38
-  __DATA.__objc_selrefs: 0x3830
-  __DATA.__objc_ivar: 0x1d0
-  __DATA.__objc_data: 0x9b8
-  __DATA.__data: 0xa38
+  __DATA.__objc_const: 0x32a8
+  __DATA.__objc_selrefs: 0x39c0
+  __DATA.__objc_ivar: 0x214
+  __DATA.__objc_data: 0xa58
+  __DATA.__data: 0xa40
   __DATA.__bss: 0x7b0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 34ED80D1-5E0F-3BAB-85F5-AC775C825A1D
-  Functions: 1590
-  Symbols:   850
-  CStrings:  4943
+  UUID: 51BCB8FE-9344-3843-B210-69537E1A1C2D
+  Functions: 1641
+  Symbols:   855
+  CStrings:  5039
 
Symbols:
+ _IMAnyServiceGUIDFromLegacyChatGUID
+ _OBJC_CLASS_$_GroupConvergenceContext
+ _OBJC_CLASS_$_GroupParticipantConvergenceResult
+ _OBJC_CLASS_$_IMDChatMemberStatusChangeContext
+ _OBJC_METACLASS_$_GroupConvergenceContext
+ _OBJC_METACLASS_$_GroupParticipantConvergenceResult
- __ConvergeGroupParticipants
CStrings:
+ "%@\n\n%@"
+ "@32@0:8Q16@24"
+ "C"
+ "C16@0:8"
+ "Could not find message part at index %ld"
+ "Failed to format translation prefix: %@"
+ "Failed to unarchive translated message parts: %@"
+ "GroupConvergenceContext"
+ "GroupParticipantConvergenceResult"
+ "Ignoring group photo because it is for a placeholder chat"
+ "Invalid translation data for part %ld"
+ "Received GenericGroupCommand from someone who is not in the group. fromIdentifier: %@ chatGuid: %@"
+ "T@\"IMDAccount\",&,N,V_account"
+ "T@\"NSArray\",&,N,V_currentParticipants"
+ "T@\"NSArray\",&,N,V_participantsToAdd"
+ "T@\"NSArray\",&,N,V_participantsToRemove"
+ "T@\"NSArray\",&,N,V_toParticipants"
+ "T@\"NSArray\",R,N,V_chatStatusChanges"
+ "T@\"NSArray\",R,N,V_memberStatusChanges"
+ "T@\"NSDictionary\",&,N,V_participantChangeGUIDs"
+ "T@\"NSString\",&,N,V_chatIdentifier"
+ "T@\"NSString\",&,N,V_fromIdentifier"
+ "T@\"NSString\",&,N,V_groupID"
+ "T@\"NSString\",&,N,V_messageID"
+ "T@\"NSString\",&,N,V_toIdentifier"
+ "TB,N,V_allowSelfRemoval"
+ "TB,N,V_isBlackholed"
+ "TB,N,V_isReflection"
+ "TC,N,V_chatStyle"
+ "We've already created a status item for this transfer, and the new one is hidden. Don't process as we won't handle it later anyway. transferGuid: %@, itemGuid: %@"
+ "__im_messageTextByReplacingMessagePartIndex:withNewPartText:"
+ "_allowSelfRemoval"
+ "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:batchContext:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:wasContextUsed:isBlackholed:shouldTrackForRequery:isFiltered:spamDetectionSource:completionBlock:"
+ "_chatIdentifier"
+ "_chatStatusChanges"
+ "_chatStyle"
+ "_currentParticipants"
+ "_fromIdentifier"
+ "_groupID"
+ "_handleGroupVisualIdentityRequest:fromParticipants:groupID:fromIdentifier:session:toIdentifier:fromToken:requestGUID:isReflection:"
+ "_isBlackholed"
+ "_isReflection"
+ "_memberStatusChanges"
+ "_messageID"
+ "_messageIDForUpdateType:participant:"
+ "_participantChangeGUIDs"
+ "_participantsToAdd"
+ "_participantsToRemove"
+ "_processParticipantConvergenceResult:forChat:"
+ "_stringSubDictionaryOfDictionary:forKey:"
+ "_toIdentifier"
+ "_toParticipants"
+ "_validateChat:containsFromIdentifier:isReflection:"
+ "allowSelfRemoval"
+ "chatStatusChangeContextForUpdateType:participant:"
+ "chatStatusChanges"
+ "currentParticipants"
+ "dictionaryForHandlesToGUIDsFromHandleInfo:"
+ "didChangeMemberStatus:"
+ "didJoinChat:style:displayName:groupID:handleInfo:category:account:isBlackholed:spamDetectionSource:"
+ "didUpdateChatStatusWithContext:"
+ "ept"
+ "groupParticipantConvergenceResultForUpdateType:context:"
+ "initWithChat:"
+ "initWithMemberStatusChanges:chatStatusChanges:"
+ "isEqualToArray:"
+ "isLQMEnabled:"
+ "isPlaceholder"
+ "isReflection"
+ "memberStatusChangeContextForUpdateType:participant:"
+ "memberStatusChanges"
+ "messagePartIndex"
+ "participantChangeGUIDs"
+ "participantsToAdd"
+ "participantsToRemove"
+ "pig"
+ "setAllowSelfRemoval:"
+ "setChatIdentifier:"
+ "setChatStatus:"
+ "setChatStyle:"
+ "setCountryCode:"
+ "setCurrentParticipants:"
+ "setFromHandleID:"
+ "setFromIdentifier:"
+ "setHandleID:"
+ "setIsReflection:"
+ "setMessageID:"
+ "setParticipantChangeGUIDs:"
+ "setParticipantsToAdd:"
+ "setParticipantsToRemove:"
+ "setStatus:"
+ "setStyle:"
+ "setToIdentifier:"
+ "setToParticipants:"
+ "setUnattributed:"
+ "setUnformattedNumber:"
+ "toParticipants"
+ "v20@0:8C16"
+ "v256@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104@108B116B120@124@132@140@148@156@164@172@180@188@196@204B212B216B220B224B228q232q240@?248"
+ "v84@0:8@16@24@32@40@48@56@64@72B80"
- "%@%@"
- "Attempting to send group photo to someone who is not in the group. toIdentifier: %@ chatGuid: %@"
- "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:batchContext:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:wasContextUsed:isBlackholed:shouldTrackForRequery:isFiltered:completionBlock:"
- "_handleGroupVisualIdentityRequest:fromParticipants:groupID:identifier:session:toIdentifier:fromToken:requestGUID:"
- "didJoinChat:style:displayName:groupID:handleInfo:category:account:isBlackholed:"
- "v248@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104@108B116B120@124@132@140@148@156@164@172@180@188@196@204B212B216B220B224B228q232@?240"

```
