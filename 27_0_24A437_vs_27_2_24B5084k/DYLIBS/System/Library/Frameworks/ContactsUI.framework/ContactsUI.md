## ContactsUI

> `/System/Library/Frameworks/ContactsUI.framework/ContactsUI`

```diff

-1461.100.1.0.0
-  __TEXT.__text: 0x36b8d8
-  __TEXT.__objc_methlist: 0x39594
+1463.200.41.0.0
+  __TEXT.__text: 0x36e264
+  __TEXT.__objc_methlist: 0x397ec
   __TEXT.__dlopen_cstrs: 0x183b
-  __TEXT.__const: 0xc470
-  __TEXT.__oslogstring: 0xaf50
-  __TEXT.__swift5_typeref: 0xefd2
-  __TEXT.__cstring: 0x1393b
-  __TEXT.__constg_swiftt: 0x5588
-  __TEXT.__swift5_reflstr: 0x3901
-  __TEXT.__swift5_fieldmd: 0x357c
+  __TEXT.__const: 0xc550
+  __TEXT.__oslogstring: 0xb29d
+  __TEXT.__swift5_typeref: 0xeff2
+  __TEXT.__cstring: 0x13960
+  __TEXT.__constg_swiftt: 0x5620
+  __TEXT.__swift5_reflstr: 0x3a11
+  __TEXT.__swift5_fieldmd: 0x35f0
   __TEXT.__swift5_builtin: 0x230
   __TEXT.__swift5_assocty: 0xeb8
-  __TEXT.__swift5_capture: 0x1594
-  __TEXT.__swift5_proto: 0x454
-  __TEXT.__swift5_types: 0x3cc
+  __TEXT.__swift5_capture: 0x15b4
+  __TEXT.__swift5_proto: 0x45c
+  __TEXT.__swift5_types: 0x3d4
   __TEXT.__swift_as_entry: 0xa8
   __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift_as_cont: 0x1e8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0x32f8
+  __TEXT.__gcc_except_tab: 0x330c
   __TEXT.__ustring: 0x79a
-  __TEXT.__unwind_info: 0x111a0
+  __TEXT.__unwind_info: 0x11250
   __TEXT.__eh_frame: 0x260c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6818
+  __DATA_CONST.__const: 0x6840
   __DATA_CONST.__objc_classlist: 0x1778
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0x980
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18610
+  __DATA_CONST.__objc_selrefs: 0x187d0
   __DATA_CONST.__objc_protorefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0xf38
   __DATA_CONST.__objc_arraydata: 0x5f0
-  __DATA_CONST.__got: 0x2b50
-  __AUTH_CONST.__const: 0xa438
-  __AUTH_CONST.__cfstring: 0xba60
-  __AUTH_CONST.__objc_const: 0x59520
+  __DATA_CONST.__got: 0x2b58
+  __AUTH_CONST.__const: 0xa5b0
+  __AUTH_CONST.__cfstring: 0xba80
+  __AUTH_CONST.__objc_const: 0x59740
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2cd0
-  __AUTH.__objc_data: 0xfa38
+  __AUTH_CONST.__auth_got: 0x2cd8
+  __AUTH.__objc_data: 0xfab8
   __AUTH.__data: 0x35f0
-  __DATA.__objc_ivar: 0x3c60
-  __DATA.__data: 0xad28
+  __DATA.__objc_ivar: 0x3c84
+  __DATA.__data: 0xadc8
   __DATA.__common: 0x358
   __DATA_DIRTY.__objc_data: 0x2318
-  __DATA_DIRTY.__data: 0xd8
-  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__data: 0xe0
+  __DATA_DIRTY.__bss: 0x148
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24397
-  Symbols:   44655
-  CStrings:  3236
+  Functions: 24470
+  Symbols:   44774
+  CStrings:  3249
 
Symbols:
+ +[CNContactListStyleApplier subtitleNumberOfLinesForAccessibilityContentSizeCategory:]
+ +[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:safeAreaInsets:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]
+ +[CNContactListViewController layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:listAppearance:safeAreaInsets:collectionViewIsShowingIndexBar:contentUnavailable:]
+ +[CNPhotosPosterConfigurationReader boundsForImageSize:normalizedVisibleRect:]
+ +[CNPhotosPosterConfigurationReader faceCropRectForNormalizedFaceRect:imageSize:normalizedVisibleRect:faceCenterFraction:]
+ -[CNCardSharedProfileCellView cachedShouldHideSharedProfileMenu]
+ -[CNCardSharedProfileCellView setCachedShouldHideSharedProfileMenu:]
+ -[CNCardSharedProfileCellView shouldHideSharedProfileMenu]
+ -[CNContact(UIAdditions) persistedLinkedContacts]
+ -[CNContactContentUnitaryViewController avatarEditingSourceContactForHeaderView:]
+ -[CNContactContentUnitaryViewController cardEditingFamilySharingGroup]
+ -[CNContactContentUnitaryViewController didSelectActionItem:actionType:sourceView:]
+ -[CNContactContentUnitaryViewController meCardAvatarEditingSourceContact]
+ -[CNContactContentUnitaryViewController setCardEditingFamilySharingGroup:]
+ -[CNContactContentUnitaryViewController setMeCardAvatarEditingSourceContact:]
+ -[CNContactDataSourceLIFOScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[CNContactHeaderEditView contactForVisualIdentityEditingFromContact:]
+ -[CNContactInlineActionsViewController actionsControllerForType:]
+ -[CNContactInlineActionsViewController actionsControllersByType]
+ -[CNContactInlineActionsViewController actionsControllersContact]
+ -[CNContactInlineActionsViewController invalidateActionsControllersIfNeeded]
+ -[CNContactInlineActionsViewController makeActionsControllerForActionType:]
+ -[CNContactInlineActionsViewController setActionsControllersByType:]
+ -[CNContactInlineActionsViewController setActionsControllersContact:]
+ -[CNContactInlineActionsViewController shouldPresentDisambiguationUIForActionType:]
+ -[CNContactListActionHelper allowsFullSwipeToDeleteContact:]
+ -[CNContactListActionHelper canShowDeleteActionForContacts:]
+ -[CNContactListActionHelper deleteContacts:offeringRemovalFromList:dismissalHandler:]
+ -[CNContactListActionHelper groupName]
+ -[CNContactListBannerView footnoteContainerLeadingConstraint]
+ -[CNContactListBannerView labelsLeadingInset]
+ -[CNContactListBannerView safeAreaInsetsDidChange]
+ -[CNContactListBannerView setFootnoteContainerLeadingConstraint:]
+ -[CNContactListBannerView setTitleLabelLeadingConstraint:]
+ -[CNContactListBannerView titleLabelLeadingConstraint]
+ -[CNContactListBannerView updateAvatarLeadingConstraint]
+ -[CNContactListBannerView updateLabelsLeadingInset]
+ -[CNContactListCollectionViewCell directionalLayoutMargins]
+ -[CNContactListDeleteContactsAction confirmationDismissalHandler]
+ -[CNContactListDeleteContactsAction finishConfirmationWithOutcome:]
+ -[CNContactListDeleteContactsAction groupNameForRemovalOption]
+ -[CNContactListDeleteContactsAction offersRemoveFromGroup]
+ -[CNContactListDeleteContactsAction removeFromGroupHandler]
+ -[CNContactListDeleteContactsAction setConfirmationDismissalHandler:]
+ -[CNContactListDeleteContactsAction setGroupNameForRemovalOption:]
+ -[CNContactListDeleteContactsAction setRemoveFromGroupHandler:]
+ -[CNContactListStyleApplier applyContactListDirectionalLayoutMargins:toLayoutSection:listAppearance:safeAreaInsets:collectionViewIsShowingIndexBar:]
+ -[CNContactListStyleApplier applyContactListStyleToHeaderFooter:withTitle:]
+ -[CNContactListStyleApplier applySearchExcerptToContentConfiguration:withSubtitleText:]
+ -[CNContactListStyleDefaultProvider avatarLeadingLayoutMarginForListAppearance:]
+ -[CNContactListStyleDefaultProvider selectionLeadingInsetForListAppearance:]
+ -[CNContactListStyleDefaultProvider selectionTrailingInsetForListAppearance:]
+ -[CNPhotosPosterConfigurationReader copyFullExtentPreviewImage]
+ -[CNPhotosPosterConfigurationReader copyVisibleFrameImage]
+ -[CNPhotosPosterConfigurationReader normalizedFaceRectInVisibleFrame]
+ -[CNPhotosPosterConfigurationReader normalizedFaceRect]
+ -[CNPhotosPosterConfigurationReader normalizedVisibleRect]
+ -[CNUIAfterCACommitScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[UINavigationBar(CNUI) cnui_setScrollPocketContributionSuppressed:]
+ -[UIView(CNDirectionalSafeArea) cnui_directionalSafeAreaInsets]
+ GCC_except_table10173
+ GCC_except_table10179
+ GCC_except_table10401
+ GCC_except_table10602
+ GCC_except_table10616
+ GCC_except_table10630
+ GCC_except_table10888
+ GCC_except_table10890
+ GCC_except_table10959
+ GCC_except_table10960
+ GCC_except_table10961
+ GCC_except_table10976
+ GCC_except_table11258
+ GCC_except_table11264
+ GCC_except_table11316
+ GCC_except_table11320
+ GCC_except_table11525
+ GCC_except_table11712
+ GCC_except_table11717
+ GCC_except_table11720
+ GCC_except_table11730
+ GCC_except_table11732
+ GCC_except_table11733
+ GCC_except_table11757
+ GCC_except_table11777
+ GCC_except_table11782
+ GCC_except_table11840
+ GCC_except_table11952
+ GCC_except_table12047
+ GCC_except_table12074
+ GCC_except_table12193
+ GCC_except_table12255
+ GCC_except_table12317
+ GCC_except_table12318
+ GCC_except_table12328
+ GCC_except_table12329
+ GCC_except_table12773
+ GCC_except_table12796
+ GCC_except_table13094
+ GCC_except_table13128
+ GCC_except_table13231
+ GCC_except_table13428
+ GCC_except_table13496
+ GCC_except_table13502
+ GCC_except_table13576
+ GCC_except_table13577
+ GCC_except_table13585
+ GCC_except_table13665
+ GCC_except_table13670
+ GCC_except_table13843
+ GCC_except_table13862
+ GCC_except_table14011
+ GCC_except_table14040
+ GCC_except_table14041
+ GCC_except_table14175
+ GCC_except_table14262
+ GCC_except_table14269
+ GCC_except_table14306
+ GCC_except_table14561
+ GCC_except_table14564
+ GCC_except_table14670
+ GCC_except_table14689
+ GCC_except_table14956
+ GCC_except_table15031
+ GCC_except_table15152
+ GCC_except_table15156
+ GCC_except_table15230
+ GCC_except_table15296
+ GCC_except_table15304
+ GCC_except_table15306
+ GCC_except_table15310
+ GCC_except_table15329
+ GCC_except_table15331
+ GCC_except_table15500
+ GCC_except_table15601
+ GCC_except_table15681
+ GCC_except_table15685
+ GCC_except_table15703
+ GCC_except_table15753
+ GCC_except_table15876
+ GCC_except_table16183
+ GCC_except_table16198
+ GCC_except_table16214
+ GCC_except_table16227
+ GCC_except_table16228
+ GCC_except_table16232
+ GCC_except_table16233
+ GCC_except_table16253
+ GCC_except_table16329
+ GCC_except_table16718
+ GCC_except_table16720
+ GCC_except_table16729
+ GCC_except_table16824
+ GCC_except_table16927
+ GCC_except_table17057
+ GCC_except_table17344
+ GCC_except_table17348
+ GCC_except_table17832
+ GCC_except_table17850
+ GCC_except_table17902
+ GCC_except_table17912
+ GCC_except_table17920
+ GCC_except_table17941
+ GCC_except_table17958
+ GCC_except_table17978
+ GCC_except_table18000
+ GCC_except_table18014
+ GCC_except_table18017
+ GCC_except_table18019
+ GCC_except_table18026
+ GCC_except_table18027
+ GCC_except_table18054
+ GCC_except_table18182
+ GCC_except_table18192
+ GCC_except_table18208
+ GCC_except_table18212
+ GCC_except_table18216
+ GCC_except_table18218
+ GCC_except_table18264
+ GCC_except_table18362
+ GCC_except_table18476
+ GCC_except_table18533
+ GCC_except_table18534
+ GCC_except_table18541
+ GCC_except_table18546
+ GCC_except_table18551
+ GCC_except_table18560
+ GCC_except_table18563
+ GCC_except_table18588
+ GCC_except_table18610
+ GCC_except_table18628
+ GCC_except_table18629
+ GCC_except_table18640
+ GCC_except_table18647
+ GCC_except_table18648
+ GCC_except_table18651
+ GCC_except_table18653
+ GCC_except_table18655
+ GCC_except_table18668
+ GCC_except_table18809
+ GCC_except_table18865
+ GCC_except_table2891
+ GCC_except_table2960
+ GCC_except_table3038
+ GCC_except_table3039
+ GCC_except_table3040
+ GCC_except_table3155
+ GCC_except_table3285
+ GCC_except_table3457
+ GCC_except_table3459
+ GCC_except_table3592
+ GCC_except_table3594
+ GCC_except_table3672
+ GCC_except_table3792
+ GCC_except_table4009
+ GCC_except_table4010
+ GCC_except_table4181
+ GCC_except_table4223
+ GCC_except_table4257
+ GCC_except_table4377
+ GCC_except_table4467
+ GCC_except_table4741
+ GCC_except_table4745
+ GCC_except_table4817
+ GCC_except_table4823
+ GCC_except_table4998
+ GCC_except_table5039
+ GCC_except_table5113
+ GCC_except_table5114
+ GCC_except_table5120
+ GCC_except_table5122
+ GCC_except_table5177
+ GCC_except_table5197
+ GCC_except_table5238
+ GCC_except_table5246
+ GCC_except_table5247
+ GCC_except_table5311
+ GCC_except_table5315
+ GCC_except_table5459
+ GCC_except_table5845
+ GCC_except_table5854
+ GCC_except_table5945
+ GCC_except_table5973
+ GCC_except_table5981
+ GCC_except_table6096
+ GCC_except_table6269
+ GCC_except_table6415
+ GCC_except_table6431
+ GCC_except_table6731
+ GCC_except_table6770
+ GCC_except_table6843
+ GCC_except_table7022
+ GCC_except_table7027
+ GCC_except_table7166
+ GCC_except_table7243
+ GCC_except_table7387
+ GCC_except_table7644
+ GCC_except_table7742
+ GCC_except_table8144
+ GCC_except_table8235
+ GCC_except_table8286
+ GCC_except_table8357
+ GCC_except_table8401
+ GCC_except_table8783
+ GCC_except_table8826
+ GCC_except_table8891
+ GCC_except_table8897
+ GCC_except_table9100
+ GCC_except_table9140
+ GCC_except_table9164
+ GCC_except_table9229
+ GCC_except_table9358
+ GCC_except_table9362
+ GCC_except_table9488
+ GCC_except_table9495
+ GCC_except_table9501
+ GCC_except_table9505
+ GCC_except_table9508
+ GCC_except_table9513
+ GCC_except_table9523
+ GCC_except_table9526
+ GCC_except_table9540
+ GCC_except_table9546
+ GCC_except_table9549
+ GCC_except_table9552
+ GCC_except_table9554
+ GCC_except_table9760
+ GCC_except_table9768
+ GCC_except_table9843
+ GCC_except_table9846
+ GCC_except_table9941
+ GCC_except_table9979
+ GCC_except_table9994
+ GCC_except_table9999
+ _OBJC_CLASS_$_CNUserDefaults
+ _OBJC_IVAR_$_CNCardSharedProfileCellView._cachedShouldHideSharedProfileMenu
+ _OBJC_IVAR_$_CNContactContentUnitaryViewController._cardEditingFamilySharingGroup
+ _OBJC_IVAR_$_CNContactContentUnitaryViewController._meCardAvatarEditingSourceContact
+ _OBJC_IVAR_$_CNContactInlineActionsViewController._actionsControllersByType
+ _OBJC_IVAR_$_CNContactInlineActionsViewController._actionsControllersContact
+ _OBJC_IVAR_$_CNContactListBannerView._footnoteContainerLeadingConstraint
+ _OBJC_IVAR_$_CNContactListBannerView._titleLabelLeadingConstraint
+ _OBJC_IVAR_$_CNContactListDeleteContactsAction._confirmationDismissalHandler
+ _OBJC_IVAR_$_CNContactListDeleteContactsAction._groupNameForRemovalOption
+ _OBJC_IVAR_$_CNContactListDeleteContactsAction._removeFromGroupHandler
+ __OBJC_$_INSTANCE_METHODS_UINavigationBar(ContactsUI|CNContactStyle|CNUI)
+ __OBJC_$_INSTANCE_METHODS_UIView(ContactsUI|ContactsUI1|CNGroupIdentityHeaderViewController|CNSensitiveContentBlurView|CNContactStyle|ABDebugging|CNDirectionalSafeArea)
+ __OBJC_CLASS_PROTOCOLS_$_UIView(ContactsUI|ContactsUI1|CNGroupIdentityHeaderViewController|CNSensitiveContentBlurView|CNContactStyle|ABDebugging|CNDirectionalSafeArea)
+ ___287+[CNContactListViewController layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:listAppearance:safeAreaInsets:collectionViewIsShowingIndexBar:contentUnavailable:]_block_invoke
+ ___355+[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:safeAreaInsets:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]_block_invoke
+ ___355+[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:safeAreaInsets:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]_block_invoke_2
+ ___49-[CNContact(UIAdditions) persistedLinkedContacts]_block_invoke
+ ___50-[CNContactListDeleteContactsAction performAction]_block_invoke_3
+ ___51+[CNContactListViewController collectionViewLayout]_block_invoke_8
+ ___51-[CNContactListViewController createCollectionView]_block_invoke_8
+ ___58-[CNPhotosPosterConfigurationReader copyVisibleFrameImage]_block_invoke
+ ___60-[CNContactListActionHelper canShowDeleteActionForContacts:]_block_invoke
+ ___75-[CNContactListStyleApplier applyContactListStyleToHeaderFooter:withTitle:]_block_invoke
+ ___77-[CNContactListActionHelper trailingSwipeActionsForContact:dataSourceFilter:]_block_invoke_2
+ ___85-[CNContactListActionHelper deleteContacts:offeringRemovalFromList:dismissalHandler:]_block_invoke
+ ___86-[CNUIAfterCACommitScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___87-[CNContactListStyleApplier applySearchExcerptToContentConfiguration:withSubtitleText:]_block_invoke
+ ___block_descriptor_121_e8_32s40bs48bs56bs64bs72bs80bs88bs96bs104bs_e71_"NSCollectionLayoutSection"24?0q8"<NSCollectionLayoutEnvironment>"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___unnamed_17
+ _associated conformance 10ContactsUI30ScrollRevealThresholdEvaluatorV0C6ActionOSHAASQ
+ _copyVisibleFrameImage.context
+ _copyVisibleFrameImage.onceToken
+ _descriptorForRequiredKeys.cn_once_object_23
+ _descriptorForRequiredKeys.cn_once_object_6
+ _descriptorForRequiredKeys.cn_once_token_23
+ _descriptorForRequiredKeys.cn_once_token_6
+ _descriptorForRequiredKeysWithDescription:.cn_once_object_15
+ _descriptorForRequiredKeysWithDescription:.cn_once_token_15
+ _getPISegmentationLoaderClass
+ _log.cn_once_object_23
+ _log.cn_once_object_24
+ _log.cn_once_object_5
+ _log.cn_once_token_23
+ _log.cn_once_token_24
+ _log.cn_once_token_5
+ _objc_msgSend$_installScrollPocketBarInteractionIfNeeded
+ _objc_msgSend$_setEdgeVisibility:
+ _objc_msgSend$actionsControllerForType:
+ _objc_msgSend$actionsControllersByType
+ _objc_msgSend$actionsControllersContact
+ _objc_msgSend$afterDelay:performBlock:delayTolerance:qualityOfService:
+ _objc_msgSend$allowsFullSwipeToDeleteContact:
+ _objc_msgSend$applyContactListDirectionalLayoutMargins:toLayoutSection:listAppearance:safeAreaInsets:collectionViewIsShowingIndexBar:
+ _objc_msgSend$applyContactListStyleToHeaderFooter:withTitle:
+ _objc_msgSend$applySearchExcerptToContentConfiguration:withSubtitleText:
+ _objc_msgSend$avatarEditingSourceContactForHeaderView:
+ _objc_msgSend$avatarLeadingLayoutMarginForListAppearance:
+ _objc_msgSend$boundsForImageSize:normalizedVisibleRect:
+ _objc_msgSend$cachedShouldHideSharedProfileMenu
+ _objc_msgSend$canShowDeleteActionForContacts:
+ _objc_msgSend$cardEditingFamilySharingGroup
+ _objc_msgSend$cnui_directionalSafeAreaInsets
+ _objc_msgSend$cnui_setScrollPocketContributionSuppressed:
+ _objc_msgSend$collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:safeAreaInsets:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:
+ _objc_msgSend$configurationState
+ _objc_msgSend$confirmationDismissalHandler
+ _objc_msgSend$contactForVisualIdentityEditingFromContact:
+ _objc_msgSend$copyFullExtentPreviewImage
+ _objc_msgSend$deleteContacts:offeringRemovalFromList:dismissalHandler:
+ _objc_msgSend$editConfiguration
+ _objc_msgSend$extent
+ _objc_msgSend$finishConfirmationWithOutcome:
+ _objc_msgSend$groupNameForRemovalOption
+ _objc_msgSend$hardStyle
+ _objc_msgSend$imageFromMetadata:size:minimumHorizontalMargin:completionHandler:
+ _objc_msgSend$imageWithCVPixelBuffer:
+ _objc_msgSend$interactions
+ _objc_msgSend$invalidateActionsControllersIfNeeded
+ _objc_msgSend$labelsLeadingInset
+ _objc_msgSend$layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:listAppearance:safeAreaInsets:collectionViewIsShowingIndexBar:contentUnavailable:
+ _objc_msgSend$makeActionsControllerForActionType:
+ _objc_msgSend$meCardAvatarEditingSourceContact
+ _objc_msgSend$normalizedFaceRect
+ _objc_msgSend$normalizedVisibleFrame
+ _objc_msgSend$normalizedVisibleRect
+ _objc_msgSend$offersRemoveFromGroup
+ _objc_msgSend$persistedLinkedContacts
+ _objc_msgSend$removeFromGroupHandler
+ _objc_msgSend$renderedBasicMonogramForContact:scope:prohibitedSources:
+ _objc_msgSend$selectionLeadingInsetForListAppearance:
+ _objc_msgSend$selectionTrailingInsetForListAppearance:
+ _objc_msgSend$setActionsControllersContact:
+ _objc_msgSend$setCachedShouldHideSharedProfileMenu:
+ _objc_msgSend$setConfirmationDismissalHandler:
+ _objc_msgSend$setGroupNameForRemovalOption:
+ _objc_msgSend$setMeCardAvatarEditingSourceContact:
+ _objc_msgSend$setRemoveFromGroupHandler:
+ _objc_msgSend$setTextToSecondaryTextVerticalPadding:
+ _objc_msgSend$shouldHideSharedProfileMenu
+ _objc_msgSend$shouldHideSharedProfileMenuInContacts
+ _objc_msgSend$shouldPresentDisambiguationUIForActionType:
+ _objc_msgSend$standardPreferences
+ _objc_msgSend$subtitleNumberOfLinesForAccessibilityContentSizeCategory:
+ _objc_msgSend$updateAvatarLeadingConstraint
+ _objc_msgSend$updateLabelsLeadingInset
+ _objc_msgSend$userHasOptedInToPreference:
+ _symbolic ScM
+ _symbolic _____ 10ContactsUI30ScrollRevealThresholdEvaluatorV
+ _symbolic _____ 10ContactsUI30ScrollRevealThresholdEvaluatorV0C6ActionO
+ _symbolic _____Sg 12FindMyLocate12ClientTargetV
+ _type_layout_string 10ContactsUI30ScrollRevealThresholdEvaluatorV
- +[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]
- +[CNContactListViewController layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:collectionViewIsShowingIndexBar:contentUnavailable:]
- -[CNContactContentUnitaryViewController actionsControllerByType]
- -[CNContactContentUnitaryViewController didSelectActionItem:actionType:]
- -[CNContactContentUnitaryViewController setActionsControllerByType:]
- -[CNContactListStyleApplier applyContactListDirectionalLayoutMargins:toLayoutSection:collectionViewIsShowingIndexBar:]
- -[CNContactListStyleApplier applyContactListStyleToHeaderFooter:withTitle:isRTL:listAppearance:superviewDirectionalLayoutMargins:]
- -[CNContactListStyleApplier applySubtitleTextColorsToSearchCellContentConfiguration:withSubtitleText:forSelectedState:]
- -[CNContactListStyleDefaultProvider cellBlueSelectionSecondaryTextColor]
- -[CNContactListStyleDefaultProvider meBannerAvatarLeadingInsetForListAppearance:]
- -[CNContactListStyleDefaultProvider sectionHeaderFooterLeadingLayoutMargin]
- -[CNContactListStyleWrapperProvider cellBlueSelectionSecondaryTextColor]
- GCC_except_table10136
- GCC_except_table10142
- GCC_except_table10364
- GCC_except_table10565
- GCC_except_table10579
- GCC_except_table10593
- GCC_except_table10849
- GCC_except_table10851
- GCC_except_table10920
- GCC_except_table10921
- GCC_except_table10922
- GCC_except_table10937
- GCC_except_table11219
- GCC_except_table11225
- GCC_except_table11277
- GCC_except_table11281
- GCC_except_table11486
- GCC_except_table11673
- GCC_except_table11678
- GCC_except_table11681
- GCC_except_table11691
- GCC_except_table11693
- GCC_except_table11694
- GCC_except_table11704
- GCC_except_table11718
- GCC_except_table11738
- GCC_except_table11801
- GCC_except_table11913
- GCC_except_table12007
- GCC_except_table12034
- GCC_except_table12153
- GCC_except_table12215
- GCC_except_table12277
- GCC_except_table12278
- GCC_except_table12288
- GCC_except_table12289
- GCC_except_table12716
- GCC_except_table12733
- GCC_except_table13054
- GCC_except_table13088
- GCC_except_table13191
- GCC_except_table13388
- GCC_except_table13456
- GCC_except_table13462
- GCC_except_table13536
- GCC_except_table13537
- GCC_except_table13545
- GCC_except_table13625
- GCC_except_table13630
- GCC_except_table13803
- GCC_except_table13822
- GCC_except_table13971
- GCC_except_table14000
- GCC_except_table14001
- GCC_except_table14135
- GCC_except_table14222
- GCC_except_table14229
- GCC_except_table14266
- GCC_except_table14522
- GCC_except_table14525
- GCC_except_table14631
- GCC_except_table14650
- GCC_except_table14917
- GCC_except_table14992
- GCC_except_table15113
- GCC_except_table15117
- GCC_except_table15191
- GCC_except_table15257
- GCC_except_table15265
- GCC_except_table15267
- GCC_except_table15271
- GCC_except_table15290
- GCC_except_table15292
- GCC_except_table15461
- GCC_except_table15562
- GCC_except_table15642
- GCC_except_table15646
- GCC_except_table15664
- GCC_except_table15714
- GCC_except_table15837
- GCC_except_table16143
- GCC_except_table16158
- GCC_except_table16174
- GCC_except_table16187
- GCC_except_table16188
- GCC_except_table16192
- GCC_except_table16193
- GCC_except_table16213
- GCC_except_table16289
- GCC_except_table16678
- GCC_except_table16680
- GCC_except_table16689
- GCC_except_table16784
- GCC_except_table16847
- GCC_except_table17017
- GCC_except_table17298
- GCC_except_table17302
- GCC_except_table17782
- GCC_except_table17800
- GCC_except_table17852
- GCC_except_table17862
- GCC_except_table17870
- GCC_except_table17891
- GCC_except_table17908
- GCC_except_table17928
- GCC_except_table17950
- GCC_except_table17964
- GCC_except_table17967
- GCC_except_table17969
- GCC_except_table17976
- GCC_except_table17977
- GCC_except_table18004
- GCC_except_table18131
- GCC_except_table18141
- GCC_except_table18157
- GCC_except_table18161
- GCC_except_table18165
- GCC_except_table18167
- GCC_except_table18213
- GCC_except_table18311
- GCC_except_table18425
- GCC_except_table18482
- GCC_except_table18483
- GCC_except_table18490
- GCC_except_table18495
- GCC_except_table18500
- GCC_except_table18509
- GCC_except_table18512
- GCC_except_table18537
- GCC_except_table18545
- GCC_except_table18559
- GCC_except_table18577
- GCC_except_table18578
- GCC_except_table18589
- GCC_except_table18597
- GCC_except_table18600
- GCC_except_table18602
- GCC_except_table18604
- GCC_except_table18617
- GCC_except_table18758
- GCC_except_table2890
- GCC_except_table2956
- GCC_except_table3034
- GCC_except_table3035
- GCC_except_table3036
- GCC_except_table3151
- GCC_except_table3281
- GCC_except_table3453
- GCC_except_table3455
- GCC_except_table3588
- GCC_except_table3590
- GCC_except_table3668
- GCC_except_table3787
- GCC_except_table4004
- GCC_except_table4005
- GCC_except_table4176
- GCC_except_table4218
- GCC_except_table4252
- GCC_except_table4372
- GCC_except_table4462
- GCC_except_table4736
- GCC_except_table4740
- GCC_except_table4811
- GCC_except_table4821
- GCC_except_table4984
- GCC_except_table5025
- GCC_except_table5099
- GCC_except_table5100
- GCC_except_table5106
- GCC_except_table5108
- GCC_except_table5163
- GCC_except_table5183
- GCC_except_table5224
- GCC_except_table5231
- GCC_except_table5232
- GCC_except_table5296
- GCC_except_table5300
- GCC_except_table5444
- GCC_except_table5821
- GCC_except_table5830
- GCC_except_table5921
- GCC_except_table5949
- GCC_except_table5957
- GCC_except_table6072
- GCC_except_table6245
- GCC_except_table6391
- GCC_except_table6407
- GCC_except_table6707
- GCC_except_table6746
- GCC_except_table6819
- GCC_except_table6998
- GCC_except_table7003
- GCC_except_table7134
- GCC_except_table7210
- GCC_except_table7354
- GCC_except_table7611
- GCC_except_table7709
- GCC_except_table8110
- GCC_except_table8167
- GCC_except_table8252
- GCC_except_table8323
- GCC_except_table8367
- GCC_except_table8748
- GCC_except_table8791
- GCC_except_table8856
- GCC_except_table8862
- GCC_except_table9030
- GCC_except_table9105
- GCC_except_table9129
- GCC_except_table9194
- GCC_except_table9321
- GCC_except_table9325
- GCC_except_table9451
- GCC_except_table9452
- GCC_except_table9458
- GCC_except_table9464
- GCC_except_table9468
- GCC_except_table9471
- GCC_except_table9476
- GCC_except_table9486
- GCC_except_table9503
- GCC_except_table9509
- GCC_except_table9512
- GCC_except_table9515
- GCC_except_table9517
- GCC_except_table9723
- GCC_except_table9731
- GCC_except_table9806
- GCC_except_table9809
- GCC_except_table9904
- GCC_except_table9942
- GCC_except_table9957
- GCC_except_table9962
- _OBJC_IVAR_$_CNContactContentUnitaryViewController._actionsControllerByType
- __OBJC_$_INSTANCE_METHODS_UINavigationBar(ContactsUI|CNContactStyle)
- __OBJC_$_INSTANCE_METHODS_UIView(ContactsUI|ContactsUI1|CNGroupIdentityHeaderViewController|CNSensitiveContentBlurView|CNContactStyle|ABDebugging)
- __OBJC_CLASS_PROTOCOLS_$_UIView(ContactsUI|ContactsUI1|CNGroupIdentityHeaderViewController|CNSensitiveContentBlurView|CNContactStyle|ABDebugging)
- ___119-[CNContactListStyleApplier applySubtitleTextColorsToSearchCellContentConfiguration:withSubtitleText:forSelectedState:]_block_invoke
- ___130-[CNContactListStyleApplier applyContactListStyleToHeaderFooter:withTitle:isRTL:listAppearance:superviewDirectionalLayoutMargins:]_block_invoke
- ___257+[CNContactListViewController layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:collectionViewIsShowingIndexBar:contentUnavailable:]_block_invoke
- ___340+[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]_block_invoke
- ___340+[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]_block_invoke_2
- ___48-[CNContactListActionHelper canShowDeleteAction]_block_invoke
- ___block_descriptor_113_e8_32s40bs48bs56bs64bs72bs80bs88bs96bs_e71_"NSCollectionLayoutSection"24?0q8"<NSCollectionLayoutEnvironment>"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___unnamed_8
- _descriptorForRequiredKeys.cn_once_object_21
- _descriptorForRequiredKeys.cn_once_token_21
- _log.cn_once_object_21
- _log.cn_once_object_22
- _log.cn_once_object_3
- _log.cn_once_token_21
- _log.cn_once_token_22
- _log.cn_once_token_3
- _objc_msgSend$actionsControllerByType
- _objc_msgSend$applyContactListDirectionalLayoutMargins:toLayoutSection:collectionViewIsShowingIndexBar:
- _objc_msgSend$applyContactListStyleToHeaderFooter:withTitle:isRTL:listAppearance:superviewDirectionalLayoutMargins:
- _objc_msgSend$applySubtitleTextColorsToSearchCellContentConfiguration:withSubtitleText:forSelectedState:
- _objc_msgSend$blueSelectionSecondaryTextColor
- _objc_msgSend$cellBlueSelectionSecondaryTextColor
- _objc_msgSend$cellSearchResultTextDisabledColor
- _objc_msgSend$collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:
- _objc_msgSend$contactListBannerFootnoteFontPrimary
- _objc_msgSend$contactListBannerFootnoteFontSecondary
- _objc_msgSend$contactListBannerFootnoteTextColorPrimary
- _objc_msgSend$contactListBannerFootnoteTextColorSecondary
- _objc_msgSend$contactListBannerTitleFontPrimary
- _objc_msgSend$downtimeWhitelistUIEnabled
- _objc_msgSend$imageFromMetadata:size:completionHandler:
- _objc_msgSend$layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:collectionViewIsShowingIndexBar:contentUnavailable:
- _objc_msgSend$meBannerAvatarLeadingInsetForListAppearance:
- _objc_msgSend$metricsForTextStyle:
- _objc_msgSend$secondaryAttributedText
- _objc_msgSend$sectionHeaderFooterLeadingLayoutMargin
- _objc_msgSend$setActionsControllerByType:
- _objc_msgSend$softStyle
- _objc_msgSend$tableCellDefaultSelectionTintColor
CStrings:
+ "CARD_ACTION_DELETE_MESSAGE"
+ "CNContactsButtonAlwaysShowUndeterminedContactsAccessUI"
+ "Could not load the minimum layer stack at %@: %@"
+ "Could not render the background layer at %@ to an image"
+ "Edit configuration carries no usable normalizedVisibleFrame"
+ "Failed to look up displayed group for delete confirmation: %@"
+ "LIST_ACTION_DELETE_CARD_OR_FROM_GROUP"
+ "Minimum layer stack at %@ carries no background pixel buffer"
+ "No edit configuration, so the crop cannot be bounded to the user's visible frame"
+ "Photos poster config at %@ carries no media"
+ "Region entry was not a rect dictionary"
+ "V:|[avatarView(avatarSize)]|"
+ "[CNContactContentViewController] Could not produce a cropped avatar for Shared Name & Photo, falling back to the un-cropped image"
+ "[CNUINavigationListItem+CNContactProperty] Phone number has nil formattedStringValue, falling back to stringValue"
+ "[Likeness Update] Seeding visual identity editor with the me card's own image and cropRect %{public}@ instead of the displayed shared profile avatar"
+ "_UIScrollPocketBarInteraction"
- "CNUINavigationListItem+CNContactProperty.m"
- "V:|-(verticalMargin)-[avatarView(avatarSize)]-(verticalMargin)-|"
- "Value is not a string, not supported"
```
