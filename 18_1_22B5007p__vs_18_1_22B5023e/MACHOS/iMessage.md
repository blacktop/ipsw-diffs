## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1301.200.8.2.1
-  __TEXT.__text: 0x8fdc0
-  __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_stubs: 0xaf40
-  __TEXT.__objc_methlist: 0x210c
-  __TEXT.__const: 0x37e
-  __TEXT.__gcc_except_tab: 0xa5a4
-  __TEXT.__cstring: 0x2e8d
-  __TEXT.__oslogstring: 0x13ad6
-  __TEXT.__objc_classname: 0x4e5
-  __TEXT.__objc_methname: 0xff1a
-  __TEXT.__objc_methtype: 0x2776
+1402.200.8.0.0
+  __TEXT.__text: 0x90930
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__objc_stubs: 0xb180
+  __TEXT.__objc_methlist: 0x2144
+  __TEXT.__const: 0x36e
+  __TEXT.__gcc_except_tab: 0xa678
+  __TEXT.__cstring: 0x2efd
+  __TEXT.__oslogstring: 0x13d26
+  __TEXT.__objc_classname: 0x4e2
+  __TEXT.__objc_methname: 0x102df
+  __TEXT.__objc_methtype: 0x27ad
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x150
-  __TEXT.__swift5_typeref: 0x253
+  __TEXT.__swift5_typeref: 0x251
   __TEXT.__swift5_reflstr: 0x1f
   __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1d60
+  __TEXT.__unwind_info: 0x1d88
   __TEXT.__eh_frame: 0x2b8
-  __DATA_CONST.__auth_got: 0x9a0
-  __DATA_CONST.__got: 0xd70
+  __DATA_CONST.__auth_got: 0x9b8
+  __DATA_CONST.__got: 0xd88
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x29b0
-  __DATA_CONST.__cfstring: 0x31a0
+  __DATA_CONST.__const: 0x2ae0
+  __DATA_CONST.__cfstring: 0x31e0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x3560
-  __DATA.__objc_selrefs: 0x3108
+  __DATA.__objc_selrefs: 0x31a0
   __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x378
   __DATA.__data: 0x770
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__data: 0xc
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1160
-  Symbols:   757
-  CStrings:  4117
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1165
+  Symbols:   771
+  CStrings:  4150
 
Symbols:
+ _CC_SHA256
+ _IDSRegistrationPropertySupportsSenderKey
+ _IDSRegistrationPropertySupportsStewie
+ _IMStickerTransferInfoDirectoryURL
+ _OBJC_CLASS_$_IMDOffGridAvailabilityTracker
+ _OBJC_CLASS_$_NSMutableData
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x9
- _kStickerTransferInfoPlistFileFolder
CStrings:
+ "%!{(MISSING)public}s alias %!s(MISSING) SIMID %!s(MISSING) no longer a valid subscription, defaulting to whether iMessage is available"
+ "-[MessageServiceSession handler:incomingMessage:originalEncryptionType:messageID:toIdentifier:fromIdentifier:fromToken:timeStamp:fromIDSID:incomingEngroup:needsDeliveryReceipt:deliveryContext:storageContext:messageContext:isBeingReplayed:mergeID:wantsCheckpointing:isSnapTrustedUser:]_block_invoke"
+ "Appending off grid status of %!@(MISSING) for handle ID %!@(MISSING) "
+ "Attempting to append off grid status to message dictionary"
+ "Found %!l(MISSING)lu off grid capable devices for %!@(MISSING)"
+ "Got off grid mode %!@(MISSING) for %!@(MISSING)"
+ "MessageServiceSession+OffGrid"
+ "Missing identifier for this off grid status payload!"
+ "NicknameWithRecordID:URI:decryptionKey:wallpaperDataTag:wallpaperLowResDataTag:wallpaperMetadataTag:hasWallpaperUpdate:dropNicknameForUnknownContacts:withCompletionBlock:"
+ "No participant found, not appending off grid status"
+ "Not appending off grid status, not a 1:1 chat"
+ "PayloadAttachments Missing attachment URL for attachment with file transfer GUID %!@(MISSING)"
+ "Recipient is off grid (%!@(MISSING)) message pending satellite send (%!@(MISSING)) agree, treating as active off grid status"
+ "Recipient is off grid (%!@(MISSING)) message pending satellite send (%!@(MISSING)) do not match, fetching off grid mode"
+ "Sticker repositioning is supported and necessary keys were added to messageDictionary."
+ "TB,R,N,V_isBackwardsCompatibleMessage"
+ "This message came from user with nickname cloudKitRecord  %!@(MISSING), SNaP trusted user: %!@(MISSING)"
+ "_appendSeenOffGridStatusToMessageDictionary:forChat:"
+ "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:completionBlock:"
+ "_currentCachedRemoteDevicesForDestinations:service:listenerID:"
+ "_getQueueIdentifierFromGUID:"
+ "_handleNicknameReceived:fromIdentifier:withMessageItem:isSnapTrustedUser:"
+ "_isBackwardsCompatibleMessage"
+ "_numberOfOffGridCapableDevicesForDestination:"
+ "_setExpectedOffGridDeliveriesForMessage:context:"
+ "_updateOffGridStatusIfNeededWithMessage:context:"
+ "boolValueForKey:withDefault:"
+ "bytes"
+ "cachedOffGridModeAndLastPublisherWithCompletion:"
+ "dataUsingEncoding:"
+ "didReceiveOffGridStatus:forID:messageGUID:account:"
+ "handleMessageDidReplace:newMessage:"
+ "handler:incomingMessage:originalEncryptionType:messageID:toIdentifier:fromIdentifier:fromToken:timeStamp:fromIDSID:incomingEngroup:needsDeliveryReceipt:deliveryContext:storageContext:messageContext:isBeingReplayed:mergeID:wantsCheckpointing:isSnapTrustedUser:"
+ "initWithDisplayIDs:didSucceed:error:isFromMeToMe:shouldDeactivate:isBackwardsCompatibleMessage:"
+ "initWithLength:"
+ "isBackwardsCompatibleMessage"
+ "isBackwardsCompatibleMessage %!@(MISSING)"
+ "isIMLLegacyRelayEnabled"
+ "isOffGridModeWithCompletion:"
+ "messageSummaryInfoForSending"
+ "mutableBytes"
+ "processMessageForSending:toChat:style:allowWatchdog:account:didReplaceMessageBlock:completionBlock:"
+ "sendMessageDictionary:encryptDictionary:fromID:fromAccount:toURIs:toGroup:priority:options:willSendBlock:callCompletionOnSuccess:completionBlock:"
+ "setBackwardsCompatibleVersion:"
+ "setExpectedOffGridCapableDeliveries:"
+ "sharedTracker"
+ "sofg"
+ "sofgid"
+ "startTrackingHandle:"
+ "stu"
+ "v12@?0B8"
+ "v148@0:8@\"MessagePushHandler\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSData\"64@\"NSNumber\"72@\"NSString\"80@\"ENGroup\"88@\"NSNumber\"96@\"NSDictionary\"104@\"NSNumber\"112@120B128@\"NSString\"132B140B144"
+ "v148@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120B128@132B140B144"
+ "v20@?0B8@\"NSData\"12"
+ "v220@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104B108B112@116@124@132@140@148@156@164@172@180@188@196B204B208@?212"
+ "v24@?0@\"IMMessageItem\"8@\"IMMessageItem\"16"
+ "v36@?0@\"MessageDeliveryController\"8@\"NSArray\"16B24I28B32"
+ "v96@0:8@16B24@28@36@44@52q60@68@?76B84@?88"
+ "valueForCapability:"
- "%!l(MISSING)u"
- "-[MessageServiceSession handler:incomingMessage:originalEncryptionType:messageID:toIdentifier:fromIdentifier:fromToken:timeStamp:fromIDSID:incomingEngroup:needsDeliveryReceipt:deliveryContext:storageContext:messageContext:isBeingReplayed:mergeID:wantsCheckpointing:]_block_invoke"
- "?0"
- "Found %!l(MISSING)u madridEndpoints: %!@(MISSING)"
- "Found %!l(MISSING)u madridLiteEndpoints: %!@(MISSING)"
- "IDS force refresh server status madrid complete: %!@(MISSING)"
- "IDS force refresh server status madrid lite complete: %!@(MISSING)"
- "Message %!@(MISSING) was sent to a user that is off grid using regular iMessage, offer send via satellite"
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
- "didReceiveOffGridStatus:forMessageGUID:account:"
- "handler:incomingMessage:originalEncryptionType:messageID:toIdentifier:fromIdentifier:fromToken:timeStamp:fromIDSID:incomingEngroup:needsDeliveryReceipt:deliveryContext:storageContext:messageContext:isBeingReplayed:mergeID:wantsCheckpointing:"
- "initWithDisplayIDs:didSucceed:error:isFromMeToMe:shouldDeactivate:destinationIsOffGrid:"
- "participantHandles"
- "v144@0:8@\"MessagePushHandler\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSData\"64@\"NSNumber\"72@\"NSString\"80@\"ENGroup\"88@\"NSNumber\"96@\"NSDictionary\"104@\"NSNumber\"112@120B128@\"NSString\"132B140"
- "v144@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120B128@132B140"
- "v216@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104B108B112@116@124@132@140@148@156@164@172@180@188@196B204@?208"
- "v32@?0@\"MessageDeliveryController\"8@\"NSArray\"16B24I28"

```
