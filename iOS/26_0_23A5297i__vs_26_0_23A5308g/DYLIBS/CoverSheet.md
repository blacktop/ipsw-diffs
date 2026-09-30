## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4557.0.6.103.0
-  __TEXT.__text: 0x163de8
-  __TEXT.__auth_stubs: 0x13e0
+4557.0.9.100.0
+  __TEXT.__text: 0x163c24
+  __TEXT.__auth_stubs: 0x1400
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x15f54
+  __TEXT.__objc_methlist: 0x16064
   __TEXT.__const: 0x2ab0
-  __TEXT.__cstring: 0x9fa4
-  __TEXT.__oslogstring: 0x8a38
-  __TEXT.__gcc_except_tab: 0xd30
+  __TEXT.__cstring: 0xa03c
+  __TEXT.__oslogstring: 0x8aef
+  __TEXT.__gcc_except_tab: 0xccc
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x4080
-  __TEXT.__objc_classname: 0x3488
-  __TEXT.__objc_methname: 0x3fcca
-  __TEXT.__objc_methtype: 0x9c89
-  __TEXT.__objc_stubs: 0x25440
-  __DATA_CONST.__got: 0x1558
-  __DATA_CONST.__const: 0x2a58
+  __TEXT.__unwind_info: 0x40b8
+  __TEXT.__objc_classname: 0x3487
+  __TEXT.__objc_methname: 0x400e2
+  __TEXT.__objc_methtype: 0x9cbc
+  __TEXT.__objc_stubs: 0x25660
+  __DATA_CONST.__got: 0x1560
+  __DATA_CONST.__const: 0x2a80
   __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc2d8
+  __DATA_CONST.__objc_selrefs: 0xc3a8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x5e0
   __DATA_CONST.__objc_arraydata: 0x1078
-  __AUTH_CONST.__auth_got: 0xa00
-  __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0xbd80
-  __AUTH_CONST.__objc_const: 0x3c310
+  __AUTH_CONST.__auth_got: 0xa10
+  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__cfstring: 0xbec0
+  __AUTH_CONST.__objc_const: 0x3c3f0
   __AUTH_CONST.__objc_doubleobj: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x1248
   __AUTH_CONST.__objc_intobj: 0x438
-  __AUTH.__objc_data: 0x1450
-  __DATA.__objc_ivar: 0x1b04
+  __AUTH.__objc_data: 0x1310
+  __DATA.__objc_ivar: 0x1b14
   __DATA.__data: 0x4e68
   __DATA.__bss: 0xd0
-  __DATA_DIRTY.__objc_data: 0x37a0
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__objc_data: 0x38e0
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6036ABAD-D07E-38FE-81DC-12B9A98C8782
-  Functions: 7039
-  Symbols:   25765
-  CStrings:  14151
+  UUID: 9F38360F-7919-38A8-9B83-E67650A9249E
+  Functions: 7063
+  Symbols:   25842
+  CStrings:  14207
 
Symbols:
+ +[CSBatteryChargingRingView _pointsPerMillimeter]
+ +[CSBatteryChargingRingView _pointsPerMillimeter].cold.1
+ +[CSBatteryChargingView batteryChargingRingViewWithConfiguration:externalBattery:]
+ -[CSBatteryChargingRingView _auxillaryGlyphImageForConfig:]
+ -[CSBatteryChargingRingView _defaultSilhouettePhysicalSize]
+ -[CSBatteryChargingRingView _silhouetteBottomOffset]
+ -[CSBatteryChargingRingView _silhouetteBottomToAuxillaryRingInset]
+ -[CSBatteryChargingRingView _silhouetteConfiguration]
+ -[CSBatteryChargingRingView _silhouetteCornerRadius]
+ -[CSBatteryChargingRingView _silhouettePhysicalSizeInMillimeters]
+ -[CSBatteryChargingRingView externalBattery]
+ -[CSBatteryChargingRingView initWithFrame:configuration:externalBattery:]
+ -[CSBatteryChargingRingView setExternalBattery:]
+ -[CSCombinedListViewController updateGlassContentInterfaceStyle:glassLuminanceValue:wallpaperLuminanceValue:]
+ -[CSCoverSheetView _layoutBackgroundContentViewForPresentationValueChange]
+ -[CSCoverSheetView _updateBackgroundContainerPinningAnimation]
+ -[CSCoverSheetView didMoveToWindow]
+ -[CSCoverSheetView setCoverSheetPresentationProgress:forPresentationValue:]
+ -[CSCoverSheetViewController _reduceMotionDidChange:]
+ -[CSCoverSheetViewController accessoryBehavior]
+ -[CSCoverSheetViewController dismissModalPresentationAnimated:completion:]
+ -[CSCoverSheetViewController frameForContentViewForContainerBounds:]
+ -[CSCoverSheetViewController landscapeBehavior]
+ -[CSCoverSheetViewController posterBoardBehavior]
+ -[CSCoverSheetViewController screenOffBehavior]
+ -[CSCoverSheetViewController setAccessoryBehavior:]
+ -[CSCoverSheetViewController setLandscapeBehavior:]
+ -[CSCoverSheetViewController setPosterBoardBehavior:]
+ -[CSCoverSheetViewController setScreenOffBehavior:]
+ -[CSCoverSheetViewController updateBackgroundGlassEffectForDraggingProgress:]
+ -[CSCoverSheetViewController updateCoverSheetDraggingProgress:forPresentationValue:]
+ -[CSCoverSheetViewController viewDidLayoutSubviews]
+ -[CSNotificationLegibilityDimController addDimView:].cold.1
+ -[CSWidgetGridViewController updatePresentationStyleForNewOrientation:]
+ GCC_except_table171
+ GCC_except_table212
+ GCC_except_table311
+ GCC_except_table451
+ GCC_except_table509
+ GCC_except_table529
+ GCC_except_table540
+ GCC_except_table619
+ GCC_except_table676
+ GCC_except_table686
+ GCC_except_table688
+ GCC_except_table697
+ GCC_except_table709
+ GCC_except_table719
+ GCC_except_table86
+ GCC_except_table89
+ _MGCopyAnswer
+ _OBJC_IVAR_$_CSBatteryChargingRingView._externalBattery
+ _OBJC_IVAR_$_CSCoverSheetView._coverSheetPresentationProgressModelValue
+ _OBJC_IVAR_$_CSCoverSheetView._coverSheetPresentationProgressPresentationValue
+ _OBJC_IVAR_$_CSCoverSheetViewController._accessoryBehavior
+ _OBJC_IVAR_$_CSCoverSheetViewController._appearanceOrientation
+ _OBJC_IVAR_$_CSCoverSheetViewController._landscapeBehavior
+ _OBJC_IVAR_$_CSCoverSheetViewController._posterBoardBehavior
+ _OBJC_IVAR_$_CSCoverSheetViewController._screenOffBehavior
+ _SBFStringForUIInterfaceOrientation
+ _UIAccessibilityReduceMotionStatusDidChangeNotification
+ __OBJC_$_CLASS_METHODS_CSBatteryChargingRingView
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.813
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.817
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.818
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.819
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.192
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.196
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.205
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.199
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.208
+ ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.779
+ ___49+[CSBatteryChargingRingView _pointsPerMillimeter]_block_invoke
+ ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.684
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.458
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.459
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.467
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.747
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.748
+ ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.497
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.790
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.791
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.798
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.796
+ ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.593
+ ___89-[CSCoverSheetViewController _updateActiveBehaviorsForReason:updatingAppearanceIfNeeded:]_block_invoke.657
+ ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.594
+ ___98-[CSCoverSheetViewController activateCameraWithHostableEntity:animated:sendingActions:completion:]_block_invoke.150
+ ___block_descriptor_40_e8_32s_e33_v24?0"CSBehavior"8"NSString"16ls32l8
+ ___block_literal_global.198
+ ___block_literal_global.227
+ ___block_literal_global.2335
+ ___block_literal_global.342
+ ___block_literal_global.410
+ ___block_literal_global.415
+ ___block_literal_global.425
+ ___block_literal_global.430
+ ___block_literal_global.435
+ ___block_literal_global.808
+ ___block_literal_global.810
+ __pointsPerMillimeter.onceToken
+ __pointsPerMillimeter.pointsPerMM
+ _objc_msgSend$_auxillaryGlyphImageForConfig:
+ _objc_msgSend$_defaultSilhouettePhysicalSize
+ _objc_msgSend$_layoutBackgroundContentViewForPresentationValueChange
+ _objc_msgSend$_setPresentationValue:forKey:
+ _objc_msgSend$_silhouetteBottomOffset
+ _objc_msgSend$_silhouetteBottomToAuxillaryRingInset
+ _objc_msgSend$_silhouetteConfiguration
+ _objc_msgSend$_silhouetteCornerRadius
+ _objc_msgSend$_updateBackgroundContainerPinningAnimation
+ _objc_msgSend$batteryChargingRingViewWithConfiguration:externalBattery:
+ _objc_msgSend$coverSheetViewControllerDidPresentPasscodeLockView:
+ _objc_msgSend$dismissModalPresentationAnimated:completion:
+ _objc_msgSend$initWithFrame:configuration:externalBattery:
+ _objc_msgSend$nativeScale
+ _objc_msgSend$setCoverSheetPresentationProgress:forPresentationValue:
+ _objc_msgSend$setSilhouette:
+ _objc_msgSend$setSilhouetteLayer:
+ _objc_msgSend$setTimeGlassInterfaceStyle:
+ _objc_msgSend$undimmedLightPasscodeLockViewForUsersCurrentStyle
+ _objc_msgSend$undimmedPasscodeLockViewForUsersCurrentStyle
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateGlassContentInterfaceStyle:glassLuminanceValue:wallpaperLuminanceValue:
+ _objc_msgSend$updateGlassContentInterfaceStyleToUserInterfaceStyle:glassLuminanceValue:wallpaperLuminanceValue:
+ _objc_msgSend$updatePresentationStyleForNewOrientation:
+ _objc_msgSend$valueWithCGPoint:
+ _objc_msgSend$valueWithCGRect:
- -[CSCombinedListViewController updateGlassContentInterfaceStyle:luminanceValue:]
- -[CSCoverSheetView _evaluateBackgroundContentViewMatchMove]
- -[CSCoverSheetView _setBackgroundContentViewMatchMoveActive:]
- -[CSCoverSheetView backgroundContentViewOffset]
- -[CSCoverSheetView backgroundContentViewScale]
- -[CSCoverSheetView setBackgroundContentViewOffset:]
- -[CSCoverSheetView setBackgroundContentViewOffset:scale:]
- -[CSCoverSheetView setBackgroundContentViewScale:]
- -[CSCoverSheetView setSuppressesBackgroundContentMatchMove:forReason:]
- -[CSCoverSheetViewController secureWindowVisibilityDidChange:]
- -[CSCoverSheetViewController updateCoverSheetDraggingProgress:]
- -[CSWidgetGridViewController _updatePresentationStyleForNewOrientation:]
- GCC_except_table169
- GCC_except_table209
- GCC_except_table308
- GCC_except_table448
- GCC_except_table506
- GCC_except_table526
- GCC_except_table536
- GCC_except_table614
- GCC_except_table671
- GCC_except_table681
- GCC_except_table683
- GCC_except_table692
- GCC_except_table704
- GCC_except_table714
- GCC_except_table85
- GCC_except_table88
- _OBJC_IVAR_$_CSCoverSheetView._backgroundContentViewMatchMoveDisabledReasons
- _OBJC_IVAR_$_CSCoverSheetView._backgroundContentViewOffset
- _OBJC_IVAR_$_CSCoverSheetView._backgroundContentViewScale
- _OBJC_IVAR_$_CSCoverSheetView._isBackgroundContentViewMatchMoveActive
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.789
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.793
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.794
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.795
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.193
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.197
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.206
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.200
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.209
- ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.755
- ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.661
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.452
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.453
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.461
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.724
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke_2
- ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.491
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.766
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.767
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.774
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.772
- ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.587
- ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.588
- ___98-[CSCoverSheetViewController activateCameraWithHostableEntity:animated:sendingActions:completion:]_block_invoke.148
- ___block_literal_global.199
- ___block_literal_global.228
- ___block_literal_global.2286
- ___block_literal_global.336
- ___block_literal_global.404
- ___block_literal_global.409
- ___block_literal_global.414
- ___block_literal_global.419
- ___block_literal_global.424
- ___block_literal_global.429
- ___block_literal_global.784
- ___block_literal_global.786
- _objc_msgSend$_evaluateBackgroundContentViewMatchMove
- _objc_msgSend$_setBackgroundContentViewMatchMoveActive:
- _objc_msgSend$lightPasscodeLockViewForUsersCurrentStyle
- _objc_msgSend$passcodeLockViewForUsersCurrentStyle
- _objc_msgSend$setBackgroundContentViewOffset:scale:
- _objc_msgSend$setForceOnlyFadeAnimations:
- _objc_msgSend$setSuppressesBackgroundContentMatchMove:forReason:
- _objc_msgSend$updateGlassContentInterfaceStyle:luminanceValue:
- _objc_msgSend$updateGlassContentInterfaceStyleToUserInterfaceStyle:luminanceValue:
CStrings:
+ "@64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56"
+ "CSCoverSheetViewController will force orientation update from %@ to %@. This should only occur on device boot or if SpringBoard was recently killed."
+ "CSNotificationLegibilityDimController adding nil dimView is not expected!"
+ "CaptureButton"
+ "Forced Orientation Change"
+ "Forced Orientation Update"
+ "QuickActionButtons"
+ "SB_COVERSHEET_TO_POSTER_SWITCHER_GESTURE"
+ "T@\"BCBatteryDevice\",&,N,V_externalBattery"
+ "T@\"CSBehavior\",&,N,V_accessoryBehavior"
+ "T@\"CSBehavior\",&,N,V_landscapeBehavior"
+ "T@\"CSBehavior\",&,N,V_posterBoardBehavior"
+ "T@\"CSBehavior\",&,N,V_screenOffBehavior"
+ "[Behavior] Restricted capabilities: %{public}@ from %@"
+ "[Charge UI] visible %d, showBattery NO – isAlreadyShowingChargingModal: %d"
+ "[Charge UI] – endedShowingChargingModal: %d"
+ "_accessoryBehavior"
+ "_appearanceOrientation"
+ "_auxillaryGlyphImageForConfig:"
+ "_coverSheetPresentationProgressModelValue"
+ "_coverSheetPresentationProgressPresentationValue"
+ "_defaultSilhouettePhysicalSize"
+ "_externalBattery"
+ "_landscapeBehavior"
+ "_layoutBackgroundContentViewForPresentationValueChange"
+ "_pointsPerMillimeter"
+ "_posterBoardBehavior"
+ "_reduceMotionDidChange:"
+ "_screenOffBehavior"
+ "_setPresentationValue:forKey:"
+ "_silhouetteBottomOffset"
+ "_silhouetteBottomToAuxillaryRingInset"
+ "_silhouetteConfiguration"
+ "_silhouetteCornerRadius"
+ "_silhouettePhysicalSizeInMillimeters"
+ "_updateBackgroundContainerPinningAnimation"
+ "accessoryBehavior"
+ "batteryChargingRingViewWithConfiguration:externalBattery:"
+ "coverSheetViewControllerDidPresentPasscodeLockView:"
+ "didMoveToWindow"
+ "dismissModalPresentationAnimated:completion:"
+ "externalBattery"
+ "frameForContentViewForContainerBounds:"
+ "initWithFrame:configuration:externalBattery:"
+ "landscape"
+ "landscapeBehavior"
+ "local"
+ "main-screen-pitch"
+ "nativeScale"
+ "notificationStructuredListViewController:didUpdateNotificationsVisibilityInViewport:"
+ "posterBoard"
+ "posterBoardBehavior"
+ "screenOffBehavior"
+ "setAccessoryBehavior:"
+ "setCoverSheetPresentationProgress:forPresentationValue:"
+ "setExternalBattery:"
+ "setLandscapeBehavior:"
+ "setPosterBoardBehavior:"
+ "setScreenOffBehavior:"
+ "setTimeGlassInterfaceStyle:"
+ "undimmedLightPasscodeLockViewForUsersCurrentStyle"
+ "undimmedPasscodeLockViewForUsersCurrentStyle"
+ "unsignedIntValue"
+ "updateBackgroundGlassEffectForDraggingProgress:"
+ "updateCoverSheetDraggingProgress:forPresentationValue:"
+ "updateGlassContentInterfaceStyle:glassLuminanceValue:wallpaperLuminanceValue:"
+ "updateGlassContentInterfaceStyleToUserInterfaceStyle:glassLuminanceValue:wallpaperLuminanceValue:"
+ "updatePresentationStyleForNewOrientation:"
+ "v24@?0@\"CSBehavior\"8@\"NSString\"16"
+ "v40@0:8q16d24d32"
+ "valueWithCGPoint:"
+ "valueWithCGRect:"
+ "\xf0\xe2\xf0\xf0\xf0\x81"
- "Orientation Change"
- "SecureAppSliderVisible"
- "Td,N,V_backgroundContentViewScale"
- "T{CGPoint=dd},N,V_backgroundContentViewOffset"
- "[Behavior] Restricted capabilities: %{public}@ from iris"
- "[Behavior] Restricted capabilities: %{public}@ from local"
- "[Charge UI][Lift Wake] visible %d, showBattery NO – isAlreadyShowingChargingModal: %d"
- "[Charge UI][Lift Wake] – endedShowingChargingModal: %d"
- "_backgroundContentViewMatchMoveDisabledReasons"
- "_backgroundContentViewOffset"
- "_backgroundContentViewScale"
- "_evaluateBackgroundContentViewMatchMove"
- "_isBackgroundContentViewMatchMoveActive"
- "_setBackgroundContentViewMatchMoveActive:"
- "_updatePresentationStyleForNewOrientation:"
- "backgroundContentViewOffset"
- "backgroundContentViewScale"
- "lightPasscodeLockViewForUsersCurrentStyle"
- "passcodeLockViewForUsersCurrentStyle"
- "secureWindowVisibilityDidChange:"
- "setBackgroundContentViewOffset:"
- "setBackgroundContentViewOffset:scale:"
- "setBackgroundContentViewScale:"
- "setForceOnlyFadeAnimations:"
- "setSuppressesBackgroundContentMatchMove:forReason:"
- "updateCoverSheetDraggingProgress:"
- "updateGlassContentInterfaceStyle:luminanceValue:"
- "updateGlassContentInterfaceStyleToUserInterfaceStyle:luminanceValue:"
- "v32@0:8q16d24"
- "\xf0\xe2\xf0\xf0\xf0\x91"

```
