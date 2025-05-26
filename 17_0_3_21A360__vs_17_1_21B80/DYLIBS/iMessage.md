## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1261.100.4.2.35
-  __TEXT.__text: 0xa18b8
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x1ee4
+1261.200.71.2.16
+  __TEXT.__text: 0xa1fcc
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_methlist: 0x1eec
   __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x7ecc
-  __TEXT.__cstring: 0x10ab5
-  __TEXT.__oslogstring: 0x12c58
-  __TEXT.__unwind_info: 0x1b30
+  __TEXT.__gcc_except_tab: 0x7f34
+  __TEXT.__cstring: 0x10b0f
+  __TEXT.__oslogstring: 0x12cf3
+  __TEXT.__unwind_info: 0x1b5c
   __TEXT.__objc_classname: 0x47b
-  __TEXT.__objc_methname: 0xe3e2
-  __TEXT.__objc_methtype: 0x2456
+  __TEXT.__objc_methname: 0xe40a
+  __TEXT.__objc_methtype: 0x243b
   __TEXT.__objc_stubs: 0xa1c0
-  __DATA_CONST.__got: 0x818
-  __DATA_CONST.__const: 0x1f50
+  __DATA_CONST.__got: 0x898
+  __DATA_CONST.__const: 0x1fc8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2508
-  __DATA_CONST.__objc_selrefs: 0x2c28
+  __DATA_CONST.__objc_selrefs: 0x2c30
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__cfstring: 0xb8a0
+  __AUTH_CONST.__cfstring: 0xb880
   __AUTH_CONST.__objc_const: 0x9e0
   __AUTH_CONST.__const: 0x6a0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x6b0
+  __AUTH_CONST.__auth_got: 0x6b8
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_classrefs: 0x418
   __DATA.__objc_superrefs: 0x88

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1143
-  Symbols:   648
-  CStrings:  4884
+  Functions: 1138
+  Symbols:   665
+  CStrings:  4885
 
Symbols:
+ _MessageDictionaryArchivedNicknameUpdatesRecordIDsKey
+ _MessageDictionaryCurrentNicknameUpdatesRecordIDsKey
+ _MessageDictionaryNicknameActiveListKey
+ _MessageDictionaryNicknameActiveListVersionKey
+ _MessageDictionaryNicknameCloudKitDecryptionRecordKey
+ _MessageDictionaryNicknameCloudKitRecordKey
+ _MessageDictionaryNicknameIgnoredListKey
+ _MessageDictionaryNicknameIgnoredListVersionKey
+ _MessageDictionaryNicknameRequestPersonalNicknameInfoKey
+ _MessageDictionaryNicknameTransitionedListKey
+ _MessageDictionaryNicknameTransitionedListVersionKey
+ _MessageDictionaryNicknameUpdateInfoIncluded
+ _MessageDictionaryPendingNicknameUpdatesHandlesKey
+ _MessageDictionaryPendingNicknameUpdatesRecordIDsKey
+ _MessageDictionaryWallpaperUpdateKey
+ _NSCocoaErrorDomain
+ _im_primary_queue
CStrings:
+ "   isTypingIndicator: %@"
+ " => completed transfer had nil or missing localURL: %@"
+ " Dropping error on the floor, sometimes we get through here and the attachment download has magically disappeared from tmp"
+ "Failed to find a chat for chatGUID: %@"
+ "Ignoring nickname update (profile: %p) (error: %@)"
+ "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:completionBlock:"
+ "_handleNicknameReceived:fromIdentifier:withMessageItem:"
+ "_nicknameFetchCompletedMessage:synchronous:profile:nickNameWasInCache:nickNameDownloadError:"
+ "_requestGroupPhotoResendForChatGUID:fromIdentifier:toIdentifier:"
+ "transcribeMessageIfNeeded:forTransfer:completion:"
+ "v200@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104B108B112@116@124@132@140@148@156@164@172@180B188@?192"
+ "v48@0:8@16B24@28B36@40"
- "   isEncrypted: %@"
- " => completed transfer had nil localURL: %@"
- "CloudKitDecryptionRecordKey"
- "CloudKitRecordKey"
- "Ignoring nickname update (isTypingIndicator: %@) (profile: %p) (error: %@)"
- "WallpaperUpdateKey"
- "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isEncrypted:isFromMe:isLastFromStorage:isFromStorage:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:completionBlock:"
- "_handleNicknameReceived:fromIdentifier:isEncrypted:withMessageItem:"
- "_nicknameFetchCompletedMessage:synchronous:isEncrypted:profile:nickNameWasInCache:nickNameDownloadError:"
- "transcribeMessageIfNeeded:forTransfer:"
- "v204@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104B108B112B116@120@128@136@144@152@160@168@176@184B192@?196"
- "v44@0:8@16@24B32@36"
- "v52@0:8@16B24B28@32B40@44"

```
