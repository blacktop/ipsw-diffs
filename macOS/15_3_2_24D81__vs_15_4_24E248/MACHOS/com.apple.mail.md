## com.apple.mail

> `/System/Library/Accessibility/BundlesBase/com.apple.mail.axbundle/Versions/A/com.apple.mail`

```diff

-287.6.0.0.0
-  __TEXT.__text: 0xb640
+287.6.4.0.0
+  __TEXT.__text: 0xb734
   __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_stubs: 0x19e0
   __TEXT.__objc_methlist: 0x1114
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x1b0
+  __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__cstring: 0x1fc2
   __TEXT.__objc_classname: 0xe97
   __TEXT.__objc_methname: 0x1888

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18BE4EA1-F714-31AD-9139-9B9217973D38
-  Functions: 350
-  Symbols:   1221
+  UUID: F5007595-1196-345C-AC95-EF34D8DF09FC
+  Functions: 351
+  Symbols:   1222
   CStrings:  1129
 
Symbols:
+ -[NSCollectionViewSectionAccessibilityAccessibility__Mail__AppKit _accessibilitySearchSectionLabelForKey:].cold.1
Functions:
~ -[ComposeSpellCheckerAccessibility setPostCompletedNotification:forSpellDocumentWithTag:] : 472 -> 476
~ -[NSSearchToolbarItemViewAccessibility__Mail__AppKit searchButtonClicked:] : 392 -> 396
~ -[MailTableViewAccessibility _accessibilityIsMessageTable] : 240 -> 244
~ -[RolloverContainerViewAccessibility _accessibilityInitAccessibility] : 620 -> 628
~ -[NSCollectionViewSectionAccessibilityAccessibility__Mail__AppKit accessibilityLabel] : 552 -> 556
~ -[NSCollectionViewSectionAccessibilityAccessibility__Mail__AppKit _accessibilitySearchSectionLabelForKey:] : 212 -> 196
~ -[ComposingPreferencesAccessibility viewDidLoad] : 192 -> 196
~ -[MailSuggestionAttachmentCellAccessibility accessibilityPerformPress] : 296 -> 300
~ ___70-[MailSuggestionAttachmentCellAccessibility accessibilityPerformPress]_block_invoke : 164 -> 168
~ -[MessageViewerAccessibility _updateMarkReadUnreadButtonImage] : 340 -> 344
~ -[MessageViewerAccessibility _updateMoveToFolderTitle] : 368 -> 372
~ -[MessageViewerAccessibility _updateMarkAsJunkButtonImage] : 340 -> 344
~ -[MessageViewerAccessibility touchBar:makeItemForIdentifier:] : 1256 -> 1260
~ +[MessageViewerAccessibility _axcAllMessageViewers] : 344 -> 348
~ -[MessageViewerAccessibility _axcMoveToFolderSegmentedControl] : 332 -> 336
~ -[MessageViewerAccessibility _axcMoveToFolderSegmentedControlCell] : 332 -> 336
~ -[MessageViewerAccessibility _axcMailboxPredictionForSelection] : 316 -> 320
~ -[MessageViewerAccessibility _axcMailBoxDisplayName] : 388 -> 392
~ -[DocumentCollectionViewItemAccessibility accessibilityLabel] : 332 -> 336
~ _accessibilityGetLabelForConversationMember : 820 -> 824
~ -[AttachmentViewControllerAccessibility addAttachmentView:] : 368 -> 376
~ -[_PaddedTextAttachmentCellAccessibility accessibilityLabel] : 256 -> 260
~ -[MailboxBadgeCellAccessibility accessibilityLabel] : 536 -> 540
~ -[AccountInformationControllerAccessibility viewDidLoad] : 192 -> 196
~ ___72-[HeaderTruncationAttachmentCellAccessibility accessibilityPerformPress]_block_invoke : 104 -> 108
~ -[ViewerPreferencesAccessibility viewDidLoad] : 192 -> 196
~ -[GeneralPreferencesAccessibility viewDidLoad] : 192 -> 196
~ +[HeaderViewControllerAccessibility _mailboxIconString] : 228 -> 232
~ ___55+[HeaderViewControllerAccessibility _mailboxIconString]_block_invoke : 356 -> 364
~ -[HeaderViewControllerAccessibility setRepresentedObject:] : 264 -> 268
~ -[HeaderViewControllerAccessibility _axcTruncationCell] : 332 -> 336
~ ___58-[HeaderViewControllerAccessibility _axcUpdateTextStorage]_block_invoke : 572 -> 580
~ -[MailboxOutlineItemViewAccessibility _axcHeaderIndicatorView] : 600 -> 604
~ -[MailboxOutlineItemViewAccessibility accessibilityCustomActions] : 528 -> 512
~ -[MailboxOutlineItemViewAccessibility accessibilityPerformPress] : 224 -> 232
~ -[AttachmentViewAccessibility accessibilityAttributeValue:] : 328 -> 332
~ -[ListSuggestionCollectionViewItemAccessibility accessibilityLabel] : 332 -> 336
~ ___67-[ListSuggestionCollectionViewItemAccessibility accessibilityLabel]_block_invoke : 372 -> 376
~ -[MailboxBehaviorsControllerAccessibility viewDidLoad] : 192 -> 196
~ -[HeadersEditorAccessibility _axcSetLabel:forSegmentedControl:] : 404 -> 412
~ -[HeadersEditorAccessibility _updateSignButton] : 236 -> 240
~ -[HeadersEditorAccessibility _updateEncryptButton] : 236 -> 240
~ -[MailSearchFieldCellAccessibility accessibilitySharedFocusElements] : 428 -> 436
~ -[QuickReplyViewAccessibility _accessibilityLoadAccessibilityInformation] : 444 -> 452
~ -[QuickReplyViewAccessibility accessibilityContents] : 196 -> 200
~ -[QuickReplyViewAccessibility accessibilityLabel] : 196 -> 200
~ -[NSImageAccessibility__Mail__AppKit __axcDescription] : 288 -> 292
~ -[QuotaBarAccessibility _accessibilityLoadAccessibilityInformation] : 224 -> 228
~ -[ContactCollectionViewItemAccessibility accessibilityLabel] : 332 -> 336
~ -[ProgressViewControllerAccessibility _axcInitAccessibility] : 284 -> 288
~ ___60-[ProgressViewControllerAccessibility _axcInitAccessibility]_block_invoke : 256 -> 260
~ -[SearchSuggestionsCollectionViewAccessibility accessibilitySelectItemsAtIndexPaths:] : 212 -> 216
~ -[ComposeViewControllerAccessibility touchBar:makeItemForIdentifier:] : 660 -> 668
~ -[ActivityViewControllerAccessibility _axcUpdateContentView] : 232 -> 236
~ -[MessageViewControllerAccessibility setRepresentedObject:] : 264 -> 268
~ -[MailSearchFieldAccessibility accessibilityLinkedUIElements] : 244 -> 248
~ -[MailboxOutlineRowViewAccessibility _axbPerformPressOnChildButton] : 420 -> 424
~ -[AXCAccessibleFilterCheckbox _textFieldCell] : 396 -> 392
~ -[LocationCollectionViewItemAccessibility accessibilityLabel] : 588 -> 592

```
