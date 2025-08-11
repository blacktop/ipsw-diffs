## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4557.0.9.100.0
-  __TEXT.__text: 0x163c24
+4557.0.10.106.0
+  __TEXT.__text: 0x1648bc
   __TEXT.__auth_stubs: 0x1400
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x16064
-  __TEXT.__const: 0x2ab0
-  __TEXT.__cstring: 0xa03c
-  __TEXT.__oslogstring: 0x8aef
-  __TEXT.__gcc_except_tab: 0xccc
+  __TEXT.__objc_methlist: 0x1610c
+  __TEXT.__const: 0x2bc0
+  __TEXT.__cstring: 0xa08a
+  __TEXT.__oslogstring: 0x8c19
+  __TEXT.__gcc_except_tab: 0xcf8
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x40b8
+  __TEXT.__unwind_info: 0x40d8
   __TEXT.__objc_classname: 0x3487
-  __TEXT.__objc_methname: 0x400e2
-  __TEXT.__objc_methtype: 0x9cbc
-  __TEXT.__objc_stubs: 0x25660
+  __TEXT.__objc_methname: 0x4048a
+  __TEXT.__objc_methtype: 0x9ce9
+  __TEXT.__objc_stubs: 0x258a0
   __DATA_CONST.__got: 0x1560
-  __DATA_CONST.__const: 0x2a80
+  __DATA_CONST.__const: 0x2a88
   __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc3a8
+  __DATA_CONST.__objc_selrefs: 0xc440
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x5e0
   __DATA_CONST.__objc_arraydata: 0x1078
   __AUTH_CONST.__auth_got: 0xa10
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0xbec0
-  __AUTH_CONST.__objc_const: 0x3c3f0
+  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__cfstring: 0xbf00
+  __AUTH_CONST.__objc_const: 0x3c508
   __AUTH_CONST.__objc_doubleobj: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x1248
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH.__objc_data: 0x1310
-  __DATA.__objc_ivar: 0x1b14
+  __DATA.__objc_ivar: 0x1b30
   __DATA.__data: 0x4e68
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x38e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F38360F-7919-38A8-9B83-E67650A9249E
-  Functions: 7063
-  Symbols:   25842
-  CStrings:  14207
+  UUID: DDCE6363-6BCE-324B-8EC4-6752169CD39D
+  Functions: 7081
+  Symbols:   25905
+  CStrings:  14244
 
Symbols:
+ -[CSCombinedListViewController _exclusivelyHasMediaSupplementaryItems]
+ -[CSCombinedListViewController _hideNotificationsDefaultDidChange]
+ -[CSCombinedListViewController _hideNotificationsDefaultDidChange].cold.1
+ -[CSCombinedListViewController _updateMediaOnlyFlagInSupplementaryContainers]
+ -[CSCombinedListViewController _updateNotificationDimmingLayerLocalizedDimMode]
+ -[CSCombinedListViewController coverSheetViewController:didObscureWallpaper:]
+ -[CSCombinedListViewController notificationStructuredListViewController:didUpdateNotificationsVisibilityInViewport:]
+ -[CSCombinedListViewController notificationStructuredListViewController:isNotificationsHistoryRevealed:]
+ -[CSCoverSheetView _addNotificationLegibilityDynamicDimView]
+ -[CSCoverSheetView notificationLegibilityDynamicDimView]
+ -[CSCoverSheetView setNotificationLegibilityDynamicDimView:]
+ -[CSCoverSheetViewController _shouldAllowGlassCoverSheet].cold.1
+ -[CSCoverSheetViewController _updateAppearanceForHavingPosterSwitcherTransition:]
+ -[CSNotificationLegibilityDimController localizedDimMode]
+ -[CSNotificationLegibilityDimController setLocalizedDimMode:]
+ -[CSNotificationLegibilityDimController setShouldAnimate:]
+ -[CSNotificationLegibilityDimController shouldAnimate]
+ -[CSNotificationLegibilityDimView layoutInsetsForSize:fadeAnchorY:]
+ GCC_except_table216
+ GCC_except_table677
+ GCC_except_table687
+ GCC_except_table689
+ GCC_except_table698
+ GCC_except_table710
+ GCC_except_table720
+ GCC_except_table8
+ _OBJC_IVAR_$_CSCombinedListViewController._hasOnlyMediaInSupplementaryContainers
+ _OBJC_IVAR_$_CSCombinedListViewController._isWallpaperObscured
+ _OBJC_IVAR_$_CSCombinedListViewController._lockScreenDefaults
+ _OBJC_IVAR_$_CSCombinedListViewController._notificationsVisibleInViewport
+ _OBJC_IVAR_$_CSCoverSheetView._notificationLegibilityDynamicDimView
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._localizedDimMode
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._shouldAnimate
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.816
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.820
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.821
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.822
+ ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.782
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.793
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.794
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.801
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.799
+ ___69-[CSNotificationLegibilityDimController _updateDimViewsWithDimLevel:]_block_invoke_4
+ ___76-[CSCombinedListViewController initWithNibName:bundle:dndBedtimeController:]_block_invoke
+ ___block_literal_global.13
+ ___block_literal_global.2339
+ ___block_literal_global.811
+ ___block_literal_global.813
+ _objc_msgSend$_addNotificationLegibilityDynamicDimView
+ _objc_msgSend$_exclusivelyHasMediaSupplementaryItems
+ _objc_msgSend$_hideNotificationsDefaultDidChange
+ _objc_msgSend$_systemImageNamed:withConfiguration:
+ _objc_msgSend$_updateAppearanceForHavingPosterSwitcherTransition:
+ _objc_msgSend$_updateMediaOnlyFlagInSupplementaryContainers
+ _objc_msgSend$_updateNotificationDimmingLayerLocalizedDimMode
+ _objc_msgSend$animationDuration:
+ _objc_msgSend$disallowGlassLockScreen
+ _objc_msgSend$groupingIdentifiers
+ _objc_msgSend$hideNotifications
+ _objc_msgSend$layoutInsetsForSize:fadeAnchorY:
+ _objc_msgSend$localizedDimMode
+ _objc_msgSend$notificationLegibilityDynamicDimView
+ _objc_msgSend$setLocalizedDimMode:
+ _objc_msgSend$setPasscodeLockViewState:animated:
+ _objc_msgSend$setShouldAnimate:
+ _objc_msgSend$shouldAnimate
- -[CSCombinedListViewController notificationStructuredListViewController:requestsUpdateNotificationDimViewFadeRadiusY:]
- -[CSCombinedListViewController notificationStructuredListViewControllerDidScrollToRevealNotificationHistory:]
- GCC_except_table213
- GCC_except_table676
- GCC_except_table686
- GCC_except_table688
- GCC_except_table697
- GCC_except_table709
- GCC_except_table719
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.813
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.817
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.818
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.819
- ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.779
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.790
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.791
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.798
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.796
- ___block_literal_global.2335
- ___block_literal_global.808
- ___block_literal_global.810
CStrings:
+ "@832@0:8{SBFScreenSpecificCGFloatValue=dddddddddddddddddddddddddddddddddd}16{SBFScreenSpecificCGFloatValue=dddddddddddddddddddddddddddddddddd}288{SBFScreenSpecificCGFloatValue=dddddddddddddddddddddddddddddddddd}560"
+ "CSCombinedListViewController hideNotifications: %{bool}u"
+ "CSCoverSheetViewController disallowGlassCoverSheet: %{bool}u"
+ "NotificationDimmingLayer localizedDimMode set to: %ld; historyWasRevealed: %d, wallpaperObscured: %d; hasOnlyMediaInSupplementaryContainers: %d; notificationsVisibleInViewport: %d"
+ "PosterSwitcherTransition"
+ "T@\"CSNotificationLegibilityDimView\",&,N,V_notificationLegibilityDynamicDimView"
+ "TB,N,V_shouldAnimate"
+ "Tq,N,V_localizedDimMode"
+ "_addNotificationLegibilityDynamicDimView"
+ "_exclusivelyHasMediaSupplementaryItems"
+ "_hasOnlyMediaInSupplementaryContainers"
+ "_hideNotificationsDefaultDidChange"
+ "_isWallpaperObscured"
+ "_localizedDimMode"
+ "_notificationLegibilityDynamicDimView"
+ "_notificationsVisibleInViewport"
+ "_shouldAnimate"
+ "_systemImageNamed:withConfiguration:"
+ "_updateAppearanceForHavingPosterSwitcherTransition:"
+ "_updateMediaOnlyFlagInSupplementaryContainers"
+ "_updateNotificationDimmingLayerLocalizedDimMode"
+ "disallowGlassLockScreen"
+ "groupingIdentifiers"
+ "hideNotifications"
+ "layoutInsetsForSize:fadeAnchorY:"
+ "localizedDimMode"
+ "notificationDimmingLayerVisibility"
+ "notificationLegibilityDynamicDimView"
+ "notificationStructuredListViewController:isNotificationsHistoryRevealed:"
+ "setLocalizedDimMode:"
+ "setNotificationLegibilityDynamicDimView:"
+ "setPasscodeLockViewState:animated:"
+ "setShouldAnimate:"
+ "shouldAnimate"
+ "{UIEdgeInsets=dddd}40@0:8{CGSize=dd}16d32"
+ "\xf0\xe2\xf0\xf0\xf0\x91"
- "@808@0:8{SBFScreenSpecificCGFloatValue=ddddddddddddddddddddddddddddddddd}16{SBFScreenSpecificCGFloatValue=ddddddddddddddddddddddddddddddddd}280{SBFScreenSpecificCGFloatValue=ddddddddddddddddddddddddddddddddd}544"
- "\xf0\xe2\xf0\xf0\xf0\x81"

```
