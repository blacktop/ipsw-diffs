## ChatKit

> `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1262.300.81.2.13
-  __TEXT.__text: 0x6235a4
+1262.400.41.2.3
+  __TEXT.__text: 0x624e7c
   __TEXT.__auth_stubs: 0x6190
-  __TEXT.__objc_methlist: 0x547d8
+  __TEXT.__objc_methlist: 0x548b8
   __TEXT.__const: 0x9b64
-  __TEXT.__gcc_except_tab: 0x17414
-  __TEXT.__cstring: 0x2f066
-  __TEXT.__oslogstring: 0x2c498
+  __TEXT.__gcc_except_tab: 0x174d4
+  __TEXT.__cstring: 0x2f116
+  __TEXT.__oslogstring: 0x2c703
   __TEXT.__dlopen_cstrs: 0x892
   __TEXT.__ustring: 0xbe
   __TEXT.__swift5_typeref: 0xe6f2
-  __TEXT.__swift5_capture: 0x1054
-  __TEXT.__constg_swiftt: 0x4b84
+  __TEXT.__swift5_capture: 0x1058
+  __TEXT.__constg_swiftt: 0x4b9c
   __TEXT.__swift5_builtin: 0x280
-  __TEXT.__swift5_reflstr: 0x2eb1
-  __TEXT.__swift5_fieldmd: 0x2a6c
+  __TEXT.__swift5_reflstr: 0x2ed1
+  __TEXT.__swift5_fieldmd: 0x2a78
   __TEXT.__swift5_assocty: 0xac8
   __TEXT.__swift5_proto: 0x374
   __TEXT.__swift5_types: 0x2ec
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__unwind_info: 0x1bfa0
+  __TEXT.__unwind_info: 0x1bfe8
   __TEXT.__eh_frame: 0x1a50
   __TEXT.__objc_classname: 0xad73
-  __TEXT.__objc_methname: 0xe460e
-  __TEXT.__objc_methtype: 0x200de
-  __TEXT.__objc_stubs: 0x91ac0
+  __TEXT.__objc_methname: 0xe47f8
+  __TEXT.__objc_methtype: 0x200b3
+  __TEXT.__objc_stubs: 0x91c20
   __DATA_CONST.__got: 0x2758
-  __DATA_CONST.__const: 0xbfb0
+  __DATA_CONST.__const: 0xbfc0
   __DATA_CONST.__objc_classlist: 0x2140
   __DATA_CONST.__objc_catlist: 0x470
   __DATA_CONST.__objc_protolist: 0xf18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7be08
-  __DATA_CONST.__objc_selrefs: 0x2bd60
+  __DATA_CONST.__objc_const: 0x7beb8
+  __DATA_CONST.__objc_selrefs: 0x2bdd0
   __DATA_CONST.__objc_arraydata: 0x1008
-  __AUTH_CONST.__const: 0x190d0
-  __AUTH_CONST.__cfstring: 0x22800
+  __AUTH_CONST.__const: 0x190f8
+  __AUTH_CONST.__cfstring: 0x22840
   __AUTH_CONST.__objc_const: 0x19b88
   __AUTH_CONST.__objc_arrayobj: 0xe40
   __AUTH_CONST.__objc_intobj: 0xf30

   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__auth_got: 0x30d8
   __AUTH.__objc_data: 0x10be0
-  __AUTH.__data: 0x3020
+  __AUTH.__data: 0x3010
   __DATA.__objc_protorefs: 0x200
   __DATA.__objc_classrefs: 0x3198
   __DATA.__objc_superrefs: 0x19b0
-  __DATA.__objc_ivar: 0x4954
+  __DATA.__objc_ivar: 0x4958
   __DATA.__objc_data: 0x238
-  __DATA.__data: 0x12750
+  __DATA.__data: 0x12740
   __DATA.__bss: 0xcfc0
   __DATA.__common: 0xf8
-  __DATA_DIRTY.__objc_data: 0x6c98
+  __DATA_DIRTY.__objc_data: 0x6cb8
   __DATA_DIRTY.__data: 0x348
   __DATA_DIRTY.__bss: 0x1c10
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AEA10B1C-9498-367D-B310-5E69D409CE87
-  Functions: 40090
-  Symbols:   117191
-  CStrings:  49683
+  UUID: 12784B19-CC95-30CE-B8DD-3FFC5C258AC5
+  Functions: 40129
+  Symbols:   117255
+  CStrings:  49715
 
Symbols:
+ +[CKChatItem unloadSizesOfChatItems:]
+ +[CKFullScreenBalloonViewDisplayConfiguration standardContext]
+ -[CKAppCardPresentationOverseer presentationBegan]
+ -[CKChatController dismissEffectPickerAnimated:]
+ -[CKChatController requestDismissKeyboardSnapshotForEffectPickerIfNeeded]
+ -[CKChatController shouldShowVotingViewForFullScreenBalloonViewController:]
+ -[CKChatController transcriptCollectionViewControllerWillBeginFullscreenEffectAnimationForOutgoingMessage:]
+ -[CKChatController(ClickyOrbConformance) presentStickerDetailControllerWithIndexPath:]
+ -[CKChatController(Collaboration) _actuallyPresentCollaborationFailureAlertForComposition:sharingURL:error:completion:].cold.3
+ -[CKChatController(ImpactEffectPicker) _resetEffectPickerViewController]
+ -[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:animated:]
+ -[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:keepingSideMountContainer:animated:]
+ -[CKChatInputController hasStickerReactionSession]
+ -[CKChatItemSizeCache ___invalidateSizeCacheMetricsForKeys:]
+ -[CKChatItemSizeCache invalidateCachedSizeForChatItems:]
+ -[CKComposeChatController prepareToDismissForSecondInstance]
+ -[CKConversationListCollectionViewController _previewForHighlightingOrDismissingContextMenuWithConfiguration:indexPath:collectionView:]
+ -[CKCoreChatController _shouldShowVotingViewForChatItem:]
+ -[CKCoreChatController shouldShowVotingViewForFullScreenBalloonViewController:]
+ -[CKCoreChatController showFullScreenAcknowledgmentPickerForChatItem:displayConfiguration:]
+ -[CKCoreChatController transcriptCollectionViewControllerWillBeginFullscreenEffectAnimationForOutgoingMessage:]
+ -[CKFullScreenBalloonViewController initWithChatItem:gradientReferenceView:delegate:]
+ -[CKFullScreenBalloonViewController shouldShowVotingView]
+ -[CKFullScreenBalloonViewControllerPhone initWithChatItem:title:interfaceActions:gradientReferenceView:pluginBalloonSnapshot:delegate:]
+ -[CKFullScreenBalloonViewDisplayConfiguration setShouldHidePickerBar:]
+ -[CKFullScreenBalloonViewDisplayConfiguration shouldHidePickerBar]
+ -[CKFullscreenEffectMessageFilter setShouldUseMaskImage:]
+ -[CKFullscreenEffectMessageFilter shouldUseMaskImage]
+ -[CKQLPreviewController shouldShowVotingViewForFullScreenBalloonViewController:]
+ -[CKTranscriptCollectionViewController _configureEditMarginInsetsForCell:]
+ -[CKTranscriptPreviewController transcriptCollectionViewControllerWillBeginFullscreenEffectAnimationForOutgoingMessage:]
+ GCC_except_table1001
+ GCC_except_table1044
+ GCC_except_table1046
+ GCC_except_table1050
+ GCC_except_table1054
+ GCC_except_table1060
+ GCC_except_table1061
+ GCC_except_table1063
+ GCC_except_table137
+ GCC_except_table176
+ GCC_except_table184
+ GCC_except_table193
+ GCC_except_table206
+ GCC_except_table209
+ GCC_except_table217
+ GCC_except_table271
+ GCC_except_table304
+ GCC_except_table306
+ GCC_except_table321
+ GCC_except_table324
+ GCC_except_table335
+ GCC_except_table347
+ GCC_except_table356
+ GCC_except_table365
+ GCC_except_table379
+ GCC_except_table386
+ GCC_except_table391
+ GCC_except_table402
+ GCC_except_table423
+ GCC_except_table425
+ GCC_except_table428
+ GCC_except_table444
+ GCC_except_table447
+ GCC_except_table450
+ GCC_except_table452
+ GCC_except_table455
+ GCC_except_table457
+ GCC_except_table462
+ GCC_except_table471
+ GCC_except_table473
+ GCC_except_table475
+ GCC_except_table477
+ GCC_except_table486
+ GCC_except_table490
+ GCC_except_table515
+ GCC_except_table520
+ GCC_except_table524
+ GCC_except_table527
+ GCC_except_table529
+ GCC_except_table532
+ GCC_except_table540
+ GCC_except_table543
+ GCC_except_table546
+ GCC_except_table551
+ GCC_except_table554
+ GCC_except_table560
+ GCC_except_table561
+ GCC_except_table566
+ GCC_except_table570
+ GCC_except_table576
+ GCC_except_table578
+ GCC_except_table579
+ GCC_except_table583
+ GCC_except_table591
+ GCC_except_table594
+ GCC_except_table595
+ GCC_except_table599
+ GCC_except_table602
+ GCC_except_table607
+ GCC_except_table608
+ GCC_except_table624
+ GCC_except_table625
+ GCC_except_table631
+ GCC_except_table638
+ GCC_except_table650
+ GCC_except_table654
+ GCC_except_table655
+ GCC_except_table673
+ GCC_except_table689
+ GCC_except_table701
+ GCC_except_table707
+ GCC_except_table709
+ GCC_except_table711
+ GCC_except_table746
+ GCC_except_table752
+ GCC_except_table753
+ GCC_except_table764
+ GCC_except_table772
+ GCC_except_table774
+ GCC_except_table797
+ GCC_except_table799
+ GCC_except_table816
+ GCC_except_table820
+ GCC_except_table822
+ GCC_except_table829
+ GCC_except_table830
+ GCC_except_table840
+ GCC_except_table843
+ GCC_except_table856
+ GCC_except_table863
+ GCC_except_table864
+ GCC_except_table866
+ GCC_except_table870
+ GCC_except_table877
+ GCC_except_table880
+ GCC_except_table883
+ GCC_except_table896
+ GCC_except_table900
+ GCC_except_table908
+ GCC_except_table912
+ GCC_except_table935
+ GCC_except_table945
+ GCC_except_table952
+ GCC_except_table976
+ GCC_except_table978
+ _IMSupportedAnimatedImageUTTypesSortedByPreference
+ _OBJC_IVAR_$_CKFullScreenBalloonViewDisplayConfiguration._shouldHidePickerBar
+ _OBJC_IVAR_$_CKFullscreenEffectMessageFilter._shouldUseMaskImage
+ ___100+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromFileItemProvider:completionHandler:]_block_invoke.185
+ ___100+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromFileItemProvider:completionHandler:]_block_invoke.188
+ ___100+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromFileItemProvider:completionHandler:]_block_invoke.189
+ ___100+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromFileItemProvider:completionHandler:]_block_invoke_2.187
+ ___100+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromFileItemProvider:completionHandler:]_block_invoke_2.190
+ ___102-[CKChatController(GroupCollaboration) _removeParticipant:fromShareURL:forChatGUID:completionHandler:]_block_invoke.307
+ ___104+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCloudKitItemProvider:completionHandler:]_block_invoke.206
+ ___104+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCloudKitItemProvider:completionHandler:]_block_invoke.209
+ ___105-[CKTranscriptCollectionViewController makeHawkingPromptForMessage:toRecipient:fromSender:withSMSOption:]_block_invoke.944
+ ___107-[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:keepingSideMountContainer:animated:]_block_invoke
+ ___107-[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:keepingSideMountContainer:animated:]_block_invoke_2
+ ___107-[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:keepingSideMountContainer:animated:]_block_invoke_3
+ ___107-[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:keepingSideMountContainer:animated:]_block_invoke_4
+ ___109+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCollaborativeItemProvider:completionHandler:]_block_invoke.211
+ ___115-[CKChatController _presentCollabAddToMessagesGroupAlertIfNecessary:collaborationType:sendBlock:completionHandler:]_block_invoke.945
+ ___156-[CKTranscriptCollectionViewController _indicesOfTranscriptPluginChatItemRemoveAndInsertedWithoutFading:inserted:removed:outInsertIndices:outRemoveIndices:]_block_invoke.736
+ ___236-[CKTranscriptCollectionViewController _updateTranscriptChatItemsWithAnimation:withIMChatItems:oldChatItems:insertedChatItems:inserted:removed:reload:reloadItemGUIDs:wantsScrollToBottom:scrollToBottomDuration:animationCurve:completion:]_block_invoke.742
+ ___39-[CKChatController addToCollaboration:]_block_invoke.1165
+ ___39-[CKChatController addToCollaboration:]_block_invoke_2.1167
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1084
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1088
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_2.1090
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_3.1094
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_4.1098
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_5.1099
+ ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_6.1103
+ ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.969
+ ___61-[CKTranscriptCollectionViewController _resendFailedMessages]_block_invoke.975
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.863.cold.1
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.865
+ ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke.866
+ ___67-[CKChatController _sendCompositionForNewCloudKitShare:completion:]_block_invoke.925
+ ___69-[CKChatController nicknameBannerView:actionButtonTapped:forUpdates:]_block_invoke.1159
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.929
+ ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.934
+ ___71-[CKTranscriptCollectionViewController touchUpInsideCellFailureButton:]_block_invoke.813
+ ___71-[CKTranscriptCollectionViewController touchUpInsideCellFailureButton:]_block_invoke.820
+ ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.893
+ ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.894
+ ___74-[CKTranscriptCollectionViewController touchUpInsideCellReportSpamButton:]_block_invoke.865
+ ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.902
+ ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.903
+ ___81+[CKComposition(UIPasteboard) requestFilenameForType:forItemProvider:completion:]_block_invoke.221
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.286
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.293
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.299
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.305
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.312
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_2.294
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_2.300
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_2.313
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_3.314
+ ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_4.315
+ ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.935
+ ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.960
+ ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.961
+ ___86-[CKChatController(ClickyOrbConformance) presentStickerDetailControllerWithIndexPath:]_block_invoke
+ ___87-[CKChatController _removeSubsharesAndSendFileProviderComposition:shareURL:completion:]_block_invoke.915
+ ___87-[CKChatController _updateAndSendCompositionForExistingCloudKitShare:share:completion:]_block_invoke.926
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.909
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.909.cold.1
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.912
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.913
+ ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke_2.914
+ ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.882
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.222
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.226
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.231
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.236
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.244
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.245
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_2.227
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_2.232
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_2.237
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_3.235
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_3.238
+ ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_4.239
+ ___97-[CKChatController(GroupCollaboration) _addParticipant:toShareURL:forChatGUID:completionHandler:]_block_invoke.289
+ ___block_descriptor_56_e8_32s40s48bs_e8_v16?0q8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e27_v32?0"IMChatItem"8Q16^B24ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8u72l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.1157
+ ___block_literal_global.1188
+ ___block_literal_global.1238
+ ___block_literal_global.1240
+ ___block_literal_global.1250
+ ___block_literal_global.1252
+ ___block_literal_global.1280
+ ___block_literal_global.3312
+ ___block_literal_global.3323
+ ___block_literal_global.3325
+ ___block_literal_global.387
+ ___block_literal_global.672
+ ___block_literal_global.757
+ ___block_literal_global.884
+ ___block_literal_global.913
+ ___block_literal_global.943
+ ___block_literal_global.963
+ ___block_literal_global.977
+ __unnamed_array_storage.422
+ __unnamed_array_storage.871
+ _block_copy_helper.126
+ _block_copy_helper.132
+ _block_copy_helper.138
+ _block_copy_helper.14
+ _block_copy_helper.148
+ _block_copy_helper.155
+ _block_copy_helper.158
+ _block_copy_helper.20
+ _block_copy_helper.26
+ _block_copy_helper.41
+ _block_copy_helper.90
+ _block_descriptor.128
+ _block_descriptor.134
+ _block_descriptor.140
+ _block_descriptor.150
+ _block_descriptor.157
+ _block_descriptor.16
+ _block_descriptor.160
+ _block_descriptor.22
+ _block_descriptor.28
+ _block_descriptor.43
+ _block_descriptor.92
+ _block_destroy_helper.127
+ _block_destroy_helper.133
+ _block_destroy_helper.139
+ _block_destroy_helper.149
+ _block_destroy_helper.15
+ _block_destroy_helper.156
+ _block_destroy_helper.159
+ _block_destroy_helper.21
+ _block_destroy_helper.27
+ _block_destroy_helper.42
+ _block_destroy_helper.91
+ _objc_msgSend$___invalidateSizeCacheMetricsForKeys:
+ _objc_msgSend$_configureEditMarginInsetsForCell:
+ _objc_msgSend$_previewForHighlightingOrDismissingContextMenuWithConfiguration:indexPath:collectionView:
+ _objc_msgSend$_resetEffectPickerViewController
+ _objc_msgSend$dismissEffectPickerAnimated:
+ _objc_msgSend$effectPickerViewControllerClose:animated:
+ _objc_msgSend$effectPickerViewControllerClose:keepingSideMountContainer:animated:
+ _objc_msgSend$hasStickerReactionSession
+ _objc_msgSend$initWithChatItem:gradientReferenceView:delegate:
+ _objc_msgSend$initWithChatItem:title:interfaceActions:gradientReferenceView:pluginBalloonSnapshot:delegate:
+ _objc_msgSend$invalidateCachedSizeForChatItems:
+ _objc_msgSend$presentStickerDetailControllerWithIndexPath:
+ _objc_msgSend$presentationBegan
+ _objc_msgSend$recordID
+ _objc_msgSend$requestDismissKeyboardSnapshotForEffectPickerIfNeeded
+ _objc_msgSend$setShouldHidePickerBar:
+ _objc_msgSend$shouldHidePickerBar
+ _objc_msgSend$shouldShowVotingViewForFullScreenBalloonViewController:
+ _objc_msgSend$shouldUseMaskImage
+ _objc_msgSend$showFullScreenAcknowledgmentPickerForChatItem:displayConfiguration:
+ _objc_msgSend$standardContext
+ _objc_msgSend$transcriptCollectionViewControllerWillBeginFullscreenEffectAnimationForOutgoingMessage:
+ _objc_msgSend$unloadSizesOfChatItems:
+ _objectdestroy.113Tm
+ _objectdestroy.120Tm
+ _objectdestroy.18Tm
- +[CKFullScreenBalloonViewDisplayConfiguration standardContextWithVotingViewShown:]
- -[CKChatController(ClickyOrbConformance) _shouldShowVotingViewForChatItem:]
- -[CKChatController(ClickyOrbConformance) presentStickerDetailControllerWithChatItem:]
- -[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:]
- -[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:keepingSideMountContainer:]
- -[CKChatItemSizeCache _invalidateCachedSizeForChatItemGUID:]
- -[CKChatItemSizeCache _invalidateSizeCacheMetricsForKey:]
- -[CKChatItemSizeCache invalidateCachedSizeForChatItem:]
- -[CKConversationListCollectionViewController _previewForHighlightingOrDismissingContextMenuWithConfiguration:collectionView:]
- -[CKFullScreenBalloonViewController initWithChatItem:gradientReferenceView:isGroupConversation:delegate:]
- -[CKFullScreenBalloonViewControllerPhone initWithChatItem:title:interfaceActions:gradientReferenceView:isGroupConversation:pluginBalloonSnapshot:delegate:]
- -[CKFullScreenBalloonViewDisplayConfiguration setShouldShowVotingView:]
- -[CKFullScreenBalloonViewDisplayConfiguration shouldShowVotingView]
- GCC_except_table1039
- GCC_except_table1041
- GCC_except_table1043
- GCC_except_table1045
- GCC_except_table1049
- GCC_except_table1055
- GCC_except_table1056
- GCC_except_table116
- GCC_except_table150
- GCC_except_table151
- GCC_except_table166
- GCC_except_table198
- GCC_except_table216
- GCC_except_table270
- GCC_except_table294
- GCC_except_table318
- GCC_except_table322
- GCC_except_table334
- GCC_except_table346
- GCC_except_table355
- GCC_except_table364
- GCC_except_table377
- GCC_except_table385
- GCC_except_table390
- GCC_except_table422
- GCC_except_table424
- GCC_except_table427
- GCC_except_table437
- GCC_except_table442
- GCC_except_table449
- GCC_except_table451
- GCC_except_table453
- GCC_except_table456
- GCC_except_table459
- GCC_except_table470
- GCC_except_table472
- GCC_except_table474
- GCC_except_table476
- GCC_except_table485
- GCC_except_table488
- GCC_except_table505
- GCC_except_table517
- GCC_except_table522
- GCC_except_table525
- GCC_except_table528
- GCC_except_table530
- GCC_except_table539
- GCC_except_table542
- GCC_except_table545
- GCC_except_table549
- GCC_except_table558
- GCC_except_table559
- GCC_except_table562
- GCC_except_table568
- GCC_except_table572
- GCC_except_table577
- GCC_except_table581
- GCC_except_table587
- GCC_except_table590
- GCC_except_table593
- GCC_except_table597
- GCC_except_table598
- GCC_except_table605
- GCC_except_table606
- GCC_except_table616
- GCC_except_table617
- GCC_except_table629
- GCC_except_table636
- GCC_except_table648
- GCC_except_table652
- GCC_except_table653
- GCC_except_table671
- GCC_except_table687
- GCC_except_table699
- GCC_except_table704
- GCC_except_table706
- GCC_except_table708
- GCC_except_table742
- GCC_except_table748
- GCC_except_table749
- GCC_except_table760
- GCC_except_table768
- GCC_except_table770
- GCC_except_table793
- GCC_except_table795
- GCC_except_table811
- GCC_except_table815
- GCC_except_table817
- GCC_except_table824
- GCC_except_table825
- GCC_except_table833
- GCC_except_table835
- GCC_except_table841
- GCC_except_table848
- GCC_except_table857
- GCC_except_table859
- GCC_except_table861
- GCC_except_table865
- GCC_except_table873
- GCC_except_table875
- GCC_except_table890
- GCC_except_table891
- GCC_except_table903
- GCC_except_table907
- GCC_except_table930
- GCC_except_table940
- GCC_except_table947
- GCC_except_table971
- GCC_except_table973
- GCC_except_table996
- _IMSupportedAnimatedImageUTTypes
- _OBJC_IVAR_$_CKFullScreenBalloonViewDisplayConfiguration._shouldShowVotingView
- ___100+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromFileItemProvider:completionHandler:]_block_invoke.186
- ___100+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromFileItemProvider:completionHandler:]_block_invoke.187
- ___100+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromFileItemProvider:completionHandler:]_block_invoke_2.188
- ___102-[CKChatController(GroupCollaboration) _removeParticipant:fromShareURL:forChatGUID:completionHandler:]_block_invoke.301
- ___104+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCloudKitItemProvider:completionHandler:]_block_invoke.204
- ___104+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCloudKitItemProvider:completionHandler:]_block_invoke.205
- ___105-[CKTranscriptCollectionViewController makeHawkingPromptForMessage:toRecipient:fromSender:withSMSOption:]_block_invoke.943
- ___109+[CKComposition(UIPasteboard) createPluginPayloadCompositionFromCollaborativeItemProvider:completionHandler:]_block_invoke.209
- ___115-[CKChatController _presentCollabAddToMessagesGroupAlertIfNecessary:collaborationType:sendBlock:completionHandler:]_block_invoke.943
- ___156-[CKTranscriptCollectionViewController _indicesOfTranscriptPluginChatItemRemoveAndInsertedWithoutFading:inserted:removed:outInsertIndices:outRemoveIndices:]_block_invoke.734
- ___236-[CKTranscriptCollectionViewController _updateTranscriptChatItemsWithAnimation:withIMChatItems:oldChatItems:insertedChatItems:inserted:removed:reload:reloadItemGUIDs:wantsScrollToBottom:scrollToBottomDuration:animationCurve:completion:]_block_invoke.741
- ___39-[CKChatController addToCollaboration:]_block_invoke.1161
- ___39-[CKChatController addToCollaboration:]_block_invoke_2.1163
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1082
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke.1086
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_2.1088
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_3.1092
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_4.1096
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_5.1097
- ___49-[CKChatController _interfaceActionsForChatItem:]_block_invoke_6.1101
- ___50-[NSArray(CKChatItems) __ck_unloadSizesAtIndexes:]_block_invoke
- ___59-[CKChatController _validateAndSendComposition:completion:]_block_invoke.965
- ___61-[CKTranscriptCollectionViewController _resendFailedMessages]_block_invoke.974
- ___62-[CKChatController sendCompositionForFileProvider:completion:]_block_invoke_3
- ___67-[CKChatController _sendCompositionForNewCloudKitShare:completion:]_block_invoke.923
- ___69-[CKChatController nicknameBannerView:actionButtonTapped:forUpdates:]_block_invoke.1155
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.926
- ___70-[CKChatController sendCompositionForPendingCollaboration:completion:]_block_invoke.927
- ___71-[CKTranscriptCollectionViewController touchUpInsideCellFailureButton:]_block_invoke.811
- ___71-[CKTranscriptCollectionViewController touchUpInsideCellFailureButton:]_block_invoke.819
- ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.891
- ___73-[CKChatController _sendCompositionForFileProviderCloudDrive:completion:]_block_invoke.892
- ___74-[CKTranscriptCollectionViewController touchUpInsideCellReportSpamButton:]_block_invoke.863
- ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.900
- ___76-[CKChatController _startSharingForURLForFileProviderCloudDrive:completion:]_block_invoke.901
- ___81+[CKComposition(UIPasteboard) requestFilenameForType:forItemProvider:completion:]_block_invoke.219
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.284
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.291
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.297
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.303
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke.310
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_2.292
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_2.298
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_2.311
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_3.312
- ___81+[CKComposition(UIPasteboard) requestMediaObjectForItemProvider:type:completion:]_block_invoke_4.313
- ___81-[CKChatController sendCompositionForCollaboration:collaborationType:completion:]_block_invoke.933
- ___85-[CKChatController(ClickyOrbConformance) presentStickerDetailControllerWithChatItem:]_block_invoke
- ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.958
- ___86-[CKChatController _presentCollabAddToMessagesGroupAlert:sendBlock:completionHandler:]_block_invoke.959
- ___87-[CKChatController _removeSubsharesAndSendFileProviderComposition:shareURL:completion:]_block_invoke.913
- ___87-[CKChatController _updateAndSendCompositionForExistingCloudKitShare:share:completion:]_block_invoke.924
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.907
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.907.cold.1
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.908
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke.911
- ___89-[CKChatController _updateAndSendCompositionForFileProvider:share:sharingURL:completion:]_block_invoke_2.912
- ___93-[CKChatController _sendCollaborationCompositionForFileProvider:sharingURL:share:completion:]_block_invoke.878
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.220
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.224
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.229
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.234
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.241
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke.242
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_2.225
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_2.230
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_2.235
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_3.233
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_3.236
- ___96+[CKComposition(UIPasteboard) requestCompositionFromItemProviderForNonCollaboration:completion:]_block_invoke_4.237
- ___96-[CKChatController(ImpactEffectPicker) effectPickerViewController:effectWithIdentifierSelected:]_block_invoke_3
- ___97-[CKChatController(GroupCollaboration) _addParticipant:toShareURL:forChatGUID:completionHandler:]_block_invoke.283
- ___98-[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:keepingSideMountContainer:]_block_invoke
- ___98-[CKChatController(ImpactEffectPicker) effectPickerViewControllerClose:keepingSideMountContainer:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48s_e23_v16?0"CKComposition"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e27_v32?0"IMChatItem"8Q16^B24ls32l8s40l8s48l8r56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0lu72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1007
- ___block_literal_global.1151
- ___block_literal_global.1153
- ___block_literal_global.1184
- ___block_literal_global.1248
- ___block_literal_global.1268
- ___block_literal_global.1276
- ___block_literal_global.3305
- ___block_literal_global.3316
- ___block_literal_global.3318
- ___block_literal_global.755
- ___block_literal_global.771
- ___block_literal_global.882
- ___block_literal_global.941
- ___block_literal_global.945
- ___block_literal_global.961
- __unnamed_array_storage.417
- __unnamed_array_storage.870
- _block_copy_helper.11
- _block_copy_helper.121
- _block_copy_helper.127
- _block_copy_helper.133
- _block_copy_helper.143
- _block_copy_helper.150
- _block_copy_helper.153
- _block_copy_helper.17
- _block_copy_helper.32
- _block_descriptor.123
- _block_descriptor.129
- _block_descriptor.13
- _block_descriptor.135
- _block_descriptor.145
- _block_descriptor.152
- _block_descriptor.155
- _block_descriptor.19
- _block_descriptor.34
- _block_destroy_helper.12
- _block_destroy_helper.122
- _block_destroy_helper.128
- _block_destroy_helper.134
- _block_destroy_helper.144
- _block_destroy_helper.151
- _block_destroy_helper.154
- _block_destroy_helper.18
- _block_destroy_helper.33
- _objc_msgSend$_invalidateCachedSizeForChatItemGUID:
- _objc_msgSend$_invalidateSizeCacheMetricsForKey:
- _objc_msgSend$_previewForHighlightingOrDismissingContextMenuWithConfiguration:collectionView:
- _objc_msgSend$effectPickerViewControllerClose:
- _objc_msgSend$effectPickerViewControllerClose:keepingSideMountContainer:
- _objc_msgSend$initWithChatItem:gradientReferenceView:isGroupConversation:delegate:
- _objc_msgSend$initWithChatItem:title:interfaceActions:gradientReferenceView:isGroupConversation:pluginBalloonSnapshot:delegate:
- _objc_msgSend$invalidateCachedSizeForChatItem:
- _objc_msgSend$presentStickerDetailControllerWithChatItem:
- _objc_msgSend$repositionSticker:associatedChatItem:onService:
- _objc_msgSend$setShouldShowVotingView:
- _objc_msgSend$standardContextWithVotingViewShown:
- _objectdestroy.108Tm
- _objectdestroy.115Tm
- _objectdestroy.15Tm
CStrings:
+ "!!!"
+ "#\""
+ "Determined index path for first unread message: scrollTarget(%@) and highlightTarget(%@)"
+ "Failed to get user's currentStatus, error: %@"
+ "InvalidateChatItems"
+ "InvalidateChatItems: ANIMATE CHAT ITEM RELOAD: %lu chat items"
+ "InvalidateChatItems: ANIMATE CHAT REMOVAL, oldChatItems: %lu"
+ "InvalidateChatItems: INSERTED %lu chat items"
+ "InvalidateChatItems: REGENERATE %lu chat items"
+ "InvalidateChatItems: old number of cached size = %lu, number of invalidated sizes = %lu, number of new chaches size = %lu"
+ "InvalidateChatItemsHandle"
+ "Querying for current user's status on share %@"
+ "Received current user's status for share %@, status: %ld, error: %@"
+ "Showing collaboration failure for error: %@"
+ "TB,N,V_shouldHidePickerBar"
+ "TB,N,V_shouldUseMaskImage"
+ "TB,N,VpresentationBegan"
+ "User tapped default alert button, action: %ld"
+ "User tapped other alert button"
+ "___invalidateSizeCacheMetrics: Current cache count: %ld – invalidation count: %ld – expected new count: %ld"
+ "___invalidateSizeCacheMetricsForKeys:"
+ "_configureEditMarginInsetsForCell:"
+ "_previewForHighlightingOrDismissingContextMenuWithConfiguration:indexPath:collectionView:"
+ "_resetEffectPickerViewController"
+ "_shouldHidePickerBar"
+ "_shouldUseMaskImage"
+ "dismissEffectPickerAnimated:"
+ "effectPickerViewControllerClose:animated:"
+ "effectPickerViewControllerClose:keepingSideMountContainer:animated:"
+ "hasStickerReactionSession"
+ "initWithChatItem:gradientReferenceView:delegate:"
+ "initWithChatItem:title:interfaceActions:gradientReferenceView:pluginBalloonSnapshot:delegate:"
+ "invalidateCachedSizeForChatItems:"
+ "presentStickerDetailControllerWithIndexPath:"
+ "presentationBegan"
+ "recordID"
+ "requestDismissKeyboardSnapshotForEffectPickerIfNeeded"
+ "setPresentationBegan:"
+ "setShouldHidePickerBar:"
+ "setShouldUseMaskImage:"
+ "shouldDelayViewControllerPresentation"
+ "shouldHidePickerBar"
+ "shouldShowVotingViewForFullScreenBalloonViewController:"
+ "shouldUseMaskImage"
+ "showFullScreenAcknowledgmentPickerForChatItem:displayConfiguration:"
+ "standardContext"
+ "transcriptCollectionViewControllerWillBeginFullscreenEffectAnimationForOutgoingMessage:"
+ "unloadSizesOfChatItems:"
+ "v32@0:8@\"<CKEffectPickerViewControllerProtocol>\"16B24B28"
- "\x13\""
- "@44@0:8@16@24B32@36"
- "@68@0:8@16@24@32@40B48@52@60"
- "Determined index path for first unread message: scrollTarget(%@) and higlightTarget(%@)"
- "TB,N,V_shouldShowVotingView"
- "Unable to invalidate for key %@. sizeMetrics %@ guid %@"
- "_invalidateCachedSizeForChatItemGUID:"
- "_invalidateSizeCacheMetricsForKey:"
- "_previewForHighlightingOrDismissingContextMenuWithConfiguration:collectionView:"
- "_shouldShowVotingView"
- "effectPickerViewControllerClose:"
- "effectPickerViewControllerClose:keepingSideMountContainer:"
- "initWithChatItem:gradientReferenceView:isGroupConversation:delegate:"
- "initWithChatItem:title:interfaceActions:gradientReferenceView:isGroupConversation:pluginBalloonSnapshot:delegate:"
- "invalidateCachedSizeForChatItem:"
- "presentStickerDetailControllerWithChatItem:"
- "repositionSticker:associatedChatItem:onService:"
- "setShouldShowVotingView:"
- "standardContextWithVotingViewShown:"
- "v24@0:8@\"<CKEffectPickerViewControllerProtocol>\"16"

```
