## BluetoothModule

> `/System/Library/ControlCenter/Bundles/BluetoothModule.bundle/BluetoothModule`

```diff

-598.0.0.0.0
-  __TEXT.__text: 0x1200
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x1cc
-  __TEXT.__const: 0x60
-  __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methname: 0xaaf
-  __TEXT.__objc_methtype: 0x470
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__cstring: 0x169
-  __TEXT.__oslogstring: 0x154
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x130
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__cfstring: 0x1e0
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x18
+599.2.0.0.0
+  __TEXT.__text: 0x78
+  __TEXT.__auth_stubs: 0x50
+  __TEXT.__objc_stubs: 0x40
+  __TEXT.__objc_methlist: 0x38
+  __TEXT.__const: 0x40
+  __TEXT.__objc_classname: 0x31
+  __TEXT.__objc_methname: 0x35d
+  __TEXT.__objc_methtype: 0x26c
+  __TEXT.__unwind_info: 0x60
+  __DATA_CONST.__auth_got: 0x30
+  __DATA_CONST.__got: 0x8
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x848
-  __DATA.__objc_selrefs: 0x200
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x120
-  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  __DATA.__objc_const: 0x5c8
+  __DATA.__objc_selrefs: 0x28
+  __DATA.__objc_ivar: 0x4
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0xc0
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
-  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
-  - /System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices
   - /System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI
   - /System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 41
-  Symbols:   68
-  CStrings:  179
+  Functions: 4
+  Symbols:   15
+  CStrings:  69
 
Symbols:
- _OBJC_CLASS_$_CCUIBluetoothMenuModuleViewController
- __os_log_impl
- _dispatch_async
- _objc_storeWeak
- _OBJC_CLASS_$_CCUIContentModuleDetailClickPresentationInteractionManager
- ___stack_chk_guard
- _objc_release_x23
- _objc_retain_x19
- _CCUILogUserInterface
- _OBJC_CLASS_$_CCUIButtonModuleViewController
- _objc_release_x9
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_CLASS_$_UIStatusBarServer
- ___stack_chk_fail
- _objc_destroyWeak
- _objc_release_x25
- _OBJC_CLASS_$_NSString
- _dispatch_get_global_queue
- _objc_initWeak
- _BluetoothConnectionStatusChangedNotification
- _OBJC_CLASS_$_BluetoothManager
- _OBJC_CLASS_$_CCUIControlCenterDefaults
- _OBJC_METACLASS_$_CCUIButtonModuleViewController
- ___NSArray0__struct
- _objc_release_x20
- _os_log_type_enabled
- _OBJC_CLASS_$_UIColor
- __dispatch_main_q
- _objc_release_x21
- _objc_retain_x21
- _objc_retain_x25
- _CCSIsInternalInstall
- ___objc_personality_v0
- _objc_msgSendSuper2
- _objc_retain_x2
- _objc_retain_x22
- _objc_opt_class
- _objc_alloc_init
- _objc_copyWeak
- _objc_release_x8
- _OBJC_CLASS_$_UIImage
- _OBJC_METACLASS_$_CCUIBluetoothModuleViewController
- __Unwind_Resume
- _objc_release_x22
- ___CFConstantStringClassReference
- _BSEqualObjects
- _objc_loadWeakRetained
- _objc_retain_x3
- _OBJC_CLASS_$_NSBundle
- __NSConcreteStackBlock
- _objc_release
- _objc_retain
- _BluetoothStateChangedNotification
CStrings:
- "defaultCenter"
- "contentModuleDetailClickPresentationInteractionControllerInteractionEnded:wasCancelled:"
- "_debugDescriptionForState:"
- "copy"
- "getStatusBarOverrideData"
- "removeObserver:name:object:"
- "setGlyphImage:"
- "_bluetoothManager"
- "_updateState"
- "@20@0:8i16"
- "_systemImageNamed:"
- "connectedDeviceNamesThatMayBeDenylisted"
- "count"
- "localizedStringWithFormat:"
- "shouldExcludeControlCenterFromStatusBarOverrides"
- "setSelected:"
- "standardDefaults"
- "stopObservingStateChanges"
- "viewDidLoad"
- "viewWillAppear:"
- "_updateWithState:"
- "power-off"
- "CONTROL_CENTER_STATUS_BLUETOOTH_OFF"
- "[Bluetooth Module] Bluetooth state updated to %!{(MISSING)public}@ [ inoperative: %!d(MISSING) enabled: %!d(MISSING) subtitle: %!{(MISSING)private}@ ]"
- "_bluetoothConnectionStatusDidChange:"
- "_canShowWhileLocked"
- "contentModuleDetailClickPresentationInteractionControllerInteractionShouldBegin:"
- "observingStateChanges"
- "v12@?0B8"
- "@\"NSArray\""
- "bluetoothState"
- "viewWillDisappear:"
- "startObservingStateChanges"
- "v32@0:8@16@?24"
- "isObservingStateChanges"
- "[Bluetooth Module] Toggled Bluetooth state from %!{(MISSING)public}@ to %!{(MISSING)public}@"
- "_bluetoothStateDidChange:"
- "disconnected"
- "@\"CCUIContentModuleDetailClickPresentationInteractionManager\""
- "[Bluetooth Module] Toggle Bluetooth state from %!{(MISSING)public}@"
- "B24@0:8@\"CCUIContentModuleDetailClickPresentationInteractionManager\"16"
- "stopObservingStateChangesIfNecessary"
- "v32@0:8@16@24"
- "CONTROL_CENTER_STATUS_BLUETOOTH_BUSY"
- "CONTROL_CENTER_STATUS_BLUETOOTH_ON"
- "_stateWithOverridesApplied:"
- "bundleForClass:"
- "buttonTapped:forEvent:"
- "startObservingStateChangesIfNecessary"
- "connected"
- "[Bluetooth Module] Bluetooth state changed"
- "_subtitleTextWithState:"
- "v28@0:8@\"CCUIContentModuleDetailClickPresentationInteractionManager\"16B24"
- "v8@?0"
- "ControlCenterUI+SystemModules"
- "_updateConnectedDeviceNames"
- "setObservingStateChanges:"
- "unavailable"
- "A"
- "v32@0:8@\"CCUIContentModuleDetailClickPresentationInteractionManager\"16@?<v@?B>24"
- "CONTROL_CENTER_STATUS_BLUETOOTH_NAME"
- "i20@0:8i16"
- "setModalPresentationStyle:"
- "setValueText:"
- "systemBlueColor"
- "CCUIContentModuleDetailClickPresentationInteractionManagerDelegate"
- "TB,N,GisObservingStateChanges,V_observingStateChanges"
- "firstObject"
- "@\"BluetoothManager\""
- "CONTROL_CENTER_STATUS_BLUETOOTH_DISCONNECTED"
- "init"
- "CCUIBluetoothModuleViewController"
- "_currentState"
- "_presentingMenuViewController"
- "bluetoothStateActionWithCompletion:"
- "busy"
- "requestAuthenticationWithCompletionHandler:"
- "v20@0:8i16"
- "B"
- "_enabledForState:"
- "_inoperativeForState:"
- "bluetooth"
- "contentModuleDetailClickPresentationInteractionController:requestsAuthenticationForPresentationWithCompletionHandler:"
- "view"
- "_connectedDeviceNames"
- "i16@0:8"
- "initWithPresentingViewController:delegate:"
- "T@\"CCUIContentModuleContext\",W,N,V_contentModuleContext"
- "length"
- "sharedInstance"
- "\x03"
- "presentedViewControllerForContentModuleDetailClickPresentationInteractionController:"
- "setTitle:"
- "_clickPresentationInteractionManager"
- "v12@?0i8"
- "[Bluetooth Module] Bluetooth connection status changed"
- "_glyphImageForState:"
- "_observingStateChanges"
- "addObserver:selector:name:object:"
- "setSelectedGlyphColor:"
- "v28@0:8@16B24"
- "CONTROL_CENTER_STATUS_BLUETOOTH_DEVICES"
- "bluetooth.slash"
- "shouldBeginTransitionToExpandedContentModule"
- "B20@0:8i16"
- "_toggleState"
- "localizedStringForKey:value:table:"
- "@\"UIViewController\"24@0:8@\"CCUIContentModuleDetailClickPresentationInteractionManager\"16"
- "v20@0:8B16"
- "setViewForInteraction:"

```
