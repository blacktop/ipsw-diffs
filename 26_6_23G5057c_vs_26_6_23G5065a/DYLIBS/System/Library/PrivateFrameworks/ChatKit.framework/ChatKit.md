## ChatKit

> `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-  __TEXT.__text: 0xbb2450
+  __TEXT.__text: 0xbb24b8
   __TEXT.__auth_stubs: 0xc200
   __TEXT.__delay_helper: 0xcd0
-  __TEXT.__objc_methlist: 0x706cc
+  __TEXT.__objc_methlist: 0x706d4
   __TEXT.__const: 0x3bda4
   __TEXT.__gcc_except_tab: 0x2439c
   __TEXT.__cstring: 0x3c5a1

   __TEXT.__unwind_info: 0x31fb8
   __TEXT.__eh_frame: 0xde74
   __TEXT.__objc_classname: 0x12626
-  __TEXT.__objc_methname: 0x117eba
+  __TEXT.__objc_methname: 0x117f4a
   __TEXT.__objc_methtype: 0x25836
-  __TEXT.__objc_stubs: 0xadbe0
+  __TEXT.__objc_stubs: 0xadc00
   __DATA_CONST.__got: 0x7310
   __DATA_CONST.__const: 0xed90
   __DATA_CONST.__objc_classlist: 0x2f10
   __DATA_CONST.__objc_catlist: 0x548
   __DATA_CONST.__objc_protolist: 0x1350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35c60
+  __DATA_CONST.__objc_selrefs: 0x35c68
   __DATA_CONST.__objc_protorefs: 0x518
   __DATA_CONST.__objc_superrefs: 0x19e8
   __DATA_CONST.__objc_arraydata: 0xef0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 70663
-  Symbols:   146859
-  CStrings:  59687
+  Symbols:   146860
+  CStrings:  59688
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA.__objc_stublist : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[CKCoreChatController _performConversationReassignment]
+ _objc_msgSend$_performConversationReassignment
+ _objc_msgSend$deviceIsLockedDownFor:senderOrigin:
+ _objc_msgSend$supportsBusinessChatForSenderOrigin:
+ _objc_msgSend$supportsDataDetectorsForSenderOrigin:
+ _objc_msgSend$supportsFocusForSenderOrigin:
+ _objc_msgSend$supportsScreenEffectsForSenderOrigin:
+ _objc_msgSend$supportsSharedWithYouForSenderOrigin:
+ _objc_msgSend$supportsSpotlightForSenderOrigin:
- ___64-[CKCoreChatController _reassignConversationWithDeferredReload:]_block_invoke
- _objc_msgSend$deviceIsLockedDown
- _objc_msgSend$supportsBusinessChat
- _objc_msgSend$supportsDataDetectors
- _objc_msgSend$supportsFocus
- _objc_msgSend$supportsScreenEffects
- _objc_msgSend$supportsSharedWithYou
- _objc_msgSend$supportsSpotlight
Functions:
~ -[CKMessagesController presentFocusStatusAuthorizationAlertIfNecessary] : 344 -> 348
~ -[CKChatController(ClickyOrbConformance) _menuForChatItem:withParentChatItem:menuAppearance:] : 2312 -> 2316
~ -[CKRecipientSelectionController serviceTypeForRecipient:] : 1176 -> 1180
~ -[CKRecipientSelectionController addRecipient:] : 1024 -> 1028
~ -[CKRecipientSelectionController _availibilityForRecipient:onService:] : 816 -> 820
~ -[CKChatController textPasteConfigurationSupporting:transformPasteItem:] : 724 -> 732
~ +[CKCoreChatController(Backgrounds) supportsTranscriptBackground] : 36 -> 44
~ -[CKFullScreenEffectManager startFullscreenEffectForChatItem:language:] : 1712 -> 1716
~ -[CKMessageEntryRichTextView _ck_beginPasteOperationAndPasteAsRichText:] : 520 -> 528
~ +[CKBusinessOnboardingController shouldShowBusinessOnboarding] : 124 -> 128
~ +[CKComposition(UIPasteboard) mediaObjectFromPhotosAsset:completion:] : 956 -> 964
~ -[CKConversation isBusinessChatDisabled] : 44 -> 48
~ +[CKOnboardingController _shouldShowSyndicationOnboardingFlowOnLaunch] : 696 -> 700
~ ___64-[CKCoreChatController _reassignConversationWithDeferredReload:]_block_invoke -> -[CKCoreChatController _performConversationReassignment] : 652 -> 648
~ +[CKUserActivityHandler openSMSURL:animate:navigationProvider:chatController:originatingProcess:] : 2972 -> 2984
~ -[CKMediaObject(Display) richIcon] : 1140 -> 1148
~ -[CKSearchViewController _searchImmediately] : 1024 -> 1028
~ -[CKMessageEntryContentView(RichLinks) richLinksEditMenuForAttributedText:inRange:] : 1332 -> 1340
~ -[CKBrowserItemPayload(CKCompositionAdditions) __ck_urlFromTextBodyForRichLink] : 552 -> 556
~ -[CKComposition(IMSuperFormat) messageWithGUID:superFormatText:superFormatSubject:fileTransferGUIDs:mediaObjects:balloonBundleID:payloadData:messageSummaryInfo:] : 1784 -> 1788
CStrings:
+ "_performConversationReassignment"
+ "deviceIsLockedDownFor:senderOrigin:"
+ "supportsBusinessChatForSenderOrigin:"
+ "supportsDataDetectorsForSenderOrigin:"
+ "supportsFocusForSenderOrigin:"
+ "supportsScreenEffectsForSenderOrigin:"
+ "supportsSharedWithYouForSenderOrigin:"
+ "supportsSpotlightForSenderOrigin:"
- "deviceIsLockedDown"
- "supportsBusinessChat"
- "supportsDataDetectors"
- "supportsFocus"
- "supportsScreenEffects"
- "supportsSharedWithYou"
- "supportsSpotlight"

```
