## ChatKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/ChatKit.framework/Versions/A/ChatKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1450.700.41.0.0
-  __TEXT.__text: 0xb34344
+1450.700.71.0.0
+  __TEXT.__text: 0xb343e0
   __TEXT.__auth_stubs: 0xb8a0
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x25c
   __TEXT.__objc_methlist: 0x6f9bc
   __TEXT.__const: 0x37154
   __TEXT.__gcc_except_tab: 0x235a4
-  __TEXT.__cstring: 0x39c2b
+  __TEXT.__cstring: 0x39c3b
   __TEXT.__oslogstring: 0x4be03
   __TEXT.__dlopen_cstrs: 0x70d
   __TEXT.__ustring: 0x1c4

   __TEXT.__unwind_info: 0x302d8
   __TEXT.__eh_frame: 0xc6bc
   __TEXT.__objc_classname: 0x11d06
-  __TEXT.__objc_methname: 0x1156fa
+  __TEXT.__objc_methname: 0x11576a
   __TEXT.__objc_methtype: 0x25066
   __TEXT.__objc_stubs: 0xabc00
   __DATA_CONST.__got: 0x6e60

   __DATA_CONST.__objc_arraydata: 0xeb8
   __AUTH_CONST.__auth_got: 0x5c70
   __AUTH_CONST.__const: 0x36440
-  __AUTH_CONST.__cfstring: 0x22d80
+  __AUTH_CONST.__cfstring: 0x22da0
   __AUTH_CONST.__objc_const: 0x97c58
   __AUTH_CONST.__objc_intobj: 0xed0
   __AUTH_CONST.__objc_arrayobj: 0xdc8

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 68144
   Symbols:   92639
-  CStrings:  53440
+  CStrings:  53441
 
Symbols:
+ _objc_msgSend$deviceIsLockedDownFor:senderOrigin:
+ _objc_msgSend$supportsBusinessChatForSenderOrigin:
+ _objc_msgSend$supportsDataDetectorsForSenderOrigin:
+ _objc_msgSend$supportsFocusForSenderOrigin:
+ _objc_msgSend$supportsScreenEffectsForSenderOrigin:
+ _objc_msgSend$supportsSharedWithYouForSenderOrigin:
+ _objc_msgSend$supportsSpotlightForSenderOrigin:
- _objc_msgSend$deviceIsLockedDown
- _objc_msgSend$supportsBusinessChat
- _objc_msgSend$supportsDataDetectors
- _objc_msgSend$supportsFocus
- _objc_msgSend$supportsScreenEffects
- _objc_msgSend$supportsSharedWithYou
- _objc_msgSend$supportsSpotlight
Functions:
~ -[CKChatController(ClickyOrbConformance) _menuForChatItem:withParentChatItem:menuAppearance:] : 2244 -> 2248
~ -[CKRecipientSelectionController serviceTypeForRecipient:] : 1176 -> 1180
~ -[CKRecipientSelectionController addRecipient:] : 1024 -> 1028
~ -[CKRecipientSelectionController _availibilityForRecipient:onService:] : 816 -> 820
~ -[CKChatController textPasteConfigurationSupporting:transformPasteItem:] : 724 -> 732
~ +[CKCoreChatController(Backgrounds) supportsTranscriptBackground] : 36 -> 44
~ -[CKFullScreenEffectManager startFullscreenEffectForChatItem:language:] : 1560 -> 1564
~ -[CKMessageEntryRichTextView _ck_beginPasteOperationAndPasteAsRichText:] : 520 -> 528
~ +[CKBusinessOnboardingController shouldShowBusinessOnboarding] : 124 -> 128
~ +[CKComposition(UIPasteboard) mediaObjectFromPhotosAsset:completion:] : 956 -> 964
~ -[CKConversation isBusinessChatDisabled] : 44 -> 48
~ +[CKOnboardingController _shouldShowSyndicationOnboardingFlowOnLaunch] : 696 -> 700
~ +[CKUserActivityHandler openSMSURL:animate:navigationProvider:chatController:originatingProcess:] : 2984 -> 2996
~ -[CKMediaObject(Display) _shouldDenyUTITypeFromRichIcon] : 316 -> 352
~ -[CKMediaObject(Display) richIcon] : 1140 -> 1148
~ -[CKSearchViewController _searchImmediately] : 1024 -> 1028
~ -[CKMessagesController presentFocusStatusAuthorizationAlertIfNecessary] : 344 -> 348
~ -[CKMessageEntryContentView(RichLinks) richLinksEditMenuForAttributedText:inRange:] : 1332 -> 1340
~ -[CKBrowserItemPayload(CKCompositionAdditions) __ck_urlFromTextBodyForRichLink] : 552 -> 556
~ -[CKComposition(IMSuperFormat) messageWithGUID:superFormatText:superFormatSubject:fileTransferGUIDs:mediaObjects:balloonBundleID:payloadData:messageSummaryInfo:] : 1784 -> 1788
~ -[CKSearchAnalytics _buildType:] : 8 -> 20
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YlB7Qh/Sources/Messages_iosmac/ChatKit/CKStoragePluginDataModel.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YlB7Qh/Sources/Messages_iosmac/ChatKit/CKTranscriptPluginViewManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YlB7Qh/Sources/Messages_iosmac/ChatKit/CKTranscriptPrintPageRenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YlB7Qh/Sources/Messages_iosmac/ChatKit/LegacyStoragePluginCounts.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YlB7Qh/Sources/Messages_iosmac/ChatKit/StoragePluginCounts.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YlB7Qh/Sources/Messages_iosmac/ChatKit/UITests/IMMockChat.m"
+ "deviceIsLockedDownFor:senderOrigin:"
+ "public.font"
+ "supportsBusinessChatForSenderOrigin:"
+ "supportsDataDetectorsForSenderOrigin:"
+ "supportsFocusForSenderOrigin:"
+ "supportsScreenEffectsForSenderOrigin:"
+ "supportsSharedWithYouForSenderOrigin:"
+ "supportsSpotlightForSenderOrigin:"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g9M5Nf/Sources/Messages_iosmac/ChatKit/CKStoragePluginDataModel.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g9M5Nf/Sources/Messages_iosmac/ChatKit/CKTranscriptPluginViewManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g9M5Nf/Sources/Messages_iosmac/ChatKit/CKTranscriptPrintPageRenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g9M5Nf/Sources/Messages_iosmac/ChatKit/LegacyStoragePluginCounts.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g9M5Nf/Sources/Messages_iosmac/ChatKit/StoragePluginCounts.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g9M5Nf/Sources/Messages_iosmac/ChatKit/UITests/IMMockChat.m"
- "deviceIsLockedDown"
- "supportsBusinessChat"
- "supportsDataDetectors"
- "supportsFocus"
- "supportsScreenEffects"
- "supportsSharedWithYou"
- "supportsSpotlight"
```
