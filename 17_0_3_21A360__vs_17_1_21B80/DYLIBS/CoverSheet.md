## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4416.11.7.0.0
-  __TEXT.__text: 0x11e168
-  __TEXT.__auth_stubs: 0x12a0
+4416.25.105.0.0
+  __TEXT.__text: 0x121560
+  __TEXT.__auth_stubs: 0x12b0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x10878
+  __TEXT.__objc_methlist: 0x10a50
   __TEXT.__const: 0x24f8
-  __TEXT.__cstring: 0x8c88
-  __TEXT.__oslogstring: 0x709b
-  __TEXT.__gcc_except_tab: 0x7d0
+  __TEXT.__cstring: 0x8c3e
+  __TEXT.__oslogstring: 0x7184
+  __TEXT.__gcc_except_tab: 0x804
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x3630
-  __TEXT.__objc_classname: 0x2d87
-  __TEXT.__objc_methname: 0x380ed
-  __TEXT.__objc_methtype: 0x84a6
-  __TEXT.__objc_stubs: 0x21420
+  __TEXT.__unwind_info: 0x36b8
+  __TEXT.__objc_classname: 0x2e01
+  __TEXT.__objc_methname: 0x3878d
+  __TEXT.__objc_methtype: 0x8605
+  __TEXT.__objc_stubs: 0x21800
   __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x24f8
+  __DATA_CONST.__const: 0x2520
   __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x588
+  __DATA_CONST.__objc_protolist: 0x5a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x33b48
-  __DATA_CONST.__objc_selrefs: 0xa990
+  __DATA_CONST.__objc_const: 0x33dd8
+  __DATA_CONST.__objc_selrefs: 0xaaa8
   __DATA_CONST.__objc_arraydata: 0x1018
   __AUTH_CONST.__objc_const: 0x4d20
   __AUTH_CONST.__cfstring: 0xae20

   __AUTH_CONST.__objc_arrayobj: 0x1230
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__auth_got: 0x960
+  __AUTH_CONST.__auth_got: 0x968
   __AUTH.__objc_data: 0x11d0
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0xdf8
   __DATA.__objc_superrefs: 0x520
-  __DATA.__objc_ivar: 0x17f4
-  __DATA.__data: 0x4268
+  __DATA.__objc_ivar: 0x1814
+  __DATA.__data: 0x4388
   __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0x3160
   __DATA_DIRTY.__bss: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6173
-  Symbols:   22782
-  CStrings:  11245
+  Functions: 6213
+  Symbols:   22918
+  CStrings:  11312
 
Symbols:
+ -[CSActivityItemViewController _backlightLuminanceDidChange]
+ -[CSActivityItemViewController _isContentVisibleAndAppeared]
+ -[CSActivityItemViewController _updateAudioCategoriesDisablingVolumeHUDWithReason:]
+ -[CSActivityItemViewController audioCategoriesDisablingVolumeHUD]
+ -[CSActivityItemViewController delegate]
+ -[CSActivityItemViewController reevaluateAudioCategoriesDisablingVolumeHUD]
+ -[CSActivityItemViewController setDelegate:]
+ -[CSActivityManager _backgroundTintColorForUserInterfaceStyle:]
+ -[CSActivityManager _shouldSetDefaultBackgroundForViewController:]
+ -[CSActivityManager _textColorForUserInterfaceStyle:]
+ -[CSActivityManager activityHostViewControllerAudioCategoriesDisablingVolumeHUDDidChange:]
+ -[CSCombinedListViewController _updateAudioCategoriesDisablingVolumeHUD]
+ -[CSCombinedListViewController activityItemViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:]
+ -[CSCombinedListViewController audioCategoriesDisablingVolumeHUD]
+ -[CSCombinedListViewController audioCategoriesObserver]
+ -[CSCombinedListViewController setAudioCategoriesObserver:]
+ -[CSCoverSheetViewController _quickActionButtonInterpretsLocation:asBesideContentForGestureView:]
+ -[CSCoverSheetViewController audioCategoriesDisablingVolumeHUD]
+ -[CSCoverSheetViewController combinedListViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:]
+ -[CSCoverSheetViewController isDepthEffectEnabled]
+ -[CSCoverSheetViewController isFloatingLayerFullscreen]
+ -[CSCoverSheetViewController isTouchLocation:inRestrictedRectForGestureView:]
+ -[CSCoverSheetViewController setDepthEffectDisabled:]
+ -[CSCoverSheetViewController setFloatingLayerFullscreen:]
+ -[CSDashBoardQuickActionsButtonSettings setStrictTouchExtraRadius:]
+ -[CSDashBoardQuickActionsButtonSettings setUsesStrictTouchAllowance:]
+ -[CSDashBoardQuickActionsButtonSettings strictTouchExtraRadius]
+ -[CSDashBoardQuickActionsButtonSettings usesStrictTouchAllowance]
+ -[CSPosterSwitcherViewController hasEverAppeared]
+ -[CSPosterSwitcherViewController setHasEverAppeared:]
+ -[CSPosterSwitcherViewController viewWillAppear:]
+ -[CSQuickActionsButton clickInteractionShouldBegin:]
+ -[CSQuickActionsButton delegate]
+ -[CSQuickActionsButton setDelegate:]
+ -[CSQuickActionsView _buttonDiameter]
+ -[CSQuickActionsView _buttonSizeWithOutsets:]
+ -[CSQuickActionsView _leadingFrameWithOutsets:]
+ -[CSQuickActionsView _minYWithOutsets:]
+ -[CSQuickActionsView _trailingFrameWithOutsets:]
+ -[CSQuickActionsView _updateFlashlightSelectionState]
+ -[CSQuickActionsView interpretsLocationAsBesideContent:inView:]
+ -[CSQuickActionsView shouldAllowClickInteractionToBegin:forButton:]
+ -[CSQuickActionsView strictlyInterpretsLocationAsContent:inView:]
+ -[CSQuickActionsViewController interpretsLocationAsBesideButtons:inView:]
+ -[CSQuickActionsViewController shouldTouchesBeginForButton:click:]
+ GCC_except_table11
+ GCC_except_table184
+ GCC_except_table207
+ GCC_except_table270
+ GCC_except_table399
+ GCC_except_table452
+ GCC_except_table46
+ GCC_except_table472
+ GCC_except_table478
+ GCC_except_table552
+ GCC_except_table60
+ GCC_except_table601
+ GCC_except_table611
+ GCC_except_table613
+ GCC_except_table622
+ GCC_except_table631
+ GCC_except_table639
+ _BSEqualSets
+ _OBJC_IVAR_$_CSActivityItemViewController._audioCategoriesDisablingVolumeHUD
+ _OBJC_IVAR_$_CSActivityItemViewController._delegate
+ _OBJC_IVAR_$_CSCombinedListViewController._audioCategoriesDisablingVolumeHUD
+ _OBJC_IVAR_$_CSCombinedListViewController._audioCategoriesObserver
+ _OBJC_IVAR_$_CSCoverSheetViewController._depthEffectDisabled
+ _OBJC_IVAR_$_CSCoverSheetViewController._floatingLayerFullscreen
+ _OBJC_IVAR_$_CSDashBoardQuickActionsButtonSettings._strictTouchExtraRadius
+ _OBJC_IVAR_$_CSDashBoardQuickActionsButtonSettings._usesStrictTouchAllowance
+ _OBJC_IVAR_$_CSPosterSwitcherViewController._hasEverAppeared
+ _OBJC_IVAR_$_CSQuickActionsButton._callingSuper
+ _OBJC_IVAR_$_CSQuickActionsButton._delegate
+ _SBFAudioCategoriesDisablingVolumeHUDUnion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivityItemViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSCombinedListViewControllerAudioCategoriesObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSQuickActionsButtonDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivityItemViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSCombinedListViewControllerAudioCategoriesObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSQuickActionsButtonDelegate
+ __OBJC_$_PROTOCOL_REFS_CSActivityItemViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_CSCombinedListViewControllerAudioCategoriesObserver
+ __OBJC_LABEL_PROTOCOL_$_CSActivityItemViewControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSCombinedListViewControllerAudioCategoriesObserver
+ __OBJC_LABEL_PROTOCOL_$_CSQuickActionsButtonDelegate
+ __OBJC_PROTOCOL_$_CSActivityItemViewControllerDelegate
+ __OBJC_PROTOCOL_$_CSCombinedListViewControllerAudioCategoriesObserver
+ __OBJC_PROTOCOL_$_CSQuickActionsButtonDelegate
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.666
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.667
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.668
+ ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.632
+ ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.538
+ ___58-[CSActivityManager _addActivityListItemForContentUpdate:]_block_invoke_2
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.601
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.643
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.644
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.651
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.649
+ ___74-[CSCoverSheetViewController _updateAppearanceForAODTransitionToInactive:]_block_invoke_3
+ ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.467
+ ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.468
+ ___block_descriptor_48_e8_32s40w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw40l8s32l8
+ ___block_literal_global.107
+ ___block_literal_global.2071
+ ___block_literal_global.222
+ ___block_literal_global.42
+ ___block_literal_global.49
+ ___block_literal_global.661
+ ___block_literal_global.663
+ ___block_literal_global.96
+ __unnamed_array_storage.364
+ __unnamed_array_storage.555
+ __unnamed_array_storage.558
+ __unnamed_array_storage.595
+ _objc_msgSend$_backgroundTintColorForUserInterfaceStyle:
+ _objc_msgSend$_buttonDiameter
+ _objc_msgSend$_buttonSizeWithOutsets:
+ _objc_msgSend$_isContentVisibleAndAppeared
+ _objc_msgSend$_leadingFrameWithOutsets:
+ _objc_msgSend$_minYWithOutsets:
+ _objc_msgSend$_quickActionButtonInterpretsLocation:asBesideContentForGestureView:
+ _objc_msgSend$_shouldSetDefaultBackgroundForViewController:
+ _objc_msgSend$_textColorForUserInterfaceStyle:
+ _objc_msgSend$_trailingFrameWithOutsets:
+ _objc_msgSend$_updateAudioCategoriesDisablingVolumeHUD
+ _objc_msgSend$_updateAudioCategoriesDisablingVolumeHUDWithReason:
+ _objc_msgSend$_updateFlashlightSelectionState
+ _objc_msgSend$activityHostViewControllerBackgroundTintColorDidChange:
+ _objc_msgSend$activityItemViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:
+ _objc_msgSend$audioCategoriesDisablingVolumeHUD
+ _objc_msgSend$audioCategoriesObserver
+ _objc_msgSend$combinedListViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:
+ _objc_msgSend$coverSheetViewController:requestsPreArmDisabled:forReason:
+ _objc_msgSend$coverSheetViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:
+ _objc_msgSend$hasEverAppeared
+ _objc_msgSend$interpretsLocationAsBesideButtons:inView:
+ _objc_msgSend$interpretsLocationAsBesideContent:inView:
+ _objc_msgSend$isDepthEffectEnabled
+ _objc_msgSend$isFloatingLayerFullscreen
+ _objc_msgSend$isTouchLocation:inRestrictedRectForGestureView:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$locationInCoordinateSpace:
+ _objc_msgSend$reevaluateAudioCategoriesDisablingVolumeHUD
+ _objc_msgSend$setAudioCategoriesObserver:
+ _objc_msgSend$setHasEverAppeared:
+ _objc_msgSend$setStrictTouchExtraRadius:
+ _objc_msgSend$setUsesStrictTouchAllowance:
+ _objc_msgSend$shouldAllowClickInteractionToBegin:forButton:
+ _objc_msgSend$strictTouchExtraRadius
+ _objc_msgSend$strictlyInterpretsLocationAsContent:inView:
+ _objc_msgSend$superclass
+ _objc_msgSend$systemBlackColor
+ _objc_msgSend$usesStrictTouchAllowance
- -[CSActivityItemViewController traitCollectionDidChange:]
- -[CSActivityManager _shouldSetBlackBackgroundForViewController:]
- -[CSCoverSheetViewController interpretsTouchLocationAsContentInListRestrictedRect:]
- -[CSLockScreenSettings allowPosterSwitcherActivationInset]
- -[CSLockScreenSettings posterSwitcherActivationInset]
- -[CSLockScreenSettings setAllowPosterSwitcherActivationInset:]
- -[CSLockScreenSettings setPosterSwitcherActivationInset:]
- GCC_except_table10
- GCC_except_table182
- GCC_except_table206
- GCC_except_table268
- GCC_except_table395
- GCC_except_table42
- GCC_except_table448
- GCC_except_table468
- GCC_except_table474
- GCC_except_table548
- GCC_except_table56
- GCC_except_table597
- GCC_except_table607
- GCC_except_table609
- GCC_except_table618
- GCC_except_table627
- GCC_except_table635
- _CGRectInset
- _OBJC_IVAR_$_CSCoverSheetViewController._posterSwitcherActivationInset
- _OBJC_IVAR_$_CSLockScreenSettings._allowPosterSwitcherActivationInset
- _OBJC_IVAR_$_CSLockScreenSettings._posterSwitcherActivationInset
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.670
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.671
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.672
- ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.636
- ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.542
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.605
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.647
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.648
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.655
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.653
- ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.473
- ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.474
- ___block_literal_global.105
- ___block_literal_global.2058
- ___block_literal_global.224
- ___block_literal_global.40
- ___block_literal_global.665
- ___block_literal_global.667
- ___block_literal_global.94
- __unnamed_array_storage.373
- __unnamed_array_storage.559
- __unnamed_array_storage.562
- __unnamed_array_storage.599
- _objc_msgSend$_shouldSetBlackBackgroundForViewController:
- _objc_msgSend$allowPosterSwitcherActivationInset
- _objc_msgSend$contentScaleFactor
- _objc_msgSend$insertSubview:above:
- _objc_msgSend$insertSubview:below:
- _objc_msgSend$interpretsTouchLocationAsContentInListRestrictedRect:
- _objc_msgSend$posterSwitcherActivationInset
- _objc_msgSend$setClipsSubviews:
CStrings:
+ "\x02\x19\x81!\x11\x16\x17\x12\x12\x18W\x12\x19$A\x12\x12\x11\x12\x11C\x1f\n\x16"
+ "\x051\x13\x1f\x03\x14#Q\xe1\x1e"
+ "\x11\""
+ "%{public}@ Updating audioCategoriesDisablingVolumeHUD to '%{public}@' for reason: %{public}@"
+ "(%@:%p) Updating audioCategoriesDisablingVolumeHUD to '%{public}@'"
+ "@\"<CSActivityItemViewControllerDelegate>\""
+ "@\"<CSCombinedListViewControllerAudioCategoriesObserver>\""
+ "@\"<CSQuickActionsButtonDelegate>\""
+ "@\"NSSet\""
+ "B32@0:8@\"CSQuickActionsButton\"16@\"_UIClickInteraction\"24"
+ "B32@0:8@\"_UIClickInteraction\"16@\"CSQuickActionsButton\"24"
+ "B40@0:8{CGPoint=dd}16@\"UIView\"32"
+ "CSActivityItemViewControllerDelegate"
+ "CSCombinedListViewControllerAudioCategoriesObserver"
+ "CSQuickActionsButtonDelegate"
+ "CoverSheetPlurals"
+ "Enforce Gating"
+ "Extra Radius"
+ "Initialization"
+ "PreArm"
+ "Rejecting Poster Switcher gesture – capability is restricted."
+ "Rejecting Poster Switcher gesture – location is beside the quick action buttons"
+ "Rejecting Poster Switcher gesture – location is in a complication"
+ "Rejecting Poster Switcher gesture – location is in combined list"
+ "Rejecting Poster Switcher gesture – location is in notification list gutter"
+ "Rejecting Poster Switcher gesture – location is in safe area"
+ "Rejecting Poster Switcher gesture – location is over a quick action button"
+ "Strict Touch Gating"
+ "T@\"<CSActivityItemViewControllerDelegate>\",W,N,V_delegate"
+ "T@\"<CSCombinedListViewControllerAudioCategoriesObserver>\",W,N,V_audioCategoriesObserver"
+ "T@\"<CSQuickActionsButtonDelegate>\",W,N,V_delegate"
+ "T@\"NSSet\",R,N"
+ "T@\"NSSet\",R,N,V_audioCategoriesDisablingVolumeHUD"
+ "TB,N,GisDepthEffectEnabled,V_depthEffectDisabled"
+ "TB,N,GisFloatingLayerFullscreen,V_floatingLayerFullscreen"
+ "TB,N,V_hasEverAppeared"
+ "TB,N,V_usesStrictTouchAllowance"
+ "Td,N,V_strictTouchExtraRadius"
+ "[Charge UI] Starting fade in for source: %@"
+ "[Charge UI][Suppressed] visible NO, suppressed for ambient presentation! source: %@"
+ "_audioCategoriesDisablingVolumeHUD"
+ "_audioCategoriesObserver"
+ "_backgroundTintColorForUserInterfaceStyle:"
+ "_backlightLuminanceDidChange"
+ "_buttonDiameter"
+ "_buttonSizeWithOutsets:"
+ "_callingSuper"
+ "_depthEffectDisabled"
+ "_floatingLayerFullscreen"
+ "_hasEverAppeared"
+ "_isContentVisibleAndAppeared"
+ "_leadingFrameWithOutsets:"
+ "_minYWithOutsets:"
+ "_quickActionButtonInterpretsLocation:asBesideContentForGestureView:"
+ "_shouldSetDefaultBackgroundForViewController:"
+ "_strictTouchExtraRadius"
+ "_textColorForUserInterfaceStyle:"
+ "_trailingFrameWithOutsets:"
+ "_updateAudioCategoriesDisablingVolumeHUD"
+ "_updateAudioCategoriesDisablingVolumeHUDWithReason:"
+ "_updateFlashlightSelectionState"
+ "_usesStrictTouchAllowance"
+ "activityItemViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:"
+ "audioCategoriesDisablingVolumeHUD"
+ "audioCategoriesObserver"
+ "clickInteractionShouldBegin:"
+ "combinedListViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:"
+ "coverSheetViewController:requestsPreArmDisabled:forReason:"
+ "coverSheetViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:"
+ "depthEffectDisabled"
+ "floatingLayerFullscreen"
+ "hasEverAppeared"
+ "interpretsLocationAsBesideButtons:inView:"
+ "interpretsLocationAsBesideContent:inView:"
+ "isDepthEffectEnabled"
+ "isFloatingLayerFullscreen"
+ "isTouchLocation:inRestrictedRectForGestureView:"
+ "localizedStringWithFormat:"
+ "locationInCoordinateSpace:"
+ "reevaluateAudioCategoriesDisablingVolumeHUD"
+ "setAudioCategoriesObserver:"
+ "setDepthEffectDisabled:"
+ "setFloatingLayerFullscreen:"
+ "setHasEverAppeared:"
+ "setStrictTouchExtraRadius:"
+ "setUsesStrictTouchAllowance:"
+ "shouldAllowClickInteractionToBegin:forButton:"
+ "shouldTouchesBeginForButton:click:"
+ "strictTouchExtraRadius"
+ "strictlyInterpretsLocationAsContent:inView:"
+ "systemBlackColor"
+ "usesStrictTouchAllowance"
+ "v24@0:8@\"CSActivityItemViewController\"16"
+ "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
+ "{CGSize=dd}20@0:8B16"
+ "\xf0\xf0\xe3\x1e\x11"
- "\x02\x19\x81!\x11\x16\x17\x12\x12\x17\x11W\x12\x19$1\x12\x12\x11\x12\x11C\x1f\n\x16"
- "\x051\x13\x1f\x03\x14#Q\xee"
- "Allow Poster Switcher Activation Area Inset"
- "Poster Switcher gesture not beginning because location for the gesture is in a complication"
- "Poster Switcher gesture not beginning because location for the gesture is in combined list"
- "Poster Switcher gesture not beginning because location for the gesture is in safe area"
- "Poster Switcher gesture not beginning because location for the gesture is over a quick action button"
- "Poster Switcher gesture not beginning because location for the gesture outside activation area"
- "Poster Switcher gesture not beginning because poster switcher capability is restricted."
- "TB,V_allowPosterSwitcherActivationInset"
- "Td,V_posterSwitcherActivationInset"
- "_allowPosterSwitcherActivationInset"
- "_posterSwitcherActivationInset"
- "_shouldSetBlackBackgroundForViewController:"
- "allowPosterSwitcherActivationInset"
- "contentScaleFactor"
- "insertSubview:above:"
- "insertSubview:below:"
- "interpretsTouchLocationAsContentInListRestrictedRect:"
- "notificationListSupplementaryViewPresentable:contentWillBecomeVisible:"
- "posterSwitcherActivationInset"
- "setAllowPosterSwitcherActivationInset:"
- "setClipsSubviews:"
- "setPosterSwitcherActivationInset:"
- "setScreenOn"
- "traitCollectionDidChange"
- "\xf0\xf0\xe3\x1e"

```
