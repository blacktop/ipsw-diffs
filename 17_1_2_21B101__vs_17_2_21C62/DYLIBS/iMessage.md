## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1261.200.71.2.16
-  __TEXT.__text: 0xa1fcc
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x1eec
+1262.300.81.2.13
+  __TEXT.__text: 0x82ed8
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_methlist: 0x1f6c
   __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x7f34
-  __TEXT.__cstring: 0x10b0f
-  __TEXT.__oslogstring: 0x12cf3
-  __TEXT.__unwind_info: 0x1b5c
+  __TEXT.__gcc_except_tab: 0x7c34
+  __TEXT.__cstring: 0x2a4c
+  __TEXT.__oslogstring: 0x1302c
+  __TEXT.__unwind_info: 0x1bb4
   __TEXT.__objc_classname: 0x47b
-  __TEXT.__objc_methname: 0xe40a
-  __TEXT.__objc_methtype: 0x243b
-  __TEXT.__objc_stubs: 0xa1c0
-  __DATA_CONST.__got: 0x898
-  __DATA_CONST.__const: 0x1fc8
+  __TEXT.__objc_methname: 0xe6e0
+  __TEXT.__objc_methtype: 0x2481
+  __TEXT.__objc_stubs: 0xa3c0
+  __DATA_CONST.__got: 0x8a0
+  __DATA_CONST.__const: 0x1fd8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2508
-  __DATA_CONST.__objc_selrefs: 0x2c30
-  __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__cfstring: 0xb880
+  __DATA_CONST.__objc_const: 0x2588
+  __DATA_CONST.__objc_selrefs: 0x2cb8
+  __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__objc_const: 0x9e0
   __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__cfstring: 0x3040
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x6a8
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_classrefs: 0x418
+  __DATA.__objc_classrefs: 0x420
   __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0x184
+  __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x3b8
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x550

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1138
+  Functions: 1085
   Symbols:   665
-  CStrings:  4885
+  CStrings:  3873
 
Symbols:
+ _IDSRegistrationPropertySupportsHybridGroupsV1
+ _OBJC_CLASS_$_IMCommSafetyRequestsManager
- _MarcoLogMadridLevel
- _MarcoShouldLogMadridLevel
CStrings:
+ "-[StickerRefreshDeliveryController sendFTMessage:attempts:withCompletionBlock:]"
+ "Adding data to be encrypted of size: %lu"
+ "Broadcasting messageReceived %@"
+ "Compressed edited message data from: %lu  to: %lu"
+ "Could not find chat for sticker reposition. message: %@ chat: %@"
+ "Failed sending repositioned sticker for guid: %@   to people: %@  error: %d"
+ "Finished sending repositioned sticker for guid: %@   to people: %@"
+ "Generating chatItem for group photo change. Was group photo removal: %@"
+ "IDSSendMessageOptionKTVerificationUUIDKey"
+ "It's been a long time since a refresh has occurred, just re-send the transfer to everyone. timeSinceLastRefresh: %f, canRefreshAsset: %@"
+ "Received %@/%@ from server following refresh request. re-uploading group photo."
+ "Received flushed cache for KT Peer URI %@"
+ "Send of sticker reposition not successful, stickerRepositionCommandGuid %@, error %ld"
+ "Send of sticker reposition successful, editCommandGuid %@"
+ "Sending sticker reposition command with guid %@ for sticker chat item with guid %@"
+ "T@\"NSNumber\",C,N,V_failReason"
+ "T@\"NSNumber\",C,N,V_responseCode"
+ "Time since last refresh: %f for chat: %@, transfer: %@"
+ "_failReason"
+ "_keyTransparencyEnforcementDictionaryForChatIdentifier:"
+ "_responseCode"
+ "_sendURL:urlToRemove:topic:sessionInfo:messageGUID:transferID:fileTransferGUID:attachmentSendContexts:failIfError:sendStatus:attachmentStatus:group:"
+ "_updateOrRemoveGroupPhotoForChat:sender:completedTransfer:isHidden:"
+ "broadcasterForKeyTransparencyListeners"
+ "checkExistingAttachmentSensitivityIfNeededFor:attachmentURL:isFromMe:"
+ "failReason"
+ "idsAccountsDidChange"
+ "keyTransparencyURIToUUIDMapping"
+ "messageDeliveryController:service:didFlushCacheForKTPeerURI:"
+ "nil message sent to %s"
+ "refreshStatusForKTPeerURI:"
+ "responseCode"
+ "scig"
+ "sendRepositionStickerMessage:chatIdentifier:accountID:style:"
+ "sendRepositionedStickerMetadata:forEditedMessage:destinations:account:fromID:completionBlock:"
+ "serviceIdentifier"
+ "sessionSpecificTransferIDForTransferID:"
+ "setFailReason:"
+ "setResponseCode:"
+ "srpi"
+ "storeRepositionedStickerLocally:"
+ "v108@0:8@16@24@32@40@48@56@64@72B80@84@92@100"
+ "v24@?0@\"FTiMessageRequestMMCSFileRefreshToken\"8B16I20"
+ "v40@0:8@\"MessageDeliveryController\"16@\"IDSService\"24@\"NSString\"32"
- "Broadcasting messageRecieved %@"
- "Compressed edited message data from: %u  to: %u"
- "Service"
- "_sendURL:urlToRemove:topic:sessionInfo:messageGUID:fileTransferGUID:attachmentSendContexts:failIfError:sendStatus:attachmentStatus:group:"
- "enforceAccountsMatchForMocAndShowDialogIfNeeded"
- "not requesting group photo - not all required keys present %@"
- "supports-hybrid-groups-v1"
- "v100@0:8@16@24@32@40@48@56@64B72@76@84@92"

```
