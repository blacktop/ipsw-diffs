## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4630.1.102.0.0
-  __TEXT.__text: 0xa2350
-  __TEXT.__objc_methlist: 0xe694
+4636.102.1.0.0
+  __TEXT.__text: 0xa2c10
+  __TEXT.__objc_methlist: 0xe8b4
   __TEXT.__const: 0xac8
   __TEXT.__gcc_except_tab: 0x988
-  __TEXT.__cstring: 0xabf2
+  __TEXT.__cstring: 0xabf9
   __TEXT.__dlopen_cstrs: 0x42e
   __TEXT.__ustring: 0x4
-  __TEXT.__oslogstring: 0x47c5
-  __TEXT.__unwind_info: 0x3268
+  __TEXT.__oslogstring: 0x4802
+  __TEXT.__unwind_info: 0x32d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2be0
-  __DATA_CONST.__objc_classlist: 0x988
+  __DATA_CONST.__objc_classlist: 0x990
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x4a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c58
+  __DATA_CONST.__objc_selrefs: 0x7cc8
   __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0x5f0
+  __DATA_CONST.__objc_superrefs: 0x5f8
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x10c0
+  __DATA_CONST.__got: 0x10c8
   __AUTH_CONST.__const: 0x9c0
   __AUTH_CONST.__cfstring: 0xa240
-  __AUTH_CONST.__objc_const: 0x2d970
+  __AUTH_CONST.__objc_const: 0x2daa0
   __AUTH_CONST.__objc_doubleobj: 0x160
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50a0
-  __DATA.__objc_ivar: 0xd30
+  __AUTH.__objc_data: 0x50f0
+  __DATA.__objc_ivar: 0xd3c
   __DATA.__data: 0x3810
   __DATA.__bss: 0x3e8
   __DATA_DIRTY.__objc_data: 0xeb0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4763
-  Symbols:   12327
-  CStrings:  1818
+  Functions: 4807
+  Symbols:   12400
+  CStrings:  1822
 
Symbols:
+ +[SBUILiveActivityMetrics _metrics]
+ -[SBSUIHandleDeviceLockSceneAction abortForUsageViolation:]
+ -[SBSUIHardwareButtonEventSceneAction abortForUsageViolation:]
+ -[SBSUIInCallDestroySceneAction abortForUsageViolation:]
+ -[SBSUIInCallRequestKeyboardFocusAction abortForUsageViolation:]
+ -[SBSUIInCallRequestPresentationModeAction abortForUsageViolation:]
+ -[SBSUIInCallShowNoticeForSystemControlsAction abortForUsageViolation:]
+ -[SBSUIInCallSilenceRingtoneAction abortForUsageViolation:]
+ -[SBSUIUserSwipedToKillAction abortForUsageViolation:]
+ -[SBUIBackgroundActivityAction abortForUsageViolation:]
+ -[SBUIBackgroundContentTouchAction abortForUsageViolation:]
+ -[SBUIButtonAction abortForUsageViolation:]
+ -[SBUIInputControlButtonAction abortForUsageViolation:]
+ -[SBUIInputControlDisableSystemGesturesAction abortForUsageViolation:]
+ -[SBUIPresentableButtonEventsAction abortForUsageViolation:]
+ -[SBUIPresentableCancelSystemDragAction abortForUsageViolation:]
+ -[SBUIPresentableHomeAffordanceThresholdAction abortForUsageViolation:]
+ -[SBUIPresentableSupportsCancellingSystemDragAction abortForUsageViolation:]
+ -[SBUIPresentableWantsHomeGestureAction abortForUsageViolation:]
+ -[SBUIRemoteAlertButtonAction abortForUsageViolation:]
+ -[SBUISActivityMetrics .cxx_destruct]
+ -[SBUISActivityMetrics _jindoMetricsProvider]
+ -[SBUISActivityMetrics _limitedWidthSystemApertureMetrics]
+ -[SBUISActivityMetrics _lockScreenNotificationListItemMetricsWithScaleFactor:screen:]
+ -[SBUISActivityMetrics _requiresPortraitLayout]
+ -[SBUISActivityMetrics _screen]
+ -[SBUISActivityMetrics _systemApertureMetricsWithJindoMetricsProvider:limitedInWidth:]
+ -[SBUISActivityMetrics _systemApertureMetrics]
+ -[SBUISActivityMetrics activeLayoutDirection]
+ -[SBUISActivityMetrics allowsPortraitInAmbient]
+ -[SBUISActivityMetrics ambientCompactDefaultMetrics]
+ -[SBUISActivityMetrics ambientDefaultMetrics]
+ -[SBUISActivityMetrics ambientWidgetMetrics]
+ -[SBUISActivityMetrics defaultMetrics]
+ -[SBUISActivityMetrics initWithWindowScene:allowsPortraitInAmbient:activeLayoutDirection:]
+ -[SBUISActivityMetrics modalFullScreenMetrics]
+ -[SBUISActivityMetrics windowScene]
+ -[SBUISFloatingDockRemoteContentAction abortForUsageViolation:]
+ -[SBUISystemApertureAlertingAction abortForUsageViolation:]
+ -[SBUISystemApertureElementSource _requiresSceneAlignedGeometry]
+ -[SBUISystemApertureElementSource _sceneAlignedAnchorFrame:]
+ -[SBUISystemApertureElementSource _sceneAlignedContainerViewFrame]
+ -[SBUISystemApertureLayoutMetrics maximumLimitedLeadingTrailingViewAndPaddingSize]
+ -[SBUISystemApertureSceneAction abortForUsageViolation:]
+ -[SBUISystemApertureSceneResizeAction abortForUsageViolation:]
+ -[_SBUISystemApertureTransientLocalSceneResizeAction abortForUsageViolation:]
+ -[_SBUISystemApertureUserInitiatedSceneResizeAction abortForUsageViolation:]
+ GCC_except_table16
+ GCC_except_table166
+ GCC_except_table168
+ _BSSizeSwap
+ _OBJC_CLASS_$_SBUISActivityMetrics
+ _OBJC_IVAR_$_SBUISActivityMetrics._activeLayoutDirection
+ _OBJC_IVAR_$_SBUISActivityMetrics._allowsPortraitInAmbient
+ _OBJC_IVAR_$_SBUISActivityMetrics._windowScene
+ _OBJC_METACLASS_$_SBUISActivityMetrics
+ __OBJC_$_INSTANCE_METHODS_SBSUIInCallShowNoticeForSystemControlsAction
+ __OBJC_$_INSTANCE_METHODS_SBSUIInCallSilenceRingtoneAction
+ __OBJC_$_INSTANCE_METHODS_SBUIPresentableCancelSystemDragAction
+ __OBJC_$_INSTANCE_METHODS_SBUIPresentableSupportsCancellingSystemDragAction
+ __OBJC_$_INSTANCE_METHODS_SBUISActivityMetrics
+ __OBJC_$_INSTANCE_VARIABLES_SBUISActivityMetrics
+ __OBJC_$_PROP_LIST_SBUISActivityMetrics
+ __OBJC_CLASS_RO_$_SBUISActivityMetrics
+ __OBJC_METACLASS_RO_$_SBUISActivityMetrics
+ _objc_msgSend$_jindoMetricsProvider
+ _objc_msgSend$_lockScreenNotificationListItemMetricsWithScaleFactor:screen:
+ _objc_msgSend$_metrics
+ _objc_msgSend$_requiresSceneAlignedGeometry
+ _objc_msgSend$_sceneAlignedAnchorFrame:
+ _objc_msgSend$_sceneAlignedContainerViewFrame
+ _objc_msgSend$_systemApertureMetricsWithJindoMetricsProvider:limitedInWidth:
+ _objc_msgSend$abort
+ _objc_msgSend$ambientCompactDefaultMetrics
+ _objc_msgSend$ambientDefaultMetrics
+ _objc_msgSend$ambientWidgetMetrics
+ _objc_msgSend$defaultMetrics
+ _objc_msgSend$initWithWindowScene:allowsPortraitInAmbient:activeLayoutDirection:
+ _objc_msgSend$maximumLimitedLeadingTrailingViewAndPaddingSize
+ _objc_msgSend$modalFullScreenMetrics
+ _objc_msgSend$setBottom:
+ _objc_msgSend$setTop:
- +[SBUILiveActivityMetrics _limitedWidthSystemApertureMetrics]
- +[SBUILiveActivityMetrics _systemApertureMetricsWithJindoMetricsProvider:maximumLeadingTrailingViewSize:uniformEdgeInsets:]
- +[SBUILiveActivityMetrics _systemApertureMetrics]
- +[SBUILiveActivityMetrics lockScreenNotificationListItemMetricsWithScaleFactor:]
- GCC_except_table11
- GCC_except_table163
- GCC_except_table165
- _objc_msgSend$_systemApertureMetricsWithJindoMetricsProvider:maximumLeadingTrailingViewSize:uniformEdgeInsets:
- _objc_msgSend$lockScreenNotificationListItemMetricsWithScaleFactor:
CStrings:
+ "%@"
+ "Not updating strict coverage required for non-mesa device"
+ "SBUISActivityMetrics.m"
+ "adi"
+ "debug"
- "SBUILiveActivityMetrics.m"
```
