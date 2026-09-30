## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-627.0.14.0.0
-  __TEXT.__text: 0xd3ad0
-  __TEXT.__objc_methlist: 0xb89c
+627.0.19.0.0
+  __TEXT.__text: 0xd413c
+  __TEXT.__objc_methlist: 0xbc24
   __TEXT.__const: 0x2624
-  __TEXT.__cstring: 0x4d41
-  __TEXT.__gcc_except_tab: 0x1d48
-  __TEXT.__oslogstring: 0x5ba6
+  __TEXT.__cstring: 0x4df1
+  __TEXT.__gcc_except_tab: 0x1d54
+  __TEXT.__oslogstring: 0x5b56
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xa2
   __TEXT.__constg_swiftt: 0x2e90

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__unwind_info: 0x2ce8
+  __TEXT.__unwind_info: 0x2d10
   __TEXT.__eh_frame: 0xa20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1938
-  __DATA_CONST.__objc_classlist: 0x5b0
+  __DATA_CONST.__const: 0x1908
+  __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b90
+  __DATA_CONST.__objc_selrefs: 0x6bf0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x398
-  __DATA_CONST.__objc_arraydata: 0xd8
-  __DATA_CONST.__got: 0xe10
+  __DATA_CONST.__objc_arraydata: 0x118
+  __DATA_CONST.__got: 0xe28
   __AUTH_CONST.__const: 0x2fd0
-  __AUTH_CONST.__cfstring: 0x3760
-  __AUTH_CONST.__objc_const: 0x15200
+  __AUTH_CONST.__cfstring: 0x3900
+  __AUTH_CONST.__objc_const: 0x156c0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH_CONST.__objc_doubleobj: 0x70
+  __AUTH_CONST.__objc_arrayobj: 0x240
+  __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__auth_got: 0xf20
-  __AUTH.__objc_data: 0x6920
+  __AUTH.__objc_data: 0x6ab0
   __AUTH.__data: 0x670
-  __DATA.__objc_ivar: 0xbac
+  __DATA.__objc_ivar: 0xbbc
   __DATA.__data: 0x2590
-  __DATA.__bss: 0x2780
+  __DATA.__bss: 0x2790
   __DATA.__common: 0x4c0
   __DATA_DIRTY.__objc_data: 0x820
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4861
-  Symbols:   9712
-  CStrings:  1236
+  Functions: 4931
+  Symbols:   9824
+  CStrings:  1247
 
Symbols:
+ +[NSUserDefaults(TVRemoteUI) tvRemoteUI]
+ +[NSUserDefaults(TVRemoteUI) tvrui_migrateAccessibilityPreferencesIfNeeded]
+ +[TVRUIFakeDevice fakeDevicesWithCount:]
+ -[NSUserDefaults(TVRemoteUI) tvrui_forceLiveTVButtons]
+ -[NSUserDefaults(TVRemoteUI) tvrui_usesSimpleGestures]
+ -[TVRUIControlPanelViewController loadView]
+ -[TVRUIDarkStyleProvider deviceListMaxHeight]
+ -[TVRUIDevicePickerViewController _updateTableViewFadeMask]
+ -[TVRUIDevicePickerViewController setTableViewFadeMask:]
+ -[TVRUIDevicePickerViewController tableViewFadeMask]
+ -[TVRUIFakeDelegate device:beganTextEditingWithAttributes:initialText:]
+ -[TVRUIFakeDelegate device:didEncounterAuthenticationThrottle:]
+ -[TVRUIFakeDelegate device:didUpdateAttributes:]
+ -[TVRUIFakeDelegate device:didUpdateNowPlayingInfo:]
+ -[TVRUIFakeDelegate device:didUpdateSiriRemoteFindingSessionState:]
+ -[TVRUIFakeDelegate device:didUpdateText:]
+ -[TVRUIFakeDelegate device:didUpdateTopShelfInfo:]
+ -[TVRUIFakeDelegate device:endedTextEditingWithAttributes:endingText:]
+ -[TVRUIFakeDelegate device:hasCaptionsEnabled:]
+ -[TVRUIFakeDelegate device:hasGuideButtonEnabled:]
+ -[TVRUIFakeDelegate device:hidesMediaControls:]
+ -[TVRUIFakeDelegate device:needsMediaControls:]
+ -[TVRUIFakeDelegate device:supportsSiri:volumeControl:]
+ -[TVRUIFakeDelegate device:supportsVolumeControl:]
+ -[TVRUIFakeDelegate device:updatedFindMyRemoteSupport:]
+ -[TVRUIFakeDelegate device:updatedPairedRemoteInfo:]
+ -[TVRUIFakeDelegate deviceBeganConnecting:]
+ -[TVRUIFakeDelegate deviceDidConnect:]
+ -[TVRUIFakeDelegate deviceDidDisconnect:reason:error:]
+ -[TVRUIFakeDelegate deviceDidEncounterAuthenticationChallenge:passwordType:passcode:]
+ -[TVRUIFakeDelegate deviceInfoUpdated:]
+ -[TVRUIFakeDevice .cxx_destruct]
+ -[TVRUIFakeDevice airplayIdentifier]
+ -[TVRUIFakeDevice captionsEnabled]
+ -[TVRUIFakeDevice classification]
+ -[TVRUIFakeDevice connectWithConnectionContext:]
+ -[TVRUIFakeDevice connect]
+ -[TVRUIFakeDevice debugName]
+ -[TVRUIFakeDevice delegate]
+ -[TVRUIFakeDevice deviceContextInformation]
+ -[TVRUIFakeDevice disconnectSystemInitiated]
+ -[TVRUIFakeDevice disconnectUserInitiated]
+ -[TVRUIFakeDevice disconnectWithTimeOut]
+ -[TVRUIFakeDevice findMyRemoteSupport]
+ -[TVRUIFakeDevice hasIdentifier:]
+ -[TVRUIFakeDevice identifier]
+ -[TVRUIFakeDevice isConnected]
+ -[TVRUIFakeDevice isConnecting]
+ -[TVRUIFakeDevice isEqualToDevice:]
+ -[TVRUIFakeDevice isModernAppleTV]
+ -[TVRUIFakeDevice isPaired]
+ -[TVRUIFakeDevice mediaRemoteIdentifier]
+ -[TVRUIFakeDevice model]
+ -[TVRUIFakeDevice name]
+ -[TVRUIFakeDevice setDelegate:]
+ -[TVRUIFakeDevice setIdentifier:]
+ -[TVRUIFakeDevice setModel:]
+ -[TVRUIFakeDevice setName:]
+ -[TVRUIFakeDevice supportsCaptionsToggle]
+ -[TVRUIFakeDevice supportsDirectCaptionQueries]
+ -[TVRUIFakeDevice supportsDonatingIntents]
+ -[TVRUIFakeDevice supportsFindMyRemote]
+ -[TVRUIFakeDevice supportsGuide]
+ -[TVRUIFakeDevice supportsLaunchingApplications]
+ -[TVRUIFakeDevice supportsModernConnections]
+ -[TVRUIFakeDevice supportsMute]
+ -[TVRUIFakeDevice supportsPaging]
+ -[TVRUIFakeDevice supportsPower]
+ -[TVRUIFakeDevice supportsSiri]
+ -[TVRUIFakeDevice supportsTouchEvents]
+ -[TVRUIFakeDevice supportsVolumeControl]
+ -[TVRUIMediaControlsViewController loadView]
+ -[TVRUITitleView sizeThatFits:]
+ -[TVRUITouchpadViewController loadView]
+ GCC_except_table187
+ GCC_except_table59
+ GCC_except_table66
+ GCC_except_table82
+ _OBJC_CLASS_$_TVRUIControlPanelView
+ _OBJC_CLASS_$_TVRUIFakeDelegate
+ _OBJC_CLASS_$_TVRUIFakeDevice
+ _OBJC_CLASS_$_TVRUIMediaControlsView
+ _OBJC_CLASS_$_TVRUITouchpadContainerView
+ _OBJC_IVAR_$_TVRUIDevicePickerViewController._tableViewFadeMask
+ _OBJC_IVAR_$_TVRUIFakeDevice._identifier
+ _OBJC_IVAR_$_TVRUIFakeDevice._model
+ _OBJC_IVAR_$_TVRUIFakeDevice._name
+ _OBJC_METACLASS_$_TVRUIControlPanelView
+ _OBJC_METACLASS_$_TVRUIFakeDelegate
+ _OBJC_METACLASS_$_TVRUIFakeDevice
+ _OBJC_METACLASS_$_TVRUIMediaControlsView
+ _OBJC_METACLASS_$_TVRUITouchpadContainerView
+ _TVRUIDidMigrateFromAXKey
+ _TVRUIForceLiveTVButtonsKey
+ _TVRUIUsesSimpleGesturesKey
+ _UIFontTextStyleExtraLargeTitle
+ _UIFontWeightLight
+ _UILayoutFittingCompressedSize
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSUserDefaults_$_TVRemoteUI
+ __OBJC_$_CATEGORY_NSUserDefaults_$_TVRemoteUI
+ __OBJC_$_CLASS_METHODS_TVRUIFakeDevice
+ __OBJC_$_CLASS_PROP_LIST_NSUserDefaults_$_TVRemoteUI
+ __OBJC_$_INSTANCE_METHODS_NSUserDefaults(TVRemoteUI|TVRemoteUI)
+ __OBJC_$_INSTANCE_METHODS_TVRUIFakeDelegate
+ __OBJC_$_INSTANCE_METHODS_TVRUIFakeDevice
+ __OBJC_$_INSTANCE_VARIABLES_TVRUIFakeDevice
+ __OBJC_$_PROP_LIST_TVRUIFakeDelegate
+ __OBJC_$_PROP_LIST_TVRUIFakeDevice
+ __OBJC_CLASS_PROTOCOLS_$_TVRUIFakeDelegate
+ __OBJC_CLASS_PROTOCOLS_$_TVRUIFakeDevice
+ __OBJC_CLASS_RO_$_TVRUIControlPanelView
+ __OBJC_CLASS_RO_$_TVRUIFakeDelegate
+ __OBJC_CLASS_RO_$_TVRUIFakeDevice
+ __OBJC_CLASS_RO_$_TVRUIMediaControlsView
+ __OBJC_CLASS_RO_$_TVRUITouchpadContainerView
+ __OBJC_METACLASS_RO_$_TVRUIControlPanelView
+ __OBJC_METACLASS_RO_$_TVRUIFakeDelegate
+ __OBJC_METACLASS_RO_$_TVRUIFakeDevice
+ __OBJC_METACLASS_RO_$_TVRUIMediaControlsView
+ __OBJC_METACLASS_RO_$_TVRUITouchpadContainerView
+ ___40+[NSUserDefaults(TVRemoteUI) tvRemoteUI]_block_invoke
+ _objc_msgSend$_updateTableViewFadeMask
+ _objc_msgSend$areMediaControlsVisible
+ _objc_msgSend$deviceListMaxHeight
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setMask:
+ _objc_msgSend$setModel:
+ _objc_msgSend$setTableViewFadeMask:
+ _objc_msgSend$tableViewFadeMask
+ _objc_msgSend$tvRemoteUI
+ _objc_msgSend$tvrui_forceLiveTVButtons
+ _objc_msgSend$tvrui_migrateAccessibilityPreferencesIfNeeded
+ _objc_msgSend$tvrui_usesSimpleGestures
- -[TVRUIDevicePickerViewController _insets]
- -[TVRUIRemoteViewController viewWillTransitionToSize:withTransitionCoordinator:]
- -[TVRUITouchpadViewController _simpleRemoteGesturesEnabled:]
- -[TVRUITouchpadViewController viewWillDisappear:]
- GCC_except_table122
- GCC_except_table190
- GCC_except_table62
- GCC_except_table69
- GCC_except_table85
- __CATEGORY_INSTANCE_METHODS_NSUserDefaults_$_TVRemoteUI
- __CATEGORY_NSUserDefaults_$_TVRemoteUI
- __CATEGORY_PROPERTIES_NSUserDefaults_$_TVRemoteUI
- ___80-[TVRUIRemoteViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke
- ___80-[TVRUIRemoteViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke_2
- ___block_descriptor_32_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8l
- ___block_descriptor_49_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
- _kAXSAppleTVRemoteSimpleGesturesEnabledNotification
- _objc_msgSend$_insets
- _objc_msgSend$currentModalContext
- _objc_msgSend$primaryButtonMinSize
- _objc_msgSend$removeObserver:name:object:
- _objc_msgSend$secondaryButtonMinSize
CStrings:
+ "#directional - toggleControlState mediaControlsAreVisible:%{bool}d small:%{bool}d landscape:%{bool}d"
+ "AppleTV11,1"
+ "AppleTV14,1"
+ "AppleTV6,2"
+ "Basement"
+ "Bedroom"
+ "Kitchen"
+ "Living Room"
+ "Office"
+ "TVRUIDidMigrateFromAX"
+ "TVRUIForceLiveTVButtons"
+ "TVRUIUsesSimpleGestures"
+ "TVRemote migration: simpleGestures=%d, forceLiveTV=%d"
+ "fake-device-%lu"
+ "group.com.apple.TVRemote"
- "#directional - toggleControlState %d %d"
- "Accessibility simple remote gestures enabled notification received"
- "Registered to listen for accessibility simple remote gestures"
- "Unregistered to listen for accessibility simple remote gestures"
```
