## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4557.0.3.103.0
-  __TEXT.__text: 0x162670
-  __TEXT.__auth_stubs: 0x13b0
+4557.0.6.103.0
+  __TEXT.__text: 0x163de8
+  __TEXT.__auth_stubs: 0x13e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x15d44
-  __TEXT.__const: 0x2a78
-  __TEXT.__cstring: 0x9ecc
-  __TEXT.__oslogstring: 0x8845
-  __TEXT.__gcc_except_tab: 0xd10
+  __TEXT.__objc_methlist: 0x15f54
+  __TEXT.__const: 0x2ab0
+  __TEXT.__cstring: 0x9fa4
+  __TEXT.__oslogstring: 0x8a38
+  __TEXT.__gcc_except_tab: 0xd30
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x4020
-  __TEXT.__objc_classname: 0x3450
-  __TEXT.__objc_methname: 0x3f4f4
-  __TEXT.__objc_methtype: 0x9b20
-  __TEXT.__objc_stubs: 0x25000
-  __DATA_CONST.__got: 0x1528
-  __DATA_CONST.__const: 0x29d0
-  __DATA_CONST.__objc_classlist: 0x790
+  __TEXT.__unwind_info: 0x4080
+  __TEXT.__objc_classname: 0x3488
+  __TEXT.__objc_methname: 0x3fcca
+  __TEXT.__objc_methtype: 0x9c89
+  __TEXT.__objc_stubs: 0x25440
+  __DATA_CONST.__got: 0x1558
+  __DATA_CONST.__const: 0x2a58
+  __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc1a8
+  __DATA_CONST.__objc_selrefs: 0xc2d8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x5d8
-  __DATA_CONST.__objc_arraydata: 0x10c0
-  __AUTH_CONST.__auth_got: 0x9e8
-  __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0xbcc0
-  __AUTH_CONST.__objc_const: 0x3c130
-  __AUTH_CONST.__objc_doubleobj: 0x640
-  __AUTH_CONST.__objc_arrayobj: 0x1290
-  __AUTH_CONST.__objc_intobj: 0x450
-  __AUTH.__objc_data: 0x1400
-  __DATA.__objc_ivar: 0x1adc
+  __DATA_CONST.__objc_superrefs: 0x5e0
+  __DATA_CONST.__objc_arraydata: 0x1078
+  __AUTH_CONST.__auth_got: 0xa00
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0xbd80
+  __AUTH_CONST.__objc_const: 0x3c310
+  __AUTH_CONST.__objc_doubleobj: 0x660
+  __AUTH_CONST.__objc_arrayobj: 0x1248
+  __AUTH_CONST.__objc_intobj: 0x438
+  __AUTH.__objc_data: 0x1450
+  __DATA.__objc_ivar: 0x1b04
   __DATA.__data: 0x4e68
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x37a0

   - /System/Library/PrivateFrameworks/PosterBoardUI.framework/PosterBoardUI
   - /System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices
   - /System/Library/PrivateFrameworks/PosterKit.framework/PosterKit
+  - /System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2ECE7E13-4BC6-3B51-AFDE-E6B498E263DF
-  Functions: 6991
-  Symbols:   25602
-  CStrings:  14069
+  UUID: 6036ABAD-D07E-38FE-81DC-12B9A98C8782
+  Functions: 7039
+  Symbols:   25765
+  CStrings:  14151
 
Symbols:
+ +[CSNotificationLegibilityDimView _fullDimColorMatrix]
+ +[CSNotificationLegibilityDimView _localizedDimColorMatrix]
+ +[CSNotificationLegibilityDimView _noDimColorMatrix]
+ -[CSBackgroundContentComponent setShouldDim:]
+ -[CSBackgroundContentComponent shouldDim:]
+ -[CSBackgroundContentComponent shouldDim]
+ -[CSCombinedListViewController updateGlassContentInterfaceStyle:luminanceValue:]
+ -[CSCoverSheetSDFView _layoutLayer:inBounds:withHorizontalOutset:]
+ -[CSCoverSheetSDFView _refractionHeight]
+ -[CSCoverSheetView _addNotificationLegibilityFullBaseLayerDimView]
+ -[CSCoverSheetView _addNotificationLegibilityLocalizedDimView]
+ -[CSCoverSheetView _animateLayer:toValues:forKeyPath:duration:dispatchGroup:]
+ -[CSCoverSheetView _animateToDimming:withDuration:dispatchGroup:]
+ -[CSCoverSheetView _evaluateBackgroundContentViewMatchMove]
+ -[CSCoverSheetView _filterForDimming:]
+ -[CSCoverSheetView _filterNumbersForDimming:]
+ -[CSCoverSheetView _layoutNotificationLegibilityFullBaseLayerView]
+ -[CSCoverSheetView _layoutNotificationLegibilityLocalizedDimView]
+ -[CSCoverSheetView _setBackgroundContentViewMatchMoveActive:]
+ -[CSCoverSheetView animationDidStop:finished:]
+ -[CSCoverSheetView isBackgroundContentViewDimmed]
+ -[CSCoverSheetView notificationLegibilityFullBaseLayerDimView]
+ -[CSCoverSheetView notificationLegibilityLocalizedDimView]
+ -[CSCoverSheetView setBackgroundContentViewDimmed:]
+ -[CSCoverSheetView setNotificationLegibilityFullBaseLayerDimView:]
+ -[CSCoverSheetView setNotificationLegibilityLocalizedDimView:]
+ -[CSCoverSheetView setSuppressesBackgroundContentMatchMove:forReason:]
+ -[CSCoverSheetViewController _updateGlassContentInterfaceStyle]
+ -[CSCoverSheetViewController notificationLegibilityDimController]
+ -[CSCoverSheetViewController secureWindowVisibilityDidChange:]
+ -[CSCoverSheetViewController setNotificationLegibilityDimController:]
+ -[CSCoverSheetViewController setWallpaperLegibilityEnvironment:]
+ -[CSCoverSheetViewController wallpaperLegibilityEnvironmentDidChange:]
+ -[CSCoverSheetViewController wallpaperLegibilityEnvironment]
+ -[CSHomeAffordanceViewController homeAffordanceInteractionDidRecognizeSingleClick:]
+ -[CSLockScreenChargingSettings extendedSubtitleStringTimeoutMultiplier]
+ -[CSLockScreenChargingSettings setExtendedSubtitleStringTimeoutMultiplier:]
+ -[CSNotificationLegibilityDimController .cxx_destruct]
+ -[CSNotificationLegibilityDimController _updateDimViewsForced:]
+ -[CSNotificationLegibilityDimController _updateDimViewsWithDimLevel:]
+ -[CSNotificationLegibilityDimController addDimView:]
+ -[CSNotificationLegibilityDimController currentDimLevel]
+ -[CSNotificationLegibilityDimController effectiveFadeInThreshold]
+ -[CSNotificationLegibilityDimController fadeAnchorY]
+ -[CSNotificationLegibilityDimController fadeRadiusY]
+ -[CSNotificationLegibilityDimController fadeWidth]
+ -[CSNotificationLegibilityDimController fullDimHeight]
+ -[CSNotificationLegibilityDimController init]
+ -[CSNotificationLegibilityDimController isDimVisible]
+ -[CSNotificationLegibilityDimController mutableDimViews]
+ -[CSNotificationLegibilityDimController setCurrentDimLevel:]
+ -[CSNotificationLegibilityDimController setDimVisible:]
+ -[CSNotificationLegibilityDimController setFadeAnchorY:]
+ -[CSNotificationLegibilityDimController setFadeRadiusY:]
+ -[CSNotificationLegibilityDimController setFadeWidth:]
+ -[CSNotificationLegibilityDimController setFullDimHeight:]
+ -[CSNotificationLegibilityDimController setMutableDimViews:]
+ -[CSNotificationLegibilityDimController setTraitCollection:]
+ -[CSNotificationLegibilityDimController traitCollection]
+ -[CSNotificationLegibilityDimController updateDimViews]
+ -[CSNotificationLegibilityDimView _configureColorMatrix]
+ -[CSNotificationLegibilityDimView _layoutBlendingMask]
+ -[CSNotificationLegibilityDimView _layoutDimViews]
+ -[CSNotificationLegibilityDimView _shouldAnimatePropertyWithKey:]
+ -[CSNotificationLegibilityDimView dimType]
+ -[CSNotificationLegibilityDimView fadeRadiusY]
+ -[CSNotificationLegibilityDimView fadeWidth]
+ -[CSNotificationLegibilityDimView initWithCoder:]
+ -[CSNotificationLegibilityDimView initWithFrame:dimType:]
+ -[CSNotificationLegibilityDimView layoutInsetsForSize:]
+ -[CSNotificationLegibilityDimView layoutSubviews]
+ -[CSNotificationLegibilityDimView setFadeRadiusY:]
+ -[CSNotificationLegibilityDimView setFadeWidth:]
+ -[CSNotificationLegibilityDimView setVisible:]
+ -[CSQuickActionsView glassLuminanceValue]
+ -[CSQuickActionsView setGlassLuminanceValue:]
+ -[CSTeachableMomentsContainerViewController homeAffordanceViewControllerDidRecognizeSingleClick:]
+ GCC_except_table169
+ GCC_except_table209
+ GCC_except_table213
+ GCC_except_table308
+ GCC_except_table448
+ GCC_except_table506
+ GCC_except_table526
+ GCC_except_table536
+ GCC_except_table614
+ GCC_except_table671
+ GCC_except_table681
+ GCC_except_table683
+ GCC_except_table692
+ GCC_except_table704
+ GCC_except_table714
+ GCC_except_table85
+ GCC_except_table88
+ _CAColorMatrixIdentity
+ _CAColorMatrixMakeMultiplyColor
+ _CGRectInset
+ _OBJC_CLASS_$_CSNotificationLegibilityDimController
+ _OBJC_CLASS_$_CSNotificationLegibilityDimView
+ _OBJC_CLASS_$_NSValue
+ _OBJC_IVAR_$_CSCoverSheetView._backgroundContentViewDimmed
+ _OBJC_IVAR_$_CSCoverSheetView._backgroundContentViewMatchMoveDisabledReasons
+ _OBJC_IVAR_$_CSCoverSheetView._isBackgroundContentViewMatchMoveActive
+ _OBJC_IVAR_$_CSCoverSheetView._notificationLegibilityFullBaseLayerDimView
+ _OBJC_IVAR_$_CSCoverSheetView._notificationLegibilityLocalizedDimView
+ _OBJC_IVAR_$_CSCoverSheetViewController._notificationLegibilityDimController
+ _OBJC_IVAR_$_CSCoverSheetViewController._wallpaperLegibilityEnvironment
+ _OBJC_IVAR_$_CSLockScreenChargingSettings._extendedSubtitleStringTimeoutMultiplier
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._currentDimLevel
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._dimVisible
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._fadeAnchorY
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._fadeRadiusY
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._fadeWidth
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._fullDimHeight
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._mutableDimViews
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._traitCollection
+ _OBJC_IVAR_$_CSNotificationLegibilityDimView._dimType
+ _OBJC_IVAR_$_CSNotificationLegibilityDimView._fadeRadiusY
+ _OBJC_IVAR_$_CSNotificationLegibilityDimView._fadeWidth
+ _OBJC_IVAR_$_CSQuickActionsView._glassLuminanceValue
+ _OBJC_METACLASS_$_CSNotificationLegibilityDimController
+ _OBJC_METACLASS_$_CSNotificationLegibilityDimView
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _PLKLegibilityEnvironmentVariantLockScreen
+ _SBUIGlassContentInterfaceStyleFromLuminance
+ _UIEdgeInsetsZero
+ __OBJC_$_CLASS_METHODS_CSNotificationLegibilityDimView
+ __OBJC_$_INSTANCE_METHODS_CSNotificationLegibilityDimController
+ __OBJC_$_INSTANCE_METHODS_CSNotificationLegibilityDimView
+ __OBJC_$_INSTANCE_VARIABLES_CSNotificationLegibilityDimController
+ __OBJC_$_INSTANCE_VARIABLES_CSNotificationLegibilityDimView
+ __OBJC_$_PROP_LIST_CSBackgroundContentComponent
+ __OBJC_$_PROP_LIST_CSNotificationLegibilityDimController
+ __OBJC_$_PROP_LIST_CSNotificationLegibilityDimView
+ __OBJC_CLASS_RO_$_CSNotificationLegibilityDimController
+ __OBJC_CLASS_RO_$_CSNotificationLegibilityDimView
+ __OBJC_METACLASS_RO_$_CSNotificationLegibilityDimController
+ __OBJC_METACLASS_RO_$_CSNotificationLegibilityDimView
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.789
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.793
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.794
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.795
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.197
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.206
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.200
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.209
+ ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.755
+ ___51-[CSCoverSheetView setBackgroundContentViewDimmed:]_block_invoke
+ ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.661
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.452
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.453
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.461
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.724
+ ___63-[CSNotificationLegibilityDimController _updateDimViewsForced:]_block_invoke
+ ___63-[CSNotificationLegibilityDimController _updateDimViewsForced:]_block_invoke.3
+ ___63-[CSNotificationLegibilityDimController _updateDimViewsForced:]_block_invoke_2
+ ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.491
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.766
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.774
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.772
+ ___69-[CSNotificationLegibilityDimController _updateDimViewsWithDimLevel:]_block_invoke
+ ___69-[CSNotificationLegibilityDimController _updateDimViewsWithDimLevel:]_block_invoke_2
+ ___69-[CSNotificationLegibilityDimController _updateDimViewsWithDimLevel:]_block_invoke_3
+ ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.587
+ ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.588
+ ___98-[CSCoverSheetViewController activateCameraWithHostableEntity:animated:sendingActions:completion:]_block_invoke.148
+ ___block_descriptor_32_e48_v32?0"CSNotificationLegibilityDimView"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e48_v32?0"CSNotificationLegibilityDimView"8Q16^B24ls32l8
+ ___block_descriptor_56_e8_32s40s48w_e18_v16?0"NSString"8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e18_v16?0"NSString"8ls32l8s40l8s48l8
+ ___block_literal_global.11
+ ___block_literal_global.199
+ ___block_literal_global.228
+ ___block_literal_global.2286
+ ___block_literal_global.336
+ ___block_literal_global.404
+ ___block_literal_global.409
+ ___block_literal_global.414
+ ___block_literal_global.419
+ ___block_literal_global.424
+ ___block_literal_global.429
+ ___block_literal_global.7
+ ___block_literal_global.784
+ ___block_literal_global.786
+ ___block_literal_global.9
+ _kCAFilterColorMatrix
+ _kCAFilterInputColorMatrix
+ _kCAFilterVibrantColorMatrix
+ _objc_msgSend$_addNotificationLegibilityFullBaseLayerDimView
+ _objc_msgSend$_addNotificationLegibilityLocalizedDimView
+ _objc_msgSend$_animateLayer:toValues:forKeyPath:duration:dispatchGroup:
+ _objc_msgSend$_animateToDimming:withDuration:dispatchGroup:
+ _objc_msgSend$_animateUsingSpringWithDampingRatio:response:tracking:dampingRatioSmoothing:responseSmoothing:targetSmoothing:projectionDeceleration:retargetImpulse:animations:completion:
+ _objc_msgSend$_configureColorMatrix
+ _objc_msgSend$_evaluateBackgroundContentViewMatchMove
+ _objc_msgSend$_filterForDimming:
+ _objc_msgSend$_filterNumbersForDimming:
+ _objc_msgSend$_fullDimColorMatrix
+ _objc_msgSend$_layoutBlendingMask
+ _objc_msgSend$_layoutDimViews
+ _objc_msgSend$_layoutLayer:inBounds:withHorizontalOutset:
+ _objc_msgSend$_layoutNotificationLegibilityFullBaseLayerView
+ _objc_msgSend$_layoutNotificationLegibilityLocalizedDimView
+ _objc_msgSend$_localizedDimColorMatrix
+ _objc_msgSend$_luminance
+ _objc_msgSend$_noDimColorMatrix
+ _objc_msgSend$_refractionHeight
+ _objc_msgSend$_setBackgroundContentViewMatchMoveActive:
+ _objc_msgSend$_updateDimViewsForced:
+ _objc_msgSend$_updateDimViewsWithDimLevel:
+ _objc_msgSend$_updateGlassContentInterfaceStyle
+ _objc_msgSend$addDimView:
+ _objc_msgSend$averageColor
+ _objc_msgSend$currentDimLevel
+ _objc_msgSend$dimType
+ _objc_msgSend$extendedSubtitleStringTimeoutMultiplier
+ _objc_msgSend$fullDimHeight
+ _objc_msgSend$homeAffordanceViewControllerDidRecognizeSingleClick:
+ _objc_msgSend$initWithFrame:dimType:
+ _objc_msgSend$isDimVisible
+ _objc_msgSend$layoutInsetsForSize:
+ _objc_msgSend$legibilityEnvironmentContextForVariant:
+ _objc_msgSend$luma
+ _objc_msgSend$mutableDimViews
+ _objc_msgSend$notificationLegibilityDimController
+ _objc_msgSend$notificationLegibilityFullBaseLayerDimView
+ _objc_msgSend$notificationLegibilityLocalizedDimView
+ _objc_msgSend$setBackgroundContentViewDimmed:
+ _objc_msgSend$setCustomSubtitle:withPriority:withTimeout:
+ _objc_msgSend$setDimVisible:
+ _objc_msgSend$setExtendedSubtitleStringTimeoutMultiplier:
+ _objc_msgSend$setFullDimHeight:
+ _objc_msgSend$setGlassLuminanceValue:
+ _objc_msgSend$setShouldDim:
+ _objc_msgSend$setSuppressesBackgroundContentMatchMove:forReason:
+ _objc_msgSend$setTraitCollection:
+ _objc_msgSend$setWallpaperLegibilityEnvironment:
+ _objc_msgSend$updateDimViews
+ _objc_msgSend$updateGlassContentInterfaceStyle:luminanceValue:
+ _objc_msgSend$updateGlassContentInterfaceStyleToUserInterfaceStyle:luminanceValue:
+ _objc_msgSend$valueWithCAColorMatrix:
+ _objc_msgSend$wallpaperLegibilityEnvironment
- +[CSNotificationDimView layerClass]
- -[CSCoverSheetView _addNotificationDimView]
- -[CSCoverSheetView _addWallpaperLegibilityContainerView]
- -[CSCoverSheetView _layoutNotificationDimView]
- -[CSCoverSheetView _layoutWallpaperLegibilityContainerView]
- -[CSCoverSheetView notificationDimView]
- -[CSCoverSheetView setNotificationDimView:]
- -[CSCoverSheetView wallpaperLegibilityContainerView]
- -[CSNotificationDimView .cxx_destruct]
- -[CSNotificationDimView _configureFilter]
- -[CSNotificationDimView _configureShadowMask]
- -[CSNotificationDimView _layoutShadowMask]
- -[CSNotificationDimView _performAlphaAnimationToAlpha:]
- -[CSNotificationDimView effectiveFadeInThreshold]
- -[CSNotificationDimView effectiveFadeRadiusY]
- -[CSNotificationDimView fadeAlpha]
- -[CSNotificationDimView fadeAnchorY]
- -[CSNotificationDimView fadeRadiusY]
- -[CSNotificationDimView fadeWidth]
- -[CSNotificationDimView initWithCoder:]
- -[CSNotificationDimView initWithFrame:]
- -[CSNotificationDimView isPerformingAlphaAnimation]
- -[CSNotificationDimView layoutSubviews]
- -[CSNotificationDimView setFadeAlpha:]
- -[CSNotificationDimView setFadeAnchorY:]
- -[CSNotificationDimView setFadeRadiusY:]
- -[CSNotificationDimView setFadeWidth:]
- -[CSNotificationDimView setFrame:]
- -[CSNotificationDimView setIsPerformingAlphaAnimation:]
- -[CSNotificationDimView setShadowMaskLayer:]
- -[CSNotificationDimView shadowMaskLayer]
- -[CSTeachableMomentsContainerViewController _homeAffordanceClickRecognized:]
- -[CSTeachableMomentsContainerViewController gestureRecognizer:shouldReceiveTouch:]
- -[CSTeachableMomentsContainerViewController homeAffordanceClickGestureRecognizer]
- -[CSTeachableMomentsContainerViewController setHomeAffordanceClickGestureRecognizer:]
- GCC_except_table168
- GCC_except_table208
- GCC_except_table212
- GCC_except_table306
- GCC_except_table446
- GCC_except_table503
- GCC_except_table523
- GCC_except_table533
- GCC_except_table611
- GCC_except_table668
- GCC_except_table678
- GCC_except_table680
- GCC_except_table689
- GCC_except_table700
- GCC_except_table710
- GCC_except_table84
- GCC_except_table87
- _OBJC_CLASS_$_CSNotificationDimView
- _OBJC_IVAR_$_CSCoverSheetView._notificationDimView
- _OBJC_IVAR_$_CSCoverSheetView._wallpaperLegibilityContainerView
- _OBJC_IVAR_$_CSNotificationDimView._effectiveFadeRadiusY
- _OBJC_IVAR_$_CSNotificationDimView._fadeAlpha
- _OBJC_IVAR_$_CSNotificationDimView._fadeAnchorY
- _OBJC_IVAR_$_CSNotificationDimView._fadeRadiusY
- _OBJC_IVAR_$_CSNotificationDimView._fadeWidth
- _OBJC_IVAR_$_CSNotificationDimView._isPerformingAlphaAnimation
- _OBJC_IVAR_$_CSNotificationDimView._shadowMaskLayer
- _OBJC_IVAR_$_CSTeachableMomentsContainerViewController._homeAffordanceClickGestureRecognizer
- _OBJC_METACLASS_$_CSNotificationDimView
- _SBSDetailedBatteryUIDismissDuration
- __OBJC_$_CLASS_METHODS_CSNotificationDimView
- __OBJC_$_INSTANCE_METHODS_CSNotificationDimView
- __OBJC_$_INSTANCE_VARIABLES_CSNotificationDimView
- __OBJC_$_PROP_LIST_CSNotificationDimView
- __OBJC_CLASS_RO_$_CSNotificationDimView
- __OBJC_METACLASS_RO_$_CSNotificationDimView
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.782
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.783
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.784
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.189
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.202
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.196
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.205
- ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.748
- ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.654
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.448
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.449
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.457
- ___55-[CSNotificationDimView _performAlphaAnimationToAlpha:]_block_invoke
- ___55-[CSNotificationDimView _performAlphaAnimationToAlpha:]_block_invoke_2
- ___55-[CSNotificationDimView _performAlphaAnimationToAlpha:]_block_invoke_3
- ___55-[CSNotificationDimView _performAlphaAnimationToAlpha:]_block_invoke_4
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.717
- ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.484
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.759
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.760
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.765
- ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.580
- ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.581
- ___98-[CSCoverSheetViewController activateCameraWithHostableEntity:animated:sendingActions:completion:]_block_invoke.147
- ___block_descriptor_56_e8_32s40s_e18_v16?0"NSString"8ls32l8s40l8
- ___block_literal_global.195
- ___block_literal_global.224
- ___block_literal_global.2263
- ___block_literal_global.332
- ___block_literal_global.400
- ___block_literal_global.405
- ___block_literal_global.410
- ___block_literal_global.415
- ___block_literal_global.425
- ___block_literal_global.777
- ___block_literal_global.779
- _kCAFilterInputAlphaValues
- _objc_msgSend$_addNotificationDimView
- _objc_msgSend$_addWallpaperLegibilityContainerView
- _objc_msgSend$_animateByRetargetingAnimations:completion:
- _objc_msgSend$_animateUsingSpringInteractive:animations:completion:
- _objc_msgSend$_configureFilter
- _objc_msgSend$_configureShadowMask
- _objc_msgSend$_isPointerTouch
- _objc_msgSend$_layoutNotificationDimView
- _objc_msgSend$_layoutShadowMask
- _objc_msgSend$_layoutWallpaperLegibilityContainerView
- _objc_msgSend$_performAlphaAnimationToAlpha:
- _objc_msgSend$fadeAlpha
- _objc_msgSend$isPerformingAlphaAnimation
- _objc_msgSend$mask
- _objc_msgSend$notificationDimView
- _objc_msgSend$setCustomSubtitle:
- _objc_msgSend$setCustomSubtitle:withTimeout:
- _objc_msgSend$setFadeAlpha:
- _objc_msgSend$setIsPerformingAlphaAnimation:
- _objc_msgSend$wallpaperLegibilityContainerView
CStrings:
+ "@\"CSNotificationLegibilityDimController\""
+ "@\"CSNotificationLegibilityDimView\""
+ "@\"PLKLegibilityEnvironment\""
+ "@\"UITraitCollection\""
+ "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48"
+ "About to create date subtitle for the charging estimate ."
+ "CSCoverSheetDimmingDispatchGroup"
+ "CSNotificationLegibilityDimController"
+ "CSNotificationLegibilityDimController set dimLevel to %ld; fadeAnchorY: %.2f; effectiveFadeInThreshold: %.2f; isDimVisible: %d; fullDimHeight: %.2f"
+ "CSNotificationLegibilityDimView"
+ "Check if the charging estimate needs to be shown"
+ "Extended Subtitle Timeout Multiplier"
+ "Received PLKLegibilityEnvironment update with new average color: %@, wallpaper luminance: %.2f"
+ "SecureAppSliderVisible"
+ "T@\"CSNotificationLegibilityDimController\",&,N,V_notificationLegibilityDimController"
+ "T@\"CSNotificationLegibilityDimView\",&,N,V_notificationLegibilityFullBaseLayerDimView"
+ "T@\"CSNotificationLegibilityDimView\",&,N,V_notificationLegibilityLocalizedDimView"
+ "T@\"CSNotificationLegibilityDimView\",R,N,V_wallpaperFloatingLayerContainerView"
+ "T@\"NSMutableArray\",&,N,V_mutableDimViews"
+ "T@\"PLKLegibilityEnvironment\",&,N,V_wallpaperLegibilityEnvironment"
+ "T@\"UITraitCollection\",&,N,V_traitCollection"
+ "TB,N,GisBackgroundContentViewDimmed,V_backgroundContentViewDimmed"
+ "TB,N,GisDimVisible,V_dimVisible"
+ "Td,N,V_extendedSubtitleStringTimeoutMultiplier"
+ "Td,N,V_fullDimHeight"
+ "Td,N,V_glassLuminanceValue"
+ "Tq,N,V_currentDimLevel"
+ "Tq,R,N,V_dimType"
+ "[Widget Row] Widget row using bottom position: %{bool}u for poster configuration requested bottom position: %{bool}u, depth effect enabled: %{bool}u"
+ "_addNotificationLegibilityFullBaseLayerDimView"
+ "_addNotificationLegibilityLocalizedDimView"
+ "_animateLayer:toValues:forKeyPath:duration:dispatchGroup:"
+ "_animateToDimming:withDuration:dispatchGroup:"
+ "_animateUsingSpringWithDampingRatio:response:tracking:dampingRatioSmoothing:responseSmoothing:targetSmoothing:projectionDeceleration:retargetImpulse:animations:completion:"
+ "_backgroundContentViewDimmed"
+ "_backgroundContentViewMatchMoveDisabledReasons"
+ "_configureColorMatrix"
+ "_currentDimLevel"
+ "_dimType"
+ "_dimVisible"
+ "_evaluateBackgroundContentViewMatchMove"
+ "_extendedSubtitleStringTimeoutMultiplier"
+ "_filterForDimming:"
+ "_filterNumbersForDimming:"
+ "_fullDimColorMatrix"
+ "_fullDimHeight"
+ "_glassLuminanceValue"
+ "_isBackgroundContentViewMatchMoveActive"
+ "_layoutBlendingMask"
+ "_layoutDimViews"
+ "_layoutLayer:inBounds:withHorizontalOutset:"
+ "_layoutNotificationLegibilityFullBaseLayerView"
+ "_layoutNotificationLegibilityLocalizedDimView"
+ "_localizedDimColorMatrix"
+ "_luminance"
+ "_mutableDimViews"
+ "_noDimColorMatrix"
+ "_notificationLegibilityDimController"
+ "_notificationLegibilityFullBaseLayerDimView"
+ "_notificationLegibilityLocalizedDimView"
+ "_refractionHeight"
+ "_setBackgroundContentViewMatchMoveActive:"
+ "_traitCollection"
+ "_updateDimViewsForced:"
+ "_updateDimViewsWithDimLevel:"
+ "_updateGlassContentInterfaceStyle"
+ "_wallpaperLegibilityEnvironment"
+ "addDimView:"
+ "averageColor"
+ "backgroundContentViewDimmed"
+ "colorMatrix"
+ "currentDimLevel"
+ "dimType"
+ "dimVisible"
+ "extendedSubtitleStringTimeoutMultiplier"
+ "filters.colorMatrix.inputColorMatrix"
+ "fullDimHeight"
+ "glassLuminanceValue"
+ "homeAffordanceViewControllerDidRecognizeSingleClick:"
+ "initWithFrame:dimType:"
+ "isBackgroundContentViewDimmed"
+ "isDimVisible"
+ "layoutInsetsForSize:"
+ "legibilityEnvironment"
+ "legibilityEnvironmentContextForVariant:"
+ "luma"
+ "mutableDimViews"
+ "notificationLegibilityDimController"
+ "notificationLegibilityFullBaseLayerDimView"
+ "notificationLegibilityLocalizedDimView"
+ "secureWindowVisibilityDidChange:"
+ "setBackgroundContentViewDimmed:"
+ "setCurrentDimLevel:"
+ "setCustomSubtitle:withPriority:withTimeout:"
+ "setDimVisible:"
+ "setExtendedSubtitleStringTimeoutMultiplier:"
+ "setFullDimHeight:"
+ "setGlassLuminanceValue:"
+ "setMutableDimViews:"
+ "setNotificationLegibilityDimController:"
+ "setNotificationLegibilityFullBaseLayerDimView:"
+ "setNotificationLegibilityLocalizedDimView:"
+ "setShouldDim:"
+ "setSuppressesBackgroundContentMatchMove:forReason:"
+ "setTraitCollection:"
+ "setWallpaperLegibilityEnvironment:"
+ "shouldDim"
+ "shouldDim:"
+ "updateDimViews"
+ "updateGlassContentInterfaceStyle:luminanceValue:"
+ "updateGlassContentInterfaceStyleToUserInterfaceStyle:luminanceValue:"
+ "v32@0:8q16d24"
+ "v32@?0@\"CSNotificationLegibilityDimView\"8Q16^B24"
+ "v36@0:8B16d20@28"
+ "v64@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24d56"
+ "valueWithCAColorMatrix:"
+ "wallpaperLegibilityEnvironment"
+ "wallpaperLegibilityEnvironmentDidChange:"
+ "{?=\"homeAffordanceViewControllerDidRecognizeSingleTap\"b1\"homeAffordanceViewControllerDidRecognizeDoubleTap\"b1\"homeAffordanceViewControllerDidFailToRecognizeDoubleTap\"b1\"homeAffordanceViewControllerDidCompleteHomeAffordanceHintAnimation\"b1\"homeAffordanceViewControllerDidRecognizeSingleClick\"b1}"
+ "{CAColorMatrix=ffffffffffffffffffff}16@0:8"
+ "{UIEdgeInsets=dddd}32@0:8{CGSize=dd}16"
+ "\xf0\xe2\xf0\xf0\xf0\x91"
- "@\"CSNotificationDimView\""
- "CSNotificationDimView"
- "T@\"CALayer\",&,N,V_shadowMaskLayer"
- "T@\"CSNotificationDimView\",&,N,V_notificationDimView"
- "T@\"UITapGestureRecognizer\",&,N,V_homeAffordanceClickGestureRecognizer"
- "T@\"UIView\",R,N,V_wallpaperFloatingLayerContainerView"
- "T@\"UIView\",R,N,V_wallpaperLegibilityContainerView"
- "TB,N,V_isPerformingAlphaAnimation"
- "Td,N,V_fadeAlpha"
- "Td,R,N,V_effectiveFadeRadiusY"
- "_addNotificationDimView"
- "_addWallpaperLegibilityContainerView"
- "_animateByRetargetingAnimations:completion:"
- "_animateUsingSpringInteractive:animations:completion:"
- "_configureFilter"
- "_configureShadowMask"
- "_effectiveFadeRadiusY"
- "_fadeAlpha"
- "_homeAffordanceClickGestureRecognizer"
- "_homeAffordanceClickRecognized:"
- "_isPerformingAlphaAnimation"
- "_isPointerTouch"
- "_layoutNotificationDimView"
- "_layoutShadowMask"
- "_layoutWallpaperLegibilityContainerView"
- "_notificationDimView"
- "_performAlphaAnimationToAlpha:"
- "_shadowMaskLayer"
- "_wallpaperLegibilityContainerView"
- "effectiveFadeRadiusY"
- "fadeAlpha"
- "homeAffordanceClickGestureRecognizer"
- "isPerformingAlphaAnimation"
- "mask"
- "notificationDimView"
- "setCustomSubtitle:"
- "setCustomSubtitle:withTimeout:"
- "setFadeAlpha:"
- "setHomeAffordanceClickGestureRecognizer:"
- "setIsPerformingAlphaAnimation:"
- "setNotificationDimView:"
- "setShadowMaskLayer:"
- "shadowMaskLayer"
- "wallpaperLegibilityContainerView"
- "{?=\"homeAffordanceViewControllerDidRecognizeSingleTap\"b1\"homeAffordanceViewControllerDidRecognizeDoubleTap\"b1\"homeAffordanceViewControllerDidFailToRecognizeDoubleTap\"b1\"homeAffordanceViewControllerDidCompleteHomeAffordanceHintAnimation\"b1}"
- "\xf0\xc2\xf0\xf0\xf0\x91"

```
