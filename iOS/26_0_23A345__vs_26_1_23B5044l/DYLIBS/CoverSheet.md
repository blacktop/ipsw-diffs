## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4557.0.10.114.0
-  __TEXT.__text: 0x170b60
-  __TEXT.__auth_stubs: 0x1410
+4557.1.8.105.0
+  __TEXT.__text: 0x171678
+  __TEXT.__auth_stubs: 0x1400
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x16114
+  __TEXT.__objc_methlist: 0x161b4
   __TEXT.__const: 0x2bf0
-  __TEXT.__cstring: 0xa0ba
+  __TEXT.__cstring: 0xa05a
   __TEXT.__oslogstring: 0x8c19
   __TEXT.__gcc_except_tab: 0xcfc
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x40e0
-  __TEXT.__objc_classname: 0x3487
-  __TEXT.__objc_methname: 0x4051e
-  __TEXT.__objc_methtype: 0x9cfd
-  __TEXT.__objc_stubs: 0x25940
-  __DATA_CONST.__got: 0x1568
+  __TEXT.__unwind_info: 0x4108
+  __TEXT.__objc_classname: 0x3489
+  __TEXT.__objc_methname: 0x4074f
+  __TEXT.__objc_methtype: 0x9d1c
+  __TEXT.__objc_stubs: 0x25aa0
+  __DATA_CONST.__got: 0x1580
   __DATA_CONST.__const: 0x2a90
   __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc458
+  __DATA_CONST.__objc_selrefs: 0xc4a8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x5e0
   __DATA_CONST.__objc_arraydata: 0x1078
-  __AUTH_CONST.__auth_got: 0xa18
-  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__auth_got: 0xa10
+  __AUTH_CONST.__const: 0x860
   __AUTH_CONST.__cfstring: 0xbf40
-  __AUTH_CONST.__objc_const: 0x3c508
+  __AUTH_CONST.__objc_const: 0x3c5a0
   __AUTH_CONST.__objc_doubleobj: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x1248
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH.__objc_data: 0x1310
-  __DATA.__objc_ivar: 0x1b30
+  __DATA.__objc_ivar: 0x1b44
   __DATA.__data: 0x4e68
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x38e0
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/ActivityProgressKit.framework/ActivityProgressKit
   - /System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices
   - /System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 47702399-8D8A-30C6-92AD-1C4F6D52ADBC
-  Functions: 7082
-  Symbols:   25914
-  CStrings:  14252
+  UUID: A27931A7-F633-3ED6-9B18-C1C53BF108E1
+  Functions: 7093
+  Symbols:   25951
+  CStrings:  14268
 
Symbols:
+ -[CSActivityFullScreenViewController _newDisplayLayoutElement]
+ -[CSActivityFullScreenViewController _updateDisplayLayoutElementForActivation:]
+ -[CSActivityFullScreenViewController viewDidMoveToWindow:shouldAppearOrDisappear:]
+ -[CSChargingViewController _hasBatteryPack]
+ -[CSCoverSheetView _addNotificationLegibilityContainers]
+ -[CSCoverSheetView _evaluateBackgroundContentViewMatchMove]
+ -[CSCoverSheetView _layoutNotificationLegibilityContainerViews]
+ -[CSCoverSheetView _makeView:untouchable:]
+ -[CSCoverSheetView _setBackgroundContentViewMatchMoveActive:]
+ -[CSCoverSheetView hitTest:withEvent:]
+ -[CSCoverSheetView setClipping:corners:radius:]
+ -[CSCoverSheetView setSuppressesBackgroundContentMatchMove:forReason:]
+ -[CSCoverSheetViewController _setHasContentAboveCoverSheet:opaque:isSignificantUserInteraction:]
+ -[CSCoverSheetViewController willUIUnlockFromSource:isLockScreenDisabledForAssertion:]
+ _OBJC_CLASS_$_APKActivityProgressEventAction
+ _OBJC_CLASS_$__UITraitGlassElevationLevel
+ _OBJC_IVAR_$_CSCoverSheetView._backgroundContentViewMatchMoveDisabledReasons
+ _OBJC_IVAR_$_CSCoverSheetView._isBackgroundContentViewMatchMoveActive
+ _OBJC_IVAR_$_CSCoverSheetView._notificationLegibiltyAboveDateTimeContainerView
+ _OBJC_IVAR_$_CSCoverSheetView._notificationLegibiltyBelowDateTimeContainerView
+ _OBJC_IVAR_$_CSCoverSheetViewController._hasOpaqueContentAboveCoverSheet
+ _SBSDisplayLayoutElementTodayViewIdentifier
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.819
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.823
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.824
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.825
+ ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.785
+ ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.687
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.461
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.462
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.470
+ ___58-[CSActivityManager _addActivityListItemForContentUpdate:]_block_invoke.52
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.750
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.751
+ ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.500
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.796
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.797
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.804
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.802
+ ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.596
+ ___86-[CSCoverSheetViewController willUIUnlockFromSource:isLockScreenDisabledForAssertion:]_block_invoke
+ ___89-[CSCoverSheetViewController _updateActiveBehaviorsForReason:updatingAppearanceIfNeeded:]_block_invoke.660
+ ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.597
+ ___block_descriptor_80_e8_32r40r48r56r64r72r_e65_v32?0"FBSDisplayLayoutElement<SBSDisplayLayoutElement>"8Q16^B24lr32l8r40l8r48l8r56l8r64l8r72l8
+ ___block_literal_global.104
+ ___block_literal_global.112
+ ___block_literal_global.2346
+ ___block_literal_global.345
+ ___block_literal_global.413
+ ___block_literal_global.423
+ ___block_literal_global.428
+ ___block_literal_global.433
+ ___block_literal_global.438
+ ___block_literal_global.814
+ ___block_literal_global.816
+ _objc_msgSend$_addNotificationLegibilityContainers
+ _objc_msgSend$_evaluateBackgroundContentViewMatchMove
+ _objc_msgSend$_hasBatteryPack
+ _objc_msgSend$_layoutNotificationLegibilityContainerViews
+ _objc_msgSend$_makeView:untouchable:
+ _objc_msgSend$_setBackgroundContentViewMatchMoveActive:
+ _objc_msgSend$_setHasContentAboveCoverSheet:opaque:isSignificantUserInteraction:
+ _objc_msgSend$handleScreenOff:
+ _objc_msgSend$isDisplayLayoutElementActive
+ _objc_msgSend$isPhoneUnlockEnabledAndRequirementsMet
+ _objc_msgSend$setClipping:corners:radius:
+ _objc_msgSend$setNSIntegerValue:forTrait:
+ _objc_msgSend$setSuppressesBackgroundContentMatchMove:forReason:
+ _objc_msgSend$traitOverrides
- -[CSActivityManager init].cold.1
- -[CSCoverSheetViewController willUIUnlockFromSource:]
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.816
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.820
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.821
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.822
- ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.782
- ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.684
- ___53-[CSCoverSheetViewController willUIUnlockFromSource:]_block_invoke
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.458
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.459
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.467
- ___58-[CSActivityManager _addActivityListItemForContentUpdate:]_block_invoke.54
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.747
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.748
- ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.497
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.793
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.794
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.801
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.799
- ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.593
- ___89-[CSCoverSheetViewController _updateActiveBehaviorsForReason:updatingAppearanceIfNeeded:]_block_invoke.657
- ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.594
- _____loadActivityProgressKitIfNecessary_block_invoke
- ___block_descriptor_64_e8_32r40r48r56r_e65_v32?0"FBSDisplayLayoutElement<SBSDisplayLayoutElement>"8Q16^B24lr32l8r40l8r48l8r56l8
- ___block_literal_global.106
- ___block_literal_global.114
- ___block_literal_global.2339
- ___block_literal_global.342
- ___block_literal_global.410
- ___block_literal_global.415
- ___block_literal_global.425
- ___block_literal_global.430
- ___block_literal_global.435
- ___block_literal_global.811
- ___block_literal_global.813
- ___loadActivityProgressKitIfNecessary.activityProgressKit
- ___loadActivityProgressKitIfNecessary.onceToken
- _dlopen
- _objc_msgSend$handleScreenOff
- _objc_msgSend$isPhoneUnlockWithVisionSupportedAndEnabled
- _objc_msgSend$phoneUnlockEnabledAndRequirementsMet
CStrings:
+ "B24@0:8i16B20"
+ "CoverSheetRotation"
+ "_addNotificationLegibilityContainers"
+ "_backgroundContentViewMatchMoveDisabledReasons"
+ "_evaluateBackgroundContentViewMatchMove"
+ "_hasBatteryPack"
+ "_hasOpaqueContentAboveCoverSheet"
+ "_isBackgroundContentViewMatchMoveActive"
+ "_layoutNotificationLegibilityContainerViews"
+ "_makeView:untouchable:"
+ "_notificationLegibiltyAboveDateTimeContainerView"
+ "_notificationLegibiltyBelowDateTimeContainerView"
+ "_setBackgroundContentViewMatchMoveActive:"
+ "_setHasContentAboveCoverSheet:opaque:isSignificantUserInteraction:"
+ "handleScreenOff:"
+ "isPhoneUnlockEnabledAndRequirementsMet"
+ "setClipping:corners:radius:"
+ "setNSIntegerValue:forTrait:"
+ "setSuppressesBackgroundContentMatchMove:forReason:"
+ "traitOverrides"
+ "v36@0:8B16Q20d28"
+ "willUIUnlockFromSource:isLockScreenDisabledForAssertion:"
+ "\xf0\xf02\xf0\xf0\xf0\x91"
- "/System/Library/PrivateFrameworks/ActivityProgressKit.framework/ActivityProgressKit"
- "APKActivityProgressEventAction"
- "handleScreenOff"
- "isPhoneUnlockWithVisionSupportedAndEnabled"
- "notificationStructuredListViewControllerDidScrollToRevealNotificationHistory:"
- "willUIUnlockFromSource:"
- "\xf0\xe2\xf0\xf0\xf0\x91"

```
