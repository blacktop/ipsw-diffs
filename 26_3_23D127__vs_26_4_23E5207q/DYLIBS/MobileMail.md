## MobileMail

> `/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x136e0
-  __TEXT.__auth_stubs: 0x6a0
+3005.16.0.0.0
+  __TEXT.__text: 0x14390
+  __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_methlist: 0x1864
   __TEXT.__const: 0x38
   __TEXT.__cstring: 0x3754
   __TEXT.__oslogstring: 0x5a
-  __TEXT.__gcc_except_tab: 0x3ac
+  __TEXT.__gcc_except_tab: 0x3b4
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x750
+  __TEXT.__unwind_info: 0x758
   __TEXT.__objc_classname: 0x13e1
   __TEXT.__objc_methname: 0x2e94
   __TEXT.__objc_methtype: 0x22b

   __DATA_CONST.__objc_selrefs: 0xd90
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x540
   __AUTH_CONST.__cfstring: 0x48e0
   __AUTH_CONST.__objc_const: 0x42e0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA2BBBB5-760D-375D-9D1F-D24C465DCA11
+  UUID: 9948FE36-1114-3665-AE30-CEAAD68ABA90
   Functions: 542
-  Symbols:   2324
+  Symbols:   2319
   CStrings:  1802
 
Symbols:
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x2
- _objc_retain_x3
- _objc_storeStrong
Functions:
~ +[AXMobileMailGlue accessibilityInitializeBundle] : 336 -> 348
~ ___49+[AXMobileMailGlue accessibilityInitializeBundle]_block_invoke : 556 -> 560
~ ___49+[AXMobileMailGlue accessibilityInitializeBundle]_block_invoke_2 : 104 -> 108
~ ___49+[AXMobileMailGlue accessibilityInitializeBundle]_block_invoke_3 : 1132 -> 1140
~ ___49+[AXMobileMailGlue accessibilityInitializeBundle]_block_invoke_4 : 92 -> 100
~ ___49+[AXMobileMailGlue accessibilityInitializeBundle]_block_invoke_5 : 164 -> 172
~ ___49+[AXMobileMailGlue accessibilityInitializeBundle]_block_invoke.553 : 164 -> 168
~ _AXMobileMailGetSelectedMessageCellElement : 540 -> 588
~ -[MailMailboxGroupedPickerTableCellAccessibility accessibilityLabel] : 96 -> 104
~ -[MailboxOutlineCellAccessibility accessibilityLabel] : 212 -> 228
~ +[MFArrowControlsViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MFArrowControlsViewAccessibility _accessibilityLoadAccessibilityInformation] : 204 -> 220
~ +[MailboxPickerOutlineControllerAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[MailboxPickerOutlineControllerAccessibility shelfButtonItem] : 128 -> 136
~ -[UITableViewAccessibility__MobileMail__UIKit isAccessibilityElement] : 140 -> 144
~ +[MailTrackingProtectionOnboardingViewControllerAccessibility _accessibilityPerformValidations:] : 136 -> 148
~ -[MailTrackingProtectionOnboardingViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 384 -> 396
~ +[UISplitViewControllerPanelImplViewAccessibility__MobileMail__UIKit _accessibilityPerformValidations:] : 148 -> 156
~ -[UISplitViewControllerPanelImplViewAccessibility__MobileMail__UIKit _accessibilityScannerGroupElements] : 464 -> 500
~ -[ComposeNavigationControllerAccessibility setContentVisible:] : 108 -> 112
~ +[ComposePlaceholderViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[ComposePlaceholderViewAccessibility accessibilityValue] : 92 -> 100
~ +[ConversationHeaderContentViewAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[ConversationHeaderContentViewAccessibility _accessibilityLoadAccessibilityInformation] : 296 -> 320
~ +[ConversationViewControllerAccessibility _accessibilityPerformValidations:] : 1960 -> 1968
~ -[ConversationViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 596 -> 656
~ ___85-[ConversationViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 104 -> 112
~ -[ConversationViewControllerAccessibility accessibilityCustomRotors] : 480 -> 500
~ ___68-[ConversationViewControllerAccessibility accessibilityCustomRotors]_block_invoke : 708 -> 716
~ -[ConversationViewControllerAccessibility _axElementForFocusInCell:shouldAllowCollapsedCell:] : 432 -> 464
~ -[ConversationViewControllerAccessibility _accessibilityFirstElementForFocus] : 340 -> 372
~ -[ConversationViewControllerAccessibility _axFirstVisibleExpandedCell] : 428 -> 440
~ ___70-[ConversationViewControllerAccessibility _axFirstVisibleExpandedCell]_block_invoke : 140 -> 144
~ -[ConversationViewControllerAccessibility _axFirstVisibleCell] : 444 -> 452
~ ___62-[ConversationViewControllerAccessibility _axFirstVisibleCell]_block_invoke : 148 -> 156
~ -[ConversationViewControllerAccessibility accessibilityScroll:] : 196 -> 200
~ ___82-[ConversationViewControllerAccessibility _axSimulateTapArrowButtonWithDirection:]_block_invoke : 96 -> 100
~ ___82-[ConversationViewControllerAccessibility _axSimulateTapArrowButtonWithDirection:]_block_invoke_2 : 96 -> 100
~ -[ConversationViewControllerAccessibility _axMessageSubjectView] : 220 -> 244
~ -[ConversationViewControllerAccessibility _accessibilityPerformLeadingActionWithCell:] : 684 -> 692
~ ___86-[ConversationViewControllerAccessibility _accessibilityPerformLeadingActionWithCell:]_block_invoke : 80 -> 84
~ -[ConversationViewControllerAccessibility _scrollToInitialPosition] : 276 -> 284
~ ___67-[ConversationViewControllerAccessibility _scrollToInitialPosition]_block_invoke : 96 -> 100
~ ___104-[ConversationViewControllerAccessibility _shrinkMessagesToBarButton:withInteraction:completionHandler:]_block_invoke : 184 -> 200
~ -[ConversationViewControllerAccessibility arrowControlsView] : 104 -> 108
~ ___87-[ConversationViewControllerAccessibility arrowControlsView:didTapButtonWithDirection:]_block_invoke : 152 -> 168
~ -[ConversationViewControllerAccessibility _selectNextMessageCommandInvoked:] : 316 -> 340
~ -[ConversationViewControllerAccessibility _selectPreviousMessageCommandInvoked:] : 316 -> 340
~ -[ConversationViewControllerAccessibility messageViewController:didTapRevealActionsButton:] : 580 -> 588
~ ___91-[ConversationViewControllerAccessibility messageViewController:didTapRevealActionsButton:]_block_invoke : 80 -> 84
~ -[ConversationViewControllerAccessibility _axCancelMarkAsReadTimer] : 88 -> 92
~ ___81-[ConversationViewControllerAccessibility scheduleAutomaticMarkAsReadForMessage:]_block_invoke_2 : 280 -> 292
~ ___81-[ConversationViewControllerAccessibility scheduleAutomaticMarkAsReadForMessage:]_block_invoke_3 : 280 -> 308
~ -[ConversationViewControllerAccessibility _accessibilityTitleForLeadingActionWithCell:] : 572 -> 592
~ ___87-[ConversationViewControllerAccessibility _accessibilityTitleForLeadingActionWithCell:]_block_invoke : 80 -> 84
~ -[ConversationViewControllerAccessibility _accessibilitySetConversationViewInsets] : 180 -> 188
~ +[DetailViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[DetailViewControllerAccessibility _accessibilitySpeakThisViewController] : 92 -> 100
~ -[UIAccessibilityDismissDraftElement _accessibilityWithdrawActiveItem] : 196 -> 204
~ +[DockContainerViewControllerAccessibility _accessibilityPerformValidations:] : 536 -> 544
~ -[DockContainerViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 424 -> 436
~ -[DockContainerViewControllerAccessibility _accessibilitySpeakThisViewController] : 84 -> 92
~ -[DockContainerViewControllerAccessibility _accessibilityIsMailComposeSceneActive] : 92 -> 96
~ -[DockContainerViewControllerAccessibility _axAddDraftsElementIfNecessaryUsingVC:] : 652 -> 708
~ ___82-[DockContainerViewControllerAccessibility _axAddDraftsElementIfNecessaryUsingVC:]_block_invoke : 216 -> 224
~ -[DockContainerViewControllerAccessibility presentViewController:animated:completion:] : 268 -> 260
~ -[DockContainerViewControllerAccessibility _accessibilityUpdateDraftElements] : 748 -> 792
~ -[DockContainerViewControllerAccessibility _axFrameForDismissDraftsElement] : 252 -> 272
~ -[DockContainerViewControllerAccessibility _axDismissDraftElement] : 404 -> 416
~ -[IndividualSwipeOptionControllerAccessibility tableView:willDisplayCell:forRowAtIndexPath:] : 160 -> 164
~ +[MFCollapsedMessageCellAccessibility _accessibilityPerformValidations:] : 300 -> 312
~ -[MFCollapsedMessageCellAccessibility accessibilityLabel] : 808 -> 896
~ -[MFCollapsedMessageCellAccessibility accessibilityHint] : 136 -> 144
~ +[MFConversationItemFooterViewAccessibility _accessibilityPerformValidations:] : 336 -> 344
~ -[MFConversationItemFooterViewAccessibility _accessibilityLoadAccessibilityInformation] : 600 -> 640
~ ___79-[MFConversationItemFooterViewAccessibility _accessibilityPerformLeadingAction]_block_invoke : 92 -> 96
~ -[MFConversationItemFooterViewAccessibility _accessibilityUpdateLeadingActionTitle:] : 268 -> 280
~ -[MFConversationItemFooterViewAccessibility _accessibilityConversationViewControllerForCell:] : 200 -> 208
~ +[MFConversationItemHeaderBlockAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MFConversationItemHeaderBlockAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ +[MFConversationViewCellAccessibility _accessibilityPerformValidations:] : 556 -> 564
~ -[MFConversationViewCellAccessibility accessibilityCustomActions] : 204 -> 220
~ ___65-[MFConversationViewCellAccessibility accessibilityCustomActions]_block_invoke : 140 -> 144
~ -[MFConversationViewCellAccessibility _accessibilityMessageIndexDescription] : 400 -> 432
~ -[MFConversationViewCellAccessibility _accessibilityMailSwipeActions] : 404 -> 416
~ ___69-[MFConversationViewCellAccessibility _accessibilityMailSwipeActions]_block_invoke : 756 -> 764
~ ___69-[MFConversationViewCellAccessibility _accessibilityMailSwipeActions]_block_invoke.383 : 80 -> 84
~ ___69-[MFConversationViewCellAccessibility _accessibilityMailSwipeActions]_block_invoke_2 : 80 -> 84
~ ___69-[MFConversationViewCellAccessibility _accessibilityMailSwipeActions]_block_invoke_3 : 56 -> 60
~ ___76-[MFConversationViewCellAccessibility _accessibilityPerformMailSwipeAction:]_block_invoke : 232 -> 244
~ +[MFExpandedMessageCellAccessibility _accessibilityPerformValidations:] : 240 -> 248
~ -[MFExpandedMessageCellAccessibility accessibilityLabel] : 284 -> 312
~ -[MFExpandedMessageCellAccessibility accessibilityDragSourceDescriptors] : 152 -> 164
~ -[MFExpandedMessageCellAccessibility accessibilityElements] : 360 -> 384
~ +[MFMailDropBannerViewAccessibility _accessibilityPerformValidations:] : 284 -> 292
~ -[MFMailDropBannerViewAccessibility accessibilityLabel] : 188 -> 208
~ -[MFMailDropBannerViewAccessibility _accessibilityLoadAccessibilityInformation] : 240 -> 252
~ -[MFMailDropBannerViewAccessibility _accessibilitySupplementaryFooterViews] : 212 -> 224
~ +[MFMailboxFilterBarButtonItemAccessibility _accessibilityPerformValidations:] : 204 -> 216
~ -[MFMailboxFilterBarButtonItemAccessibility _accessibilityLoadAccessibilityInformation] : 268 -> 272
~ +[MFMailboxFilterPickerControlAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[MFMailboxFilterPickerControlAccessibility accessibilityLabel] : 84 -> 92
~ -[MFMailboxFilterPickerControlAccessibility accessibilityValue] : 84 -> 92
~ -[MFMailboxFilterPickerControlAccessibility accessibilityFrame] : 192 -> 200
~ +[MFMessageContentViewAccessibility _accessibilityPerformValidations:] : 212 -> 220
~ ___73-[MFMessageContentViewAccessibility generateSnapshotImageWithCompletion:]_block_invoke : 288 -> 296
~ -[MFMessageContentViewAccessibility _accessibilityLoadAccessibilityInformation] : 208 -> 220
~ -[MFMessageHeaderViewAccessibility accessibilityContainerType] : 164 -> 176
~ +[MFMessageViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MFMessageViewControllerAccessibility messageContentView:didFinishRenderingWithHeight:] : 192 -> 200
~ +[MFSwipableCollectionViewLayoutAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[MFSwipableCollectionViewLayoutAccessibility initialLayoutAttributesForAppearingItemAtIndexPath:] : 112 -> 116
~ -[CategorizationOptionViewAccessibility _accessibilityLoadAccessibilityInformation] : 720 -> 752
~ +[MFTiltedTabViewAccessibility _accessibilityPerformValidations:] : 256 -> 264
~ -[MFTiltedTabViewAccessibility _accessibilityLoadAccessibilityInformation] : 268 -> 272
~ ___74-[MFTiltedTabViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 632 -> 660
~ ___74-[MFTiltedTabViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 248 -> 252
~ ___74-[MFTiltedTabViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 156 -> 164
~ -[MFTiltedTabViewAccessibility accessibilityElements] : 112 -> 116
~ -[MFTiltedTabViewAccessibility accessibilityFrame] : 196 -> 200
~ +[MFTriageInteractionAccessibility _accessibilityPerformValidations:] : 140 -> 152
~ -[MFTriageInteractionAccessibility swipeActionWithPreparation:completion:] : 136 -> 144
~ +[MailActionCellAccessibility _accessibilityPerformValidations:] : 296 -> 304
~ -[MailActionCellAccessibility accessibilityLabel] : 152 -> 168
~ -[MailActionCellAccessibility accessibilityTraits] : 716 -> 736
~ ___50-[MailActionCellAccessibility accessibilityTraits]_block_invoke : 80 -> 84
~ ___50-[MailActionCellAccessibility accessibilityTraits]_block_invoke.328 : 80 -> 84
~ +[BucketCollectionViewCellAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[BucketCollectionViewCellAccessibility accessibilityLabel] : 360 -> 388
~ -[UIInheritedViewAccessibility__MobileMail__SwiftUI accessibilityFrame] : 268 -> 276
~ +[MailAppControllerAccessibility _accessibilityPerformValidations:] : 364 -> 376
~ -[MailAppControllerAccessibility _accessibilitySplitViewControllerScannerGroupElements] : 584 -> 612
~ -[MailAppControllerAccessibility _axAccessibilityGroupForKey:fromSplitController:] : 412 -> 424
~ -[MailAppControllerAccessibility _axVisibleViewController] : 292 -> 320
~ -[MailAppControllerAccessibility _accessibilityFirstElementForReadFromTop] : 96 -> 104
~ -[MailAppControllerAccessibility _accessibilityFirstElementForFocus] : 268 -> 288
~ -[MailStatusBarViewAccessibility accessibilityLabel] : 300 -> 312
~ -[MailStatusBarViewAccessibility isAccessibilityElement] : 60 -> 64
~ -[MailStatusBarViewAccessibility accessibilityFrame] : 180 -> 184
~ ___52-[MailStatusBarViewAccessibility accessibilityFrame]_block_invoke : 76 -> 80
~ +[MailStatusLabelViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MailStatusLabelViewAccessibility accessibilityLabel] : 148 -> 160
~ +[MailStatusProgressBarViewAccessibility _accessibilityPerformValidations:] : 196 -> 204
~ -[MailStatusProgressBarViewAccessibility updateWithStatusInfo:] : 184 -> 180
~ ___63-[MailStatusProgressBarViewAccessibility updateWithStatusInfo:]_block_invoke : 396 -> 412
~ ___63-[MailStatusProgressBarViewAccessibility updateWithStatusInfo:]_block_invoke.349 : 80 -> 84
~ -[WKContentViewAccessibility__MobileMail__WebKit accessibilityContainerType] : 164 -> 176
~ -[Mail_UIScrollViewAccessibility _accessibilityVisibleContentInset] : 164 -> 168
~ +[MailboxTableCellAccessibility _accessibilityPerformValidations:] : 484 -> 492
~ -[MailboxTableCellAccessibility setDetailsDisclosureButton:] : 188 -> 200
~ ___69-[MailboxTableCellAccessibility _accessibilityMailboxUsesUnreadCount]_block_invoke : 352 -> 384
~ ___69-[MailboxTableCellAccessibility _accessibilityMailboxUsesUnreadCount]_block_invoke_2 : 80 -> 84
~ -[MailboxTableCellAccessibility accessibilityLabel] : 188 -> 208
~ -[MailboxTableCellAccessibility accessibilityValue] : 328 -> 352
~ -[MailboxTableCellAccessibility accessibilityTraits] : 248 -> 252
~ -[MailboxTableCellAccessibility accessibilityPerformEscape] : 376 -> 400
~ ___59-[MailboxTableCellAccessibility accessibilityPerformEscape]_block_invoke : 80 -> 84
~ ___59-[MailboxTableCellAccessibility accessibilityPerformEscape]_block_invoke_2 : 148 -> 152
~ +[MessageListCollectionViewCellAccessibility _accessibilityPerformValidations:] : 1676 -> 1684
~ -[MessageListCollectionViewCellAccessibility _axSetDisclosureButtonTraits] : 100 -> 104
~ -[MessageListCollectionViewCellAccessibility accessibilityTraits] : 172 -> 176
~ -[MessageListCollectionViewCellAccessibility accessibilityLabel] : 1968 -> 2092
~ ___64-[MessageListCollectionViewCellAccessibility accessibilityLabel]_block_invoke : 124 -> 128
~ -[MessageListCollectionViewCellAccessibility accessibilityHint] : 604 -> 632
~ ___63-[MessageListCollectionViewCellAccessibility accessibilityHint]_block_invoke : 72 -> 76
~ -[MessageListCollectionViewCellAccessibility accessibilityUserInputLabels] : 108 -> 120
~ -[MessageListCollectionViewCellAccessibility _accessibilityPerformCellAction:] : 1204 -> 1208
~ ___78-[MessageListCollectionViewCellAccessibility _accessibilityPerformCellAction:]_block_invoke : 72 -> 76
~ ___78-[MessageListCollectionViewCellAccessibility _accessibilityPerformCellAction:]_block_invoke_2 : 80 -> 84
~ ___78-[MessageListCollectionViewCellAccessibility _accessibilityPerformCellAction:]_block_invoke_3 : 224 -> 236
~ ___78-[MessageListCollectionViewCellAccessibility _accessibilityPerformCellAction:]_block_invoke_5 : 84 -> 88
~ -[MessageListCollectionViewCellAccessibility _accessibilityToggleReadAction:] : 72 -> 76
~ -[MessageListCollectionViewCellAccessibility _accessibilityToggleFlagAction:] : 72 -> 76
~ -[MessageListCollectionViewCellAccessibility _accessibilityRemoveHighImpactAction:] : 72 -> 76
~ -[MessageListCollectionViewCellAccessibility _accessibilityDeleteAction:] : 248 -> 264
~ -[MessageListCollectionViewCellAccessibility _axPostAnnouncementForActionCompletionIfNecessary] : 396 -> 424
~ -[MessageListCollectionViewCellAccessibility _accessibilityMailboxController] : 88 -> 96
~ ___77-[MessageListCollectionViewCellAccessibility _accessibilityMailboxController]_block_invoke : 80 -> 84
~ -[MessageListCollectionViewCellAccessibility _accessibilityToggleThreadAction:] : 292 -> 308
~ ___79-[MessageListCollectionViewCellAccessibility _accessibilityToggleThreadAction:]_block_invoke : 96 -> 100
~ ___82-[MessageListCollectionViewCellAccessibility accessibilityElementDidBecomeFocused]_block_invoke : 100 -> 108
~ -[MessageListCollectionViewCellAccessibility _privateAccessibilityCustomActions] : 1932 -> 2004
~ ___80-[MessageListCollectionViewCellAccessibility _privateAccessibilityCustomActions]_block_invoke : 68 -> 72
~ ___80-[MessageListCollectionViewCellAccessibility _privateAccessibilityCustomActions]_block_invoke_2 : 76 -> 80
~ -[MessageListCollectionViewCellAccessibility _accessibilityScrollStatus] : 256 -> 276
~ ___76-[MessageListCollectionViewCellAccessibility _accessibilityLinkedUIElements]_block_invoke : 304 -> 344
~ -[MessageListCollectionViewCellAccessibility _accessibilityScannerActivateBehavior] : 128 -> 132
~ -[MessageListCollectionViewCellAccessibility _accessibilityIsThreadedChildCell] : 412 -> 428
~ ___79-[MessageListCollectionViewCellAccessibility _accessibilityIsThreadedChildCell]_block_invoke : 72 -> 76
~ -[MessageListCollectionViewCellAccessibility _accessibilityThreadCount] : 76 -> 80
~ -[MessageListCollectionViewCellAccessibility _axProcessMailLabel:children:] : 224 -> 232
~ -[MessageListCollectionViewCellAccessibility _accessibilityThreadedDisclosureButton] : 164 -> 172
~ -[MessageListCollectionViewCellAccessibility automationElements] : 264 -> 280
~ -[MessageListCollectionViewCellAccessibility _accessibilityEquivalenceTag] : 172 -> 192
~ -[MessageListCollectionViewCellAccessibility _accessibilityLabelWithoutAttributes] : 332 -> 372
~ -[MessageListCollectionViewCellAccessibility layoutSubviews] : 196 -> 208
~ -[MessageListCollectionViewCellAccessibility prepareForReuse] : 224 -> 228
~ +[MessageListSearchViewControllerAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ ___90-[MessageListSearchViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 68 -> 72
~ +[MessageListViewControllerAccessibility _accessibilityPerformValidations:] : 600 -> 608
~ -[MessageListViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 600 -> 612
~ ___84-[MessageListViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 112 -> 116
~ ___84-[MessageListViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 240 -> 264
~ -[MessageListViewControllerAccessibility viewWillAppear:] : 128 -> 136
~ -[MessageListViewControllerAccessibility _updateBackButtonImageWithCount:] : 364 -> 404
~ -[MessageListViewControllerAccessibility shelfButtonItem] : 128 -> 136
~ -[MessageListViewControllerAccessibility _axSetCategoryButtonsTrait] : 536 -> 556
~ +[MessageStatusIndicatorManagerAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[MessageStatusIndicatorManagerAccessibility _axLabelForMask:] : 620 -> 692
~ ___62-[MessageStatusIndicatorManagerAccessibility _axValueForMask:]_block_invoke : 80 -> 84
~ -[MessageStatusIndicatorManagerAccessibility statusIndicatorImageWithOptionsMask:] : 144 -> 148
~ -[MessageStatusIndicatorManagerAccessibility _accessibilitySetImageNameForImage:options:] : 188 -> 200
~ +[MessageViewStatusIndicatorManagerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MessageViewStatusIndicatorManagerAccessibility _accessibilityLoadAccessibilityInformation] : 188 -> 196
~ ___92-[MessageViewStatusIndicatorManagerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 84 -> 92
~ _accessibilityLocalizedString : 156 -> 164
~ _accessibilitySubstituteReadPhonemeInString : 96 -> 100
~ _accessibilityLabelForFlagColor : 464 -> 500
~ ___accessibilityApproximateVisibleSummaryText_block_invoke : 116 -> 132
~ ___accessibilityApproximateVisibleSummaryText_block_invoke.350 : 376 -> 392
~ +[MobileMail_UISwipeHandlerAccessibility _accessibilityPerformValidations:] : 252 -> 264
~ -[MobileMail_UISwipeHandlerAccessibility _swipeRecognizerEnded:wasCancelled:] : 332 -> 352
~ -[PSSpecifierAccessibility__MobileMail__Preferences accessibilityLabel] : 180 -> 188
~ +[SelectedColorButtonAccessibility buttonWithType:radius:color:] : 176 -> 184
~ -[StackElementAccessibility itemViewCreateIfNeeded:] : 320 -> 344
~ +[TiltedTabViewControllerAccessibility _accessibilityPerformValidations:] : 496 -> 504
~ -[TiltedTabViewControllerAccessibility _axPrepareDockedLabelForIndex:] : 380 -> 384
~ ___70-[TiltedTabViewControllerAccessibility _axPrepareDockedLabelForIndex:]_block_invoke : 80 -> 84
~ -[TiltedTabViewControllerAccessibility tiltedTabViewDidPresent:] : 228 -> 236
~ -[TiltedTabViewControllerAccessibility tiltedTabView:contentViewForItemAtIndex:] : 124 -> 128
~ -[TiltedTabViewControllerAccessibility tiltedTabView:snapshotViewForItemAtIndex:] : 124 -> 128
~ -[TiltedTabViewControllerAccessibility _accessibilityUpdateDraftLabelForBorrowedView:withActorAtIndex:] : 760 -> 804
~ ___103-[TiltedTabViewControllerAccessibility _accessibilityUpdateDraftLabelForBorrowedView:withActorAtIndex:]_block_invoke_2 : 284 -> 304
~ +[UIApplication(MailAccessibilityCategory) _accessibilityPerformValidations:] : 136 -> 144
~ -[UIApplication(MailAccessibilityCategory) _accessibilityFilenameForAttachmentCID:] : 164 -> 176
~ -[UIApplication(MailAccessibilityCategory) _accessibilityApplicationIsModal] : 92 -> 96
~ +[MobileMail_UIDimmingViewAccessibility _accessibilityPerformValidations:] : 108 -> 116
~ -[MobileMail_UIDimmingViewAccessibility _accessibilityObscuredScreenAllowedViews] : 420 -> 440
~ ___81-[MobileMail_UIDimmingViewAccessibility _accessibilityObscuredScreenAllowedViews]_block_invoke : 80 -> 84
~ -[UIMailToolbarButtonAccessibility accessibilityLabel] : 404 -> 424
~ -[UIViewAccessibility__MobileMail__UIKit _accessibilityUseAccessibilityFrameForHittest] : 120 -> 124
~ -[UIViewAccessibility__MobileMail__UIKit _accessibilityIsFirstElementForFocus] : 120 -> 124
~ -[UIViewAccessibility__MobileMail__UIKit _accessibilityIsApplicationSceneView] : 68 -> 72
~ -[UIViewAccessibility__MobileMail__UIKit accessibilityElements] : 832 -> 884
~ -[UIViewAccessibility__MobileMail__UIKit _accessibilityOverridesInvalidFrames] : 120 -> 124

```
