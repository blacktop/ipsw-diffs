## SiriUIActivation

> `/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation`

```diff

-3404.71.4.11.4
-  __TEXT.__text: 0x22578
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x1c34
+3405.21.1.1.2
+  __TEXT.__text: 0x23938
+  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__objc_methlist: 0x1db4
   __TEXT.__const: 0x2be
-  __TEXT.__gcc_except_tab: 0xadc
-  __TEXT.__cstring: 0x39c2
-  __TEXT.__oslogstring: 0x4104
+  __TEXT.__gcc_except_tab: 0xafc
+  __TEXT.__cstring: 0x3e62
+  __TEXT.__oslogstring: 0x44d4
   __TEXT.__swift5_typeref: 0x177
   __TEXT.__constg_swiftt: 0x134
   __TEXT.__swift5_reflstr: 0x11b

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0xaa0
-  __TEXT.__eh_frame: 0x5c0
-  __TEXT.__objc_classname: 0x318
-  __TEXT.__objc_methname: 0x77ca
-  __TEXT.__objc_methtype: 0x14aa
-  __TEXT.__objc_stubs: 0x5380
-  __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0xb80
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__unwind_info: 0xad0
+  __TEXT.__eh_frame: 0x5c8
+  __TEXT.__objc_classname: 0x337
+  __TEXT.__objc_methname: 0x7c06
+  __TEXT.__objc_methtype: 0x14e9
+  __TEXT.__objc_stubs: 0x5680
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0xbb0
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a40
+  __DATA_CONST.__objc_selrefs: 0x1b58
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__const: 0x3d0
-  __AUTH_CONST.__cfstring: 0x7c0
-  __AUTH_CONST.__objc_const: 0x1c30
+  __AUTH_CONST.__cfstring: 0x800
+  __AUTH_CONST.__objc_const: 0x1dc0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x18c
-  __DATA.__data: 0x688
-  __DATA.__bss: 0x250
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x1a0
+  __DATA.__data: 0x6d8
   __DATA.__common: 0x18
+  __DATA.__bss: 0x200
   __DATA_DIRTY.__objc_data: 0x328
-  __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__data: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI
   - /System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
+  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 720
-  Symbols:   973
-  CStrings:  1703
+  Functions: 766
+  Symbols:   1031
+  CStrings:  1792
 
Symbols:
+ _BluetoothDeviceConnectSuccessNotification
+ _BluetoothDeviceDisconnectSuccessNotification
+ _BluetoothHandsfreeEndedVoiceCommand
+ _BluetoothHandsfreeInitiatedVoiceCommand
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _OBJC_CLASS_$_BluetoothManager
+ _OBJC_CLASS_$_SiriBluetoothDeviceSource
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ _kAFSiriCapabilitiesDidChangeNotification
+ _objc_getProperty
+ _objc_setProperty_atomic
+ _objc_setProperty_atomic_copy
CStrings:
+ "\x12\x11"
+ "%s #dismissal GMS availability did change"
+ "%s #dismissal Resetting gesture behaviors"
+ "%s #dismissal Siri capabilities did change"
+ "%s #dismissal Updating shareHomeGesture from %d to %d"
+ "%s #dismissal Updating shouldDismissForSwipesOutsideContent from %d to %d"
+ "%s #dismissal Updating shouldDismissForTapOutsideContent from %d to %d"
+ "%s #dismissal Updating shouldDismissForTapsOutsideContent from %d to %d"
+ "%s #dismissal Updating shouldPassTouchesThroughToSpringBoard from %d to %d"
+ "%s #shih Error getting current persona id: %@"
+ "%s #shih Guest success"
+ "%s #shih Not a supported device, ignoring bluetooth"
+ "%s #shih Not a supported device, ignoring bluetooth disconnect"
+ "%s #shih connected success (Apple:%d)"
+ "%s #shih disconnected success"
+ "%s #shih ended voice control"
+ "%s #shih headphone monitor setup start"
+ "%s #shih initiated voice control"
+ "%s #shih multiple devices connected, this is not allowed"
+ "%s #shih setup observer"
+ "%s #shih updated assignment made<%d> to device %@ for user %@"
+ "-[SiriHeadphoneIdentityHelper assignUserData:connected:identifier:]"
+ "-[SiriHeadphoneIdentityHelper bluetoothDeviceConnectSuccess:]"
+ "-[SiriHeadphoneIdentityHelper bluetoothDeviceDisconnectSuccess:]"
+ "-[SiriHeadphoneIdentityHelper bluetoothDeviceEndedVoiceControl:]"
+ "-[SiriHeadphoneIdentityHelper bluetoothDeviceInitiatedVoiceControl:]"
+ "-[SiriHeadphoneIdentityHelper init:]"
+ "-[SiriHeadphoneIdentityHelper setupBluetoothNotificationObservers]"
+ "-[SiriHeadphoneIdentityHelper updatePersonaId:identifier:]_block_invoke"
+ "-[SiriPresentationSpringBoardMainScreenViewController resetGestureBehaviors]"
+ "-[SiriPresentationSpringBoardMainScreenViewController setShouldDismissForSwipesOutsideContent:]_block_invoke"
+ "-[SiriPresentationSpringBoardMainScreenViewController setShouldDismissForTapOutsideContent:]_block_invoke"
+ "-[SiriPresentationSpringBoardMainScreenViewController setShouldDismissForTapsOutsideContent:]_block_invoke"
+ "-[SiriPresentationSpringBoardMainScreenViewController setShouldPassTouchesThroughToSpringBoard:]_block_invoke"
+ "00000000-0000-0000-0000-000000000000"
+ "@\"<NSObject>\""
+ "@\"BluetoothManager\""
+ "@\"NSString\""
+ "SiriHeadphoneIdentityHelper"
+ "T@\"<NSObject>\",W,V_viewController"
+ "T@\"BluetoothManager\",&,V_bluetoothManager"
+ "T@\"NSString\",C,V_btIdentifier"
+ "T@\"NSString\",C,V_userProfileIdentifier"
+ "TB,V_headphoneConnected"
+ "_GenerativeModelsAvailabilityDidChange"
+ "_SiriCapabilitiesDidChange"
+ "_bluetoothManager"
+ "_btIdentifier"
+ "_generativeModelsAvailabilityDidChange"
+ "_headphoneConnected"
+ "_siriCapabilitiesDidChange"
+ "_startObservingNotifications"
+ "_userProfileIdentifier"
+ "_viewController"
+ "address"
+ "assignUserData:connected:identifier:"
+ "associatedUserProfileIdentifier"
+ "bluetoothDeviceConnectSuccess:"
+ "bluetoothDeviceDisconnectSuccess:"
+ "bluetoothDeviceEndedVoiceControl:"
+ "bluetoothDeviceForIdentifier:bluetoothDevice:"
+ "bluetoothDeviceInitiatedVoiceControl:"
+ "bluetoothManager"
+ "btIdentifier"
+ "clearUserData"
+ "com.apple.gms.availability.notification"
+ "configureJetsamListener"
+ "currentPersonaId:"
+ "deactivate"
+ "headphoneConnected"
+ "init:"
+ "isAppleAudioDevice"
+ "isBluetoothSpeaker:"
+ "isHeadphoneConnected"
+ "isSupportedHeadphoneDevice:"
+ "object"
+ "setBluetoothManager:"
+ "setBtIdentifier:"
+ "setHeadphoneConnected:"
+ "setUserProfileIdentifier:"
+ "setViewController:"
+ "setupBluetoothNotificationObservers"
+ "setupHeadphoneMonitor"
+ "updatePersonaId:identifier:"
+ "updateUserProfileMeta:"
+ "userProfileIdentifier"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v36@0:8@16B24@28"
+ "viewController"

```
