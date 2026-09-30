## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2060.60.41.2.3
-  __TEXT.__text: 0xba12c
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_methlist: 0x103bc
-  __TEXT.__const: 0x5c0
-  __TEXT.__gcc_except_tab: 0x2274
-  __TEXT.__oslogstring: 0x6648
-  __TEXT.__cstring: 0x68cb
-  __TEXT.__dlopen_cstrs: 0x9bb
+2084.10.7.2.5
+  __TEXT.__text: 0xc2138
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x10e1c
+  __TEXT.__const: 0x620
+  __TEXT.__gcc_except_tab: 0x2280
+  __TEXT.__oslogstring: 0x690d
+  __TEXT.__cstring: 0x6b4a
+  __TEXT.__dlopen_cstrs: 0x9ba
   __TEXT.__ustring: 0xca
-  __TEXT.__unwind_info: 0x3158
-  __TEXT.__objc_classname: 0x23b7
-  __TEXT.__objc_methname: 0x2b8cc
-  __TEXT.__objc_methtype: 0x7273
-  __TEXT.__objc_stubs: 0x1b300
-  __DATA_CONST.__got: 0xf58
-  __DATA_CONST.__const: 0x27e0
-  __DATA_CONST.__objc_classlist: 0x608
-  __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x3a8
+  __TEXT.__unwind_info: 0x3218
+  __TEXT.__objc_classname: 0x240f
+  __TEXT.__objc_methname: 0x2cbc2
+  __TEXT.__objc_methtype: 0x740b
+  __TEXT.__objc_stubs: 0x1bea0
+  __DATA_CONST.__got: 0xf98
+  __DATA_CONST.__const: 0x2700
+  __DATA_CONST.__objc_classlist: 0x620
+  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x3a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8618
+  __DATA_CONST.__objc_selrefs: 0x8958
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x678
-  __AUTH_CONST.__auth_got: 0x768
-  __AUTH_CONST.__const: 0xfc0
-  __AUTH_CONST.__cfstring: 0x5400
-  __AUTH_CONST.__objc_const: 0x28410
+  __AUTH_CONST.__auth_got: 0x770
+  __AUTH_CONST.__const: 0x1060
+  __AUTH_CONST.__cfstring: 0x5720
+  __AUTH_CONST.__objc_const: 0x29a38
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x20a8
-  __AUTH.__data: 0x138
-  __DATA.__objc_ivar: 0x1358
-  __DATA.__data: 0x2be8
-  __DATA.__bss: 0x7d8
-  __DATA_DIRTY.__objc_data: 0x1ba8
+  __AUTH.__objc_data: 0x2210
+  __AUTH.__data: 0x128
+  __DATA.__objc_ivar: 0x1474
+  __DATA.__data: 0x2b88
+  __DATA.__bss: 0x7c8
+  __DATA_DIRTY.__objc_data: 0x1b30
   __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0x268
+  __DATA_DIRTY.__bss: 0x278
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F8CED89-FBB6-3DA0-AA9B-FA8ED99040D0
-  Functions: 5540
-  Symbols:   19968
-  CStrings:  9298
+  UUID: 74F45909-AC55-35CC-9C01-52316A12C097
+  Functions: 5746
+  Symbols:   20535
+  CStrings:  9535
 
Symbols:
+ +[SHSheetRemoteSceneSettings settingsWithSessionContext:presnetationStyle:hostProcessType:customizationGroups:collaborationOptions:cloudShareRequest:isSLMEnabled:]
+ -[SFShareSheetSlotManager activityViewControllerDidDisappearWithSessionID:]
+ -[SFShareSheetSlotManager activityViewControllerSessionDidEndWithSessionID:testingSnapshot:completionHandler:]
+ -[SFShareSheetSlotManager requestSharedURLForCollaborationRequest:completionHandler:]
+ -[SHSheetContentDataSource actionUserDefaultsActivity]
+ -[SHSheetContentDataSource initWithState:excludeSectionTypes:topActionsMaximumCount:]
+ -[SHSheetContentDataSource initWithState:excludeSectionTypes:topActionsMaximumCount:].cold.1
+ -[SHSheetContentDataSource topActionsMaximumCount]
+ -[SHSheetContentDataSourceChangeRequest setTopActionsMaximumCount:]
+ -[SHSheetContentDataSourceChangeRequest topActionsMaximumCount]
+ -[SHSheetContentDataSourceManager moreActionIdentifier]
+ -[SHSheetContentDataSourceManager setMoreActionIdentifier:]
+ -[SHSheetContentDataSourceState actionIdentifiers]
+ -[SHSheetContentDataSourceState moreActionIdentifier]
+ -[SHSheetContentDataSourceState setActionIdentifiers:]
+ -[SHSheetContentDataSourceState setMoreActionIdentifier:]
+ -[SHSheetContentLayoutContext setShowAllActions:]
+ -[SHSheetContentLayoutContext showAllActions]
+ -[SHSheetContentLayoutProvider _createHorizontalLayoutSectionWithContext:iconWidth:sectionHeight:]
+ -[SHSheetContentLayoutProvider _layoutForTopActionSectionWithContext:]
+ -[SHSheetContentLayoutSpec initWithTraitCollection:tintColor:deviceClass:portraitWindowSize:]
+ -[SHSheetContentLayoutSpec linkViewHeaderInsets]
+ -[SHSheetContentLayoutSpec portraitWindowSize]
+ -[SHSheetContentLayoutSpec sharingAppSectionHeight]
+ -[SHSheetContentLayoutSpec topActionsSectionHeight]
+ -[SHSheetContext setSnapshotHandler:]
+ -[SHSheetContext setTestingReferenceSnapshot:]
+ -[SHSheetContext snapshotHandler]
+ -[SHSheetContext testingReferenceSnapshot]
+ -[SHSheetGroupActivitySharingController directlyCreateActivity]
+ -[SHSheetGroupActivitySharingController directlyCreateActivity].cold.1
+ -[SHSheetGroupActivitySharingController isPossibleToDirectlyCreateActivity]
+ -[SHSheetGroupActivitySharingController prepareForShareSheetSessionWithCompletion:]
+ -[SHSheetInteractor activityViewControllerSessionDidEndWithCompletionHandler:]
+ -[SHSheetInteractor shouldShowProgressForCollaborationPerformer:]
+ -[SHSheetPresenter didUpdateSheetSize]
+ -[SHSheetPresenter isCompactSize]
+ -[SHSheetPresenter isSLMEnabled]
+ -[SHSheetPresenter isSheetResizable]
+ -[SHSheetRemoteScene isSLMEnabled]
+ -[SHSheetRemoteSceneSettings isSLMEnabled]
+ -[SHSheetRemoteSceneSettings setIsSLMEnabled:]
+ -[SHSheetRemoteSceneViewController isCompactSize]
+ -[SHSheetRemoteSceneViewController isResizable]
+ -[SHSheetRemoteSceneViewController isSLMEnabled]
+ -[SHSheetRemoteSceneViewController preferredContentSizeDidChangeForChildContentContainer:]
+ -[SHSheetRemoteSceneViewController scene:didReceiveSizeUpdateAction:]
+ -[SHSheetRemoteSceneViewController setIsCompactSize:]
+ -[SHSheetRemoteSceneViewController setIsResizable:]
+ -[SHSheetRemoteSceneViewController setIsSLMEnabled:]
+ -[SHSheetRouter isVisionIdiom]
+ -[SHSheetServiceManager activityViewControllerSessionDidEndWithCompletionHandler:]
+ -[SHSheetServiceManager requestSharedURLForCollaborationRequest:completionHandler:]
+ -[SHSheetSession _updateTestingSnapshotIfNeededForResolvedItems:activityType:]
+ -[SHSheetSession numberOfVisibleActionActivities].cold.1
+ -[SHSheetSession setShowCollaborationOptions:]
+ -[SHSheetSession setSnapshotHandler:]
+ -[SHSheetSession setTestingReferenceSnapshot:]
+ -[SHSheetSession showCollaborationOptions]
+ -[SHSheetSession snapshotHandler]
+ -[SHSheetSession testingReferenceSnapshot]
+ -[SHSheetSizeUpdateAction initWithSize:isResizable:]
+ -[SHSheetSizeUpdateAction isCompact]
+ -[SHSheetSizeUpdateAction isResizable]
+ -[SHSheetSizeUpdateAction isSLMEnabled]
+ -[SHSheetUIServiceClientContext hostPortraitWindowSize]
+ -[SHSheetUIServiceClientContext sharingStyle]
+ -[SHSheetUIServiceClientContext showCollaborationOptions]
+ -[SHSheetViewModel setShowCollaborationOptions:]
+ -[SHSheetViewModel showCollaborationOptions]
+ -[UIActivity sessionIdentifier]
+ -[UIActivity setSessionIdentifier:]
+ -[UIActivityActionGroupCell needsLeftIconLayout]
+ -[UIActivityActionHorizontalCell .cxx_destruct]
+ -[UIActivityActionHorizontalCell _configureImageViewForPlaceholder:]
+ -[UIActivityActionHorizontalCell _createTitleLabel]
+ -[UIActivityActionHorizontalCell _disableRasterizeInAnimations]
+ -[UIActivityActionHorizontalCell _installSubviewsIfNeeded]
+ -[UIActivityActionHorizontalCell _legacyIconSizeForContentSizeCategory:]
+ -[UIActivityActionHorizontalCell _placeholderString]
+ -[UIActivityActionHorizontalCell _setLayoutSpec:]
+ -[UIActivityActionHorizontalCell _titleLabelFont]
+ -[UIActivityActionHorizontalCell _updateConstraints]
+ -[UIActivityActionHorizontalCell _updateContentTintColor]
+ -[UIActivityActionHorizontalCell _updateDarkening]
+ -[UIActivityActionHorizontalCell _updateImageView]
+ -[UIActivityActionHorizontalCell _updateTitleView]
+ -[UIActivityActionHorizontalCell activityImageView]
+ -[UIActivityActionHorizontalCell activityProxy]
+ -[UIActivityActionHorizontalCell allConstraints]
+ -[UIActivityActionHorizontalCell configureLayoutIfNeeded:]
+ -[UIActivityActionHorizontalCell contentTintColor]
+ -[UIActivityActionHorizontalCell createTargetedPreview]
+ -[UIActivityActionHorizontalCell didInstallSubviews]
+ -[UIActivityActionHorizontalCell identifier]
+ -[UIActivityActionHorizontalCell imageEffectView]
+ -[UIActivityActionHorizontalCell imageSlotID]
+ -[UIActivityActionHorizontalCell imageSlotView]
+ -[UIActivityActionHorizontalCell image]
+ -[UIActivityActionHorizontalCell isDisabled]
+ -[UIActivityActionHorizontalCell isLongPressable]
+ -[UIActivityActionHorizontalCell isPulsing]
+ -[UIActivityActionHorizontalCell labelForPositioning]
+ -[UIActivityActionHorizontalCell largeTextConstraints]
+ -[UIActivityActionHorizontalCell layoutSpec]
+ -[UIActivityActionHorizontalCell prepareForReuse]
+ -[UIActivityActionHorizontalCell regularConstraints]
+ -[UIActivityActionHorizontalCell setActivityImageView:]
+ -[UIActivityActionHorizontalCell setActivityProxy:]
+ -[UIActivityActionHorizontalCell setAllConstraints:]
+ -[UIActivityActionHorizontalCell setContentTintColor:]
+ -[UIActivityActionHorizontalCell setDidInstallSubviews:]
+ -[UIActivityActionHorizontalCell setDisabled:]
+ -[UIActivityActionHorizontalCell setHighlighted:]
+ -[UIActivityActionHorizontalCell setIdentifier:]
+ -[UIActivityActionHorizontalCell setImage:]
+ -[UIActivityActionHorizontalCell setImageEffectView:]
+ -[UIActivityActionHorizontalCell setImageSlotID:]
+ -[UIActivityActionHorizontalCell setImageSlotView:]
+ -[UIActivityActionHorizontalCell setIsPulsing:]
+ -[UIActivityActionHorizontalCell setLabelForPositioning:]
+ -[UIActivityActionHorizontalCell setLargeTextConstraints:]
+ -[UIActivityActionHorizontalCell setLayoutSpec:]
+ -[UIActivityActionHorizontalCell setLongPressable:]
+ -[UIActivityActionHorizontalCell setRegularConstraints:]
+ -[UIActivityActionHorizontalCell setSelected:]
+ -[UIActivityActionHorizontalCell setTitle:]
+ -[UIActivityActionHorizontalCell setTitleLabel:]
+ -[UIActivityActionHorizontalCell setTitleSlotID:]
+ -[UIActivityActionHorizontalCell setTitleSlotView:]
+ -[UIActivityActionHorizontalCell setVibrantLabelView:]
+ -[UIActivityActionHorizontalCell setupConstraints]
+ -[UIActivityActionHorizontalCell titleLabel]
+ -[UIActivityActionHorizontalCell titleSlotID]
+ -[UIActivityActionHorizontalCell titleSlotView]
+ -[UIActivityActionHorizontalCell title]
+ -[UIActivityActionHorizontalCell traitCollectionDidChange:]
+ -[UIActivityActionHorizontalCell vibrantLabelView]
+ -[UIActivityContentContext hostPortraitWindowSize]
+ -[UIActivityContentContext setHostPortraitWindowSize:]
+ -[UIActivityContentContext setSharingStyle:]
+ -[UIActivityContentContext sharingStyle]
+ -[UIActivityContentViewController _addResizeGestureIfNeeded]
+ -[UIActivityContentViewController _configureHorizontalActionCell:itemIdentifier:]
+ -[UIActivityContentViewController _handleResizeGesture:]
+ -[UIActivityContentViewController _isOnlyCompactSize]
+ -[UIActivityContentViewController _isOnlyFullSize]
+ -[UIActivityContentViewController _provideCellForCollectionView:indexPath:itemIdentifier:].cold.2
+ -[UIActivityContentViewController _removeResizeGestureIfNeeded]
+ -[UIActivityContentViewController _resetPanGesture:]
+ -[UIActivityContentViewController _scrollViewForScrollingType:].cold.1
+ -[UIActivityContentViewController _scrollViewForScrollingType:].cold.2
+ -[UIActivityContentViewController _scrollViewForScrollingType:].cold.3
+ -[UIActivityContentViewController _shouldShowCloseButton]
+ -[UIActivityContentViewController _updateBlurBackgroundIfNeeded]
+ -[UIActivityContentViewController _updateContent:]
+ -[UIActivityContentViewController _updatePreferredContentSize]
+ -[UIActivityContentViewController _updateShowAllActions]
+ -[UIActivityContentViewController _wantsResizePanGesture]
+ -[UIActivityContentViewController collectionViewResizeGestureRecognizer]
+ -[UIActivityContentViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[UIActivityContentViewController gestureRecognizerShouldBegin:]
+ -[UIActivityContentViewController headerViewResizeGestureRecognizer]
+ -[UIActivityContentViewController hostPortraitWindowSize]
+ -[UIActivityContentViewController hostSLMEnabled]
+ -[UIActivityContentViewController isCompactSize]
+ -[UIActivityContentViewController isDraggingFromInitialPosition]
+ -[UIActivityContentViewController isResizable]
+ -[UIActivityContentViewController isSLMEnabled]
+ -[UIActivityContentViewController observeValueForKeyPath:ofObject:change:context:]
+ -[UIActivityContentViewController scrollViewDidEndDragging:willDecelerate:]
+ -[UIActivityContentViewController scrollViewWillBeginDragging:]
+ -[UIActivityContentViewController setCollectionViewResizeGestureRecognizer:]
+ -[UIActivityContentViewController setHeaderViewResizeGestureRecognizer:]
+ -[UIActivityContentViewController setHostSLMEnabled:]
+ -[UIActivityContentViewController setIsDraggingFromInitialPosition:]
+ -[UIActivityContentViewController setShowAllActions:]
+ -[UIActivityContentViewController sharingStyle]
+ -[UIActivityContentViewController showAllActions]
+ -[UIActivityContentViewController viewIsAppearing:]
+ -[UIActivityViewController customDetent]
+ -[UIActivityViewController initialPreferredContentHeight]
+ -[UIActivityViewController setCustomDetent:]
+ -[UIActivityViewController setInitialPreferredContentHeight:]
+ -[UIActivityViewController setSnapshotHandler:]
+ -[UIActivityViewController setTestingReferenceSnapshot:]
+ -[UIActivityViewController snapshotHandler]
+ -[UIActivityViewController testingReferenceSnapshot]
+ -[UIActivityViewController viewDidLayoutSubviews]
+ -[UIApplicationExtensionActivity _activityImageUTI]
+ -[UICollaborationSocialActivity .cxx_destruct]
+ -[UICollaborationSocialActivity activityTitle]
+ -[UICollaborationSocialActivity canPerformWithActivityItems:]
+ -[UICollaborationSocialActivity canPerformWithCollaborationItem:activityItems:]
+ -[UICollaborationSocialActivity canPerformWithCollaborationType:isPostShare:]
+ -[UICollaborationSocialActivity collaborationItem]
+ -[UICollaborationSocialActivity isPostShare]
+ -[UICollaborationSocialActivity prepareWithActivityItems:]
+ -[UICollaborationSocialActivity prepareWithActivityItems:].cold.1
+ -[UICollaborationSocialActivity prepareWithActivityItems:].cold.2
+ -[UICollaborationSocialActivity setCollaborationItem:]
+ -[UICollaborationSocialActivity setIsPostShare:]
+ -[UIMailActivity _isHTML:]
+ -[UISUIActivityViewControllerConfiguration collaborationIsPostShare]
+ -[UISUIActivityViewControllerConfiguration collaborationType]
+ -[UISUIActivityViewControllerConfiguration setCollaborationIsPostShare:]
+ -[UISUIActivityViewControllerConfiguration setCollaborationType:]
+ -[UISUIActivityViewControllerConfiguration setTestingReferenceSnapshot:]
+ -[UISUIActivityViewControllerConfiguration testingReferenceSnapshot]
+ -[UISharePlayActivity _prepareWithActivityItems:completion:]
+ -[UISharePlayActivity performActivity]
+ -[_UIActivityContentFooterView _disableRasterizeInAnimations]
+ -[_UIActivityMatchingContext collaborationIsPostShare]
+ -[_UIActivityMatchingContext collaborationType]
+ -[_UIActivityMatchingContext setCollaborationIsPostShare:]
+ -[_UIActivityMatchingContext setCollaborationType:]
+ -[_UIActivityMatchingContext setTestingReferenceSnapshot:]
+ -[_UIActivityMatchingContext testingReferenceSnapshot]
+ -[_UIActivityUserDefaultsActivityCell layoutMarginsDidChange]
+ -[_UIActivityUserDefaultsDataSource tableView:titleForHeaderInSection:]
+ -[_UIActivityUserDefaultsViewController tableView:titleForHeaderInSection:]
+ -[_UIActivityViewControllerPresentationController adaptivePresentationStyleForTraitCollection:]
+ -[_UIActivityViewControllerPresentationController compactCornerRadius]
+ -[_UIActivityViewControllerPresentationController cornerRadius]
+ -[_UIActivityViewControllerPresentationController hasSourceItem]
+ -[_UIActivityViewControllerPresentationController initWithPresentedViewController:presentingViewController:]
+ -[_UIActivityViewControllerPresentationController isCompactSize]
+ -[_UIActivityViewControllerPresentationController layoutMargins]
+ -[_UIActivityViewControllerPresentationController preferredContentSizeDidChangeForChildContentContainer:]
+ -[_UIActivityViewControllerPresentationController setCompactCornerRadius:]
+ -[_UIActivityViewControllerPresentationController setCornerRadius:]
+ -[_UIActivityViewControllerPresentationController setLayoutMargins:]
+ -[_UIActivityViewControllerPresentationController updateWithCompactSize:]
+ -[_UIHostActivityProxy activityImageUTI]
+ -[_UIHostActivityProxy setActivityImageUTI:]
+ -[_UIUserDefaultsActivity _systemImageName]
+ -[_UIUserDefaultsActivity initWithActivityCategory:]
+ GCC_except_table106
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table122
+ GCC_except_table128
+ GCC_except_table173
+ GCC_except_table186
+ GCC_except_table195
+ GCC_except_table45
+ GCC_except_table62
+ GCC_except_table94
+ _OBJC_CLASS_$_NSSecurityScopedURLWrapper
+ _OBJC_CLASS_$_SFApplicationExtensionsCache
+ _OBJC_CLASS_$_SHSheetSizeUpdateAction
+ _OBJC_CLASS_$_UIActivityActionHorizontalCell
+ _OBJC_CLASS_$_UICollaborationSocialActivity
+ _OBJC_CLASS_$_UIPanGestureRecognizer
+ _OBJC_CLASS_$__UIActivityViewControllerPresentationController
+ _OBJC_CLASS_$__UIHostedWindowScene
+ _OBJC_IVAR_$_SHSheetContentDataSource._actionUserDefaultsActivity
+ _OBJC_IVAR_$_SHSheetContentDataSource._topActionsMaximumCount
+ _OBJC_IVAR_$_SHSheetContentDataSourceChangeRequest._topActionsMaximumCount
+ _OBJC_IVAR_$_SHSheetContentDataSourceManager._moreActionIdentifier
+ _OBJC_IVAR_$_SHSheetContentDataSourceState._actionIdentifiers
+ _OBJC_IVAR_$_SHSheetContentDataSourceState._moreActionIdentifier
+ _OBJC_IVAR_$_SHSheetContentLayoutContext._showAllActions
+ _OBJC_IVAR_$_SHSheetContentLayoutSpec._linkViewHeaderInsets
+ _OBJC_IVAR_$_SHSheetContentLayoutSpec._portraitWindowSize
+ _OBJC_IVAR_$_SHSheetContentLayoutSpec._sharingAppSectionHeight
+ _OBJC_IVAR_$_SHSheetContentLayoutSpec._topActionsSectionHeight
+ _OBJC_IVAR_$_SHSheetContext._snapshotHandler
+ _OBJC_IVAR_$_SHSheetContext._testingReferenceSnapshot
+ _OBJC_IVAR_$_SHSheetRemoteScene._isSLMEnabled
+ _OBJC_IVAR_$_SHSheetRemoteSceneSettings._isSLMEnabled
+ _OBJC_IVAR_$_SHSheetRemoteSceneViewController._isCompactSize
+ _OBJC_IVAR_$_SHSheetRemoteSceneViewController._isResizable
+ _OBJC_IVAR_$_SHSheetRemoteSceneViewController._isSLMEnabled
+ _OBJC_IVAR_$_SHSheetRouter._isVisionIdiom
+ _OBJC_IVAR_$_SHSheetSession._showCollaborationOptions
+ _OBJC_IVAR_$_SHSheetSession._snapshotHandler
+ _OBJC_IVAR_$_SHSheetSession._testingReferenceSnapshot
+ _OBJC_IVAR_$_SHSheetUIServiceClientContext._hostPortraitWindowSize
+ _OBJC_IVAR_$_SHSheetUIServiceClientContext._sharingStyle
+ _OBJC_IVAR_$_SHSheetUIServiceClientContext._showCollaborationOptions
+ _OBJC_IVAR_$_SHSheetViewModel._showCollaborationOptions
+ _OBJC_IVAR_$_UIActivity._sessionIdentifier
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._activityImageView
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._activityProxy
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._allConstraints
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._contentTintColor
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._didInstallSubviews
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._disabled
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._identifier
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._image
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._imageEffectView
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._imageSlotID
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._imageSlotView
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._isPulsing
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._labelForPositioning
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._largeTextConstraints
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._layoutSpec
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._longPressable
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._regularConstraints
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._title
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._titleLabel
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._titleSlotID
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._titleSlotView
+ _OBJC_IVAR_$_UIActivityActionHorizontalCell._vibrantLabelView
+ _OBJC_IVAR_$_UIActivityContentContext._hostPortraitWindowSize
+ _OBJC_IVAR_$_UIActivityContentContext._sharingStyle
+ _OBJC_IVAR_$_UIActivityContentViewController._collectionViewResizeGestureRecognizer
+ _OBJC_IVAR_$_UIActivityContentViewController._headerViewResizeGestureRecognizer
+ _OBJC_IVAR_$_UIActivityContentViewController._hostPortraitWindowSize
+ _OBJC_IVAR_$_UIActivityContentViewController._hostSLMEnabled
+ _OBJC_IVAR_$_UIActivityContentViewController._isDraggingFromInitialPosition
+ _OBJC_IVAR_$_UIActivityContentViewController._sharingStyle
+ _OBJC_IVAR_$_UIActivityContentViewController._showAllActions
+ _OBJC_IVAR_$_UIActivityViewController._customDetent
+ _OBJC_IVAR_$_UIActivityViewController._initialPreferredContentHeight
+ _OBJC_IVAR_$_UIActivityViewController._snapshotHandler
+ _OBJC_IVAR_$_UIActivityViewController._testingReferenceSnapshot
+ _OBJC_IVAR_$_UICollaborationSocialActivity._collaborationItem
+ _OBJC_IVAR_$_UICollaborationSocialActivity._isPostShare
+ _OBJC_IVAR_$_UISUIActivityViewControllerConfiguration._collaborationIsPostShare
+ _OBJC_IVAR_$_UISUIActivityViewControllerConfiguration._collaborationType
+ _OBJC_IVAR_$_UISUIActivityViewControllerConfiguration._testingReferenceSnapshot
+ _OBJC_IVAR_$__UIActivityMatchingContext._collaborationIsPostShare
+ _OBJC_IVAR_$__UIActivityMatchingContext._collaborationType
+ _OBJC_IVAR_$__UIActivityMatchingContext._testingReferenceSnapshot
+ _OBJC_IVAR_$__UIActivityViewControllerPresentationController._compactCornerRadius
+ _OBJC_IVAR_$__UIActivityViewControllerPresentationController._cornerRadius
+ _OBJC_IVAR_$__UIActivityViewControllerPresentationController._layoutMargins
+ _OBJC_IVAR_$__UIHostActivityProxy._activityImageUTI
+ _OBJC_METACLASS_$_SHSheetSizeUpdateAction
+ _OBJC_METACLASS_$_UIActivityActionHorizontalCell
+ _OBJC_METACLASS_$_UICollaborationSocialActivity
+ _OBJC_METACLASS_$_UIPopoverPresentationController
+ _OBJC_METACLASS_$__UIActivityViewControllerPresentationController
+ _OUTLINED_FUNCTION_3
+ _SFUIShareSheetPopoverBackgroundViewFunction
+ _SHSheetContentActionsSectionIdentifier
+ _SHSheetContentTopActionsSectionIdentifier
+ __NSExtensionIsCollaborationSpecific
+ __OBJC_$_INSTANCE_METHODS_SHSheetSizeUpdateAction
+ __OBJC_$_INSTANCE_METHODS_UIActivityActionHorizontalCell
+ __OBJC_$_INSTANCE_METHODS_UICollaborationSocialActivity
+ __OBJC_$_INSTANCE_METHODS__UIActivityViewControllerPresentationController
+ __OBJC_$_INSTANCE_VARIABLES_UIActivityActionHorizontalCell
+ __OBJC_$_INSTANCE_VARIABLES_UICollaborationSocialActivity
+ __OBJC_$_INSTANCE_VARIABLES__UIActivityViewControllerPresentationController
+ __OBJC_$_PROP_LIST_SHSheetInteractor.391
+ __OBJC_$_PROP_LIST_SHSheetPresenter.621
+ __OBJC_$_PROP_LIST_SHSheetSession.502
+ __OBJC_$_PROP_LIST_SHSheetSizeUpdateAction
+ __OBJC_$_PROP_LIST_UIActivityActionHorizontalCell
+ __OBJC_$_PROP_LIST_UICollaborationSocialActivity
+ __OBJC_$_PROP_LIST__UIActivityViewControllerPresentationController
+ __OBJC_CLASS_PROTOCOLS_$_UICollaborationSocialActivity
+ __OBJC_CLASS_RO_$_SHSheetSizeUpdateAction
+ __OBJC_CLASS_RO_$_UIActivityActionHorizontalCell
+ __OBJC_CLASS_RO_$_UICollaborationSocialActivity
+ __OBJC_CLASS_RO_$__UIActivityViewControllerPresentationController
+ __OBJC_METACLASS_RO_$_SHSheetSizeUpdateAction
+ __OBJC_METACLASS_RO_$_UIActivityActionHorizontalCell
+ __OBJC_METACLASS_RO_$_UICollaborationSocialActivity
+ __OBJC_METACLASS_RO_$__UIActivityViewControllerPresentationController
+ __ShareSheetApplicationKeyWindow
+ __ShareSheetIsPhotos
+ __ShareSheetIsPhotos.cold.1
+ __ShareSheetSolariumEnabled
+ __UISolariumEnabled
+ ___40-[SHSheetSession _configureWithContext:]_block_invoke.14
+ ___60-[UISharePlayActivity _prepareWithActivityItems:completion:]_block_invoke
+ ___62-[UIActivityContentViewController _updateHeaderLinkViewAction]_block_invoke_6
+ ___63-[UIActivityViewController _updateSheetPresentationController:]_block_invoke
+ ___64-[SHSheetActivityPerformer _enqueueBackgroundOperationsIfNeeded]_block_invoke.96
+ ___64-[SHSheetActivityPerformer _enqueueBackgroundOperationsIfNeeded]_block_invoke.97
+ ___67-[SHSheetActivityPerformer _performPresentationWithViewController:]_block_invoke.75
+ ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke.23
+ ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke.34
+ ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke_2.24
+ ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke_2.24.cold.1
+ ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke_2.35
+ ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke_2.35.cold.1
+ ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.146
+ ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.147
+ ___81-[UIActivityContentViewController _configureHorizontalActionCell:itemIdentifier:]_block_invoke
+ ___81-[UIActivityContentViewController _configureHorizontalActionCell:itemIdentifier:]_block_invoke_2
+ ___81-[UIActivityContentViewController _configureHorizontalActionCell:itemIdentifier:]_block_invoke_3
+ ___82-[UIActivityContentViewController observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke.40
+ ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke.42
+ ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke.44
+ ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.41
+ ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.41.cold.1
+ ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.43
+ ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.43.cold.1
+ ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.45
+ ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.45.cold.1
+ ___86-[UIActivityContentViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke_2
+ ___94-[SHSheetRouter dismissForActivityPerformerResult:didPresentFromShareSheet:completionHandler:]_block_invoke.141
+ ____loadItemProviderInline_block_invoke.531
+ ____loadItemProviderInline_block_invoke.531.cold.1
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.503
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.505
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.505.cold.1
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.506
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.508
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.508.cold.1
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.509
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.510
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.510.cold.1
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.511
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.513
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.513.cold.1
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.517
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.520
+ ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.521
+ ___block_descriptor_32_e36_v16?0"NSSecurityScopedURLWrapper"8l
+ ___block_descriptor_40_e8_32s_e64_d16?0"<UISheetPresentationControllerDetentResolutionContext>"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e21_v24?0q8"NSString"16lr32l8r40l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e21_v24?0q8"NSString"16lr48l8s32l8r56l8s40l8
+ ___block_literal_global.10
+ ___block_literal_global.1002
+ ___block_literal_global.1007
+ ___block_literal_global.1011
+ ___block_literal_global.1017
+ ___block_literal_global.102
+ ___block_literal_global.107
+ ___block_literal_global.112
+ ___block_literal_global.117
+ ___block_literal_global.122
+ ___block_literal_global.127
+ ___block_literal_global.14
+ ___block_literal_global.142
+ ___block_literal_global.145
+ ___block_literal_global.148
+ ___block_literal_global.151
+ ___block_literal_global.178
+ ___block_literal_global.198
+ ___block_literal_global.312
+ ___block_literal_global.316
+ ___block_literal_global.32
+ ___block_literal_global.321
+ ___block_literal_global.356
+ ___block_literal_global.360
+ ___block_literal_global.366
+ ___block_literal_global.40
+ ___block_literal_global.497
+ ___block_literal_global.51
+ ___block_literal_global.530
+ ___block_literal_global.54
+ ___block_literal_global.58
+ ___block_literal_global.611
+ ___block_literal_global.615
+ ___block_literal_global.67
+ ___block_literal_global.72
+ ___block_literal_global.92
+ ___block_literal_global.97
+ ___initValCNContactCropRectKey_block_invoke
+ ___initValCNContactCropRectKey_block_invoke.cold.1
+ ___initValCNContactFullscreenImageDataKey_block_invoke
+ ___initValCNContactFullscreenImageDataKey_block_invoke.cold.1
+ ___initValCNContactThumbnailImageDataKey_block_invoke
+ ___initValCNContactThumbnailImageDataKey_block_invoke.cold.1
+ ___initValMCFeatureAccountModificationAllowed_block_invoke
+ ___initValMCFeatureAccountModificationAllowed_block_invoke.cold.1
+ _audit_stringSharedWithYouCore
+ _classSFUIShareSheetPopoverBackgroundView
+ _getSFUIShareSheetPopoverBackgroundViewClass
+ _initSFUIShareSheetPopoverBackgroundView
+ _initSFUIShareSheetPopoverBackgroundView.cold.1
+ _objc_msgSend$_addResizeGestureIfNeeded
+ _objc_msgSend$_configureHorizontalActionCell:itemIdentifier:
+ _objc_msgSend$_createHorizontalLayoutSectionWithContext:iconWidth:sectionHeight:
+ _objc_msgSend$_detents
+ _objc_msgSend$_glassButtonConfiguration
+ _objc_msgSend$_isHTML:
+ _objc_msgSend$_isOnlyCompactSize
+ _objc_msgSend$_isOnlyFullSize
+ _objc_msgSend$_layoutForTopActionSectionWithContext:
+ _objc_msgSend$_removeResizeGestureIfNeeded
+ _objc_msgSend$_resetPanGesture:
+ _objc_msgSend$_setAdjustsContentInsetWhenScrollDisabled:
+ _objc_msgSend$_setBottomAlignsPopoverIfSourceViewNotSet:
+ _objc_msgSend$_setCornerRadius:
+ _objc_msgSend$_setIgnoredEdgesForSafeArea:
+ _objc_msgSend$_setPreferredContentSize:
+ _objc_msgSend$_setSecondaryButtonAction:
+ _objc_msgSend$_setShouldHideArrow:
+ _objc_msgSend$_shouldShowCloseButton
+ _objc_msgSend$_updateBlurBackgroundIfNeeded
+ _objc_msgSend$_updateContent:
+ _objc_msgSend$_updatePreferredContentSize
+ _objc_msgSend$_updateShowAllActions
+ _objc_msgSend$_updateTestingSnapshotIfNeededForResolvedItems:activityType:
+ _objc_msgSend$_wantsResizePanGesture
+ _objc_msgSend$_windowHostingScene
+ _objc_msgSend$accessibilityIdentifier
+ _objc_msgSend$actionUserDefaultsActivity
+ _objc_msgSend$activityViewControllerDidDisappearWithSessionID:
+ _objc_msgSend$activityViewControllerDidFailAirdropTransfer:
+ _objc_msgSend$activityViewControllerSessionDidEndWithCompletionHandler:
+ _objc_msgSend$activityViewControllerSessionDidEndWithSessionID:testingSnapshot:completionHandler:
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$adjustedContentInset
+ _objc_msgSend$canPerformWithCollaborationType:isPostShare:
+ _objc_msgSend$collaborationIsPostShare
+ _objc_msgSend$collaborationType
+ _objc_msgSend$collectionViewResizeGestureRecognizer
+ _objc_msgSend$compactCornerRadius
+ _objc_msgSend$containsView:
+ _objc_msgSend$cornerRadius
+ _objc_msgSend$customDetent
+ _objc_msgSend$customDetentWithIdentifier:resolver:
+ _objc_msgSend$didUpdateSheetSize
+ _objc_msgSend$directlyCreateActivity
+ _objc_msgSend$extensionsResultWithMatchingAttributes:testingReferenceSnapshot:
+ _objc_msgSend$hasSourceItem
+ _objc_msgSend$headerViewResizeGestureRecognizer
+ _objc_msgSend$hostPortraitWindowSize
+ _objc_msgSend$hostSLMEnabled
+ _objc_msgSend$imageEffectView
+ _objc_msgSend$initWithActivityCategory:
+ _objc_msgSend$initWithState:excludeSectionTypes:topActionsMaximumCount:
+ _objc_msgSend$initWithTraitCollection:tintColor:deviceClass:portraitWindowSize:
+ _objc_msgSend$initialPreferredContentHeight
+ _objc_msgSend$isCompact
+ _objc_msgSend$isCompactSize
+ _objc_msgSend$isDraggingFromInitialPosition
+ _objc_msgSend$isKeyWindow
+ _objc_msgSend$isPossibleToDirectlyCreateActivity
+ _objc_msgSend$isPostShare
+ _objc_msgSend$isResizable
+ _objc_msgSend$isSLMEnabled
+ _objc_msgSend$isSheetResizable
+ _objc_msgSend$isVisionIdiom
+ _objc_msgSend$linkViewHeaderInsets
+ _objc_msgSend$moreActionIdentifier
+ _objc_msgSend$needsLeftIconLayout
+ _objc_msgSend$popViewControllerAnimated:
+ _objc_msgSend$prepareForShareSheetSessionWithCompletion:
+ _objc_msgSend$removeGestureRecognizer:
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$requestSharedURLForCollaborationRequest:completionHandler:
+ _objc_msgSend$resolvedBottomCornerRadiusForView:
+ _objc_msgSend$scene:didReceiveSizeUpdateAction:
+ _objc_msgSend$setActionIdentifiers:
+ _objc_msgSend$setCanOverlapSourceViewRect:
+ _objc_msgSend$setCollaborationIsPostShare:
+ _objc_msgSend$setCollaborationType:
+ _objc_msgSend$setCollectionViewResizeGestureRecognizer:
+ _objc_msgSend$setCompactCornerRadius:
+ _objc_msgSend$setCustomDetent:
+ _objc_msgSend$setHeaderViewResizeGestureRecognizer:
+ _objc_msgSend$setHidesBackButton:
+ _objc_msgSend$setHitTestsAsOpaque:
+ _objc_msgSend$setHostPortraitWindowSize:
+ _objc_msgSend$setImageEffectView:
+ _objc_msgSend$setInitialPreferredContentHeight:
+ _objc_msgSend$setIsCompactSize:
+ _objc_msgSend$setIsDraggingFromInitialPosition:
+ _objc_msgSend$setIsPostShare:
+ _objc_msgSend$setIsResizable:
+ _objc_msgSend$setIsSLMEnabled:
+ _objc_msgSend$setLayoutMargins:
+ _objc_msgSend$setMoreActionIdentifier:
+ _objc_msgSend$setPopoverLayoutMargins:
+ _objc_msgSend$setSessionIdentifier:
+ _objc_msgSend$setShowAllActions:
+ _objc_msgSend$setShowCollaborationOptions:
+ _objc_msgSend$setSnapshotHandler:
+ _objc_msgSend$setTestingReferenceSnapshot:
+ _objc_msgSend$setTopActionsMaximumCount:
+ _objc_msgSend$setUserSelectedShareOptions:
+ _objc_msgSend$sharingAppSectionHeight
+ _objc_msgSend$showAllActions
+ _objc_msgSend$showCollaborationOptions
+ _objc_msgSend$snapshotHandler
+ _objc_msgSend$sourceItem
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$tableView:titleForHeaderInSection:
+ _objc_msgSend$testingReferenceSnapshot
+ _objc_msgSend$topActionsMaximumCount
+ _objc_msgSend$topActionsSectionHeight
+ _objc_msgSend$translationInView:
+ _objc_msgSend$updateHostingController:withContext:hostProcessType:hostPresentationStyle:optionGroups:collaborationOptionsData:cloudShareRequest:isSLMEnabled:
+ _objc_msgSend$updateWithCompactSize:
+ _objc_msgSend$windows
+ _softLinkOnceCNContactCropRectKey
+ _softLinkOnceCNContactFullscreenImageDataKey
+ _softLinkOnceCNContactThumbnailImageDataKey
+ _softLinkOnceMCFeatureAccountModificationAllowed
+ _solariumLayout
- +[SHSheetRemoteSceneSettings settingsWithSessionContext:presnetationStyle:hostProcessType:customizationGroups:collaborationOptions:cloudShareRequest:]
- +[UIActivityItemImageRep activityItemImageRepWithAsset:thumbnailProvider:dataProvider:]
- -[NSDictionary(ShareSheet) sh_removingUnsupportedTypes]
- -[SFShareSheetSlotManager activityViewControllerDidDisappearWithSessionID:testingSnapshot:]
- -[SFShareSheetSlotManager requestSharedURLForFileOrFolderURL:completionHandler:]
- -[SHSheetContentDataSource initWithState:excludeSectionTypes:]
- -[SHSheetContentDataSource initWithState:excludeSectionTypes:].cold.1
- -[SHSheetContentLayoutProvider _createHorizontalLayoutSectionWithContext:iconWidth:]
- -[SHSheetContentLayoutSpec initWithTraitCollection:tintColor:deviceClass:]
- -[SHSheetServiceManager requestSharedURLForFileOrFolderURL:completionHandler:]
- -[UIActivityItemImageRep .cxx_destruct]
- -[UIActivityItemImageRep asset]
- -[UIActivityItemImageRep dataProvider]
- -[UIActivityItemImageRep data]
- -[UIActivityItemImageRep setAsset:]
- -[UIActivityItemImageRep setDataProvider:]
- -[UIActivityItemImageRep setThumbnailProvider:]
- -[UIActivityItemImageRep thumbnailProvider]
- -[UIActivityItemImageRep thumbnail]
- -[UIMailActivity setSessionID:]
- -[UIMessageActivity setSessionID:]
- -[UISharePlayActivity setSessionID:]
- GCC_except_table118
- GCC_except_table126
- GCC_except_table169
- GCC_except_table193
- GCC_except_table196
- GCC_except_table205
- GCC_except_table223
- GCC_except_table224
- GCC_except_table234
- GCC_except_table236
- GCC_except_table241
- GCC_except_table43
- GCC_except_table73
- GCC_except_table87
- GCC_except_table92
- GCC_except_table96
- _ALAssetFunction
- _ALAssetPropertyAssetURLFunction
- _ALAssetsLibraryErrorDomainFunction
- _AssetsLibraryLibrary
- _AssetsLibraryLibrary.sLib
- _AssetsLibraryLibrary.sOnce
- _AssetsLibraryLibraryCore.frameworkLibrary
- _IsALAsset
- _IsAssetURL
- _IsPhotoAssetURL
- _IsVideoAssetURL
- _IsVideoAssetURL.cold.1
- _NewRepresentationFromPhotoAsset
- _OBJC_CLASS_$_UIActivityItemImageRep
- _OBJC_IVAR_$_UIActivityItemImageRep._asset
- _OBJC_IVAR_$_UIActivityItemImageRep._dataProvider
- _OBJC_IVAR_$_UIActivityItemImageRep._thumbnailProvider
- _OBJC_METACLASS_$_UIActivityItemImageRep
- _RepresentationFromPhotoAssetURL
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_ShareSheet
- __OBJC_$_CATEGORY_NSDictionary_$_ShareSheet
- __OBJC_$_CLASS_METHODS_UIActivityItemImageRep
- __OBJC_$_INSTANCE_METHODS_UIActivityItemImageRep
- __OBJC_$_INSTANCE_VARIABLES_UIActivityItemImageRep
- __OBJC_$_PROP_LIST_SHSheetInteractor.385
- __OBJC_$_PROP_LIST_SHSheetPresenter.614
- __OBJC_$_PROP_LIST_SHSheetSession.480
- __OBJC_$_PROP_LIST_UIActivityItemImageRep
- __OBJC_$_PROP_LIST_UIPeopleSuggestionRecipientActivity
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UIRemoteSheet
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIPeopleSuggestionRecipientActivity
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIPeopleSuggestionRecipientActivity
- __OBJC_CLASS_RO_$_UIActivityItemImageRep
- __OBJC_LABEL_PROTOCOL_$_UIPeopleSuggestionRecipientActivity
- __OBJC_METACLASS_RO_$_UIActivityItemImageRep
- __OBJC_PROTOCOL_$_UIPeopleSuggestionRecipientActivity
- ___64-[SHSheetActivityPerformer _enqueueBackgroundOperationsIfNeeded]_block_invoke.98
- ___64-[SHSheetActivityPerformer _enqueueBackgroundOperationsIfNeeded]_block_invoke.99
- ___67-[SHSheetActivityPerformer _performPresentationWithViewController:]_block_invoke.77
- ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke.15
- ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke.18
- ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke_2.16
- ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke_2.16.cold.1
- ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke_2.19
- ___71-[UIApplicationExtensionActivity prepareWithActivityExtensionItemData:]_block_invoke_2.19.cold.1
- ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.143
- ___77-[SHSheetRouter activityPerformer:preparePresentationWithContext:completion:]_block_invoke.144
- ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke.32
- ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke.34
- ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke.36
- ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.33
- ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.33.cold.1
- ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.35
- ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.35.cold.1
- ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.37
- ___84-[UIApplicationExtensionActivity _instantiateExtensionViewControllerWithInputItems:]_block_invoke_2.37.cold.1
- ___94-[SHSheetRouter dismissForActivityPerformerResult:didPresentFromShareSheet:completionHandler:]_block_invoke.138
- ___AssetsLibraryLibraryCore_block_invoke
- ___AssetsLibraryLibrary_block_invoke
- ___ImageForItem_block_invoke
- ___ImageForItem_block_invoke_2
- ___ImageForItem_block_invoke_3
- ___ImageForItem_block_invoke_4
- ___IsAssetURL_block_invoke
- ___IsAssetURL_block_invoke_2
- ___IsAssetURL_block_invoke_3
- ___RepresentationFromPhotoAssetURL_block_invoke
- ___RepresentationFromPhotoAssetURL_block_invoke_2
- ___RepresentationFromPhotoAssetURL_block_invoke_3
- ____NSItemProviderForUIActivityItemImageRep_block_invoke
- ____NSItemProviderForUIActivityItemImageRep_block_invoke_2
- ____NSItemProviderForUIActivityItemImageRep_block_invoke_3
- ____loadItemProviderInline_block_invoke.550
- ____loadItemProviderInline_block_invoke.550.cold.1
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.524
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.524.cold.1
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.525
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.527
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.527.cold.1
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.528
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.529
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.529.cold.1
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.530
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.532
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.532.cold.1
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.536
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.539
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.540
- ____loadItemProvidersFromActivityItemsStartingAtIndex_block_invoke.541
- ___block_descriptor_40_e8_32s_e13_"NSData"8?0ls32l8
- ___block_descriptor_40_e8_32s_e14_"UIImage"8?0ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_e8_32r40r_e24_v28?0q8"NSString"16B24lr32l8r40l8
- ___block_descriptor_48_e8_32s40s_e63_v32?0?<v?"<NSSecureCoding>""NSError">8#16"NSDictionary"24ls32l8s40l8
- ___block_descriptor_52_e8_32s40r_e17_v16?0"ALAsset"8lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e17_v16?0"ALAsset"8lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40bs48r56r_e24_v28?0q8"NSString"16B24lr48l8s32l8r56l8s40l8
- ___block_descriptor_68_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
- ___block_literal_global.104
- ___block_literal_global.109
- ___block_literal_global.114
- ___block_literal_global.119
- ___block_literal_global.12
- ___block_literal_global.143
- ___block_literal_global.188
- ___block_literal_global.192
- ___block_literal_global.30
- ___block_literal_global.315
- ___block_literal_global.319
- ___block_literal_global.354
- ___block_literal_global.361
- ___block_literal_global.38
- ___block_literal_global.43
- ___block_literal_global.44
- ___block_literal_global.516
- ___block_literal_global.52
- ___block_literal_global.549
- ___block_literal_global.57
- ___block_literal_global.583
- ___block_literal_global.61
- ___block_literal_global.66
- ___block_literal_global.754
- ___block_literal_global.759
- ___block_literal_global.763
- ___block_literal_global.769
- ___block_literal_global.8
- ___block_literal_global.84
- ___block_literal_global.89
- ___block_literal_global.94
- ___block_literal_global.99
- ___getALAssetPropertyTypeSymbolLoc_block_invoke
- ___getALAssetTypePhotoSymbolLoc_block_invoke
- ___getALAssetTypeVideoSymbolLoc_block_invoke
- ___getALAssetsLibraryClass_block_invoke
- ___getALAssetsLibraryClass_block_invoke.cold.1
- _audit_stringAssetsLibrary
- _classALAsset
- _constantValALAssetPropertyAssetURL
- _constantValALAssetsLibraryErrorDomain
- _getALAssetClass
- _getALAssetPropertyAssetURL
- _getALAssetPropertyType
- _getALAssetPropertyType.cold.1
- _getALAssetPropertyTypeSymbolLoc.ptr
- _getALAssetTypePhoto
- _getALAssetTypePhoto.cold.1
- _getALAssetTypePhotoSymbolLoc.ptr
- _getALAssetTypeVideoSymbolLoc.ptr
- _getALAssetsLibraryClass
- _getALAssetsLibraryClass.softClass
- _getALAssetsLibraryErrorDomain
- _initALAsset
- _initALAsset.cold.1
- _initValALAssetPropertyAssetURL
- _initValALAssetPropertyAssetURL.cold.1
- _initValALAssetsLibraryErrorDomain
- _initValALAssetsLibraryErrorDomain.cold.1
- _objc_msgSend$_createHorizontalLayoutSectionWithContext:iconWidth:
- _objc_msgSend$_isPhotoServiceAccessGranted
- _objc_msgSend$activityItemImageRepWithAsset:thumbnailProvider:dataProvider:
- _objc_msgSend$activityViewControllerDidDisappearWithSessionID:testingSnapshot:
- _objc_msgSend$addTarget:action:forEvents:
- _objc_msgSend$asset
- _objc_msgSend$assetForURL:resultBlock:failureBlock:
- _objc_msgSend$data
- _objc_msgSend$dataWithLength:
- _objc_msgSend$defaultRepresentation
- _objc_msgSend$fullScreenImage
- _objc_msgSend$getBytes:fromOffset:length:error:
- _objc_msgSend$imageWithCGImage:
- _objc_msgSend$initWithCGImage:
- _objc_msgSend$initWithCGImage:scale:orientation:
- _objc_msgSend$initWithState:excludeSectionTypes:
- _objc_msgSend$initWithTraitCollection:tintColor:deviceClass:
- _objc_msgSend$mutableBytes
- _objc_msgSend$requestSharedURLForFileOrFolderURL:completionHandler:
- _objc_msgSend$setAsset:
- _objc_msgSend$setDataProvider:
- _objc_msgSend$setShowOptions:
- _objc_msgSend$setThumbnailProvider:
- _objc_msgSend$updateHostingController:withContext:hostProcessType:hostPresentationStyle:optionGroups:collaborationOptionsData:cloudShareRequest:
- _objc_msgSend$valueForProperty:
CStrings:
+ "### ISAirDrop:%d with itemIdentifier: %@"
+ "%@: canPerform:NO collaborationType:%ld supportedCollaborationTypes:%@"
+ "%@: canPerform:YES collaborationType:%ld supportedCollaborationTypes:%@"
+ ", isCollaborative, collaborationType: %@, collaborationIsPostShare: %@"
+ ", usingTestingReferenceSnapshot"
+ ":"
+ "<%@: identifier:%@ activity:%@ iconImageSlotID:%u, textSlot:%u, isDisabled:%@, isFavorite:%@, isRestricted:%@, isUserDefaultsActivity:%@, activityIdentifierShare:%@, activityIdentifierOpen:%@, activityIdentifierCopy:%@, textHeight:%f, activityTitle:%@, activityFooter:%@, bundleIdentifier:%@, activityImageUTI:%@>"
+ "?A#\""
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"UIPanGestureRecognizer\""
+ "@\"UISheetPresentationControllerDetent\""
+ "@24@0:8B16B20"
+ "@40@0:8@16d24d32"
+ "@40@0:8@16q24Q32"
+ "@56@0:8@16@24Q32{CGSize=dd}40"
+ "@68@0:8@16q24q32@40@48@56B64"
+ "ActionsView"
+ "AppsView"
+ "B28@0:8q16B24"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "DocumentManager"
+ "DriveRSA"
+ "Edit Actions"
+ "Failed to archive SWCollaborationMetadata: %@"
+ "Failed to archive SWCollaborationShareOptions: %@"
+ "NSExtensionActivationSupportsCollaborationWithTypes"
+ "NSExtensionIconUTI"
+ "NSExtensionIsCollaborationSpecific"
+ "No current detent was found."
+ "Photos"
+ "Preparing collaboration extension with resolved activity items:%@, metadata:%@, options:%@"
+ "SFCollaborationActivityPostShareTitle"
+ "SFCollaborationActivityPreShareTitle"
+ "SFUIShareSheetPopoverBackgroundView"
+ "SHSheetContentActionsSectionIdentifier"
+ "SHSheetContentSectionTypeTopActions"
+ "SHSheetContentTopActionsSectionIdentifier"
+ "SHSheetRemoteSceneViewController received size update"
+ "SHSheetSizeUpdateAction"
+ "SWCollaborationMetadata"
+ "SWCollaborationShareOptions"
+ "SharePlay: Unexpectedly unable to directly create activity"
+ "ShareSheet.Edit"
+ "ShareSheetScrollHorizontalApps"
+ "ShareSheetSolarium"
+ "ShareSheetTestability"
+ "SharedWithYou"
+ "Sharing/SFShareSheetSlotManager/activityViewControllerSessionDidEnd"
+ "Sharing/SFShareSheetSlotManager/requestSharedURLForCollaborationRequest"
+ "T@\"NSArray\",C,N,V_actionIdentifiers"
+ "T@\"NSNumber\",&,N,V_hostSLMEnabled"
+ "T@\"NSNumber\",N,V_collaborationIsPostShare"
+ "T@\"NSNumber\",N,V_collaborationType"
+ "T@\"NSString\",&,N,V_sessionIdentifier"
+ "T@\"NSString\",C,N,V_activityImageUTI"
+ "T@\"NSUUID\",C,N,V_moreActionIdentifier"
+ "T@\"SFShareSheetSessionTestingSnapshot\",&,N,V_testingReferenceSnapshot"
+ "T@\"UIPanGestureRecognizer\",&,N,V_collectionViewResizeGestureRecognizer"
+ "T@\"UIPanGestureRecognizer\",&,N,V_headerViewResizeGestureRecognizer"
+ "T@\"UISheetPresentationControllerDetent\",&,N,V_customDetent"
+ "T@\"UIVisualEffectView\",&,N,V_imageEffectView"
+ "T@\"_UIUserDefaultsActivity\",R,N,V_actionUserDefaultsActivity"
+ "T@?,C,N,V_snapshotHandler"
+ "TB,N,V_isCompactSize"
+ "TB,N,V_isDraggingFromInitialPosition"
+ "TB,N,V_isPostShare"
+ "TB,N,V_isResizable"
+ "TB,N,V_isSLMEnabled"
+ "TB,N,V_showAllActions"
+ "TB,N,V_showCollaborationOptions"
+ "TB,R,N,V_isSLMEnabled"
+ "TB,R,N,V_isVisionIdiom"
+ "TB,R,N,V_showCollaborationOptions"
+ "TQ,N,V_topActionsMaximumCount"
+ "TQ,R,N,V_topActionsMaximumCount"
+ "Td,N,V_compactCornerRadius"
+ "Td,N,V_cornerRadius"
+ "Td,N,V_initialPreferredContentHeight"
+ "Td,R,N,V_sharingAppSectionHeight"
+ "Td,R,N,V_topActionsSectionHeight"
+ "There is no app section."
+ "There is no custom view section."
+ "There is no people section."
+ "Tq,R,N,V_sharingStyle"
+ "T{CGSize=dd},N,V_hostPortraitWindowSize"
+ "T{CGSize=dd},R,N,V_hostPortraitWindowSize"
+ "T{CGSize=dd},R,N,V_portraitWindowSize"
+ "T{NSDirectionalEdgeInsets=dddd},R,N,V_linkViewHeaderInsets"
+ "T{UIEdgeInsets=dddd},N,V_layoutMargins"
+ "UIActivityActionHorizontalCell"
+ "UIActivityContentTopActionCellIdentifier"
+ "UICollaborationSocialActivity"
+ "_UIActivityViewControllerPresentationController"
+ "_actionIdentifiers"
+ "_actionUserDefaultsActivity"
+ "_addResizeGestureIfNeeded"
+ "_bottomAlignsPopoverIfSourceViewNotSet"
+ "_collaborationIsPostShare"
+ "_collaborationType"
+ "_collectionViewResizeGestureRecognizer"
+ "_compactCornerRadius"
+ "_configureHorizontalActionCell:itemIdentifier:"
+ "_cornerRadius"
+ "_createHorizontalLayoutSectionWithContext:iconWidth:sectionHeight:"
+ "_customDetent"
+ "_detents"
+ "_disableRasterizeInAnimations"
+ "_glassButtonConfiguration"
+ "_handleResizeGesture:"
+ "_headerViewResizeGestureRecognizer"
+ "_hostPortraitWindowSize"
+ "_hostSLMEnabled"
+ "_imageEffectView"
+ "_initialPreferredContentHeight"
+ "_isCompactSize"
+ "_isDraggingFromInitialPosition"
+ "_isHTML:"
+ "_isOnlyCompactSize"
+ "_isOnlyFullSize"
+ "_isPostShare"
+ "_isResizable"
+ "_isSLMEnabled"
+ "_isVisionIdiom"
+ "_layoutForTopActionSectionWithContext:"
+ "_layoutMargins"
+ "_linkViewHeaderInsets"
+ "_moreActionIdentifier"
+ "_portraitWindowSize"
+ "_removeResizeGestureIfNeeded"
+ "_resetPanGesture:"
+ "_setAdjustsContentInsetWhenScrollDisabled:"
+ "_setBottomAlignsPopoverIfSourceViewNotSet:"
+ "_setCornerRadius:"
+ "_setIgnoredEdgesForSafeArea:"
+ "_setPreferredContentSize:"
+ "_setSecondaryButtonAction:"
+ "_setShouldHideArrow:"
+ "_sharingAppSectionHeight"
+ "_shouldShowCloseButton"
+ "_showAllActions"
+ "_showCollaborationOptions"
+ "_snapshotHandler"
+ "_testingReferenceSnapshot"
+ "_topActionsMaximumCount"
+ "_topActionsSectionHeight"
+ "_updateBlurBackgroundIfNeeded"
+ "_updateContent:"
+ "_updatePreferredContentSize"
+ "_updateShowAllActions"
+ "_updateTestingSnapshotIfNeededForResolvedItems:activityType:"
+ "_wantsResizePanGesture"
+ "_windowHostingScene"
+ "accessibilityIdentifier"
+ "actionIdentifiers"
+ "actionUserDefaultsActivity"
+ "activityViewControllerDidDisappearWithSessionID:"
+ "activityViewControllerDidFailAirdropTransfer:"
+ "activityViewControllerSessionDidEndWithCompletionHandler:"
+ "activityViewControllerSessionDidEndWithSessionID:testingSnapshot:completionHandler:"
+ "adaptivePresentationStyleForTraitCollection:"
+ "addObserver:forKeyPath:options:context:"
+ "adjustedContentInset"
+ "canPerformWithCollaborationType:isPostShare:"
+ "collaborationIsPostShare"
+ "collaborationType"
+ "collectionViewResizeGestureRecognizer"
+ "com.apple.CloudSharingUI.CreateiCloudLinkExtension"
+ "compactCornerRadius"
+ "containsView:"
+ "cornerRadius"
+ "customDetent"
+ "customDetentWithIdentifier:resolver:"
+ "d16@?0@\"<UISheetPresentationControllerDetentResolutionContext>\"8"
+ "didUpdateSheetSize"
+ "directlyCreateActivity"
+ "ellipsis"
+ "extensionsResultWithMatchingAttributes:testingReferenceSnapshot:"
+ "hasSourceItem"
+ "headerViewResizeGestureRecognizer"
+ "horizontal cell _activitySubtitle:%@"
+ "hostPortraitWindowSize"
+ "hostSLMEnabled"
+ "imageEffectView"
+ "initWithActivityCategory:"
+ "initWithSize:isResizable:"
+ "initWithState:excludeSectionTypes:topActionsMaximumCount:"
+ "initWithTraitCollection:tintColor:deviceClass:portraitWindowSize:"
+ "initialPreferredContentHeight"
+ "isCompact"
+ "isCompactSize"
+ "isDraggingFromInitialPosition"
+ "isKeyWindow"
+ "isPossibleToDirectlyCreateActivity"
+ "isPostShare"
+ "isResizable"
+ "isSLMEnabled"
+ "isSheetResizable"
+ "isVisionIdiom"
+ "layoutMarginsDidChange"
+ "linkViewHeaderInsets"
+ "moreActionIdentifier"
+ "needsLeftIconLayout"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "popViewControllerAnimated:"
+ "portraitWindowSize"
+ "prepareForShareSheetSessionWithCompletion:"
+ "removeGestureRecognizer:"
+ "removeObjectsInArray:"
+ "removeObserver:forKeyPath:"
+ "requestSharedURLForCollaborationRequest:completionHandler:"
+ "resolvedBottomCornerRadiusForView:"
+ "scene:didReceiveSizeUpdateAction:"
+ "setActionIdentifiers:"
+ "setCanOverlapSourceViewRect:"
+ "setCollaborationIsPostShare:"
+ "setCollaborationType:"
+ "setCollectionViewResizeGestureRecognizer:"
+ "setCompactCornerRadius:"
+ "setCustomDetent:"
+ "setHeaderViewResizeGestureRecognizer:"
+ "setHidesBackButton:"
+ "setHitTestsAsOpaque:"
+ "setHostPortraitWindowSize:"
+ "setHostSLMEnabled:"
+ "setImageEffectView:"
+ "setInitialPreferredContentHeight:"
+ "setIsCompactSize:"
+ "setIsDraggingFromInitialPosition:"
+ "setIsPostShare:"
+ "setIsResizable:"
+ "setIsSLMEnabled:"
+ "setLayoutMargins:"
+ "setMoreActionIdentifier:"
+ "setPopoverLayoutMargins:"
+ "setShowAllActions:"
+ "setShowCollaborationOptions:"
+ "setSnapshotHandler:"
+ "setTestingReferenceSnapshot:"
+ "setTopActionsMaximumCount:"
+ "setUserSelectedShareOptions:"
+ "settingsWithSessionContext:presnetationStyle:hostProcessType:customizationGroups:collaborationOptions:cloudShareRequest:isSLMEnabled:"
+ "sharingAppSectionHeight"
+ "shouldShowProgressForCollaborationPerformer:"
+ "showAllActions"
+ "showCollaborationOptions"
+ "snapshotHandler"
+ "sourceItem"
+ "subarrayWithRange:"
+ "testingReferenceSnapshot"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:shouldChangeTextInRanges:replacementText:"
+ "topActionsMaximumCount"
+ "topActionsSectionHeight"
+ "translationInView:"
+ "updateHostingController:withContext:hostProcessType:hostPresentationStyle:optionGroups:collaborationOptionsData:cloudShareRequest:isSLMEnabled:"
+ "updateWithCompactSize:"
+ "v16@?0@\"NSSecurityScopedURLWrapper\"8"
+ "v24@?0q8@\"NSString\"16"
+ "v32@0:8@\"SHSheetRemoteScene\"16@\"SHSheetSizeUpdateAction\"24"
+ "v40@0:8@\"NSString\"16@\"SFShareSheetSessionTestingSnapshot\"24@?<v@?@\"NSSecurityScopedURLWrapper\">32"
+ "v48@0:8@16@24@32^v40"
+ "windows"
+ "\xf0\xf0sA"
- ", isCollaborative"
- "/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary"
- "/System/Library/Frameworks/ManagedConfiguration.framework/ManagedConfiguration"
- "9"
- "<%@: identifier:%@ activity:%@ iconImageSlotID:%u, textSlot:%u, isDisabled:%@, isFavorite:%@, isRestricted:%@, isUserDefaultsActivity:%@, activityIdentifierShare:%@, activityIdentifierOpen:%@, activityIdentifierCopy:%@, textHeight:%f, activityTitle:%@, activityFooter:%@, bundleIdentifier:%@>"
- "?D!"
- "@\"NSData\"8@?0"
- "@32@0:8@16d24"
- "@40@0:8@16@?24@?32"
- "@64@0:8@16q24q32@40@48@56"
- "ALAsset"
- "ALAssetPropertyAssetURL"
- "ALAssetPropertyType"
- "ALAssetTypePhoto"
- "ALAssetTypeVideo"
- "ALAssetsLibrary"
- "ALAssetsLibraryErrorDomain"
- "Manage"
- "MobileSlideShow"
- "Sharing/SFShareSheetSlotManager/requestSharedURLForFileOrFolderURL"
- "T@,&,N,V_asset"
- "T@?,C,N,V_dataProvider"
- "T@?,C,N,V_thumbnailProvider"
- "TB,?,R,N"
- "UIActivityItemImageRep"
- "UIPeopleSuggestionRecipientActivity"
- "_allowsConnection"
- "_asset"
- "_createHorizontalLayoutSectionWithContext:iconWidth:"
- "_dataProvider"
- "_isPhotoServiceAccessGranted"
- "_thumbnailProvider"
- "activityItemImageRepWithAsset:thumbnailProvider:dataProvider:"
- "activityViewControllerDidDisappearWithSessionID:testingSnapshot:"
- "addTarget:action:forEvents:"
- "asset"
- "assetForURL:resultBlock:failureBlock:"
- "data"
- "dataProvider"
- "dataWithLength:"
- "defaultRepresentation"
- "fullScreenImage"
- "getBytes:fromOffset:length:error:"
- "imageWithCGImage:"
- "initWithCGImage:"
- "initWithCGImage:scale:orientation:"
- "initWithState:excludeSectionTypes:"
- "initWithTraitCollection:tintColor:deviceClass:"
- "mutableBytes"
- "requestSharedURLForFileOrFolderURL:completionHandler:"
- "setAsset:"
- "setDataProvider:"
- "setThumbnailProvider:"
- "settingsWithSessionContext:presnetationStyle:hostProcessType:customizationGroups:collaborationOptions:cloudShareRequest:"
- "softlink:r:path:/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary"
- "thumbnailProvider"
- "updateHostingController:withContext:hostProcessType:hostPresentationStyle:optionGroups:collaborationOptionsData:cloudShareRequest:"
- "v16@?0@\"ALAsset\"8"
- "v28@?0q8@\"NSString\"16B24"
- "v32@0:8@\"NSString\"16@\"SFShareSheetSessionTestingSnapshot\"24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "valueForProperty:"
- "\xf0\xf03A"

```
