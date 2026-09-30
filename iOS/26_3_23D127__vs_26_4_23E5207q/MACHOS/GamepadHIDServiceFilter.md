## GamepadHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/GamepadHIDServiceFilter.plugin/GamepadHIDServiceFilter`

```diff

-13.3.1.0.0
-  __TEXT.__text: 0x3658
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0x540
-  __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x574
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__cstring: 0x175
-  __TEXT.__oslogstring: 0x4f4
-  __TEXT.__objc_methname: 0xc0c
-  __TEXT.__objc_classname: 0x280
-  __TEXT.__objc_methtype: 0xbbc
-  __TEXT.__unwind_info: 0x1e0
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x220
-  __DATA_CONST.__cfstring: 0xe0
+13.4.8.0.0
+  __TEXT.__text: 0x2a00
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__objc_methlist: 0x428
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x394
+  __TEXT.__oslogstring: 0x4da
+  __TEXT.__objc_methname: 0x800
+  __TEXT.__cstring: 0x83
+  __TEXT.__objc_classname: 0x96
+  __TEXT.__objc_methtype: 0xa6e
+  __TEXT.__unwind_info: 0x1b8
+  __DATA_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x770
-  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_const: 0x4c8
+  __DATA.__objc_selrefs: 0x2a8
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x720
-  __DATA.__bss: 0xa9
+  __DATA.__data: 0x1e0
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
+  - /System/Library/PrivateFrameworks/GameControllerIO.framework/GameControllerIO
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 026E4EF1-EA6B-3FA9-98A3-5194474EA7E7
-  Functions: 112
-  Symbols:   97
-  CStrings:  280
+  UUID: 623C7D84-9A6D-3A24-B477-98BA7E30D641
+  Functions: 68
+  Symbols:   86
+  CStrings:  203
 
Symbols:
+ _GCDriverClientInterface
+ _GCDriverServerInterface
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
- _GCGenericDeviceDriverConfigurationServiceClientInterface
- _GCGenericDeviceDriverConfigurationServiceServerInterface
- _OBJC_CLASS_$_NSMutableString
- _OBJC_CLASS_$_NSString
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_CLASS_$_NSXPCInterface
- __os_log_default
- _hexStringFromByteArray
- _isPartnerSupportEnabled
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x23
- _objc_retain_x8
- _os_variant_has_internal_diagnostics
CStrings:
- ""
- "%02x%@"
- ":"
- "GCAdaptiveTriggersServiceClientInterface"
- "GCAdaptiveTriggersServiceServerInterface"
- "GCBatteryServiceClientInterface"
- "GCBatteryServiceServerInterface"
- "GCGameIntentServiceClientInterface"
- "GCIdleServiceClientInterface"
- "GCIdleServiceServerInterface"
- "GCLightServiceClientInterface"
- "GCLightServiceServerInterface"
- "GCMotionServiceClientInterface"
- "GCMotionServiceServerInterface"
- "GCNintendoJoyConFusionGestureServiceClientInterface"
- "GCNintendoJoyConFusionGestureServiceServerInterface"
- "GCPartnersEnable"
- "GameController"
- "Partners mode enabled? %d"
- "_GCDriverServerInterface"
- "analytics"
- "appendString:"
- "boolForKey:"
- "com.apple.GameController"
- "com.apple.GameController.Daemon"
- "com.apple.GameController.Haptics"
- "com.apple.GameController.Settings"
- "com.apple.gamecontroller"
- "com.apple.runtime-issues"
- "default"
- "homeButtonLongPressGesture:"
- "initWithSuiteName:"
- "interfaceWithProtocol:"
- "monitor"
- "readAdaptiveTriggerStatusWithReply:"
- "readBatteryWithReply:"
- "readLightWithReply:"
- "readSensorsActiveWithReply:"
- "requestIdleDisconnect:"
- "setAdaptiveTriggerModeFeedbackWithResistiveStrengths:forIndex:"
- "setAdaptiveTriggerModeFeedbackWithStartPosition:resistiveStrength:forIndex:"
- "setAdaptiveTriggerModeOffForIndex:"
- "setAdaptiveTriggerModeSlopeFeedbackWithStartPosition:endPosition:startStrength:endStrength:forIndex:"
- "setAdaptiveTriggerModeVibrationWithAmplitudes:frequency:forIndex:"
- "setAdaptiveTriggerModeVibrationWithStartPosition:amplitude:frequency:forIndex:"
- "setAdaptiveTriggerModeWeaponWithStartPosition:endPosition:resistiveStrength:forIndex:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithString:"
- "updateAdaptiveTriggerStatusWithLeftMode:leftStatus:leftArmPosition:rightMode:rightStatus:rightArmPosition:"
- "updateBattery:isCharging:"
- "updateLightWithRed:green:blue:"
- "updateSensorsActive:"
- "uppercaseString"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?CB>16"
- "v24@0:8@?<v@?CCCCCC>16"
- "v24@0:8@?<v@?fff>16"
- "v24@0:8C16B20"
- "v28@0:8@\"NSArray\"16i24"
- "v28@0:8@16i24"
- "v28@0:8I16Q20"
- "v28@0:8f16f20f24"
- "v28@0:8f16f20i24"
- "v32@0:8@\"NSArray\"16f24i28"
- "v32@0:8@16f24i28"
- "v32@0:8f16f20f24i28"
- "v36@0:8f16f20f24f28i32"
- "v40@0:8C16C20C24C28C32C36"

```
