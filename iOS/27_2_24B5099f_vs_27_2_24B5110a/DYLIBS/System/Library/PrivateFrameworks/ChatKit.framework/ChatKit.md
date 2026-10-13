## ChatKit

> `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1491.200.95.0.0
-  __TEXT.__text: 0xbea40c
+1491.200.101.2.5
+  __TEXT.__text: 0xbef184
   __TEXT.__delay_stubs: 0x1c0
   __TEXT.__delay_helper: 0x3088
-  __TEXT.__objc_methlist: 0x73844
-  __TEXT.__const: 0x41bc4
-  __TEXT.__gcc_except_tab: 0x206b0
-  __TEXT.__cstring: 0x3fb97
-  __TEXT.__oslogstring: 0x55ea7
+  __TEXT.__objc_methlist: 0x73c04
+  __TEXT.__const: 0x41c54
+  __TEXT.__gcc_except_tab: 0x206dc
+  __TEXT.__cstring: 0x3fbd7
+  __TEXT.__oslogstring: 0x56127
   __TEXT.__dlopen_cstrs: 0xa9e
   __TEXT.__ustring: 0x20a
-  __TEXT.__constg_swiftt: 0x1e138
-  __TEXT.__swift5_typeref: 0x4973a
+  __TEXT.__constg_swiftt: 0x1e1b0
+  __TEXT.__swift5_typeref: 0x4976c
   __TEXT.__swift5_builtin: 0x9b0
-  __TEXT.__swift5_reflstr: 0x130b3
-  __TEXT.__swift5_fieldmd: 0x1112c
+  __TEXT.__swift5_reflstr: 0x13103
+  __TEXT.__swift5_fieldmd: 0x11170
   __TEXT.__swift5_assocty: 0x4aa0
   __TEXT.__swift5_proto: 0x1d2c
-  __TEXT.__swift5_types: 0x14b8
+  __TEXT.__swift5_types: 0x14c0
   __TEXT.__swift5_capture: 0x94c0
   __TEXT.__swift_as_entry: 0x64c
   __TEXT.__swift_as_ret: 0x5dc
   __TEXT.__swift_as_cont: 0xe50
   __TEXT.__swift5_protos: 0xe0
   __TEXT.__swift5_mpenum: 0x140
-  __TEXT.__unwind_info: 0x3dce8
+  __TEXT.__unwind_info: 0x3d980
   __TEXT.__eh_frame: 0x12fc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf480
-  __DATA_CONST.__objc_classlist: 0x3030
+  __DATA_CONST.__const: 0xf570
+  __DATA_CONST.__objc_classlist: 0x3068
   __DATA_CONST.__objc_catlist: 0x568
   __DATA_CONST.__objc_protolist: 0x13f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37988
+  __DATA_CONST.__objc_selrefs: 0x37b48
   __DATA_CONST.__objc_protorefs: 0x580
-  __DATA_CONST.__objc_superrefs: 0x19d8
+  __DATA_CONST.__objc_superrefs: 0x19e8
   __DATA_CONST.__objc_arraydata: 0xed0
-  __DATA_CONST.__got: 0x7d50
-  __AUTH_CONST.__const: 0x3fd48
-  __AUTH_CONST.__cfstring: 0x24420
-  __AUTH_CONST.__objc_const: 0x9e220
+  __DATA_CONST.__got: 0x7dd8
+  __AUTH_CONST.__const: 0x3fd28
+  __AUTH_CONST.__cfstring: 0x24480
+  __AUTH_CONST.__objc_const: 0x9e8a8
   __AUTH_CONST.__objc_arrayobj: 0xde0
   __AUTH_CONST.__objc_intobj: 0xf18
   __AUTH_CONST.__objc_doubleobj: 0x870
   __AUTH_CONST.__objc_floatobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH_CONST.__auth_got: 0x6c48
-  __AUTH.__objc_data: 0x2c9a8
-  __AUTH.__data: 0x15cf8
-  __DATA.__objc_ivar: 0x4a34
-  __DATA.__data: 0x22760
+  __AUTH_CONST.__auth_got: 0x6c50
+  __AUTH.__objc_data: 0x2cc28
+  __AUTH.__data: 0x15df8
+  __DATA.__objc_ivar: 0x4a64
+  __DATA.__data: 0x22980
   __DATA.__objc_stublist: 0x38
-  __DATA.__common: 0x15f0
+  __DATA.__common: 0x1610
   __DATA_DIRTY.__objc_data: 0x68a8
   __DATA_DIRTY.__data: 0x6a0
   __DATA_DIRTY.__bss: 0x520

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 75321
-  Symbols:   73922
-  CStrings:  13288
+  Functions: 75458
+  Symbols:   74051
+  CStrings:  13297
 
Symbols:
+ +[CKComposition(UIPasteboard) compositionByMergingResolvedCompositions:itemProviders:]
+ +[CKComposition(UIPasteboard) requestCompositionsFromItemProviders:completion:]
+ -[CKChatController _conversationCanSendComposition:error:]
+ -[CKChatController _detailsPresentationDecision]
+ -[CKChatController _tapCanPresentDetailsViewController]
+ -[CKChatController appendCompositionFromItemProviders:dragItems:]
+ -[CKChatController isConversationBlockedByCommunicationLimits]
+ -[CKChatController isPerformingAnimatedCompositionChange]
+ -[CKChatController messageEntryViewIsBlockedByCommunicationLimits:]
+ -[CKChatController setIsPerformingAnimatedCompositionChange:]
+ -[CKChatController setStagedDropCoordinator:]
+ -[CKChatController stagedDropCoordinator]
+ -[CKChatItem allowsCopyingMessage]
+ -[CKComposeChatController _askToManagingParentAllowedByScreenTime]
+ -[CKComposeChatController _isAskToRequestCompose]
+ -[CKComposeChatController _recipientSelectionControllerFrame]
+ -[CKComposeChatController askToAllowedByScreenTime]
+ -[CKComposeChatController askToScreenTimeHandleIDs]
+ -[CKComposeChatController conversationAllowedByScreenTime]
+ -[CKComposeChatController isChatAllowedByScreenTime:]
+ -[CKComposeChatController isConversationBlockedByCommunicationLimits]
+ -[CKComposeChatController recipientSelectionControllerShouldAllowManagingParentsWhenBlocked:]
+ -[CKComposeChatController setAskToAllowedByScreenTime:]
+ -[CKComposeChatController setAskToScreenTimeHandleIDs:]
+ -[CKCompositionResolutionSlot .cxx_destruct]
+ -[CKCompositionResolutionSlot dealloc]
+ -[CKCompositionResolutionSlot initWithDispatchGroup:]
+ -[CKCompositionResolutionSlot leave]
+ -[CKConversation canSendComposition:allowedByScreenTime:error:]
+ -[CKConversationListCollectionViewController _updateConversationListVisibilityForSearchPresented:animated:]
+ -[CKDetailsPresentationDecision .cxx_destruct]
+ -[CKDetailsPresentationDecision canPresentDetails]
+ -[CKDetailsPresentationDecision initWithCanPresentDetails:viewControllerForPresentingDetailsOverride:]
+ -[CKDetailsPresentationDecision setCanPresentDetails:]
+ -[CKDetailsPresentationDecision setViewControllerForPresentingDetailsOverride:]
+ -[CKDetailsPresentationDecision viewControllerForPresentingDetailsOverride]
+ -[CKMessageEntryRichTextView stagedImageViewForTransferGUID:]
+ -[CKRecipientSelectionController _updateSearchResultsSafeAreaExtensionView]
+ -[CKRecipientSelectionController isObservingConversationContext]
+ -[CKRecipientSelectionController searchResultsSafeAreaExtensionView]
+ -[CKRecipientSelectionController setIsObservingConversationContext:]
+ -[CKRecipientSelectionController setSearchResultsSafeAreaExtensionView:]
+ -[CKReportSpamChatItem senderIsUnknownInternational]
+ -[CKReportSpamChatItem unknownSenderTranscriptText]
+ -[CKReusableVideoPlayer playerViewController:willTransitionToVisibilityOfPlaybackControls:withAnimationCoordinator:]
+ -[CKSMSComposeController supportsInterweavedCompositionTextInsertion]
+ -[CKSearchViewController _updateTraitOverridesForCurrentSplitViewEnvironment]
+ -[CKTextBalloonView allowsTextSelection]
+ -[CKTextBalloonView setAllowsTextSelection:]
+ -[CKTextBalloonView supportsTextSelection]
+ -[CKTextMessagePartChatItem allowsCopyingMessage]
+ -[CKTextReplyPreviewBalloonView supportsTextSelection]
+ -[CKUITheme _primarySplitViewColumnBackgroundColor]
+ -[CKVideoPlayerBalloonView _isPointInInlinePlaybackControlsZone:]
+ -[CKVideoPlayerBalloonView isShowingInlinePlaybackControls]
+ -[CKVideoPlayerBalloonView reusablePlayer:didChangeVisibilityOfPlaybackControls:]
+ -[CKVideoPlayerBalloonView setShowingInlinePlaybackControls:]
+ GCC_except_table1007
+ GCC_except_table1014
+ GCC_except_table1015
+ GCC_except_table1017
+ GCC_except_table1025
+ GCC_except_table1027
+ GCC_except_table1043
+ GCC_except_table1046
+ GCC_except_table1054
+ GCC_except_table1059
+ GCC_except_table1063
+ GCC_except_table1086
+ GCC_except_table1103
+ GCC_except_table1134
+ GCC_except_table1136
+ GCC_except_table1164
+ GCC_except_table1166
+ GCC_except_table1211
+ GCC_except_table1216
+ GCC_except_table1219
+ GCC_except_table1224
+ GCC_except_table1226
+ GCC_except_table1227
+ GCC_except_table1229
+ GCC_except_table1231
+ GCC_except_table1239
+ GCC_except_table1257
+ GCC_except_table1268
+ GCC_except_table151
+ GCC_except_table153
+ GCC_except_table165
+ GCC_except_table166
+ GCC_except_table211
+ GCC_except_table237
+ GCC_except_table245
+ GCC_except_table259
+ GCC_except_table269
+ GCC_except_table275
+ GCC_except_table282
+ GCC_except_table296
+ GCC_except_table297
+ GCC_except_table298
+ GCC_except_table331
+ GCC_except_table345
+ GCC_except_table356
+ GCC_except_table358
+ GCC_except_table365
+ GCC_except_table381
+ GCC_except_table383
+ GCC_except_table384
+ GCC_except_table394
+ GCC_except_table395
+ GCC_except_table405
+ GCC_except_table419
+ GCC_except_table426
+ GCC_except_table428
+ GCC_except_table438
+ GCC_except_table439
+ GCC_except_table442
+ GCC_except_table448
+ GCC_except_table451
+ GCC_except_table453
+ GCC_except_table457
+ GCC_except_table469
+ GCC_except_table475
+ GCC_except_table482
+ GCC_except_table484
+ GCC_except_table486
+ GCC_except_table488
+ GCC_except_table492
+ GCC_except_table500
+ GCC_except_table503
+ GCC_except_table505
+ GCC_except_table511
+ GCC_except_table514
+ GCC_except_table521
+ GCC_except_table524
+ GCC_except_table530
+ GCC_except_table532
+ GCC_except_table538
+ GCC_except_table542
+ GCC_except_table544
+ GCC_except_table553
+ GCC_except_table582
+ GCC_except_table583
+ GCC_except_table585
+ GCC_except_table599
+ GCC_except_table600
+ GCC_except_table608
+ GCC_except_table609
+ GCC_except_table612
+ GCC_except_table615
+ GCC_except_table620
+ GCC_except_table621
+ GCC_except_table630
+ GCC_except_table632
+ GCC_except_table640
+ GCC_except_table646
+ GCC_except_table647
+ GCC_except_table648
+ GCC_except_table649
+ GCC_except_table651
+ GCC_except_table656
+ GCC_except_table659
+ GCC_except_table663
+ GCC_except_table664
+ GCC_except_table665
+ GCC_except_table668
+ GCC_except_table672
+ GCC_except_table675
+ GCC_except_table676
+ GCC_except_table682
+ GCC_except_table686
+ GCC_except_table693
+ GCC_except_table702
+ GCC_except_table703
+ GCC_except_table707
+ GCC_except_table710
+ GCC_except_table718
+ GCC_except_table719
+ GCC_except_table728
+ GCC_except_table735
+ GCC_except_table736
+ GCC_except_table737
+ GCC_except_table740
+ GCC_except_table750
+ GCC_except_table752
+ GCC_except_table753
+ GCC_except_table754
+ GCC_except_table755
+ GCC_except_table756
+ GCC_except_table765
+ GCC_except_table771
+ GCC_except_table772
+ GCC_except_table783
+ GCC_except_table784
+ GCC_except_table792
+ GCC_except_table794
+ GCC_except_table796
+ GCC_except_table797
+ GCC_except_table802
+ GCC_except_table803
+ GCC_except_table837
+ GCC_except_table839
+ GCC_except_table840
+ GCC_except_table844
+ GCC_except_table870
+ GCC_except_table871
+ GCC_except_table886
+ GCC_except_table887
+ GCC_except_table896
+ GCC_except_table907
+ GCC_except_table910
+ GCC_except_table912
+ GCC_except_table935
+ GCC_except_table938
+ GCC_except_table955
+ GCC_except_table958
+ GCC_except_table959
+ GCC_except_table962
+ GCC_except_table970
+ GCC_except_table971
+ GCC_except_table974
+ GCC_except_table975
+ GCC_except_table985
+ GCC_except_table989
+ GCC_except_table992
+ GCC_except_table999
+ _IMBalloonBundleIDIsAskToRequest
+ _IMSharedHelperCurrentRegionStrengthensUnknownSenderScamWarnings
+ _OBJC_CLASS_$_CKBalloonDoubleTapGestureRecognizer
+ _OBJC_CLASS_$_CKCompositionResolutionSlot
+ _OBJC_CLASS_$_CKDetailsPresentationDecision
+ _OBJC_CLASS_$_CKStagedDropCoordinator
+ _OBJC_CLASS_$_CKStagedImageTextAttachment
+ _OBJC_CLASS_$_LPHomeAccessoryInfo
+ _OBJC_IVAR_$_CKChatController._isPerformingAnimatedCompositionChange
+ _OBJC_IVAR_$_CKChatController._stagedDropCoordinator
+ _OBJC_IVAR_$_CKComposeChatController._askToAllowedByScreenTime
+ _OBJC_IVAR_$_CKComposeChatController._askToScreenTimeHandleIDs
+ _OBJC_IVAR_$_CKCompositionResolutionSlot._didLeave
+ _OBJC_IVAR_$_CKCompositionResolutionSlot._dispatchGroup
+ _OBJC_IVAR_$_CKDetailsPresentationDecision._canPresentDetails
+ _OBJC_IVAR_$_CKDetailsPresentationDecision._viewControllerForPresentingDetailsOverride
+ _OBJC_IVAR_$_CKRecipientSelectionController._isObservingConversationContext
+ _OBJC_IVAR_$_CKRecipientSelectionController._searchResultsSafeAreaExtensionView
+ _OBJC_IVAR_$_CKTextBalloonView._allowsTextSelection
+ _OBJC_IVAR_$_CKVideoPlayerBalloonView._showingInlinePlaybackControls
+ _OBJC_METACLASS_$_CKBalloonDoubleTapGestureRecognizer
+ _OBJC_METACLASS_$_CKCompositionResolutionSlot
+ _OBJC_METACLASS_$_CKDetailsPresentationDecision
+ _OBJC_METACLASS_$_CKStagedDropCoordinator
+ _OBJC_METACLASS_$_CKStagedImageTextAttachment
+ _OBJC_METACLASS_$__TtC7ChatKitP33_46950E96D597C3C2B2F6D28ED528938B39CKStagedImageTextAttachmentViewProvider
+ __CLASS_METHODS_CKStagedImageTextAttachment
+ __CLASS_PROPERTIES_CKStagedImageTextAttachment
+ __DATA_CKStagedDropCoordinator
+ __DATA_CKStagedImageTextAttachment
+ __DATA__TtC7ChatKitP33_43F7786CC9C2682E0D21B0BB8AA55ED016CKStagedDropItem
+ __DATA__TtC7ChatKitP33_46950E96D597C3C2B2F6D28ED528938B39CKStagedImageTextAttachmentViewProvider
+ __INSTANCE_METHODS_CKStagedDropCoordinator
+ __INSTANCE_METHODS_CKStagedImageTextAttachment
+ __INSTANCE_METHODS__TtC7ChatKitP33_46950E96D597C3C2B2F6D28ED528938B39CKStagedImageTextAttachmentViewProvider
+ __IVARS_CKStagedImageTextAttachment
+ __IVARS__TtC7ChatKitP33_43F7786CC9C2682E0D21B0BB8AA55ED016CKStagedDropItem
+ __METACLASS_DATA_CKStagedDropCoordinator
+ __METACLASS_DATA_CKStagedImageTextAttachment
+ __METACLASS_DATA__TtC7ChatKitP33_43F7786CC9C2682E0D21B0BB8AA55ED016CKStagedDropItem
+ __METACLASS_DATA__TtC7ChatKitP33_46950E96D597C3C2B2F6D28ED528938B39CKStagedImageTextAttachmentViewProvider
+ __OBJC_$_INSTANCE_METHODS_CKCompositionResolutionSlot
+ __OBJC_$_INSTANCE_METHODS_CKDetailsPresentationDecision
+ __OBJC_$_INSTANCE_VARIABLES_CKCompositionResolutionSlot
+ __OBJC_$_INSTANCE_VARIABLES_CKDetailsPresentationDecision
+ __OBJC_$_PROP_LIST_CKDetailsPresentationDecision
+ __OBJC_CLASS_RO_$_CKBalloonDoubleTapGestureRecognizer
+ __OBJC_CLASS_RO_$_CKCompositionResolutionSlot
+ __OBJC_CLASS_RO_$_CKDetailsPresentationDecision
+ __OBJC_METACLASS_RO_$_CKBalloonDoubleTapGestureRecognizer
+ __OBJC_METACLASS_RO_$_CKCompositionResolutionSlot
+ __OBJC_METACLASS_RO_$_CKDetailsPresentationDecision
+ __PROPERTIES_CKStagedImageTextAttachment
+ ___107-[CKConversationListCollectionViewController _updateConversationListVisibilityForSearchPresented:animated:]_block_invoke
+ ___107-[CKConversationListCollectionViewController _updateConversationListVisibilityForSearchPresented:animated:]_block_invoke_2
+ ___116-[CKReusableVideoPlayer playerViewController:willTransitionToVisibilityOfPlaybackControls:withAnimationCoordinator:]_block_invoke
+ ___51-[CKUITheme _primarySplitViewColumnBackgroundColor]_block_invoke
+ ___61-[CKMessageEntryRichTextView stagedImageViewForTransferGUID:]_block_invoke
+ ___65-[CKChatController appendCompositionFromItemProviders:dragItems:]_block_invoke
+ ___65-[CKChatController appendCompositionFromItemProviders:dragItems:]_block_invoke_2
+ ___65-[CKChatController appendCompositionFromItemProviders:dragItems:]_block_invoke_3
+ ___71-[CKChatController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke_6
+ ___79+[CKComposition(UIPasteboard) requestCompositionsFromItemProviders:completion:]_block_invoke
+ ___79+[CKComposition(UIPasteboard) requestCompositionsFromItemProviders:completion:]_block_invoke_2
+ ___79+[CKComposition(UIPasteboard) requestCompositionsFromItemProviders:completion:]_block_invoke_3
+ ___86+[CKComposition(UIPasteboard) compositionByMergingResolvedCompositions:itemProviders:]_block_invoke
+ ___block_descriptor_40_e8_32r_e15_v32?08Q16^B24lr32l8
+ ___block_descriptor_49_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e37_v40?0"NSString"8{_NSRange=QQ}16^B32ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSArray"8lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s_e31_v32?0"NSItemProvider"8Q16^B24ls32l8s40l8
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _symbolic So10UIDragItemC_ypt
+ _symbolic _____ 7ChatKit16CKStagedDropItem33_43F7786CC9C2682E0D21B0BB8AA55ED0LLC
+ _symbolic _____ 7ChatKit39CKStagedImageTextAttachmentViewProvider33_46950E96D597C3C2B2F6D28ED528938BLLC
- -[CKChatController appendCompositionFromItemProviders:]
- -[CKTranscriptCollectionViewController _shouldBlockUnknownSenderRichLinks]
- -[CKTranscriptCollectionViewController updateTranscriptChatItems:inserted:removed:reload:regenerate:animated:checkFiltered:completion:]
- -[CKUITheme _conversationListBackgroundColor]
- GCC_except_table1001
- GCC_except_table1005
- GCC_except_table1013
- GCC_except_table1018
- GCC_except_table1021
- GCC_except_table1040
- GCC_except_table1041
- GCC_except_table1057
- GCC_except_table1080
- GCC_except_table1083
- GCC_except_table1127
- GCC_except_table1129
- GCC_except_table1152
- GCC_except_table1157
- GCC_except_table1204
- GCC_except_table1206
- GCC_except_table1208
- GCC_except_table1210
- GCC_except_table1218
- GCC_except_table1221
- GCC_except_table1223
- GCC_except_table1225
- GCC_except_table1233
- GCC_except_table1251
- GCC_except_table1262
- GCC_except_table139
- GCC_except_table201
- GCC_except_table207
- GCC_except_table217
- GCC_except_table252
- GCC_except_table255
- GCC_except_table258
- GCC_except_table277
- GCC_except_table279
- GCC_except_table281
- GCC_except_table285
- GCC_except_table287
- GCC_except_table293
- GCC_except_table308
- GCC_except_table328
- GCC_except_table330
- GCC_except_table334
- GCC_except_table351
- GCC_except_table360
- GCC_except_table372
- GCC_except_table373
- GCC_except_table378
- GCC_except_table380
- GCC_except_table390
- GCC_except_table391
- GCC_except_table392
- GCC_except_table396
- GCC_except_table406
- GCC_except_table410
- GCC_except_table412
- GCC_except_table421
- GCC_except_table423
- GCC_except_table435
- GCC_except_table447
- GCC_except_table454
- GCC_except_table456
- GCC_except_table465
- GCC_except_table468
- GCC_except_table474
- GCC_except_table479
- GCC_except_table490
- GCC_except_table502
- GCC_except_table504
- GCC_except_table509
- GCC_except_table513
- GCC_except_table518
- GCC_except_table520
- GCC_except_table523
- GCC_except_table526
- GCC_except_table529
- GCC_except_table535
- GCC_except_table537
- GCC_except_table543
- GCC_except_table549
- GCC_except_table575
- GCC_except_table579
- GCC_except_table587
- GCC_except_table597
- GCC_except_table603
- GCC_except_table604
- GCC_except_table607
- GCC_except_table610
- GCC_except_table616
- GCC_except_table617
- GCC_except_table623
- GCC_except_table624
- GCC_except_table635
- GCC_except_table641
- GCC_except_table642
- GCC_except_table643
- GCC_except_table644
- GCC_except_table655
- GCC_except_table658
- GCC_except_table661
- GCC_except_table669
- GCC_except_table670
- GCC_except_table671
- GCC_except_table677
- GCC_except_table678
- GCC_except_table681
- GCC_except_table692
- GCC_except_table696
- GCC_except_table705
- GCC_except_table708
- GCC_except_table711
- GCC_except_table713
- GCC_except_table717
- GCC_except_table723
- GCC_except_table731
- GCC_except_table741
- GCC_except_table742
- GCC_except_table744
- GCC_except_table745
- GCC_except_table746
- GCC_except_table747
- GCC_except_table748
- GCC_except_table757
- GCC_except_table764
- GCC_except_table768
- GCC_except_table776
- GCC_except_table780
- GCC_except_table785
- GCC_except_table787
- GCC_except_table788
- GCC_except_table791
- GCC_except_table800
- GCC_except_table801
- GCC_except_table831
- GCC_except_table833
- GCC_except_table834
- GCC_except_table838
- GCC_except_table864
- GCC_except_table865
- GCC_except_table874
- GCC_except_table881
- GCC_except_table890
- GCC_except_table901
- GCC_except_table904
- GCC_except_table906
- GCC_except_table929
- GCC_except_table932
- GCC_except_table949
- GCC_except_table952
- GCC_except_table953
- GCC_except_table956
- GCC_except_table964
- GCC_except_table965
- GCC_except_table968
- GCC_except_table969
- GCC_except_table977
- GCC_except_table979
- GCC_except_table986
- GCC_except_table991
- GCC_except_table993
- GCC_except_table996
- _IMServiceCapabilityDisplayUnknownSenderLinks
- ___45-[CKUITheme _conversationListBackgroundColor]_block_invoke
- ___55-[CKChatController appendCompositionFromItemProviders:]_block_invoke
- ___55-[CKChatController appendCompositionFromItemProviders:]_block_invoke_2
- ___55-[CKChatController appendCompositionFromItemProviders:]_block_invoke_3
- ___55-[CKChatController appendCompositionFromItemProviders:]_block_invoke_4
- _searchControllerObscuresConversationList.sBehavior
CStrings:
+ "Drop preview generation failed because the entry view's text view is not in a window. UIDragPreviewTarget requires that its container be in a window."
+ "DropInteraction returned a staged image preview"
+ "Not starting text selection: copying is not allowed for this message"
+ "REPORT_SPAM_SCAM_STATUS"
+ "Refusing to copy: copying is not allowed for any selected message"
+ "SENDER_IS_UNKNOWN_INTERNATIONAL_SENDER_SCAM_STATUS"
+ "Unexpectedly had no destination imageView available to morph into."
+ "Unexpectedly had to skip a dragItem because no transferGUID was available."
+ "Unexpectedly had to skip a dragItem because there was no stagedItem already prepared."
+ "Updating conversation list view visibility for searchPresented=%{BOOL}d, shouldHideConversationList=%{BOOL}d, animated=%{BOOL}d"
+ "com.apple.home.accessoryinfo"
+ "stagedPreviewForDragItem has valid target view, and will center at (%f, %f)"
- ": NOT muted (expired "
- "Drop preview generation failed because the entry view is not in a window. UIDragPreviewTarget requires that its container (the entry view in this case) be in a window."
- "Mute Identifiers"
```
