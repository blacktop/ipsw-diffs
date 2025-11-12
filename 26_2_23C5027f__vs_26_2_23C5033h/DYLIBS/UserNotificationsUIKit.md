## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-1003.2.7.0.0
-  __TEXT.__text: 0x1a8320
-  __TEXT.__auth_stubs: 0x28b0
-  __TEXT.__objc_methlist: 0x1a17c
-  __TEXT.__const: 0x4324
-  __TEXT.__gcc_except_tab: 0x2e1c
-  __TEXT.__cstring: 0xd3d6
-  __TEXT.__oslogstring: 0xd6ad
+1003.2.10.100.0
+  __TEXT.__text: 0x1af4d0
+  __TEXT.__auth_stubs: 0x2970
+  __TEXT.__objc_methlist: 0x1a994
+  __TEXT.__const: 0x4354
+  __TEXT.__gcc_except_tab: 0x2f98
+  __TEXT.__cstring: 0xd526
+  __TEXT.__oslogstring: 0xd9ad
   __TEXT.__ustring: 0x22
-  __TEXT.__swift5_typeref: 0x3b88
+  __TEXT.__swift5_typeref: 0x3ba8
   __TEXT.__swift5_fieldmd: 0x1234
   __TEXT.__constg_swiftt: 0x1cc4
   __TEXT.__swift5_reflstr: 0x136e
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0x258
-  __TEXT.__swift5_capture: 0xe98
+  __TEXT.__swift5_capture: 0xeb8
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_proto: 0x170
   __TEXT.__swift5_types: 0x12c
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__unwind_info: 0x70a8
-  __TEXT.__eh_frame: 0xcb8
-  __TEXT.__objc_classname: 0x36b3
-  __TEXT.__objc_methname: 0x44bdd
-  __TEXT.__objc_methtype: 0xbd6f
-  __TEXT.__objc_stubs: 0x277e0
-  __DATA_CONST.__got: 0x17b0
-  __DATA_CONST.__const: 0x40f8
-  __DATA_CONST.__objc_classlist: 0x7b8
+  __TEXT.__unwind_info: 0x7280
+  __TEXT.__eh_frame: 0xcc0
+  __TEXT.__objc_classname: 0x3761
+  __TEXT.__objc_methname: 0x45f41
+  __TEXT.__objc_methtype: 0xbf13
+  __TEXT.__objc_stubs: 0x284e0
+  __DATA_CONST.__got: 0x1808
+  __DATA_CONST.__const: 0x4190
+  __DATA_CONST.__objc_classlist: 0x7e8
   __DATA_CONST.__objc_catlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x5f0
+  __DATA_CONST.__objc_protolist: 0x608
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc5e8
-  __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_superrefs: 0x538
+  __DATA_CONST.__objc_selrefs: 0xc918
+  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x558
   __DATA_CONST.__objc_arraydata: 0x158
-  __AUTH_CONST.__auth_got: 0x1468
-  __AUTH_CONST.__const: 0x5a80
-  __AUTH_CONST.__cfstring: 0x7d80
-  __AUTH_CONST.__objc_const: 0x25548
+  __AUTH_CONST.__auth_got: 0x14c8
+  __AUTH_CONST.__const: 0x5ad0
+  __AUTH_CONST.__cfstring: 0x7e40
+  __AUTH_CONST.__objc_const: 0x263a0
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x2850
-  __AUTH.__data: 0x4d0
-  __DATA.__objc_ivar: 0x1648
-  __DATA.__data: 0x5350
+  __AUTH.__objc_data: 0x2a50
+  __AUTH.__data: 0x500
+  __DATA.__objc_ivar: 0x1714
+  __DATA.__data: 0x5450
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1910
   __DATA.__common: 0x60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 37F0A101-1327-34C7-988B-1BC4A9EF2ADB
-  Functions: 10706
-  Symbols:   28033
-  CStrings:  13544
+  UUID: A668B3AC-6F56-34B5-BDD9-BECAA98E1710
+  Functions: 10906
+  Symbols:   28639
+  CStrings:  13766
 
Symbols:
+ +[NCToggleControl dismissControlWithClearAllText:]
+ +[NCToggleControl showLessControlWithClearAllText:glyphOrientation:]
+ -[NCActionButtonsPresentingView .cxx_destruct]
+ -[NCActionButtonsPresentingView actionButtonsView]
+ -[NCActionButtonsPresentingView defaultActionTriggered]
+ -[NCActionButtonsPresentingView initWithActionButtonsView:interfaceEdge:layoutLocation:]
+ -[NCActionButtonsPresentingView interfaceEdge]
+ -[NCActionButtonsPresentingView layoutLocation]
+ -[NCActionButtonsPresentingView setActionButtonsView:]
+ -[NCActionButtonsPresentingView setDefaultActionTriggered:]
+ -[NCActionButtonsPresentingView setInterfaceEdge:]
+ -[NCActionButtonsPresentingView setLayoutLocation:]
+ -[NCClickInteractionPresentedControl _configureGlass]
+ -[NCClickInteractionPresentedControl _configureGlass].cold.1
+ -[NCClickInteractionPresentedControl initWithTitle:]
+ -[NCClickInteractionPresenter _animatePresentation:completion:]
+ -[NCClickInteractionPresenter _morphTransitionHelper]
+ -[NCClickInteractionPresenter initWithTitle:sourceView:]
+ -[NCClickInteractionPresenter setMorphTransitionHelper:]
+ -[NCGlyphControl .cxx_destruct]
+ -[NCGlyphControl _configureGlassForPresentedView]
+ -[NCGlyphControl _configureGlassForPresentedView].cold.1
+ -[NCGlyphControl _configureGlyphViewIfNecessaryWithImage:]
+ -[NCGlyphControl _configurePresentedViewIfNecessary]
+ -[NCGlyphControl _cornerRadius]
+ -[NCGlyphControl _handleTouchUpInsideWithEvent:]
+ -[NCGlyphControl _sendActionsForEvents:withEvent:]
+ -[NCGlyphControl gestureRecognizerShouldBegin:]
+ -[NCGlyphControl glyphView]
+ -[NCGlyphControl glyph]
+ -[NCGlyphControl init]
+ -[NCGlyphControl layoutSubviews]
+ -[NCGlyphControl presentedView]
+ -[NCGlyphControl setGlyph:]
+ -[NCGlyphControl setGlyphView:]
+ -[NCGlyphControl setHighlighted:]
+ -[NCGlyphControl setPresentedView:]
+ -[NCGlyphControl sizeThatFits:]
+ -[NCNotificationStructuredListViewController _updateListVisibleAreaForSize:reason:]
+ -[NCNotificationStructuredListViewController notificationStructuredListView:didUpdateViewFrame:]
+ -[NCPlatterActionButton .cxx_destruct]
+ -[NCPlatterActionButton _configureBackgroundColoringViewIfNecessary]
+ -[NCPlatterActionButton _configureBackgroundViewIfNecessary]
+ -[NCPlatterActionButton _configureTitleLabelEffects]
+ -[NCPlatterActionButton _configureTitleLabelIfNecessary]
+ -[NCPlatterActionButton _fontProvider]
+ -[NCPlatterActionButton _handleHoverGestureRecognizerEvent:]
+ -[NCPlatterActionButton _layoutBackgroundView]
+ -[NCPlatterActionButton _layoutTitleLabel]
+ -[NCPlatterActionButton _materialBackgroundView]
+ -[NCPlatterActionButton _setFontProvider:]
+ -[NCPlatterActionButton _updateTitleLabelFont]
+ -[NCPlatterActionButton _wordCountForText:]
+ -[NCPlatterActionButton adjustForContentSizeCategoryChange]
+ -[NCPlatterActionButton adjustsFontForContentSizeCategory]
+ -[NCPlatterActionButton backgroundMaterialRecipe]
+ -[NCPlatterActionButton backgroundTintColor]
+ -[NCPlatterActionButton backgroundView]
+ -[NCPlatterActionButton cornerRadius]
+ -[NCPlatterActionButton customBackgroundView]
+ -[NCPlatterActionButton font]
+ -[NCPlatterActionButton initWithFrame:]
+ -[NCPlatterActionButton isBackgroundGlass]
+ -[NCPlatterActionButton layoutSubviews]
+ -[NCPlatterActionButton materialGroupNameBase]
+ -[NCPlatterActionButton preferredContentSizeCategory]
+ -[NCPlatterActionButton setAdjustsFontForContentSizeCategory:]
+ -[NCPlatterActionButton setBackgroundMaterialRecipe:]
+ -[NCPlatterActionButton setBackgroundTintColor:]
+ -[NCPlatterActionButton setBackgroundView:]
+ -[NCPlatterActionButton setCornerRadius:]
+ -[NCPlatterActionButton setCustomBackgroundView:]
+ -[NCPlatterActionButton setFont:]
+ -[NCPlatterActionButton setHighlighted:]
+ -[NCPlatterActionButton setIsBackgroundGlass:]
+ -[NCPlatterActionButton setMaterialGroupNameBase:]
+ -[NCPlatterActionButton setPreferredContentSizeCategory:]
+ -[NCPlatterActionButton setTextColor:]
+ -[NCPlatterActionButton setTitle:]
+ -[NCPlatterActionButton setTitleAlpha:]
+ -[NCPlatterActionButton setTitleLabel:]
+ -[NCPlatterActionButton setTitleLabelVisualStylingProvider:]
+ -[NCPlatterActionButton sizeThatFits:]
+ -[NCPlatterActionButton textColor]
+ -[NCPlatterActionButton titleAlpha]
+ -[NCPlatterActionButton titleLabelVisualStylingProvider]
+ -[NCPlatterActionButton titleLabel]
+ -[NCPlatterActionButton title]
+ -[NCPlatterActionButton willMoveToSuperview:]
+ -[NCPlatterActionButtonsView .cxx_destruct]
+ -[NCPlatterActionButtonsView _hideNonDefaultActionButtons]
+ -[NCPlatterActionButtonsView _layoutButtonsStackView]
+ -[NCPlatterActionButtonsView _layoutClippingView]
+ -[NCPlatterActionButtonsView _maxAllowedButtonWidth]
+ -[NCPlatterActionButtonsView _performNonDefaultActionButtonsHideRevealAnimation:]
+ -[NCPlatterActionButtonsView _revealNonDefaultActionButtons]
+ -[NCPlatterActionButtonsView _widthMultipleForVerticallyStackedButtonsWithCount:]
+ -[NCPlatterActionButtonsView actionButtonCount]
+ -[NCPlatterActionButtonsView adjustForContentSizeCategoryChange]
+ -[NCPlatterActionButtonsView adjustsFontForContentSizeCategory]
+ -[NCPlatterActionButtonsView backgroundMaterialRecipe]
+ -[NCPlatterActionButtonsView backgroundTintColor]
+ -[NCPlatterActionButtonsView buttonsStackView]
+ -[NCPlatterActionButtonsView clippingView]
+ -[NCPlatterActionButtonsView customBackgroundView]
+ -[NCPlatterActionButtonsView defaultActionButton]
+ -[NCPlatterActionButtonsView defaultAction]
+ -[NCPlatterActionButtonsView defaultWidth]
+ -[NCPlatterActionButtonsView glassLuminance]
+ -[NCPlatterActionButtonsView hasGlassBackground]
+ -[NCPlatterActionButtonsView highlightDefaultActionButton]
+ -[NCPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:glassLuminance:]
+ -[NCPlatterActionButtonsView isVerticallyStacked]
+ -[NCPlatterActionButtonsView layoutSubviews]
+ -[NCPlatterActionButtonsView materialGroupNameBase]
+ -[NCPlatterActionButtonsView senderForActionWithIdentifier:]
+ -[NCPlatterActionButtonsView setAdjustsFontForContentSizeCategory:]
+ -[NCPlatterActionButtonsView setBackgroundMaterialRecipe:]
+ -[NCPlatterActionButtonsView setBackgroundTintColor:]
+ -[NCPlatterActionButtonsView setClippingView:]
+ -[NCPlatterActionButtonsView setCustomBackgroundView:]
+ -[NCPlatterActionButtonsView setDefaultActionButton:]
+ -[NCPlatterActionButtonsView setHasGlassBackground:]
+ -[NCPlatterActionButtonsView setHighlightDefaultActionButton:]
+ -[NCPlatterActionButtonsView setMaterialGroupNameBase:]
+ -[NCPlatterActionButtonsView setStretchedWidth:]
+ -[NCPlatterActionButtonsView setTextColor:]
+ -[NCPlatterActionButtonsView sizeThatFits:]
+ -[NCPlatterActionButtonsView stretchedWidth]
+ -[NCPlatterActionButtonsView textColor]
+ -[NCPlatterActionButtonsView willMoveToSuperview:]
+ -[NCSwipeInteraction .cxx_destruct]
+ -[NCSwipeInteraction _actionButtonTriggerDistanceForView:]
+ -[NCSwipeInteraction _actuateFeedbackForDefaultActionLockedIfNecessary]
+ -[NCSwipeInteraction _actuateFeedbackForDefaultActionUnlockedIfNecessary]
+ -[NCSwipeInteraction _addActionButtonViewsAtLayoutLocation:interfaceEdge:]
+ -[NCSwipeInteraction _addActionButtonViewsAtLayoutLocation:interfaceEdge:].cold.1
+ -[NCSwipeInteraction _addActionButtonViewsAtLayoutLocation:interfaceEdge:].cold.2
+ -[NCSwipeInteraction _addActionButtonViewsAtLayoutLocation:interfaceEdge:].cold.3
+ -[NCSwipeInteraction _addActionButtonViewsAtLayoutLocation:interfaceEdge:].cold.4
+ -[NCSwipeInteraction _addActionButtonsAndRevealAnimated:fastAnimation:layoutLocation:completion:]
+ -[NCSwipeInteraction _handlePanGesture:]
+ -[NCSwipeInteraction _hideAnimated:fastAnimation:velocity:completion:]
+ -[NCSwipeInteraction _interfaceEdgeForLayoutLocation:]
+ -[NCSwipeInteraction _interfaceEdgeToPresentOnForAbsoluteTranslation:]
+ -[NCSwipeInteraction _interfaceEdgeToPresentOnForComparisonValue:]
+ -[NCSwipeInteraction _interfaceEdgeToPresentOnForInitialPanTranslation:andInitialPanVelocity:]
+ -[NCSwipeInteraction _layoutLocationForInterfaceEdge:]
+ -[NCSwipeInteraction _panHorizontalTranslation]
+ -[NCSwipeInteraction _panHorizontalVelocity]
+ -[NCSwipeInteraction _panLocation]
+ -[NCSwipeInteraction _performSwipeHintingForLayoutLocation:]
+ -[NCSwipeInteraction _removeActionButtons]
+ -[NCSwipeInteraction _revealToPosition:animated:fastAnimation:velocity:completion:]
+ -[NCSwipeInteraction _setViewPosition:withVelocity:usingNonInteractiveSpring:animated:completion:]
+ -[NCSwipeInteraction _setViewPositionHelper:withVelocity:usingNonInteractiveSpring:animated:completion:]
+ -[NCSwipeInteraction _setupContentOffsetFloatAnimatableProperty]
+ -[NCSwipeInteraction _shouldContinuePresentingActionButtons]
+ -[NCSwipeInteraction _updateActionButtonRevealPercentageForTargetPosition:]
+ -[NCSwipeInteraction _updateActionRevealStateForTargetPosition:currentPosition:velocity:]
+ -[NCSwipeInteraction _updatePosition:]
+ -[NCSwipeInteraction _updateRevealPercentage:]
+ -[NCSwipeInteraction _updateTargetPosition:]
+ -[NCSwipeInteraction defaultActionFeedbackGenerator]
+ -[NCSwipeInteraction delegate]
+ -[NCSwipeInteraction didMoveToView:]
+ -[NCSwipeInteraction didPlayHaptic]
+ -[NCSwipeInteraction gestureRecognizerShouldBegin:]
+ -[NCSwipeInteraction hideActionsAnimated:fastAnimation:completion:]
+ -[NCSwipeInteraction hintActionsForLayoutLocation:]
+ -[NCSwipeInteraction initWithDelegate:]
+ -[NCSwipeInteraction isPerformingSwipeHinting]
+ -[NCSwipeInteraction materialGroupNameBase]
+ -[NCSwipeInteraction revealActionsForLayoutLocation:completion:]
+ -[NCSwipeInteraction senderForActionWithIdentifier:]
+ -[NCSwipeInteraction setDefaultActionFeedbackGenerator:]
+ -[NCSwipeInteraction setDidPlayHaptic:]
+ -[NCSwipeInteraction setMaterialGroupNameBase:]
+ -[NCSwipeInteraction setPerformingSwipeHinting:]
+ -[NCSwipeInteraction setView:]
+ -[NCSwipeInteraction setViewToMove:]
+ -[NCSwipeInteraction viewToMove]
+ -[NCSwipeInteraction view]
+ -[NCSwipeInteraction willMoveToView:]
+ GCC_except_table197
+ GCC_except_table37
+ GCC_except_table76
+ GCC_except_table81
+ GCC_except_table98
+ _CFLocaleCopyCurrent
+ _CFStringGetLength
+ _CFStringTokenizerAdvanceToNextToken
+ _CFStringTokenizerCreate
+ _NCUILogSwipeInteraction
+ _OBJC_CLASS_$_NCActionButtonsPresentingView
+ _OBJC_CLASS_$_NCGlyphControl
+ _OBJC_CLASS_$_NCMorphTransitionHelper
+ _OBJC_CLASS_$_NCPlatterActionButton
+ _OBJC_CLASS_$_NCPlatterActionButtonsView
+ _OBJC_CLASS_$_NCSwipeInteraction
+ _OBJC_CLASS_$_UIHoverGestureRecognizer
+ _OBJC_CLASS_$_UIPanGestureRecognizer
+ _OBJC_CLASS_$__UIStatesFeedbackGenerator
+ _OBJC_IVAR_$_NCActionButtonsPresentingView._actionButtonsView
+ _OBJC_IVAR_$_NCActionButtonsPresentingView._defaultActionTriggered
+ _OBJC_IVAR_$_NCActionButtonsPresentingView._interfaceEdge
+ _OBJC_IVAR_$_NCActionButtonsPresentingView._layoutLocation
+ _OBJC_IVAR_$_NCClickInteractionPresenter._morphTransitionHelper
+ _OBJC_IVAR_$_NCGlyphControl._glyphView
+ _OBJC_IVAR_$_NCGlyphControl._presentedView
+ _OBJC_IVAR_$_NCPlatterActionButton._adjustsFontForContentSizeCategory
+ _OBJC_IVAR_$_NCPlatterActionButton._backgroundMaterialRecipe
+ _OBJC_IVAR_$_NCPlatterActionButton._backgroundTintColor
+ _OBJC_IVAR_$_NCPlatterActionButton._backgroundTintColoringView
+ _OBJC_IVAR_$_NCPlatterActionButton._backgroundView
+ _OBJC_IVAR_$_NCPlatterActionButton._cornerRadius
+ _OBJC_IVAR_$_NCPlatterActionButton._customBackgroundView
+ _OBJC_IVAR_$_NCPlatterActionButton._font
+ _OBJC_IVAR_$_NCPlatterActionButton._fontProvider
+ _OBJC_IVAR_$_NCPlatterActionButton._isBackgroundGlass
+ _OBJC_IVAR_$_NCPlatterActionButton._materialGroupNameBase
+ _OBJC_IVAR_$_NCPlatterActionButton._preferredContentSizeCategory
+ _OBJC_IVAR_$_NCPlatterActionButton._textColor
+ _OBJC_IVAR_$_NCPlatterActionButton._title
+ _OBJC_IVAR_$_NCPlatterActionButton._titleAlpha
+ _OBJC_IVAR_$_NCPlatterActionButton._titleLabel
+ _OBJC_IVAR_$_NCPlatterActionButton._titleLabelVisualStylingProvider
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._adjustsFontForContentSizeCategory
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._backgroundMaterialRecipe
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._backgroundTintColor
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._buttonsStackView
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._clippingView
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._customBackgroundView
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._defaultAction
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._defaultActionButton
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._defaultWidth
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._glassLuminance
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._hasGlassBackground
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._highlightDefaultActionButton
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._materialGroupNameBase
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._stretchedWidth
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._textColor
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._verticallyStacked
+ _OBJC_IVAR_$_NCSwipeInteraction._actionButtonsPresentingView
+ _OBJC_IVAR_$_NCSwipeInteraction._animationCompletion
+ _OBJC_IVAR_$_NCSwipeInteraction._animationCount
+ _OBJC_IVAR_$_NCSwipeInteraction._defaultActionFeedbackGenerator
+ _OBJC_IVAR_$_NCSwipeInteraction._delegate
+ _OBJC_IVAR_$_NCSwipeInteraction._didPlayHaptic
+ _OBJC_IVAR_$_NCSwipeInteraction._materialGroupNameBase
+ _OBJC_IVAR_$_NCSwipeInteraction._panGestureRecognizer
+ _OBJC_IVAR_$_NCSwipeInteraction._panGestureStartingPosition
+ _OBJC_IVAR_$_NCSwipeInteraction._performWithoutRetargetingAnimationCompletion
+ _OBJC_IVAR_$_NCSwipeInteraction._performingSwipeHinting
+ _OBJC_IVAR_$_NCSwipeInteraction._swipeHintingHideAnimationBlock
+ _OBJC_IVAR_$_NCSwipeInteraction._targetPositionAnimatableProperty
+ _OBJC_IVAR_$_NCSwipeInteraction._view
+ _OBJC_IVAR_$_NCSwipeInteraction._viewToMove
+ _OBJC_METACLASS_$_NCActionButtonsPresentingView
+ _OBJC_METACLASS_$_NCGlyphControl
+ _OBJC_METACLASS_$_NCMorphTransitionHelper
+ _OBJC_METACLASS_$_NCPlatterActionButton
+ _OBJC_METACLASS_$_NCPlatterActionButtonsView
+ _OBJC_METACLASS_$_NCSwipeInteraction
+ __DATA_NCMorphTransitionHelper
+ __INSTANCE_METHODS_NCMorphTransitionHelper
+ __IVARS_NCMorphTransitionHelper
+ __METACLASS_DATA_NCMorphTransitionHelper
+ __OBJC_$_INSTANCE_METHODS_NCActionButtonsPresentingView
+ __OBJC_$_INSTANCE_METHODS_NCGlyphControl
+ __OBJC_$_INSTANCE_METHODS_NCPlatterActionButton
+ __OBJC_$_INSTANCE_METHODS_NCPlatterActionButtonsView
+ __OBJC_$_INSTANCE_METHODS_NCSwipeInteraction
+ __OBJC_$_INSTANCE_VARIABLES_NCActionButtonsPresentingView
+ __OBJC_$_INSTANCE_VARIABLES_NCGlyphControl
+ __OBJC_$_INSTANCE_VARIABLES_NCPlatterActionButton
+ __OBJC_$_INSTANCE_VARIABLES_NCPlatterActionButtonsView
+ __OBJC_$_INSTANCE_VARIABLES_NCSwipeInteraction
+ __OBJC_$_PROP_LIST_NCActionButtonsPresentingView
+ __OBJC_$_PROP_LIST_NCClickInteractionPresentableView
+ __OBJC_$_PROP_LIST_NCGlyphControl
+ __OBJC_$_PROP_LIST_NCPlatterActionButton
+ __OBJC_$_PROP_LIST_NCPlatterActionButtonsView
+ __OBJC_$_PROP_LIST_NCSwipeInteraction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NCClickInteractionPresentableView
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NCClickInteractionPresentableView
+ __OBJC_$_PROTOCOL_REFS_NCClickInteractionPresentableView
+ __OBJC_$_PROTOCOL_REFS__UIMorphable
+ __OBJC_CLASS_PROTOCOLS_$_NCPlatterActionButton
+ __OBJC_CLASS_PROTOCOLS_$_NCPlatterActionButtonsView
+ __OBJC_CLASS_PROTOCOLS_$_NCSwipeInteraction
+ __OBJC_CLASS_RO_$_NCActionButtonsPresentingView
+ __OBJC_CLASS_RO_$_NCGlyphControl
+ __OBJC_CLASS_RO_$_NCPlatterActionButton
+ __OBJC_CLASS_RO_$_NCPlatterActionButtonsView
+ __OBJC_CLASS_RO_$_NCSwipeInteraction
+ __OBJC_LABEL_PROTOCOL_$_NCClickInteractionPresentableView
+ __OBJC_LABEL_PROTOCOL_$__UIMorphable
+ __OBJC_METACLASS_RO_$_NCActionButtonsPresentingView
+ __OBJC_METACLASS_RO_$_NCGlyphControl
+ __OBJC_METACLASS_RO_$_NCPlatterActionButton
+ __OBJC_METACLASS_RO_$_NCPlatterActionButtonsView
+ __OBJC_METACLASS_RO_$_NCSwipeInteraction
+ __OBJC_PROTOCOL_$_NCClickInteractionPresentableView
+ __OBJC_PROTOCOL_$__UIMorphable
+ __UISolariumEnabled
+ __UIStatesFeedbackGeneratorSwipeActionStateConfirm
+ __UIStatesFeedbackGeneratorSwipeActionStateOpen
+ ___104-[NCSwipeInteraction _setViewPositionHelper:withVelocity:usingNonInteractiveSpring:animated:completion:]_block_invoke
+ ___104-[NCSwipeInteraction _setViewPositionHelper:withVelocity:usingNonInteractiveSpring:animated:completion:]_block_invoke_2
+ ___162-[NCPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:glassLuminance:]_block_invoke
+ ___40-[NCPlatterActionButton setHighlighted:]_block_invoke
+ ___40-[NCSwipeInteraction _handlePanGesture:]_block_invoke
+ ___58-[NCPlatterActionButtonsView _hideNonDefaultActionButtons]_block_invoke
+ ___58-[NCPlatterActionButtonsView _hideNonDefaultActionButtons]_block_invoke_2
+ ___60-[NCPlatterActionButton _handleHoverGestureRecognizerEvent:]_block_invoke
+ ___60-[NCPlatterActionButton _handleHoverGestureRecognizerEvent:]_block_invoke_2
+ ___60-[NCPlatterActionButtonsView _revealNonDefaultActionButtons]_block_invoke
+ ___60-[NCPlatterActionButtonsView _revealNonDefaultActionButtons]_block_invoke_2
+ ___60-[NCPlatterActionButtonsView senderForActionWithIdentifier:]_block_invoke
+ ___60-[NCPlatterActionButtonsView senderForActionWithIdentifier:]_block_invoke_2
+ ___60-[NCSwipeInteraction _performSwipeHintingForLayoutLocation:]_block_invoke
+ ___63-[NCClickInteractionPresenter _animatePresentation:completion:]_block_invoke
+ ___63-[NCClickInteractionPresenter _animatePresentation:completion:]_block_invoke_2
+ ___64-[NCPlatterActionButtonsView adjustForContentSizeCategoryChange]_block_invoke
+ ___64-[NCSwipeInteraction _setupContentOffsetFloatAnimatableProperty]_block_invoke
+ ___64-[NCSwipeInteraction revealActionsForLayoutLocation:completion:]_block_invoke
+ ___67-[NCPlatterActionButtonsView setAdjustsFontForContentSizeCategory:]_block_invoke
+ ___70-[NCSwipeInteraction _hideAnimated:fastAnimation:velocity:completion:]_block_invoke
+ ___83-[NCSwipeInteraction _revealToPosition:animated:fastAnimation:velocity:completion:]_block_invoke
+ ___98-[NCSwipeInteraction _setViewPosition:withVelocity:usingNonInteractiveSpring:animated:completion:]_block_invoke
+ ___block_descriptor_33_e55_v32?0"UIView<PLContentSizeCategoryAdjusting>"8Q16^B24l
+ ___block_descriptor_40_e8_32r_e55_v32?0"UIView<PLContentSizeCategoryAdjusting>"8Q16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e16_B16?0"UIView"8ls32l8
+ ___block_descriptor_48_e8_32s40r_e31_v48?0"UIAction"816:24Q32^B40ls32l8r40l8
+ ___block_descriptor_56_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _flat unique So12_UIMorphable_p
+ _kCFAllocatorDefault
+ _objc_msgSend$_actionButtonTriggerDistanceForView:
+ _objc_msgSend$_actuateFeedbackForDefaultActionLockedIfNecessary
+ _objc_msgSend$_addActionButtonViewsAtLayoutLocation:interfaceEdge:
+ _objc_msgSend$_addActionButtonsAndRevealAnimated:fastAnimation:layoutLocation:completion:
+ _objc_msgSend$_animatePresentation:completion:
+ _objc_msgSend$_configureBackgroundColoringViewIfNecessary
+ _objc_msgSend$_configureGlass
+ _objc_msgSend$_configureGlassForPresentedView
+ _objc_msgSend$_configureGlyphViewIfNecessaryWithImage:
+ _objc_msgSend$_configurePresentedViewIfNecessary
+ _objc_msgSend$_configureTitleLabelEffects
+ _objc_msgSend$_handleTouchUpInsideWithEvent:
+ _objc_msgSend$_hideAnimated:fastAnimation:velocity:completion:
+ _objc_msgSend$_hideNonDefaultActionButtons
+ _objc_msgSend$_interfaceEdgeForLayoutLocation:
+ _objc_msgSend$_interfaceEdgeToPresentOnForAbsoluteTranslation:
+ _objc_msgSend$_interfaceEdgeToPresentOnForComparisonValue:
+ _objc_msgSend$_interfaceEdgeToPresentOnForInitialPanTranslation:andInitialPanVelocity:
+ _objc_msgSend$_layoutButtonsStackView
+ _objc_msgSend$_layoutClippingView
+ _objc_msgSend$_layoutLocationForInterfaceEdge:
+ _objc_msgSend$_materialBackgroundView
+ _objc_msgSend$_maxAllowedButtonWidth
+ _objc_msgSend$_panHorizontalTranslation
+ _objc_msgSend$_panHorizontalVelocity
+ _objc_msgSend$_panLocation
+ _objc_msgSend$_performNonDefaultActionButtonsHideRevealAnimation:
+ _objc_msgSend$_performSwipeHintingForLayoutLocation:
+ _objc_msgSend$_performWithoutRetargetingAnimations:
+ _objc_msgSend$_presentedView
+ _objc_msgSend$_removeActionButtons
+ _objc_msgSend$_revealNonDefaultActionButtons
+ _objc_msgSend$_revealToPosition:animated:fastAnimation:velocity:completion:
+ _objc_msgSend$_setAllowedScrollTypesMask:
+ _objc_msgSend$_setCanPanVertically:
+ _objc_msgSend$_setViewPosition:withVelocity:usingNonInteractiveSpring:animated:completion:
+ _objc_msgSend$_setViewPositionHelper:withVelocity:usingNonInteractiveSpring:animated:completion:
+ _objc_msgSend$_setupContentOffsetFloatAnimatableProperty
+ _objc_msgSend$_shouldContinuePresentingActionButtons
+ _objc_msgSend$_updateActionButtonRevealPercentageForTargetPosition:
+ _objc_msgSend$_updateActionRevealStateForTargetPosition:currentPosition:velocity:
+ _objc_msgSend$_updateListVisibleAreaForSize:reason:
+ _objc_msgSend$_updatePosition:
+ _objc_msgSend$_updateRevealPercentage:
+ _objc_msgSend$_updateTargetPosition:
+ _objc_msgSend$_updateTitleLabelFont
+ _objc_msgSend$_widthMultipleForVerticallyStackedButtonsWithCount:
+ _objc_msgSend$_wordCountForText:
+ _objc_msgSend$actionButtonCount
+ _objc_msgSend$actionButtonsView
+ _objc_msgSend$animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:
+ _objc_msgSend$arrangedSubviews
+ _objc_msgSend$buttonCustomBackgroundViewForSwipeInteraction:
+ _objc_msgSend$buttonsCornerRadiusForSwipeInteraction:
+ _objc_msgSend$buttonsGlassBackgroundIdForSwipeInteraction:
+ _objc_msgSend$buttonsGlassBackgroundSmoothnessForSwipeInteraction:
+ _objc_msgSend$buttonsGlassBackgroundStateForSwipeInteraction:
+ _objc_msgSend$buttonsGlassLuminanceForSwipeInteraction:
+ _objc_msgSend$buttonsRecipeForSwipeInteraction:
+ _objc_msgSend$buttonsStackView
+ _objc_msgSend$buttonsTextColorForSwipeInteraction:
+ _objc_msgSend$buttonsTintColorForSwipeInteraction:
+ _objc_msgSend$customBackgroundView
+ _objc_msgSend$defaultActionButton
+ _objc_msgSend$defaultActionTriggered
+ _objc_msgSend$defaultWidth
+ _objc_msgSend$didPlayHaptic
+ _objc_msgSend$dismissControlWithClearAllText:
+ _objc_msgSend$enumerateEventHandlers:
+ _objc_msgSend$glassLuminance
+ _objc_msgSend$glyphView
+ _objc_msgSend$groupNameBase
+ _objc_msgSend$hasGlassBackground
+ _objc_msgSend$initWithActionButtonsView:interfaceEdge:layoutLocation:
+ _objc_msgSend$initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:glassLuminance:
+ _objc_msgSend$initWithStyle:view:
+ _objc_msgSend$initWithTitle:sourceView:
+ _objc_msgSend$initWithVariant:size:smoothness:subdued:
+ _objc_msgSend$initWithViews:
+ _objc_msgSend$interfaceEdge
+ _objc_msgSend$isPerformingSwipeHinting
+ _objc_msgSend$isVerticallyStacked
+ _objc_msgSend$layoutLocation
+ _objc_msgSend$layoutMarginsGuide
+ _objc_msgSend$morphToViews:alongsideAnimation:completion:
+ _objc_msgSend$presentedView
+ _objc_msgSend$recipe
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$sendActionsForControlEvents:
+ _objc_msgSend$setActive:
+ _objc_msgSend$setAllowsGrouping:
+ _objc_msgSend$setCustomBackgroundView:
+ _objc_msgSend$setDefaultActionButton:
+ _objc_msgSend$setDefaultActionTriggered:
+ _objc_msgSend$setDidPlayHaptic:
+ _objc_msgSend$setHighlightDefaultActionButton:
+ _objc_msgSend$setIsBackgroundGlass:
+ _objc_msgSend$setMorphTransitionHelper:
+ _objc_msgSend$setPerformingSwipeHinting:
+ _objc_msgSend$setStretchedWidth:
+ _objc_msgSend$setTitleAlpha:
+ _objc_msgSend$setViewToMove:
+ _objc_msgSend$shouldContinuePresentingActionButtonsForSwipeInteraction:
+ _objc_msgSend$shouldVerticallyStackButtonsForSwipeInteraction:
+ _objc_msgSend$showLessControlWithClearAllText:glyphOrientation:
+ _objc_msgSend$spacing
+ _objc_msgSend$stretchedWidth
+ _objc_msgSend$swipeInteraction:actionsToRevealFromLayoutLocation:
+ _objc_msgSend$swipeInteraction:didMoveToNewXPosition:
+ _objc_msgSend$swipeInteraction:shouldRevealActionsFromLayoutLocation:
+ _objc_msgSend$swipeInteractionDidBeginHidingActions:
+ _objc_msgSend$swipeInteractionDidBeginRevealingActions:
+ _objc_msgSend$swipeInteractionDidCompleteHidingActions:
+ _objc_msgSend$swipeInteractionDidCompleteRevealingActions:
+ _objc_msgSend$swipeInteractionDidSignificantUserInteraction:
+ _objc_msgSend$tertiarySystemFillColor
+ _objc_msgSend$transitionToState:ended:atLocation:
+ _objc_msgSend$translationInView:
+ _objc_msgSend$viewToMove
+ _objc_msgSend$viewToMoveForSwipeInteraction:
+ _symbolic ______p So12_UIMorphableP
- +[NCToggleControl dismissControlWithMaterialRecipe:clearAllText:]
- +[NCToggleControl showLessControlWithMaterialRecipe:clearAllText:glyphOrientation:]
- -[NCClickInteractionPresentedControl _backgroundMaterialView]
- -[NCClickInteractionPresentedControl _configureMaterialViewsIfNecessary]
- -[NCClickInteractionPresentedControl _materialRecipe]
- -[NCClickInteractionPresentedControl _newMaterialViewWithRecipe:]
- -[NCClickInteractionPresentedControl initWithTitle:materialRecipe:]
- -[NCClickInteractionPresenter _animatePresentation:cancelled:completion:]
- -[NCClickInteractionPresenter _frictionForTransitionPresentation:cancelled:]
- -[NCClickInteractionPresenter _tensionForTransitionPresentation:cancelled:]
- -[NCClickInteractionPresenter initWithTitle:sourceView:materialRecipe:]
- -[NCClickInteractionPresenter materialRecipe]
- -[NCNotificationStructuredListViewController _updateListVisibleAreaForSize:]
- -[NCNotificationSummarizedInlineExpandingSectionList materialGroupNameBaseForNotificationSummaryExpandedHeaderView:]
- -[NCToggleControl _updateTitleLabelVisualStyling]
- -[NCToggleControl setVisualStyle:]
- -[NCToggleControlPair materialGroupNameBase]
- -[NCToggleControlPair setMaterialGroupNameBase:]
- GCC_except_table196
- GCC_except_table68
- GCC_except_table77
- GCC_except_table82
- GCC_except_table97
- _OBJC_CLASS_$_PLGlyphControl
- _OBJC_IVAR_$_NCClickInteractionPresentedControl._backgroundMaterialView
- _OBJC_IVAR_$_NCClickInteractionPresentedControl._materialRecipe
- _OBJC_IVAR_$_NCClickInteractionPresenter._materialRecipe
- _OBJC_IVAR_$_NCToggleControlPair._materialGroupNameBase
- _OBJC_METACLASS_$_PLGlyphControl
- ___53-[NCClickInteractionPresentedControl setHighlighted:]_block_invoke
- ___53-[NCClickInteractionPresenter _setUpPresentedControl]_block_invoke
- ___73-[NCClickInteractionPresenter _animatePresentation:cancelled:completion:]_block_invoke
- ___73-[NCClickInteractionPresenter _animatePresentation:cancelled:completion:]_block_invoke_2
- ___block_descriptor_49_e8_32bs40w_e11_v16?0B8B12lw40l8s32l8
- ___block_descriptor_73_e8_32w_e5_v8?0lw32l8
- _objc_msgSend$_animatePresentation:cancelled:completion:
- _objc_msgSend$_configureMaterialViewsIfNecessary
- _objc_msgSend$_frictionForTransitionPresentation:cancelled:
- _objc_msgSend$_glyphView
- _objc_msgSend$_newMaterialViewWithRecipe:
- _objc_msgSend$_tensionForTransitionPresentation:cancelled:
- _objc_msgSend$_updateListVisibleAreaForSize:
- _objc_msgSend$_updateVisualStylingOfView:
- _objc_msgSend$dismissControlWithMaterialRecipe:clearAllText:
- _objc_msgSend$initWithMaterialRecipe:
- _objc_msgSend$initWithTitle:materialRecipe:
- _objc_msgSend$initWithTitle:sourceView:materialRecipe:
- _objc_msgSend$materialGroupNameBaseForNotificationSummaryExpandedHeaderView:
- _objc_msgSend$setBlurEnabled:
- _objc_msgSend$setVisualStyle:
- _objc_msgSend$showLessControlWithMaterialRecipe:clearAllText:glyphOrientation:
CStrings:
+ "%{public}@ presentedView is not setup before glass configruation."
+ "%{public}@: Cannot infer which side to reveal actions. Gesture translation: %f velocity: %f"
+ "%{public}@: Denying pan gesture. Pan gesture translation and velocity are both 0. Cannot infer edge to reveal action buttons on."
+ "%{public}@: Denying pan gesture. recognizerMatches: %{public}d actionsRevealed: %{public}d"
+ "%{public}@: Must provide 4 or less actions per location"
+ "%{public}@: Must provide actions for reveal"
+ "%{public}@: Must provide only one UIAction with defaultAction=YES per location"
+ "%{public}@: Must provide view to present actions in"
+ "@\"<NCSwipeInteractionDelegate>\""
+ "@\"NCActionButtonsPresentingView\""
+ "@\"NCGlyphControl\""
+ "@\"NCMorphTransitionHelper\""
+ "@\"NCPlatterActionButton\""
+ "@\"NCPlatterActionButtonsView\""
+ "@\"UIFont\""
+ "@\"UIView<NCClickInteractionPresentableView>\""
+ "@\"_UIStatesFeedbackGenerator\""
+ "@104@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48d56B64B68Q72d80q88d96"
+ "@40@0:8@16Q24Q32"
+ "B16@?0@\"UIView\"8"
+ "NCActionButtonsPresentingView"
+ "NCClickInteractionPresentableView"
+ "NCGlyphControl"
+ "NCMorphTransitionHelper"
+ "NCPlatterActionButton"
+ "NCPlatterActionButtonsView"
+ "NCSwipeInteraction"
+ "Q24@0:8d16"
+ "T@\"<NCSwipeInteractionDelegate>\",R,W,N,V_delegate"
+ "T@\"MTVisualStylingProvider\",&,N,V_titleLabelVisualStylingProvider"
+ "T@\"NCMorphTransitionHelper\",&,N,G_morphTransitionHelper,V_morphTransitionHelper"
+ "T@\"NCPlatterActionButton\",&,N,V_defaultActionButton"
+ "T@\"NCPlatterActionButtonsView\",&,N,V_actionButtonsView"
+ "T@\"UIAction\",R,N,V_defaultAction"
+ "T@\"UIColor\",&,N,V_backgroundTintColor"
+ "T@\"UIColor\",C,N,V_backgroundTintColor"
+ "T@\"UIColor\",C,N,V_textColor"
+ "T@\"UIFont\",C,N,V_font"
+ "T@\"UIImage\",C,N"
+ "T@\"UIImageView\",&,N,V_glyphView"
+ "T@\"UIStackView\",R,N,V_buttonsStackView"
+ "T@\"UIView\",&,N,V_clippingView"
+ "T@\"UIView\",&,N,V_presentedView"
+ "T@\"UIView\",C,N,V_customBackgroundView"
+ "T@\"UIView\",W,N,V_view"
+ "T@\"UIView\",W,N,V_viewToMove"
+ "T@\"UIView<NCClickInteractionPresentableView>\",R,W,N,V_sourceView"
+ "T@\"_UIStatesFeedbackGenerator\",&,N,V_defaultActionFeedbackGenerator"
+ "TB,N,GisPerformingSwipeHinting,V_performingSwipeHinting"
+ "TB,N,V_defaultActionTriggered"
+ "TB,N,V_didPlayHaptic"
+ "TB,N,V_hasGlassBackground"
+ "TB,N,V_highlightDefaultActionButton"
+ "TB,N,V_isBackgroundGlass"
+ "TB,R,N,GisVerticallyStacked,V_verticallyStacked"
+ "TQ,N,V_interfaceEdge"
+ "TQ,N,V_layoutLocation"
+ "Td,N,V_cornerRadius"
+ "Td,N,V_stretchedWidth"
+ "Td,N,V_titleAlpha"
+ "Td,R,N,V_defaultWidth"
+ "Td,R,N,V_glassLuminance"
+ "Tq,N,V_backgroundMaterialRecipe"
+ "_UIMorphable"
+ "_actionButtonTriggerDistanceForView:"
+ "_actionButtonsPresentingView"
+ "_actionButtonsView"
+ "_actuateFeedbackForDefaultActionLockedIfNecessary"
+ "_actuateFeedbackForDefaultActionUnlockedIfNecessary"
+ "_addActionButtonViewsAtLayoutLocation:interfaceEdge:"
+ "_addActionButtonsAndRevealAnimated:fastAnimation:layoutLocation:completion:"
+ "_animatePresentation:completion:"
+ "_animationCompletion"
+ "_animationCount"
+ "_backgroundMaterialRecipe"
+ "_backgroundTintColor"
+ "_backgroundTintColoringView"
+ "_buttonsStackView"
+ "_configureBackgroundColoringViewIfNecessary"
+ "_configureGlass"
+ "_configureGlassForPresentedView"
+ "_configureGlyphViewIfNecessaryWithImage:"
+ "_configurePresentedViewIfNecessary"
+ "_configureTitleLabelEffects"
+ "_customBackgroundView"
+ "_defaultActionButton"
+ "_defaultActionFeedbackGenerator"
+ "_defaultActionTriggered"
+ "_defaultWidth"
+ "_didPlayHaptic"
+ "_glassLuminance"
+ "_handleHoverGestureRecognizerEvent:"
+ "_handlePanGesture:"
+ "_hasGlassBackground"
+ "_hideAnimated:fastAnimation:velocity:completion:"
+ "_hideNonDefaultActionButtons"
+ "_highlightDefaultActionButton"
+ "_interfaceEdge"
+ "_interfaceEdgeForLayoutLocation:"
+ "_interfaceEdgeToPresentOnForAbsoluteTranslation:"
+ "_interfaceEdgeToPresentOnForComparisonValue:"
+ "_interfaceEdgeToPresentOnForInitialPanTranslation:andInitialPanVelocity:"
+ "_isBackgroundGlass"
+ "_layoutButtonsStackView"
+ "_layoutClippingView"
+ "_layoutLocation"
+ "_layoutLocationForInterfaceEdge:"
+ "_materialBackgroundView"
+ "_maxAllowedButtonWidth"
+ "_morphTransitionHelper"
+ "_panGestureRecognizer"
+ "_panGestureStartingPosition"
+ "_panHorizontalTranslation"
+ "_panHorizontalVelocity"
+ "_panLocation"
+ "_performNonDefaultActionButtonsHideRevealAnimation:"
+ "_performSwipeHintingForLayoutLocation:"
+ "_performWithoutRetargetingAnimationCompletion"
+ "_performingSwipeHinting"
+ "_removeActionButtons"
+ "_revealNonDefaultActionButtons"
+ "_revealToPosition:animated:fastAnimation:velocity:completion:"
+ "_scrollState ignoring schedule animation; current scrollState: %{public}s"
+ "_setAllowedScrollTypesMask:"
+ "_setCanPanVertically:"
+ "_setViewPosition:withVelocity:usingNonInteractiveSpring:animated:completion:"
+ "_setViewPositionHelper:withVelocity:usingNonInteractiveSpring:animated:completion:"
+ "_setupContentOffsetFloatAnimatableProperty"
+ "_shouldContinuePresentingActionButtons"
+ "_stretchedWidth"
+ "_swipeHintingHideAnimationBlock"
+ "_targetPositionAnimatableProperty"
+ "_titleAlpha"
+ "_titleLabelVisualStylingProvider"
+ "_updateActionButtonRevealPercentageForTargetPosition:"
+ "_updateActionRevealStateForTargetPosition:currentPosition:velocity:"
+ "_updateListVisibleAreaForSize:reason:"
+ "_updatePosition:"
+ "_updateRevealPercentage:"
+ "_updateTargetPosition:"
+ "_updateTitleLabelFont"
+ "_verticallyStacked"
+ "_viewToMove"
+ "_widthMultipleForVerticallyStackedButtonsWithCount:"
+ "_wordCountForText:"
+ "actionButtonCount"
+ "actionButtonsView"
+ "animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:"
+ "arrangedSubviews"
+ "backgroundMaterialRecipe"
+ "backgroundTintColor"
+ "buttonsStackView"
+ "clippingView"
+ "cornerRadius"
+ "customBackgroundView"
+ "d40@0:8d16d24d32"
+ "defaultActionButton"
+ "defaultActionFeedbackGenerator"
+ "defaultActionTriggered"
+ "defaultWidth"
+ "didPlayHaptic"
+ "dismissControlWithClearAllText:"
+ "enumerateEventHandlers:"
+ "glassLuminance"
+ "glyphView"
+ "hasGlassBackground"
+ "highlightDefaultActionButton"
+ "initWithActionButtonsView:interfaceEdge:layoutLocation:"
+ "initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:glassLuminance:"
+ "initWithStyle:view:"
+ "initWithTitle:sourceView:"
+ "initWithVariant:size:smoothness:subdued:"
+ "initWithViews:"
+ "interfaceEdge"
+ "isBackgroundGlass"
+ "isPerformingSwipeHinting"
+ "isVerticallyStacked"
+ "layoutLocation"
+ "layoutMarginsGuide"
+ "morphAnimation"
+ "morphToViews:alongsideAnimation:completion:"
+ "morphTransitionHelper"
+ "notificationStructuredListView:didUpdateViewFrame:"
+ "performingSwipeHinting"
+ "reverseObjectEnumerator"
+ "sendActionsForControlEvents:"
+ "setActionButtonsView:"
+ "setActive:"
+ "setAllowsGrouping:"
+ "setClippingView:"
+ "setCustomBackgroundView:"
+ "setDefaultActionButton:"
+ "setDefaultActionFeedbackGenerator:"
+ "setDefaultActionTriggered:"
+ "setDidPlayHaptic:"
+ "setGlyphView:"
+ "setHasGlassBackground:"
+ "setHighlightDefaultActionButton:"
+ "setInterfaceEdge:"
+ "setIsBackgroundGlass:"
+ "setLayoutLocation:"
+ "setMorphTransitionHelper:"
+ "setPerformingSwipeHinting:"
+ "setPresentedView:"
+ "setStretchedWidth:"
+ "setTitleAlpha:"
+ "setTitleLabelVisualStylingProvider:"
+ "setViewToMove:"
+ "showLessControlWithClearAllText:glyphOrientation:"
+ "spacing"
+ "stretchedWidth"
+ "swipe-action-button-identifier"
+ "tertiarySystemFillColor"
+ "titleAlpha"
+ "titleLabelVisualStylingProvider"
+ "transitionToState:ended:atLocation:"
+ "update visibleSize to width: %.2f; height: %.2f; reason %{public}@"
+ "v32@0:8Q16Q24"
+ "v32@?0@\"UIView<PLContentSizeCategoryAdjusting>\"8Q16^B24"
+ "v40@0:8@16@?24@?32"
+ "v40@0:8B16B20Q24@?32"
+ "v40@0:8B16B20d24@?32"
+ "v48@0:8d16B24B28d32@?40"
+ "v48@0:8d16d24B32B36@?40"
+ "v48@?0@\"UIAction\"8@16:24Q32^B40"
+ "v56@0:8@\"NCNotificationStructuredListView\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "verticallyStacked"
+ "viewDidAppear"
+ "viewFrameChanged"
+ "viewToMove"
+ "viewWillTransition"
+ "willMoveToSuperview:"
+ "x"
+ "\xa3"
- "@\"NSString\"24@0:8@\"NCNotificationSummaryExpandedHeaderView\"16"
- "@\"PLGlyphControl\""
- "@32@0:8q16@24"
- "@40@0:8q16@24q32"
- "T@\"UIView\",R,W,N,V_sourceView"
- "Tq,R,N,G_materialRecipe,V_materialRecipe"
- "_animatePresentation:cancelled:completion:"
- "_configureMaterialViewsIfNecessary"
- "_frictionForTransitionPresentation:cancelled:"
- "_newMaterialViewWithRecipe:"
- "_tensionForTransitionPresentation:cancelled:"
- "_updateListVisibleAreaForSize:"
- "_updateVisualStylingOfView:"
- "d24@0:8B16B20"
- "dismissControlWithMaterialRecipe:"
- "dismissControlWithMaterialRecipe:clearAllText:"
- "initWithMaterialRecipe:"
- "initWithTitle:materialRecipe:"
- "initWithTitle:sourceView:materialRecipe:"
- "materialGroupNameBaseForNotificationSummaryExpandedHeaderView:"
- "setBlurEnabled:"
- "setVisualStyle:"
- "showLessControlWithMaterialRecipe:clearAllText:glyphOrientation:"

```
