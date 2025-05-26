## MobileStoreDemoKit

> `/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit`

```diff

-1254.42.1.0.0
-  __TEXT.__text: 0x279c4
+1254.60.17.0.0
+  __TEXT.__text: 0x28d20
   __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x1c50
+  __TEXT.__objc_methlist: 0x1de0
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x5db6
+  __TEXT.__cstring: 0x60f8
   __TEXT.__oslogstring: 0x3309
-  __TEXT.__gcc_except_tab: 0x9e8
-  __TEXT.__unwind_info: 0x838
-  __TEXT.__objc_classname: 0x348
-  __TEXT.__objc_methname: 0x5556
-  __TEXT.__objc_methtype: 0xa65
-  __TEXT.__objc_stubs: 0x3c00
+  __TEXT.__gcc_except_tab: 0xa78
+  __TEXT.__unwind_info: 0x8c4
+  __TEXT.__objc_classname: 0x375
+  __TEXT.__objc_methname: 0x58be
+  __TEXT.__objc_methtype: 0xbbb
+  __TEXT.__objc_stubs: 0x3ea0
   __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x4e8
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__const: 0x540
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x27e0
-  __DATA_CONST.__objc_selrefs: 0x1548
+  __DATA_CONST.__objc_const: 0x2b80
+  __DATA_CONST.__objc_selrefs: 0x1610
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__cfstring: 0x4340
-  __AUTH_CONST.__objc_const: 0xcd0
+  __AUTH_CONST.__cfstring: 0x4500
+  __AUTH_CONST.__objc_const: 0xdf0
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH.__objc_data: 0x6e0
+  __AUTH.__objc_data: 0x780
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x1b0
-  __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x1f4
+  __DATA.__objc_classrefs: 0x1c8
+  __DATA.__objc_superrefs: 0xb8
+  __DATA.__objc_ivar: 0x20c
   __DATA.__data: 0x9e0
   __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 985
-  Symbols:   3329
-  CStrings:  2149
+  Functions: 1023
+  Symbols:   3478
+  CStrings:  2220
 
Symbols:
+ +[MSDKPeerDemoAXSettings supportsSecureCoding]
+ +[MSDKPeerDemoIPDStatus supportsSecureCoding]
+ -[MSDKDemoState _isMuseBuddyDemoModeEnabled]
+ -[MSDKDemoState _isPressDemoModeEnabled]
+ -[MSDKPeerDemoAXSettings description]
+ -[MSDKPeerDemoAXSettings encodeWithCoder:]
+ -[MSDKPeerDemoAXSettings gazeAccessibility]
+ -[MSDKPeerDemoAXSettings initWithCoder:]
+ -[MSDKPeerDemoAXSettings init]
+ -[MSDKPeerDemoAXSettings pointerControl]
+ -[MSDKPeerDemoAXSettings setGazeAccessibility:]
+ -[MSDKPeerDemoAXSettings setPointerControl:]
+ -[MSDKPeerDemoAXSettings setStaticFoveation:]
+ -[MSDKPeerDemoAXSettings staticFoveation]
+ -[MSDKPeerDemoDeviceManager getAccessibiltiySettingsOnPeer:withCompletion:]
+ -[MSDKPeerDemoDeviceManager initiateIPDResetOnPeer:targetIPD:withCompletion:]
+ -[MSDKPeerDemoDeviceManager queryIPDResetStageOnPeer:withCompletion:]
+ -[MSDKPeerDemoDeviceManager readIPDStatusFromPeer:withCompletion:]
+ -[MSDKPeerDemoDeviceManager setAccessibiltiySettingsOnPeer:newSettings:withCompletion:]
+ -[MSDKPeerDemoDeviceManager skipAutoIPDAdjustmentOnPeer:withCompletion:]
+ -[MSDKPeerDemoIPDStatus clipOnState]
+ -[MSDKPeerDemoIPDStatus currentIPD]
+ -[MSDKPeerDemoIPDStatus description]
+ -[MSDKPeerDemoIPDStatus encodeWithCoder:]
+ -[MSDKPeerDemoIPDStatus initWithCoder:]
+ -[MSDKPeerDemoIPDStatus initWithTargetIPD:currentIPD:clipOnState:]
+ -[MSDKPeerDemoIPDStatus setClipOnState:]
+ -[MSDKPeerDemoIPDStatus setCurrentIPD:]
+ -[MSDKPeerDemoIPDStatus setTargetIPD:]
+ -[MSDKPeerDemoIPDStatus targetIPD]
+ GCC_except_table10
+ GCC_except_table72
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table83
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table90
+ GCC_except_table91
+ _OBJC_CLASS_$_MSDKPeerDemoAXSettings
+ _OBJC_CLASS_$_MSDKPeerDemoIPDStatus
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_MSDKPeerDemoAXSettings._gazeAccessibility
+ _OBJC_IVAR_$_MSDKPeerDemoAXSettings._pointerControl
+ _OBJC_IVAR_$_MSDKPeerDemoAXSettings._staticFoveation
+ _OBJC_IVAR_$_MSDKPeerDemoIPDStatus._clipOnState
+ _OBJC_IVAR_$_MSDKPeerDemoIPDStatus._currentIPD
+ _OBJC_IVAR_$_MSDKPeerDemoIPDStatus._targetIPD
+ _OBJC_METACLASS_$_MSDKPeerDemoAXSettings
+ _OBJC_METACLASS_$_MSDKPeerDemoIPDStatus
+ __OBJC_$_CLASS_METHODS_MSDKPeerDemoAXSettings
+ __OBJC_$_CLASS_METHODS_MSDKPeerDemoIPDStatus
+ __OBJC_$_CLASS_PROP_LIST_MSDKPeerDemoAXSettings
+ __OBJC_$_CLASS_PROP_LIST_MSDKPeerDemoIPDStatus
+ __OBJC_$_INSTANCE_METHODS_MSDKPeerDemoAXSettings
+ __OBJC_$_INSTANCE_METHODS_MSDKPeerDemoIPDStatus
+ __OBJC_$_INSTANCE_VARIABLES_MSDKPeerDemoAXSettings
+ __OBJC_$_INSTANCE_VARIABLES_MSDKPeerDemoIPDStatus
+ __OBJC_$_PROP_LIST_MSDKPeerDemoAXSettings
+ __OBJC_$_PROP_LIST_MSDKPeerDemoIPDStatus
+ __OBJC_CLASS_PROTOCOLS_$_MSDKPeerDemoAXSettings
+ __OBJC_CLASS_PROTOCOLS_$_MSDKPeerDemoIPDStatus
+ __OBJC_CLASS_RO_$_MSDKPeerDemoAXSettings
+ __OBJC_CLASS_RO_$_MSDKPeerDemoIPDStatus
+ __OBJC_METACLASS_RO_$_MSDKPeerDemoAXSettings
+ __OBJC_METACLASS_RO_$_MSDKPeerDemoIPDStatus
+ ___56-[MSDKPeerDemoDeviceManager _setUpXPCConnectionIfNeeded]_block_invoke.138
+ ___56-[MSDKPeerDemoDeviceManager _setUpXPCConnectionIfNeeded]_block_invoke.138.cold.1
+ ___66-[MSDKPeerDemoDeviceManager readIPDStatusFromPeer:withCompletion:]_block_invoke
+ ___66-[MSDKPeerDemoDeviceManager readIPDStatusFromPeer:withCompletion:]_block_invoke_2
+ ___69-[MSDKPeerDemoDeviceManager queryIPDResetStageOnPeer:withCompletion:]_block_invoke
+ ___72-[MSDKPeerDemoDeviceManager skipAutoIPDAdjustmentOnPeer:withCompletion:]_block_invoke
+ ___72-[MSDKPeerDemoDeviceManager skipAutoIPDAdjustmentOnPeer:withCompletion:]_block_invoke_2
+ ___75-[MSDKPeerDemoDeviceManager getAccessibiltiySettingsOnPeer:withCompletion:]_block_invoke
+ ___77-[MSDKPeerDemoDeviceManager initiateIPDResetOnPeer:targetIPD:withCompletion:]_block_invoke
+ ___87-[MSDKPeerDemoDeviceManager setAccessibiltiySettingsOnPeer:newSettings:withCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e43_v24?0"MSDKPeerDemoIPDStatus"8"NSError"16ls32l8
+ _kMSDKPeerDemoAXSettingsPropertyGazeAccessibility
+ _kMSDKPeerDemoAXSettingsPropertyPointerControl
+ _kMSDKPeerDemoAXSettingsPropertyStaticFoveation
+ _kMSDKPeerDemoIPDStatusPropertyClipOnState
+ _kMSDKPeerDemoIPDStatusPropertyCurrentIPD
+ _kMSDKPeerDemoIPDStatusPropertyTargetIPD
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$clipOnState
+ _objc_msgSend$currentIPD
+ _objc_msgSend$gazeAccessibility
+ _objc_msgSend$getAccessibiltiySettingsOnPeer:withCompletion:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initiateIPDResetOnPeer:targetIPD:withCompletion:
+ _objc_msgSend$pointerControl
+ _objc_msgSend$queryIPDResetStageOnPeer:withCompletion:
+ _objc_msgSend$readIPDStatusFromPeer:withCompletion:
+ _objc_msgSend$setAccessibiltiySettingsOnPeer:newSettings:withCompletion:
+ _objc_msgSend$setClipOnState:
+ _objc_msgSend$setCurrentIPD:
+ _objc_msgSend$setGazeAccessibility:
+ _objc_msgSend$setPointerControl:
+ _objc_msgSend$setStaticFoveation:
+ _objc_msgSend$setTargetIPD:
+ _objc_msgSend$skipAutoIPDAdjustmentFromPeer:withCompletion:
+ _objc_msgSend$staticFoveation
+ _objc_msgSend$targetIPD
+ _objc_msgSend$unsignedIntegerValue
- GCC_except_table76
- ___56-[MSDKPeerDemoDeviceManager _setUpXPCConnectionIfNeeded]_block_invoke.120
- ___56-[MSDKPeerDemoDeviceManager _setUpXPCConnectionIfNeeded]_block_invoke.120.cold.1
CStrings:
+ "-[MSDKPeerDemoDeviceManager getAccessibiltiySettingsOnPeer:withCompletion:]"
+ "-[MSDKPeerDemoDeviceManager initiateIPDResetOnPeer:targetIPD:withCompletion:]"
+ "-[MSDKPeerDemoDeviceManager queryIPDResetStageOnPeer:withCompletion:]"
+ "-[MSDKPeerDemoDeviceManager readIPDStatusFromPeer:withCompletion:]"
+ "-[MSDKPeerDemoDeviceManager setAccessibiltiySettingsOnPeer:newSettings:withCompletion:]"
+ "-[MSDKPeerDemoDeviceManager skipAutoIPDAdjustmentOnPeer:withCompletion:]"
+ "/var/MobileAsset"
+ "<%@[%p]: PointerControl=%lu GazeAccessibility=%lu StaticFoveation=%lu>"
+ "<%@[%p]: TaregtIPD=%f CurrentIPD=%f ClipOnState=%lu>"
+ "@40@0:8d16d24Q32"
+ "AssetsV2/com_apple_MobileAsset_SystemEnvironmentAsset"
+ "ClipOnState"
+ "CurrentIPD"
+ "DemoMode"
+ "MSDKPeerDemoAXSettings"
+ "MSDKPeerDemoIPDStatus"
+ "MobileAssetDomain"
+ "PressDemoMode"
+ "Q"
+ "TQ,N,V_clipOnState"
+ "TQ,N,V_gazeAccessibility"
+ "TQ,N,V_pointerControl"
+ "TQ,N,V_staticFoveation"
+ "TargetIPD"
+ "Td,N,V_currentIPD"
+ "Td,N,V_targetIPD"
+ "_clipOnState"
+ "_currentIPD"
+ "_gazeAccessibility"
+ "_isMuseBuddyDemoModeEnabled"
+ "_isPressDemoModeEnabled"
+ "_pointerControl"
+ "_staticFoveation"
+ "_targetIPD"
+ "boolForKey:"
+ "clipOnState"
+ "com.apple.musebuddy"
+ "currentIPD"
+ "gazeAccessibility"
+ "getAccessibiltiySettingsOnPeer:withCompletion:"
+ "initWithSuiteName:"
+ "initWithTargetIPD:currentIPD:clipOnState:"
+ "initiateIPDResetOnPeer:targetIPD:withCompletion:"
+ "pointerControl"
+ "queryIPDResetStageOnPeer:withCompletion:"
+ "readIPDStatusFromPeer:withCompletion:"
+ "setAccessibiltiySettingsOnPeer:newSettings:withCompletion:"
+ "setClipOnState:"
+ "setCurrentIPD:"
+ "setGazeAccessibility:"
+ "setPointerControl:"
+ "setStaticFoveation:"
+ "setTargetIPD:"
+ "skipAutoIPDAdjustmentFromPeer:withCompletion:"
+ "skipAutoIPDAdjustmentOnPeer:withCompletion:"
+ "staticFoveation"
+ "targetIPD"
+ "unsignedIntegerValue"
+ "v24@0:8Q16"
+ "v24@0:8d16"
+ "v24@?0@\"MSDKPeerDemoIPDStatus\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"MSDKPeerDemoAXSettings\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"MSDKPeerDemoIPDStatus\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"MSDKPeerDemoAXSettings\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16d24@?<v@?d@\"NSError\">32"
+ "v40@0:8@16d24@?32"

```
