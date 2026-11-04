## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-704.2.4.100.0
-  __TEXT.__text: 0xb751c
-  __TEXT.__objc_methlist: 0xb5a8
-  __TEXT.__const: 0x2c7a
-  __TEXT.__cstring: 0x4834
-  __TEXT.__gcc_except_tab: 0x85c
-  __TEXT.__oslogstring: 0x44cb
+704.3.7.100.0
+  __TEXT.__text: 0xc404c
+  __TEXT.__objc_methlist: 0xbe88
+  __TEXT.__const: 0x2d8a
+  __TEXT.__cstring: 0x4a24
+  __TEXT.__gcc_except_tab: 0xa10
+  __TEXT.__oslogstring: 0x4abb
   __TEXT.__dlopen_cstrs: 0x14e
-  __TEXT.__constg_swiftt: 0x2a7c
-  __TEXT.__swift5_typeref: 0x2c2e
+  __TEXT.__constg_swiftt: 0x2d1c
+  __TEXT.__swift5_typeref: 0x2d98
   __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_reflstr: 0x1e02
-  __TEXT.__swift5_fieldmd: 0x138c
+  __TEXT.__swift5_reflstr: 0x2122
+  __TEXT.__swift5_fieldmd: 0x1514
   __TEXT.__swift5_assocty: 0x198
-  __TEXT.__swift5_proto: 0xcc
-  __TEXT.__swift5_types: 0x12c
-  __TEXT.__swift5_capture: 0xfc8
-  __TEXT.__swift5_protos: 0x10
+  __TEXT.__swift5_proto: 0xd0
+  __TEXT.__swift5_types: 0x13c
+  __TEXT.__swift5_capture: 0x1210
+  __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x38f8
-  __TEXT.__eh_frame: 0x3e8
+  __TEXT.__unwind_info: 0x3d18
+  __TEXT.__eh_frame: 0x430
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1438
-  __DATA_CONST.__objc_classlist: 0x3b0
+  __DATA_CONST.__const: 0x1618
+  __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x5b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x69b0
+  __DATA_CONST.__objc_selrefs: 0x6ea0
   __DATA_CONST.__objc_protorefs: 0x228
-  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0xd68
-  __AUTH_CONST.__const: 0x4531
-  __AUTH_CONST.__cfstring: 0x2f80
-  __AUTH_CONST.__objc_const: 0x11260
+  __DATA_CONST.__got: 0xd98
+  __AUTH_CONST.__const: 0x4d71
+  __AUTH_CONST.__cfstring: 0x30e0
+  __AUTH_CONST.__objc_const: 0x11f10
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH_CONST.__auth_got: 0x1358
-  __AUTH.__objc_data: 0x17d0
-  __AUTH.__data: 0x6f0
-  __DATA.__objc_ivar: 0x750
-  __DATA.__data: 0x3a80
+  __AUTH_CONST.__auth_got: 0x1468
+  __AUTH.__objc_data: 0x1a90
+  __AUTH.__data: 0x7f8
+  __DATA.__objc_ivar: 0x7c4
+  __DATA.__data: 0x3bb0
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x3a68
-  __DATA_DIRTY.__data: 0xe80
+  __DATA_DIRTY.__objc_data: 0x3ca8
+  __DATA_DIRTY.__data: 0xec0
   __DATA_DIRTY.__bss: 0x8c0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5070
-  Symbols:   5640
-  CStrings:  856
+  Functions: 5417
+  Symbols:   5902
+  CStrings:  890
 
Symbols:
+ +[CCUIConnectivityManager _selectableVPNConfigurationsFromConfigurations:]
+ +[CCUIConnectivityManager _tetheringServiceDynamicStoreKey]
+ +[CCUIStatusBar _newStatusBarWithFrame:screen:]
+ +[CCUIStatusBar newSecondaryHorizontalStatusBarWithWindowScene:]
+ +[CCUIWiFiModuleViewController showsLoadingPlaceholderForMenuActionsCount:scanCompleted:]
+ -[CCUIConnectivityManager _reloadSelectableVPNConfigurations]
+ -[CCUIConnectivityManager _sendStateUpdateToVPNViewControllersObservingStateChanges]
+ -[CCUIConnectivityManager _startObservingTetheringServiceStateIfNecessary]
+ -[CCUIConnectivityManager _startObservingVPNConfigurationsIfNecessary]
+ -[CCUIConnectivityManager _startVPNConfigurationWithIdentifier:afterConfigurationChange:]
+ -[CCUIConnectivityManager _updateVPNConfigurationSessionsForVPNConfigurations:]
+ -[CCUIConnectivityManager connectVPNConfiguration:]
+ -[CCUIConnectivityManager selectableVPNConfigurations]
+ -[CCUIConnectivityManager setSelectableVPNConfigurations:]
+ -[CCUIConnectivityManager setTetheringServiceDynamicStore:]
+ -[CCUIConnectivityManager setVpnConfigurationManager:]
+ -[CCUIConnectivityManager setVpnConfigurationSessions:]
+ -[CCUIConnectivityManager statusForVPNConfiguration:]
+ -[CCUIConnectivityManager tetheringServiceDynamicStore]
+ -[CCUIConnectivityManager vpnConfigurationManager]
+ -[CCUIConnectivityManager vpnConfigurationSessions]
+ -[CCUIContentModuleContainerViewController _contentBoundsForPresentationFrame:]
+ -[CCUIContentModuleContainerViewController isSliderModule]
+ -[CCUIHeaderPocketView _forwardHitTestToStatusBarIfNeeded:point:event:]
+ -[CCUIHeaderPocketView presentSensorAttributionExpandedView:completion:]
+ -[CCUIHeaderPocketView secondaryStatusBar]
+ -[CCUIHeaderPocketView setAlpha:]
+ -[CCUIHeaderPocketView setSecondaryStatusBar:]
+ -[CCUIHeaderPocketView setStatusBar:]
+ -[CCUIHeaderPocketView setVerticalStatusBarPresentationTranslation:]
+ -[CCUIHeaderPocketView targetSecondaryStatusBarFrame]
+ -[CCUIHeaderPocketView targetStatusBarFrame]
+ -[CCUIHeaderPocketView verticalStatusBarPresentationTranslation]
+ -[CCUIMainViewController _applyHeaderMode:orientationHint:]
+ -[CCUIMainViewController _overlayStatusBarTargetFrameInSuperview]
+ -[CCUIMainViewController _reachabilityOffsetPoint]
+ -[CCUIMainViewController _rebuildStatusBarForHeaderMode:orientationHint:]
+ -[CCUIMainViewController _signpostedEditingCompletionFromEditing:toEditing:completion:]
+ -[CCUIMainViewController _updateVerticalStatusBarVisibleContentFrameWithTargetFrame:]
+ -[CCUIMainViewController currentPageIndex]
+ -[CCUIMainViewController expandedModuleIdentifier]
+ -[CCUIMainViewController hostBatteryPartFrameForStatusBar:]
+ -[CCUIMainViewController hostStatusBarAvoidanceFrameDidChange]
+ -[CCUIMainViewController isDisplayingExpandedModule]
+ -[CCUIMainViewController isHostStatusBarHiddenAtPresentation]
+ -[CCUIMainViewController layoutOverlayStatusBar]
+ -[CCUIMainViewController overlayReachabilityOffset]
+ -[CCUIMainViewController overlayStatusBar]
+ -[CCUIMainViewController presentControlsGalleryWithCompletion:]
+ -[CCUIMainViewController restoreCurrentPageIndexForDisplayTransition:]
+ -[CCUIMainViewController setEditing:completion:]
+ -[CCUIMainViewController setSensorAttributionViewControllerExpanded:]
+ -[CCUIMainViewController setSensorAttributionViewControllerExpanded:completion:]
+ -[CCUIMainViewController statusBarDidUpdateVerticalStatusBarVisibleContentFrame:]
+ -[CCUIMainViewController statusBarShouldIgnoreTouches:]
+ -[CCUIOverlayStatusBarPresentationProvider _addExpandedStatusBarAlphaAnimationToBatch:transitionState:visible:]
+ -[CCUIOverlayStatusBarPresentationProvider _addVerticalStatusBarFanOutAnimationToBatch:transitionState:expanded:]
+ -[CCUIOverlayStatusBarPresentationProvider _adoptsHostStatusBarStyle]
+ -[CCUIOverlayStatusBarPresentationProvider _applyExpandedStatusBarStyleForPresented:]
+ -[CCUIOverlayStatusBarPresentationProvider _cancelPendingExpandedStatusBarStyleChange]
+ -[CCUIOverlayStatusBarPresentationProvider _isTransitioningVerticalToVertical]
+ -[CCUIOverlayStatusBarPresentationProvider _scheduleExpandedStatusBarHostStyleForCollapse]
+ -[CCUIOverlayStatusBarPresentationProvider _skipsStatusBarSwapAnimation]
+ -[CCUIOverlayStatusBarPresentationProvider _verticalStatusBarPresentationTranslationForTransitionState:]
+ -[CCUIOverlayStatusBarPresentationProvider pendingExpandedStatusBarStyleChange]
+ -[CCUIOverlayStatusBarPresentationProvider setPendingExpandedStatusBarStyleChange:]
+ -[CCUIOverlayStatusBarPresentationProvider setSupportsVerticalStatusBar:]
+ -[CCUIOverlayStatusBarPresentationProvider supportsVerticalStatusBar]
+ -[CCUIStatusBar _alignExpandedStatusBarToHostBatteryPart]
+ -[CCUIStatusBar _convertAvoidanceFrame:toCoordinateSpaceOfStatusBarFrame:]
+ -[CCUIStatusBar _expandedStatusBarMode]
+ -[CCUIStatusBar _isTransitioningVerticalToVertical]
+ -[CCUIStatusBar _setNeedsLayoutAfterExpandedContentLayout]
+ -[CCUIStatusBar _setVerticalStatusBarVisibleContentFrame:]
+ -[CCUIStatusBar _updateAvoidanceFramesWithCompactTrailingFrame:]
+ -[CCUIStatusBar _updateExpandedAvoidanceFrameWithExpandedFrame:]
+ -[CCUIStatusBar _updateVerticalStatusBarVisibleContentFrame]
+ -[CCUIStatusBar _verticalStatusBarHitRegionFrame]
+ -[CCUIStatusBar compactStatusBarAxis]
+ -[CCUIStatusBar disabledPartIdentifiers]
+ -[CCUIStatusBar initWithFrame:windowScene:screenType:]
+ -[CCUIStatusBar nonExpandedStatusBarMode]
+ -[CCUIStatusBar pointInside:withEvent:]
+ -[CCUIStatusBar setCompactStatusBarAxis:]
+ -[CCUIStatusBar setDisabledPartIdentifiers:]
+ -[CCUIStatusBar setExpandedStatusBarAlpha:]
+ -[CCUIStatusBar setExpandedStatusBarStyleRequest:]
+ -[CCUIStatusBar setNonExpandedStatusBarMode:]
+ -[CCUIStatusBar setVerticalStatusBarExpanded:]
+ -[CCUIStatusBar verticalStatusBarVisibleContentFrame]
+ -[CCUIStatusBarStyleSnapshot batteryPartFrame]
+ -[CCUIStatusBarStyleSnapshot initWithHidden:hiddenPartIdentifier:leadingStyleRequest:trailingStyleRequest:overlayData:actionsByPartIdentifier:statusBarInsets:avoidanceFrame:statusBarAxis:]
+ -[CCUIStatusBarStyleSnapshot initWithHidden:hiddenPartIdentifier:leadingStyleRequest:trailingStyleRequest:overlayData:actionsByPartIdentifier:statusBarInsets:avoidanceFrame:statusBarAxis:statusBarMode:]
+ -[CCUIStatusBarStyleSnapshot initWithHidden:hiddenPartIdentifier:leadingStyleRequest:trailingStyleRequest:overlayData:actionsByPartIdentifier:statusBarInsets:avoidanceFrame:statusBarAxis:statusBarMode:batteryPartFrame:]
+ -[CCUIStatusBarStyleSnapshot statusBarAxis]
+ -[CCUIStatusBarStyleSnapshot statusBarMode]
+ -[CCUIVPNConfigurationSession .cxx_destruct]
+ -[CCUIVPNConfigurationSession _fetchStatus]
+ -[CCUIVPNConfigurationSession _handleSessionEvent:]
+ -[CCUIVPNConfigurationSession _startIfConfigurationChangeWasPending]
+ -[CCUIVPNConfigurationSession _updateWithSessionStatus:]
+ -[CCUIVPNConfigurationSession dealloc]
+ -[CCUIVPNConfigurationSession initWithIdentifier:statusChangeHandler:]
+ -[CCUIVPNConfigurationSession invalidate]
+ -[CCUIVPNConfigurationSession startAfterConfigurationChange]
+ -[CCUIVPNConfigurationSession start]
+ -[CCUIVPNConfigurationSession status]
+ -[CCUIVPNModuleViewController _connectedVPNConfigurations]
+ -[CCUIVPNModuleViewController _menuActionForVPNConfiguration:status:]
+ -[CCUIVPNModuleViewController _menuActionSubtitleForVPNStatus:]
+ -[CCUIVPNModuleViewController _multipleVPNConfigurationsAvailable]
+ -[CCUIVPNModuleViewController _soleDisabledVPNConfiguration]
+ -[CCUIVPNModuleViewController _subtitleTextForConnectedVPNConfigurations:]
+ -[CCUIVPNModuleViewController contentModuleContext]
+ -[CCUIVPNModuleViewController contextMenuItems]
+ -[CCUIVPNModuleViewController contextMenuShouldPresentForControlTemplateView:withCompletion:]
+ -[CCUIVPNModuleViewController contextMenu]
+ -[CCUIVPNModuleViewController initWithContentModuleContext:]
+ -[CCUIVPNModuleViewController menuDisplayName]
+ -[CCUIVPNModuleViewController setContentModuleContext:]
+ -[CCUIWiFiModuleViewController setScanning:]
+ GCC_except_table115
+ GCC_except_table15
+ GCC_except_table179
+ GCC_except_table186
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table26
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table70
+ GCC_except_table8
+ GCC_except_table83
+ _BSRectEqualToRect
+ _CCUIGridGeometryInfoContentDimension
+ _CCUITetheringServiceDynamicStoreCallBack
+ _OBJC_CLASS_$_CCUIVPNConfigurationSession
+ _OBJC_CLASS_$_NEConfiguration
+ _OBJC_CLASS_$_NEConfigurationManager
+ _OBJC_CLASS_$_SBIconListPageControl
+ _OBJC_CLASS_$_UIStatusBarAnimationParameters
+ _OBJC_CLASS_$__TtC15ControlCenterUI19IconListPageControl
+ _OBJC_CLASS_$__TtC15ControlCenterUI34CurrentPageIndicatorBackgroundView
+ _OBJC_IVAR_$_CCUIConnectivityManager._selectableVPNConfigurations
+ _OBJC_IVAR_$_CCUIConnectivityManager._tetheringServiceDynamicStore
+ _OBJC_IVAR_$_CCUIConnectivityManager._vpnConfigurationManager
+ _OBJC_IVAR_$_CCUIConnectivityManager._vpnConfigurationSessions
+ _OBJC_IVAR_$_CCUIHeaderPocketView._secondaryStatusBar
+ _OBJC_IVAR_$_CCUIHeaderPocketView._verticalStatusBarPresentationTranslation
+ _OBJC_IVAR_$_CCUIMainViewController._headerAreaDismissalPanGesture
+ _OBJC_IVAR_$_CCUIMainViewController._headerAreaDismissalPanTouchedStatusBar
+ _OBJC_IVAR_$_CCUIMainViewController._headerAreaDismissalTapGesture
+ _OBJC_IVAR_$_CCUIMainViewController._headerMode
+ _OBJC_IVAR_$_CCUIMainViewController._hostStatusBarHiddenAtPresentation
+ _OBJC_IVAR_$_CCUIMainViewController._secondaryStatusBar
+ _OBJC_IVAR_$_CCUIMainViewController._statusBar
+ _OBJC_IVAR_$_CCUIOverlayStatusBarPresentationProvider._pendingExpandedStatusBarStyleChange
+ _OBJC_IVAR_$_CCUIOverlayStatusBarPresentationProvider._supportsVerticalStatusBar
+ _OBJC_IVAR_$_CCUIStatusBar._compactStatusBarAxis
+ _OBJC_IVAR_$_CCUIStatusBar._disabledPartIdentifiers
+ _OBJC_IVAR_$_CCUIStatusBar._isExpanded
+ _OBJC_IVAR_$_CCUIStatusBar._nonExpandedStatusBarMode
+ _OBJC_IVAR_$_CCUIStatusBar._supportsEdgeAlignedLayout
+ _OBJC_IVAR_$_CCUIStatusBar._supportsVerticalStatusBar
+ _OBJC_IVAR_$_CCUIStatusBar._verticalStatusBarVisibleContentFrame
+ _OBJC_IVAR_$_CCUIStatusBarStyleSnapshot._batteryPartFrame
+ _OBJC_IVAR_$_CCUIStatusBarStyleSnapshot._statusBarAxis
+ _OBJC_IVAR_$_CCUIStatusBarStyleSnapshot._statusBarMode
+ _OBJC_IVAR_$_CCUIVPNConfigurationSession._session
+ _OBJC_IVAR_$_CCUIVPNConfigurationSession._startsWhenConfigurationChangeIsHandled
+ _OBJC_IVAR_$_CCUIVPNConfigurationSession._status
+ _OBJC_IVAR_$_CCUIVPNConfigurationSession._statusChangeHandler
+ _OBJC_IVAR_$_CCUIVPNModuleViewController._contentModuleContext
+ _OBJC_IVAR_$_CCUIWiFiModuleViewController._hasCompletedAScan
+ _OBJC_IVAR_$_CCUIWiFiModuleViewController._scanning
+ _OBJC_METACLASS_$_CCUIVPNConfigurationSession
+ _OBJC_METACLASS_$_SBIconListPageControl
+ _OBJC_METACLASS_$__TtC15ControlCenterUI19IconListPageControl
+ _OBJC_METACLASS_$__TtC15ControlCenterUI34CurrentPageIndicatorBackgroundView
+ _OBJC_METACLASS_$__TtC15ControlCenterUIP33_AC37E3D049C737740B7D6B7D39BF56C132PrimaryActionFallbackTapDelegate
+ _SBHIconGridSizeClassDefault
+ _SCDynamicStoreCreate
+ _SCDynamicStoreSetDispatchQueue
+ _SCDynamicStoreSetNotificationKeys
+ _SCError
+ _SCErrorString
+ __DATA__TtC15ControlCenterUI19IconListPageControl
+ __DATA__TtC15ControlCenterUI34CurrentPageIndicatorBackgroundView
+ __DATA__TtC15ControlCenterUIP33_AC37E3D049C737740B7D6B7D39BF56C132PrimaryActionFallbackTapDelegate
+ __INSTANCE_METHODS__TtC15ControlCenterUI19IconListPageControl
+ __INSTANCE_METHODS__TtC15ControlCenterUI34CurrentPageIndicatorBackgroundView
+ __INSTANCE_METHODS__TtC15ControlCenterUIP33_AC37E3D049C737740B7D6B7D39BF56C132PrimaryActionFallbackTapDelegate
+ __IVARS_CCUIIconListView
+ __IVARS__TtC15ControlCenterUI19IconListPageControl
+ __IVARS__TtC15ControlCenterUI34CurrentPageIndicatorBackgroundView
+ __METACLASS_DATA__TtC15ControlCenterUI19IconListPageControl
+ __METACLASS_DATA__TtC15ControlCenterUI34CurrentPageIndicatorBackgroundView
+ __METACLASS_DATA__TtC15ControlCenterUIP33_AC37E3D049C737740B7D6B7D39BF56C132PrimaryActionFallbackTapDelegate
+ __OBJC_$_INSTANCE_METHODS_CCUIVPNConfigurationSession
+ __OBJC_$_INSTANCE_VARIABLES_CCUIVPNConfigurationSession
+ __OBJC_$_PROP_LIST_CCUIVPNConfigurationSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CCUIMainViewControllerProtocol
+ __OBJC_CLASS_RO_$_CCUIVPNConfigurationSession
+ __OBJC_METACLASS_RO_$_CCUIVPNConfigurationSession
+ __PROTOCOLS__TtC15ControlCenterUIP33_AC37E3D049C737740B7D6B7D39BF56C132PrimaryActionFallbackTapDelegate
+ __UIStatusBarPartIdentifierVisibleExpanded
+ ___111-[CCUIOverlayStatusBarPresentationProvider _addExpandedStatusBarAlphaAnimationToBatch:transitionState:visible:]_block_invoke
+ ___113-[CCUIOverlayStatusBarPresentationProvider _addVerticalStatusBarFanOutAnimationToBatch:transitionState:expanded:]_block_invoke
+ ___42-[CCUIVPNModuleViewController contextMenu]_block_invoke
+ ___43-[CCUIVPNConfigurationSession _fetchStatus]_block_invoke
+ ___47-[CCUIVPNModuleViewController contextMenuItems]_block_invoke
+ ___51-[CCUIConnectivityManager connectVPNConfiguration:]_block_invoke
+ ___52-[CCUIWiFiModuleViewController _updateWiFiMenuItems]_block_invoke_2
+ ___58-[CCUIStatusBar _setNeedsLayoutAfterExpandedContentLayout]_block_invoke
+ ___58-[CCUIVPNModuleViewController _connectedVPNConfigurations]_block_invoke
+ ___61-[CCUIConnectivityManager _reloadSelectableVPNConfigurations]_block_invoke
+ ___64-[CCUIMainViewController pagingViewController:editingDidChange:]_block_invoke
+ ___69-[CCUIVPNModuleViewController _menuActionForVPNConfiguration:status:]_block_invoke
+ ___70-[CCUIConnectivityManager _startObservingVPNConfigurationsIfNecessary]_block_invoke
+ ___70-[CCUIVPNConfigurationSession initWithIdentifier:statusChangeHandler:]_block_invoke
+ ___74+[CCUIConnectivityManager _selectableVPNConfigurationsFromConfigurations:]_block_invoke
+ ___74+[CCUIConnectivityManager _selectableVPNConfigurationsFromConfigurations:]_block_invoke_2
+ ___79-[CCUIConnectivityManager _updateVPNConfigurationSessionsForVPNConfigurations:]_block_invoke
+ ___85-[CCUIOverlayStatusBarPresentationProvider _applyExpandedStatusBarStyleForPresented:]_block_invoke
+ ___87-[CCUIMainViewController _signpostedEditingCompletionFromEditing:toEditing:completion:]_block_invoke
+ ___90-[CCUIOverlayStatusBarPresentationProvider _scheduleExpandedStatusBarHostStyleForCollapse]_block_invoke
+ ___93-[CCUIVPNModuleViewController contextMenuShouldPresentForControlTemplateView:withCompletion:]_block_invoke
+ ___block_descriptor_32_e18_v16?0"UIAction"8l
+ ___block_descriptor_32_e45_q24?0"NEConfiguration"8"NEConfiguration"16l
+ ___block_descriptor_32_e8_B16?08l
+ ___block_descriptor_40_e8_32bs_e11_v16?0B8B12ls32l8
+ ___block_descriptor_40_e8_32s_e25_B16?0"NEConfiguration"8ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_40_e8_32w_e29_v24?0"NSArray"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_e8_32s40s_e40_"UIMenuElement"16?0"NEConfiguration"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8ls32l8w40l8
+ ___block_descriptor_48_e8_32w_e12_v20?0i8^v12lw32l8
+ ___block_descriptor_56_e8_32s40s48w_e37_v24?0"NEConfiguration"8"NSError"16ls32l8w48l8s40l8
+ ___block_descriptor_64_e8_32s_e5_v8?0ls32l8
+ ___swift_closure_destructor.101Tm
+ ___swift_closure_destructor.181Tm
+ ___swift_closure_destructor.516Tm
+ __bs_set_crash_log_message
+ __os_log_default
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _keypath_set.225Tm
+ _ne_session_cancel
+ _ne_session_create
+ _ne_session_get_status
+ _ne_session_release
+ _ne_session_set_event_handler
+ _ne_session_start
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $s15ControlCenterUI012IconListPageA14LayoutObserverP
+ _symbolic Ieg_Sg
+ _symbolic SaySo10SBIconViewCG
+ _symbolic SaySo40CCUIContentModuleContainerViewControllerCG
+ _symbolic SbSg
+ _symbolic So10NSMapTableCySo10SBIconViewC_____G 15ControlCenterUI0A20ResizeGestureHandlerC
+ _symbolic So21SBIconListPageControlC
+ _symbolic So21SBIconListPageControlCSgXw
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 15ControlCenterUI012IconListPageA0C
+ _symbolic _____ 15ControlCenterUI20PagingViewControllerC24ModuleExpansionCandidateV
+ _symbolic _____ 15ControlCenterUI32PrimaryActionFallbackTapDelegate022_AC37E3D049C737740B7D6M9D39BF56C1LLC
+ _symbolic _____ 15ControlCenterUI34CurrentPageIndicatorBackgroundViewC
+ _symbolic _____Sg 15ControlCenterUI32PrimaryActionFallbackTapDelegate022_AC37E3D049C737740B7D6M9D39BF56C1LLC
+ _symbolic _____Sg 15ControlCenterUI34CurrentPageIndicatorBackgroundViewC
+ _symbolic _____Sg 8Dispatch0A8WorkItemC
+ _symbolic _____SgXw 15ControlCenterUI34CurrentPageIndicatorBackgroundViewC
+ _symbolic _____SgXwz_Xx 15ControlCenterUI34CurrentPageIndicatorBackgroundViewC
+ _symbolic _____Sg_ABt 10Foundation4UUIDV
+ _symbolic ______pSgXw 15ControlCenterUI012IconListPageA14LayoutObserverP
+ _symbolic _____ySiG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15ControlCenterUI20PagingViewControllerC24ModuleExpansionCandidateV
- -[CCUIHeaderPocketView setMode:orientationHint:]
- -[CCUIHeaderPocketView setStatusBarDelegate:]
- -[CCUIHeaderPocketView statusBarDelegate]
- -[CCUIMainViewController overlayReachabilityHeight]
- -[CCUIStatusBar _updateCompactTrailingStatusBarAvoidanceFrame]
- -[CCUIStatusBar initWithFrame:windowScene:]
- -[CCUIVPNModuleViewController init]
- GCC_except_table155
- GCC_except_table162
- GCC_except_table2
- GCC_except_table45
- GCC_except_table47
- GCC_except_table51
- GCC_except_table64
- GCC_except_table89
- _OBJC_IVAR_$_CCUIHeaderPocketView._statusBarDelegate
- _OBJC_IVAR_$_CCUIMainViewController._headerPocketViewDismissalPanGesture
- _OBJC_IVAR_$_CCUIMainViewController._headerPocketViewDismissalTapGesture
- _UIRectInsetEdges
- ___getWFPersonalHotspotNETRBStateChangeNotificationSymbolLoc_block_invoke
- ___swift_closure_destructor.140Tm
- ___swift_closure_destructor.443Tm
- _getWFPersonalHotspotNETRBStateChangeNotificationSymbolLoc.ptr
CStrings:
+ "4\""
+ "@\"UIMenuElement\"16@?0@\"NEConfiguration\"8"
+ "B16@?0@\"NEConfiguration\"8"
+ "B16@?0@8"
+ "Begin presentation: animated=%{BOOL}d, interactive=%{BOOL}d, currentState=%{public}@, transitionState=%{public}@, presentationStateWillChange=%{BOOL}d, transitionStateWillChange=%{BOOL}d, currentPageIndex=%ld"
+ "CCUIStatusBar.m"
+ "CONTROL_CENTER_STATUS_VPN_CONNECTIONS"
+ "CONTROL_CENTER_STATUS_VPN_SETTINGS"
+ "CONTROL_CENTER_STATUS_WIFI_NO_NETWORKS"
+ "ControlCenterUI.CurrentPageIndicatorBackgroundView"
+ "ControlCenterUI/CurrentPageIndicatorBackgroundView.swift"
+ "Disallowing editing during restoration: %{public}s"
+ "Invalid condition not satisfying: %@"
+ "Page control moved to page %ld: scrubbing=%{bool}d, fromPresentationContinuation=%{bool}d"
+ "Refusing display-transition page-index restore: %ld is outside valid range [%ld, %ld]"
+ "Saved icon state was not usable; layout status: %{public}ld, lists: %{public}ld, icons: %{public}ld"
+ "Scrolled to default page after dismissal: fromPageIndex=%ld, toPageIndex=%ld, isOnDefaultPage=%{BOOL}d"
+ "[Hotspot] (ConnectivityManager) Failed to create the tethering service dynamic store: %{public}s"
+ "[Hotspot] (ConnectivityManager) Failed to observe the tethering service state at %{public}@: %{public}s"
+ "[Hotspot] (ConnectivityManager) Observing the tethering service state at %{public}@"
+ "[Hotspot] (ConnectivityManager) Tethering service state changed, Sending state update to hotspotViewControllersObservingStateChanges: %{public}@"
+ "[VPN] (ConnectivityManager) Connecting VPN configuration %{public}@"
+ "[VPN] (ConnectivityManager) Error enabling VPN configuration %{public}@: %{public}@"
+ "[VPN] (ConnectivityManager) Error loading VPN configuration %{public}@: %{public}@"
+ "[VPN] (ConnectivityManager) Error loading VPN configurations: %{public}@"
+ "[VPN] (ConnectivityManager) Failed to create session for VPN configuration %{public}@"
+ "[VPN] (ConnectivityManager) Loaded %lu selectable VPN configurations"
+ "[VPN] (ConnectivityManager) No session for VPN configuration %{public}@"
+ "[VPN] (ConnectivityManager) Started VPN configuration %{public}@ (afterConfigurationChange: %{public}@)"
+ "[VPN] Updated VPN control (subtitle: %{private}@, inoperative: %{public}@, enabled: %{public}@, multipleVPNConfigurationsAvailable: %{public}@)"
+ "com.apple.ControlCenter.ConnectivityManager"
+ "com.apple.MobileInternetSharing"
+ "failure in %{public}@ of <%{public}@:%p> (%{public}@:%i) : %{public}@"
+ "prefs:root=VPN"
+ "q24@?0@\"NEConfiguration\"8@\"NEConfiguration\"16"
+ "v16@?0@\"NSArray\"8"
+ "v20@?0i8^v12"
+ "v24@?0@\"NEConfiguration\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "windowScene"
+ "\xc1a"
+ "\xf02#1"
+ "\xf0\xe3\x82"
- "$!"
- "Begin presentation: animated=%{BOOL}d, interactive=%{BOOL}d, currentState=%{public}@, transitionState=%{public}@, presentationStateWillChange=%{BOOL}d, transitionStateWillChange=%{BOOL}d"
- "NSString *getWFPersonalHotspotNETRBStateChangeNotification(void)"
- "WFPersonalHotspotNETRBStateChangeNotification"
- "[Hotspot] (ConnectivityManager) Received WFPersonalHotspotNETRBStateChangeNotification, Sending state update to hotspotViewControllersObservingStateChanges: %{public}@"
- "[VPN] Updated VPN control (subtitle: %{public}@, inoperative: %{public}@, enabled: %{public}@)"
- "aQ"
- "\x91\xa2!!"
- "\xf0\x92!b"
```
