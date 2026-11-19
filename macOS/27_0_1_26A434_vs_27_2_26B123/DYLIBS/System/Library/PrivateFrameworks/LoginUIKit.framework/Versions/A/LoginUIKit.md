## LoginUIKit

> `/System/Library/PrivateFrameworks/LoginUIKit.framework/Versions/A/LoginUIKit`

```diff

-415.0.0.0.0
-  __TEXT.__text: 0xad5c4
-  __TEXT.__objc_methlist: 0xacec
-  __TEXT.__const: 0x1350
-  __TEXT.__cstring: 0xa2a5
-  __TEXT.__gcc_except_tab: 0x112c
+415.2.6.0.0
+  __TEXT.__text: 0xb05c8
+  __TEXT.__objc_methlist: 0xb10c
+  __TEXT.__const: 0x1348
+  __TEXT.__cstring: 0xa725
+  __TEXT.__gcc_except_tab: 0x1210
   __TEXT.__dlopen_cstrs: 0x404
   __TEXT.__ustring: 0x3a
-  __TEXT.__oslogstring: 0x72c
+  __TEXT.__oslogstring: 0x701
   __TEXT.__swift5_typeref: 0x524
   __TEXT.__constg_swiftt: 0x480
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_reflstr: 0xfe
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x3c
-  __TEXT.__unwind_info: 0x2da0
+  __TEXT.__unwind_info: 0x2ed0
   __TEXT.__eh_frame: 0xf08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x980
+  __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6060
+  __DATA_CONST.__objc_selrefs: 0x6310
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x4e8
-  __DATA_CONST.__objc_arraydata: 0x1a8
-  __DATA_CONST.__got: 0x11b0
-  __AUTH_CONST.__const: 0x3518
-  __AUTH_CONST.__cfstring: 0x8e80
-  __AUTH_CONST.__objc_const: 0x10ee8
+  __DATA_CONST.__objc_arraydata: 0x210
+  __DATA_CONST.__got: 0x11e8
+  __AUTH_CONST.__const: 0x35f8
+  __AUTH_CONST.__cfstring: 0x91a0
+  __AUTH_CONST.__objc_const: 0x11358
   __AUTH_CONST.__objc_intobj: 0x1c8
-  __AUTH_CONST.__objc_arrayobj: 0x1e0
+  __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1190
-  __AUTH_CONST.__auth_ptr: 0x280
+  __AUTH_CONST.__auth_got: 0x11a8
+  __AUTH_CONST.__auth_ptr: 0x278
   __AUTH.__objc_data: 0x35c0
   __AUTH.__data: 0x340
-  __DATA.__objc_ivar: 0xb40
-  __DATA.__data: 0xf30
+  __DATA.__objc_ivar: 0xb94
+  __DATA.__data: 0xfb8
   __DATA.__bss: 0xe40
-  __DATA.__common: 0xd8
+  __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x4a8
   __DATA_DIRTY.__data: 0x58
   __DATA_DIRTY.__bss: 0x58

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4732
-  Symbols:   9630
-  CStrings:  1418
+  Functions: 4842
+  Symbols:   9840
+  CStrings:  1443
 
Symbols:
+ +[LUI2MessageViewController heightForLineCount:]
+ +[LUI2WiFiNetwork(Images) _getVariableValue:accessibilityDescription:forBars:]
+ +[LUI2WiFiNetwork(Images) _wifiImageWithSymbolName:bars:paletteColors:]
+ +[LUI2WiFiNetwork(Images) connectedMenuBarImageForBars:]
+ -[LUI2CollectionView _handlePointerEvent:]
+ -[LUI2CollectionView isHandlingPointerEvent]
+ -[LUI2CollectionView mouseDragged:]
+ -[LUI2MessageViewController _currentLineHeight]
+ -[LUI2MessageViewController maxContentHeight]
+ -[LUI2MessageViewController scrollViewMaxHeightConstraint]
+ -[LUI2MessageViewController setScrollViewMaxHeightConstraint:]
+ -[LUI2UIController _hasPlatformSSOMessage]
+ -[LUI2UIController _platformSSOMessageLayoutActive]
+ -[LUI2UIController _updateMessageLayoutForPlatformSSO]
+ -[LUI2UIController delegate]
+ -[LUI2UIController messageHiddenBeforePlatformSSO]
+ -[LUI2UIController messagePlatformSSOBottomConstraint]
+ -[LUI2UIController messageUsingPlatformSSOLayout]
+ -[LUI2UIController platformSSOUIVisibilityDidChange]
+ -[LUI2UIController setDelegate:]
+ -[LUI2UIController setMessageHiddenBeforePlatformSSO:]
+ -[LUI2UIController setMessagePlatformSSOBottomConstraint:]
+ -[LUI2UIController setMessageUsingPlatformSSOLayout:]
+ -[LUI2UserCollectionViewController _beginLayoutTransitionTo:]
+ -[LUI2UserCollectionViewController _endLayoutTransition:]
+ -[LUI2UserCollectionViewController _pointerInputIsDrivingSelection]
+ -[LUI2UserCollectionViewController layoutTransitionGeneration]
+ -[LUI2UserCollectionViewController openingMultiUserLayout]
+ -[LUI2UserCollectionViewController setLayoutTransitionGeneration:]
+ -[LUI2UserCollectionViewController setOpeningMultiUserLayout:]
+ -[LUI2WiFiController _applyUIState:]
+ -[LUI2WiFiController _beginUIStateQuery]
+ -[LUI2WiFiController _clearNetworks]
+ -[LUI2WiFiController _currentDelegates]
+ -[LUI2WiFiController _handleInterfaceEventOfType:]
+ -[LUI2WiFiController _invalidateCachedUIStateAfterConnectionLoss]
+ -[LUI2WiFiController _invalidateCachedUIState]
+ -[LUI2WiFiController _notifyDelegates:block:]
+ -[LUI2WiFiController _notifyStatusUpdated]
+ -[LUI2WiFiController _refreshStatusFromInterfaceOffQueue]
+ -[LUI2WiFiController _refreshStatusFromUIState]
+ -[LUI2WiFiController _requeryUIState]
+ -[LUI2WiFiController _setStatus:]
+ -[LUI2WiFiController _setStatusFromInterface]
+ -[LUI2WiFiController addDelegate:]
+ -[LUI2WiFiController cachedUIState]
+ -[LUI2WiFiController delegatesLock]
+ -[LUI2WiFiController delegates]
+ -[LUI2WiFiController interfaceRSSI]
+ -[LUI2WiFiController monitorCount]
+ -[LUI2WiFiController monitoringGeneration]
+ -[LUI2WiFiController proxyQueue]
+ -[LUI2WiFiController proxyUnusable]
+ -[LUI2WiFiController queryInFlight]
+ -[LUI2WiFiController refreshStatus]
+ -[LUI2WiFiController removeDelegate:]
+ -[LUI2WiFiController scanCount]
+ -[LUI2WiFiController setCachedUIState:]
+ -[LUI2WiFiController setDelegates:]
+ -[LUI2WiFiController setDelegatesLock:]
+ -[LUI2WiFiController setInterfaceRSSI:]
+ -[LUI2WiFiController setMonitorCount:]
+ -[LUI2WiFiController setMonitoringGeneration:]
+ -[LUI2WiFiController setProxyQueue:]
+ -[LUI2WiFiController setProxyUnusable:]
+ -[LUI2WiFiController setQueryInFlight:]
+ -[LUI2WiFiController setScanCount:]
+ -[LUI2WiFiController setStatus:]
+ -[LUI2WiFiController setUiStateQueried:]
+ -[LUI2WiFiController status]
+ -[LUI2WiFiController uiStateQueried]
+ -[LUI2WiFiViewController _beginScanning]
+ -[LUI2WiFiViewController _endScanning]
+ -[LUI2WiFiViewController _menuBarImageForState:bars:]
+ -[LUI2WiFiViewController _showDisabledMenu]
+ -[LUI2WiFiViewController _tintedMenuBarImageForStatus:]
+ -[LUI2WiFiViewController initWithNibName:bundle:]
+ -[LUI2WiFiViewController menuShowingDisabled]
+ -[LUI2WiFiViewController scanning]
+ -[LUI2WiFiViewController setMenuShowingDisabled:]
+ -[LUI2WiFiViewController setScanning:]
+ -[LUI2WiFiViewController setTintedMenuBarImages:]
+ -[LUI2WiFiViewController tintedMenuBarImages]
+ -[LUI2WiFiViewController wifiControllerDidUpdateStatus:]
+ -[LUIAuthenticationManager ahpManager:didEvictModule:]
+ -[LUIAuthenticationManager ahpManager:didLoseConnectionToModule:]
+ -[LUIAuthenticationManager providerForModule:]
+ -[LUIAuthenticationServiceProvider resetActivationState]
+ -[LUITestUser _generateTestAvatarIfNeeded]
+ -[LUITestUser avatarDescriptor]
+ -[LUITestUser avatarStickerConfiguration]
+ -[LUITestUser reloadAvatarInfo]
+ -[LUITestUser setTestAvatarDescriptor:]
+ -[LUITestUser setTestAvatarGenerated:]
+ -[LUITestUser setTestAvatarStickerConfiguration:]
+ -[LUITestUser testAvatarDescriptor]
+ -[LUITestUser testAvatarGenerated]
+ -[LUITestUser testAvatarStickerConfiguration]
+ -[LUITestUserController _injectedTestUserCount]
+ -[LUITestUserController _injectedTestUsers]
+ GCC_except_table100
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table137
+ GCC_except_table27
+ GCC_except_table31
+ GCC_except_table45
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table71
+ GCC_except_table82
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table96
+ OBJC_IVAR_$_LUI2CollectionView._pointerEventDepth
+ OBJC_IVAR_$_LUI2MessageViewController._scrollViewMaxHeightConstraint
+ OBJC_IVAR_$_LUI2UIController._delegate
+ OBJC_IVAR_$_LUI2UIController._messageHiddenBeforePlatformSSO
+ OBJC_IVAR_$_LUI2UIController._messagePlatformSSOBottomConstraint
+ OBJC_IVAR_$_LUI2UIController._messageUsingPlatformSSOLayout
+ OBJC_IVAR_$_LUI2UserCollectionViewController._layoutTransitionGeneration
+ OBJC_IVAR_$_LUI2UserCollectionViewController._openingMultiUserLayout
+ OBJC_IVAR_$_LUI2WiFiController._cachedUIState
+ OBJC_IVAR_$_LUI2WiFiController._delegates
+ OBJC_IVAR_$_LUI2WiFiController._delegatesLock
+ OBJC_IVAR_$_LUI2WiFiController._interfaceRSSI
+ OBJC_IVAR_$_LUI2WiFiController._monitorCount
+ OBJC_IVAR_$_LUI2WiFiController._monitoringGeneration
+ OBJC_IVAR_$_LUI2WiFiController._proxyQueue
+ OBJC_IVAR_$_LUI2WiFiController._proxyUnusable
+ OBJC_IVAR_$_LUI2WiFiController._queryInFlight
+ OBJC_IVAR_$_LUI2WiFiController._scanCount
+ OBJC_IVAR_$_LUI2WiFiController._status
+ OBJC_IVAR_$_LUI2WiFiController._uiStateQueried
+ OBJC_IVAR_$_LUI2WiFiViewController._menuShowingDisabled
+ OBJC_IVAR_$_LUI2WiFiViewController._scanning
+ OBJC_IVAR_$_LUI2WiFiViewController._tintedMenuBarImages
+ OBJC_IVAR_$_LUITestUser._testAvatarDescriptor
+ OBJC_IVAR_$_LUITestUser._testAvatarGenerated
+ OBJC_IVAR_$_LUITestUser._testAvatarStickerConfiguration
+ _LUITestUserHasComplexPassword
+ _OBJC_CLASS_$_NSHashTable
+ __37-[LUI2WiFiController startMonitoring]_block_invoke
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LAAHPManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LAAHPManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_LAAHPManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_LUIAuthenticationManager
+ __OBJC_LABEL_PROTOCOL_$_LAAHPManagerDelegate
+ __OBJC_PROTOCOL_$_LAAHPManagerDelegate
+ ___26-[LUI2WiFiController init]_block_invoke_2
+ ___30-[LUI2CollectionView mouseUp:]_block_invoke
+ ___32-[LUI2CollectionView mouseDown:]_block_invoke
+ ___34-[LUI2WiFiController stopScanning]_block_invoke_2
+ ___35-[LUI2CollectionView mouseDragged:]_block_invoke
+ ___35-[LUI2WiFiController refreshStatus]_block_invoke
+ ___35-[LUI2WiFiController startScanning]_block_invoke_2
+ ___36-[LUI2WiFiController stopMonitoring]_block_invoke_2
+ ___37-[LUI2WiFiController startMonitoring]_block_invoke_2
+ ___38-[LUI2UserView finishAddingUserAvatar]_block_invoke
+ ___40-[LUI2WiFiController _beginUIStateQuery]_block_invoke
+ ___40-[LUI2WiFiController _beginUIStateQuery]_block_invoke_2
+ ___42-[LUI2WiFiController _notifyStatusUpdated]_block_invoke
+ ___44-[TRMPortManager _stopMatchingNotifications]_block_invoke
+ ___45-[LUI2WiFiController _notifyDelegates:block:]_block_invoke
+ ___48-[LUI2WiFiController didUpdateUIState:previous:]_block_invoke
+ ___49-[LUI2WiFiController clientConnectionInvalidated]_block_invoke
+ ___50-[LUI2WiFiController _handleInterfaceEventOfType:]_block_invoke
+ ___56-[LUIAuthenticationServiceProvider resetActivationState]_block_invoke
+ ___57-[LUI2WiFiController _refreshStatusFromInterfaceOffQueue]_block_invoke
+ ___57-[LUI2WiFiController _refreshStatusFromInterfaceOffQueue]_block_invoke_2
+ ___65-[LUI2WiFiController _invalidateCachedUIStateAfterConnectionLoss]_block_invoke
+ ___block_descriptor_32_e61_v24?0"<LUI2WiFiControllerDelegate>"8"LUI2WiFiController"16l
+ ___block_descriptor_40_e8_32s_e61_v24?0"<LUI2WiFiControllerDelegate>"8"LUI2WiFiController"16l
+ ___block_descriptor_40_e8_32w_e53_v48?0"NSSet"8"NSSet"16"LUI2WiFiNetwork"24{?=qq}32l
+ ___block_descriptor_56_e8_32s40s48w_e53_v48?0"NSSet"8"NSSet"16"LUI2WiFiNetwork"24{?=qq}32l
+ ___block_descriptor_56_e8_32s_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56bs_e5_v8?0l
+ _objc_exception_rethrow
+ _objc_msgSend$LUIMemojiDescriptorRandom
+ _objc_msgSend$_applyUIState:
+ _objc_msgSend$_beginLayoutTransitionTo:
+ _objc_msgSend$_beginScanning
+ _objc_msgSend$_beginUIStateQuery
+ _objc_msgSend$_clearNetworks
+ _objc_msgSend$_currentDelegates
+ _objc_msgSend$_currentLineHeight
+ _objc_msgSend$_endLayoutTransition:
+ _objc_msgSend$_endScanning
+ _objc_msgSend$_generateTestAvatarIfNeeded
+ _objc_msgSend$_handleInterfaceEventOfType:
+ _objc_msgSend$_handlePointerEvent:
+ _objc_msgSend$_hasPlatformSSOMessage
+ _objc_msgSend$_injectedTestUserCount
+ _objc_msgSend$_injectedTestUsers
+ _objc_msgSend$_invalidateCachedUIState
+ _objc_msgSend$_invalidateCachedUIStateAfterConnectionLoss
+ _objc_msgSend$_menuBarImageForState:bars:
+ _objc_msgSend$_notifyDelegates:block:
+ _objc_msgSend$_notifyStatusUpdated
+ _objc_msgSend$_platformSSOMessageLayoutActive
+ _objc_msgSend$_pointerInputIsDrivingSelection
+ _objc_msgSend$_refreshStatusFromInterfaceOffQueue
+ _objc_msgSend$_refreshStatusFromUIState
+ _objc_msgSend$_requeryUIState
+ _objc_msgSend$_setStatus:
+ _objc_msgSend$_setStatusFromInterface
+ _objc_msgSend$_showDisabledMenu
+ _objc_msgSend$_tintedMenuBarImageForStatus:
+ _objc_msgSend$_updateMessageLayoutForPlatformSSO
+ _objc_msgSend$_wifiImageWithSymbolName:bars:paletteColors:
+ _objc_msgSend$addAvatarPresentedOnScreenCallbackWithQueue:block:
+ _objc_msgSend$addDelegate:
+ _objc_msgSend$cachedUIState
+ _objc_msgSend$connectedMenuBarImageForBars:
+ _objc_msgSend$hashTableWithOptions:
+ _objc_msgSend$heightForLineCount:
+ _objc_msgSend$interfaceRSSI
+ _objc_msgSend$isHandlingPointerEvent
+ _objc_msgSend$layoutTransitionGeneration
+ _objc_msgSend$lineFragmentRectForGlyphAtIndex:effectiveRange:
+ _objc_msgSend$maxContentHeight
+ _objc_msgSend$monitorCount
+ _objc_msgSend$monitoringGeneration
+ _objc_msgSend$openingMultiUserLayout
+ _objc_msgSend$platformSSOUIVisible
+ _objc_msgSend$providerForModule:
+ _objc_msgSend$proxyQueue
+ _objc_msgSend$proxyUnusable
+ _objc_msgSend$queryInFlight
+ _objc_msgSend$queryWiFiUIState
+ _objc_msgSend$refreshStatus
+ _objc_msgSend$removeDelegate:
+ _objc_msgSend$resetActivationState
+ _objc_msgSend$scanCount
+ _objc_msgSend$serialQueue
+ _objc_msgSend$setCachedUIState:
+ _objc_msgSend$setInterfaceRSSI:
+ _objc_msgSend$setLayoutTransitionGeneration:
+ _objc_msgSend$setManagerDelegate:
+ _objc_msgSend$setMonitorCount:
+ _objc_msgSend$setMonitoringGeneration:
+ _objc_msgSend$setOpeningMultiUserLayout:
+ _objc_msgSend$setProxyUnusable:
+ _objc_msgSend$setQueryInFlight:
+ _objc_msgSend$setScanCount:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$setTestAvatarDescriptor:
+ _objc_msgSend$setTestAvatarGenerated:
+ _objc_msgSend$setTestAvatarStickerConfiguration:
+ _objc_msgSend$setUiStateQueried:
+ _objc_msgSend$status
+ _objc_msgSend$testAvatarDescriptor
+ _objc_msgSend$testAvatarGenerated
+ _objc_msgSend$testAvatarStickerConfiguration
+ _objc_msgSend$tintedMenuBarImages
+ _objc_msgSend$uiStateQueried
+ _objc_msgSend$wifiControllerDidUpdateStatus:
+ _objc_terminate
+ _swift_bridgeObjectRelease_n
- -[LUI2WiFiController _notifyEventUpdate:]
- -[LUI2WiFiController delegate]
- -[LUI2WiFiController isDeviceAttached]
- -[LUI2WiFiController isServiceActive]
- -[LUI2WiFiController monitoring]
- -[LUI2WiFiController scanning]
- -[LUI2WiFiController setDelegate:]
- -[LUI2WiFiController setIsDeviceAttached:]
- -[LUI2WiFiController setIsServiceActive:]
- -[LUI2WiFiController setMonitoring:]
- -[LUI2WiFiController setScanning:]
- -[LUI2WiFiNetwork(Images) _getVariableValue:accessibilityDescription:forBars:]
- -[LUI2WiFiNetwork(Images) _wifiImageWithSymbolName:paletteColors:]
- -[LUI2WiFiNetwork(Images) menuBarImage]
- -[LUI2WiFiViewController wifiController:didReceiveEventUpdate:]
- -[LUITestUserController _randomUserAvatar]
- GCC_except_table113
- GCC_except_table117
- GCC_except_table135
- GCC_except_table34
- GCC_except_table41
- GCC_except_table64
- GCC_except_table65
- GCC_except_table69
- GCC_except_table80
- GCC_except_table83
- GCC_except_table86
- GCC_except_table90
- GCC_except_table98
- OBJC_IVAR_$_LUI2WiFiController._delegate
- OBJC_IVAR_$_LUI2WiFiController._isDeviceAttached
- OBJC_IVAR_$_LUI2WiFiController._isServiceActive
- OBJC_IVAR_$_LUI2WiFiController._monitoring
- OBJC_IVAR_$_LUI2WiFiController._scanning
- ___41-[LUI2WiFiController _notifyEventUpdate:]_block_invoke
- ___45-[LUI2WiFiController interfaceAddedWithName:]_block_invoke
- ___47-[LUI2WiFiController interfaceRemovedWithName:]_block_invoke
- ___60-[LUI2WiFiController linkDidChangeForWiFiInterfaceWithName:]_block_invoke
- ___60-[LUI2WiFiController modeDidChangeForWiFiInterfaceWithName:]_block_invoke
- ___60-[LUI2WiFiController ssidDidChangeForWiFiInterfaceWithName:]_block_invoke
- ___66-[LUI2WiFiController powerStateDidChangeForWiFiInterfaceWithName:]_block_invoke
- ___block_descriptor_40_e8_32w_e48_v36?0"NSSet"8"NSSet"16"LUI2WiFiNetwork"24B32l
- ___block_descriptor_56_e8_32s40s48w_e48_v36?0"NSSet"8"NSSet"16"LUI2WiFiNetwork"24B32l
- ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0l
- _objc_msgSend$_notifyEventUpdate:
- _objc_msgSend$_wifiImageWithSymbolName:paletteColors:
- _objc_msgSend$isDeviceAttached
- _objc_msgSend$isServiceActive
- _objc_msgSend$menuBarImage
- _objc_msgSend$monitoring
- _objc_msgSend$scanning
- _objc_msgSend$setIsDeviceAttached:
- _objc_msgSend$setIsServiceActive:
- _objc_msgSend$setMonitoring:
- _objc_msgSend$setScanning:
- _objc_msgSend$wifiController:didReceiveEventUpdate:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
+ "AHP manager evicted module %@"
+ "AHP manager lost the connection to module %@"
+ "Blank User"
+ "LUI2WiFiController CWWiFiUIProxyClient is nil (root with no console user) - status will come from CWInterface"
+ "LUI2WiFiController UI state carries no connection bits"
+ "LUI2WiFiController UI state unavailable"
+ "LUI2WiFiController already monitoring (%lu clients)"
+ "LUI2WiFiController already scanning (%lu clients)"
+ "LUI2WiFiController cleared network list (interface unavailable or powered off)"
+ "LUI2WiFiController discarding superseded UI state query"
+ "LUI2WiFiController ignoring UI state push while not monitoring"
+ "LUI2WiFiController interface refreshed off-queue - power:%d rssi:%ld"
+ "LUI2WiFiController interface updated - power:%d rssi:%ld"
+ "LUI2WiFiController status -> state:%ld bars:%ld"
+ "LUI2WiFiController status from interface - rssi:%ld state:%ld bars:%ld"
+ "LUI2WiFiController still monitoring (%lu clients)"
+ "LUI2WiFiController still scanning (%lu clients)"
+ "LWUITestInjectBlankMustChangeUser"
+ "LWUITestInjectMigratedMustChangeUser"
+ "Migrated User"
+ "Module of service %@ is gone: dropping activation state for %@"
+ "No service provider for module: %@"
+ "TestUserHasComplexPassword"
+ "WIFI_DISABLED"
+ "WiFi didUpdateStatus %p"
+ "WiFi menu showing disabled state"
+ "_updateScanResults: ignoring empty scan result batch"
+ "blankUser"
+ "com.apple.loginUIKit.wifiController.proxy"
+ "migratedUser"
+ "realpassword"
+ "v24@?0@\"<LUI2WiFiControllerDelegate>\"8@\"LUI2WiFiController\"16"
+ "v48@?0@\"NSSet\"8@\"NSSet\"16@\"LUI2WiFiNetwork\"24{?=qq}32"
+ "\xf0Q"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
- "/System/Library/Desktop Pictures/Mac "
- "LUI2WiFiController already monitoring"
- "LUI2WiFiController already scanning"
- "LUI2WiFiController interface updated - power:%d attached:%d active:%d"
- "Unknown enclosure color %ld"
- "WiFi CWEventTypePowerDidChange"
- "WiFi didReceiveEventUpdate: %l"
- "v36@?0@\"NSSet\"8@\"NSSet\"16@\"LUI2WiFiNetwork\"24B32"
- "\xf0A"
```
