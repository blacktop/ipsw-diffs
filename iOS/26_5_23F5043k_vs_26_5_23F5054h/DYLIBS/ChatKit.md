## ChatKit

> `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1450.600.13.2.2
-  __TEXT.__text: 0xbb08a4
+1450.600.43.2.1
+  __TEXT.__text: 0xbb0844
   __TEXT.__auth_stubs: 0xc1f0
   __TEXT.__delay_helper: 0xcd0
-  __TEXT.__objc_methlist: 0x70564
-  __TEXT.__const: 0x3bd54
-  __TEXT.__gcc_except_tab: 0x24230
-  __TEXT.__cstring: 0x3c581
-  __TEXT.__oslogstring: 0x4e363
+  __TEXT.__objc_methlist: 0x70664
+  __TEXT.__const: 0x3bd64
+  __TEXT.__gcc_except_tab: 0x242d0
+  __TEXT.__cstring: 0x3c411
+  __TEXT.__oslogstring: 0x4e5f3
   __TEXT.__dlopen_cstrs: 0xb55
-  __TEXT.__ustring: 0x4d6
-  __TEXT.__swift5_typeref: 0x404c2
+  __TEXT.__ustring: 0x1c4
+  __TEXT.__swift5_typeref: 0x40592
   __TEXT.__constg_swiftt: 0x1bd84
   __TEXT.__swift5_builtin: 0x820
   __TEXT.__swift5_reflstr: 0x10d61
   __TEXT.__swift5_fieldmd: 0xf424
   __TEXT.__swift5_assocty: 0x42b0
-  __TEXT.__swift5_capture: 0x79ec
+  __TEXT.__swift5_capture: 0x7a00
   __TEXT.__swift5_proto: 0x1860
   __TEXT.__swift5_types: 0x12a8
   __TEXT.__swift_as_entry: 0x480
   __TEXT.__swift_as_ret: 0x428
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__swift5_mpenum: 0xe8
-  __TEXT.__unwind_info: 0x31f10
+  __TEXT.__unwind_info: 0x31f58
   __TEXT.__eh_frame: 0xddd4
   __TEXT.__objc_classname: 0x12616
-  __TEXT.__objc_methname: 0x117aca
+  __TEXT.__objc_methname: 0x117e4a
   __TEXT.__objc_methtype: 0x257f6
-  __TEXT.__objc_stubs: 0xad820
-  __DATA_CONST.__got: 0x72f8
-  __DATA_CONST.__const: 0xed20
+  __TEXT.__objc_stubs: 0xadac0
+  __DATA_CONST.__got: 0x7300
+  __DATA_CONST.__const: 0xed78
   __DATA_CONST.__objc_classlist: 0x2f08
   __DATA_CONST.__objc_catlist: 0x548
   __DATA_CONST.__objc_protolist: 0x1350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35b78
+  __DATA_CONST.__objc_selrefs: 0x35c20
   __DATA_CONST.__objc_protorefs: 0x518
   __DATA_CONST.__objc_superrefs: 0x19e8
-  __DATA_CONST.__objc_arraydata: 0xf20
+  __DATA_CONST.__objc_arraydata: 0xef0
   __AUTH_CONST.__auth_got: 0x6108
-  __AUTH_CONST.__const: 0x3a178
-  __AUTH_CONST.__cfstring: 0x24200
-  __AUTH_CONST.__objc_const: 0x99c48
-  __AUTH_CONST.__objc_arrayobj: 0xe58
+  __AUTH_CONST.__const: 0x3a228
+  __AUTH_CONST.__cfstring: 0x24120
+  __AUTH_CONST.__objc_const: 0x99ce8
+  __AUTH_CONST.__objc_arrayobj: 0xe28
   __AUTH_CONST.__objc_intobj: 0x1008
   __AUTH_CONST.__objc_doubleobj: 0x880
   __AUTH_CONST.__objc_floatobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH.__objc_data: 0x28970
   __AUTH.__data: 0x13e28
-  __DATA.__objc_ivar: 0x48f0
-  __DATA.__data: 0x1fbf8
+  __DATA.__objc_ivar: 0x48fc
+  __DATA.__data: 0x1fc18
   __DATA.__objc_stublist: 0x38
-  __DATA.__bss: 0x3aae0
+  __DATA.__bss: 0x3ab10
   __DATA.__common: 0x1370
   __DATA_DIRTY.__objc_data: 0x87a0
   __DATA_DIRTY.__data: 0x7a8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F67859B7-28EA-33C7-9405-BE79DE4E8299
-  Functions: 70606
-  Symbols:   146697
-  CStrings:  59619
+  UUID: 58AC89A8-17FD-3E0A-9BA2-9FF02B919E30
+  Functions: 70636
+  Symbols:   146801
+  CStrings:  59645
 
Symbols:
+ -[CKComposition isForwardedAudioMessage]
+ -[CKComposition setIsForwardedAudioMessage:]
+ -[CKCoreChatController isHoldingPosterKeyboardFrameUpdatesForPosterRenderingTranscriptBackground:]
+ -[CKCoreChatController posterKeyboardUpdateHoldReasons]
+ -[CKCoreChatController setPosterKeyboardUpdateHoldReasons:]
+ -[CKCoreChatController(Background_Crossplatform) _currentBackgroundCanDockTranscript]
+ -[CKCoreChatController(Backgrounds) beginHoldingPosterKeyboardUpdatesForReason:]
+ -[CKCoreChatController(Backgrounds) endHoldingPosterKeyboardUpdatesForReason:]
+ -[CKGroupRecipientSelectionController _convertHandles:toAccount:]
+ -[CKGroupRecipientSelectionController _needsRetargetBeforeAddingParticipantsForService:]
+ -[CKGroupRecipientSelectionController showHawkingWarning]
+ -[CKGroupRecipientSelectionController supportsHawkingWarning]
+ -[CKIMComposeRecipient description]
+ -[CKIMDaemonController fileTransfer:acceptedWithPath:autoRename:overwrite:options:source:]
+ -[CKPosterRenderingTranscriptBackground _shouldBeSendingKeyboardEventsToBackground]
+ -[CKPosterRenderingTranscriptBackground keyboardFrameDidChange:accountingForSalientRectFrame:duration:curve:isVisible:].cold.1
+ -[CKPosterRenderingTranscriptBackground keyboardWillHideFromFrame:toFrame:duration:curve:isVisible:].cold.1
+ -[CKPosterRenderingTranscriptBackground keyboardWillShowFromFrame:toFrame:duration:curve:isVisible:].cold.1
+ -[CKRecipientSelectionController _hawkingWarningString]
+ -[CKRecipientSelectionController _makeServiceLabelSubviews]
+ -[CKRecipientSelectionController installServiceLabelInView:]
+ -[CKRecipientSelectionController refreshHawkingWarningVisibility]
+ -[CKRecipientSelectionController refreshHawkingWarningVisibility].cold.1
+ -[CKRecipientSelectionController refreshHawkingWarningVisibility].cold.2
+ -[CKRecipientSelectionController refreshServiceLabelScrollInsets]
+ -[CKRecipientSelectionController serviceLabelContainerView]
+ -[CKRecipientSelectionController setHawkingWarningVisibilityFetchQueue:]
+ -[CKRecipientSelectionController setHawkingWarningVisibilityFetchToken:]
+ -[CKRecipientSelectionController setServiceLabelContainerView:]
+ -[CKRecipientSelectionController showHawkingWarning]
+ -[CKRecipientSelectionController supportsHawkingWarning]
+ -[CKUIBehavior macAddToGroupDialogMaximumSize]
+ -[CKUIBehavior macAddToGroupDialogMaximumSize].cold.1
+ -[CKUIBehavior macAddToGroupDialogMinimumSize]
+ -[CKUIBehavior macAddToGroupDialogMinimumSize].cold.1
+ GCC_except_table246
+ GCC_except_table342
+ _CKTranscriptBackgroundKeyboardUpdateHoldReasonInlineReply
+ _CKTranscriptIgnoreContentOffsetUpdatesReasonTranscriptOverlayViewControllerPresentation
+ _IMChatPropertyRCSGroupURI
+ _OBJC_IVAR_$_CKComposition._isForwardedAudioMessage
+ _OBJC_IVAR_$_CKCoreChatController._posterKeyboardUpdateHoldReasons
+ _OBJC_IVAR_$_CKRecipientSelectionController._hawkingWarningVisibility
+ _OBJC_IVAR_$_CKRecipientSelectionController._hawkingWarningVisibilityFetchQueue
+ _OBJC_IVAR_$_CKRecipientSelectionController._hawkingWarningVisibilityFetchToken
+ _OBJC_IVAR_$_CKRecipientSelectionController._serviceLabelContainerView
+ ___115-[CKChatController _presentCollabAddToMessagesGroupAlertIfNecessary:collaborationType:sendBlock:completionHandler:]_block_invoke.1431
+ ___145-[CKChatController _sendAutomaticallyPlacedSticker:stickerReactionSession:forChatItem:forParentChatItem:stickerFrame:animationCompletionHandler:]_block_invoke.1287
+ ___39-[CKChatController addToCollaboration:]_block_invoke.1655
+ ___39-[CKChatController addToCollaboration:]_block_invoke_2.1657
+ ___43-[CKComposeChatController sendComposition:]_block_invoke.370
+ ___45-[CKChatController _handleChatItemDidChange:]_block_invoke.1632
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.799
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.802
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.800
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.803
+ ___46-[CKUIBehavior macAddToGroupDialogMaximumSize]_block_invoke
+ ___46-[CKUIBehavior macAddToGroupDialogMinimumSize]_block_invoke
+ ___47-[CKChatController sendComposition:animations:]_block_invoke.892
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1562
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1566
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_2.1567
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_3.1571
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_4.1575
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_5.1576
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_6.1580
+ ___53-[CKChatController _showOrHideNicknameBannerIfNeeded]_block_invoke.1647
+ ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke.448
+ ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke.449
+ ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke.453
+ ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke.462
+ ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke_2.454
+ ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke_3.456
+ ___58-[CKChatController chatInputControllerDidSelectFunCamera:]_block_invoke.1283
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1453
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1456
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1454
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1458
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1338
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1339
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1340
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1340.cold.1
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1341
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1342
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1343
+ ___65-[CKRecipientSelectionController refreshHawkingWarningVisibility]_block_invoke
+ ___65-[CKRecipientSelectionController refreshHawkingWarningVisibility]_block_invoke.671
+ ___65-[CKRecipientSelectionController refreshHawkingWarningVisibility]_block_invoke_2
+ ___67-[CKChatController _sendCompositionForNewCloudKitShare:completion:]_block_invoke.1402
+ ___68-[CKChatController verifyCompositionSendForFileProvider:completion:]_block_invoke.1333
+ ___68-[CKChatController verifyCompositionSendForFileProvider:completion:]_block_invoke.1335
+ ___69-[CKChatController nicknameBannerView:actionButtonTapped:forUpdates:]_block_invoke.1649
+ ___69-[CKRecipientSelectionController _openStewieAppForRoadsideIfRequired]_block_invoke.488
+ ___69-[CKRecipientSelectionController _openStewieAppForRoadsideIfRequired]_block_invoke.488.cold.1
+ ___69-[CKRecipientSelectionController _openStewieAppForRoadsideIfRequired]_block_invoke.489
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1412
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1413
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1414
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1416
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1418
+ ___70-[CKRecipientSelectionController _openStewieAppForEmergencyIfRequired]_block_invoke.485
+ ___70-[CKRecipientSelectionController _openStewieAppForEmergencyIfRequired]_block_invoke.485.cold.1
+ ___70-[CKRecipientSelectionController _openStewieAppForEmergencyIfRequired]_block_invoke.486
+ ___71-[CKCoreChatController(Backgrounds) _setupTranscriptBackgroundIfNeeded]_block_invoke.287.cold.1
+ ___71-[CKCoreChatController(Backgrounds) _setupTranscriptBackgroundIfNeeded]_block_invoke.290
+ ___71-[CKCoreChatController(Backgrounds) _setupTranscriptBackgroundIfNeeded]_block_invoke_2.291
+ ___72-[CKChatController _verifyCompositionSendForNewFileProvider:completion:]_block_invoke.1368
+ ___72-[CKChatController _verifyCompositionSendForNewFileProvider:completion:]_block_invoke.1369
+ ___72-[CKChatController textPasteConfigurationSupporting:transformPasteItem:]_block_invoke.1696
+ ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1371
+ ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1372
+ ___75-[CKCoreChatController(Backgrounds) updateTranscriptBackground:transferID:]_block_invoke.315
+ ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1379
+ ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1380
+ ___77-[CKChatController selectedBalloonIntersectingRect:chatItemForRepositioning:]_block_invoke.1275
+ ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1419
+ ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1420
+ ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke_2.1421
+ ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1446
+ ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1447
+ ___86-[CKRecipientSelectionController refreshAvailabilityForRecipients:context:completion:]_block_invoke.509
+ ___87-[CKChatController _removeSubsharesAndSendFileProviderComposition:shareURL:completion:]_block_invoke.1393
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1387
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1387.cold.1
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1388
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1390
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1391
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke_2.1392
+ ___89-[CKCoreChatController(Backgrounds) _transitionToPosterKitPosterConfiguration:onChannel:]_block_invoke.308
+ ___89-[CKCoreChatController(Backgrounds) _transitionToPosterKitPosterConfiguration:onChannel:]_block_invoke.308.cold.1
+ ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1355
+ ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1357
+ ___94-[CKCoreChatController(Backgrounds) _updateChannelToUseConfigurationDuringTestWithCompletion:]_block_invoke.265
+ ___94-[CKCoreChatController(Backgrounds) _updateChannelToUseConfigurationDuringTestWithCompletion:]_block_invoke_2.270
+ ___95-[CKChatController _updateAndSendCompositionForExistingCloudKitShare:share:attempt:completion:]_block_invoke.1410
+ ___Block_byref_object_copy_.1866
+ ___Block_byref_object_dispose_.1867
+ ___block_descriptor_32_e8_Q12?0B8l
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0ls32l8s40l8w64l8s48l8s56l8
+ ___block_literal_global.1206
+ ___block_literal_global.1295
+ ___block_literal_global.1310
+ ___block_literal_global.1316
+ ___block_literal_global.1322
+ ___block_literal_global.1359
+ ___block_literal_global.1429
+ ___block_literal_global.1644
+ ___block_literal_global.1646
+ ___block_literal_global.1756
+ ___block_literal_global.1758
+ ___block_literal_global.1763
+ ___block_literal_global.1771
+ ___block_literal_global.1774
+ ___block_literal_global.1782
+ ___block_literal_global.1784
+ ___block_literal_global.1786
+ ___block_literal_global.1788
+ ___block_literal_global.1790
+ ___block_literal_global.1792
+ ___block_literal_global.1796
+ ___block_literal_global.1812
+ ___block_literal_global.2198
+ ___block_literal_global.2274
+ ___block_literal_global.2276
+ ___block_literal_global.2340
+ ___block_literal_global.2407
+ ___block_literal_global.2422
+ ___block_literal_global.2424
+ ___block_literal_global.2479
+ ___block_literal_global.2481
+ ___block_literal_global.2620
+ ___block_literal_global.2622
+ ___block_literal_global.2665
+ ___block_literal_global.2667
+ ___block_literal_global.4140
+ ___block_literal_global.4150
+ ___block_literal_global.4152
+ ___block_literal_global.512
+ ___block_literal_global.6174
+ ___block_literal_global.6176
+ ___block_literal_global.6183
+ ___block_literal_global.6232
+ ___block_literal_global.6236
+ ___block_literal_global.6246
+ ___block_literal_global.6250
+ ___block_literal_global.6264
+ ___block_literal_global.6268
+ ___block_literal_global.6327
+ ___block_literal_global.6331
+ ___block_literal_global.6341
+ ___block_literal_global.6345
+ ___block_literal_global.6361
+ ___block_literal_global.6367
+ ___block_literal_global.6371
+ ___block_literal_global.6380
+ ___block_literal_global.6389
+ ___block_literal_global.6393
+ ___block_literal_global.6415
+ ___block_literal_global.6419
+ ___block_literal_global.6431
+ ___block_literal_global.6440
+ ___block_literal_global.6460
+ ___block_literal_global.6472
+ ___block_literal_global.6474
+ ___block_literal_global.6476
+ ___block_literal_global.6478
+ ___block_literal_global.845
+ ___block_literal_global.865
+ _areBannersSupported.once.6434
+ _areBannersSupported.once.6454
+ _attachmentBrowserDefaultSizeForSquare.once.6317
+ _attachmentBrowserDefaultSizeForSquare.sBehavior.6316.0
+ _attachmentBrowserDefaultSizeForSquare.sBehavior.6316.1
+ _attachmentBrowserGridInterItemSpacing.once.6321
+ _attachmentBrowserGridInterItemSpacing.sBehavior.6320
+ _canPresentOverKeyboard.once.6202
+ _canShowContactPhotosInConversationList.once.6238
+ _canShowContactPhotosInConversationList.sBehavior.6237
+ _contactPhotoTranscriptInsets.sBehavior.6269
+ _conversationListMinimumWidthForHiddenContactImage.once.6254
+ _conversationListMinimumWidthForHiddenContactImage.sBehavior.6253
+ _conversationListMultiSelectAccessoryUsesDefaultStyling.once.6248
+ _conversationListMultiSelectAccessoryUsesDefaultStyling.sBehavior.6247
+ _conversationListPrefersEditButtonOnTrailingEdge.once.6244
+ _conversationListPrefersEditButtonOnTrailingEdge.sBehavior.6243
+ _defaultAVPlayerViewContorllerControlsInsets.once.6277
+ _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6276.0
+ _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6276.1
+ _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6276.2
+ _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6276.3
+ _defaultConversationViewingMessageCount.once.6230
+ _defaultConversationViewingMessageCount.sBehavior.6229
+ _detonatedItemBalloonViewSize.once.6365
+ _detonatedItemBalloonViewSize.sBehavior.6364.0
+ _detonatedItemBalloonViewSize.sBehavior.6364.1
+ _detonatedItemDocumentIconSize.once.6369
+ _detonatedItemDocumentIconSize.sBehavior.6368.0
+ _detonatedItemDocumentIconSize.sBehavior.6368.1
+ _documentIconSize.once.6281
+ _documentIconSize.sBehavior.6280.0
+ _documentIconSize.sBehavior.6280.1
+ _entryFieldShouldUseBackdropView.once.6387
+ _entryFieldShouldUseBackdropView.once.6413
+ _entryViewAlwaysUsesConcentricPadding.once.6297
+ _entryViewAlwaysUsesConcentricPadding.sBehavior.6296
+ _entryViewConcentricPadding.once.6301
+ _entryViewConcentricPadding.sBehavior.6300
+ _entryViewHorizontalCoverInsets.once.6399
+ _entryViewHorizontalCoverInsets.once.6424
+ _entryViewHorizontalCoverInsets.sBehavior.6398.0
+ _entryViewHorizontalCoverInsets.sBehavior.6398.1
+ _entryViewHorizontalCoverInsets.sBehavior.6398.2
+ _entryViewHorizontalCoverInsets.sBehavior.6398.3
+ _entryViewHorizontalCoverInsets.sBehavior.6423.0
+ _entryViewHorizontalCoverInsets.sBehavior.6423.1
+ _entryViewHorizontalCoverInsets.sBehavior.6423.2
+ _entryViewHorizontalCoverInsets.sBehavior.6423.3
+ _entryViewMaxHandWritingPluginShelfHeight.once.6313
+ _entryViewMaxHandWritingPluginShelfHeight.sBehavior.6312
+ _entryViewVerticalCoverInsets.once.6395
+ _entryViewVerticalCoverInsets.once.6421
+ _entryViewVerticalCoverInsets.sBehavior.6394
+ _entryViewVerticalCoverInsets.sBehavior.6420
+ _get_witness_table 7SwiftUI16ScrollViewReaderVyAA15ModifiedContentVyAA0D0PAAE12onTapGesture5count7performQrSi_yyctFQOyAG011_QuickLook_aB0E05quickN7Preview_2inQrAA7BindingVy10Foundation3URLVSgG_qd__tSkRd__AR7ElementRtd__lFQOy20CommunicationDetails0wcD0VyAA6ZStackVyAA05TupleD0VyAEyAEyAEy7ChatKit023KeyboardListenerWrapperD0VAA12_FrameLayoutVGAA14_OpacityEffectVGAA25_AppearanceActionModifierVG_AEyAEyAA9LazyVGridVyAA7ForEachVys18EnumeratedSequenceVySayA2_0w9WalletTabD0V10WalletPassVGGSSAEyAEyAgAEAhiJQrSi_yyctFQOyA21_04CellD0V_Qo_A2_0w6DoubleiJ8ModifierVGA2_0wD17CommonContextMenuVGGGAA14_PaddingLayoutVGA38_GtGGG_SayARGQo__Qo_AA31AccessibilityAttachmentModifierVGGAaFHPyHC.196
+ _groupRecipientSelectionPresentationStyle.once.6343
+ _groupRecipientSelectionPresentationStyle.sBehavior.6342
+ _isAppStripInKeyboard.once.6305
+ _joystickUsesWindow.once.6383
+ _joystickUsesWindow.once.6409
+ _keyboardSizeDeterminesAppCardDetentHeight.once.6206
+ _lowClearanceInLandscape.once.6194
+ _macAddToGroupDialogMaximumSize.once
+ _macAddToGroupDialogMaximumSize.sBehavior.0
+ _macAddToGroupDialogMaximumSize.sBehavior.1
+ _macAddToGroupDialogMinimumSize.once
+ _macAddToGroupDialogMinimumSize.sBehavior.0
+ _macAddToGroupDialogMinimumSize.sBehavior.1
+ _minTranscriptMarginInsets.once.6273
+ _minTranscriptMarginInsets.sBehavior.6272.1
+ _minTranscriptMarginInsets.sBehavior.6272.3
+ _numberOfButtonsInPhotoPicker.once.6329
+ _numberOfButtonsInPhotoPicker.sBehavior.6328
+ _objc_msgSend$_convertHandles:toAccount:
+ _objc_msgSend$_currentBackgroundCanDockTranscript
+ _objc_msgSend$_hawkingWarningString
+ _objc_msgSend$_makeServiceLabelSubviews
+ _objc_msgSend$_needsRetargetBeforeAddingParticipantsForService:
+ _objc_msgSend$_shouldBeSendingKeyboardEventsToBackground
+ _objc_msgSend$_targetToService:newComposition:supportsEncryption:
+ _objc_msgSend$beginHoldingPosterKeyboardUpdatesForReason:
+ _objc_msgSend$endHoldingPosterKeyboardUpdatesForReason:
+ _objc_msgSend$installServiceLabelInView:
+ _objc_msgSend$isForwardedAudioMessage
+ _objc_msgSend$isHoldingPosterKeyboardFrameUpdatesForPosterRenderingTranscriptBackground:
+ _objc_msgSend$macAddToGroupDialogMaximumSize
+ _objc_msgSend$macAddToGroupDialogMinimumSize
+ _objc_msgSend$originalUnformattedID
+ _objc_msgSend$posterKeyboardUpdateHoldReasons
+ _objc_msgSend$refreshHawkingWarningVisibility
+ _objc_msgSend$refreshServiceLabelScrollInsets
+ _objc_msgSend$serviceLabelContainerView
+ _objc_msgSend$setBreaksLinesForInteractiveText:
+ _objc_msgSend$setFallbackStyle:
+ _objc_msgSend$setIsForwardedAudioMessage:
+ _objc_msgSend$setPosterKeyboardUpdateHoldReasons:
+ _objc_msgSend$setServiceLabelContainerView:
+ _objc_msgSend$showHawkingWarning
+ _objc_msgSend$stringFromContact:
+ _objc_msgSend$supportsHawkingWarning
+ _photoPickerMaxPopoverPhotoHeight.once.6335
+ _photoPickerMaxPopoverPhotoHeight.sBehavior.6334
+ _photoPickerPopoverWidth.once.6325
+ _photoPickerPopoverWidth.sBehavior.6324
+ _presentForwardingUIModally.once.6214
+ _presentsAutocompleteInAPopover.once.6293
+ _presentsQuickLookController.once.6210
+ _presentsQuickLookController.sBehavior.6209
+ _previewMaxWidth.once.6258
+ _previewMaxWidth.sBehavior.6257
+ _resetsIdleTimer.once.6442
+ _resetsIdleTimer.once.6462
+ _searchLinksThumbnailWidth.once.6355
+ _searchLinksThumbnailWidth.sBehavior.6354
+ _searchPhotosThumbnailWidth.once.6353
+ _searchPhotosThumbnailWidth.sBehavior.6352
+ _shouldAlignRecipientGlyphsWithMargins.once.6339
+ _shouldAlignRecipientGlyphsWithMargins.sBehavior.6338
+ _shouldRefreshAlternateAddressesSheet.once.6289
+ _shouldRefreshAlternateAddressesSheet.sBehavior.6288
+ _shouldShowDisclosureChevronInRecipientAtoms.once.6285
+ _shouldSuppressRotationInNewCompose.once.6190
+ _shouldUnreadIndicatorChangeOnSelection.once.6252
+ _shouldUnreadIndicatorChangeOnSelection.sBehavior.6251
+ _shouldUseSimpleTimestampsInTranscript.once.6438
+ _shouldUseSimpleTimestampsInTranscript.once.6458
+ _shouldUseSimpleTimestampsInTranscript.sBehavior.6437
+ _shouldUseSimpleTimestampsInTranscript.sBehavior.6457
+ _showMMSSetup.once.6226
+ _showPendingInConversationList.once.6234
+ _showPendingInConversationList.sBehavior.6233
+ _showsConversationListCellChevronImage.once.6240
+ _showsConversationListCellChevronImage.sBehavior.6239
+ _suggestedAppStripLimit.once.6357
+ _suggestedAppStripLimit.sBehavior.6356
+ _supportedInterfaceOrientations.once.6222
+ _supportedInterfaceOrientations.sBehavior.6221
+ _supportsEntryViewPlusButtonLongPress.once.6309
+ _supportsEntryViewPlusButtonLongPress.sBehavior.6308
+ _symbolic So22CKNavigationControllerC
+ _symbolic _____y_____y_____y_____y_____y_____yADyADy__________G_____G_____G_ADyADy_____y_____y_____ySay_____GGSSADyADy_____y______Qo______G_____GGG_____GAZGtGGG_Say_____GQo__Qo_ 7SwiftUI4ViewPAAE12onTapGesture5count7performQrSi_yyctFQO AC011_QuickLook_aB0E05quickJ7Preview_2inQrAA7BindingVy10Foundation3URLVSgG_qd__tSkRd__AN7ElementRtd__lFQO 20CommunicationDetails0s6ScrollC0V AA6ZStackV AA05TupleC0V AA15ModifiedContentV 7ChatKit023KeyboardListenerWrapperC0V AA12_FrameLayoutV AA14_OpacityEffectV AA25_AppearanceActionModifierV AA9LazyVGridV AA7ForEachV s18EnumeratedSequenceV A0_0s9WalletTabC0V10WalletPassV AcAEAdeFQrSi_yyctFQO A16_04CellC0V A0_0s6DoubleeF8ModifierV A0_0sC17CommonContextMenuV AA14_PaddingLayoutV AN
+ _symbolic _____y_____y_____y_____y_____y_____y_____yAByAByABy__________G_____G_____G_AByABy_____y_____y_____ySay_____GGSSAByABy_____y______Qo______G_____GGG_____GA_GtGGG_Say_____GQo__Qo______GG 7SwiftUI16ScrollViewReaderV AA15ModifiedContentV AA0D0PAAE12onTapGesture5count7performQrSi_yyctFQO AG011_QuickLook_aB0E05quickN7Preview_2inQrAA7BindingVy10Foundation3URLVSgG_qd__tSkRd__AR7ElementRtd__lFQO 20CommunicationDetails0wcD0V AA6ZStackV AA05TupleD0V 7ChatKit023KeyboardListenerWrapperD0V AA12_FrameLayoutV AA14_OpacityEffectV AA25_AppearanceActionModifierV AA9LazyVGridV AA7ForEachV s18EnumeratedSequenceV A2_0w9WalletTabD0V10WalletPassV AgAEAhiJQrSi_yyctFQO A18_04CellD0V A2_0w6DoubleiJ8ModifierV A2_0wD17CommonContextMenuV AA14_PaddingLayoutV AR AA31AccessibilityAttachmentModifierV
+ _theme.once.6181
+ _theme.once.6378
+ _theme.once.6405
+ _theme.once.6429
+ _theme.once.6450
+ _theme.sBehavior.6180
+ _theme.sBehavior.6377
+ _theme.sBehavior.6404
+ _theme.sBehavior.6428
+ _theme.sBehavior.6449
+ _transcriptContactImageDiameter.once.6262
+ _transcriptContactImageDiameter.sBehavior.6261
+ _transcriptGroupTypingContactImageDiameter.once.6266
+ _transcriptGroupTypingContactImageDiameter.sBehavior.6265
+ _transcriptHeaderViewMaxRows.once.6218
+ _transcriptHeaderViewMaxRows.sBehavior.6217
+ _usesActionMenu.once.6391
+ _usesActionMenu.once.6417
+ _usesPopovers.once.6198
+ _usesPopovers.sBehavior.6197
+ _usesUncollapsedSplitview.once.6186
+ _usesUncollapsedSplitview.sBehavior.6185
- -[CKComposeChatController _invalidateBlackholeAlertView]
- -[CKComposeChatController _updateBlackholeAlertView]
- -[CKComposeChatController _updateBlackholeAlertView].cold.1
- -[CKComposeChatController _updateBlackholeAlertView].cold.2
- -[CKComposeChatController _updateBlackholeAlertView].cold.3
- -[CKComposeChatController blackholeAlertView]
- -[CKComposeChatController setBlackholeAlertStatusQueue:]
- -[CKComposeChatController setBlackholeAlertView:]
- -[CKComposeChatController viewDidDisappear:]
- -[CKIMDaemonController fileTransfer:acceptedWithPath:autoRename:overwrite:options:]
- GCC_except_table108
- GCC_except_table165
- GCC_except_table326
- _OBJC_IVAR_$_CKComposeChatController._blackholeAlertStatus
- _OBJC_IVAR_$_CKComposeChatController._blackholeAlertStatusQueue
- _OBJC_IVAR_$_CKComposeChatController._blackholeAlertView
- ___115-[CKChatController _presentCollabAddToMessagesGroupAlertIfNecessary:collaborationType:sendBlock:completionHandler:]_block_invoke.1421
- ___145-[CKChatController _sendAutomaticallyPlacedSticker:stickerReactionSession:forChatItem:forParentChatItem:stickerFrame:animationCompletionHandler:]_block_invoke.1277
- ___39-[CKChatController addToCollaboration:]_block_invoke.1646
- ___39-[CKChatController addToCollaboration:]_block_invoke_2.1648
- ___43-[CKComposeChatController sendComposition:]_block_invoke.373
- ___43-[CKServiceChatItem _showsEncryptedSubtext]_block_invoke
- ___45-[CKChatController _handleChatItemDidChange:]_block_invoke.1623
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.788
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.791
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.789
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.792
- ___47-[CKChatController sendComposition:animations:]_block_invoke.881
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1552
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1556
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_2.1558
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_3.1562
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_4.1566
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_5.1567
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_6.1571
- ___52-[CKComposeChatController _updateBlackholeAlertView]_block_invoke
- ___52-[CKComposeChatController _updateBlackholeAlertView]_block_invoke_2
- ___53-[CKChatController _showOrHideNicknameBannerIfNeeded]_block_invoke.1638
- ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke.451
- ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke.452
- ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke.456
- ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke.465
- ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke_2.457
- ___57-[CKComposeChatController messageEntryViewSendButtonHit:]_block_invoke_3.459
- ___57-[CKRecipientSelectionController sendingServiceEncrypted]_block_invoke
- ___58-[CKChatController chatInputControllerDidSelectFunCamera:]_block_invoke.1273
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1443
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1446
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1444
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1448
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1328
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1329
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1330
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1330.cold.1
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1331
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1332
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1333
- ___67-[CKChatController _sendCompositionForNewCloudKitShare:completion:]_block_invoke.1392
- ___68-[CKChatController verifyCompositionSendForFileProvider:completion:]_block_invoke.1323
- ___68-[CKChatController verifyCompositionSendForFileProvider:completion:]_block_invoke.1325
- ___69-[CKChatController nicknameBannerView:actionButtonTapped:forUpdates:]_block_invoke.1640
- ___69-[CKRecipientSelectionController _openStewieAppForRoadsideIfRequired]_block_invoke.490
- ___69-[CKRecipientSelectionController _openStewieAppForRoadsideIfRequired]_block_invoke.490.cold.1
- ___69-[CKRecipientSelectionController _openStewieAppForRoadsideIfRequired]_block_invoke.491
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1402
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1403
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1404
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1406
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1408
- ___70-[CKRecipientSelectionController _openStewieAppForEmergencyIfRequired]_block_invoke.487
- ___70-[CKRecipientSelectionController _openStewieAppForEmergencyIfRequired]_block_invoke.487.cold.1
- ___70-[CKRecipientSelectionController _openStewieAppForEmergencyIfRequired]_block_invoke.488
- ___71-[CKCoreChatController(Backgrounds) _setupTranscriptBackgroundIfNeeded]_block_invoke.284
- ___71-[CKCoreChatController(Backgrounds) _setupTranscriptBackgroundIfNeeded]_block_invoke.284.cold.1
- ___71-[CKCoreChatController(Backgrounds) _setupTranscriptBackgroundIfNeeded]_block_invoke_2.288
- ___72-[CKChatController _verifyCompositionSendForNewFileProvider:completion:]_block_invoke.1358
- ___72-[CKChatController _verifyCompositionSendForNewFileProvider:completion:]_block_invoke.1359
- ___72-[CKChatController textPasteConfigurationSupporting:transformPasteItem:]_block_invoke.1687
- ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1361
- ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1362
- ___75-[CKCoreChatController(Backgrounds) updateTranscriptBackground:transferID:]_block_invoke.312
- ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1369
- ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1370
- ___77-[CKChatController selectedBalloonIntersectingRect:chatItemForRepositioning:]_block_invoke.1265
- ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1409
- ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1410
- ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke_2.1411
- ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1436
- ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1437
- ___86-[CKRecipientSelectionController refreshAvailabilityForRecipients:context:completion:]_block_invoke.511
- ___87-[CKChatController _removeSubsharesAndSendFileProviderComposition:shareURL:completion:]_block_invoke.1383
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1377
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1377.cold.1
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1378
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1380
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1381
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke_2.1382
- ___89-[CKCoreChatController(Backgrounds) _transitionToPosterKitPosterConfiguration:onChannel:]_block_invoke.305
- ___89-[CKCoreChatController(Backgrounds) _transitionToPosterKitPosterConfiguration:onChannel:]_block_invoke.305.cold.1
- ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1345
- ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1347
- ___94-[CKCoreChatController(Backgrounds) _updateChannelToUseConfigurationDuringTestWithCompletion:]_block_invoke.262
- ___94-[CKCoreChatController(Backgrounds) _updateChannelToUseConfigurationDuringTestWithCompletion:]_block_invoke_2.267
- ___95-[CKChatController _updateAndSendCompositionForExistingCloudKitShare:share:attempt:completion:]_block_invoke.1400
- ___Block_byref_object_copy_.1857
- ___Block_byref_object_dispose_.1858
- ___block_literal_global.1190
- ___block_literal_global.1196
- ___block_literal_global.1285
- ___block_literal_global.1309
- ___block_literal_global.1312
- ___block_literal_global.1419
- ___block_literal_global.1439
- ___block_literal_global.1479
- ___block_literal_global.1672
- ___block_literal_global.1729
- ___block_literal_global.1747
- ___block_literal_global.1754
- ___block_literal_global.1762
- ___block_literal_global.1765
- ___block_literal_global.1773
- ___block_literal_global.1775
- ___block_literal_global.1777
- ___block_literal_global.2202
- ___block_literal_global.2204
- ___block_literal_global.2331
- ___block_literal_global.2336
- ___block_literal_global.2397
- ___block_literal_global.2410
- ___block_literal_global.2412
- ___block_literal_global.2427
- ___block_literal_global.2482
- ___block_literal_global.2484
- ___block_literal_global.2621
- ___block_literal_global.2623
- ___block_literal_global.381
- ___block_literal_global.4131
- ___block_literal_global.4141
- ___block_literal_global.4143
- ___block_literal_global.514
- ___block_literal_global.524
- ___block_literal_global.6166
- ___block_literal_global.6168
- ___block_literal_global.6175
- ___block_literal_global.6180
- ___block_literal_global.6184
- ___block_literal_global.6234
- ___block_literal_global.6238
- ___block_literal_global.6248
- ___block_literal_global.6260
- ___block_literal_global.6263
- ___block_literal_global.6267
- ___block_literal_global.6325
- ___block_literal_global.6329
- ___block_literal_global.6351
- ___block_literal_global.6353
- ___block_literal_global.6355
- ___block_literal_global.6372
- ___block_literal_global.6377
- ___block_literal_global.6381
- ___block_literal_global.6399
- ___block_literal_global.6403
- ___block_literal_global.641
- ___block_literal_global.6423
- ___block_literal_global.6428
- ___block_literal_global.6432
- ___block_literal_global.6448
- ___block_literal_global.6462
- ___block_literal_global.6466
- ___block_literal_global.6468
- ___block_literal_global.799
- ___block_literal_global.854
- _areBannersSupported.once.6426
- _areBannersSupported.once.6446
- _attachmentBrowserDefaultSizeForSquare.once.6309
- _attachmentBrowserDefaultSizeForSquare.sBehavior.6308.0
- _attachmentBrowserDefaultSizeForSquare.sBehavior.6308.1
- _attachmentBrowserGridInterItemSpacing.once.6313
- _attachmentBrowserGridInterItemSpacing.sBehavior.6312
- _canPresentOverKeyboard.once.6194
- _canShowContactPhotosInConversationList.once.6230
- _canShowContactPhotosInConversationList.sBehavior.6229
- _contactPhotoTranscriptInsets.sBehavior.6261
- _conversationListMinimumWidthForHiddenContactImage.once.6246
- _conversationListMinimumWidthForHiddenContactImage.sBehavior.6245
- _conversationListMultiSelectAccessoryUsesDefaultStyling.once.6240
- _conversationListMultiSelectAccessoryUsesDefaultStyling.sBehavior.6239
- _conversationListPrefersEditButtonOnTrailingEdge.once.6236
- _conversationListPrefersEditButtonOnTrailingEdge.sBehavior.6235
- _defaultAVPlayerViewContorllerControlsInsets.once.6269
- _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6268.0
- _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6268.1
- _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6268.2
- _defaultAVPlayerViewContorllerControlsInsets.sBehavior.6268.3
- _defaultConversationViewingMessageCount.once.6222
- _defaultConversationViewingMessageCount.sBehavior.6221
- _detonatedItemBalloonViewSize.once.6357
- _detonatedItemBalloonViewSize.sBehavior.6356.0
- _detonatedItemBalloonViewSize.sBehavior.6356.1
- _detonatedItemDocumentIconSize.once.6361
- _detonatedItemDocumentIconSize.sBehavior.6360.0
- _detonatedItemDocumentIconSize.sBehavior.6360.1
- _documentIconSize.once.6273
- _documentIconSize.sBehavior.6272.0
- _documentIconSize.sBehavior.6272.1
- _entryFieldShouldUseBackdropView.once.6379
- _entryFieldShouldUseBackdropView.once.6405
- _entryViewAlwaysUsesConcentricPadding.once.6289
- _entryViewAlwaysUsesConcentricPadding.sBehavior.6288
- _entryViewConcentricPadding.once.6293
- _entryViewConcentricPadding.sBehavior.6292
- _entryViewHorizontalCoverInsets.once.6391
- _entryViewHorizontalCoverInsets.once.6416
- _entryViewHorizontalCoverInsets.sBehavior.6390.0
- _entryViewHorizontalCoverInsets.sBehavior.6390.1
- _entryViewHorizontalCoverInsets.sBehavior.6390.2
- _entryViewHorizontalCoverInsets.sBehavior.6390.3
- _entryViewHorizontalCoverInsets.sBehavior.6415.0
- _entryViewHorizontalCoverInsets.sBehavior.6415.1
- _entryViewHorizontalCoverInsets.sBehavior.6415.2
- _entryViewHorizontalCoverInsets.sBehavior.6415.3
- _entryViewMaxHandWritingPluginShelfHeight.once.6305
- _entryViewMaxHandWritingPluginShelfHeight.sBehavior.6304
- _entryViewVerticalCoverInsets.once.6387
- _entryViewVerticalCoverInsets.once.6413
- _entryViewVerticalCoverInsets.sBehavior.6386
- _entryViewVerticalCoverInsets.sBehavior.6412
- _get_witness_table 7SwiftUI16ScrollViewReaderVyAA0D0PAAE12onTapGesture5count7performQrSi_yyctFQOyAE011_QuickLook_aB0E05quickL7Preview_2inQrAA7BindingVy10Foundation3URLVSgG_qd__tSkRd__AP7ElementRtd__lFQOy20CommunicationDetails0ucD0VyAA6ZStackVyAA05TupleD0VyAA15ModifiedContentVyA1_yA1_y7ChatKit023KeyboardListenerWrapperD0VAA12_FrameLayoutVGAA14_OpacityEffectVGAA25_AppearanceActionModifierVG_A1_yA1_yAA9LazyVGridVyAA7ForEachVys18EnumeratedSequenceVySayA2_0u9WalletTabD0V10WalletPassVGGSSA1_yA1_yAeAEAfgHQrSi_yyctFQOyA21_04CellD0V_Qo_A2_0u6DoublegH8ModifierVGA2_0uD17CommonContextMenuVGGGAA14_PaddingLayoutVGA38_GtGGG_SayAPGQo__Qo_GAaDHPyHC.196
- _groupRecipientSelectionPresentationStyle.once.6335
- _groupRecipientSelectionPresentationStyle.sBehavior.6334
- _isAppStripInKeyboard.once.6297
- _joystickUsesWindow.once.6375
- _joystickUsesWindow.once.6401
- _keyboardSizeDeterminesAppCardDetentHeight.once.6198
- _lowClearanceInLandscape.once.6186
- _minTranscriptMarginInsets.once.6265
- _minTranscriptMarginInsets.sBehavior.6264.1
- _minTranscriptMarginInsets.sBehavior.6264.3
- _numberOfButtonsInPhotoPicker.once.6321
- _numberOfButtonsInPhotoPicker.sBehavior.6320
- _objc_msgSend$_invalidateBlackholeAlertView
- _objc_msgSend$_updateBlackholeAlertView
- _objc_msgSend$blackholeAlertView
- _objc_msgSend$setBlackholeAlertView:
- _objc_msgSend$setDouble:forKey:
- _objc_msgSend$submitAndOpenTapToRadarWithNotificationIdentifier:notificationTitle:notificationBody:draftTitle:problemDescription:attachments:deviceClasses:classification:reproducibility:
- _photoPickerMaxPopoverPhotoHeight.once.6327
- _photoPickerMaxPopoverPhotoHeight.sBehavior.6326
- _photoPickerPopoverWidth.once.6317
- _photoPickerPopoverWidth.sBehavior.6316
- _presentForwardingUIModally.once.6206
- _presentsAutocompleteInAPopover.once.6285
- _presentsQuickLookController.once.6202
- _presentsQuickLookController.sBehavior.6201
- _previewMaxWidth.once.6250
- _previewMaxWidth.sBehavior.6249
- _resetsIdleTimer.once.6434
- _resetsIdleTimer.once.6454
- _searchLinksThumbnailWidth.once.6347
- _searchLinksThumbnailWidth.sBehavior.6346
- _searchPhotosThumbnailWidth.once.6345
- _searchPhotosThumbnailWidth.sBehavior.6344
- _shouldAlignRecipientGlyphsWithMargins.once.6331
- _shouldAlignRecipientGlyphsWithMargins.sBehavior.6330
- _shouldRefreshAlternateAddressesSheet.once.6281
- _shouldRefreshAlternateAddressesSheet.sBehavior.6280
- _shouldShowDisclosureChevronInRecipientAtoms.once.6277
- _shouldSuppressRotationInNewCompose.once.6182
- _shouldUnreadIndicatorChangeOnSelection.once.6244
- _shouldUnreadIndicatorChangeOnSelection.sBehavior.6243
- _shouldUseSimpleTimestampsInTranscript.once.6430
- _shouldUseSimpleTimestampsInTranscript.once.6450
- _shouldUseSimpleTimestampsInTranscript.sBehavior.6429
- _shouldUseSimpleTimestampsInTranscript.sBehavior.6449
- _showMMSSetup.once.6218
- _showPendingInConversationList.once.6226
- _showPendingInConversationList.sBehavior.6225
- _showsConversationListCellChevronImage.once.6232
- _showsConversationListCellChevronImage.sBehavior.6231
- _suggestedAppStripLimit.once.6349
- _suggestedAppStripLimit.sBehavior.6348
- _supportedInterfaceOrientations.once.6214
- _supportedInterfaceOrientations.sBehavior.6213
- _supportsEntryViewPlusButtonLongPress.once.6301
- _supportsEntryViewPlusButtonLongPress.sBehavior.6300
- _symbolic _____y_____y_____y_____y_____y_____y_____yAEyAEy__________G_____G_____G_AEyAEy_____y_____y_____ySay_____GGSSAEyAEy_____y______Qo______G_____GGG_____GA_GtGGG_Say_____GQo__Qo_G 7SwiftUI16ScrollViewReaderV AA0D0PAAE12onTapGesture5count7performQrSi_yyctFQO AE011_QuickLook_aB0E05quickL7Preview_2inQrAA7BindingVy10Foundation3URLVSgG_qd__tSkRd__AP7ElementRtd__lFQO 20CommunicationDetails0ucD0V AA6ZStackV AA05TupleD0V AA15ModifiedContentV 7ChatKit023KeyboardListenerWrapperD0V AA12_FrameLayoutV AA14_OpacityEffectV AA25_AppearanceActionModifierV AA9LazyVGridV AA7ForEachV s18EnumeratedSequenceV A2_0u9WalletTabD0V10WalletPassV AeAEAfgHQrSi_yyctFQO A18_04CellD0V A2_0u6DoublegH8ModifierV A2_0uD17CommonContextMenuV AA14_PaddingLayoutV AP
- _theme.once.6173
- _theme.once.6370
- _theme.once.6397
- _theme.once.6421
- _theme.once.6442
- _theme.sBehavior.6172
- _theme.sBehavior.6369
- _theme.sBehavior.6396
- _theme.sBehavior.6420
- _theme.sBehavior.6441
- _transcriptContactImageDiameter.once.6254
- _transcriptContactImageDiameter.sBehavior.6253
- _transcriptGroupTypingContactImageDiameter.once.6258
- _transcriptGroupTypingContactImageDiameter.sBehavior.6257
- _transcriptHeaderViewMaxRows.once.6210
- _transcriptHeaderViewMaxRows.sBehavior.6209
- _usesActionMenu.once.6383
- _usesActionMenu.once.6409
- _usesPopovers.once.6190
- _usesPopovers.sBehavior.6189
- _usesUncollapsedSplitview.once.6178
- _usesUncollapsedSplitview.sBehavior.6177
CStrings:
+ "<%@ %p>{%@}"
+ "BEGIN holding keyboard event updates for reason: %{public}@"
+ "CKRecipientSelectionController Blackhole Status"
+ "Chat supports encryption: %d, Message encrypted: %d, Service: %@, Message GUID: %@"
+ "Current service %@, new participant(s) supported service %@. Chat has existing RCS group identity, targeting to new service before adding recipients..."
+ "DetailsWalletScrollView"
+ "END holding keyboard event updates updates for reason: %{public}@"
+ "Encryption"
+ "Hawking Warning Visibility: %{BOOL}d"
+ "Q12@?0B8"
+ "RCS encryption discrepancy detected: %@"
+ "RCSEncryptionDiscrepancy"
+ "Refreshing Hawking Warning Visibility"
+ "Refreshing Hawking Warning Visibility for Current Composition"
+ "Skipping keyboard event update - updates are currently held"
+ "T@\"NSCountedSet\",&,N,V_posterKeyboardUpdateHoldReasons"
+ "T@\"UIScrollView\",&,N,V_serviceLabelContainerView"
+ "TB,N,V_isForwardedAudioMessage"
+ "TranscriptOverlayViewControllerPresentation"
+ "Unable to get any name for contact: %s"
+ "Updating encryption support from %{BOOL}d to %{BOOL}d before adding recipients."
+ "_convertHandles:toAccount:"
+ "_currentBackgroundCanDockTranscript"
+ "_hawkingWarningString"
+ "_hawkingWarningVisibility"
+ "_hawkingWarningVisibilityFetchQueue"
+ "_hawkingWarningVisibilityFetchToken"
+ "_isForwardedAudioMessage"
+ "_makeServiceLabelSubviews"
+ "_needsRetargetBeforeAddingParticipantsForService:"
+ "_posterKeyboardUpdateHoldReasons"
+ "_serviceLabelContainerView"
+ "_serviceLabelStringForService wants Hawking label"
+ "_serviceLabelStringForService wants Satellite label"
+ "_shouldBeSendingKeyboardEventsToBackground"
+ "_targetToService:newComposition:supportsEncryption:"
+ "beginHoldingPosterKeyboardUpdatesForReason:"
+ "endHoldingPosterKeyboardUpdatesForReason:"
+ "fileTransfer:acceptedWithPath:autoRename:overwrite:options:source:"
+ "inlineReply"
+ "installServiceLabelInView:"
+ "isForwardedAudioMessage"
+ "isHoldingPosterKeyboardFrameUpdatesForPosterRenderingTranscriptBackground:"
+ "macAddToGroupDialogMaximumSize"
+ "macAddToGroupDialogMinimumSize"
+ "originalUnformattedID"
+ "posterKeyboardUpdateHoldReasons"
+ "refreshHawkingWarningVisibility"
+ "refreshServiceLabelScrollInsets"
+ "serviceLabelContainerView"
+ "setBreaksLinesForInteractiveText:"
+ "setFallbackStyle:"
+ "setIsForwardedAudioMessage:"
+ "setPosterKeyboardUpdateHoldReasons:"
+ "setServiceLabelContainerView:"
+ "showHawkingWarning"
+ "stringFromContact:"
+ "supportsHawkingWarning"
+ "v56@0:8@16@24B32B36q40q48"
- "@\"CKTranscriptMultilineLabelCell\""
- "CKComposeChatController Blackhole Status"
- "CKRecipientSelectionControllerEncryptionIssueLastSeenDate"
- "CKServiceChatItemEncryptionIssueLastSeenDate"
- "Downgrading encryption because some new particpant(s) do not support encryption."
- "Mac"
- "New Compose tried to display “iMessage” without an encryption status label underneath. An “Encrypted” label had to be manually added.\n\nService: %@\nEncryption Capability: %@"
- "Please file a radar. iMessage is always encrypted, but an iMessage conversation was staged without an encryption status."
- "Please file a radar. iMessage is always encrypted, but the encryption flag was missing on a correctly encrypted message."
- "T@\"CKTranscriptMultilineLabelCell\",&,N,V_blackholeAlertView"
- "Transcript tried to display CKServiceChatItem with “iMessage” but no encryption status label underneath. An “Encrypted” label had to be manually added.\n\nGUID: %@\nService Name: %@\nItem Service Name: %@\nDowngraded: %d\n\n%@"
- "Watch"
- "[Internal] New iMessage conversation did not display its encryption status"
- "[Internal] iMessage conversation did not display its encryption status"
- "[RCS Encryption] iMessage incorrectly detected as unencrypted"
- "_blackholeAlertStatus"
- "_blackholeAlertStatusQueue"
- "_blackholeAlertView"
- "_invalidateBlackholeAlertView"
- "_updateBlackholeAlertView"
- "blackholeAlertView"
- "com.apple.MobileSMS.iMessageEncryption"
- "fileTransfer:acceptedWithPath:autoRename:overwrite:options:"
- "iPhone"
- "setBlackholeAlertView:"
- "setDouble:forKey:"
- "submitAndOpenTapToRadarWithNotificationIdentifier:notificationTitle:notificationBody:draftTitle:problemDescription:attachments:deviceClasses:classification:reproducibility:"
- "v48@0:8@16@24B32B36q40"

```
