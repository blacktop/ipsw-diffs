## ChatKit

> `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1450.200.75.0.0
-  __TEXT.__text: 0xb23a1c
+1450.200.88.2.1
+  __TEXT.__text: 0xb23cc4
   __TEXT.__auth_stubs: 0xbe50
   __TEXT.__delay_helper: 0x99c
-  __TEXT.__objc_methlist: 0x7170c
+  __TEXT.__objc_methlist: 0x7177c
   __TEXT.__const: 0x32c84
-  __TEXT.__gcc_except_tab: 0x28abc
-  __TEXT.__cstring: 0x514c7
-  __TEXT.__oslogstring: 0x4b6b3
+  __TEXT.__gcc_except_tab: 0x28afc
+  __TEXT.__cstring: 0x513c7
+  __TEXT.__oslogstring: 0x4b743
   __TEXT.__dlopen_cstrs: 0xb0e
   __TEXT.__ustring: 0x18e
-  __TEXT.__constg_swiftt: 0x1af58
-  __TEXT.__swift5_typeref: 0x3fe2c
+  __TEXT.__constg_swiftt: 0x1af80
+  __TEXT.__swift5_typeref: 0x3fe0c
   __TEXT.__swift5_builtin: 0x7a8
-  __TEXT.__swift5_reflstr: 0x10251
-  __TEXT.__swift5_fieldmd: 0xe7e4
+  __TEXT.__swift5_reflstr: 0x10261
+  __TEXT.__swift5_fieldmd: 0xe7f0
   __TEXT.__swift5_assocty: 0x4058
   __TEXT.__swift5_capture: 0x7308
   __TEXT.__swift5_proto: 0x175c

   __TEXT.__swift_as_ret: 0x3d0
   __TEXT.__swift5_protos: 0xbc
   __TEXT.__swift5_mpenum: 0xd0
-  __TEXT.__unwind_info: 0x2deb8
+  __TEXT.__unwind_info: 0x2def8
   __TEXT.__eh_frame: 0xd4ac
-  __TEXT.__objc_classname: 0xb859
-  __TEXT.__objc_methname: 0x10d88f
-  __TEXT.__objc_methtype: 0x229e5
-  __TEXT.__objc_stubs: 0xa68c0
-  __DATA_CONST.__got: 0x7230
-  __DATA_CONST.__const: 0xeeb8
+  __TEXT.__objc_classname: 0xb86b
+  __TEXT.__objc_methname: 0x10da3e
+  __TEXT.__objc_methtype: 0x22a0b
+  __TEXT.__objc_stubs: 0xa6a80
+  __DATA_CONST.__got: 0x7240
+  __DATA_CONST.__const: 0xef10
   __DATA_CONST.__objc_classlist: 0x2ef0
   __DATA_CONST.__objc_catlist: 0x558
   __DATA_CONST.__objc_protolist: 0x1340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x362e0
+  __DATA_CONST.__objc_selrefs: 0x36340
   __DATA_CONST.__objc_protorefs: 0x4f8
   __DATA_CONST.__objc_superrefs: 0x1a68
   __DATA_CONST.__objc_arraydata: 0xfd8
   __AUTH_CONST.__auth_got: 0x5f38
-  __AUTH_CONST.__const: 0x38360
-  __AUTH_CONST.__cfstring: 0x246c0
-  __AUTH_CONST.__objc_const: 0x9b3a0
+  __AUTH_CONST.__const: 0x38380
+  __AUTH_CONST.__cfstring: 0x24700
+  __AUTH_CONST.__objc_const: 0x9b428
   __AUTH_CONST.__objc_arrayobj: 0xe70
   __AUTH_CONST.__objc_intobj: 0x1128
   __AUTH_CONST.__objc_doubleobj: 0x870
   __AUTH_CONST.__objc_floatobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH.__objc_data: 0x28a48
+  __AUTH.__objc_data: 0x28a78
   __AUTH.__data: 0x12d60
-  __DATA.__objc_ivar: 0x4b40
-  __DATA.__data: 0x1f8e0
+  __DATA.__objc_ivar: 0x4b30
+  __DATA.__data: 0x1f900
   __DATA.__objc_stublist: 0x40
-  __DATA.__bss: 0x39110
+  __DATA.__bss: 0x39150
   __DATA.__common: 0x1328
   __DATA_DIRTY.__objc_data: 0x8760
   __DATA_DIRTY.__data: 0x7d0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BA49FC53-4034-3E20-9B14-B7E45BD30A51
-  Functions: 69973
-  Symbols:   146289
-  CStrings:  60641
+  UUID: 17051162-95C9-3563-BDB2-8EA21F26F124
+  Functions: 69994
+  Symbols:   146332
+  CStrings:  60656
 
Symbols:
+ +[CKConversation(Content_Utilities) _iMessage_canSendComposition:reachabilityContext:forceSMS:error:]
+ +[CKCoreChatController syncedSettingsManager]
+ +[CKCoreChatController(Backgrounds) shouldSuppressTranscriptBackgroundUIForConversation:]
+ +[CKCoreChatController(Backgrounds) supportsTranscriptBackground]
+ +[CKInlineReplyChatController supportsTranscriptBackground]
+ +[CKMediaObject(Display) _generateIconWithSize:scale:type:fileURL:]
+ +[CKMediaObject(Display) generateAndCacheIconForMediaObjectWithUTIType:fileURL:completion:]
+ +[CKMentionsUtilities isPredictionBarAvailableForMentions]
+ +[CKPreviewDispatchCache defaultPreviewPriority]
+ +[CKPreviewDispatchCache(CKMediaObject_Icon) iconPreviewCache]
+ +[CKPreviewDispatchCache(CKMediaObject_Icon) iconPreviewCache].cold.1
+ -[CKChatController _handleIsFilteredChange]
+ -[CKChatSceneDelegate sendMenuPresentationShouldUseKeyboardSnapshot:]
+ -[CKConversation eligibleToSendWithMadrid]
+ -[CKConversation serviceReachabilityContext]
+ -[CKConversation shouldDisplayGroupIdentity]
+ -[CKConversation shouldSuppressTranscriptBackgroundUI]
+ -[CKMediaObject(Display) cachedIcon]
+ -[CKMessagesController messagesSceneDelegateDidUpdateEffectiveGeometryForScene:previousEffectiveGeometry:]
+ -[CKMessagesController sendMenuPresentationShouldUseKeyboardSnapshot:]
+ -[CKMessagesSceneDelegate windowScene:didUpdateEffectiveGeometry:]
+ -[CKMessagesSplitViewCoordinator effectiveGeometryDidUpdateForScene:previousEffectiveGeometry:]
+ -[CKPreviewDispatchCache objectForKeyedSubscript:]
+ -[CKPreviewDispatchCache setObject:forKeyedSubscript:]
+ -[CKTranscriptPreviewController shouldSuppressTranscriptBackgroundUI]
+ -[NSUserDefaults(SendAnimation) ck_isUsingSpecialGlassDuringSendAnimationEnabled]
+ GCC_except_table1001
+ GCC_except_table1005
+ GCC_except_table1028
+ GCC_except_table1031
+ GCC_except_table1038
+ GCC_except_table1045
+ GCC_except_table1075
+ GCC_except_table1077
+ GCC_except_table1100
+ GCC_except_table1105
+ GCC_except_table1107
+ GCC_except_table1152
+ GCC_except_table1154
+ GCC_except_table1156
+ GCC_except_table1158
+ GCC_except_table1162
+ GCC_except_table1166
+ GCC_except_table1169
+ GCC_except_table1171
+ GCC_except_table1173
+ GCC_except_table1181
+ GCC_except_table1198
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table130
+ GCC_except_table1556
+ GCC_except_table158
+ GCC_except_table1583
+ GCC_except_table1590
+ GCC_except_table1595
+ GCC_except_table1609
+ GCC_except_table162
+ GCC_except_table175
+ GCC_except_table209
+ GCC_except_table235
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table249
+ GCC_except_table253
+ GCC_except_table256
+ GCC_except_table260
+ GCC_except_table264
+ GCC_except_table289
+ GCC_except_table302
+ GCC_except_table321
+ GCC_except_table353
+ GCC_except_table362
+ GCC_except_table366
+ GCC_except_table371
+ GCC_except_table373
+ GCC_except_table401
+ GCC_except_table404
+ GCC_except_table420
+ GCC_except_table428
+ GCC_except_table432
+ GCC_except_table434
+ GCC_except_table440
+ GCC_except_table452
+ GCC_except_table454
+ GCC_except_table474
+ GCC_except_table497
+ GCC_except_table503
+ GCC_except_table523
+ GCC_except_table532
+ GCC_except_table538
+ GCC_except_table549
+ GCC_except_table553
+ GCC_except_table577
+ GCC_except_table580
+ GCC_except_table583
+ GCC_except_table594
+ GCC_except_table597
+ GCC_except_table603
+ GCC_except_table616
+ GCC_except_table630
+ GCC_except_table641
+ GCC_except_table644
+ GCC_except_table646
+ GCC_except_table650
+ GCC_except_table655
+ GCC_except_table659
+ GCC_except_table663
+ GCC_except_table669
+ GCC_except_table681
+ GCC_except_table683
+ GCC_except_table689
+ GCC_except_table707
+ GCC_except_table718
+ GCC_except_table720
+ GCC_except_table723
+ GCC_except_table735
+ GCC_except_table746
+ GCC_except_table753
+ GCC_except_table783
+ GCC_except_table786
+ GCC_except_table790
+ GCC_except_table812
+ GCC_except_table821
+ GCC_except_table828
+ GCC_except_table837
+ GCC_except_table848
+ GCC_except_table851
+ GCC_except_table853
+ GCC_except_table876
+ GCC_except_table879
+ GCC_except_table896
+ GCC_except_table900
+ GCC_except_table904
+ GCC_except_table913
+ GCC_except_table917
+ GCC_except_table925
+ GCC_except_table927
+ GCC_except_table931
+ GCC_except_table934
+ GCC_except_table939
+ GCC_except_table941
+ GCC_except_table945
+ GCC_except_table951
+ GCC_except_table953
+ GCC_except_table956
+ GCC_except_table957
+ GCC_except_table959
+ GCC_except_table961
+ GCC_except_table967
+ GCC_except_table969
+ GCC_except_table972
+ GCC_except_table978
+ GCC_except_table985
+ GCC_except_table990
+ GCC_except_table996
+ _CKConversationGroupPhoto
+ _CKConversationGroupPhoto.cold.1
+ _CKConversationGroupPhoto.onceToken
+ _CKConversationGroupPhoto.osLog
+ _CKDefaultsKeySendAnimationSpecialGlassDuringSendEnabled
+ _OBJC_CLASS_$_NSProgress
+ _OBJC_CLASS_$_UIKeyboardSceneDelegate
+ __CLASS_PROPERTIES__TtC7ChatKit23ClarityUIChatController
+ __OBJC_$_CLASS_METHODS_CKAttachmentBalloonView(CKMediaObject|CKComposition|CKMessagePartChatItem|LinkPresentationHelper)
+ __OBJC_$_CLASS_METHODS_CKPreviewDispatchCache(CKMediaObject_Icon|CKMediaObject_Display|MKMapSnapshotter)
+ __OBJC_$_INSTANCE_METHODS_CKAttachmentBalloonView(CKMediaObject|CKComposition|CKMessagePartChatItem|LinkPresentationHelper)
+ __OBJC_$_INSTANCE_METHODS_CKPreviewDispatchCache(CKMediaObject_Icon|CKMediaObject_Display|MKMapSnapshotter)
+ ___103+[CKComposition(UIPasteboard) _pasteAttributedStringWithItemProvider:builderContext:completionHandler:]_block_invoke.527
+ ___103+[CKComposition(UIPasteboard) _pasteAttributedStringWithItemProvider:builderContext:completionHandler:]_block_invoke.528
+ ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke.623
+ ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke.624
+ ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke.635
+ ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke.636
+ ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke_2.625
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.639
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.640
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.645
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.650
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.656
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.665
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.666
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.667
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.644
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.649
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.651
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.657
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.668
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_3.654
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_3.658
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_4.655
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_4.659
+ ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_5.661
+ ___115-[CKChatController _presentCollabAddToMessagesGroupAlertIfNecessary:collaborationType:sendBlock:completionHandler:]_block_invoke.1343
+ ___124+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromItemProvider:builderContext:shareOptions:completionHandler:]_block_invoke.530
+ ___124+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromItemProvider:builderContext:shareOptions:completionHandler:]_block_invoke.531
+ ___130+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCloudKitItemProvider:collaborationShareOptions:completionHandler:]_block_invoke.614
+ ___130+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCloudKitItemProvider:collaborationShareOptions:completionHandler:]_block_invoke.616
+ ___135+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCollaborativeItemProvider:collaborationShareOptions:completionHandler:]_block_invoke.618
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.535
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.535.cold.1
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.535.cold.2
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.535.cold.3
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.535.cold.4
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.537
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.542
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.542.cold.1
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.543
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.564
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.566
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.581
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.586
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.591
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.595
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.596
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.536
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.538
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.544
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.565
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.569
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.587
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.597
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_3.574
+ ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_3.589
+ ___145-[CKChatController _sendAutomaticallyPlacedSticker:stickerReactionSession:forChatItem:forParentChatItem:stickerFrame:animationCompletionHandler:]_block_invoke.1215
+ ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1784
+ ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1784.cold.1
+ ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1785
+ ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1789
+ ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1789.cold.1
+ ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke_2.1787
+ ___34-[CKMediaObject(Display) richIcon]_block_invoke.245
+ ___34-[CKMediaObject(Display) richIcon]_block_invoke.249
+ ___39-[CKChatController addToCollaboration:]_block_invoke.1576
+ ___39-[CKChatController addToCollaboration:]_block_invoke_2.1578
+ ___41-[CKMediaObject(Display) previewMetadata]_block_invoke.326
+ ___41-[CKMediaObject(Display) previewMetadata]_block_invoke_2.327
+ ___45-[CKChatController _handleChatItemDidChange:]_block_invoke.1554
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.732
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.735
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.733
+ ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.736
+ ___47-[CKChatController sendComposition:animations:]_block_invoke.825
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1483
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1487
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_2.1489
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_3.1493
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_4.1497
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_5.1498
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_6.1502
+ ___58-[CKChatController chatInputControllerDidSelectFunCamera:]_block_invoke.1211
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1365
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1368
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1366
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1370
+ ___61+[CKAttachmentBalloonView _linkViewThumbnailFromMediaObject:]_block_invoke
+ ___61+[CKAttachmentBalloonView _linkViewThumbnailFromMediaObject:]_block_invoke_2
+ ___61-[CKMediaObject(Display) prewarmPreviewForWidth:orientation:]_block_invoke.283
+ ___62+[CKPreviewDispatchCache(CKMediaObject_Icon) iconPreviewCache]_block_invoke
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1254.cold.1
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1256
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1257
+ ___65-[CKMediaObject(Display) generateOOPPreviewForWidth:orientation:]_block_invoke.288
+ ___65-[CKMediaObject(Display) generateOOPPreviewForWidth:orientation:]_block_invoke_2.289
+ ___67-[CKChatController _sendCompositionForNewCloudKitShare:completion:]_block_invoke.1316
+ ___69-[CKChatController nicknameBannerView:actionButtonTapped:forUpdates:]_block_invoke.1570
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1327
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1332
+ ___72-[CKChatController textPasteConfigurationSupporting:transformPasteItem:]_block_invoke.1617
+ ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1284
+ ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1285
+ ___75-[CKCoreChatController(Backgrounds) updateTranscriptBackground:transferID:]_block_invoke.263
+ ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1293
+ ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1294
+ ___77-[CKChatController selectedBalloonIntersectingRect:chatItemForRepositioning:]_block_invoke.1203
+ ___81+[CKComposition(UIPasteboard) requestFilenameForType:forItemProvider:completion:]_block_invoke.638
+ ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1333
+ ___81-[NSUserDefaults(SendAnimation) ck_isUsingSpecialGlassDuringSendAnimationEnabled]_block_invoke
+ ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1358
+ ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1359
+ ___87-[CKChatController _removeSubsharesAndSendFileProviderComposition:shareURL:completion:]_block_invoke.1307
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1301
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1301.cold.1
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1304
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1305
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke_2.1306
+ ___89-[CKCoreChatController(Backgrounds) _transitionToPosterKitPosterConfiguration:onChannel:]_block_invoke.256
+ ___89-[CKCoreChatController(Backgrounds) _transitionToPosterKitPosterConfiguration:onChannel:]_block_invoke.256.cold.1
+ ___91+[CKMediaObject(Display) generateAndCacheIconForMediaObjectWithUTIType:fileURL:completion:]_block_invoke
+ ___91+[CKMediaObject(Display) generateAndCacheIconForMediaObjectWithUTIType:fileURL:completion:]_block_invoke_2
+ ___91+[CKMediaObject(Display) generateAndCacheIconForMediaObjectWithUTIType:fileURL:completion:]_block_invoke_3
+ ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1273
+ ___94-[CKPreviewDispatchCache(CKMediaObject_Display) enqueueSaveBlock:forMediaObject:withPriority:]_block_invoke.201
+ ___95-[CKChatController _updateAndSendCompositionForExistingCloudKitShare:share:attempt:completion:]_block_invoke.1324
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.711
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.723
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.730
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.738
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.752
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.761
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_2.712
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_2.731
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_2.739
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_2.753
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_3.732
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_3.740
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_3.740.cold.1
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_3.754
+ ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_4.734
+ ___CKConversationGroupPhoto_block_invoke
+ ___block_descriptor_48_e8_32s40s_e62_"NSProgress"16?0?<v?"<NSItemProviderWriting>""NSError">8ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s_e27_"UIImage"16?0"NSString"8ls32l8s40l8
+ ___block_literal_global.1149
+ ___block_literal_global.1238
+ ___block_literal_global.1244
+ ___block_literal_global.1247
+ ___block_literal_global.1275
+ ___block_literal_global.1301
+ ___block_literal_global.1309
+ ___block_literal_global.1393
+ ___block_literal_global.1427
+ ___block_literal_global.1437
+ ___block_literal_global.1449
+ ___block_literal_global.1459
+ ___block_literal_global.1464
+ ___block_literal_global.1474
+ ___block_literal_global.1484
+ ___block_literal_global.1492
+ ___block_literal_global.1502
+ ___block_literal_global.1510
+ ___block_literal_global.1520
+ ___block_literal_global.1537
+ ___block_literal_global.1547
+ ___block_literal_global.1568
+ ___block_literal_global.1602
+ ___block_literal_global.1651
+ ___block_literal_global.1681
+ ___block_literal_global.1686
+ ___block_literal_global.1694
+ ___block_literal_global.1712
+ ___block_literal_global.1716
+ ___block_literal_global.1732
+ ___block_literal_global.1787
+ ___block_literal_global.1849
+ ___block_literal_global.1882
+ ___block_literal_global.1922
+ ___block_literal_global.1930
+ ___block_literal_global.1944
+ ___block_literal_global.1985
+ ___block_literal_global.205
+ ___block_literal_global.2103
+ ___block_literal_global.2108
+ ___block_literal_global.2119
+ ___block_literal_global.2142
+ ___block_literal_global.4
+ ___block_literal_global.4000
+ ___block_literal_global.4008
+ ___block_literal_global.4010
+ ___block_literal_global.778
+ ___block_literal_global.804
+ ___block_literal_global.985
+ _ck_isSlowSendAnimationEnabled.result
+ _ck_isUsingSpecialGlassDuringSendAnimationEnabled.onceToken
+ _ck_isUsingSpecialGlassDuringSendAnimationEnabled.result
+ _ck_isVerySlowSendAnimationEnabled.result
+ _ck_isVeryVerySlowSendAnimationEnabled.result
+ _get_witness_table 7SwiftUI10_ShapeViewVyAA9RectangleVAA03AnyC5StyleVGAA0D0HPyHC.82
+ _iconPreviewCache.cache
+ _iconPreviewCache.onceToken
+ _objc_msgSend$_dismissEditMenu
+ _objc_msgSend$_generateIconWithSize:scale:type:fileURL:
+ _objc_msgSend$_iMessage_canSendComposition:reachabilityContext:forceSMS:error:
+ _objc_msgSend$activeKeyboardSceneDelegate
+ _objc_msgSend$cachedIcon
+ _objc_msgSend$canLazilyLoadImagesUsingLinkPresentation
+ _objc_msgSend$ck_isUsingSpecialGlassDuringSendAnimationEnabled
+ _objc_msgSend$defaultPreviewPriority
+ _objc_msgSend$effectiveGeometryDidUpdateForScene:previousEffectiveGeometry:
+ _objc_msgSend$eligibleToSendWithMadrid
+ _objc_msgSend$fetchCollaborationNoticesForChatGUIDs:completionHandler:
+ _objc_msgSend$generateAndCacheIconForMediaObjectWithUTIType:fileURL:completion:
+ _objc_msgSend$iMessageEnabledForReachabilityContext:
+ _objc_msgSend$iconPreviewCache
+ _objc_msgSend$initWithItemProvider:properties:placeholderImage:
+ _objc_msgSend$isKnownSenderWithUnknownFilteringEnabled:
+ _objc_msgSend$isPredictionBarAvailableForMentions
+ _objc_msgSend$messagesSceneDelegateDidUpdateEffectiveGeometryForScene:previousEffectiveGeometry:
+ _objc_msgSend$progressWithTotalUnitCount:
+ _objc_msgSend$sendMenuPresentationShouldUseKeyboardSnapshot:
+ _objc_msgSend$serviceReachabilityContext
+ _objc_msgSend$setCancellable:
+ _objc_msgSend$setPausable:
+ _objc_msgSend$shouldDisplayGroupIdentity
+ _objc_msgSend$shouldSuppressTranscriptBackgroundUI
+ _objc_msgSend$shouldSuppressTranscriptBackgroundUIForConversation:
+ _objc_msgSend$windowingModeEnabled
- +[CKConversation(Content_Utilities) _iMessage_canSendComposition:lastAddressedHandle:lastAddressedSIMID:currentService:forceSMS:error:]
- +[CKMediaObject(Display) iconCache].cold.1
- +[CKPreviewDispatchCache _defaultPreviewPriority]
- +[UIKeyboard(CKUtilities) __ck_isPredictionBarEnabled]
- -[CKChatController detailsToolbarItem]
- -[CKChatController setDetailsToolbarItem:]
- -[CKChatController(MacToolbar) _configureDetailsToolbarItem]
- -[CKChatController(MacToolbar) _updatedDetailsToolbarItemImage]
- -[CKConversation cachedIsKnownSender]
- -[CKConversation setCachedIsKnownSender:]
- -[CKConversation supportsTranscriptBackgrounds]
- -[CKCoreChatController setSyncedSettingsManager:]
- -[CKCoreChatController syncedSettingsManager]
- -[CKCoreChatController(Backgrounds) supportsTranscriptBackground]
- -[CKInlineReplyChatController supportsTranscriptBackground]
- -[CKMacToolbarController alignmentRectForItemWithIdentifier:]
- -[CKMessageEntryView is3rdPartyKeyboardVisible]
- -[CKMessageEntryView isPredictionBarEnabled]
- -[CKMessageEntryView showsKeyboardPredictionBar]
- -[CKMessagesSplitViewCoordinator proposedColumnWidth]
- -[CKMessagesSplitViewCoordinator setProposedColumnWidth:]
- GCC_except_table1000
- GCC_except_table1004
- GCC_except_table1027
- GCC_except_table1030
- GCC_except_table1037
- GCC_except_table1044
- GCC_except_table1074
- GCC_except_table1076
- GCC_except_table1099
- GCC_except_table1104
- GCC_except_table1106
- GCC_except_table1151
- GCC_except_table1153
- GCC_except_table1155
- GCC_except_table1157
- GCC_except_table1160
- GCC_except_table1165
- GCC_except_table1167
- GCC_except_table1170
- GCC_except_table1172
- GCC_except_table1180
- GCC_except_table1197
- GCC_except_table131
- GCC_except_table1557
- GCC_except_table1584
- GCC_except_table1592
- GCC_except_table1597
- GCC_except_table1610
- GCC_except_table216
- GCC_except_table229
- GCC_except_table232
- GCC_except_table237
- GCC_except_table250
- GCC_except_table271
- GCC_except_table275
- GCC_except_table281
- GCC_except_table284
- GCC_except_table288
- GCC_except_table300
- GCC_except_table314
- GCC_except_table319
- GCC_except_table323
- GCC_except_table346
- GCC_except_table355
- GCC_except_table361
- GCC_except_table367
- GCC_except_table370
- GCC_except_table372
- GCC_except_table375
- GCC_except_table379
- GCC_except_table393
- GCC_except_table399
- GCC_except_table402
- GCC_except_table410
- GCC_except_table414
- GCC_except_table421
- GCC_except_table433
- GCC_except_table446
- GCC_except_table453
- GCC_except_table485
- GCC_except_table496
- GCC_except_table513
- GCC_except_table522
- GCC_except_table534
- GCC_except_table539
- GCC_except_table548
- GCC_except_table556
- GCC_except_table559
- GCC_except_table575
- GCC_except_table579
- GCC_except_table596
- GCC_except_table612
- GCC_except_table629
- GCC_except_table632
- GCC_except_table639
- GCC_except_table643
- GCC_except_table645
- GCC_except_table649
- GCC_except_table658
- GCC_except_table662
- GCC_except_table668
- GCC_except_table673
- GCC_except_table682
- GCC_except_table687
- GCC_except_table699
- GCC_except_table706
- GCC_except_table722
- GCC_except_table734
- GCC_except_table740
- GCC_except_table747
- GCC_except_table752
- GCC_except_table782
- GCC_except_table784
- GCC_except_table789
- GCC_except_table810
- GCC_except_table820
- GCC_except_table826
- GCC_except_table836
- GCC_except_table847
- GCC_except_table850
- GCC_except_table852
- GCC_except_table875
- GCC_except_table878
- GCC_except_table895
- GCC_except_table898
- GCC_except_table903
- GCC_except_table911
- GCC_except_table915
- GCC_except_table924
- GCC_except_table926
- GCC_except_table930
- GCC_except_table933
- GCC_except_table938
- GCC_except_table940
- GCC_except_table948
- GCC_except_table952
- GCC_except_table955
- GCC_except_table958
- GCC_except_table960
- GCC_except_table965
- GCC_except_table968
- GCC_except_table971
- GCC_except_table977
- GCC_except_table983
- GCC_except_table987
- GCC_except_table994
- _OBJC_IVAR_$_CKChatController._detailsToolbarItem
- _OBJC_IVAR_$_CKConversation._cachedIsKnownSender
- _OBJC_IVAR_$_CKCoreChatController._syncedSettingsManager
- _OBJC_IVAR_$_CKMessagesSplitViewCoordinator._proposedColumnWidth
- __OBJC_$_CLASS_METHODS_CKAttachmentBalloonView
- __OBJC_$_CLASS_METHODS_CKPreviewDispatchCache(CKMediaObject_Display|MKMapSnapshotter)
- __OBJC_$_CLASS_PROP_LIST_CKMediaObject
- __OBJC_$_INSTANCE_METHODS_CKAttachmentBalloonView(CKMediaObject|CKComposition|CKMessagePartChatItem)
- __OBJC_$_INSTANCE_METHODS_CKPreviewDispatchCache(CKMediaObject_Display|MKMapSnapshotter)
- ___103+[CKComposition(UIPasteboard) _pasteAttributedStringWithItemProvider:builderContext:completionHandler:]_block_invoke.524
- ___103+[CKComposition(UIPasteboard) _pasteAttributedStringWithItemProvider:builderContext:completionHandler:]_block_invoke.525
- ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke.617
- ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke.618
- ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke.632
- ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke.633
- ___109+[CKComposition(UIPasteboard) compositionFromNonCollaborationItemProviders:builderContext:completionHandler:]_block_invoke_2.622
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.636
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.637
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.642
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.647
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.653
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.661
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.662
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke.663
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.641
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.646
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.648
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.654
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_2.665
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_3.651
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_3.655
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_4.652
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_4.656
- ___112+[CKComposition(UIPasteboard) _requestCompositionFromItemProviderForNonCollaboration:builderContext:completion:]_block_invoke_5.658
- ___115-[CKChatController _presentCollabAddToMessagesGroupAlertIfNecessary:collaborationType:sendBlock:completionHandler:]_block_invoke.1341
- ___124+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromItemProvider:builderContext:shareOptions:completionHandler:]_block_invoke.527
- ___124+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromItemProvider:builderContext:shareOptions:completionHandler:]_block_invoke.528
- ___130+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCloudKitItemProvider:collaborationShareOptions:completionHandler:]_block_invoke.610
- ___130+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCloudKitItemProvider:collaborationShareOptions:completionHandler:]_block_invoke.611
- ___135+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCollaborativeItemProvider:collaborationShareOptions:completionHandler:]_block_invoke.615
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.529
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.532.cold.1
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.532.cold.2
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.532.cold.3
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.532.cold.4
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.534
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.539
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.539.cold.1
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.540
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.561
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.563
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.578
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.583
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.588
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.592
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke.593
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.533
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.535
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.541
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.562
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.566
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.584
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_2.591
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_3.571
- ___142+[CKComposition(UIPasteboard) _createPluginPayloadCompositionFromFileItemProvider:builderContext:collaborationShareOptions:completionHandler:]_block_invoke_3.586
- ___145-[CKChatController _sendAutomaticallyPlacedSticker:stickerReactionSession:forChatItem:forParentChatItem:stickerFrame:animationCompletionHandler:]_block_invoke.1213
- ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1786
- ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1786.cold.1
- ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1787
- ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1791
- ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke.1791.cold.1
- ___166+[CKUtilities quickSaveConfirmationAlertForMediaObjects:momentShareURL:popoverSource:metricsSource:cancelHandler:preSaveHandler:postSaveHandler:postAnyActionHandler:]_block_invoke_2.1789
- ___34-[CKMediaObject(Display) richIcon]_block_invoke.242
- ___34-[CKMediaObject(Display) richIcon]_block_invoke.246
- ___35+[CKMediaObject(Display) iconCache]_block_invoke
- ___39-[CKChatController addToCollaboration:]_block_invoke.1574
- ___39-[CKChatController addToCollaboration:]_block_invoke_2.1576
- ___41-[CKMediaObject(Display) previewMetadata]_block_invoke.325
- ___41-[CKMediaObject(Display) previewMetadata]_block_invoke_2.326
- ___45-[CKChatController _handleChatItemDidChange:]_block_invoke.1552
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.730
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke.733
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.731
- ___46-[CKChatController viewDidAppearDeferredSetup]_block_invoke_2.734
- ___47-[CKChatController sendComposition:animations:]_block_invoke.823
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1481
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1485
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_2.1487
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_3.1491
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_4.1495
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_5.1496
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_6.1500
- ___58-[CKChatController chatInputControllerDidSelectFunCamera:]_block_invoke.1209
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1363
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.1366
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1364
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke_2.1368
- ___61-[CKMediaObject(Display) prewarmPreviewForWidth:orientation:]_block_invoke.282
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1250
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1251
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.1252.cold.1
- ___65-[CKMediaObject(Display) generateOOPPreviewForWidth:orientation:]_block_invoke.287
- ___65-[CKMediaObject(Display) generateOOPPreviewForWidth:orientation:]_block_invoke_2.288
- ___67-[CKChatController _sendCompositionForNewCloudKitShare:completion:]_block_invoke.1314
- ___69-[CKChatController nicknameBannerView:actionButtonTapped:forUpdates:]_block_invoke.1568
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1324
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.1325
- ___72-[CKChatController textPasteConfigurationSupporting:transformPasteItem:]_block_invoke.1615
- ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1282
- ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.1283
- ___75-[CKCoreChatController(Backgrounds) updateTranscriptBackground:transferID:]_block_invoke.264
- ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1291
- ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.1292
- ___77-[CKChatController selectedBalloonIntersectingRect:chatItemForRepositioning:]_block_invoke.1201
- ___81+[CKComposition(UIPasteboard) requestFilenameForType:forItemProvider:completion:]_block_invoke.635
- ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.1331
- ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1356
- ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.1357
- ___87-[CKChatController _removeSubsharesAndSendFileProviderComposition:shareURL:completion:]_block_invoke.1305
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1299
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1299.cold.1
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1300
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.1303
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke_2.1304
- ___89-[CKCoreChatController(Backgrounds) _transitionToPosterKitPosterConfiguration:onChannel:]_block_invoke.257
- ___89-[CKCoreChatController(Backgrounds) _transitionToPosterKitPosterConfiguration:onChannel:]_block_invoke.257.cold.1
- ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.1269
- ___94-[CKPreviewDispatchCache(CKMediaObject_Display) enqueueSaveBlock:forMediaObject:withPriority:]_block_invoke.191
- ___95-[CKChatController _updateAndSendCompositionForExistingCloudKitShare:share:attempt:completion:]_block_invoke.1322
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.708
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.720
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.727
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.735
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.749
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke.758
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_2.709
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_2.728
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_2.736
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_2.750
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_3.729
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_3.737
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_3.737.cold.1
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_3.751
- ___96+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:builderContext:completion:]_block_invoke_4.731
- ___block_literal_global.1147
- ___block_literal_global.1236
- ___block_literal_global.1242
- ___block_literal_global.1245
- ___block_literal_global.1273
- ___block_literal_global.1305
- ___block_literal_global.1339
- ___block_literal_global.1359
- ___block_literal_global.1403
- ___block_literal_global.1429
- ___block_literal_global.1451
- ___block_literal_global.1461
- ___block_literal_global.1466
- ___block_literal_global.1486
- ___block_literal_global.1494
- ___block_literal_global.1504
- ___block_literal_global.1512
- ___block_literal_global.1522
- ___block_literal_global.1530
- ___block_literal_global.1539
- ___block_literal_global.1544
- ___block_literal_global.1549
- ___block_literal_global.1564
- ___block_literal_global.1600
- ___block_literal_global.1653
- ___block_literal_global.1677
- ___block_literal_global.1684
- ___block_literal_global.1692
- ___block_literal_global.1700
- ___block_literal_global.1714
- ___block_literal_global.1730
- ___block_literal_global.1884
- ___block_literal_global.1926
- ___block_literal_global.1938
- ___block_literal_global.1946
- ___block_literal_global.1987
- ___block_literal_global.2105
- ___block_literal_global.2110
- ___block_literal_global.2144
- ___block_literal_global.4003
- ___block_literal_global.4011
- ___block_literal_global.4013
- ___block_literal_global.527
- ___block_literal_global.573
- ___block_literal_global.776
- ___block_literal_global.802
- _get_witness_table 7SwiftUI10_ShapeViewVyAA9RectangleVAA03AnyC5StyleVGAA0D0HPyHC.79
- _iconCache.once
- _iconCache.sIconCache
- _objc_msgSend$__ck_isPredictionBarEnabled
- _objc_msgSend$_configureDetailsToolbarItem
- _objc_msgSend$_defaultPreviewPriority
- _objc_msgSend$_iMessage_canSendComposition:lastAddressedHandle:lastAddressedSIMID:currentService:forceSMS:error:
- _objc_msgSend$detailsToolbarItem
- _objc_msgSend$fetchCollaborationNoticesForChatGUID:completionHandler:
- _objc_msgSend$iMessageEnabledForSenderLastAddressedHandle:simID:previousService:
- _objc_msgSend$is3rdPartyKeyboardVisible
- _objc_msgSend$isPredictionBarEnabled
- _objc_msgSend$macToolbarDetailsButtonProps
- _objc_msgSend$proposedColumnWidth
- _objc_msgSend$setDetailsToolbarItem:
- _objc_msgSend$setProposedColumnWidth:
CStrings:
+ "@\"UIImage\"16@?0@\"NSString\"8"
+ "@56@0:8{CGSize=dd}16d32@40@48"
+ "ActivityTypingBubble-%@"
+ "B24@0:8@\"CKSendMenuPresentation\"16"
+ "Backgrounds disabled in Settings; suppress in UI."
+ "CKMediaObject_Icon"
+ "Fetching collaboration notices for chat GUIDs: %@"
+ "LinkPresentationHelper"
+ "Not returning group photo because isKnownSender == NO, for chat with identifier: %@"
+ "SendAnimationSpecialGlassDuringSendEnabled"
+ "T@\"CKPreviewDispatchCache\",R,N"
+ "T@\"UIView\",R,N,V_primaryVirtualBackgroundView"
+ "T@\"UIView\",R,N,V_secondaryVirtualBackgroundView"
+ "TB,N,V_wasDetectedAsSMSCategory"
+ "TB,R,N,Gck_isUsingSpecialGlassDuringSendAnimationEnabled"
+ "TB,R,N,GsupportsTranscriptBackground"
+ "Using chat display name."
+ "Withholding chat display name because shouldDisplayGroupIdentity == false."
+ "_\t"
+ "_dismissEditMenu"
+ "_generateIconWithSize:scale:type:fileURL:"
+ "_handleIsFilteredChange"
+ "_iMessage_canSendComposition:reachabilityContext:forceSMS:error:"
+ "activeKeyboardSceneDelegate"
+ "cachedIcon"
+ "canLazilyLoadImagesUsingLinkPresentation"
+ "chatIsFilteredChanged:"
+ "ck_isUsingSpecialGlassDuringSendAnimationEnabled"
+ "ck_verySlowSendAnimationEnabled"
+ "ck_veryVerySlowSendAnimationEnabled"
+ "defaultPreviewPriority"
+ "effectiveGeometryDidUpdateForScene:previousEffectiveGeometry:"
+ "eligibleToSendWithMadrid"
+ "fetchCollaborationNoticesForChatGUIDs:completionHandler:"
+ "generateAndCacheIconForMediaObjectWithUTIType:fileURL:completion:"
+ "iMessage enabled: %{bool}d"
+ "iMessageEnabledForReachabilityContext:"
+ "iconPreviewCache"
+ "initWithItemProvider:properties:placeholderImage:"
+ "isKnownSenderWithUnknownFilteringEnabled:"
+ "isPredictionBarAvailableForMentions"
+ "maximumConcurrentCompilationTaskCount"
+ "messagesSceneDelegateDidUpdateEffectiveGeometryForScene:previousEffectiveGeometry:"
+ "progressWithTotalUnitCount:"
+ "send-menu-photos"
+ "sendMenuPresentationShouldUseKeyboardSnapshot:"
+ "setCancellable:"
+ "setPausable:"
+ "shouldDisplayGroupIdentity"
+ "shouldSuppressTranscriptBackgroundUI"
+ "shouldSuppressTranscriptBackgroundUIForConversation:"
+ "showGroupNameAndPhoto"
+ "showGroupNameAndPhotoChange"
+ "windowingModeEnabled"
- ": conversation is not Known because isFiltered: "
- ": conversation isKnown because filterActionKnownSender"
- ": conversation isKnown because hasKnownParticipantsCache"
- "B60@0:8@16@24@32@40B48^@52"
- "Backgrounds disabled in Settings; no further preparation needed."
- "T@\"CKMacBarButtonToolbarItem\",&,N,V_detailsToolbarItem"
- "T@\"UIVisualEffectView\",R,N,V_primaryVirtualBackgroundView"
- "T@\"UIVisualEffectView\",R,N,V_secondaryVirtualBackgroundView"
- "TB,N,V_cachedIsKnownSender"
- "Td,N,V_proposedColumnWidth"
- "Ti,N,V_wasDetectedAsSMSCategory"
- "__ck_isPredictionBarEnabled"
- "_cachedIsKnownSender"
- "_configureDetailsToolbarItem"
- "_defaultPreviewPriority"
- "_detailsToolbarItem"
- "_iMessage_canSendComposition:lastAddressedHandle:lastAddressedSIMID:currentService:forceSMS:error:"
- "_proposedColumnWidth"
- "_updatedDetailsToolbarItemImage"
- "alignmentRectForItemWithIdentifier:"
- "cachedIsKnownSender"
- "chat: %s > isKnownSender changed from %{bool}d to %{bool}d for reason: %s"
- "ck_veryVeryslowSendAnimationEnabled"
- "ck_veryslowSendAnimationEnabled"
- "detailsToolbarItem"
- "fetchCollaborationNoticesForChatGUID:completionHandler:"
- "iMessage enabled: %@"
- "iMessageEnabledForSenderLastAddressedHandle:simID:previousService:"
- "is not known because there are no messages from a contact"
- "is not known because there are no messages from a contact or myself"
- "is3rdPartyKeyboardVisible"
- "isKnown because there is a message from contact"
- "isKnown because there is a message from contact or myself"
- "isPredictionBarEnabled"
- "o\t"
- "proposedColumnWidth"
- "send-menu-photos-dark"
- "send-menu-photos-light"
- "setCachedIsKnownSender:"
- "setDetailsToolbarItem:"
- "setProposedColumnWidth:"
- "showsKeyboardPredictionBar"
- "supportsTranscriptBackgrounds"

```
