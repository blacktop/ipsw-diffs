## ContactsUI

> `/System/iOSSupport/System/Library/Frameworks/ContactsUI.framework/Versions/A/ContactsUI`

```diff

-1461.100.1.0.0
-  __TEXT.__text: 0x2819e4
-  __TEXT.__objc_methlist: 0x3222c
+1463.200.41.0.0
+  __TEXT.__text: 0x283254
+  __TEXT.__objc_methlist: 0x3241c
   __TEXT.__dlopen_cstrs: 0xcf4
   __TEXT.__const: 0x5f28
   __TEXT.__constg_swiftt: 0x22f0
-  __TEXT.__swift5_typeref: 0x573e
+  __TEXT.__swift5_typeref: 0x5746
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_reflstr: 0x1b6f
   __TEXT.__swift5_fieldmd: 0x19e0
   __TEXT.__swift5_assocty: 0x768
   __TEXT.__swift5_proto: 0x270
   __TEXT.__swift5_types: 0x1d0
-  __TEXT.__cstring: 0xed26
-  __TEXT.__oslogstring: 0x7dbf
+  __TEXT.__cstring: 0xed4c
+  __TEXT.__oslogstring: 0x7ef1
   __TEXT.__swift5_capture: 0x90c
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_cont: 0xb8
   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x27b4
+  __TEXT.__gcc_except_tab: 0x27d0
   __TEXT.__ustring: 0x79a
-  __TEXT.__unwind_info: 0xce38
+  __TEXT.__unwind_info: 0xcea0
   __TEXT.__eh_frame: 0x10c4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x56f8
+  __DATA_CONST.__const: 0x5748
   __DATA_CONST.__objc_classlist: 0x1358
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x7d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x154c8
+  __DATA_CONST.__objc_selrefs: 0x15620
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0xd30
   __DATA_CONST.__objc_arraydata: 0x508
   __DATA_CONST.__got: 0x2360
-  __AUTH_CONST.__const: 0x6550
-  __AUTH_CONST.__cfstring: 0x9d20
-  __AUTH_CONST.__objc_const: 0x4cd00
+  __AUTH_CONST.__const: 0x6570
+  __AUTH_CONST.__cfstring: 0x9d40
+  __AUTH_CONST.__objc_const: 0x4cea0
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2028
+  __AUTH_CONST.__auth_got: 0x2030
   __AUTH.__objc_data: 0xaa30
   __AUTH.__data: 0x1738
-  __DATA.__objc_ivar: 0x3648
-  __DATA.__data: 0x7670
+  __DATA.__objc_ivar: 0x366c
+  __DATA.__data: 0x7690
   __DATA.__common: 0x230
   __DATA_DIRTY.__objc_data: 0x2508
   __DATA_DIRTY.__data: 0x238

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19186
-  Symbols:   38042
-  CStrings:  2456
+  Functions: 19234
+  Symbols:   38129
+  CStrings:  2461
 
Symbols:
+ +[CNContactListStyleApplier subtitleNumberOfLinesForAccessibilityContentSizeCategory:]
+ +[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:safeAreaInsets:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]
+ +[CNContactListViewController layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:listAppearance:safeAreaInsets:collectionViewIsShowingIndexBar:contentUnavailable:]
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
+ -[CNUIAfterCACommitScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]
+ -[UINavigationBar(CNUI) cnui_setScrollPocketContributionSuppressed:]
+ -[UIView(CNDirectionalSafeArea) cnui_directionalSafeAreaInsets]
+ GCC_except_table10005
+ GCC_except_table10011
+ GCC_except_table10064
+ GCC_except_table10265
+ GCC_except_table10439
+ GCC_except_table10459
+ GCC_except_table10464
+ GCC_except_table10679
+ GCC_except_table10706
+ GCC_except_table10825
+ GCC_except_table10887
+ GCC_except_table10949
+ GCC_except_table10950
+ GCC_except_table10960
+ GCC_except_table10961
+ GCC_except_table11361
+ GCC_except_table11627
+ GCC_except_table11883
+ GCC_except_table11951
+ GCC_except_table11956
+ GCC_except_table12008
+ GCC_except_table12222
+ GCC_except_table12241
+ GCC_except_table12390
+ GCC_except_table12782
+ GCC_except_table12785
+ GCC_except_table12891
+ GCC_except_table12910
+ GCC_except_table13177
+ GCC_except_table13334
+ GCC_except_table13338
+ GCC_except_table13412
+ GCC_except_table13478
+ GCC_except_table13486
+ GCC_except_table13488
+ GCC_except_table13492
+ GCC_except_table13511
+ GCC_except_table13513
+ GCC_except_table13673
+ GCC_except_table13804
+ GCC_except_table13808
+ GCC_except_table13868
+ GCC_except_table13901
+ GCC_except_table14223
+ GCC_except_table14236
+ GCC_except_table14237
+ GCC_except_table14241
+ GCC_except_table14242
+ GCC_except_table14262
+ GCC_except_table14337
+ GCC_except_table14647
+ GCC_except_table14649
+ GCC_except_table14658
+ GCC_except_table14753
+ GCC_except_table14816
+ GCC_except_table14840
+ GCC_except_table15248
+ GCC_except_table15252
+ GCC_except_table15728
+ GCC_except_table15778
+ GCC_except_table15792
+ GCC_except_table15813
+ GCC_except_table15830
+ GCC_except_table15850
+ GCC_except_table15872
+ GCC_except_table15889
+ GCC_except_table15891
+ GCC_except_table15898
+ GCC_except_table15899
+ GCC_except_table15926
+ GCC_except_table16049
+ GCC_except_table16059
+ GCC_except_table16075
+ GCC_except_table16079
+ GCC_except_table16083
+ GCC_except_table16085
+ GCC_except_table16131
+ GCC_except_table16225
+ GCC_except_table16337
+ GCC_except_table16521
+ GCC_except_table16577
+ GCC_except_table2733
+ GCC_except_table2802
+ GCC_except_table2880
+ GCC_except_table2881
+ GCC_except_table2882
+ GCC_except_table3577
+ GCC_except_table3578
+ GCC_except_table3746
+ GCC_except_table3788
+ GCC_except_table3822
+ GCC_except_table3939
+ GCC_except_table4013
+ GCC_except_table4290
+ GCC_except_table4494
+ GCC_except_table4535
+ GCC_except_table4604
+ GCC_except_table4605
+ GCC_except_table4611
+ GCC_except_table4613
+ GCC_except_table4668
+ GCC_except_table4688
+ GCC_except_table4729
+ GCC_except_table4737
+ GCC_except_table4738
+ GCC_except_table4800
+ GCC_except_table4804
+ GCC_except_table4943
+ GCC_except_table5308
+ GCC_except_table5317
+ GCC_except_table5406
+ GCC_except_table5434
+ GCC_except_table5442
+ GCC_except_table5557
+ GCC_except_table5800
+ GCC_except_table5816
+ GCC_except_table6125
+ GCC_except_table6198
+ GCC_except_table6369
+ GCC_except_table6374
+ GCC_except_table6513
+ GCC_except_table6590
+ GCC_except_table6726
+ GCC_except_table6967
+ GCC_except_table7032
+ GCC_except_table7451
+ GCC_except_table7485
+ GCC_except_table7536
+ GCC_except_table7607
+ GCC_except_table7651
+ GCC_except_table8059
+ GCC_except_table8124
+ GCC_except_table8130
+ GCC_except_table8224
+ GCC_except_table8264
+ GCC_except_table8288
+ GCC_except_table8335
+ GCC_except_table8766
+ GCC_except_table8774
+ GCC_except_table8843
+ GCC_except_table8846
+ GCC_except_table8941
+ GCC_except_table8981
+ GCC_except_table8997
+ GCC_except_table9002
+ GCC_except_table9037
+ GCC_except_table9115
+ GCC_except_table9121
+ GCC_except_table9212
+ GCC_except_table9335
+ GCC_except_table9779
+ GCC_except_table9780
+ GCC_except_table9781
+ OBJC_IVAR_$_CNCardSharedProfileCellView._cachedShouldHideSharedProfileMenu
+ OBJC_IVAR_$_CNContactContentUnitaryViewController._cardEditingFamilySharingGroup
+ OBJC_IVAR_$_CNContactContentUnitaryViewController._meCardAvatarEditingSourceContact
+ OBJC_IVAR_$_CNContactInlineActionsViewController._actionsControllersByType
+ OBJC_IVAR_$_CNContactInlineActionsViewController._actionsControllersContact
+ OBJC_IVAR_$_CNContactListBannerView._footnoteContainerLeadingConstraint
+ OBJC_IVAR_$_CNContactListBannerView._titleLabelLeadingConstraint
+ OBJC_IVAR_$_CNContactListDeleteContactsAction._confirmationDismissalHandler
+ OBJC_IVAR_$_CNContactListDeleteContactsAction._groupNameForRemovalOption
+ OBJC_IVAR_$_CNContactListDeleteContactsAction._removeFromGroupHandler
+ _OBJC_CLASS_$_CNUserDefaults
+ __OBJC_$_INSTANCE_METHODS_UINavigationBar(CNContactStyle|CNUI)
+ __OBJC_$_INSTANCE_METHODS_UIView(ContactsUI|CNGroupIdentityHeaderViewController|CNSensitiveContentBlurView|CNContactStyle|ABDebugging|CNDirectionalSafeArea)
+ ___287+[CNContactListViewController layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:listAppearance:safeAreaInsets:collectionViewIsShowingIndexBar:contentUnavailable:]_block_invoke
+ ___355+[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:safeAreaInsets:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]_block_invoke
+ ___355+[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:safeAreaInsets:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]_block_invoke_2
+ ___49-[CNContact(UIAdditions) persistedLinkedContacts]_block_invoke
+ ___50-[CNContactListDeleteContactsAction performAction]_block_invoke_3
+ ___51+[CNContactListViewController collectionViewLayout]_block_invoke_8
+ ___51-[CNContactListViewController createCollectionView]_block_invoke_8
+ ___60-[CNContactListActionHelper canShowDeleteActionForContacts:]_block_invoke
+ ___75-[CNContactListStyleApplier applyContactListStyleToHeaderFooter:withTitle:]_block_invoke
+ ___77-[CNContactListActionHelper trailingSwipeActionsForContact:dataSourceFilter:]_block_invoke_2
+ ___85-[CNContactListActionHelper deleteContacts:offeringRemovalFromList:dismissalHandler:]_block_invoke
+ ___86-[CNUIAfterCACommitScheduler afterDelay:performBlock:delayTolerance:qualityOfService:]_block_invoke
+ ___87-[CNContactListStyleApplier applySearchExcerptToContentConfiguration:withSubtitleText:]_block_invoke
+ ___block_descriptor_121_e8_32s40bs48bs56bs64bs72bs80bs88bs96bs104bs_e71_"NSCollectionLayoutSection"24?0q8"<NSCollectionLayoutEnvironment>"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_56_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
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
+ _objc_msgSend$avatarLeadingLayoutMarginForListAppearance:
+ _objc_msgSend$cachedShouldHideSharedProfileMenu
+ _objc_msgSend$canShowDeleteActionForContacts:
+ _objc_msgSend$cardEditingFamilySharingGroup
+ _objc_msgSend$cnui_directionalSafeAreaInsets
+ _objc_msgSend$cnui_setScrollPocketContributionSuppressed:
+ _objc_msgSend$collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:safeAreaInsets:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:
+ _objc_msgSend$configurationState
+ _objc_msgSend$confirmationDismissalHandler
+ _objc_msgSend$deleteContacts:offeringRemovalFromList:dismissalHandler:
+ _objc_msgSend$finishConfirmationWithOutcome:
+ _objc_msgSend$groupNameForRemovalOption
+ _objc_msgSend$hardStyle
+ _objc_msgSend$interactions
+ _objc_msgSend$invalidateActionsControllersIfNeeded
+ _objc_msgSend$labelsLeadingInset
+ _objc_msgSend$layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:listAppearance:safeAreaInsets:collectionViewIsShowingIndexBar:contentUnavailable:
+ _objc_msgSend$makeActionsControllerForActionType:
+ _objc_msgSend$meCardAvatarEditingSourceContact
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
+ _symbolic _____Sg 12FindMyLocate12ClientTargetV
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
- GCC_except_table10035
- GCC_except_table10236
- GCC_except_table10410
- GCC_except_table10430
- GCC_except_table10435
- GCC_except_table10649
- GCC_except_table10676
- GCC_except_table10795
- GCC_except_table10857
- GCC_except_table10919
- GCC_except_table10920
- GCC_except_table10930
- GCC_except_table10931
- GCC_except_table11331
- GCC_except_table11597
- GCC_except_table11853
- GCC_except_table11921
- GCC_except_table11926
- GCC_except_table11978
- GCC_except_table12192
- GCC_except_table12211
- GCC_except_table12360
- GCC_except_table12753
- GCC_except_table12756
- GCC_except_table12862
- GCC_except_table12881
- GCC_except_table13148
- GCC_except_table13305
- GCC_except_table13309
- GCC_except_table13383
- GCC_except_table13449
- GCC_except_table13457
- GCC_except_table13459
- GCC_except_table13463
- GCC_except_table13482
- GCC_except_table13484
- GCC_except_table13644
- GCC_except_table13775
- GCC_except_table13779
- GCC_except_table13839
- GCC_except_table13872
- GCC_except_table14177
- GCC_except_table14193
- GCC_except_table14206
- GCC_except_table14211
- GCC_except_table14212
- GCC_except_table14232
- GCC_except_table14307
- GCC_except_table14617
- GCC_except_table14619
- GCC_except_table14628
- GCC_except_table14723
- GCC_except_table14786
- GCC_except_table14810
- GCC_except_table15212
- GCC_except_table15216
- GCC_except_table15688
- GCC_except_table15738
- GCC_except_table15752
- GCC_except_table15773
- GCC_except_table15790
- GCC_except_table15810
- GCC_except_table15832
- GCC_except_table15846
- GCC_except_table15849
- GCC_except_table15851
- GCC_except_table15858
- GCC_except_table15859
- GCC_except_table16008
- GCC_except_table16018
- GCC_except_table16034
- GCC_except_table16038
- GCC_except_table16042
- GCC_except_table16044
- GCC_except_table16090
- GCC_except_table16184
- GCC_except_table16296
- GCC_except_table16480
- GCC_except_table2732
- GCC_except_table2798
- GCC_except_table2876
- GCC_except_table2877
- GCC_except_table2878
- GCC_except_table3573
- GCC_except_table3574
- GCC_except_table3742
- GCC_except_table3784
- GCC_except_table3818
- GCC_except_table3935
- GCC_except_table4009
- GCC_except_table4282
- GCC_except_table4490
- GCC_except_table4531
- GCC_except_table4600
- GCC_except_table4601
- GCC_except_table4607
- GCC_except_table4609
- GCC_except_table4664
- GCC_except_table4684
- GCC_except_table4725
- GCC_except_table4732
- GCC_except_table4733
- GCC_except_table4795
- GCC_except_table4799
- GCC_except_table4938
- GCC_except_table5294
- GCC_except_table5303
- GCC_except_table5392
- GCC_except_table5420
- GCC_except_table5428
- GCC_except_table5543
- GCC_except_table5786
- GCC_except_table5802
- GCC_except_table6111
- GCC_except_table6184
- GCC_except_table6355
- GCC_except_table6360
- GCC_except_table6491
- GCC_except_table6567
- GCC_except_table6703
- GCC_except_table6944
- GCC_except_table7009
- GCC_except_table7427
- GCC_except_table7461
- GCC_except_table7512
- GCC_except_table7583
- GCC_except_table7627
- GCC_except_table8034
- GCC_except_table8099
- GCC_except_table8105
- GCC_except_table8199
- GCC_except_table8239
- GCC_except_table8263
- GCC_except_table8310
- GCC_except_table8739
- GCC_except_table8747
- GCC_except_table8816
- GCC_except_table8819
- GCC_except_table8914
- GCC_except_table8954
- GCC_except_table8970
- GCC_except_table8975
- GCC_except_table9010
- GCC_except_table9088
- GCC_except_table9094
- GCC_except_table9185
- GCC_except_table9308
- GCC_except_table9750
- GCC_except_table9751
- GCC_except_table9752
- GCC_except_table9976
- GCC_except_table9982
- OBJC_IVAR_$_CNContactContentUnitaryViewController._actionsControllerByType
- _OBJC_CLASS_$_UIFontMetrics
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UINavigationBar_$_CNContactStyle
- __OBJC_$_INSTANCE_METHODS_UIView(ContactsUI|CNGroupIdentityHeaderViewController|CNSensitiveContentBlurView|CNContactStyle|ABDebugging)
- ___119-[CNContactListStyleApplier applySubtitleTextColorsToSearchCellContentConfiguration:withSubtitleText:forSelectedState:]_block_invoke
- ___130-[CNContactListStyleApplier applyContactListStyleToHeaderFooter:withTitle:isRTL:listAppearance:superviewDirectionalLayoutMargins:]_block_invoke
- ___257+[CNContactListViewController layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:collectionViewIsShowingIndexBar:contentUnavailable:]_block_invoke
- ___340+[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]_block_invoke
- ___340+[CNContactListViewController collectionViewLayoutWithFloatingHeaderViews:contactListStyleApplier:trailingSwipeActionsProvider:shouldDisplaySupplementaryHeaderItemForSection:shouldShowSeparatorsForSection:directionalLayoutMargins:collectionViewIsShowingIndexBar:numberOfItemsInSection:contentUnavailable:collectionViewIsSelectingIndexPath:]_block_invoke_2
- ___48-[CNContactListActionHelper canShowDeleteAction]_block_invoke
- ___block_descriptor_113_e8_32s40bs48bs56bs64bs72bs80bs88bs96bs_e71_"NSCollectionLayoutSection"24?0q8"<NSCollectionLayoutEnvironment>"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
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
- _objc_msgSend$layoutSectionForLayoutConfiguration:layoutEnvironment:section:contactListStyleApplier:shouldDisplaySupplementaryHeaderItemForSection:headerViewsFloat:directionalLayoutMargins:collectionViewIsShowingIndexBar:contentUnavailable:
- _objc_msgSend$meBannerAvatarLeadingInsetForListAppearance:
- _objc_msgSend$metricsForTextStyle:
- _objc_msgSend$scaledFontForFont:
- _objc_msgSend$secondaryAttributedText
- _objc_msgSend$sectionHeaderFooterLeadingLayoutMargin
- _objc_msgSend$setActionsControllerByType:
- _objc_msgSend$softStyle
- _objc_msgSend$tableCellDefaultSelectionTintColor
CStrings:
+ "CARD_ACTION_DELETE_MESSAGE"
+ "CNContactsButtonAlwaysShowUndeterminedContactsAccessUI"
+ "Failed to look up displayed group for delete confirmation: %@"
+ "LIST_ACTION_DELETE_CARD_OR_FROM_GROUP"
+ "V:|[avatarView(avatarSize)]|"
+ "[CNContactContentViewController] Could not produce a cropped avatar for Shared Name & Photo, falling back to the un-cropped image"
+ "[CNUINavigationListItem+CNContactProperty] Phone number has nil formattedStringValue, falling back to stringValue"
+ "_UIScrollPocketBarInteraction"
- "CNUINavigationListItem+CNContactProperty.m"
- "V:|-(verticalMargin)-[avatarView(avatarSize)]-(verticalMargin)-|"
- "Value is not a string, not supported"
```
