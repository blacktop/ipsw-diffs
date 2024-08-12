## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1303.100.13.0.0
-  __TEXT.__text: 0x905e0
-  __TEXT.__auth_stubs: 0x1330
-  __TEXT.__objc_stubs: 0xb000
-  __TEXT.__objc_methlist: 0x2124
-  __TEXT.__const: 0x37e
-  __TEXT.__gcc_except_tab: 0xa620
-  __TEXT.__cstring: 0x2ead
-  __TEXT.__oslogstring: 0x13c06
-  __TEXT.__objc_classname: 0x4e4
-  __TEXT.__objc_methname: 0x10062
-  __TEXT.__objc_methtype: 0x2779
+1305.100.2.2.9
+  __TEXT.__text: 0x90b70
+  __TEXT.__auth_stubs: 0x1360
+  __TEXT.__objc_stubs: 0xb1e0
+  __TEXT.__objc_methlist: 0x2164
+  __TEXT.__const: 0x36e
+  __TEXT.__gcc_except_tab: 0xa670
+  __TEXT.__cstring: 0x2fed
+  __TEXT.__oslogstring: 0x13cd6
+  __TEXT.__objc_classname: 0x4e2
+  __TEXT.__objc_methname: 0x1032e
+  __TEXT.__objc_methtype: 0x27ad
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x150
   __TEXT.__swift5_typeref: 0x251

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1d78
+  __TEXT.__unwind_info: 0x1d90
   __TEXT.__eh_frame: 0x2b8
-  __DATA_CONST.__auth_got: 0x9a8
-  __DATA_CONST.__got: 0xd68
+  __DATA_CONST.__auth_got: 0x9c0
+  __DATA_CONST.__got: 0xda0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2ab8
-  __DATA_CONST.__cfstring: 0x31e0
+  __DATA_CONST.__const: 0x2ae0
+  __DATA_CONST.__cfstring: 0x3240
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3590
-  __DATA.__objc_selrefs: 0x3138
-  __DATA.__objc_ivar: 0x1b4
+  __DATA.__objc_const: 0x3560
+  __DATA.__objc_selrefs: 0x31b8
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x378
   __DATA.__data: 0x770
   __DATA.__bss: 0x60

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1162
-  Symbols:   765
-  CStrings:  4134
+  Functions: 1169
+  Symbols:   775
+  CStrings:  4155
 
Symbols:
+ _CC_SHA256
+ _IDSRegistrationPropertySupportsSenderKey
+ _IDSRegistrationPropertySupportsStewie
+ _IMChatErrorDomain
+ _IMServiceCapabilityGroupIdentity
+ _IMSharedHelperMissingKeysInStickerUserInfo
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_IMDOffGridAvailabilityTracker
+ _OBJC_CLASS_$_NSMutableData
+ _objc_retain_x9
CStrings:
+ "-[MessageServiceSession handler:incomingMessage:originalEncryptionType:messageID:toIdentifier:fromIdentifier:fromToken:timeStamp:fromIDSID:incomingEngroup:needsDeliveryReceipt:deliveryContext:storageContext:messageContext:isBeingReplayed:mergeID:wantsCheckpointing:isSnapTrustedUser:]_block_invoke"
+ "@44@0:8@16B24I28B32B36B40"
+ "AttemptedInvalidStickerReposition"
+ "Found %!l(MISSING)lu off grid capable devices for %!@(MISSING)"
+ "Got off grid mode %!@(MISSING) for %!@(MISSING)"
+ "MessageServiceSession+OffGrid"
+ "MissingStickerMetadata"
+ "NicknameWithRecordID:URI:decryptionKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:hasWallpaperUpdate:dropNicknameForUnknownContacts:withCompletionBlock:"
+ "NilStickerMetadata"
+ "PayloadAttachments Missing attachment URL for attachment with file transfer GUID %!@(MISSING)"
+ "Recipient is off grid (%!@(MISSING)) message pending satellite send (%!@(MISSING)) agree, treating as active off grid status"
+ "Recipient is off grid (%!@(MISSING)) message pending satellite send (%!@(MISSING)) do not match, fetching off grid mode"
+ "This message came from user with nickname cloudKitRecord  %!@(MISSING), SNaP trusted user: %!@(MISSING)"
+ "[MessageDeliveryController] Attempting sticker repositioning with missing reposition metadata."
+ "[MessageDeliveryController] Attempting sticker repositioning with nil reposition metadata."
+ "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:completionBlock:"
+ "_checkStickerRepositioningMetadata:"
+ "_convergesDisplayNames"
+ "_currentCachedRemoteDevicesForDestinations:service:listenerID:"
+ "_getQueueIdentifierFromGUID:"
+ "_handleNicknameReceived:fromIdentifier:withMessageItem:isSnapTrustedUser:"
+ "_numberOfOffGridCapableDevicesForDestination:"
+ "_setExpectedOffGridDeliveriesForMessage:context:"
+ "_updateOffGridStatusIfNeededWithMessage:context:"
+ "boolValueForKey:withDefault:"
+ "bytes"
+ "dataUsingEncoding:"
+ "handleMessageDidReplace:newMessage:"
+ "handler:incomingMessage:originalEncryptionType:messageID:toIdentifier:fromIdentifier:fromToken:timeStamp:fromIDSID:incomingEngroup:needsDeliveryReceipt:deliveryContext:storageContext:messageContext:isBeingReplayed:mergeID:wantsCheckpointing:isSnapTrustedUser:"
+ "initWithDisplayIDs:didSucceed:error:isFromMeToMe:shouldDeactivate:isBackwardsCompatibleMessage:"
+ "initWithLength:"
+ "isIMLLegacyRelayEnabled"
+ "isOffGridModeWithCompletion:"
+ "mutableBytes"
+ "processMessageForSending:toChat:style:allowWatchdog:account:didReplaceMessageBlock:completionBlock:"
+ "sendMessageDictionary:encryptDictionary:fromID:fromAccount:toURIs:toGroup:priority:options:willSendBlock:callCompletionOnSuccess:completionBlock:"
+ "sharedTracker"
+ "startTrackingHandle:"
+ "stu"
+ "supportsCapability:"
+ "v12@?0B8"
+ "v148@0:8@\"MessagePushHandler\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSData\"64@\"NSNumber\"72@\"NSString\"80@\"ENGroup\"88@\"NSNumber\"96@\"NSDictionary\"104@\"NSNumber\"112@120B128@\"NSString\"132B140B144"
+ "v148@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120B128@132B140B144"
+ "v220@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104B108B112@116@124@132@140@148@156@164@172@180@188@196B204B208@?212"
+ "v24@?0@\"IMMessageItem\"8@\"IMMessageItem\"16"
+ "v96@0:8@16B24@28@36@44@52q60@68@?76B84@?88"
+ "valueForCapability:"
- "!"
- "%!l(MISSING)u"
- "-[MessageServiceSession handler:incomingMessage:originalEncryptionType:messageID:toIdentifier:fromIdentifier:fromToken:timeStamp:fromIDSID:incomingEngroup:needsDeliveryReceipt:deliveryContext:storageContext:messageContext:isBeingReplayed:mergeID:wantsCheckpointing:]_block_invoke"
- "@48@0:8@16B24I28B32B36B40B44"
- "Found %!l(MISSING)u madridEndpoints: %!@(MISSING)"
- "Found %!l(MISSING)u madridLiteEndpoints: %!@(MISSING)"
- "IDS force refresh server status madrid complete: %!@(MISSING)"
- "IDS force refresh server status madrid lite complete: %!@(MISSING)"
- "NicknameWithRecordID:URI:decryptionKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:hasWallpaperUpdate:withCompletionBlock:"
- "TB,R,N,V_destinationIsOffGrid"
- "This message came from user with nickname cloudKitRecord  %!@(MISSING)"
- "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:completionBlock:"
- "_destinationIsOffGrid"
- "_handleNicknameReceived:fromIdentifier:withMessageItem:"
- "_handleOffGridForMessage:context:"
- "com.apple.madrid.lite"
- "destinationIsOffGrid"
- "destinationURIs"
- "handler:incomingMessage:originalEncryptionType:messageID:toIdentifier:fromIdentifier:fromToken:timeStamp:fromIDSID:incomingEngroup:needsDeliveryReceipt:deliveryContext:storageContext:messageContext:isBeingReplayed:mergeID:wantsCheckpointing:"
- "iMessage;+;%!@(MISSING)"
- "iMessage;-;%!@(MISSING)"
- "initWithDisplayIDs:didSucceed:error:isFromMeToMe:shouldDeactivate:destinationIsOffGrid:isBackwardsCompatibleMessage:"
- "participantHandles"
- "v144@0:8@\"MessagePushHandler\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSData\"64@\"NSNumber\"72@\"NSString\"80@\"ENGroup\"88@\"NSNumber\"96@\"NSDictionary\"104@\"NSNumber\"112@120B128@\"NSString\"132B140"
- "v144@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120B128@132B140"
- "v216@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104B108B112@116@124@132@140@148@156@164@172@180@188@196B204@?208"

```
